---
otero_id: 9544
otero_key: "23U6D2KP"
title: "Demand Heterogeneity in IT Infrastructure Services: Modeling and Evaluation of a Dynamic Approach to Defining Service Levels"
authors: "Sagnika Sen; T. S. Raghu; Ajay Vinze"
year: "2009"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0196"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/23U6D2KP/fulltext/images/78fe745082988c9e6a6dbb923e2297141a0ea4bd2d597df8d2d47b406b2537e2.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Demand Heterogeneity in IT Infrastructure Services: Modeling and Evaluation of a Dynamic Approach to Defining Service Levels

Sagnika Sen, T. S. Raghu, Ajay Vinze,

## To cite this article:

Sagnika Sen, T. S. Raghu, Ajay Vinze, (2009) Demand Heterogeneity in IT Infrastructure Services: Modeling and Evaluation of a Dynamic Approach to Defining Service Levels. Information Systems Research 20(2):258-276. http://dx.doi.org/10.1287/ isre.1080.0196

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2009, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/23U6D2KP/fulltext/images/ed4e23171151b46ca004f947c7853c7c870aec6e7b86539b271ff8dca8feaa18.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Demand Heterogeneity in IT Infrastructure Services: Modeling and Evaluation of a Dynamic Approach to Defining Service Levels

Sagnika Sen

Information Systems and Decision Sciences Department, California State University, Fullerton, California 92834, ssen@fullerton.edu

T. S. Raghu, Ajay Vinze

Department of Information Systems, Arizona State University, Tempe, Arizona 85287 {raghu.santanam@asu.edu, ajay.vinze@asu.edu}

key feature of service-oriented models of information technology is the promise of prespecified quality levels enforceable via service level agreements (SLAs). This poses difficult management problems when considerable variability exists in user preferences and service demand within any organization. Because variance in expectations impact service levels, effective pricing and resource allocation mechanisms are needed to deliver services at the promised quality level. In this paper, we propose a mechanism for SLA formulation that is responsive to demand fluctuations and user preference variance, with the objective of maximizing organizationa welfare of the participants. This formulation features a dynamic priority based price-penalty scheme targeted to individual users. An analytical model is presented and evaluated for effectiveness of a proposed dynamic priority-based pricing scheme vis-à-vis a baseline fixed-price single-quality level SLA. Simulations using data from an existing SLA is used to provide evidence that the proposed dynamic pricing scheme is likely to be more effective than a fixed-price approach from a system welfare perspective.

Key words: IT services; service level agreements; outsourcing; simulation

History: Seunglin Wang, Senior Editor; Alok Gupta, Associate Editor. This paper was received on July 5, 2006, and was with the authors 8 months for 2 revisions. Published online in Articles in Advance February 26, 2009.

## 1. Introduction

Service-oriented business models for managing information technology (IT) have gained prominence in recent years. These models view IT as a set of services that can be provided by external parties or an internal organization to support organizational business processes. Recent proliferation of on-demand computing models, subscription based services, and managed infrastructure services demonstrate this business-value driven approach towards IT. Despite the growth of the services model, a rising number of problematic deals in recent IT service outsourcing arrangements leading to litigations and deal terminations are also being evidenced (Deloitte Consulting 2005). Complexities in defining services, performance measures, and poor demand management have been cited as prominent reasons for such terminations.

A large percentage of these problematic service outsourcing arrangements (about 42%) are IT infrastructure related.

Currently, service level agreements (SLAs) for most IT service contracts guarantee a prespecified level of service for an organization at an aggregate level. These guarantees are typically augmented with penalty (reward) schemes for not meeting (exceeding) the prespecified service level. There are two related issues that complicate demand management in IT service contexts—variations in demand volume and variations in user preference. First, user demand pattern for different services may be nonstationary in nature. “Within any organization, the demand for IT services is not constant, but varies over time” (Litten 2004, p. 6). Second, the complexity of the service environment is further exacerbated on account of possible variances in user preferences for service quality. Such variances arise from diverse functional and operational requirements within an organization. Sapiera (2003, p. 72) noted “   there are some services that are not easily pigeonholed    would all voice over IP traffic be important or only that traffic between specific places?” Pre-specification of price and quality levels at the organizational level provides little flexibility to the provider to respond to demand variations and exerts considerable pressure on the success of the service arrangement from both customer and service provider’s perspective. It is apparent from the practitioner literature that poorly defined SLAs often lead to inefficient allocation of resources, which adversely affects both customer and provider organizations.

In this research we address demand management issues in IT infrastructure services in the context of SLAs from the perspective of the economic welfare of the participating stakeholders. Previous literature has advocated dynamic pricing approaches as a solution to demand management issues (Gupta et al. 1996, Marbach 2004, Bhargava and Sun 2005), where dynamic pricing is used as a mechanism for resource allocation via congestion control. This stream of research provides a strong direction as to the possible ways of modifying the SLA structure. However, some significant contextual distinctions entail further investigation—both in terms of model formulation and evaluation. First, while admission control has been the primary motivation for previous dynamic pricing literature; in IT outsourcing contexts, the objective of any pricing scheme is to serve all users from the customer organizations. Second, specific conditions under which users and providers prefer dynamic over fixed price approaches and associated implications have not been considered in previous studies. Demand uncertainties and user heterogeneity may lead to preference misalignment in IT service outsourcing arrangements.

The main objective of our research is to investigate the impact of nonstationary demand and user heterogeneity in service provisioning scenarios, and identify if misalignment in preferences over the pricing schemes can be overcome to increase the system welfare. While the context for this research is IT services, the general approach itself is applicable in contexts where multiple users contend for the services of resources (network, human, processing power, or databases).<sup>1</sup> The issues are particularly relevant as IT organizations are also increasingly moving towards chargeback systems (Ross et al. 1999) that have been shown to generate positive value in the relationship between IT departments and business units (Hamblen 2005, Quinlan 2003).

In this paper, we investigate the impact of nonstationary demand and user heterogeneity on a combination of dynamic pricing and penalty mechanisms in the context of IT support and management services, where timeliness of response is a dominant performance measure criterion. Using a dynamic prioritybased price-penalty approach, we model a scheme to enable user focused formulation of SLAs in a multiple service environment. The effectiveness of this approach to SLA formulation is evaluated by comparing it to the current industry practice of fixed-price single quality-level scheme. Effectiveness is defined in terms of economic welfare of the participant organizations and is measured through an extensive simulation study using real life data from a long-term services contract between a large public organization and a prominent service provider. Our modeling approach enables us to consider both multiple service types and multiple priority classes in an (M/M/n) queue discipline where priorities are not prespecified for different service categories. The model results are further extended by simulating nonstationary demand patterns that could cause wide variations in service performance thus enabling us to examine the effectiveness of the dynamic price-penalty approach under more extreme conditions.

Our results provide insights on three perspectives to SLA formulation and associated practices. First, our results indicate that blanket performance guarantees for the entire customer organization may not be in the interests of both IT service providers and customer organizations, especially when demand is unpredictable. Second, our results demonstrate that dynamic priority pricing approach, even when not used as a congestion control tool, can yield socially superior results. Third, we find that alignment of interests between the supplier and customer organization depends on utilization rates and heterogeneity in service types; and finally, demand heterogeneity can be addressed effectively in a single vendor contractual arrangement through dynamic resource allocation mechanism such as the price-penalty scheme proposed in the paper. In essence, our work examines the system level characteristics that impact the performance of services agreements.

The remainder of the paper is organized as follows. In §2, we discuss issues and concepts for addressing demand heterogeneity as detailed in the extant literature. Section 3 describes the formal pricing model, welfare expressions, and resource requirements. In §4 we detail the design of the simulation experiment, results, and discussion. Concluding remarks and future research directions are presented in §5.

## 2. Related Work

Segmentation via differential pricing has long been proposed as a useful strategy to address heterogeneity in customer requirements. The practice of offering varying levels of service at different prices exists in many other service contexts (such as airlines, postal and cargo services, and utilities) as a mechanism of accommodating variations in user preferences and congestion control. A recent survey of pricing practices (Rehme 2006) in the service sector reveals that contracts written with a long-term view tend to have dynamic pricing arrangements.

Offering a priori quality guarantee implies commitment to a certain level of capacity (resource). Such commitment has significant economic implication for the provider, especially if demand variance is high. Congestion because of high demand has been found to cause dramatic performance degradation (Son and Kim 2004). Even temporary imbalance between capacity and demand has been shown to result in reduction in service standards and consequent loss in revenue (Oliva and Sterman 2001). As utility-oriented view towards IT services gains momentum, the need for appropriate pricing models as a mechanism for balancing the resource-quality tradeoff is being recognized as becoming imminent (Bhargava and Sundaresan 2004).

One of the earliest work in pricing and congestion control issues in service facilities characterized by customer queues brought the notion of delay costs in pricing computer services (Mendelson 1985). This work incorporated a microeconomic pricing approach to a single processor computing facility to investigate the effect of delay cost on price, capacity, and utilization within an organization. Mendelson’s model was later extended (Dewan and Mendelson 1990, Mendelson and Whang 1990) to derive an incentive compatible price for M/M/1 queues. In this model, socially optimal results were obtained when customers make a myopic decision to join a queue based on prices and expected waiting times. In a related model optimal pricing and capacity decisions for a service facility with nonlinear delay costs have also been investigated (Dewan and Mendelson 1990). In the context of multiple service class networks it has been shown that service specific pricing improves overall network performance and increases organizational utility (Cocchi et al. 1991). To accommodate delay sensitive user requests, (Gupta et al. 1996) presented a dynamic priority based pricing mechanism for adaptive resource allocation. This concept is further extended to a real time database context (Konana et al. 2000), where requests (queries) are serviced in accordance with individual preferences. More recently, Marbach (2004) has addressed bandwidth allocation to packets under a static pricing scheme using a single link fluid-flow approach. Both Marbach (2004) and Gupta et al. (1996) make important contributions to the literature in this context highlighting the usefulness of user-selected multiple priority queues and they also demonstrate the analytical complexities of multiple priorities.

Price and resource allocation related research has taken place in different IT service contexts (Bhargava and Sun 2005, Cheng and Koehler 2003, Keon and Anandalingam 2003, Maglaras and Zeevi 2005). Cheng and Koehler (2003) develop a two-part pricing scheme for application service providers (ASP) for optimal resource allocation. This model is applicable for single quality level for one particular service. Multiple quality guarantee and corresponding prices in telecommunication services context has been developed (Keon and Anandalingam 2003). In this model users are prespecified into different classes based on the application type (e.g., voice, data) and the resources are not shared among the different service classes. A similar concept is used (Maglaras and Zeevi 2005), where level of service is divided into two categories—guaranteed and best-effort. Residual capacity from the guaranteed category is used in the lower level best-effort service. Although the Maglaras and Zeevi (2005) model does not exactly fit our service set-up (all services are guaranteed, although at different priorities), it provides two significant findings; first, optimal operational regime is close to heavy traffic, second, real time congestion notification results in increased revenues. Bhargava and Sun (2005) propose a performance contingent pricing for broadband network services and advocate customer segmentation by offering differing performance guarantees.

This research closely follows the lead of Konana et al. (2000) and Gupta et al. (1996), with some important distinctions. We focus on an interorganizational context where customer balking is not a desirable outcome. Given this, and the nonzero delay costs experienced by customers, we require that all service requests enter the system. This places a slightly increased level of system load than could be expected in the contexts studied in Gupta et al. (1996) and (Konana et al. 2000). More important, such an arrangement may lead to potential misalignment of interests between the provider and the customer. The setting therefore necessitates the investigation of the relative impacts of fixed and dynamic pricing approaches to the two organizations and as well as to the system welfare. In addition, our work involves comparing the proposed dynamic price-penalty scheme to the current practice of single quality level SLAs. By doing so, we establish equivalence conditions when participants are indifferent between our proposed approach to SLA formulation and current industry practice. This equivalence condition is used in evaluating the effectiveness of our model in comparison to single-quality guarantee SLAs. We implement both multiple service types and multiple priority classes in an (M/M/n) queue discipline where priorities are not prespecified for different service categories. We also extend the setting by incorporating nonstationary demand patterns. Because such demand patterns cause wide variations in service performance, it enables us to examine the effectiveness of the proposed dynamic scheme under more extreme conditions. Finally, although our model is constructed for a stylized IT service environment, the results and the corresponding implications for formulating dynamic price-penalty schemes and determining necessary cross-subsidies for creating a winwin situation is applicable to many other service contexts with similar requirements.

## 3. Research Model

The pricing scheme developed in this paper is applicable to scenarios where service request arise from normal day-to-day operations within an organization. Specifically, the setting here is for support and management of IT Infrastructure services such as software installation requests, individual computer configuration requests, and troubleshooting. Customer requests for those services are placed in queue and are served in the order they arrive (traditional fixed price scheme) or according to the user’s perceived level of urgency (proposed dynamic priority based scheme). Providers allocate certain number of human resources to the customer organization based on the latter’s demand estimate. Provider’s cost for servicing a request is proportional to the time a resource spends on servicing the request, and unutilized resources are not considered. This is a reasonable assumption because in many service settings providers can use any idle time of the resources in servicing other customer organizations. We start with a fixed-price scheme in a single service context under stationary distribution assumptions, and extend it to a multiple service context and derive the equivalency condition between dynamic and fixed-price schemes. We then relax the stationary distribution assumption of the analytical model (along with a number of other restrictions) for extending and implementing the model in a discrete event simulation setting.

In a fixed-price scheme, the provider states the price and quality level for each of the services rendered. The quality guarantee for a particular service pertains to the entire organization. The performance record of the provider as such is an average value across all users in the organization and can be evaluated on a periodic basic.

To maintain analytical tractability, we make few simplifying assumptions. We assume Poisson arrival process for service requests and an exponential service time (a standard assumption in queuing models). We make no distinction between the human resources in terms of their skills to serve a request, i.e., we assume that each of the servers can serve any request equally efficiently. Also, the requests do not require any intermediate step to be taken by different resources; one request is served by one human resource.

## Notations Used:

i: index to represent a user

$j \colon$ index to represent a service type

$k \colon$ index to represent a priority class

$S _ { \mathrm { F P _ { j } } } \mathrm { : }$ service price (fixed-price scheme) for service type j

$R \colon$ revenue (dynamic scheme) from servicing a request

$S _ { j k } \mathrm { : }$ service price (dynamic scheme) for service type j in priority class k

$P _ { j k } \colon$ penalty (dynamic scheme) for service type j in priority class k for each unit time delay

$\mu _ { j } \colon$ mean service rate for service type j

$\delta _ { i j } .$ delay cost of user i for service type j (	¯ is the expected delay cost over all users)

$\lambda _ { j } \colon$ arrival rate of requests in service type j (fixed-price scheme) $\begin{array} { r } { ( = \lambda _ { j } = \sum _ { k } \lambda _ { j k } ) } \end{array}$

$\lambda _ { j k } \mathrm { : }$ arrival rate of requests in service type j in priority class k

$U _ { i } { \mathrm { : } }$ user utility

$\overline { { \omega } } _ { j k } \mathrm { : \Omega }$ mean waiting time in service type j priority class k

$\bar { \omega } _ { k } \mathrm { : }$ mean waiting time in priority class k

n: number of resources in the system

C: cost per resource per unit time

L: service level as specified in the SLA

T : the maximum allowable time to service a request (From the time the request is made to the time of completion of the request)

$W _ { q } ( 0 )$ : probability that a customer will spend 0 time in the queue

: provider’s total profit from the services agreement

## 3.1. Fixed-Price Model

In deriving the resource requirements the expressions are presented in a single-service setting. For multiple service systems, the entire service system is considered as a composite queue with three different service rates to determine the total number of resources.

In the context of support and management services, it can be reasonably stated that timeliness is a major determinant of performance. The customer might ask the provider to complete each request in a particular service category within a specified time limit, depending on the complexity of the service request. A service level of 95% implies that this condition is to be met for at least 95% of all the requests.

3.1.1. Resource Requirements. In the fixed price model customers are served on first-come-first-serve (FCFS) basis. Hence, we apply the M/M/n queuing discipline to determine the required number of resources from this model.

Because the price and the expected service level are already agreed upon between the customer and the provider, the provider’s aim is to maximize profit subject to meeting the expected service level. This implies that the probability of serving each request within the maximum allowable time limit must be greater than or equal to the target specified in the SLA.

Formally,

$$
p (t <   T) \geq L.\tag{1}
$$

The probability density function of the total waiting time for an $\mathbf { M } / \mathbf { M } / \mathbf { n }$ queue is given by Gross and Harris (1998)

$$
w (t) = \frac {\mu e ^ {- \mu t} (\lambda - n \mu + W _ {q} (0)) - (1 - W _ {q} (0)) (\lambda - n \mu) \mu e ^ {- (n \mu - \lambda) t}}{(\lambda - (n - 1) \mu)}.
$$

For an optimal or near optimal design the probability that a customer has zero waiting time is very small. Hence, we ignore the $W _ { q } ( 0 )$ term in wt. Therefore,

$$
\begin{array}{l} p (t <   T) = \int_ {0} ^ {T} w (t) d t \\ \qquad = \frac {\mu (\lambda - n \mu)}{(\lambda - (n - 1) \mu)} \\ \qquad \cdot \bigg [ \frac {1}{(n \mu - \lambda)} (e ^ {- (n \mu - \lambda) T} - 1) - \frac {1}{\mu} (e ^ {- \mu T} - 1) \bigg ]. \end{array}
$$

Note that for given values of arrival and service rate this probability value depends only on $n ,$ the staffing level. Because the mean service rate $\mu$ is known to the provider (assuming homogeneous resources) for a particular type of service, the provider optimally chooses n from the estimated arrival rate for given values of  and $\mu$ . Hence, Equation (1) becomes

$$
\begin{array}{l} L = \frac {\mu (\lambda - n \mu)}{(\lambda - (n - 1) \mu)} \\ \qquad \cdot \bigg [ \frac {1}{(n \mu - \lambda)} (e ^ {- (n \mu - \lambda) T} - 1) - \frac {1}{\mu} (e ^ {- \mu T} - 1) \bigg ]. \end{array}\tag{1a}
$$

Solution of 1a provides us the value of $n ,$ the number of resources assigned to the customer in the fixed price scheme. Because the fixed price scheme is the baseline for our comparison, the dynamic scheme would use the same number of resources.

3.2. Dynamic Pricing Scheme Based on Priorities We denote the IT services by a set $( j = 1 , 2 , \ldots , J )$ Different service types $( j )$ are associated with varying levels of complexity, $\mathrm { e . g . , }$ a software installation request could be less complex and less time consuming compared to a configuration management request. The processing time for a particular service $( 1 / \mu _ { j } )$ is a characteristic of the service; more complex services require higher processing times.

We have previously argued different users or user groups $( i = 1 , 2 , \dots , I )$ may exist within an organization, and may belong to different levels in the organizational hierarchy, and $. / \mathrm { o r }$ different functional units. To accommodate these differences in user preferences, the proposed dynamic scheme allows $\mathrm { { u s e r s } } ^ { 2 }$ to choose specific priority level for the request. The provider’s performance is evaluated based on the context (userassigned priority) of the request. Such prioritization of requests would require price-differentiation among the priority classes; in the absence of such differentiation, all users would opt for the highest priority. As such, the price a user pays for a particular request is based on the service type and the economic significance of the request to the user. The latter is captured by offering the user with a menu of price-priority choices $( k = 1 , 2 , \ldots , K ) ^ { 3 }$ for any service request.

Literature in queuing theory has demonstrated the negative externality costs (Haviv and Ritov 1998,

Mendelson 1985, Nadiminti et al. 2002) that customers waiting in a queue impose on other customers. Each arriving customer incurs a cost per unit time until their request is fulfilled. The cost is a function of the perceived urgency of the request to the user at the time of placing the request—delay-cost/time $( \delta _ { i j } )$ models demand heterogeneity arising from user preference variance. As the value of the delay-cost/time varies from one user to other, it provides the rationale for users to choose between priority classes.

In the proposed priority pricing scheme, userassigned priority level of a particular service determines the order in which it is served. The prices for different services in each priority class are based on the level of congestion in the system at the time of arrival of the request. User’s selection of priority level is a function of the waiting time estimate by the provider as well as their individual valuation of the service request. To alleviate the possibility that the provider may report inflated waiting times to induce the customers to choose higher priorities, we have introduced a penalty for delay in servicing a request. The penalty term acts as a disincentive for opportunistic behavior. Incentives of this type has been shown to be effective in prior literature (Raghu et al. 2003).

Given a fixed number of resources (derived from the fixed-price model), the price should correspond to the demand. This implies that the prices need to be set dynamically depending on the congestion in the system. Given the resource level, the provider gives an estimate of the waiting time for each service in each priority class, and the price S and penalty P are derived based on the estimate of waiting $\mathrm { t i m e ^ { 4 } }$ (details about how these values are set are provided in §3.3.3).

In essence, this setting corresponds to an alternative form of SLA formulation that differs from the fixed-price ones in two important aspects: the SLA is defined at the individual transactional level and, given the number of resources; the SLAs can adjust to volume/waiting time.

3.2.1. Dynamic Pricing Scheme. As discussed above, the price structure for a service in a priority class includes a price and a penalty,

$$
R _ {j k} = S _ {j k} - P _ {j k} * \bar {\omega} _ {j k}.\tag{2}
$$

where,

$$
P _ {j k} > 0, \quad \text { and } \quad P _ {j k} > P _ {j k ^ {\prime}} \quad \text { for   } k <   k ^ {\prime}.
$$

$S _ { j k }$ denotes the price of the service in a particular priority class if the request is served immediately upon arrival and $P _ { j k }$ denotes the penalty per unit time for not serving a request as soon as it is logged. The justification for the linear penalty scheme comes from the proven effectiveness in preventing opportunistic behavior in agency-settings (Holmstrom and Milgrom 1987). The amount of penalty corresponds to the priority class- higher the penalty, greater is the penalty per unit time. This design ensures that requests with higher priority are served earlier (Gross and Harris 1998). Penalty prices depend on a number of service system related properties including arrival and service rates; a detailed discussion of penalty price determination is provided in §3.3.3.

3.2.2. User’s Decision Function. We assume that individual users in the customer organization behave rationally, i.e., individuals maximize their utility while placing a request as they choose the priority class that matches their reservation price for the service and waiting time. This utility is captured by the total cost for the payment of the service and the delay cost incurred in waiting in the system. Formally,

$$
\underset {k} {\mathrm{Max}} u _ {i} (j, k) = - (S _ {j k} - P _ {j k} \overline {{\omega}} _ {j k}) - \delta_ {i j} \overline {{\omega}} _ {j k}.\tag{3}
$$

Note that the user’s choice of k depends on two factors. The individual delay cost $\delta _ { i j } ,$ and congestion in the system.

3.2.3. Service Provider’s Decision Function. With a fixed number of resources, the service provider’s objective is to maximize its profit over the decision period in which $S _ { j k }$ and $P _ { j k }$ remain constant. The cost $( C _ { j } = C / \mu _ { j } )$ incurred by the provider in servicing a request is a function of the service rate $\mu _ { j }$ . Because the providers may use any unused portion of their resources, only the variable portion of the resource cost is used in allocating resource costs to different services and priority classes. Allocating any unutilized portion of the resource costs to $S _ { j k }$ is also not practicable as it is not possible to predict a priori how the unutilized resource could possibly have been distributed among the different requests if more were to come. The provider’s decision problem can be represented as a profit maximizing problem as shown below:

$$
\begin{array}{l} \pi (S, P) = \sum_ {j} \sum_ {k} [ (S _ {j k} - P _ {j k} \bar {\omega} _ {j k}) ] \lambda_ {j k} \\ \qquad - \sum_ {j} \frac {C}{\mu_ {j}} \sum_ {k} \lambda_ {j k} \quad \left(\text { since } \lambda_ {j} = \sum_ {k} \lambda_ {j k}\right). \end{array}\tag{4}
$$

To maintain analytical tractability, we assume penalty to be fixed and solve for the price. Solving the optimization problem yields the following equation for the price:

$$
S _ {j k} = C _ {j} + P _ {j k} \bar {\omega} _ {j k} + \sum_ {j = 1} ^ {J} \sum_ {n = k} ^ {K} \bar {\omega} _ {j n} ^ {\prime} \lambda_ {j n} P _ {j n}.\tag{5}
$$

Equation (5) provides an expression for the pricepenalty relationship for a service in a given priority class. The arrival of a service in a higher priority class imposes a delay on requests in all other lower priority classes, as well as on other services in the same priority class $\begin{array} { r } { ( \sum _ { j = 1 } ^ { J } \sum _ { n = k } ^ { K } \bar { \omega } _ { j n } ^ { \prime } \lambda _ { j n } P _ { j n } ) } \end{array}$ . In other words, the price for a higher priority request incorporates the delay costs it is imposing on all lower priority ones. The optimal value of the price $( S _ { j k } )$ of a service in a priority class is the sum of the cost of the service, expected penalty to be paid based on the estimated waiting time, and the delay cost it is imposing on all other services. As the arrival rate and the waiting time decreases, the price of the service decreases. This implies that in low demand situations customers get a higher quality of service. At the limit, when the arrival rate is zero, the penalty is highest, i.e., there is no room for delay—the results (Equation (5)) show that the slope of the price function becomes indeterminate. On the other hand, as the arrival rate (and hence the waiting time) increases, the price increases, i.e., the providers are not penalized for any deviation from the agreed-upon service level caused by underestimated traffic. The dynamic pricing scheme thus acts as a resource allocation mechanism by adjusting prices according to demand when resource levels are fixed.

## 3.3. Provider and Customer Welfare in the Dynamic and Fixed-Price Models

The effectiveness of the proposed dynamic priority pricing scheme in comparison to the traditional fixed pricing scheme is measured in terms of the economic welfares of the customer and the provider organizations. In this section we drop the subscript j as we derive the expressions in a single-service setting. Welfare expressions for the multiple-service setting are obtained by summing over all the services.

3.3.1. Provider Welfare. Provider’s welfare in the dynamic as well as the fixed price scheme is modeled as the total profit from the service arrangement. In both pricing schemes $( C / \mu )$ represents the average cost of servicing a request. For the fixed-price scheme the revenue from a request is simply the subscription price, while for the dynamic scheme the revenue equals the price less the penalty paid to the customer. Hence the provider welfare expressions in the fixed and dynamic price settings are, respectively

$$
W _ {p _ {\mathrm{FP}}} = S _ {\mathrm{FP}} - (C / \mu) \lambda ,\tag{6a}
$$

$$
W _ {p _ {\text { dynamic }}} (S, P, \lambda) = \sum_ {k} [ (S _ {k} - P _ {k} \bar {\omega} _ {k}) ] \lambda_ {k} - (C / \mu) \sum_ {k} \lambda_ {k},
$$

$$
\text { where } \lambda = \sum_ {k} \lambda_ {k}.\tag{6b}
$$

3.3.2. Customer Welfare. Customer welfare in both schemes is modeled as the cost incurred by the users through payments for services and expected value of individual delay cost 	¯ spent in waiting for service delivery. Using the mean waiting time (   , the total cost incurred by all users in the system is given by $\lambda \bar { \delta } \bar { \omega } .$ . Hence the customer welfare expressions in the fixed-price and dynamic-price scenarios are, respectively,

$$
\begin{array}{c} {W _ {\mathrm {cust_ {FP}}} = - S _ {\mathrm{FP}} - \lambda \bar {\delta} \overline {{\omega}},} \\ {W _ {\mathrm {cust_ {dynamic}}} = \sum_ {k} (- S _ {k} + P _ {k} \overline {{\omega}} _ {k} - \bar {\delta} _ {k} \overline {{\omega}} _ {k}) \lambda_ {k},} \end{array}\tag{7a}
$$

$$
\text { where } \lambda = \sum_ {k} \lambda_ {k}.\tag{7b}
$$

3.3.3. Welfare Comparison and Initial Prices for the Dynamic Scheme. A comparison between the two systems would be meaningful, if essential parameters (i.e., the arrival and service rates, number of resources) remain identical. We derive the equivalence condition that makes both customer and provider indifferent between fixed and dynamic pricing scenarios. Because we use the fixed-price scheme as the baseline for our comparison (resource requirement comes from this scheme), the starting values of the dynamic prices of a particular service are based on the corresponding fixed price values obtained from this equivalence condition.

It is possible to derive the equivalence condition collectively for all the priority classes only when estimates of delay cost distribution within each priority class are available. This implies that there may be multiple solutions for the priority prices (penalties) based on a priori estimate of delay cost distributions. For analytical convenience we derive the equivalence relation for each priority class separately. We assume the fixed subscription price to be reflective of the expected delay cost 	¯ over all users, and derive the equivalence relationship for the priority class in the middle based on this fixed-price. Next, we use this result to set the initial prices for the other priority classes (for details please see §B of the supplementary material<sup>5</sup>). Essentially, we derive the prices such that the middle priority class receives the same level of service as in the fixed price scenario, under the assumption that all requests belong only to the middle class. Because we derive the equivalence condition for each priority class separately, we drop the subscript k from Equations (6b) and (7b). For a dynamic scheme with no priority classes, the average waiting time is the same as the fixed price case (the arrival and service rates are same, too). Using Equations (7a), (7b) (or (6a), (6b); both will yield same result) and the price-penalty relationship in Equation (5), we obtain the following condition for price at which the customer and provider are indifferent between dynamic and fixed pricing schemes—

$$
P = \frac {1}{\lambda^ {2} \overline {{\omega}} ^ {\prime}} (S _ {\mathrm{FP}} - C (\lambda / \mu))\tag{8}
$$

The term $\left( C ( \lambda / \mu ) \right)$ on the right hand side of Equation (8) represents the total cost for resources used. Penalty for service delays should depend on the arrival rate and resulting waiting time changes in the system. Given the penalty, the price for service provisioning can be determined from Equation (5). The price and penalty values, thus obtained, are used as the starting point in the simulation experiments. The price is updated every week, based on past arrival data (this is discussed in detail in §4.2 and Figure 2).<sup>6</sup>

Mean Waiting Time. Mean waiting time $( \overline { { \omega } } _ { j k } )$ estimates are required to compute the values for $S _ { j k }$ . For a single service $( J = 1 )$ queue, this waiting time in priority class k is given by Gross and Harris (1998),

$$
\Rightarrow \bar {\omega} _ {k} = \frac {1}{\left(1 - \sum_ {i = 1} ^ {k} \alpha_ {i}\right) \left(1 - \sum_ {i = 1} ^ {k - 1} \alpha_ {i}\right)} \bar {\omega} _ {0},\tag{9}
$$

where

$$
\alpha_ {I} = \frac {\lambda_ {I}}{n \mu}, \qquad \bar {\omega} _ {0} = \frac {P _ {0} (\lambda / \mu) ^ {n}}{n ! (1 - \lambda / n \mu) n \mu},
$$

$$
P _ {0} = \left[ \sum_ {l = 0} ^ {n - 1} \frac {1}{l !} \left(\frac {\lambda}{\mu}\right) ^ {l} + \frac {1}{n !} \left(\frac {\lambda}{\mu}\right) ^ {n} \frac {n \mu}{n \mu - \lambda} \right] ^ {- 1}, \quad \lambda = \sum_ {k} \lambda_ {k}.
$$

For a multiple-service scenario, the characteristics of our particular queuing system are—multiclass, multiserver queue with nonpreemptive priorities. Because of the inherently complex nature of priority queues, it leads to analytical intractability in some situations (Jewkes and Stanford 2003, Marbach 2004, Sleptchenko 2003, Stanford 1997, Wierman et al. 2003). In our system, service rate in a particular priority class is a complex function of the relative proportion of different service types in that priority class and all other higher priority classes, thus making a closed form solution infeasible. At this stage, the mean waiting time in a single-service setting is given by Equation (9) under assumptions of a stationary demand pattern. Mean waiting time estimation is necessary to get closed-form solution for prices. Given that closedform solutions for $\overline { { \omega } } _ { j k }$ in the multiple-service setting is not feasible (even under stationary demand patterns), we would need approximations. The approximations can affect the effectiveness of the dynamic scheme in an IT services setting. We develop a simulation setting that is based on the analytical approach outlined in this section to further investigate the performance of the dynamic pricing approach under nonstationary demand scenarios.

## 4. Computational Experiments and Results

Our computational approach compares performance under dynamic priority pricing scheme with the fixedprice scheme. We use the solution of the singleservice setting as an initial approximation (for details refer to $\ S \mathrm { A }$ of the supplementary material available at http://isr.pubs.informs.org/ecompanion.html). The computational model can highlight the implications of using dynamic congestion control and resource allocation practices in IT services.

The welfare Equations ((6a) and (6b); (7a) and (7b)) and the waiting time Equation (9) indicate the variables which would impact the performance of the service process. Clearly, arrival rate characteristic has significant impact on the pricing schedule, waiting time, (i.e., congestion level) and welfare. Demand heterogeneity in service types (and therefore service rates and user delay cost distributions) can impact the approximations in the pricing schedule for priority classes. We focus on service characteristics by first addressing welfare impacts of implementing dynamic pricing scheme. Demand uncertainty because of nonstationary arrival rate requires mechanisms for efficient resource allocation. We conjecture that the dynamic pricing scheme will allow for more efficient resource allocation under uncertain demand and therefore lead to welfare improvements over fixed price scheme for both customer and provider organization. Also, when multiple services are handled demand heterogeneity will add an additional layer of complexity to the system. We therefore surmise the dynamic pricing scheme’s impact to be more pronounced under this setting.

Level of congestion is an important factor in investigating performance of service systems based on queues. Different levels of congestion effectively translates to different levels of resource utilization, higher traffic implies higher resource utilization and vice-versa. Nonstationary demand patterns can cause such changes in congestion levels, especially because resource requirements to deliver a particular level of service are predetermined based on customer organization’s estimate of average demand. At higher traffic, as users with varying quality preferences compete for resources, the prioritization scheme in dynamic pricing would cater to them in a more effective way than fixed-price scheme which treats each user equally. The provider benefits from the ability to price differentiate and from increased revenues at higher traffic. Also, with high utilization rate comes the possibility of performance degradation (Son and Kim 2004). While we believe that the customer would benefit from prioritization, benefits from the dynamic scheme would likely reduce at higher congestion levels. The providers will be better off with increasingly higher utilization as it will generate more revenue.

Finally, we investigate the operational performance impact of the dynamic pricing scheme (i.e., waiting times). For the same arrival rate pattern, we expect the fixed price scheme (which uses a FCFS discipline) to yield better waiting time performance overall when compared to that of the dynamic pricing scheme (which can lead to high waiting times for low priority services). Because of the differences in delay cost for individual requests, we assert that the superior operational characteristic of the fixed price scheme will not translate to better financial outcome for either the customer or provider organization.

## 4.1. Design of Simulation Experiments

Simulation experiments allow for strong internal validity because we can control the experimental conditions through multiple replications. While we can build stronger results through stringent internal controls, external validity (i.e., whether the model is a justifiable abstraction of a real-life setting) is potentially a concern. To mitigate external validity concerns, we used data from an outsourcing arrangement between a prominent service provider and a large public organization in setting parameters like arrival patterns, service levels, and service rates. This outsourcing arrangement in turn conforms to the general SLA specification guidelines (Open Group 2004) of the industry. The data pertains to 3-year performance record of the provider available from help-desk logs. This log provides detailed information about the request start and closure time, resource assignment, steps taken to resolve a request, and userassigned urgency for a number of services. These data provided the basis for selecting a range of arrival and service rates in our simulation set up. Price parameters in the study are based on price information from this same contract. From the service related data set, we chose three services—password reset, desktop upgrades, and video and telecomm services—as representative services with varying demand and quality requirements. The service rates and arrival patterns of these services were used as the basis for simulation experiments.

Refocusing our attention on internal validity, we first checked whether expected quality levels are indeed achieved with the number of resources derived from our model. Next, for the priority-pricing scheme with multiple services, we first ran the system without any pricing mechanism to check whether the predicted (using our heuristic, explained in §A of the supplementary material available at http://isr.pubs. informs.org/ecompanion.html.) and actual values of waiting times are close (usually within 5% of the predicted value). We further tested this assumption in the final simulation setup as well. Finally, in each replication, same random number seeds are used for both dynamic and fixed price scenarios to generate arrival, service, and delay cost to facilitate comparison across scenarios.

We compare the two alternative pricing schemes by tracking customer and provider welfare in terms of cost and profit respectively and evaluate performance (in terms of average waiting time) under varying levels of congestion and different demand patterns. The factors in the experiment are (Panel A, Table 1)— arrival pattern (stationary versus nonstationary), congestion level (resource utilization), and pricing scheme (dynamic and fixed). Heterogeneity is introduced by using different customer profiles with different delaycost distributions.

We use four nonstationary demand patterns and one stationary arrival pattern (because our interests primarily relate to time-varying demand, there are more nonstationary scenarios; we use the stationary scenario as a baseline case). The four nonstationary demand patterns represent four varying levels of congestion, and associated resource utilization. Figure 1 provides a sample stationary versus nonstationary demand pattern. The nonstationary demand pattern represents widely fluctuating demand, as observed in many related scenarios (e.g., Paich and Sterman 1993). We investigate the four nonstationary arrival patterns with expected utilization rates at about 75%, 80%, 85%, and 90%. The simulation experiments consist of five scenarios—one stationary arrival and four nonstationary arrivals. Each of the four nonstationary arrival scenarios represents different utilization rates. Within each scenario, we evaluate customer welfare (cost), provider welfare (profit), and waiting time under fixed and dynamic pricing schemes. Panel B of Table 1 presents the design structure of the simulation experiments.

Table 1 Experimental Factors and Design

<table><tr><td colspan="2">Panel A</td></tr><tr><td>Experimental factors</td><td>Operationalized as</td></tr><tr><td>Arrival pattern</td><td>Stationary, nonstationary</td></tr><tr><td>Congestion level</td><td>Resource utilization (four levels)</td></tr><tr><td>Pricing scheme</td><td>Dynamic, fixed</td></tr><tr><td>User preference</td><td>User delay cost distribution (3 profiles)</td></tr><tr><td colspan="2">Panel B</td></tr><tr><td colspan="2">Dependent variablesProvider welfare (profit) and customer welfare (cost)</td></tr><tr><td colspan="2">Independent variablesStationary arrival (utilization rate: 75%)Nonstationary arrival (utilization rates: 75%; 80%; 85%; 90%)</td></tr></table>

In the simulation experiments we used three customer profile types (low, medium, high) from a delay-cost perspective. Each profile represents customer population from different statistical distributions (we use normal distributions). These groups can be considered to be representative of various functional and/or operational organizational subunits, as discussed previously. It is assumed that users at the extreme end of the delay cost distribution, users with the lowest and highest delay costs have low arrival rates, and users with medium delay costs will make the majority of the requests.

Figure 1 A Sample Stationary vs. Nonstationary Arrival Scenario (Single-Service Setting)  
![](/api/attachments/23U6D2KP/fulltext/images/6f58dba153e6e22d7f5d0b2e3af43c6fd791bed3845a1243d9faf17f8842195b.jpg)

Figure 2 provides a conceptual overview of our simulation approach. The service facility is implemented in a discrete event simulation package (Simprocess). The dynamic pricing scheme requires periodic update of the prices based on past arrival rates. The pricegenerator module calculates the prices according to Equation (5) (Figure 3 provides details about the price setting process). This is a separate mathematical program (written in Maple) that takes inputs (past arrival rates) from Simprocess and sends output (prices) to the simulation program at the start of each interval. More details about each of the modules are provided in §B, supplementary material available at http://isr. pubs.informs.org/ecompanion.html.

Each of the simulation experiments is run for a sixmonth (26 weeks) time period with 50 replications for each experiment. For the dynamic scheme, prices are updated weekly based on arrival records in the past week (many variations in the demand pattern are the result of seasonality, and a week is a reasonable timeperiod to capture such variations).<sup>7</sup>

## 4.2. Results and Discussions

The results presented indicate the total welfare over a six-month period (averaged over all 50 replications). Customer welfare number represents the cost incurred, as such they are represented in negative values (refer to Equations (7a) and (7b)).

For single- and multiple-service settings, the procedures for parameter value selections are detailed in §B of supplementary material available at http:// isr.pubs.informs.org/ecompanion.html. Single-service parameters and welfare values are provided in Tables 2 and 3, respectively; multiple-service parameters and welfare values are provided in Tables 3 and 4, respectively. As mentioned previously estimated arrival rate  ), service rate , and the fixed-price $( S _ { \mathrm { F P } } )$ are based on real-life data. The dynamic scheme is implemented with three priority classes. Supplement A, available at http://isr.pubs. informs.org/ecompanion.html, provides the arrival rates used for each scenario.

Figure 2 Conceptual Overview of Simulation Program (for One Replication)  
![](/api/attachments/23U6D2KP/fulltext/images/5ee6d6b0fae83d15c867946ce23d69f30302cc5bd56038ea321475dc3ad1bdf3.jpg)

Single-Service Setting. This is a base case scenario with only one service type, referred to as Service A. In Table 3 we present the welfare values of the participants for each of the scenarios studied.<sup>8</sup>

Multiple-Service Setting. The multiple-services setting is modeled with three services, each with three priority classes. The resulting welfare values are presented in Table 5. This setting represents a higher degree of complexity with the three services varying significantly in terms of their service time, estimated arrival rates, and prices. The services are increasingly more complex (requiring more processing time) and more expensive<sup>9</sup> from A to C. Accordingly, volume of requests decreases from A to C.

Our discussions are mainly centered on the multiple-service setting as it is representative of a more realistic setting inclusive of heterogeneity. The single service and multiple-service results provided comparable results and we discuss the differences.

Single-Service Setting—Provider and customer organizations are always misaligned under the singleservice setting (see Table 3). Under stationary demand, dynamic pricing enhances customer welfare but diminishes provider welfare. In other words, when congestion controls are imposed under less demanding circumstances, the priorities and penalties end up benefiting the customer. Nonstationary demand enhances the attractiveness of dynamic pricing for the provider. However, the customer organization now prefers the fixed price scheme. Further interpretation of these results is possible when analyzed in conjunction with the multiple-service setting results (Table 5). We therefore revisit the single-service setting towards the end of this section.

Figure 3 Price Setting Process for the Entire Simulation Run (One Replication)  
![](/api/attachments/23U6D2KP/fulltext/images/ec4ee0e59d441d0ee1524fd114bd40658b6b41942c741f60efad2fcaee72448a.jpg)

Who benefits from the dynamic scheme? The most significant observation from our experiments is that the benefits accruing from the dynamic price-penalty scheme are unequally distributed between the participants in the service arrangement. The choice of dynamic over the fixed-price scheme is a function of both arrival pattern and system characteristics. Under nonstationary demand conditions, customers favor fixed pricing scheme under single-service setting, and prefer the dynamic scheme in the multiple-service setting (as seen in Table 5). Under stationary demand pattern, although the participants should have been indifferent theoretically, the apparent conflict of choice (for the customers) may arise from lack of user heterogeneity or demand fluctuations. The difference narrows for the multiple-services setting primarily because of the increase in user heterogeneity.

Interestingly, customer and provider welfares are aligned only under high-congestion levels in the multiple-services setting.<sup>11</sup> These results highlight the significant role that resource utilization plays in service provisioning. Clearly, resource utilization affects customer and provider organizations in opposing directions-providers benefit more from increasing resource utilization while customer’s benefit reduce. In other words, the results demonstrate that underestimating demand would adversely impact customer organization through reduced level of service while the provider organization benefits through higher prices for services.

Operational Performance. In the fixed-price scheme the operational performance is better than in the dynamic scheme (refer to Tables 6(a) and 6(b)). Priority 1 requests in the dynamic scheme receive a higher level of service (less average waiting time)<sup>12</sup> than in the fixed-price scheme, whereas both priority 2 and 3 requests receive lower service levels than in fixed-price. The stochastic nature of the system makes it is infeasible to accurately predict waiting times for the next period and the dynamic scheme introduces some uncertainty via errors in waiting time estimates. Estimation errors have a greater impact on lowerpriority users, especially with increasing utilization rate—higher utilization rates are typically associated with lower operational performance. In this situation, as long as the total gain in the customer organization from having customized service outweighs the loss from having lower service levels for some users, the dynamic scheme can be considered more beneficial for the customer. This explains the reason for customer welfare increase under dynamic pricing scheme in multiple-service settings (especially under nonstationary demand pattern). In summary, the results imply that lower priority classes would have proportionately higher rate of performance degradation as volumeprice adjustments are made.

Table 2 Simulation Parameters: Single Service (Service A)

<table><tr><td>Service rate (μ): 8.0/hr;service level (L): 95%Estimated arrival rate* (λ): 12.0/hrNo of resources required (n): 2Fixed SLA price ( $S_{FP}$ )**:$1,048,320.00 for 6 months</td><td>Resource cost/unit time (C): $100.00Penalties: Priority 1: $20.40/hr;Priority 2: $10.20/hr;Priority 3: $5.10/hrMaximum time allowed for completing a service (T): 1hr</td></tr></table>

∗Required for estimating the level of resource.  
∗∗This is equivalent to charging \$20/request, based on the arrival rate estimate (12/hr for 26 weeks).

Welfare Implications. Customer’s choice of dynamic versus fixed-price schemes is guided by the operational performance of the system. On the other hand, the provider’s choice is impacted by the effectiveness of the resource allocation mechanism, i.e., pricing appropriate for the congestion level and user population.

The sensitivity of waiting-time (and by association, price) to volume in the dynamic scheme, as discussed previously, can impact the effectiveness of provider’s resource allocation mechanism under stationary versus nonstationary demand. The provider prefers fixed-price scheme for stationary, predictable, demand patterns as the dynamic scheme may introduce additional uncertainties via frequent waiting time updates. Nonstationary demand, on the other hand, justifies the dynamic-scheme for the provider (except for two anomalous cases in multiple-service setting). Variable pricing acts as a resource allocation mechanism and compensates for any performance deviations arising from random changes in the system. Thus, provider benefits more from increasing resource utilization (higher traffic).

Because customers’ preference depends on operational performance, they incur increasingly higher costs with higher resource utilization, and associated performance degradation. User heterogeneity plays an important role in this situation. In multiple-service settings, resources are shared among services with considerably varying characteristics (processing time, volume). As users compete for resources they gain from personalized services and can receive a better match of service level with their delay cost attribute.

Under nonstationary demand, mean waiting time changes over time and is a function of the total arrivals in the system and arrivals in each priority class (and it varies with each service type in a multiple service system). Several options are possible on how waiting times are communicated to the user—historical waiting times; or moving average of waiting times; or waiting time estimate based on the queue status at the time of the service request. Each of these possibilities can be simulated in our model. We used the most accurate of the above options, i.e., the waiting time estimate based on the queue lengths at the time of service request. Even this estimate can be inaccurate, especially for low-priority requests, if high priority requests arrive subsequent to the request. We gauge the effect of such inaccuracies in estimating waiting times (and subsequently prices). We recorded the actual versus the estimated waiting times for each service in each priority class. Overall, we observed that the actual waiting time closely follows the predicted value.

Table 3 Provider and Customer Welfare in the Single-Service Setting

<table><tr><td rowspan="2">Arrival pattern</td><td rowspan="2">Utilization on rate (%)</td><td rowspan="2">Pricing scheme</td><td colspan="3">Provider welfare (profit) in ‘000</td><td colspan="3">Customer welfare (cost) in ‘000</td><td rowspan="2">Total system welfare in ‘000 ($)</td><td colspan="2">Subsidy may be provided to</td></tr><tr><td>Avg. ($)</td><td>Std. dev.</td><td>Percentage of change from fixed-price scheme</td><td>Avg. ($)</td><td>Std. dev.</td><td>Percentage of change from fixed-price scheme</td><td>Provider ($)</td><td>Customer ($)</td></tr><tr><td rowspan="4">Stationary</td><td rowspan="2">74.81</td><td>Dynamic</td><td>282</td><td>6</td><td>-27.88**</td><td>-1,161</td><td>6</td><td>-10.57**</td><td>-879</td><td>28</td><td>—</td></tr><tr><td>Fixed</td><td>391</td><td>4</td><td></td><td>-1,298</td><td>7</td><td></td><td>-907</td><td></td><td></td></tr><tr><td rowspan="2">76.59</td><td>Dynamic</td><td>422</td><td>61</td><td>10.93**</td><td>-1,424</td><td>70</td><td>2.13**</td><td>-1,002</td><td>—</td><td>30</td></tr><tr><td>Fixed</td><td>380</td><td>4</td><td></td><td>-1,395</td><td>28</td><td></td><td>-1,014</td><td></td><td></td></tr><tr><td rowspan="6">Nonstationary</td><td rowspan="2">79.67</td><td>Dynamic</td><td>600</td><td>110</td><td>69.41**</td><td>-1,660</td><td>122</td><td>16.24**</td><td>-1,060</td><td>—</td><td>232</td></tr><tr><td>Fixed</td><td>355</td><td>3</td><td></td><td>-1,428</td><td>21</td><td></td><td>-1,074</td><td></td><td></td></tr><tr><td rowspan="2">85.79</td><td>Dynamic</td><td>1,318</td><td>195</td><td>348.16**</td><td>-2,609</td><td>216</td><td>61.28**</td><td>-1,290</td><td>—</td><td>992</td></tr><tr><td>Fixed</td><td>294</td><td>5</td><td></td><td>-1,617</td><td>37</td><td></td><td>-1,323</td><td></td><td></td></tr><tr><td rowspan="2">87.50</td><td>Dynamic</td><td>3,878</td><td>1,998</td><td>1,218.2**</td><td>-5,307</td><td>1,989</td><td>203.82*</td><td>-1,429</td><td>—</td><td>3,560</td></tr><tr><td>Fixed</td><td>282</td><td>5</td><td></td><td>-1,747</td><td>39</td><td></td><td>-1,465</td><td></td><td></td></tr></table>

∗∗Significant at p < 0 05.

Table 4 Simulation Parameters: Multiple Service

<table><tr><td>Service A</td><td>Service B</td><td>Service C</td></tr><tr><td>Service rate ( $\mu$ ): 8.0/hrEstimated arrival rate ( $\lambda_{A}$ ): 16.0/hrFixed SLA price ( $S_{FP_{A}}$ ): $1,397,760.00 for 6 monthsMaximum time allowed completing a service ( $T_{A}$ ): 1 hrPenalties:Priority 1: $6.72/hrPriority 2: $3.36/hrPriority 3: $1.68/hrService level (L): 95%Resource cost/unit time (C): $100.00Total number of resources required (n): 7</td><td>Service rate ( $\mu$ ): 4.0/hrEstimated arrival rate ( $\lambda_{B}$ ): 8.0/hrFixed SLA price ( $S_{FP_{B}}$ ): $1,397,760.00 for 6 monthsMaximum time allowed completing a service ( $T_{B}$ ): 4 hrPenalties:Priority 1: $6.72/hrPriority 2: $3.36/hrPriority 3: $1.68/hr</td><td>Service rate ( $\mu$ ): 1.0/hrEstimated arrival rate ( $\lambda_{C}$ ): 2.0/hrFixed SLA price ( $S_{FP_{C}}$ ): $1,397,760.00 for 6 monthsMaximum time allowed completing a service ( $T_{C}$ ): 8 hrPenalties:Priority 1: $6.72/hrPriority 2: $3.36/hrPriority 3: $1.68/hr</td></tr></table>

Side Payments to Induce Preference Alignment. The total system welfare is significantly greater under the dynamic pricing scheme. The provider and customer preferences for the pricing schemes are in most cases, however, not aligned. The unequal distribution of benefits among the participants suggests a possible redistribution of benefits to make participants indifferent between the choices. For example, at 85% resource utilization (single-service), the provider can pay back the customer \$991 K =\$2609 − 1617; the excess cost the customer incurs in the dynamic scheme) to make the latter indifferent between the two pricing schemes. The provider would still make \$32 K =\$1024 − \$992; the gain in the dynamic scheme over fixed price—the subsidy paid to the provider) more than in the fixed-price scheme. This redistribution possibility exists for all nonstationary arrivals in the single-service setting. It seems then the apparent conflicts in preference can be resolved if certain pay-back provisions are considered. The rationale for this argument is the fact that the dynamic prioritybased pricing scheme equips the provider with better resource allocation capabilities by matching individual users with their own service level requirements. Higher the resource utilization, indicating congestion, greater is the provider’s benefit from having such capabilities. If the providers are willing to pass off some of their realized benefits to the customers, the dynamic approaches to service provisioning can be more effectively implemented.

Table 5 Provider and Customer Welfare in the Multiple-Service Setting

<table><tr><td rowspan="2">Arrival pattern</td><td rowspan="2">Utilization rate</td><td rowspan="2">Pricing scheme</td><td colspan="3">Provider welfare (profit) in ‘000</td><td colspan="3">Customer welfare (cost) in ‘000</td><td rowspan="2">Total system welfare in ‘000 ($)</td><td colspan="2">Subsidy may be provided to</td></tr><tr><td>Avg. ($)</td><td>Std. dev.</td><td>Percentage of change from fixed-price scheme</td><td>Avg. ($)</td><td>Std. dev.</td><td>Percentage of change from fixed-price scheme</td><td>Provider ($)</td><td>Customer</td></tr><tr><td rowspan="2">Stationary</td><td rowspan="2">85.31</td><td>Dynamic</td><td>1,569</td><td>16</td><td>-0.47</td><td>-5,877</td><td>58</td><td>-10.28**</td><td>-4,308</td><td>8</td><td>—</td></tr><tr><td>Fixed</td><td>1,575</td><td>2</td><td></td><td>-6,550</td><td>9</td><td></td><td>-4,975</td><td></td><td></td></tr><tr><td rowspan="8">Nonstationary</td><td rowspan="2">76.19</td><td>Dynamic</td><td>476</td><td>53</td><td>-74.52**</td><td>-4,165</td><td>84</td><td>-28.92**</td><td>-3,689</td><td>1,393</td><td>—</td></tr><tr><td>Fixed</td><td>1,869</td><td>3</td><td></td><td>-5,860</td><td>12</td><td></td><td>-3,991</td><td></td><td></td></tr><tr><td rowspan="2">81.83</td><td>Dynamic</td><td>1,155</td><td>89</td><td>-32.51**</td><td>-5,455</td><td>214</td><td>-12.51**</td><td>-4,300</td><td>556</td><td>—</td></tr><tr><td>Fixed</td><td>1,711</td><td>1</td><td></td><td>-6,235</td><td>8</td><td></td><td>-4,524</td><td></td><td></td></tr><tr><td rowspan="2">86.18</td><td>Dynamic</td><td>2,430</td><td>477</td><td>52.84**</td><td>-6,596</td><td>431</td><td>-3.34**</td><td>-4,166</td><td>—</td><td>—</td></tr><tr><td>Fixed</td><td>1,589.92</td><td>4</td><td></td><td>-6,824</td><td>192</td><td></td><td>-5,234</td><td></td><td></td></tr><tr><td rowspan="2">90.26</td><td>Dynamic</td><td>3,896</td><td>78</td><td>169.14**</td><td>-7,698</td><td>3</td><td>-1.20</td><td>-3,801</td><td>—</td><td>—</td></tr><tr><td>Fixed</td><td>1,448</td><td>64</td><td></td><td>-7,791</td><td>43</td><td></td><td>-6,343</td><td></td><td></td></tr></table>

∗∗Significant at p < 0 01.

Table 6a Waiting Time Comparisons in the Fixed vs. Dynamic Pricing Schemes (Single-Service Setting)

<table><tr><td colspan="10">Waiting time* in hours average (std. dev)</td></tr><tr><td colspan="2">Stationary arrival</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 75%)</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 80%)</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 85%)</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 90%)</td></tr><tr><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td></tr><tr><td colspan="10">Service A**</td></tr><tr><td>0.28 (0.01)</td><td>0.32 (0.03)</td><td>0.38 (0.14)</td><td>0.46 (0.25)</td><td>0.28 (0.01)</td><td>0.32 (0.03)</td><td>0.40 (0.17)</td><td>0.44 (0.17)</td><td>0.67 (0.35)</td><td>2.04 (1.87)</td></tr></table>

∗The dynamic price waiting time is a weighted average across all three priority classes.  
∗∗All means are different, p < 0 01.

Table 6b Waiting Time Comparisons in the Fixed vs. Dynamic Pricing Schemes (Multiple-Service Setting)

<table><tr><td colspan="10">Waiting time* in hours average (std. dev)</td></tr><tr><td colspan="2">Stationary arrival</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 75%)</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 80%)</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 85%)</td><td colspan="2">Nonstationary arrival (Utilization rate ≈ 90%)</td></tr><tr><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td><td>Fixed-price</td><td>Dynamic price</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="2">Service A**</td><td></td><td></td><td></td><td></td></tr><tr><td>0.36 (0.07)</td><td>0.62 (0.18)</td><td>0.22 (0.03)</td><td>0.33 (0.05)</td><td>0.28 (0.08)</td><td>0.49 (0.14)</td><td>0.40 (0.17)</td><td>0.77 (0.58)</td><td>0.63 (0.33)</td><td>1.46 (0.79)</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="2">Service B**</td><td></td><td></td><td></td><td></td></tr><tr><td>0.49 (0.07)</td><td>1.44 (0.38)</td><td>0.34 (0.034)</td><td>0.68 (0.09)</td><td>0.42 (0.08)</td><td>1.14 (0.23)</td><td>0.53 (0.19)</td><td>1.61 (1.46)</td><td>0.76 (0.34)</td><td>3.66 (2.59)</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="2">Service C**</td><td></td><td></td><td></td><td></td></tr><tr><td>1.23, 0.11</td><td>3.97 (0.71)</td><td>1.11 (0.08)</td><td>2.23 (0.34)</td><td>1.14 (0.08)</td><td>2.23 (0.34)</td><td>1.26 (0.20)</td><td>6.9 (10.14)</td><td>1.52 (0.36)</td><td>9.63 (7.05)</td></tr></table>

∗The dynamic price waiting time is a weighted average across all three priority classes.  
∗∗All means are different, p < 0 01.

Similar to the single-service setting, it is possible to resolve the conflicts in the multiple-service setting. For example, at 76.19% utilization rate, the customers could pay the provider \$1,393 K, and still be \$302 K better off when compared to fixed-price scheme.

Differences in Results between Single and Multiple-Service Settings. In light of the findings from the multiple-service setting, we note that user heterogeneity (i.e., multiple services) adds an interesting twist to the preference for dynamic and fixed price schemes. In the absence of user heterogeneity, provider’s preference for dynamic scheme under stationary demand is significantly diminished. In Table 5, we can see that user heterogeneity can make the provider at least indifferent between fixed and dynamic pricing schemes.

While nonstationary demand enhances provider’s welfare under dynamic pricing (see Table 3), the lack of user heterogeneity now ends up reducing the resulting benefits of personalized services for the customer. Therefore, we see a misalignment again. Essentially, the results show that resource utilization, nonstationary demand, and user heterogeneity are important factors that determine the relative preferences and alignment of interests in a service setting.

The results from single service scenario may seem to imply that it is better for the customer to split a multiple services contract into single service fixedprice contracts with a different vendor for each type of service. We conducted additional simulations in the single-service setting on Services B and C and analyzed the combined cost for the customer organization for three single-service contracts. We find that the combined cost of three single-service contracts is higher than the cost for a multiple service contract. Such suboptimization occurs because each provider serves only a subset of more homogenous set of users. When the entire user population is served by a single vendor, the resource allocation mechanism and corresponding service customization is more effective. Because the same resources can serve all request types equally efficiently under the current setting, segmenting the user population and dedicating resources to each service separately does not serve a purpose.

To summarize, key implications from our research suggest

• Resource utilization is a key source for conflict between the customer and provider. Variations in resource utilization arise from over/underestimation of demand. The SLA should include customer’s guarantee of the expected demand (in probabilistic terms) and include rules for volume-price adjustments should the actual demand deviate from the estimate. Providers, in turn, should promise service levels based on expected demand. This would reduce the likelihood of future conflicts arising from performance degradation because of overload or provider’s cost overrun due to underutilized resources.

• Customers contracting for heterogeneous systems (variance in volume, processing time, price, and user characteristics for the services included in the outsourcing arrangement) should evaluate the volume-quality trade-off possibilities among the different services before enforcing service levels for individual services. Such trade-offs, if possible, may result in increased organizational welfare; this is especially so when resource skill requirements are similar for the different services.

• Costs and benefits of demanding dedicated resources for specific services need to be carefully evaluated. Dedicating resources to individual services can be a suboptimal decision—resource pooling can improve service levels and system welfare. Using a pool of resources to serve regular service requests according to user-selected priorities would be efficient for both the customer and provider organizations; while an escalation procedure with dedicated resources having higher level of expertise may be a viable option for more complex and nonroutine service requests.

A general concern with simulation models is the sensitivity of the results with respect to the simulation parameters—in this case arrival rates and user delay-cost distributions. We have introduced maximum variance in arrival rates possible- given the limitation that we had to discard arrival values (generated from a random distribution) that resulted in infinite queue length (i.e., where the ratio /n > 1). Regarding the user delay cost (estimation procedures are provided in §B, supplementary material available at http://isr.pubs.informs.org/ecompanion.html.), we used values that justify the fixed-price as it is used as the baseline. High values of delay cost (compared to the fixed-price for a service) bias the customer towards a dynamic scheme, while low values make prioritization unnecessary. Test runs of the simulation confirmed this.

There are some constraining limitations in reading our results from both a domain and a methodological perspective. From a domain perspective, we did not incorporate possible interdependencies among different service types to maintain analytical tractability. It is possible that servicing certain types of requests have a positive/negative impact on other request types, or two request types must be serviced in a sequential manner. Presence of such dependencies results in interrelated performance measures, which in turn implies that incentives (penalties in the current model) on those performance measures should not be designed on stand-alone basis. For tractability purposes, we also considered all resources to be homogeneous. In our analysis, differences in skill levels for individual services are not modeled. We argue for this being a reasonable assumption in the present context (help-desk type of services) and do not believe it overly limits the results obtained.

From a methodological standpoint, derivation of the prices do not directly model user characteristics, rather they induce the users to self-select according to their reservation prices. This was deemed necessary as the providers have no information about individual user’s valuation of their request. Longer relationship with the customer would provide more information to the provider about different user groups, and prices can be refined accordingly. Finally, the welfare implications may be context specific to some extent. The exact cutoff points for the switching behavior and the relative profit gain/cost reduction values will vary depending on the service and user characteristics.

## 5. Conclusion

In this research, we explored the effect of demand heterogeneity (variance in quantity and quality requirement across users) on the pricing and subsequent resource allocation issues for support and management of IT infrastructure services. Using an analytical model for the price-penalty scheme we developed, fixed-price SLA models under varying levels of congestion and user preference was evaluated. The results demonstrate that while a dynamic pricing scheme may yield socially superior outcome, individual organization’s interests may be affected by the degree of heterogeneity and resource utilization. In the context of these results, the current level of discontent with the performance of outsourced IT contracts is not surprising.

A significant implication of our research to practice is that it brings to light the sources of conflict in interest in an outsourced service arrangement arising from differences in orientation, incentives, and costs between customers and providers. Our results indicate that blanket performance guarantees for the entire customer organization may not be in the interests of both IT service providers and customer organizations, especially when demand is unpredictable. Even when prioritized services with volume-price adaptation schemes are used, our results indicate that misalignments are possible. The degree of heterogeneity in services provided and level of resource utilization have quite opposing effects on the customer and provider organizations.

To the extent that variations in resource utilization arise from over/underestimation of demand, the services contracts should include some form of agreement on expected demand levels and include rules for volume-price adjustments should the actual demand deviate from the estimate. Providers, in turn, can begin to promise service levels based on expected demand. This would reduce the likelihood of future conflicts arising from performance degradation because of overload or provider’s cost overrun due to underutilized resources.

Customers contracting for heterogeneous systems (variance in volume, processing time, price, and user characteristics for the services included in the outsourcing arrangement) should evaluate the volumequality trade-off possibilities among the different services before enforcing service levels for individual services. Such trade-offs, if possible, may result in increased organizational welfare; this is especially so when resource skill requirements are similar for the different services.

The findings also point to the need to analyze the costs and benefits of demanding dedicated resources for specific services. Dedicating resources to individual services can be a suboptimal decision—resource pooling can improve service levels and system welfare. In essence, the findings in this research calls for a careful evaluation of the requirements of the different services. Where feasible, resource sharing among services should be considered. It follows that using a pool of resources to serve regular service requests according to user-selected priorities would be efficient for both the customer and provider organizations; while an escalation procedure with dedicated resources having higher level of expertise may be a viable option for more complex and nonroutine service requests.

In summary, both customer organizations and service provider organizations in long-term time and materials type of contracts would benefit from inclusion of terms related to demand levels and demand distributions, service heterogeneity, dedicated and nondedicated resources. Explicit specification of how urgency levels of requests are defined and handled would also benefit the long-term contractual relationship. Operationally, contingent pay-off schedules can be implemented to account for the natural uncertainties of demand and service level variances.

## Acknowledgments

A previous version of this article was published in the Proceedings of the 2005 Institute for Civil Infrastructure Systems (ICIS) Workshop on e-Business [Web]. The paper is substantially revised and extended.

## References

Bhargava, H. K., D. Sun. 2005. Performance-contingent pricing for broadband services. Proc. 38th Annual Hawaii Internat. Conf. Systems Sci., HICSS ’05, 211b. Big Island, HI.

Bhargava, H. K., S. Sundaresan. 2004. Computing as utility: Managing availability, commitment, and pricing through contingent bid auctions. J. Management Inform. Systems 21(2) 201–227.

Cheng, H. K., G. J. Koehler. 2003. Optimal pricing policies of webenabled application services. Decision Support Systems 35(3) 259–272.

Cocchi, R., D. Estrin, S. Shenker, L. Zhang. 1991. A study of priority pricing in multiple service class networks. Proc. Comm. Architecture and Protocols. Zurich, 123–130.

Deloitte Consulting. 2005. Calling a change in the outsourcing market: The realities for the world’s largest organizations. (April). Report. http//www.deloitte.com/dtt/cda/doc/ content/us\_outsourcing\_callingachange.pdf.

Dewan, S., H. Mendelson. 1990. User delay costs and internal pricing for a service facility. Management Sci. 36(12) 1502–1516.

Gross, D., C. M. Harris. 1998. Fundamentals of Queueing Theory. John Wiley, New York.

Gupta, A., D. O. Stahl, A. B. Whinston. 1996. An economic approach to networked computing with priority classes. J. Organ. Com put. Electronic Commerce 6(1) 71–95.

Hamblen, M. 2005. The chargeback CONUNDRUM. Computerworld 39(7) 38.

Haviv, M., Y. A. Ritov. 1998. Externalities, tangible externalities, and queue disciplines. Management Sci. 44(6) 850–858.

Holmstrom, B., P. Milgrom. 1987. Aggregation and linearity in the provision of intertemporal incentives. Econometrica 55(2) 308–328.

Jewkes, E. M., D. A. Stanford. 2003. A two priority queue with crossover feedback. Queueing Systems 43(1–2) 129–135.

Keon, N. J., G. Anandalingam. 2003. Optimal pricing for multiple services in telecommunications networks offering quality-ofservice guarantees. Networking, IEEE/ACM Trans. 11(1) 66–80.

Konana, P., A. Gupta, A. B. Whinston. 2000. Integrating user preferences and real-time workload in information services. Inform. Systems Res. 11(2) 177–196.

Litten, K. 2004. IT service management: Selecting the right metrics for performance management. (April 1). White Paper, International Network Services, Santa Clara, CA.

Maglaras, C., A. Zeevi. 2005. Pricing and design of differentiated services: Approximate analysis and structural insights. Oper. Res. 53(2) 242–262.

Marbach, P. 2004. Analysis of a static pricing scheme for priority services. IEEE/ACM Trans. Networking 12(2) 312–325.

Mendelson, H. 1985. Pricing computer services—Queuing effects. Comm. ACM 28(3) 312–321.

Mendelson, H., S. Whang. 1990. Optimal incentive-compatible priority pricing for the M/M/1. Oper. Res. 38(5) 870–883.

Nadiminti, R., T. Mukhopadhyay, C. H. Kriebel. 2002. Research report: Intrafirm resource allocation with asymmetric information and negative externalities. Inform. Systems Res. 13(4) 428–434.

Neeleman, D. 2007. JetBlue’s customer bill of rights. http://www. jetblue.com/about/ourcompany/promise/index.html.

Oliva, R., J. D. Sterman. 2001. Cutting corners and working overtime: Quality erosion in the service industry. Management Sci. 47(7) 894–914.

Open Group. 2004. SLA Management Handbook' Enterprise Perspective, Vol. 4. The Open Group. http://www.opengroup.org/ pubs/catalog/g045.html.

Paich, M., J. D. Sterman. 1993. Boom, bust, and failures to learn in experimental markets. Management Sci. 39(12) 1439.

Quinlan, T. 2003. Value of an IT chargeback system—Part two. J. Bank Cost Management Accounting 16(1) 39–47.

Raghu, T. S., P. K. Sen, H. R. Rao. 2003. Relative performance of incentive mechanisms: Computational modeling and simulation of delegated investment decisions. Management Sci. 49(2) 160–178.

Rehme, J. 2006. Prices and contracts for service selling: Service level agreements, contracts, and price models. Technical report, Industrializing After Sales Service (IASS).

Ricardo, A. 2006. Pay-As-You-Drive: Dynamic insurance emerges in Europe. Technical report, Forrester Research. http://www. forrester.com/Research/Document/Excerpt/0,7211,38860,00.html.

Ross, J. W., M. R. Vitale, C. M. Beath. 1999. The untapped potential of IT chargeback. MIS Quart. 23(2) 215–237.

Sapiera, J. 2003. How SLAs are used. Network Comput. (March 21) 71–75.

Sleptchenko, A. 2003. Multi-class, multi-server queues with non-preemptive priorities. Technical Report 2003-016, EURANDOM, Eindhoven, The Netherlands.

Son, J. H., M. H. Kim. 2004. An analysis of the optimal number of servers in distributed client/server environments. Decision Support Systems 36(3) 297–312.

Stanford, D. A. 1997. Waiting and interdeparture times in priority queues with poisson- and general-arrival streams. Oper. Res. 45(5) 725–735.

Wierman, A., T. Osogami, M. Harchol-Balter. 2003. Analyzing the effect of prioritized background tasks in multiserver systems. Technical Report CMU-CS-03-213. Carnegie Mellon University, Pittsburgh.
