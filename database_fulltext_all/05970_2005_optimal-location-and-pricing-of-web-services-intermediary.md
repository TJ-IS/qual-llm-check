---
otero_id: 5970
otero_key: "SKC6TYDR"
title: "Optimal location and pricing of Web services intermediary"
authors: "Qian Candy Tang; Hsing Kenneth Cheng"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.04.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Optimal location and pricing of Web services intermediary

Qian Candy Tang, Hsing Kenneth Cheng

Department of Decision and Information Sciences, Warrington College of Business Administration, University of Florida, P.O. Box 117169, Stuzin 351, Gainesville, FL 32611-7169, USA

Available online 18 May 2004

## Abstract

The Web services technology allows for the distribution and integration of loosely coupled software components over the Internet. This paper studies the optimal pricing and location strategy of a Web service intermediary (WSI), which offers a timesensitive composite Web service. We first derive the optimal solution in a linear city model and then extend the analyses to the more general unit circle model. Our analyses show that that the optimal strategy is determined by delay cost, integration cost, and prices of the constituent Web services. We find that the WSI is optimally located between the Web service providers and charges a penetration price if the delay cost is low. In addition, there could be multiple optimal locations for the WSI if the Web service providers are far away from each other. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Web services intermediary; Spatial model; Pricing; Location model

## 1. Introduction

The software industry has long been a battlefield where firms try to win customers via proprietary platforms and technologies. Web services, a new computing paradigm, for the first time is gaining endorsement simultaneously from major software developers like IBM, Sun, and Microsoft, who traditionally compete with each other with their own technologies. According to the Stencil Group, Web services are ‘‘loosely coupled, reusable software components that semantically encapsulate discrete functionality and are distributed and programmatically accessible over standard Internet protocols’’ (www.stencilgroup.com), see also Refs [3,5]. From the technical perspective, Web Services represent a collection of standard protocols including XML, SOAP, WSDL, and UDDI for the creation, distribution, discovery, and integration of semantic software components that encapsulate business functionalities. From the business perspective, Web services enable just-in-time software service provisioning through the integration of loosely coupled software components. Central to the Web services architecture are the concepts of software as service and platform independence.

As opposed to packaged monolithic applications that have to be developed or licensed, Web services encapsulate specific business functionalities that can be ‘‘rented’’ over the Internet. Web services decompose business processes into granular components and thus allow customers to select the services on an asneeded basis. The service-oriented architecture also opens new business opportunities for firms by allowing them to sell their software components as Web services over the Internet. For example, CitiBank developed CitiConnect, a payment-processing service that can be plugged into other company’s transaction process [6]. The spectrum of Web services spans from personal services such as stock quote, messaging services to enterprise-centric services such as call center control, payroll management, shipping and logistics, and so on.

Another key feature of the Web services is the openness of technology. The stack of Web services core protocols includes XML, WSDL, SOAP, and UDDI. The XML (extensible Markup Language) protocol allows self-describing data to be exchanged independent of platform and language. The XMLbased messaging protocol SOAP (Service-Oriented Architecture Protocol) supports the invocation of components similar to RPC (Remote Procedure Call) on existing Internet network. The WSDL (Web Services Description Language) builds on XML and describes what the Web service does, where it is located, and how to communicate with it. The UDDI (Universal Description, Discovery and Integration) represents a set of protocols for the description, registration, dynamic lookup, and integration of software components. In essence, the Web services architecture provides a platform-, language-, and vendor-neutral framework for the interaction and integration of software components via standard networking technologies.

The modularity and platform independence of Web services will greatly affect software development and deployment. Internally, the Web services technology changes the fundamental cost structure of software development and enterprise application integration. By leveraging existing systems and outsourcing standard modules, a firm can decrease software development cost and duration dramatically. With interoperable software components that encapsulate business functionalities available over the Internet, firms are endowed with the flexibility of choosing the best-of-breed software components and pay for the services on an as-needed basis. Externally, Business-to-Business (B2B) integration or collaboration is made more cost-efficient because the firms no longer have to set up a separate integration project with each business partner. As a result, business alliances can be created and decoupled on the fly and firms can dynamically lookup, bind, and consume Web services over the Internet.

Furthermore, the flexibility, reusability, and interoperability of the Web services paradigm help create a new business model of Web services intermediary (WSI). A WSI provides value-added services including directory and search engine, auditing, quality-of-service (QoS) assurance, as well as the integration or orchestration of Web services [1,4]. For example, salcentral.com, which originally called itself ‘‘the Napster of Web services’’, provides a Web services search engine and tools to develop and integrate Web services. Both the consumers and producers of the Web services benefit from the maintenance service provided by the WSI, which hosts the latest version of the Web services and offers tools to manage and control them.

While the Web services paradigm is a promising solution to bridge the platform discrepancy and geographical distance between software components, some constraints may hinder the widespread adoption of Web services and its service-oriented framework. For example, the performance of a service-oriented architecture is restricted by the computing power of local servers and the robustness and capabilities of the underlying network through which the Web services are distributed. Response time is especially important for time-sensitive applications such as stock quote and instant messaging. With computing power doubled every 18 months, according to the Moore’s Law, the ability to increase the processing power of local servers at decreasing cost has become the norm. In contrast, the network infrastructure is less scalable and network topology is even more inflexible to change. Johansson [7] suggests that the network latency, which is directly related to the physical distance between two entities on the network, constitutes a rather salient proportion of response time in high bandwidth network. Therefore, the success of a Web services-oriented architecture requires prudent planning of the Web services distribution network.

In this paper, we focus on the optimal strategy of a Web service intermediary (WSI), which offers a new time-sensitive composite Web service by integrating two complementary Web service components. At the same time, the constituent Web service components are offered by two independent service providers.

Customers can buy the composite Web service from the WSI, or buy the individual Web service components from the service providers and then create the desired composite Web service by integrating the two Web services in a Do-It-by-Yourself fashion. In the context of Web services paradigm, the purchase of Web services involves executing the software component stored at the service provider’s server, while the customers do not own and house the software component. Consequently, customers incur a ‘‘delay cost’’ resulting from the turnaround time of executing the Web service located at the service provider’s server, including the local processing time and the network delay. The network delay has been found to be proportional to the physical distance between the customer and the service provider’s server and has become the dominant term of customers’ delay cost [7]. The total cost for a customer to obtain the composite Web service from the WSI includes the price, the delay cost of executing the Web service. If the customer instead chooses to create the composite Web service by himself, the total cost is the sum of the prices of two Web service components, the delay cost, and the integration cost. Given the locations of the individual Web service providers in the distribution network and customer demand, the WSI has to optimally choose its location in the network as well as the price for the composite service it sells.

We propose a spatial model to solve the joint location and pricing decision problem of the WSI. We first derive the optimal location and price in a linear city model to study a special case where the service providers are located at the end points of a line segment, i.e., all customers are located between the service providers. In the linear city model, the midpoint position between the service providers is the optimal location for the WSI. Further, our analysis shows that the WSI will always charge a marketcovering price for its composite service, regardless of the delay cost. However, the WSI can charge a higher price in the presence of a higher delay cost and integration cost and its profit also increases with delay cost and integration cost. The impact of delay cost is found to be not as high as the integration cost. We then extend the analyses to the more general unit circle model where the service providers do not span the entire network; that is, not all customers are located between them. We find that when the delay cost is small, the WSI is optimally located at the midpoint position and charge a market-covering price. If, however, the distance between the service providers is large, there could be multiple optimal locations for the WSI.

This paper is organized as follows. Section 2 describes the location and pricing issues facing the WSI with discussion on related literature. We first present a linear city model and show the impact of the integration cost and delay cost on WSI’s optimal pricing and profit. Section 3 discusses the WSI’s location and pricing decision problem in a more general setting by extending the analyses of the linear city model to the unit circle model. Section 4 summarizes the managerial implications and concludes the paper with discussion on future research directions.

## 2. The location and pricing issues of Web service intermediary

Consider two independent software vendors offering two complementary Web services denoted by S1 and S2. Let $P _ { 1 }$ and $P _ { 2 }$ be the price of S1 and S2, respectively. A Web service intermediary (WSI) offers a new time-sensitive composite Web service denoted by S3 produced by integrating S1 and S2. Examples of time-sensitive Web services include stock quote, credit check required for payment services, and so on. The WSI charges a price of $P _ { 3 }$ for its integrated Web service S3. Customers who are interested in the integrated service can either buy the composite service from the WSI or buy the two Web services S1 and S2 from the service providers and integrate by themselves, in which case the customer incurs an integration cost c (see Table 1 for summary of notation used in this paper).

Suppose the reservation prices of the customers for the integrated service are sufficiently high so that all customers either buy from the WSI or from the service vendors, and each customer has one unit demand for the integrated service. As described in Section 1, customers experience response delay from executing Web services stored at the service provider’s server. In case a customer incurs the same cost to buy from the WSI as to buy individual components and create the desired integrated service by himself, the customer will buy the composite service from the WSI due to the added valued provided by the WSI.

<table><tr><td colspan="2">Summary of notation</td></tr><tr><td>S1, S2</td><td>individual Web services that have complementary functionalities</td></tr><tr><td>S3</td><td>composite Web service offered by the Web Service Intermediary (WSI)</td></tr><tr><td> $P_{1}, P_{2}$ , and  $P_{3}$ </td><td>prices of S1, S2 and S3</td></tr><tr><td> $\bar{P}_{3}$ </td><td>the highest price WSI can charge for the composite service to attract all customers</td></tr><tr><td>c</td><td>integration cost if customers integrate S1 and S2 by themselves</td></tr><tr><td>t</td><td>delay cost of executing the Web service per unit of distance between the customer and the service provider</td></tr><tr><td>d</td><td>distance between the two independent service providers</td></tr><tr><td>x</td><td>location of the WSI</td></tr><tr><td>y</td><td>location of the customer</td></tr></table>

As the response time is a major concern for consumers of time-sensitive integrated Web service S3, it is important to analyze the composition of response time of applications over the Internet. According to Johansson et al. [8], the response time of applications over the Internet is composed of two parts—local processing time and network response time. Local processing time is determined by the capacity of the local server and the request load. Network response time can be further divided into transmit time, queuing delay, and network latency. Transmit time is related to network bandwidth while the queuing delay is determined by capacity of network devices and amount of data transmission jobs. Network latency is the time taken to transport data between two locations on the network and is generally a function of physical distance between the two nodes on the network. Johansson [7] pointed out that while much research has been done on network design in consideration of network bandwidth and device capacity, the network latency is usually ignored in previous research. As the cost of computing is halved roughly every 18 months, in accord with the wellknown Moore’s Law of computing, the network latency has become the dominant term of response time of applications over the Internet.

In an abstract sense, the Internet is composed of two parts, the cores and the edges. Local servers and client machines are located at the edges, connected by the switches and routers at the core. The network latency for exchanging data between the server and the client is a function of number of routers and switches between them, which is correlated with the physical distance between the server and the client. To model the impact of network latency on the response time of Web services, let t be the delay cost per unit of distance between the customer and the Web service provider where the distance corresponds to the number of routers and switches between them.

In deciding whether to buy (i.e., to ‘‘execute’’) the integrated Web service S3 located at the WSI or to integrate the Web services S1 and S2 located at their corresponding service providers, the customer must take into account not only the prices of the Web services under consideration but also the delay cost from each alternative. Likewise, the WSI faces a joint decision to optimally choose its location on the Internet and to price its service offering to attract potential customers and to maximize its profit.

The choice of optimal location for the WSI bears some resemblance to the facility location problem in the literature. Information systems research on network design has traditionally taken an operations research (OR) approach, borrowing methods from classic OR problems such as the facility location problem [2]. The facility location problem, usually modeled as a mixed integer programming problem, is defined as choosing the number of facilities and locations to minimize total cost (or maximize profit) subject to capacity constraints, demand constraints, and others. Solution methodologies include developing heuristics based on dynamic programming [9], Lagrangean relaxation [10], and so on. Sun [12] and Sun and Koehler [12] were among the first to study the location model for Web services intermediaries. Mixed integer programming models were proposed in Refs. [11,12] to decide the best location of a WSI by considering the usage requirement, server’s capacity, and assignment constraints. Efficient heuristics were developed to tackle the location problem as the proposed model became computationally intractable.

Several special characteristics of the Web services market suggest solving the location and pricing problem of WSI differently from the traditional facility location problem. First, while the facility setup cost is an important factor in the facility location problem, we treat it as sunk cost and focus on the WSI’s

![](/api/attachments/SKC6TYDR/fulltext/images/96142bd3cb3413fafd302f9f6276a642b106fdf997620eac1bbcddcd85e7eac9.jpg)

S2

Fig. 1. A linear city model.

revenue from selling the composite service. Second, because the facility location problem deals with cost minimization, it usually solves the decision problem for one single company without consideration of competitions. The WSI, however, has to compete with the individual service providers by selecting the right location and the right price. Our problem is unique in that we consider the joint decision of location and pricing problem in a market of complementary Web services. Last, as will be illustrated below, the functional form of delay cost of accessing Web services for a customer in the network is dependent on the location of the customer. Although in facility location problems, one can model the delay cost as a function of distance between nodes, there is no flexibility to choose different delay cost functions for customers at different locations.

We propose two spatial models to study the joint decision problem for a WSI offering an integrated timesensitive Web service. We first study a special case by examining a linear city model in the following subsection and then extend the analyses to a more general case by adopting a unit circle model in Section 3.

## 2.1. Linear city model: a special case

Assume the two Web service providers offering S1 and S2 are located at the end points of a unit length linear city and let x be the WSI’s location on this linear city (see Fig. 1). Due to the symmetry of this linear city model, we consider without loss of generality the case where $0 \le x \le 1 / 2$ . The potential customers of the integrated service are uniformly distributed in this linear city between 0 and 1. Recall that the customers incur a delay cost t per unit of distance from consuming (accessing) the Web service.

The customer at location $y ( 0 \leq y \leq 1 )$ incurs a delay cost of ty for consuming the Web service S1 and $t ( 1 - y )$ for S2. The delay cost for the same customer to access the integrated Web service offered by the WSI is $t | y - x |$ . Then, the total cost for the consumer located at y to buy the integrated service from the WSI is composed of the price of the integrated service $( P _ { 3 } )$ and the delay cost, as shown in Eq. (1).

$$
P _ {3} + t | y - x |\tag{1}
$$

The total cost for customers between 0 and 1 to purchase the Web services S1 and S2 separately and integrate by themselves includes the prices of the individual Web services $( P _ { 1 }$ and $P _ { 2 } ) _ { 2 }$ , the integration cost (c), and the total delay cost that equals $t y + t ( 1 - y ) = t .$ Eq. (2) describes the total cost for customers who choose to create the integrated Web service by themselves.

$$
P _ {1} + P _ {2} + c + t\tag{2}
$$

By evaluating the total costs in Eqs. (1) and (2), each customer decides whether to buy the integrated service from the WSI or to create the integrated service by purchasing the individual Web services from the service vendors separately. The marginal customers who are indifferent between buying from the WSI and creating the integrated Web service by themselves are described in Eqs. (3) and (4), where y<sub>1</sub><sup>m</sup> and $y _ { 2 } ^ { \mathrm { m } }$ denote the distance between the marginal customer and the WSI (see Fig. 2).

$$
P _ {1} + P _ {2} + c + t = P _ {3} + t y _ {1} ^ {\mathrm{m}}\tag{3}
$$

$$
P _ {1} + P _ {2} + c + t = P _ {3} + t y _ {2} ^ {\mathrm{m}}\tag{4}
$$

For customers between the two marginal customers at $y _ { 1 } ^ { \mathrm { m } }$ and $y _ { 2 } ^ { \mathrm { m } }$ , the total cost to buy the composite Web service from the WSI is lower than to buy S1 and S2 separately and to create the composite service by themselves. Therefore, they will buy from the WSI. However, if the WSI sets price $P _ { 3 }$ too high, all customers between 0 and 1 would create the integrated service by themselves, leaving no demand for the WSI. On the other hand, if the WSI set the price $P _ { 3 }$ low enough, all customers between 0 and 1 would buy from the WSI. In summary, the demand of the WSI is $D { = } y _ { 1 } { + } y _ { 2 }$ , where

![](/api/attachments/SKC6TYDR/fulltext/images/80766f2ef012045750a9f5d642d3d1f4ac3453e31dc785652a71be3df5c48405.jpg)  
Fig. 2. Demand of the intermediary.

$$
y _ {1} = \left\{ \begin{array}{l l} 0, & \text { if } y _ {1} ^ {\mathrm{m}} \leq 0 \\ y _ {1} ^ {\mathrm{m}}, & \text { if } 0 <   y _ {1} ^ {\mathrm{m}} <   x \\ x, & \text { if } y _ {1} ^ {\mathrm{m}} \geq x \end{array} \right.\tag{5a}
$$

$$
y _ {1} = \left\{ \begin{array}{l l} 0, & \text { if } y _ {2} ^ {\mathrm{m}} \leq 0 \\ y _ {2} ^ {\mathrm{m}}, & \text { if } 0 <   y _ {2} ^ {\mathrm{m}} <   1 - x \\ 1 - x, & \text { if } y _ {2} ^ {\mathrm{m}} \geq 1 - x \end{array} \right.\tag{5b}
$$

The WSI seeks to optimally set the location (x) and price $( P _ { 3 } )$ to maximize its profit (see Eq. (6)).

$$
\max _ {P _ {3}, x} \pi = P _ {3} D = P _ {3} (y _ {1} + y _ {2})\tag{6}
$$

$$
\mathrm{s.t.} (5 \mathrm{a}) \text { and } (5 \mathrm{b})
$$

Proposition 1. In the unit-length linear city model, the WSI’s optimal price and profit are $P _ { 3 } ^ { * } { = } P _ { I } { + }$ $P _ { 2 } + c + I / 2$ t and $\pi ^ { * } { = } P _ { I } { + } P _ { 2 } { + } c { + } I / 2$ t. The midpoint position between the service providers is the optimal location for the WSI, $i . e . , x ^ { * } = I / 2 .$ Further, the WSI captures the entire market demand.

Proof. We solve this joint decision problem in two steps. First, we find the optimal price and profit for the WSI given any particular position x. Then, the optimal location is selected as the one that yields the highest profit obtained in the previous step. The derivation of the optimal profit and location is quite tedious and delegated to Appendix A. 5

Proposition 1 suggests that if all customers are located between the service providers, in which case all customers incur the same cost if they integrate the composite Web services by purchasing S1 and S2 from the service providers, the optimal location of the WSI would be the midpoint position between the service providers. In addition, the WSI is best off by setting a penetration price to capture entire market demand. In addition, as the delay cost or the integration cost increases, the WSI will also increase the price of the composite Web service and obtain more profit. The optimal price and profit increases faster with the integration cost than with the delay cost. This can be easily seen as $( \partial \pi ^ { * } / \partial c ) { > } ( \partial \pi ^ { * } / \partial t )$ . It is quite intuitive that the WSI gains more profit when the integration cost is higher as more customers will switch to the WSI due to the higher cost of integrating the individual Web services. However, when the delay cost increases, the costs of buying from the WSI and the service providers will both grow. The increased profit of the WSI in the presence of larger delay cost suggests that the negative impact of delay cost is higher for the service providers than the WSI.

In the linear city model, we assume that the service vendors are located at ‘‘extreme points’’ such that all customers are located between the service providers. In the next section, we will relax this assumption by considering a unit circle model.

## 3. Optimal location and pricing in unit circle model

In this section, we study the more general case of a unit circle model where the two service providers do not cover the entire network. Let 0 be the location of the first service provider on the unit circle, and the second service provider is located at distance d clockwise from the first provider. Without loss of generality, we consider the case where $0 \leq d \leq 1 / 2$ Suppose the Web service intermediary (WSI) offering the integrated service is located at x clockwise $( 0 \leq x < 1 )$ on the unit circle. There are N potential customers of the integrated service uniformly distributed along the unit circle.

The unit circle model is depicted in Fig. 3, where points A and B represent the locations of the Web service providers of S1 and S2 and the WSI is located at point E. For the purpose of analysis, we mark points C, D, and F, which are diagonal to points A, B, and E on the unit circle, respectively.

One distinctive feature of the unit circle model is that the delay cost for a customer along the unit circle is conditional on his location, as the shortest route to reach a node could be traveled either clockwise or counter-clockwise. For example, for a particular customer located at y clockwise from point A, the total cost to purchase the integrated service from the WSI is

![](/api/attachments/SKC6TYDR/fulltext/images/426076e6de9fb9d04ca222cd8cd470b6ac614d89c5e4ed212f18ed4a3879152d.jpg)  
Fig. 3. Unit circle model.

$$
\begin{array}{l} P _ {3} + t | y - x |, \text {   if   } | y - x | \leq 1 / 2, \text {   and   } \\ P _ {3} + t (1 - | y - x |), \text {   if   } | y - x | > 1 / 2 \end{array} .\tag{7}
$$

If the customer integrates the service by himself, the delay cost is the sum of delay costs of accessing the Web services S1 and S2. Unlike the linear city model where all customers are located between the two service providers and incur the same delay cost when accessing the Web services S1 and S2, customers at different locations experience different response delay due to different shortest route of access. For example, customers located between A and B incur a delay cost of td, and the customers located between C and D incur a delay cost of $t ( 1 - d )$ . Customers located within the BC and DA segments incur a delay cost between td and $t ( 1 - d )$ . Eq. (8) summarizes the total cost for a customer at $y \left( 0 \leq y < 1 \right)$ integrating the Web service by himself, which includes the prices of the Web services S1 and S2, the integration cost, and delay cost.

$$
\begin{array}{l l} P _ {1} + P _ {2} + c + t d, & \text { if } 0 \leq y \leq d \\ P _ {1} + P _ {2} + c + t (2 y - d), & \text { if } d <   y \leq 1 / 2 \\ P _ {1} + P _ {2} + c + t (1 - d), & \text { if } 1 / 2 <   y \leq 1 / 2 + d \\ P _ {1} + P _ {2} + c + t (2 - 2 y + d), & \text { if } 1 / 2 + d <   y <   1 \end{array}\tag{8}
$$

Given the total costs in Eqs. (7) and (8), one can find the location of the marginal customers who are indifferent between buying from the WSI and creating the integrated service by themselves. The demand of the WSI at a particular location can be further calculated as a function of the delay cost, integration cost, distance between the individual service providers and their prices. Using the same approach as in the previous section, one can solve the joint decision problem of optimal location and pricing for the WSI. However, the complexity of the profit function, which stems from the conditional format of total costs in Eqs. (7) and (8), makes the problem rather tedious and intractable. Therefore, we adopt a different approach to solve the location and pricing problem in the unit circle model.

Lemma 1. The highest market-covering price ${ \bar { P } } _ { 3 }$ for the WSI located at is

$$
\left(\min \{P _ {1} + P _ {2} + c + t x, P _ {1} + P _ {2} + c + t (\frac {1}{2} - d), P _ {1} + P _ {2} + c + t (d - x) \}, \quad 0 \leq x \leq d \right.\tag{9.1}
$$

$$
d <   x \leq \frac {1}{2}\tag{9.2}
$$

$$
\frac {1}{2} <   x \leq \frac {1}{2} + d\tag{9.3}
$$

$$
\frac {1}{2} + d \leq x <   1\tag{9.4}
$$

Proof. The highest market-covering price is the highest possible price of the integrated service that allows the WSI to capture the entire market demand.

This price is calculated in two steps. First, for each customer, we calculate each customer’s total cost to create the integrated Web service by himself. Then, the highest market-covering price is selected as the lowest of those total costs in the previous step. Detailed derivation is left to Appendix A. 5

Lemma 2. When the WSI charges the highest marketcovering price, the WSI achieves maximum profit if it is located between the two Web service providers.

Proof. Because the WSI captures the entire market demand, its profit is constrained by the highest market-covering price it can charge. By inspection of Eqs. (9.1)–(9.4), one gets $\bar { P } _ { 3 } \leq P _ { 1 } + P _ { 2 } + c$ in Eqs. (9.2) – (9.4), while $\bar { P } _ { 3 } \ge P _ { 1 } + P _ { 2 } + c$ in Eq. (9.1). Therefore, to yield maximum profit while still attracting all customers, the WSI will choose to locate between the service providers. 5

Lemma 3. If the WSI raises its market-covering price ${ \bar { P } } _ { 3 }$ by $\varDelta P _ { 3 } { = } (  ( k t ) / N )$ , where k is a positive integer, it will lose no less than min {k, N} customers. Furthermore, $i f k t { / } N { < } \varDelta P _ { 3 } { < } ( k { + } \ I ) t { / } N ,$ the WSI loses demand of no less than min $\{ k + I , N \}$

Proof. See Appendix A.

Proposition 2. When $t \leq 2 ( P _ { I } + P _ { 2 } + c )$ , the WSI’s optimal location is between the service providers of S1 and S2 and the optimal price is the marketcovering price P¯ 3 inEq. (9.1).

Proof. Proposition 2 is derived from Lemmas 1 –3. See Appendix A for detailed proof. 5

Proposition 3. When $t \leq 2 ( P _ { I } + P _ { 2 } + c ) ,$ , and $d > I / 3 ,$ there are multiple optimal locations for the WSI. The optimal location and pricing of the WSI are described by Eq. (10.1).

$$
\text {   If   } \frac {1}{3} <   d \leq \frac {1}{2}, \quad P _ {3} ^ {*} = P _ {1} + P _ {2} + c + t \left(\frac {1}{2} - d\right)
$$

$$
a n d \quad \frac {1}{2} - d \leq x ^ {*} \leq 2 d - \frac {1}{2};\tag{10.1}
$$

When $t \leq 2 ( P _ { I } + P _ { 2 } + c )$ and $0 \leq d \leq I / 3 , E q$ . (10.2) describes the optimal location and pricing of the WSI.

$$
\text {   If   } 0 \leq d \leq \frac {1}{3}, \quad P _ {3} ^ {*} = P _ {1} + P _ {2} + c + t / 2
$$

and $x ^ { * } = d / 2 ,$

ð10:2Þ

Note that the multiple optimal locations in $E q . \ ( l 0 . l )$ include the midpoint between the two Web service providers of S1 and S2.

Proof. Proposition 3 is derived from Lemma 1 and Proposition 2. See Appendix A for detailed proof. 5

Propositions 2 and 3 are consistent with our analysis of the linear city model, see Proposition 1. However, in the linear city model, the service providers are located at extreme points such that the WSI is always located between them. In the unit circle model, the WSI can select the intensity of competition by locating at different regions on the unit circle. For example, the competition between the WSI and the service providers is maximal if the WSI is located between A and B; the competition is minimal in section CD; and the section BC and DA represents regions of moderate competition. Proposition 2 suggests that if the delay cost is small, the WSI prefers maximum competition and will set the price to capture the entire market demand. This result is quite ‘‘unconventional’’ in the sense that classic economic theories, such as the theory of Bertrand competition, suggest that firms prefer reduced competition to avoid price war. This unusual result can be explained by two characteristics of the Web service market. First, as an executable program distributed over the Internet, the performance of this Web-service based platform is greatly constrained by the underlying networking infrastructure. In particular, customers incur a delay cost due to network latency, which is proportional to the physical distance from the Web service providers. Second, due to the platform independence and software modularity, a Web-service-based platform boasts the flexibility of integrating different services on the fly, across the street, or across the ocean. In a market of complementary Web services, the delay cost of integrating two Web services is the sum of delay cost of accessing each Web service separately. On the other hand, customers incur a single delay if they obtain the composite Web service from the WSI directly. The WSI, although facing a strong competition, can charge a higher price while still attracting all customers in market. This is not a deviant from the penetration price in Bertrand competition, because the WSI sets the price to cover the entire market.

While the linear city model yields one single optimal location for the WSI, Proposition 3 suggests that there could be multiple optimal locations for the WSI in the unit circle model. In fact, the result in the linear city model can be viewed as a special case of the unit circle model because the midpoint position is always the optimal location in Proposition 3.

## 4. Conclusions and future research

Web services, defined as software services that encapsulate discrete business functionalities programmatically accessible over the Internet, have become a promising solution to a platform-independent, serviceoriented distributed computing infrastructure. Built on open technologies and modular software components, the Web services paradigm provides benefits such as reduced integration cost, flexibility to choose best-ofbreed software components, and dynamic integration of complementary software components. From the business perspective, the Web services paradigm has the potential to change the cost structure of software development, affect software deployment as well as create new business opportunities. For example, the Web services intermediary (WSI) is a new business model that offers value-added services, including service integration and orchestration, service hosting and maintenance, etc. As an Internet-based technology, the performance of a Web-service-based computing environment is constrained by the capabilities of the network where the Web services are distributed. Therefore, the profitability of a WSI is determined not only by its pricing but also by its location decisions. Specifically, when customers are sensitive to delay cost, the location of the WSI becomes one crucial decision factor.

In this paper, we study the optimal location and pricing for a WSI in a market of complementary Web services. We propose a spatial model to study this joint decision problem. A linear city model is first presented to study a special case where the individual service providers are located at the ends of the linear city model. We derive analytical solutions to the optimal location and price for the WSI. Our research indicates that the WSI is optimally located at the midpoint between the service providers. The optimal pricing strategy for the WSI is a penetration price that grabs all customers in market. Furthermore, the WSI’s optimal price and profit are increasing in the delay cost and the integration cost, while the integration cost plays a more significant role compared to the delay cost. To study the general case where not all customers reside between the service providers, a unit circle model is applied. Analytical results show that when the delay cost is low, the highest market-covering price is the optimal price and the WSI’s profit is maximized if it is located at the midpoint between the service providers. In addition, there exist multiple optimal locations for the WSI if the distance between the service providers is large.

The purpose of this paper is to provide a theoretical foundation for the location and pricing of a WSI. Like any research, it has limitations and there are several interesting issues worthy of future research. First, our analysis in the unit circle model only gives conclusive result under the condition when the delay cost is small, i.e., $t \leq 2 ( P _ { 1 } + P _ { 2 } + c )$ There are no analytical conclusions for other cases of the delay cost. As a direct analytical derivation becomes too complicated, one might consider adopting a simulation study of the unit circle Web services market to draw insights. We anticipate that the results for the high delay cost case in the unit circle should be consistent with the analytical results we derive in this paper. Secondly, we study the optimal location and decision of a single-site WSI in this research. It is of practical interest to study the location and pricing problem of a WSI with two mirror sites. Finally, we only consider demand for the integrated Web service in our derivation of optimal location and price. In future research, we will examine the location and pricing decisions for the WSI that functions as a Web service marketplace by offering individual Web service components (S1 and S2) as well as the integrated Web services (S3).

## Appendix A

Proof of Proposition 1. First, we derive the WSI’s optimal price and profit given location x. Note that the WSI’s demand is conditional on the price of the integrated service $P _ { 3 } ,$ see Eqs. (3), (4), (5a), and (5b). Therefore, we need to calculate the WSI’s optimal price and profit under different classifications of the demand function. 5

Case 1-1. If $P _ { 3 } \geq P _ { 1 } + P _ { 2 } + c + t ,$ we have $y _ { 1 } = y _ { 2 } = 0$ This makes zero profit for the WSI because the price is too high. We will disregard this situation in the future analysis.

Case 1-2. If $P _ { 1 } + P _ { 2 } + c + t ( 1 - x ) { \le } P _ { 3 } { \le } P _ { 1 } + P _ { 2 } + c + t ,$ we have $0 \leq y _ { 1 } ^ { \mathrm { { m } } } , y _ { 2 } ^ { \mathrm { { m } } } \leq x .$ . The total demand of the WSI is $D = y _ { 1 } ^ { \mathrm { m } } + y _ { 2 } ^ { \mathrm { m } }$ . The decision problem of the WSI is to optimally set the price $P _ { 3 }$ to maximize profit, described in Eq. (A1).

$$
\max _ {P _ {3}} \pi = 2 P _ {3} \frac {\left(P _ {1} + P _ {2} + c + t - P _ {3}\right)}{t}\tag{A1}
$$

$$
\mathrm{s.t.} P _ {1} + P _ {2} + c + t (1 - x) \leq P _ {3} \leq P _ {1} + P _ {2} + c + t
$$

By solving the profit maximization problem in Eq. (A1), one gets the optimal price and profit in Eq. (A2).

$$
\begin{array}{l} P _ {3} ^ {*} = P _ {1} + P _ {2} + c + t (1 - x), \\ \pi^ {*} = 2 x [ P _ {1} + P _ {2} + c + t (1 - x) ] \end{array}\tag{A2}
$$

Case 1-3. If $P _ { 1 } + P _ { 2 } + c + t x \le P _ { 3 } \le P _ { 1 } + P _ { 2 } + c + t ( 1 -$ x), we have $y _ { 1 } ^ { \mathrm { m } } \geq x$ and $y _ { 2 } ^ { \mathrm { m } } \leq 1 - x ,$ so the total demand of the WSI is $D = x + y _ { 2 } ^ { \mathrm { m } }$ . Similar to the Case 1-2, we solve the profit maximization problem for the WSI. The optimal price and profit in this case are summarized as below.

(i) If $\mathfrak { t } \geq 2 ( P _ { 1 } + P _ { 2 } + c )$ and $( P _ { 1 } + P _ { 2 } + c + t ) / 3 t \leq x \leq 1 /$ 2, the optimal price and profit are the same as in Eq. (A2).

(ii) If $t \geq 2 ( P _ { 1 } + P _ { 2 } + c )$ and $0 \leq x \leq ( P _ { 1 } + P _ { 2 } + c + t ) / 3 t$ or if $\cdot 0 { \leq } t { \leq } 2 \ ( P _ { 1 } { + } P _ { 2 } { + } c )$ and $0 { \leq } x { \leq } ( t - ( P _ { 1 } +$ $P _ { 2 } + c ) ) / t ,$ the optimal price and profits are

$$
\begin{array}{l} P _ {3} ^ {*} = \frac {P _ {1} + P _ {2} + c + t (1 - x)}{2} \text { and } \\ \pi^ {*} = \frac {[ P _ {1} + P _ {2} + c + t (1 + x) ] ^ {2}}{4 t} \end{array}\tag{A3}
$$

(iii) If $0 \leq t \leq 2 ( P _ { 1 } + P _ { 2 } + c )$ and $t - ( P _ { 1 } + P _ { 2 } + c ) /$ $t \le x \le 1 / 2$ , the price and profits are

$$
\begin{array}{l} P _ {3} ^ {*} = P _ {1} + P _ {2} + c + t x \text { and } \\ \pi^ {*} = P _ {1} + P _ {2} + c + t x \end{array}\tag{A4}
$$

Case 1-4. If $P _ { 3 } \leq P _ { 1 } + P _ { 2 } + c + t x ,$ we have $y _ { 1 } ^ { \mathrm { m } } \geq x$ and $y _ { 2 } ^ { \mathrm { m } } \geq 1 - x .$ . This suggests that the WSI captures the whole market demand. In addition, if the WSI attracts all demand in market, it does not gain more profit if it lowers the price. Therefore, the bounding solution gives the optimal price and profit in this case, which is the same as in Eq. (A4).

By comparing the maximal profits in 1-2 Cases 1-3 Cases 1-4, we can determine the optimal profit $\pi ^ { * }$ for the WSI given any location x. Next, given the WSI’s optimal profit at any location x, the optimal location of the WSI is selected as the one that yields maximum profit.

Because the profit in Case 1-3 is conditional on the delay cost t, we determine the optimal location and profit for the WSI under different setting of t. First, we look at the scenario when $t \geq 2 ( P _ { 1 } + P _ { 2 } + c )$ . If $0 \leq x \leq ( P _ { 1 } + P _ { 2 } + c + t ) / 3 t$ , we need to compare the profits in Eqs. (A2) and (A3) to derive the optimal price and profit. It can be shown that the optimal profit is described in Eq. (A3). Note that the profit in Eq. (A3) is increasing in x. Therefore, the intermediary will set its location at the upper bound. In summary, the optimal location, price, and profit for the range $0 \leq x \leq$ $( P _ { 1 } + P _ { 2 } + c + t ) / 3 t$ are

$$
\begin{array}{l} \tilde {x} = \frac {P _ {1} + P _ {2} + c + t}{3 t}, \quad \tilde {P} _ {3} = \frac {2 (P _ {1} + P _ {2} + c + t)}{3}, \\ \tilde {\pi} = \frac {4 (P _ {1} + P _ {2} + c + t) ^ {2}}{9 t} \end{array} \tag {A}\tag{A5}
$$

In a similar manner, we compare the profits in Eqs. (A2) and (A4) for the scenario when $( P _ { 1 } + P _ { 2 } + c + t ) /$ $3 t \le x \le 1 / 2$ . Our analysis shows that the maximum profit is found in $\operatorname { E q . } \left( \operatorname { A 2 } \right)$ . Consequently, the optimal location, price, and profit for the range $( P _ { 1 } + P _ { 2 } + c + t ) /$ $3 t \le x \le 1 / 2$ are

$$
\begin{array}{l} \widehat {x} = \frac {1}{2}, \quad \widehat {P} _ {3} = P _ {1} + P _ {2} + c + 0. 5 t, \\ \widehat {\pi} = P _ {1} + P _ {2} + c + 0. 5 t \end{array}\tag{A6}
$$

By comparing the profits in Eqs. (A5) and (A6), we conclude that $x ^ { * } = 1 / 2$ is the optimal location for the WSI. This is because when $t \geq 2 ( P _ { 1 } + P _ { 2 } + c )$

$$
\begin{array}{l} \widehat {\pi} - \tilde {\pi} = \frac {0 . 5 t ^ {2} + t (P _ {1} + P _ {2} + c) - 4 (P _ {1} + P _ {2} + c) ^ {2}}{9 t} \\ \geq 0 \end{array} \tag {A7}
$$

The corresponding optimal price and profit are

$$
P _ {3} ^ {*} = P _ {1} + P _ {2} + c + 0. 5 t, \quad \pi^ {*} = P _ {1} + P _ {2} + c + 0. 5 t\tag{A8}
$$

Next, we consider the scenario when $0 \leq t \leq$ $2 ( P _ { 1 } + P _ { 2 } + c )$ . Following a similar solution procedure, we find that the optimal location is $x ^ { * } = 1 / 2$ and the corresponding price and profit are the same as in Eq. (A8).

To summarize the above two scenarios, the optimal location of the WSI is $x ^ { * } = 1 / 2$ , independent of the delay cost. In addition, the optimal price and profit is shown in Eq. (A8). By inspection, the optimal profits and prices are increasing in delay cost t and integration cost c. In addition, $\partial \pi ^ { * } / \partial c { > } \partial \pi ^ { * } / \partial t ,$ suggesting that integration cost has bigger impact on profit (and price ) than the delay cost.

Proof of Lemma 1. Note that the total cost to buy from the Web service intermediary (WSI) or to create the integrated Web service by buying S1 and S2 from individual service providers (SP) is determined by the customer’s and the WSI’s locations, see Eqs. (7) and (8). Therefore, we need to calculate the highest market penetration price ${ \bar { P } } _ { 3 }$ under four scenarios, i.e., the WSI is located in the AB, BC, CD, or DA segment. In each scenario, we consider demand of customers in AB, BC, CD and DA.

Scenario 1: The WSI is between A and B (0 V x V d)

For customers between AB, the total cost to buy from the SP is $P _ { 1 } + P _ { 2 } + c +$ td while the highest cost to buy from the WSI is $P _ { 3 } + t x$ if $0 \leq x \leq d / 2$ , or $P _ { 3 } + t ( d - x )$ if $d / 2 < x \leq d .$ Thus, the WSI attracts all customers between AB if $P _ { 3 } \leq \operatorname* { m i n } \{ P _ { 1 } + P _ { 2 } + c + t x ,$ $P _ { 1 } { + } P _ { 2 } { + } c + t ( d - x ) \}$ . Similarly, all customers between CD will buy from the WSI if $P _ { 3 } \leq P _ { 1 } + P _ { 2 } +$ $c + t ( 1 / 2 - d )$

For customers between BC, the cost to buy from SP and WSI are greater than the cost incurred by the customer at location B, but the increased cost is greater if buying from SP. This implies that if customer at point B will buy from WSI, all customers between BC will buy from the WSI too. Likewise, all customers between DA will buy from the WSI if the customer at location A prefers the WSI. In summary, the highest price the WSI can charge to capture all market demand is described in Eq. (9.1).

Scenario 2: The WSI is between B and C $( d < x \leq 1 / 2 )$

Due to similar argument as in scenario 1, the WSI captures the entire market demand in section AB if $P _ { 3 } \leq P _ { 1 } + P _ { 2 } + c + t ( d - x )$ while all customers between CD prefer the WSI if $P _ { 3 } \leq P _ { 1 } + P _ { 2 } + c + t ( 1 /$ $2 - 2 d + x )$ . In addition, all customers between BC will buy from WSI if the customer at location B buys from WSI and all customers between DA will buy from the WSI as long as customer at A prefers to buy from the WSI. Adding the fact that $d { < } x \leq 1 / 2$ and $d - x < 0$ , the highest price that could still capture the whole market is $P _ { 1 } + P _ { 2 } + c + t ( d - x )$

Scenario 3: The WSI is between C and D $( 1 / 2 <$ $x \leq 1 / 2 + d )$

Consider the marginal customer who is located between AB and diagonal to the WSI. The cost to buy from SP is $P _ { 1 } + P _ { 2 } + c + t d$ while the cost to buy from WSI is $P _ { 3 } + t / 2$ . Therefore, the customer will buy from WSI if $P _ { 3 } \leq P _ { 1 } + P _ { 2 } + c + t ( d - 1 / 2 )$ . For all other customers, they have a higher or equal cost to buy from SP while a lower cost to buy from WSI. Thus, they will all buy from WSI if the marginal customer buys from WSI.

Scenario 4: The WSI is between D and A (1/2 + $d \leq x < 1 )$

Similar to the argument in previous scenarios, all customers will buy from WSI if the customer at point B buys from the WSI. The highest price the WSI can charge is $P _ { 1 } + P _ { 2 } + c + t ( x - 1 )$ . 5

Proof of Lemma 3. We prove this lemma by induction. Let DN denote the reduced demand when the WSI raises its price above the market-covering price. First consider raising price to $\bar { P } _ { 3 } + t / N ( k { = } 1 )$ Because ${ \bar { P } } _ { 3 }$ is the highest market penetration price, there is one marginal customer who is indifferent between the WSI and the service providers. This marginal consumer will switch to the service providers if the WSI raises the price, i.e., DN = 1. At the same time, the customer next to the marginal customer but closer to the WSI becomes indifferent between the service providers and the WSI. Suppose we have $\Delta N \geq k - 1$ when $\Delta P _ { 3 } { = } ( k - 1 ) t / N$ and there is one marginal customer (denoted by $\theta _ { 0 } )$ . If we further raise the price by $t / N ,$ the marginal customer at $\theta _ { 0 }$ will switch to the service providers. At the same time, the customer next to $\theta _ { 0 }$ and closer to or further from the WSI becomes the next marginal customer. The WSI continues to loose customers in this way until all customers in market switch to the service providers. In summary, we have $\Delta N \geq$ min $\{ k , N \}$ when $\Delta P _ { 3 } = k t / N .$ If $k t / N { < } \Delta P _ { 3 } < ( k + 1 ) t / N ,$ it is similar to the case of $\Delta P _ { 3 } = k t / N$ except that one more customer switches to the WSI instead of becoming the kth marginal customer. 5

Proof of Proposition 2. We first prove that the market-covering price is optimal for the WSI if $t \leq 2 ( P _ { 1 } + P _ { 2 } + c )$ . When the price of the integrated service is ${ \bar { P } } _ { 3 } ,$ , the WSI obtains total profit $\pi = \bar { P } _ { 3 } N .$ . If the WSI sets a price below ${ \bar { P } } _ { 3 } ^ { }$ , it will lose profit because reducing price would not increase the WSI’s demand. On the other hand, if the WSI raises its price by $\Delta \bar { P } _ { 3 }$ , the WSI’s profit becomes

$$
\begin{array}{c} \pi = (\bar {P} _ {3} + \Delta P _ {3}) (N - \Delta N) \\ = \bar {P} _ {3} N + \Delta P _ {3} (N - \Delta N) - \Delta \bar {P} _ {3} \end{array}\tag{A9a}
$$

Obviously, if $\Delta P _ { 3 }$ is very large, all customers will switch to the service providers $( \Delta N { = } N )$ and the WSI has zero profit. We now restrict our attention when $\Delta N { < } N$ . Lemma 3 suggests that when $( k - 1 ) t /$ $N { < } \Delta P _ { 3 } { < } k t / N ,$ $\Delta N \ge k$ , thus $\Delta N \bar { P } _ { 3 } \geq k \bar { P } _ { 3 }$ . Further, we have $\Delta P _ { 3 } ( N - \Delta N ) { \leq } \Delta P _ { 3 } N { = } k t$ . According to the functional form of ${ \bar { P } } _ { 3 }$ in Lemma 1, we have $\bar { P } _ { 3 } { > } t \mathrm { ~ i f ~ } t { \le } 2 ( P _ { 1 } { + } P _ { 2 } { + } c )$ . Therefore, the WSI’s profit decreases when it charges a price higher than ${ \bar { P } } _ { 3 }$ regardless of its location x. Moreover, Lemma 2 suggests that if the WSI charges the highest marketcovering price ${ \bar { P } } _ { 3 }$ , it gains maximum profit if it is located between the service providers. In summary, the WSI’s total profit is maximized if it is located between the service providers and sets the price at ${ \bar { P } } _ { 3 }$ 5

Proof of Proposition 3. The highest market penetration price in Eq. (9.1) can be rewritten as follows.

$$
\bar {P} _ {3} = \left\{ \begin{array}{l l} P _ {1} + P _ {2} + c + t x, & \text { if } 0 \leq x \leq \frac {d}{2} \text { and } x \leq \frac {1}{2} - d \quad (\mathrm{A} 1 0 - a) \\ P _ {1} + P _ {2} + c + t (d - x), & \text { if } \frac {d}{2} \leq x \leq d \text { and } x \geq 2 d - \frac {1}{2} \quad (\mathrm{A} 1 0 - b) \\ P _ {1} + P _ {2} + c + t \left(\frac {1}{2} - d\right), & \text { if } d \geq \frac {1}{3} \text { and } \frac {1}{2} - d \leq x \leq 2 d - \frac {1}{2} (\mathrm{A} 1 0 - c) \end{array} \right.
$$

Note that if $d \ge 1 / 3$ , there could be multiple optimal locations $( 1 / 2 - d \le x \le 2 d - 1 / 2 )$ for the WSI because the price in Eq. (A10-c) is lower than in Eqs. (A10-a) and (A10-b). In addition, note that price in Eq. (A10-a) is increasing in x while the price in Eq. (A10-b) is decreasing in x. Therefore, the optimal location for the WSI is $d / 2$ for Eq. (A10-a) or (A10-b). In cases where there are multiple optimal locations, d/2 is in the range between $1 / 2 - d$ and $2 d - 1 / 2$ . In summary, $d / 2$ is the optimal location, regardless of the functional form of the optimal price ${ \bar { P } } _ { 3 } .$ 5

## References

[1] H.K. Cheng, Q.C. Tang, J.L. Zhao, Web Services Technology and Service-Oriented Application Provisioning: An Analytical Study of Three Market Strategies Warrington College of Business Administration, University of Florida, working paper, 2003.

[2] D. Erlenkotter, Facility location with price-sensitive demands: private, public and quasi-public, Management Science 24 (4) (1977) 378–386.

[3] C. Ferris, J. Farrell, What are Web services? Communications of the ACM 46 (6) (2003) 31.

[4] X. Geng, Y. Huang, A.B. Winston, Smart marketplaces: a step beyond Web services, International Journal of Information Systems and e-Business Management 1 (1) (2003) 15 – 34.

[5] K. Gottschalk, S. Graham, H. Kreger, J. Snell, Introduction to Web services architecture, IBM Systems Journal 41 (2) (2002) 170– 177.

[6] J. Hagel III, J.S. Brown, Your next IT strategy, Harvard Business Review, (2001 (Oct.)) 105– 113.

[7] J.M. Johansson, On the impact of network latency on distributed systems design, Information Technology and Management 1 (3) (2000) 183 – 194.

[8] J.M. Johansson, S.T. March, J.D. Naumann, The effects of parallel processing on update response time in distributed database design, Proceedings of International Conference on Information Systems, 2000, pp. 187– 196.

[9] B. Li, M.J. Golin, G.F. Italiano, X. Deng, On the optimal

placement of Web proxies in the Internet, Proceedings of IEEE INFOCOM, 1999, pp. 1282– 1290.

[10] Q. Liu, V.N. Padmanabham, G.M. Voelker, On the placement of Web server replicas, Proceedings of IEEE INFOCOM, 2001, pp. 1587– 1596.

[11] Y. Sun, A location model for web services intermediaries. Warrington College of Business Administration, University of Florida, doctoral dissertation, 2003.

[12] Y. Sun, G.J. Koehler, A location model for web services intermediaries. California State University, San Marcos working paper, 2003.

![](/api/attachments/SKC6TYDR/fulltext/images/4b29116d7b883114b6b5f5c51a71bc95d16d7b9082d11406cf69656c0138e5f7.jpg)  
Ms. Qian ‘‘Candy’’ Tang is a PhD candidate at the Department of Decision and Information Sciences of Warrington College of Business Administration at the University of Florida. She received her MS degree in DIS from University of Florida in 2003. Her research interests include economics of Information Systems and the impact of IT on firm strategies. She is a member of AIS, DSI and INFORMS.

![](/api/attachments/SKC6TYDR/fulltext/images/08764640008f1e2d96886f616f60e22113fee77708bda4075d56a84e4148a155.jpg)

Dr. Hsing ‘‘Kenny’’ Cheng is Associate Professor of Information Technology and the American Economic Institutions Faculty Fellow at the Department of Decision and Information Sciences of Warrington College of Business Administration at the University of Florida. Prior to joining UF, he served on the faculty at The College of William and Mary from 1992 to 1998. He received his PhD in computers and information systems from William E. Simon

Graduate School of Business Administration, University of Rochester in 1992. Dr. Cheng’s work has appeared in Computers and Operations Research, Decision Support Systems, European Journal of Operational Research, IEICE Transactions, Information Technology and Management, International Journal of Web Services Research, Journal of Business Ethics, Journal of Information Systems and e-Business Management, Journal of Management Information Systems, and Socio-Economic Planning Sciences. Dr. Cheng is a member of ACM, AIS, DSI, and INFORMS. He is a program cochair of the Second Workshop on e-Business, 2003.
