---
otero_id: 16421
otero_key: "JQ47RZ9V"
title: "Service Agreement Trifecta: Backup Resources, Price and Penalty in the Availability-Aware Cloud"
authors: "Shuai Yuan; Sanjukta Das; R. Ramesh; Chunming Qiao"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0755"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [198.255.74.30] On: 25 April 2025, At: 23:47 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/JQ47RZ9V/fulltext/images/400df132357f081aa07f80fdb3f7bd05d08bd4fcb4e8b886b90832072d42a47b.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Service Agreement Trifecta: Backup Resources, Price and Penalty in the Availability-Aware Cloud

Shuai Yuan, Sanjukta Das, R. Ramesh, Chunming Qiao

To cite this article:

Shuai Yuan, Sanjukta Das, R. Ramesh, Chunming Qiao (2018) Service Agreement Trifecta: Backup Resources, Price and Penalty in the Availability-Aware Cloud. Information Systems Research 29(4):947-964. https://doi.org/10.1287/ isre.2017.0755

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Service Agreement Trifecta: Backup Resources, Price and Penalty in the Availability-Aware Cloud

Shuai Yuan,<sup>a</sup> Sanjukta Das,<sup>b</sup> R. Ramesh,<sup>b</sup> Chunming Qiao<sup>c</sup>

<sup>a</sup> Department of Finance, Operations, and Information Systems, Goodman School of Business, Brock University, St. Catharines, Ontario L2S 3A1, Canada; <sup>b</sup> Department of Management Science and Systems, School of Management, University at Bufalo, State University of New York, Bufalo, New York 14260; <sup>c</sup> Department of Computer Science and Engineering, School of Engineering and Applied Sciences, University at Bufalo, State University of New York, Bufalo, New York 14260

Contact: shuai.yuan@brocku.ca (SY); sdsmith4@bufalo.edu, http://orcid.org/0000-0001-7963-3254 (SD); rramesh@bufalo.edu (RR); qiao@computer.org (CQ)

Received: May 22, 2015 Revised: September 1, 2016; June 8, 2017; October 12, 2017 Accepted: October 12, 2017 Published Online in Articles in Advance: June 29, 2018

https://doi.org/10.1287/isre.2017.0755

Copyright: © 2018 INFORMS

Abstract. Service Level Agreements (SLA) for cloud services entail complex trade-ofs between interrelated variables such as price, penalty, and service availability (uptime) guarantee, with resource management strategies afecting fulfillment of the SLA. In this study, we address three key components of the SLA-based cloud resource management and pricing problem, from the service-provider’s perspective: (1) availability-aware backup resource provisioning; (2) price-penalty schedule determination; and (3) penalty-deferred pricing over two periods. Using the convexity of the provider’s expected total cost over the number of backup resources, we present a dichotomous search algorithm to derive the total cost minimizing number of backup resources for a given level of SLA-specified service availability guarantee. Next, we derive closed-form solutions for the lower bound of the feasible price range, yielding a schedule of breakeven price-penalty combinations, which establishes the baseline required in the economic modeling of the service contracts and related negotiation processes, and may also elicit client preference information. We then model a two-period pricing problem specifically designed to incentivize penalty deferrals in the event of an SLA violation. Detailed experimental studies of the proposed models have been carried out using real-world datacenter log data. The computational study validates the convexity of the probability density function of SLA violations over the number of backup resources. The results demonstrate significant interaction efects between the SLA parameters (price, penalty rate, and provisioning cost) and the backup resource provisioning decisions made by the provider, leading to key practical managerial implications for SLA design and resource deployment in the availability-aware cloud.

History: Vĳay Mookerjee, Senior Editor; Subodha Kumar, Associate Editor. Funding: This work is supported in part by a Google Faculty Research Award [2011\_R2\_549] and a National Science Foundation (NSF) grant [CSR-1409809]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0755.

Keywords: cloud computing • resource management • pricing • service level agreement

## 1. Introduction

Cloud computing deemphasizes the need for companies to maintain significant in-house infrastructure. Server instances, also known as virtual machines (VMs), with various computing and storage capabilities (i.e., diferent combinations of CPU, memory, storage, and networking), are commonly ofered by cloud computing service providers such as Amazon Web Services (AWS), Google, Microsoft, Rackspace, and Salesforce. The clients, ranging from individuals and small institutions to large firms, usually rent and pay only for a set of VMs through a usage-based (pay-asyou-go) posted pricing model. Each of these VMs is mapped onto a physical server within a cloud datacenter. A cloud service provider and a client are typically bound by a Service Level Agreement (SLA) articulating various contract constructs, such as contract duration, service window, price, penalty, and service availability.

An SLA between a cloud service provider and its client is as follows: The client requires n VMs to be available over a specified service window T, at an uptime guarantee of α of the duration T. Such requirements can be client-specified or part of a schedule of service levels formally ofered by a provider. A unit penalty π is paid by the provider if the promised service level is not met within the service window. Major cloud service providers presently set a high standard in this regard. The latest ITIC 2017–2018 survey data found that 80% of respondents now consider 99.99% to be the minimum acceptable levels of availability for their main line of business servers (ITIC 2017). Although virtualized resources at diferent levels (computation, storage, networking) have been implemented to ensure high availability, the availability issue of cloud service is still one of the many obstacles to wider adoption of cloud computing (Armbrust et al. 2010). Cloud datacenters are susceptible to diferent types of failures ranging from frequent, small scale failures (such as disk failures) to less frequent, largescale failures (such as power distribution unit failures) (Dean 2009, Gill et al. 2011, Levy 2011). Failures at the physical infrastructure level inevitably render the mapped VMs unavailable due to loss of connectivity, software bugs, human errors, etc. According to a recent Emerson Report (Emerson 2011), on average, a complete unplanned outage (power, human error, etc.) in a datacenter typically lasts about 134 minutes; collectively, these outages result in \$426 billion in losses worldwide. Driven by the need to comply with the SLA, a provider typically allocates a set of k additional VMs as backup to the client as best-efort sustenance of the uptime guarantee. Thus, downtime will result only if at least k <sup>+</sup> 1 VMs concurrently fail.

The interactions between the various SLA constructs are influenced by the availability guarantee. As the uptime guarantee in an SLA becomes more stringent, the likelihood of violating the SLA also increases, for a given number of deployed resources. Thus, a client demanding higher service levels may need to be charged more since the provider may have to provision more backup resources to improve failure resiliency such that the cost to the provider rises as backups increase, in addition to the potential waste of resources. On the other hand, a client willing to accept a lower penalty rate may be ofered a relatively lower price, as the provider uses fewer backup resources to mitigate the penalty risk. Given the interdependency of the SLA constructs, we address three closely related cloud resource management and pricing problems in this research: (1) availability-aware backup resource provisioning; (2) price-penalty schedule determination; (3) penaltydeferred pricing over two periods.

This paper is organized as follows: Section 2 highlights our research contribution. Section 3 presents the related work. Section 4 presents the algorithm for deriving the optimal number of backup resources that minimize the expected aggregate of provisioning and penalty costs. In Section 5, we develop a price-penalty schedule for a given client, and then model a twoperiod pricing problem to incentivize penalty deferrals in the event of an SLA violation. Computational analyses have been done in Section 6 to study the impact of various model parameters. We conclude with Section 7.

## 2. Summary of Research Contributions

The theoretical contributions of our work are as follows. With the goal of cost-efectively managing availability-related risks, we jointly consider the inter twined problems of resource allocation and the asso ciated pricing. Our framework deconstructs this prob lem into its logical solvable components, bearing in mind the ability to apply the outcomes in practice. We create a mechanism to customize contract constructs for each client: This is a key consideration given the current heterogeneity in cloud services and client service expectations. Our methodology incorporates learning from historical data that includes the state of the system, in the form of failures and repairs, to inform the provisioning of resource and design of the price-penalty schedule. The outputs of our work can serve as inputs to a negotiated contract in the future, where questions about the formation of the initial ofer are key as it provides the baseline from which a provider would start to negotiate and sets the tone of the subsequent steps, as well as the future success of the contract. Because our work is from the perspective of the service provider, we model the service disruption risk faced by the client as an SLA violation risk faced by the provider, allocating resources and deriving breakeven prices that enable the provider to cost efectively mitigate this risk. As discussed in Section 3, none of the existing work models the availability issue in the cloud resource allocation and pricing process. Our work also contributes to the inventory management literature by accommodating the specific challenges brought on by the increasing need to assure varying levels of service availability across diferent cloud clients, especially with regard to modeling the provisioning of backup resources to minimize costs for the cloud service provider. A key distinction in the product being inventoried in our case from existing modeling is that it is a non-revenue-earning product that nonetheless afects contract profitability. In addition, to our knowledge, the literature has not considered situations wherein the fluctuating demand is a bigger challenge for the provider than it is for the client. This work adds to the extant literature and industrial practices in the domain of cloud computing by modeling the impact of the critical metric of service availability on resource provisioning and price-penalty schedule designing, whose efects are starkly diferent from the more commonly modeled metrics of performance and reliability.

The availability-aware resource provisioning problem arises in satisfying an SLA with four fixed parameters, i.e., service window, service availability required over that window, price, and penalty. The objective is to determine the optimal number of backup resources that minimizes the expected aggregate of provisioning and penalty costs. Our problem is analogous to the newsvendor model when we consider under- and over-provisioning issues based on the trade-of between provisioning cost and expected penalty cost for a given availability requirement, as the newsvendor also faces overage and underage costs if he orders too much or too little. In Section 3, we elaborate on the significant diferences between our work and existing newsvendor problems. We define under-provisioning as the case wherein fewer backup VMs are allocated to save on the provisioning cost, relative to the probability of exposure to penalties due to SLA violation. We define over-provisioning as the case wherein many more backup VMs are unnecessarily allocated to stave of the likelihood of violating the SLA, thereby impacting the profitability of the contract. In most modern cloud service contracts, the client pays only for the VMs demanded, while backup provisioning is determined and controlled by the provider, typically without the client’s knowledge. However, the amount of backup VMs provisioned has key risk implications for the contract. As k is increased for a given SLA, the risk of over-provisioning increases and that of under-provisioning decreases. This manifests in the form of increased expected operating costs and decreased expected penalty costs for the provider. Given a pair of key convexity results, we design an eficient dichotomous search algorithm to determine the optimal number of backup VMs. We empirically validate the convexity of the SLA violation probability over $k ,$ test the efects of key contract parameters such as penalty rate and provisioning cost on $k ,$ and benchmark the dichotomous search algorithm against alternative strategies for backup resource provisioning.

Next, we derive a price-penalty schedule where breakeven prices are derived for various penalty levels. When the penalty is relatively low, the provider allocates fewer backup VMs, thereby enabling him to lower the breakeven price for the VMs. On the other hand, a higher penalty rate will drive the provider to ofset the risk of increased expected penalty costs through additional backup provisioning; this in turn leads the provider to set a higher price for such a contract. The examination of any real-world negotiation process reveals that each party generally has a feasible price interval for the deal to successfully materialize. Note that while the upper bound of this range is driven by competitive forces, the lower bound reflects in-house capabilities, limitations, contractual liabilities, and risk exposures to the revenue. We empirically evaluate the efect of the contract parameters such as penalty and provisioning cost on contract price. A price-penalty schedule is particularly useful for clients who may be unable to precisely articulate their desired penalty level up front. This schedule also serves as an important tool for the provider in the following two aspects: (1) SLA negotiation is a process of joint, but typically noncoordinated, decision making between clients and providers to resolve conflicting objectives. In cloud environments, clients and providers have their respective cost-benefit models for negotiation and decisionmaking purposes (Siebenhaar et al. 2012, Dastjerdi and Buyya 2015), which are typically privately held information on either side of the negotiation (Oliver 1996). The determination of the lower bound of the feasible range of prices is therefore crucial during the more exploratory contract creation stage of the contract life cycle as it helps define the initial ofer and thus shape future counterofers for both parties, given the nature of the client’s request and the service provider’s capability. (2) Making multiple ofers simultaneously is a well established tactic suggested by negotiation practitioners to help discover the underlying interests of the client; the client is thereby prompted to divulge her relative preferences by accepting one particular ofer, perhaps revealing a hitherto undisclosed preference (Malhotra and Bazerman 2007). As the provider, in our case, earns the same return across all combinations in this schedule, the price-penalty schedule provides him with an eficient mechanism to elicit client preference information.

Despite optimal resource allocation in concordance with the price-penalty schedule design, it is still possible that the uptime guarantee will remain unmet at the end of a service window. As a result, the provider must now pay the SLA-specified penalty. We model this specific instance where the contract fails to execute as expected, i.e., the uptime guarantee is not satisfied within a given service window. In most pay-as-yougo cloud platforms such as AWS, penalty payments take the form of “service credits” that are applied toward the next billing cycle. This strategy reflects the provider’s desire to defer any monetary penalty payments. At this time, the onus is largely on the client to report outages and the client has no choice as to deferral of the penalty payment. Note that the issue of availability of cloud services and applications is a primary concern among information technology (IT) professionals as stated in a 2012 global survey of more than 1,300 IT professionals aimed at better understanding the top priorities and challenges when moving applications and services to the cloud (Cisco 2012). Given this concern, placing additional hurdles in the way of reporting outages and choice-less deferred penalty payment practices further exacerbates cloud adoption woes. On the other hand, the cloud datacenter provider seeks to secure his revenue stream and minimize costs, which includes penalty payments. Balancing these two trade-ofs, we therefore model a scenario where the client is given a choice to collect the penalty payment at the end of the service window or defer it to the next period. The provider incentivizes the deferral by charging a lower price for the next period. This serves two purposes: (1) It locks the client in for another period, and (2) It ofers the provider an opportunity to make up for the service shortfall as a risk-hedging method and possibly avoid having to pay the penalty. We analytically determine the bounds on the price where the provider can profitably incentivize the client to defer the penalty payment. Finally, we empirically evaluate the impact of penalizable downtime on pricing in future periods using a two-period setting.

Figure 1. An Overview of the Availability-Aware SLA Framework with Integrated Modules  
![](/api/attachments/JQ47RZ9V/fulltext/images/6906f5aa895d707043d9776aebf72d8e8cba16ef7216cba7fe3d042be34cd4a9.jpg)

The proposed availability-aware SLA framework consists of five modules as shown in Figure 1. Details of the modules are provided in the online appendix.

## 3. Related Work

The single-period problem, also known as the newsvendor problem, is one of the classical problems in the literature on inventory management (Arrow et al. 1951). Many extensions of the single-period problem have addressed a wide variety of realistic issues by considering how changes in key parametric assumptions might moderate the set of results, e.g., modeling on customer demand, supplier pricing policies, and buyer risk profile. Customer demand is modeled as a function of price (Whitin 1955, Mills 1959), and influenced by marketing efort (Gerchak and Mossman 1992, Kraiselburd et al. 2004) and stocking quantity (Baker and Urban 1988, Urban and Baker 1997, Urban 2002). Also, instead of a fixed supplier price per unit as the standard assumption, Qin et al. (2011) summarized the impact of diferent supplier quantity discounting schemes (i.e., linear quantity discount, all-units quantity discount, and incremental units quantity discount) on the inventory quantity decision. The basic model also specifies that the buyer is risk neutral. Studies such as (Eeckhoudt et al. 1995, Arcelus et al. 2006) focus on buyers: Those who are risk averse and/or risk takers would moderate the final decision on order quantity. However, the existing literature has not considered situations wherein the fluctuating demand is a bigger challenge for the provider than it is for the client due to pay-as-you-go cloud pricing policy and rapid elasticity of the cloud service. To our knowledge, existing literature has also not modeled the provisioning of non-revenue-generating resources that are critical to assuring service level metrics such as availability.

Much of the pertinent work in the contract design literature has focused on the balance between IT business value and underlying risks, mostly to address the uncertain demands of the clients. Dey et al. (2010) develops a contract-theoretic model that incorporates several closely related factors such as the quality of the developed system, timeliness of delivery, payment, and cost to analyze the design of an outsourcing software development contract. Wu et al. (2012) analytically and experimentally investigates how firms can best capture IT project value by deriving the optimal contract that specifies vendor compensation and the optimal stage length. Das et al. (2011) address the risk of demand uncertainties faced by a storage grid provider, specifically the downside risk associated with capacity overbuilding, through revenue-maximizing spot prices and the use of financial instruments such as forward contracts. Kaufman and Sougstad (2008) fundamentally addresses the trade-of between profitability of IT service contract and service level risk rising from user demand uncertainty by applying Value-at-Risk (VaR) theory and methods, while defining service level using two distinct levels, high and low. Yang et al. (2009) model the supplier’s reliability as asymmetric information and analyze its impact on the manufacturer’s risk-management strategies. To our knowledge, none of the studies consider the availability issue as part of the pricing process and its impact on IT service performance. Our work adds to the domain by developing an availability-aware decision-making framework for SLA design and laying a foundation for further study in the area of cloud resource management. We also model a two-period pricing problem specifically designed to incentivize penalty deferrals in the event of an SLA violation. This contributes a risk-hedging tool that can be used by the provider to manage contractual relationships across multiple time windows, given the likelihood of SLA violations.

Optimal resource allocation vis-à-vis SLA/quality of service (QoS) requirements is another related area. Most existing information systems (IS) literature performs cost-efectiveness analysis and develops policies to meet demand uncertainty and satisfy service performance. Wang et al. (2008) addresses the problem of autonomic resource management in a shared data center to meet diferent service quality targets at minimum operational cost. Du et al. (2014) proposes provisioning policy and pricing algorithms to cost-efectively manage resources by strategically allocating digital media content across multiple tiers to avoid overcapacitating high-performance tiered infrastructure platforms. Liu et al. (2010) models and identifies a resource allocation policy associated with providing personalization services for content-delivery websites to maximize revenues, modeling the tradeof between more personalized content to the end user and the negative externalities of higher waiting costs for other requests. Sen et al. (2010) explores the value of sharing demand-related information in reducing conflict between organizations in IT service outsourcing. They design a dynamic resource adaptation mechanism where resource levels are periodically adjusted according to a demand forecast to achieve a steady level of service. In addition, Goudarzi et al. (2012) studies the SLA-based resource provision problem to minimize the total energy cost by efective VM placement. Wu et al. (2011) proposes algorithms to reduce infrastructure VM cost and minimize SLA violations defined by customer QoS requirements, i.e., response time in the context of Software as a Service through efective platform layer resource allocation strategies. Each of these papers take into account various QoS requirements, with some focusing on the overarching goal of resource minimization. They are not, however, particularly amenable to the specific resource allocation challenges inherent within contracts for IT services, such as cloud services, which are increasingly bound by strict SLAs stipulating various availability guarantees. To our knowledge, our work is the first to create an integrated modeling framework for resource allocation and pricing, while managing the risks and costs associated with a critical SLA-specified condition, in our case, the availability or uptime guarantee.

## 4. The Availability-Aware Backup Provisioning Model

We first introduce some assumptions and notations needed in the proposed algorithms. Without loss of generality and for the sake of tractability, we assume that the provider faces a single type of failure and a 1:1 mapping of virtual to physical servers for a given client in the datacenter since uptime guarantees are clientspecific. Failure types may be broadly classified according to the independence of the failure cases. We focus solely on independent failure types (e.g., disk failures), as the underlying downtime distribution is precisely derived for this type. This was reinforced by our advice from Google (a funding source for our research) which stress the vast prevalence of independent disk failures as opposed to non-independent failures. Furthermore, while the same server may host multiple VMs, the VMs for a given client may be spread across many physical server racks to ease the SLA violation risk from single points of failure.

An SLA codifies the relationship between the provider and a given client. Negotiated SLAs may be required in cases where the service provisioning is tailored for each client. In some cases, clients with special needs (for service availability and other QoS attributes) cannot be accommodated by a one-size-fitsall SLA framework, thus necessitating an SLA specifically customized for a client. Service provisioning for such an SLA is vital in managing resources for the provider (Rajavel and Thangarathinam 2015). The service provider, in our model, allocates k backup VMs to ofer some failure resiliency to the n VMs demanded. When any of the n VMs fails, one of the k backup VMs is used as a replacement. Du et al. (2015) derives the downtime distribution function under three distinct checkpointing strategies that dictate the backup and replacement process. Based on the specific checkpointing strategy used, the corresponding downtime probability density function (pdf) would serve as inputs to our models. Table 1 lists additional notations used in this paper along with brief definitions.

Table 1. Notations

<table><tr><td> $\alpha$ :</td><td>Uptime guarantee specified in the SLA,  $0 \leq \alpha \leq 1$ </td></tr><tr><td> $T$ :</td><td>Service window over which the uptime guarantee has to be fulfilled (e.g., if SLA specifies 99% availability in each week, then service window is one week)</td></tr><tr><td> $n$ :</td><td>Number of VMs the client demands</td></tr><tr><td> $p$ :</td><td>Price for each of the  $n$  VMs demanded per unit of time</td></tr><tr><td> $\pi$ :</td><td>Penalty per unit of time as a result of SLA violation</td></tr><tr><td> $\tau$ :</td><td>Accumulated downtime within one service window  $T$ </td></tr><tr><td> $v(\tau)$ :</td><td>Probability density function of the total downtime within a service window  $T$  for an  $(n,k)$  VM configuration, derived by the algorithm specified in Du et al. (2015)</td></tr><tr><td> $h$ :</td><td>Provisioning cost per VM per unit of time</td></tr></table>

While the provider can reduce the likelihood of SLA violation by providing more backup VMs, this reduction is a trade-of against a higher provisioning cost, with the client paying only for the n VMs demanded. Therefore the provider must determine the optimal number of backup VMs such that his expected total cost is minimized, where expected total cost aggregates the provisioning cost and the expected penalty. Thus, we have the following expected total cost with k backups denoted as $Q _ { k }$

$$
Q _ {k} = h k T + \pi \int_ {(1 - \alpha) T} ^ {T} v (\tau) (\tau - (1 - \alpha) T) d \tau .\tag{1}
$$

To derive the closed form solution to the optimal number of backup VMs from Equation (1), we need a diferentiable functional form of the downtime distribution v<sup>(</sup>τ<sup>)</sup>. We empirically derived the downtime pdf of $( n , k )$ configurations from real-world server log data collected from the Center for Computational Research (CCR) at SUNY Bufalo using the algorithm in Du et al. (2015). We then extensively tested the derived downtime distribution data for fit with a range of distributions including exponential, gamma, Weibull, lognormal, and log-logistic distributions using the Chi-Square Goodness of Fit Test. None of these fits were satisfactory. We provide experimental details of this exercise in Section 6.

Hence, we carried out a piecewise linear approximation of the derived downtime distribution data along the lines of Wang (2012). Because most piecewise linear approximation algorithms rely extensively on some data-dependent threshold-based strategies, there is a trade-of between approximation accuracy and compression rate, which the user typically resolves via a trial and error process. Instead, we use a two-stage top-down segmentation approach to first recursively decompose data into non-overlapping intervals until all partitioned linear segments satisfy a data-independent threshold r. The threshold r is used to control the approximation accuracy, with $0 \leq r \leq 1$ . The higher the value of $r ,$ the greater the number of partitioned line segments and the better the fit of the distribution to the linearized segments. The goodness of the linear approximation for each partitioned segment x is measured using a coeficient of determination $r _ { x } ,$ computed as $r _ { x } = 1 - S S _ { \mathrm { e r r } } / S S _ { \mathrm { t o t } } ,$ where ${ \sf S S } _ { \mathrm { e r r } }$ denotes the sum of squared prediction errors and ${ \mathrm { S S } } _ { \mathrm { t o t } }$ denotes the total sum of squares. We adapt this approach to derive each partitioned segment of downtime distribution during the approximation of v<sup>(</sup>τ<sup>)</sup>. The initial $v ( \tau )$ is considered as a single segment, denoted by $( \tau _ { 1 } , v ( \tau _ { 1 } ) ) , ( \tau _ { 2 } , v ( \tau _ { 2 } ) ) , \ldots ,$ $( \tau _ { i } , v ( \tau _ { i } ) ) , \ldots , ( \tau _ { p } , v ( \tau _ { p } ) ) , 1 { \leq } i { \leq } p .$ , where $( \tau _ { 1 } , v ( \tau _ { 1 } ) )$ and $( \tau _ { p } , v ( \tau _ { p } ) )$ are the two boundaries of the distribution. In our approximation, we set $\begin{array} { r } { { \mathrm { S } } { \mathrm { S } } _ { \mathrm { t o t } } { = } { \sum _ { i = 1 } ^ { p } } ( v ( \tau _ { i } ) { - } \overline { { v ( \tau ) } } ) ^ { { 2 } } } \end{array}$ where $\overline { { v ( \tau ) } }$ is the mean value of $( v ( \tau _ { 1 } ) , v ( \tau _ { 2 } ) , \ldots , v ( \tau _ { i } )$ $\textstyle \dots , v ( \tau _ { p } ) )$ . We also set $\begin{array} { r } { { \mathsf { S } } { \mathsf { S } } _ { \mathrm { e r r } } { = } \sum _ { i = 1 } ^ { p } ( v ( \tau _ { i } ) { - } l _ { i } ) ^ { 2 } } \end{array}$ , where $l _ { i } =$ $v ( \tau _ { 1 } ) + \dot { ( } v ( \tau _ { p } ) - v ( \tau _ { 1 } ) ) ( ( \tau _ { i } - \tau _ { 1 } ) / ( \tau _ { p } - \tau _ { 1 } ) )$ is the ith value of the interpolation line that connects $( \tau _ { 1 } , v ( \tau _ { 1 } ) )$ and $( \tau _ { p } , v ( \tau _ { p } ) )$ . The partition on the downtime distribution continues until $r _ { x }$ in each segment x satisfies the condition $r _ { x } \ge r .$

Finally, the linear approximation is fine-tuned using least-squares linear regression to reduce the approximation error in the final iteration. We present our adaptation as the Piecewise Linear Approximation of Downtime algorithm in Figure 2. In Section $^ { 6 , }$ we study how our results are afected by the approximation accuracy level. This gives us an understanding of the accuracy level that would sufice for the datacenter provider. Next, we formally define and derive the closed form expressions for the expected penalizable downtime, which is a key construct in the optimal backup resource provisioning algorithm.

## 4.1. Expected Penalizable Downtime

We define expected penalizable downtime as the amount of downtime accumulated within the service window T in excess of the downtime allowable under the SLA-specified uptime guarantee, which is denoted by $\begin{array} { r } { \int _ { ( 1 - \alpha ) T } ^ { T } \dot { v ( \tau ) } ( \tau - ( 1 - \alpha ) T ) } \end{array}$ dτ. Suppose that the downtime distribution is partitioned into m general non-overlapping segments according to the piecewise

## Figure 2. Piecewise Linear Approximation Algorithm of Downtime

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs:
Downtime distribution data set  $v(\tau)$ , approximation accuracy r, number of segments m = 1.
Step 1:
Calculate  $r_{x} = 1 - \frac{SS_{err}}{SS_{tot}}$ , for each  $x = 1, \ldots, m$ .
Step 2:
If  $\min r_{x} \geq r$  then go to Step 3;
Else partition the segment with the minimum  $r_{x}$  into two parts;
 $m = m + 1;$ 
Go to Step 1.
Step 3:
Perform least-squares linear regression on each of the m segments;
Derive the intersection points of the regression lines derived for each segment;
Connect the intersection points.
Return:
Piecewise linear function of  $v(\tau)$  with m segments
</div>

linear approximation algorithm as follows:

$$
v (\tau) = \left\{ \begin{array}{l l} a _ {0} \tau + b _ {0}, & 0 \leq \tau \leq \gamma_ {0}, \\ a _ {1} \tau + b _ {1}, & \gamma_ {0} \leq \tau \leq \gamma_ {1}, \\ a _ {2} \tau + b _ {2}, & \gamma_ {1} \leq \tau \leq \gamma_ {2}, \\ & . \\ a _ {i} \tau + b _ {i}, & \gamma_ {i - 1} \leq \tau \leq \gamma_ {i}, \\ & . \\ a _ {m - 1} \tau + b _ {m - 1}, & \gamma_ {m - 2} \leq \tau \leq T, \\ & \text {where} 1 \leq i \leq m - 1   \text {and} i   \text {is integer}. \end{array} \right.
$$

We derive the expected penalizable downtime in closed form by first locating the segment that contains the lower limit of its integral, $\mathrm { i . e . , } ( \bar { 1 } - \alpha ) T$ . The closed form expression depends on the specific segment that contains the lower limit. We derive closed form expressions for three general cases that cover all possibilities of the lower limit location of the expected penalizable downtime. The online appendix provides the complete derivation and exposition of the three cases. A simple inspection of the lower limit in the integral would reveal the appropriate closed form expression to be used in the backup resource provisioning algorithm described in Section 4.2.

## 4.2. Optimal Backup Provisioning Algorithm

We first establish the convexity of the expected penalizable downtime and the expected total cost over the number of backup resources provisioned k in the following lemmas. We begin by assuming that the probability of SLA violation $\begin{array} { r } { \int _ { ( 1 - \alpha ) T } ^ { T } v ( \tau ) d \tau } \end{array}$ is decreasing and convex in k which is empirically validated in Section 6.2. We present the following lemmas:

Lemma 1. Assuming the probability of SLA violation is decreasing and convex in $k ,$ the expected penalizable downtime is decreasing and convex in $k .$

Proof. Let $\tau _ { 0 } = ( 1 - \alpha ) T , k _ { 1 } < k _ { 2 }$ . We get $\begin{array} { r } { \int _ { \tau _ { 0 } } ^ { T } v ( \tau , k _ { 1 } ) d \tau > } \end{array}$ $\begin{array} { r } { \int _ { \tau _ { 0 } } ^ { T } v ( \tau , k _ { 2 } ) d \tau } \end{array}$ from our assumption. Since $\tau - \tau _ { 0 } > 0$ when $\tau \in ( \tau _ { 0 } , T )$ , we get the following inequality:

$$
\int_ {\tau_ {0}} ^ {T} v (\tau , k _ {1}) (\tau - \tau_ {0}) d \tau > \int_ {\tau_ {0}} ^ {T} v (\tau , k _ {2}) (\tau - \tau_ {0}) d \tau .
$$

Therefore,

$$
\begin{array}{l} \int_ {\tau_ {0}} ^ {T} v (\tau , k _ {2}) (\tau - \tau_ {0}) d \tau - \int_ {\tau_ {0}} ^ {T} v (\tau , k _ {1}) (\tau - \tau_ {0}) d \tau <   0, \\ \mathrm{i.e.,} \int_ {\tau_ {0}} ^ {T} v (\tau , k) (\tau - \tau_ {0}) d \tau , \end{array}
$$

is a decreasing function in k.

For any $k _ { 1 } , { \bar { k } } _ { 2 } \in k , k _ { 1 } \neq k _ { 2 } ,$ , according to our assumption, we have

$$
\int_ {\tau_ {0}} ^ {T} v \left(\tau , \frac {1}{2} (k _ {1} + k _ {2})\right) d \tau <   \frac {\int_ {\tau_ {0}} ^ {T} v (\tau , k _ {1}) d \tau + \int_ {\tau_ {0}} ^ {T} v (\tau , k _ {2}) d \tau}{2}.
$$

Since $( \tau - \tau _ { 0 } ) > 0$ when $\tau \in ( \tau _ { 0 } , T )$ , we get the following inequality:

$$
\begin{array}{l} \int_ {\tau_ {0}} ^ {T} v \big (\tau , \frac {1}{2} (k _ {1} + k _ {2}) \big) (\tau - \tau_ {0}) d \tau \\ <   \frac {\int_ {\tau_ {0}} ^ {T} v (\tau , k _ {1}) (\tau - \tau_ {0}) d \tau + \int_ {\tau_ {0}} ^ {T} v (\tau , k _ {2}) (\tau - \tau_ {0}) d \tau}{2}. \end{array}
$$

Therefore, $\begin{array} { r } { \int _ { \tau _ { 0 } } ^ { T } v ( \tau ) ( \tau - \tau _ { 0 } ) d \tau } \end{array}$ is also a convex function in k. QED.

Lemma 2. The expected total cost is a convex function of k.

Proof. See the online appendix.

For any given configuration $( n , k )$ , the expected total cost is obtained from Equation (1) using the corresponding piecewise linear functional form of $v ( \tau )$ Because the expected total cost is convex in $k ,$ the dichotomous search algorithm in Figure 3 yields the optimal $k ^ { * }$ for a given n. Because the number of iterations of this algorithm can be determined by

## Figure 3. Dichotomous Search Algorithm to Derive the Optimal Number of Backup VMs

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: $q = 0, i^q = 1, j^q = n, Q_k$ as calculated from (1) given $n, T, \alpha, v(\tau), h, \pi, \epsilon &gt; 0, l &gt; 0$ While $j^q - i^q &gt; l$ $k^{q^-} = \frac{1}{2}(i^q + j^q) - \epsilon, k^{q^+} = \frac{1}{2}(i^q + j^q) + \epsilon;$ if $Q_{k^{q^-}} \geq Q_{k^{q^+}} i^{q+1} = k^{q^-}, j^{q+1} = j^q;$ else $i^{q+1} = i^q, j^{q+1} = k^{q^+};$ end if $q = q + 1;$ end while $k^* = \frac{1}{2}(i^q + j^q);$ Return $k^*$
</div>

$l = ( 1 / 2 ^ { q } ) ( n - 1 ) + 2 \epsilon ( 1 - 1 / 2 ^ { q } )$ (Bazaraa et al. 2013), the complexity of the algorithm is $O ( \log n )$

We also provide a divide-and-conquer search algorithm in the online appendix for those cases wherein our assumption on the probability of SLA violation $\begin{array} { r } { \int _ { ( 1 - \alpha ) T } ^ { T } v ( \tau ) \dot { d } \tau } \end{array}$ being decreasing and convex in k is not guaranteed to hold. The worst-case complexity of this algorithm is O<sup>(</sup>n<sup>)</sup>.

In Section 5, we explore the interactions between price, penalty, and the backup allocation strategy. However, if the provisioning cost is suficiently high, the service provider may choose to allocate fewer backup resources. The provider trades of the provisioning cost against the expected penalty cost and may choose to bear the risk of a higher penalty, if the provisioning cost is high enough. Proposition 1 derives the lower bound on the provisioning cost beyond which the provider has no incentive to allocate any backup VMs. In Section $^ { 6 , }$ we also computationally study how interaction between the provisioning cost and the penalty rate afects determination of optimal k .

Proposition 1. The provider would choose not to allocate any backup VMs if the unit provisioning cost satisfies the following condition:

$$
\begin{array}{c} h \geq \frac {\pi}{T} \Bigg (\int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau , k = 0)   d \tau \\ - \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau , k = 1)   d \tau \Bigg). \end{array}
$$

Proof. The expected total cost for $k = 0$ is hnT <sup>+</sup> π $\begin{array} { r } { { \cdot } \int _ { ( 1 - \alpha ) T } ^ { T } ( \tau - ( 1 - \alpha ) T ) v ( \tau , k = 0 ) d \tau } \end{array}$

Similarly, the expected total cost for k <sup></sup>1 is $h ( n { + } 1 ) T$ $\begin{array} { r l } {  { + \pi \int _ { ( 1 - \alpha ) T } ^ { T } \bigl ( \dot { \tau } - ( 1 - \dot { \alpha _ { \alpha } } ) T \bigr ) v ( \tau , k = 1 ) d \tau . } } \end{array}$

From Lemma $2 , k ^ { * } = 0$ as long as

$$
\begin{array}{c} h n T + \pi \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau , k = 0) d \tau \leq h (n + 1) T \\ + \pi \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau , k = 1) d \tau , \end{array}
$$

or,

$$
\begin{array}{c} h \geq \frac {\pi}{T} \Bigg (\int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau , k = 0) d \tau \\ - \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau , k = 1)   d \tau \Bigg). \end{array}\tag{QED.}
$$

## 5. Availability-Aware Pricing Strategy

We first derive the breakeven price that can be charged, given a specific penalty level. This analysis is used to develop a price-penalty schedule for a given client. We then model a two-period pricing problem where the

SLA is violated in Period 1. The provider considers the strategy of deferring the penalty payment by another service window to make up the service deficit; the client is incentivized to accept the deferral in exchange for a price discount. This strategy can provide certain benefits to the cloud datacenter operator: It locks in the client for another service window and provides an opportunity to the operator to make up for the service shortfall and thus avoid paying the penalty. If the price in the second service window is set such that the buyer is incentivized to select the deferral option, then the buyer also benefits as a result of the lower cost. We analytically derive the price needed to incentivize the client to select the deferral option when faced with a violation of their SLA.

## 5.1. Price-Penalty Schedule

Typical cloud clients use the services to deliver a variety of end-user functionalities, from data collection and analysis to running user authentication services to managing configurations on a multitude of end user devices. These functionalities may vary in their mission-criticality. The clients may also vary in their risk tolerance, particularly with regard to the risk of nonavailability. Clients using cloud services for more mission-critical tasks or who have a low tolerance for risk may favor higher penalty levels as a hedge against the risk of nonavailability. Clients with fewer critical usage patterns or who are less risk-averse or those who are more price-sensitive may not emphasize penalty rates as much, and may instead seek lower prices. We develop a price-penalty schedule that would form the basis of a possible negotiation between the provider and the client. The schedule presents the breakeven prices at varying penalty levels such that the provider would be indiferent between the choices. In a negotiated solution, the provider would present the client with the schedule after appropriately marking up the breakeven prices for its profitability and the client would choose from this schedule based on the missioncriticality of the usage and their risk tolerance. Modeling the interaction between the provider and the client is an important area for future research.

The breakeven price for a given penalty level is obtained as follows: Consider a configuration (n, k) with the optimal backup level k . In the case of resource over-provisioning (surplus), the expected penalty cost is zero since the accumulated expected downtime is less than the expected penalizable downtime. Similarly, in the case of resource under-provisioning (deficit), the accrued expected downtime exceeds the expected penalizable downtime. Note that revenues are earned only from the n VMs, regardless of the backup VMs allocated; this is in congruence with current practice in cloud service SLAs. Therefore, considering the likelihood of each of these two cases, the expected total profit for the provider is as follows:

$$
\begin{array}{l} \int_ {0} ^ {(1 - \alpha) T} (n p T - h (n + k) T) v (\tau) d \tau \\ \qquad + \int_ {(1 - \alpha) T} ^ {T} (n p T - h (n + k) T - \pi (\tau - (1 - \alpha) T)) v (\tau) d \tau \\ \qquad = n p T - h (n + k) T - \pi \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau) d \tau . \end{array}
$$

Thus, the breakeven price $p ^ { \prime }$ for a given penalty π and backup level k is derived as follows:

$$
\begin{array}{c} n p T - h (n + k) T - \pi \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau)   d \tau \geq 0, \\ p ^ {\prime} \geq \frac {h (n + k) T + \pi \int_ {(1 - \alpha) T} ^ {T} (\tau - (1 - \alpha) T) v (\tau)   d \tau}{n T}. \end{array}
$$

Therefore, the price-penalty schedule is obtained as follows: First, for each penalty level, the optimal $k ^ { * }$ is derived using the dichotomous search algorithm. Next, given π and $\bar { k } ^ { * }$ , the breakeven price $p ^ { \prime }$ is derived. We observe that, as expected, the breakeven price increases with increasing penalty levels, ceteris paribus. We further computationally explore this relationship in Section 6.

## 5.2. Penalty-Deferred Pricing

The SLA-promised uptime guarantee is one of the factors that determine the optimal backup resource allocation. However, the realized uptime could difer from the guaranteed uptime. In this section, we focus on the scenario wherein the realized uptime is less than the guaranteed uptime in a given time window. This is the case where an SLA is violated in a time window.

Note that the provider’s objective is to minimize the expected total cost, which is an aggregate of provisioning and penalty costs. In cases where the penalty rate is significantly low, it may be advantageous for the provider to intentionally under-provision. Similarly, cases with high penalty rates may induce the provider to purposely over-provision. Now, consider the high penalty rate case. We introduce a mechanism called the penalty deferral strategy whereby if the uptime guarantee is violated, the client has the option to delay receiving the penalty payment to the next service window. In exchange, the provider appropriately incentivizes the client so that the latter benefits from deferring. Our penalty deferral strategy is inspired by the current practice at AWS where clients must report outages, and AWS, upon verification, pays a penalty in the form of service credits, applicable toward the following month’s consumption. In addition to placing the onus on the client for outage tracking and reporting, a relatively onerous task, the AWS policy ofers no choice as to penalty payments and the redemption thereof. By contrast, even if our strategy were to be implemented in a setting where the provider assumes the responsibility of tracking and recording downtime proactively, he can still benefit from locking in the client for another period and from adjusting his resource allocations such that he may be able to fulfill the uptime guarantee requirement. The proposed strategy is more client-friendly while allowing the provider to increase revenue and goodwill. In the following discussion, we focus on the special case of high penalty contracts that have been violated and derive the optimal price discount that would incentivize the client to choose the deferral option.

Let $\alpha _ { i } ^ { \mathrm { { o b j } } }$ be the target level of service set by the provider in a particular service window i; $k _ { i }$ be the optimal number of backup VMs in i; $\alpha _ { i }$ be the actual service level provided by the end of the service window $i ;$ and $p _ { i }$ be the unit price in $i .$ When $i = 1$ , the target service level $\alpha _ { i } ^ { \mathrm { { o b j } } }$ is equal to the SLA specified uptime guarantee, α. When $i > 1$ , the target service level is a function of α and the accumulated actual service level $\alpha _ { i - 1 }$ . Note that at the end of each service window $i ,$ the actual service level provided will be $\alpha _ { i } \geq \alpha _ { i } ^ { \mathrm { o b j } }$ (surplus case) or $\alpha _ { i } < \alpha _ { i } ^ { \mathrm { o b j } }$ (deficit case).

If $\alpha _ { i } \geq \alpha _ { i } ^ { \mathrm { { o b j } } }$ , as per current practice, the entire surplus is for the client to keep and has no efect on resource allocation in the next time period. Here we exclusively focus on the riskier proposition for the provider, i.e., the service deficit. In the case of a deficit $\dot { ( \alpha _ { i } < \alpha _ { i } ^ { \mathrm { o b j } } ) }$ , the client is provided with two options. In the first, the client may accept the penalty payment from the provider at the end of service window i and the provider starts the next window with $\boldsymbol \alpha _ { i + 1 } ^ { \mathrm { o b j } }$ reset to α. In the alternate option, if the provider suficiently incentivizes the client with a lower price, he may defer the penalty payment until the next service window $i + 1$ . In this case, the provider takes the deficit from window i into account in determining $\boldsymbol \alpha _ { i + 1 } ^ { \mathrm { o b j } }$ The provider needs to set $\alpha _ { i + 1 } ^ { \mathrm { o b j } } > \alpha$ in the service window i <sup>+</sup> 1 to attain accumulated α across both service windows. Let ∆k denote the additional backup VMs allocated by the provider to fulfill the higher uptime commitment $\boldsymbol \alpha _ { i + 1 } ^ { \mathrm { o b j } }$ . Hence, $k _ { i + 1 } = k _ { i } + \Delta k$ . Intuitively, $p _ { i + 1 }$ should be set to less than $p _ { i }$ to appropriately incentivize the client. Otherwise, the client would always prefer immediate penalty payments.

We now develop the foundations of a multi-period rolling service window model by considering a tractable two-period problem. In fact, in most payas-you-go cloud platforms, the service window over which the uptime guarantee must be fulfilled is one month. The service window is not suficiently long to incorporate present value discounting in the model.

Figure 4. Client’s Decision Tree for the Two-Period Problem  
![](/api/attachments/JQ47RZ9V/fulltext/images/3b7d0d4d2cb927da47422f83e07c199d83a20b5ae66f433b28c769bdb9a96f31.jpg)

Hence, for tractability, in our study, the discount factor is assumed to be 1, to lay a foundation for future research. The client’s decision tree for the two-period problem is shown in Figure 4. In the case of SLA violation (deficit) in period 1, the client has two choices, i.e., receive the penalty payment in period 1 or defer it. To determine the optimal price to charge for period $^ { 2 , }$ we model the client’s expected costs under each option. The client’s expected cost is comprised of the payment for n servers less the expected penalty. Let $E C _ { A }$ be the expected cost in period 2 if the client chooses to accept the penalty in period 1; likewise let $E C _ { B }$ be the expected cost in period 2 if the client chooses to defer the collection of penalties in exchange for a lower price in period 2. The client is indiferent between the two choices when $E C _ { A } = E C _ { B }$ . Note that the question of deferring the penalty arises only when the downtime exceeds the maximum allowable downtime; hence, we impose the following condition: $\tau _ { 1 } > ( 1 - \alpha ) t _ { 1 }$ . We therefore have the following proposition.

Proposition 2. The client would choose to defer the penalty incurred within the service window to the next period so long as $\underline { { { p } } } _ { 2 } \leq p _ { 2 } \leq \bar { p } _ { 2 }$ where

$$
\begin{array}{r l} \bar {p} _ {2} = & \left[ p n t _ {2} - \pi (\tau_ {1} - (1 - \alpha) t _ {1}) - \pi \int_ {(1 - \alpha) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha) t _ {2}) \right. \\ & \left. \cdot v (\tau_ {2}, k _ {1}) d \tau_ {2} + \pi \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) \right. \\ & \left. \cdot v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} \right] \frac {1}{n t _ {2}}, \end{array}
$$

$$
\begin{array}{r l} \underline {{p}} _ {2} = & \left[ h (n + k _ {1}) t _ {1} + h (n + k _ {1} + \Delta k) t _ {2} \right. \\ & \left. + \pi \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) \right. \\ & \left. \cdot v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} - n p t _ {1} \right] \frac {1}{n t _ {2}}. \end{array}
$$

Proof. We first derive the expected total cost for the case where the client chooses to accept the penalty at the end of period 1

$$
\begin{array}{l} E C _ {A} = E C _ {A} (s u r p l u s i n p e r i o d 2) + E C _ {A} (d e f i c i t i n p e r i o d 2) \\ \qquad = \int_ {0} ^ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} [ p n t _ {1} - \pi (\tau_ {1} - (1 - \alpha_ {1} ^ {\mathrm{obj}}) t _ {1} + p n t _ {2} ] \\ \qquad \cdot v (\tau_ {2}, k _ {1})   d \tau_ {2} \\ \qquad + \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} [ p n t _ {1} - \pi (\tau_ {1} - (1 - \alpha_ {1} ^ {\mathrm{obj}}) t _ {1} \\ \qquad + p n t _ {2} - \pi (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2} ] v (\tau_ {2}, k _ {1})   d \tau_ {2} \\ \qquad = p n t _ {1} - \pi (\tau_ {1} - (1 - \alpha_ {1} ^ {\mathrm{obj}}) t _ {1}) + p n t _ {2} \\ \qquad - \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} \pi (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) v (\tau_ {2}, k _ {1})   d \tau_ {2}. \end{array}
$$

For the case where the client chooses to defer, the target service level in period $2 , \alpha _ { 2 } ^ { \mathrm { { o b j } } }$ , is then updated based on the deviation of the SLA-specified uptime guarantee, $\alpha ,$ from the service level in period 1 as: $\alpha _ { 2 } ^ { \mathrm { o b j } } = ( \alpha ( t _ { 1 } + t _ { 2 } ) -$ $( t _ { 1 } - \tau _ { 1 } ) ) / t _ { 2 }$

Finally, the expected total cost when the client chooses to defer is denoted by $E C _ { B }$ and modeled using the expected cost of each case aggregated across both periods, as shown below

$$
\begin{array}{l} E C _ {B} = E C _ {B} (s u r p l u s i n p e r i o d 2) + E C _ {B} (d e f i c i t i n p e r i o d 2) \\ \qquad = \int_ {0} ^ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} (p n t _ {1} + p _ {2} n t _ {2}) v (\tau_ {2}, k _ {1} + \Delta k)   d \tau_ {2} \\ \qquad + \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} (p n t _ {1} + p _ {2} n t _ {2} - \pi (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) \\ \qquad \cdot v (\tau_ {2}, k _ {1} + \Delta k)   d \tau_ {2} \\ \qquad = p n t _ {1} + p _ {2} n t _ {2} \\ \qquad - \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} \pi (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) v (\tau_ {2}, k _ {1} + \Delta k)   d \tau_ {2}. \end{array}
$$

The client is indiferent between the two choices when $E C _ { A } = E C _ { B }$ . Hence, we get

$$
\begin{array}{l} \bar {p} _ {2} = \left[ p n t _ {2} - \pi (\tau_ {1} - (1 - \alpha) t _ {1}) \right. \\ \quad \left. - \pi \int_ {(1 - \alpha) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha) t _ {2}) v (\tau_ {2}, k _ {1}) d \tau_ {2} \right. \\ \quad \left. + \pi \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} \right] \frac {1}{n t _ {2}}. \end{array}
$$

Therefore, the client would choose to defer the penalty so long as ${ p _ { 2 } } \le \bar { p } _ { 2 }$

In addition, the provider’s profit function under the deferral strategy is as follows:

$$
\begin{array}{l} \int_ {0} ^ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} [ n p t _ {1} + n p _ {2} t _ {2} - h (n + k _ {1}) t _ {1} - h (n + k _ {1} + \Delta k) t _ {2} ] \\ \quad \cdot v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} \\ \quad + \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} [ n p t _ {1} + n p _ {2} t _ {2} - h (n + k _ {1}) t _ {1} - h (n + k _ {1} + \Delta k) t _ {2} \\ \quad - \pi (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) ] v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} \\ = n p t _ {1} + n p _ {2} t _ {2} - h (n + k _ {1}) t _ {1} - h (n + k _ {1} + \Delta k) t _ {2} \\ \quad - \pi \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} [ \tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2} ] v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2}. \end{array}
$$

Therefore, the minimum price the provider should charge is determined where

$$
\begin{array}{l} n p t _ {1} + n p _ {2} t _ {2} - h (n + k _ {1}) t _ {1} - h (n + k _ {1} + \Delta k) t _ {2} \\ \qquad - \pi \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} \geq 0, \\ \underline {{p}} _ {2} \geq \frac {1}{n t _ {2}} \bigg [ h (n + k _ {1}) t _ {1} + h (n + k _ {1} + \Delta k) t _ {2} \\ \qquad + \pi \int_ {(1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}} ^ {t _ {2}} (\tau_ {2} - (1 - \alpha_ {2} ^ {\mathrm{obj}}) t _ {2}) v (\tau_ {2}, k _ {1} + \Delta k) d \tau_ {2} - n p t _ {1} \bigg ]. \end{array}
$$

Therefore, the provider would profit so long as $p _ { 2 } \geq \underline { { p } } _ { 2 }$

Thus, the provider can profit while the client chooses to defer the penalty incurred within the service window to the next period, if and only if $p _ { 2 } \leq p _ { 2 } \leq \bar { p } _ { 2 }$ . In <sup>¯</sup>the case of a contract with the profile of $p _ { 2 } \geq \bar { p } _ { 2 } ,$ the <sup>¯</sup>provider would not ofer the penalty deferral option to the client since the discount is too large for the provider to profit. QED.

In the online appendix, the penalty deferral strategy is computationally evaluated in comparison with a status quo strategy where the buyer does not have the option of deferring the penalty.

## 6. Experimental Results

The computational analyses in this section study the impact of various parameters on the number of backups provisioned and the two types of costs faced by the cloud datacenter provider. The objectives of the computational studies are: (1) test the goodness-of-fit of various well behaved distributions against that of the downtime probability distribution derived from realworld server log data; (2) validate the convexity of the SLA violation probability in the number of backup VMs; (3) study how the accuracy of the piecewise linear approximation process afects key model parameters such as penalizable downtime and provider’s total cost; (4) evaluate the interactions between penalty rate, provisioning costs, and the optimal number of backup VMs provisioned; (5) compare how our VM provisioning algorithm performs vis-à-vis a set of benchmark provisioning strategies.

## 6.1. Downtime Distribution Fitting

As discussed in Section 4, a diferentiable functional form of the downtime distribution v<sup>(</sup>τ<sup>)</sup> is needed to derive the closed form solution to the optimal number of backup VMs. We derived the downtime pdf from real-world server log data collected from the CCR, a large high-performance computer center at SUNY Buffalo, using the sample path randomization algorithm in Du et al. (2015). We use a server log data set also obtained from the CCR. This data set is comprised of failure and repair events of 1,143 cores identified by their IDs and general failure types. The algorithm derives the transient downtime pdf for a single failure type (server level failures) and a 1:1 physical to virtual server mapping. The algorithm was based on the limiting behavior of the underlying birth-death process of VM failures and repairs, using a sample path randomization approach. Note that, although steady-state probabilities for the birth-death process are relatively easy to obtain, we may be unable to establish in practice that the system has reached steady state in any given time window. This approach derives the exact transient pdf of an $( n , k )$ allocation. See Du et al. (2015) for complete details of this data set and the algorithm that estimates the downtime pdf. The histogram in $\mathrm { F i g \mathrm { - } }$ ure 5 shows the estimated downtime pdf. We perform distribution-fitting exercises against well behaved distributions, specifically exponential, gamma, Weibull, log normal, and log logistic distributions. The best fit parameters were derived for each of these standard distributions. Figure 5 compares these distributions against the estimated downtime pdf. We observe that none of the distributions appear to closely approximate the estimated downtime pdf.

Figure 5. Downtime Distribution v<sup>(</sup>τ<sup>)</sup> Fitting  
![](/api/attachments/JQ47RZ9V/fulltext/images/341cd74c41376379ee0e34ad2976a7f1eecc7332cd6d9770a2f88b18bff32c98.jpg)

Table 2. Goodness-of-Fit Test Results

<table><tr><td>Distribution</td><td>Exponential</td><td>Normal</td><td>Weibull</td><td>Gamma</td><td>Loglogistc</td><td>Lognormal</td></tr><tr><td>Estimated parameters</td><td> $\mu = 7,182.36$ </td><td> $\mu = 7,182.36$  $\sigma = 1,072.11$ </td><td>A = 7,596.95B = 9.29304</td><td>a = 35.8565b = 200.308</td><td> $\mu = 8.8922$  $\sigma = 0.0856973$ </td><td> $\mu = 8.86537$  $\sigma = 0.179622$ </td></tr><tr><td>Test-statistic</td><td> $3.2599e + 03$ </td><td> $5.6469e + 05$ </td><td> $2.0999e + 06$ </td><td> $7.1657e + 05$ </td><td> $9.4499e + 05$ </td><td> $7.2361e + 05$ </td></tr><tr><td>p-value</td><td>&lt;0.05</td><td>&lt;0.05</td><td>&lt;0.05</td><td>&lt;0.05</td><td>&lt;0.05</td><td>&lt;0.05</td></tr></table>

This is confirmed in the Chi-Square Goodness of Fit Tests that tested each distribution (with their best fit parameters) against the estimated downtime pdf, as shown from the respective p-values in Table 2. Our experiments find no suitable well behaved, diferentiable distribution to satisfactorily fit the downtime pdf estimated from real-world high performance computer center data. This motivates the need for a piecewise linear approximation of $v ( \tau )$ as discussed in Section 4. The piecewise linear approximation frees the cloud datacenter provider from having to enforce a specific distribution on his cloud server log data and enables him to apply our models to any server log data.

In Section 4.2, we assume that the probability of SLA violation, $\begin{array} { r } { \int _ { ( 1 - \alpha ) T } ^ { T } v ( \tau ) d \tau , } \end{array}$ , is decreasing and convex in k. We now empirically validate this assumption through

## 6.2. Convexity of SLA Violation Probability Distribution

two sets of experiments using $n = 5 0$ and $n = 1 0 0 ,$ as follows: In each set, k is set to 2%, $4 \% , \ldots , 3 0 \%$ of n with an increment size of 2%. We derive the downtime distributions for each $( n , k )$ combination where $T = 3 0$ days using the sample path randomization algorithm from Du et al. (2015). This algorithm divides the service window into $T / \Delta t$ consecutive intervals of length $\Delta t$ of vanishing size; we set $\Delta t = 5$ minutes in our experiments. At each level of $k ,$ the uptime guarantee α is set at three diferent levels: 90%, 95%, and 99%. We derive the SLA violation probability at each of the three levels for each $( n , k )$ combination in our experiments. Figure 6 confirms that the SLA violation probability is decreasing and convex in k. We also find in our experiments that the SLA violation probability drops to zero at $k \geq 2 8 \%$ of n when $n = 5 0$ , and at $k \geq 2 4 \%$ when $n =$ 100. This experiment may be replicated by the cloud service provider on their own data to determine the upper bound of the search space in the optimal backup resource provisioning algorithm in Section 4. At the other extreme, SLA violation is certain when $k = 2 \%$ to 10% for $n = 5 0$ and $n = 1 0 0$ . Note that this may be acceptable to a cost-minimizing provider when the penalty rate is suficiently lower than the provisioning cost. Clients whose cloud service jobs are non-missioncritical or are only ancillary to their main business may select lower penalty rates, as such contracts may also be priced lower; we explore the relationship between price and penalty in depth in Section 6.4. Finally, as expected, for a given value of k, it becomes harder to satisfy the service level as the uptime guarantee α increases.

Figure 6. SLA Violation Probability Decreases with Increasing Backup VMs  
![](/api/attachments/JQ47RZ9V/fulltext/images/9c627718c314a9580ef4942d0523ffd68a29ab48c96668b57126b73878caea6e.jpg)

![](/api/attachments/JQ47RZ9V/fulltext/images/b934bcdcd4b54a4870fc4e3da1f641dd1b8c3dd511188e7ed04d93b1bfb11e37.jpg)

## 6.3. Impact of Approximation Accuracy on Penalizable Downtime and Total Cost

Accuracy, a parameter in the piecewise linear approximation algorithm, afects the number of segments into which v<sup>(</sup>τ<sup>)</sup> is partitioned. Increasing the accuracy parameter increases the number of linear segments used to approximate the downtime pdf, thereby reducing the error in approximation. The greater number of segments, however, implies increasing complexity in our analytical models. Understanding how the accuracy parameter afects the two key functions in our model, expected penalizable downtime, and the provider’s expected total cost, would enable the provider to appropriately set this parameter. We provide a visualization in the online appendix to show the high degree of precision that is achieved by the piecewise linear approximation under high values of the accuracy parameter. In this section, we explore the impact of approximation accuracy on these two functions. We derived the expected total cost and penalizable downtime curves for two diferent cases, n <sup></sup> 50 and $n = 1 0 0 _ { \cdot }$ , using $\alpha = 0 . 9 9$ and $T = 3 0$ days, with accuracy, r, set to five levels ranging from 0.1 to 0.99. The closest (best) approximation in our experiments is achieved with $r = 0 . { \bar { 9 } } 9$

As shown in Figure 7, when accuracy is set between 0.8 to 0.99, the expected penalizable downtime and the expected total cost lie within a tight range. When the accuracy level drops below 0.8, both functions are significantly diferent than those derived using the best approximation, with an especially large diference noted for the penalizable downtime for $n = 5 0$ This informs the provider that an accuracy rate of 0.8 may be suficient for the purposes of resource provisioning and price-penalty schedule design as per our analytical models. However, in some cases, the optimal number of backup VMs is more sensitive to the approximation accuracy as the downtime distribution shows high variance leading to dramatic changes in the penalizable downtime and total cost, depending on the accuracy parameter. This then necessitates the selection of a higher accuracy level in piecewise linear approximation.

Figure 7. Impact of Approximation Accuracy Level (n <sup></sup> 50, 100)  
![](/api/attachments/JQ47RZ9V/fulltext/images/b818f399a580b169ff2632452abcbd7f9a71a93114b4493a22ca4a9048c7d563.jpg)

6.4. Impact of Penalty on Backup VM Provisioning The penalty rate for nonavailability in cloud SLAs would largely be driven by the mission-criticality of the tasks that a client assigns to the datacenter. A client running highly mission-critical jobs may insist on high penalty rates to hedge against loss of revenue and reputation from nonavailability of services to its end-users. The cloud provider in turn reacts to the penalty rate by allocating backup resources accordingly. Another parameter that plays a role in this interaction between penalty and backup allocation strategy is the provisioning cost. Specifically, how large must the penalty rate be in relation to the provisioning cost before we see a significant change in the backup allocation? We therefore explore how backup provisioning, $k ^ { * } ,$ changes with changing ratio between the penalty and the provisioning cost, h. We set h to 1 and derived the optimal $k ^ { * }$ for increasing penalty rates, ranging from 1:1 to 5,000:1, for $n = 5 0$ and $n = 1 0 0$

As Figure 8 illustrates, when the penalty rate is at par or even slightly higher than h (1:1 and 5:1 for $n = 5 0 ;$ 1:1, 5:1, and 10:1 for $n = 1 0 0 )$ , k remains unchanged at two. However, when the ratio is increased to 50:1, $k ^ { * }$ increases sharply, specifically in the case of $n =$ 100, from 1 to 16. At that point, the penalty rate is large enough to induce the provider to allocate significantly more backup VMs, for $n = 1 0 0$ . There is a steady increase in $k ^ { * }$ beyond the 50:1 ratio, albeit at a slowing pace. This is because for a given failure and repair time distribution, as k increases, the expected penalizable downtime reduces until it is close to zero. When the penalty rates are quite high, the provider will allocate many more backup resources such that the SLA violation probability is as close to zero as possible. Once this point is reached, this high level of backup allocation may continue to hedge the provider’s SLA violation risk at even higher penalty rates. This experiment highlights how the penalty rate, which is largely clientdriven, afects the provider’s decisions on resource provisioning, given the provisioning cost. In the online appendix, we also computationally extend our analysis by studying the impact of penalty and provisioning cost on VM pricing.

![](/api/attachments/JQ47RZ9V/fulltext/images/1e3e264cce3cd2e8bb2f019875724cded657e7d9297f287276c87e73c3d96618.jpg)

## 6.5. Benchmarking the Dichotomous Search Algorithm

Instead of using the dichotomous search algorithm provided in Section 4, a cloud service provider may set the number of backup VMs to a fixed percentage of the n primary VMs demanded by the client. To our knowledge, this is the only study that determines the optimal availability-aware backup resource allocation in a cloud datacenter. Discussions with practitioners in cloud datacenters reveal that ad hoc rules of thumb are usually followed, setting the number of backup VMs to a certain fixed number. We therefore benchmark the quality of our solutions to the following suitable rules of thumb, i.e., k <sup></sup> 10%n, 15%n, 20%n, 25%n, 30%n, 35%n, for two scenarios where $n = 5 0$ and $n = 1 0 0$ with a service window of 30 days. We derive the expected penalty cost for each case on the basis of the expected penalizable downtime. We also derive the provisioning cost and the expected total cost for each case. In this study, we set the ratio between unit provisioning cost and penalty rate to 1:100. We also model other ratios ranging from 1:500, 1:1,000, to 1:5,000 for $n = 5 0$ and n <sup></sup> 100 scenarios, which are provided in the online appendix.

Figure 9 compares these three costs across all of the benchmarks and our optimal solution. Without solving a model such as ours, the cloud service provider would not know a priori what an appropriate fixed percentage should be, given the failure and repair characteristics of the datacenter. As can be seen from the figure, if he guesses too low at 10% of $n ,$ the expected penalty costs overpower the savings on provisioning cost and thus drive up the expected total cost; if he guesses too high at 35% of $n ,$ the additional provisioning cost does not buy him any significant savings in the expected penalty cost, which appears to stabilize after a certain point for this example. Even if the provider were to guess right, for a diferent set of failure and repair characteristics, the same rule of thumb provides no assurance of stable results. Note that the computation time to determine k is negligible with the longest being 0.836 seconds. Finally, Figure 9 also empirically validates the convexity of the expected total cost function as proven in Lemma 2.

Figure 8. Sensitivity of Optimal k to Varying Penalty and Demand (n <sup></sup> 50, 100)  
![](/api/attachments/JQ47RZ9V/fulltext/images/c729dac5bacc279030257301f3416f0ad42d202d050ebe83cea242aaeb6a8211.jpg)

![](/api/attachments/JQ47RZ9V/fulltext/images/61eb4919e5acd1c6eca2160752732727a358061518cf7dc58bc5bb1ed544f237.jpg)

## 7. Managerial Implications and Concluding Remarks

Cloud datacenter providers simultaneously administer multiple SLAs, with each contract stipulating penalties for nonavailability of service. Providing additional backup resources helps manage the risk of violating the SLA. However, the optimal administration of these SLAs is crucial to the profitability of each contract;

under-provisioning may result in high penalty costs and loss of reputation, while over-provisioning erodes profits in an increasingly competitive market due to poor resource utilization. In general, most of the extant contract design research optimizes utility or profits. Our focus is primarily on availability-aware design and management of cloud SLAs: To our knowledge, this is the first study of this kind. The notions of over- and under-provisioning are driven by availability, which in turn drive strategic decisions within the contractual relationship. In spite of the seemingly unlimited provisioning capabilities (Mell and Grance 2011) because of cloud virtualization technologies (Wang et al. 2010), the actual service level is bounded by 100%. Thus, the influence of over-provisioning is bounded. It is therefore unrealistic for the provider to “save” a large amount of service uptime toward future demands by over-provisioning backup VMs at a certain point.

Figure 9. Comparison on the Costs Between Dichotomous Search Algorithm and the Benchmark  
![](/api/attachments/JQ47RZ9V/fulltext/images/965f47c1792c2ce38ec7d483b39cb9fd001c9c62935f4f4561e2ac26d08640e0.jpg)

![](/api/attachments/JQ47RZ9V/fulltext/images/c40afa425c4e8cdbf8ced98bf624ab2da541145dbefdb2c59be1ba413787860f.jpg)

Accordingly, the focus and contributions of this paper are threefold: (i) optimally allocating backup resources for an SLA that minimizes total cost by balancing and managing the risks of under- and overprovisioning; (ii) deriving a price-penalty schedule that presents an array of eficient choices for an agreed settlement between a service provider and a client; and (iii) developing eficient penalty deferral strategies that incentivize clients to continue with the service for extended periods when an SLA is violated.

We conducted extensive computational studies to validate and supplement the analytical work. First, using real-world server log data, we show that downtime distribution functions need not fit any standard pdf, thereby necessitating piecewise linearization of the downtime pdf, instead of imposing strong distributional assumptions that may not hold in practice. Next, we show that the linearization process can tolerate a modicum of imprecision in the approximation accuracy parameter in serving the purpose of our cloud contract management and design models. Finally, we demonstrate that a profit-maximizing provider may deliberately choose to assume a certain amount of risk of SLA violation when the penalty rate is relatively low; under-provisioning may be a profit-maximizing strategy for clients who are price-sensitive or run low-risk, less critical services on the cloud.

Some key managerial implications emerge from this study. First, better understanding of the provisioning cost is crucial for efective resource provisioning. As demonstrated in our experiments, the ratio between provisioning cost and penalty rate has a direct impact on quantification of backup resources. For example, when the penalty rates are significantly higher than the provisioning cost, the provider will allocate considerably more backup resources such that the SLA violation probability is as close to zero as possible. The provisioning cost also plays a part in the breakeven price, which can be viewed as the lower bound on the prices quoted during the SLA negotiation process.

This would depend on a reasonably accurate estimation of various costs such as electricity, network bandwidth, cooling, labor, operations, software, and hardware which account for the majority of the provisioning cost in a cloud datacenter.

Second, the current strategy of estimating backup resource allocation using rules of thumb is not cost efective or resource eficient, having significant profit implications. By incorporating the calculated downtime distribution of a particular datacenter, without imposing onerous distributional assumptions, providers could fine-tune resource provisioning policies for each client, where simply relying on “guesstimates” would mean greater erosion in profit by overor under-provisioning.

Third, the provider should be able to diferentiate availability of the cloud services, given the heterogeneity among the clients, based on the end-use of their oferings and ensuing risk implications. Thus, the construction of SLA and backup resource allocation strategies also depend on the client type. For instance, under-provisioning may be a profit-maximizing strategy for clients who are price-sensitive or who run less critical services on the cloud. On the other hand, the provider would be inclined to allocate more backup VMs for high-availability clients associated with potentially high penalty rates. In either case, precise resource provisioning, as formulated by our models, would help drive profitability.

Finally, there is a non-zero possibility of violating the SLA, even for high-availability clients. A state-of-theart incentive design in the event that the provider does not meet the availability commitment may be instrumental in reducing the likelihood of eventually paying the corresponding penalty, while locking in the client for one more contract window and regenerating goodwill. Note that our proposed mechanism is inspired by current practices followed by providers such as AWS, but is designed to incentivize the client to willingly opt for a penalty deferral.

Future research may study the availability-aware backup resource allocation problem with dynamic reallocations of VMs based on real-time needs within a service window. Based on our study, the provider, at the commencement of service, derives the optimal number of backup VMs to mitigate the SLA violation risk, using agreed-upon SLA constructs, e.g., price, penalty, and uptime guarantee. This backup allocation would, in turn, determine the predicted level of service that can be achieved for that client in a given service window. While the initial allocation, albeit optimal, is decided on the basis of the SLA-specified service level, it is likely that actual failure and repair events may result in some deviation from the predicted level of service at runtime. Future research may consider the extensions of a scenario wherein the provider periodically reassesses the backup VMs provisioned since the number of backup VMs may need to be increased or decreased based on the monitoring of service to minimize the total expected cost. In cases where the actual service level is lower than expected, it may be advantageous to the provider to add more backups to mitigate the predicted shortfall. Similarly, cases with a higher service level may incentivize the provider to remove some of the allocated backup VMs. However, there are some challenges that must be addressed. These include: (1) the reprovisioning must be appropriately timed, as it afects the system’s ability to recover in time, and (2) the quantum of reprovisioning must be suitably determined as it may afect operating costs, in addition to the chance of recovery. Because of the increasing operating and maintenance costs associated with rapid growth in the size of datacenters, the number of clients, and their demand instances, initial resource allocation planning and subsequent dynamic reallocations become crucial for service providers to be profitable in an increasingly competitive space. The cloud service providers would benefit from this future avenue of research on the dynamic backup resource provisioning that strategically intervenes to manage resources for a given contract over its life cycle.

## Acknowledgments

The authors would like to thank the senior editor, the associate editor, and the anonymous reviewers for their detailed and constructive comments.

## References

Arcelus FJ, Kumar S, Srinivasan G (2006) Pricing, rebate, advertising and ordering policies of a retailer facing price—Dependent stochastic demand in newsvendor framework under diferent risk preferences. Internat. Trans. Oper. Res. 13(3):209–227.

Armbrust M, Fox A, Grifith R, Joseph AD, Katz R, Konwinski A, Lee G, Patterson D, Rabkin A, Stoica I (2010) A view of cloud computing. Comm. ACM 53(4):50–58.

Arrow KJ, Harris T, Marschak J (1951) Optimal inventory policy. Econometrica: J. Econometric Soc. 19(3):250–272.

Baker R, Urban TL (1988) Single-period inventory dependent demand models. Omega 16(6):605–607.

Bazaraa MS, Sherali HD, Shetty CM (2013) Nonlinear Programming: Theory and Algorithms (John Wiley & Sons, Hoboken, NJ).

Cisco (2012) Cisco global cloud networking survey. https://www .cisco.com/c/dam/en/us/solutions/enterprise-networks/2012 \_Cisco\_Global\_Cloud\_Networking\_Survey\_Results.pdf.

Das S, Du AY, Gopal R, Ramesh R (2011) Risk management and optimal pricing in online storage grids. Inform. Systems Res. 22(4):756–773.

Dastjerdi AV, Buyya R (2015) An autonomous time-dependent SLA negotiation strategy for cloud computing. Comput. J. 58(11): 3202–3216.

Dean J (2009) Designs, lessons and advice from building large distributed systems. http://www.cs.cornell.edu/projects/ladis 2009/ talks/dean-keynote-ladis2009.pdf.

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Du AY, Das S, Gopal RD, Ramesh R (2014) Optimal management of digital content on tiered infrastructure platforms. Inform. Systems Res. 25(4):730–746.

Du AY, Das S, Yang Z, Qiao C, Ramesh R (2015) Predicting transient downtime in virtual server systems: An eficient sample path randomization approach. IEEE Trans. Comput. 64(12):3541–3554.

Eeckhoudt L, Gollier C, Schlesinger H (1995) The risk-averse (and prudent) newsboy. Management Sci. 41(5):786–794.

Emerson (2011) Understanding the cost of data center downtime: An analysis of the financial impact on infrastructure vulnerability. White paper. https://www.anixter.com/content/dam/ Suppliers/Liebert/White%20Paper/Downtime%20-%20data-center -uptime\_24661-R05-11.pdf.

Gerchak Y, Mossman D (1992) On the efect of demand randomness on inventories and costs. Oper. Res. 40(4):804–807.

Gill P, Jain N, Nagappan N (2011) Understanding network failures in data centers: Measurement, analysis, and implications. Proc. ACM SIGCOMM 2011 Conf. (ACM, New York), 350–361.

Goudarzi H, Ghasemazar M, Pedram M (2012) SLA-based optimization of power and migration cost in cloud computing. Proc. 12th IEEE/ACM Internat. Sympos. Cluster, Cloud Grid Comput. (IEEE Computer Society, Washington, DC), 172–179.

ITIC (2017) ITIC 2017–2018 global server hardware, server OS reliability report. https://cloud.kapostcontent.net/pub/3dee045e -4b09-48e3-9077-8b126a9f2093/itic-2017-2018-global-server -hardware-server-os-reliability-report.pdf?kui<sup></sup>E2mHO3mgy vTuSgumkzvevA.

Kaufman RJ, Sougstad R (2008) Risk management of contract portfolios in IT services: The profit-at-risk approach. J. Management Inform. Systems 25(1):17–48.

Kraiselburd S, Narayanan V, Raman A (2004) Contracting in a supply chain with stochastic demand and substitute products. Production Oper. Management 13(1):46–62.

Levy S (2011) In The Plex: How Google Thinks, Works, and Shapes Our Lives (Simon & Schuster, New York).

Liu D, Sarkar S, Sriskandarajah C (2010) Resource allocation policies for personalization in content delivery sites. Inform. Systems Res. 21(2):227–248.

Malhotra D, Bazerman MH (2007) Investigative negotiation. Harvard Bus. Rev. 85(9):72–78.

Mell P, Grance T (2011) The NIST definition of cloud computing. http://faculty.winthrop.edu/domanm/csci411/Handouts/ NIST.pdf.

Mills ES (1959) Uncertainty and price theory. Quart. J. Econom. 73(1):117–130.

Oliver JR (1996) A machine-learning approach to automated negotiation and prospects for electronic commerce. J. Management Inform. Systems 13(3):83–112.

Qin Y, Wang R, Vakharia AJ, Chen Y, Seref MM (2011) The newsvendor problem: Review and directions for future research. Eur. J. Oper. Res. 213(2):361–374.

Rajavel R, Thangarathinam M (2015) Optimizing negotiation conflict in the cloud service negotiation framework using probabilistic decision making model. Sci. World J. 2015:858975.

Sen S, Raghu T, Vinze A (2010) Demand information sharing in heterogeneous IT services environments. J. Management Inform. Systems 26(4):287–316.

Siebenhaar M, Nguyen TAB, Lampe U, Schuller D, Steinmetz R (2012) Concurrent negotiations in cloud-based systems. Vanmechelen K, Altmann J, Rana OF, eds. Econom. Grids, Clouds, Systems, Services, GECON 2011, Lecture Notes Comput. Sci., Vol. 7150 (Springer, Berlin Heidelberg), 17–31.

Urban TL (2002) The interdependence of inventory management and retail shelf management. Internat. J. Phys. Distribution Logistics Management 32(1):41–58.

Urban TL, Baker R (1997) Optimal ordering and pricing policies in a single-period environment with multivariate demand and markdowns. Eur. J. Oper. Res. 103(3):573–583.

Wang L, Von Laszewski G, Younge A, He X, Kunze M, Tao J, Fu C (2010) Cloud computing: A perspective study. New Generation Comput. 28(2):137–146.

Wang S (2012) Online monitoring and prediction of complex time series events from nonstationary time series data. Unpublished doctoral thesis, Rutgers University, Piscataway, NJ.

Wang X, Du Z, Chen Y, Li S (2008) Virtualization-based autonomic resource management for multi-tier web applications in shared data center. J. Systems Software 81(9):1591–1608.

Whitin TM (1955) Inventory control and price theory. Management Sci. 2(1):61–68.

Wu D, Ding M, Hitt LM (2012) IT implementation contract design: Analytical and experimental investigation of IT value, learning, and contract structure. Inform. Systems Res. 24(3):787–801.

Wu L, Garg SK, Buyya R (2011) SLA-based resource allocation for software as a service provider (SaaS) in cloud computing environments. Proc. 11th IEEE/ACM Internat. Sympos. Cluster, Cloud Grid Comput., 195–204.

Yang Z, Aydin G, Babich V, Beil DR (2009) Supply disruptions, asymmetric information, and a backup production option. Management Sci. 55(2):192–209.
