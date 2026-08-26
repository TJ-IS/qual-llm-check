---
otero_id: 1316
otero_key: "ZV6GXU4S"
title: "Multi-agent system approach to context-aware coordinated web services under general market mechanism"
authors: "OhByung Kwon"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.07.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Multi-agent system approach to context-aware coordinated web services under general market mechanism

OhByung Kwon<sup>\*</sup>

School of Management and International Relations, Kyunghee University Sochen-ri 1, Giheung-eup, Yongin-si, Gyunggi-do, 449-701, Korea Received 18 June 2003; received in revised form 25 July 2004; accepted 26 July 2004 Available online 11 September 2004

## Abstract

Web services have been emerging as a new business opportunity over the last few years. However, these web services are still passive, often lacking rich representations and rich strategies to attract customers. This paper proposes a context-aware coordinated web service mechanism for autonomous and intelligent service provision. Multi-agent intelligent architecture is adopted to coordinate web services that are federated in a web service coordinator, which is also an agent. To provide more effective advertisement and at the same time guarantee higher profits, case-based reasoning is applied to automatically estimate user preferences. We describe a proof-of-concept prototype that was developed using JATLite. Using a simulation-based experimental study performed with an illustrative example, we found that our mechanism with multi-agents yields higher levels of user preference, higher overall profit across all federating merchants, and an increased rate of wins than current web service mechanisms, which do not include these features. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Web service; Multi-agent intelligent system (MAIS); Case-based reasoning; Context-awareness

## 1. Introduction

The number of users of mobile terminals (phones, PDAs, and communicators) is increasing rapidly. The miniature size of mobile terminals, and the fact that they easily fit into a pocket, makes them an ideal channel for offering personalized and localized services to mobile users. Mobile commerce creates a broad range of new business opportunities, such as content and service providers.

One potential business opportunity includes suggesting products to shoppers who are walking around, by providing them with access to web services through mobile devices. In the past, there has not been communication or competition in real-time between off-line sellers and on-line sellers. However, if buyers carry their own wireless devices, they can compare products online even when they are shopping at a traditional brick-and-mortar shop. If this kind of ubiquity and <sup>b</sup>reachabililty<sup>Q</sup> is incorporated, buyers may increase their satisfaction level by making more informed purchases—whether with on- or off-line businesses.

However, there are very few web services that, on behalf of their owners, can autonomously negotiate with shoppers. Current web services can only provide ads such as product description, price, discount, and other conditions as a seller inputs them. To increase customer satisfaction, web services may dynamically vary products’ selling conditions by observing customer preferences and behaviors. For example, some buyers may be prioritizing on price, and others may see product qualities as the more important factor.

These lead to the motivation to build an intelligent system that can successfully provide an advertisement suitable enough to sell its own products, and at the same time to yield a profit for itself. As a result, the prompt and adaptive mobile web service requires intelligence and autonomy. These naturally lead us to apply intelligent agent-based systems. It is well known that the type of agent plays a significant role in facilitating electronic market [16]. While researchers proposed an earlier agent-based mobile commerce prototype [10,15,32,33,35,36,51], the prototype system did not provide scalability or interoperability, both of which are crucial for realistic automated transactions, particularly in a mobile setting.

Meanwhile, the general market mechanism, which has been widely accepted to analyze multiple-agent systems, is basically assumed to describe a market. However, when considering context-awareness, the base mechanism does not consider some important features: (1) the fact that consumer’s utility function is not known mathematically to the sellers, and (2) the mobility of the consumer. The consumer’s utility is ever changing according to the location of the consumer and the location of sellers. Since location is one of the core components in a traditional marketing product mix, web services need to be intelligent enough to not just estimate the consumer’s utility as accurately as possible, but also dynamically adjust itself to the consumers’ current contexts. In our mechanism, these two features are considered.

Hence, this paper proposes a context-aware coordinated web service that meets the requirements mentioned above for mobile shopping. We adopted a multi-agent intelligent system (MAIS) architecture for the following reasons. First, we assume that many web services are ready to service a request that is delivered by a Web Service Coordinator (WSC), which gives federating web services more chances to successfully match the product to a customer’s preference and at the same time incur less risk. Secondly, an intelligent agent can contain transaction rules to intelligently and autonomously produce advertisements under the delegation of its human owner(s). Finally, to come up with different buyers’ diverse preferences, personalization is needed. Personalization, to a very limited extent, is already available today and an agent system can make it possible. Agent technology has already been used with client/server models and their extensions to build mobile commerce applications [39].

A case-based reasoning (CBR) capability is also included in our prototype, since we assume that a user’s utility function is hardly represented as a mathematical function. CBR is an AI methodology that provides the foundations of a technology for intelligent systems [18]. The methodology consists of indexing cases, retrieving the best past case from memory, adapting the old solution to conform to the new situation, testing whether the proposed solution is successful, and learning to prohibit solution fails. CBR has been viewed as a technology for automated, intelligent problem solving [44].

We have developed a prototype system and an experiment to illustrate the possibility of the mechanism proposed in this paper. Experiments by simulation will be described if the proposed mechanism is relatively competitive.

The rest of this paper is organized as follows. Section 2 reviews existing research on comparative shopping. In Section 3, we describe our multi-agent framework and architecture with an agent behavior algorithm. In Sections 4 and 5, we present a prototype system and experimental analysis to show the feasibility of the idea, and we conclude in Section 6.

## 2. Literature review

## 2.1. General market mechanism

The general equilibrium theory has recently been successfully adapted in computation multi-agent systems in many application domains [47]. Prices may change, and the agents may change their consumption and production plans, but actual production and consumption only occur once the market has reached a general equilibrium. They say that $( p ^ { * } , x ^ { * } , y ^ { * } )$ is a general (Walrasian) equilibrium if markets clear: $\begin{array} { r } { \sum _ { i } x _ { i } ^ { * } = \sum _ { i } e _ { i } + \sum _ { j } y _ { j } ^ { * } } \end{array}$ , and each consumer i maximizes its preferences given the prices:

$$
\begin{array}{l} x _ {i} ^ {*} = \arg \max \\ \qquad \times \left(u _ {i} (x _ {i}) | x _ {i} \in R _ {+} ^ {n}, p ^ {*} x _ {i} \leq p ^ {*} e _ {i} + \sum_ {j} \theta_ {i j} p ^ {*} y _ {j}\right), \end{array}
$$

and each producer j maximizes its profits given the prices:

$$
y _ {j} ^ {*} = \arg \max \left(p ^ {*} y _ {j} | y _ {j} \in Y _ {j}\right)
$$

where $u _ { i } ( x _ { i } ) , x _ { i } { = } [ x _ { i 1 } , x _ { i 2 } , . . . , x _ { i n } ] ^ { T } ,$ , where $x _ { i g } { \in } R .$ <sub>+</sub> is consumer $i \ ' \mathrm { s }$ allocation of good $g , p { = } [ p _ { 1 } , p _ { 2 } , . . . , p _ { n } ]$ where $p _ { g } { \in } R$ is the price for good $g , e _ { i } { = } [ e _ { i 1 } , e _ { i 2 } , . . . ,$ $e _ { i n } ] ^ { T } ;$ , where $e _ { i g } { \in } R$ is consumer $i \ ' \mathrm { s }$ endowment of commodity $g . \bar { y _ { j } } { = } [ y _ { j 1 } , y _ { j 2 } , . . . , y _ { j n } ] ^ { T }$ is the production vector, where $y _ { j g }$ is the amount of good g that producer j produces. The profit of producer j is $p ^ { * } y _ { j } .$ where $y _ { j } { \in } Y _ { j }$ . Let $\theta _ { i j }$ be the fraction of producer j that consumer i owns.

It is well known that the general equilibrium solutions from these equations have some very desirable properties such as Pareto efficiency, coalitional stability, existence, and uniqueness under gross substitutes.

## 2.1.1. Extension of general equilibrium

Some of the producers may coordinate to save costs. In this case, the Nash equilibrium is often too weak because subgroups of agents can deviate in a coordinated manner. The String Nash equilibrium is a solution concept that guarantees more stability [4].

Under unlimited and costless computation, each coalition would solve its optimization problem, which would define the value of that coalition. However, in practice, in many domains it is too complex from a combinatorial viewpoint to solve the problem exactly. Instead, only an approximate solution can be found. In this paper, we adopted case-based reasoning.

Additionally, our model includes the following features:

(1) The consumer’s utility is a function of the producers’ price and quality, where quality is an association of some features such as installment program, brand power, etc. The function is assumed to not be predefined.

(2) The contextual data, such as weather, calendar, and distance between consumer and merchant, affect the consumer’s utility.

## 2.2. Context-aware computing

As Steve Mann first used the term humanistic intelligence, successful implementation has appeared since the late 1990s [27]. Context is a powerful concept in human–computer interaction [14]. More specifically, user context <sup>b</sup>is any information that can be used to characterize the situation of an entity<sup>Q</sup> [13]. Context includes but is not limited to the location of use, the collection of nearby people and objects, accessible devices, and changes to these objects over time. It may include lighting, noise level, network connectivity, communication costs, communication bandwidth, and even social situations.

The term context-aware computing is commonly understood by those working in ubiquitous/pervasive computing, where it is felt that context is key in their efforts to disperse and transparently weave computer technology into our lives. One goal of context-aware computing is to acquire and utilize information about the context of a device in order to provide services that are appropriate to the particular people, place, time, events, etc.

Context-aware computing is becoming more crucial in mobile distributed computing systems. These systems aim to provide people with ubiquitous access to information, communication and computation. For example, CAMP (Context-Aware Mobile Portal) is a modular mobile Internet portal enhanced with context awareness features, such as user preferences, location and temperature [26]. Location-aware applications are other examples of context-awareness which take advantage of locationawaking sensors. Some excellent work in this area includes PARCTab at Xerox PARC [46], the InfoPad project at Berkeley [22], the Olivetti Active Badge system [39] and the Personal Shopping Assistant proposed at AT&T [3].

Automatic contextual reconfiguration and contexttriggered actions are core categories in context-aware applications [38]. Automatic reconfiguration is the process of autonomously adding new components and removing existing components, based on contextual information. Context-triggered action means that certain actions, which we define as patterns in this paper, are activated according to the change of context. Schilit used IF THEN rules to implement the feature. Tewari et al. [43] considered location context to develop agent-based electronic commerce. They addressed the location sensitive decision support system using agents and tried to apply it to the restaurant recommendations examples.

## 2.3. Web services

Current computer-based electronic commerce prototype systems have usually used agent technology. Since agent’s autonomous, intelligent, and cooperative features well fit to automated transaction between sellers and buyers, the agents are regarded as a candidate to substitute or at least support human traders. However, even though there have been lots of suggestions how to apply agent technologies to electronic commerce [10,32,35,36,43,51], they have seldom addressed the main limitations of agent-based transaction: scalability and interoperability. To resolve these limitations, web service could be one of the good candidates to be conjointly used with agent technology.

A web service interacts with its environment through a collection of operations that are networkaccessible through standardized XML messaging. A web service is described by an XML-based service description that covers all of the details that are necessary to interact with the services, including message formats, transport protocol and location [5]. The web service mainly aims to increase the service productivity on the web by providing reusable service components [50].

The two primary currently emerging web services infrastructure standards are J2EE and .NET. HP’s Application Server, BEA’s WebLogic, IBM’s Web-Sphere are examples of J2EE-compliant application servers that combine web server farms with EJB engines. Services are performed through Web Services Description Language (WSDL) interfaces, registering these services at Universal Description, Discovery, and Integration (UDDI) operator sites and communicating with clients and other web services through SOAP messaging [9,11].

Personalization has been emerging as a hot issue to increase the usability of web services. Applying agents as delegated service discovery, adapting their behavior based on the dynamic characteristics of the web services in the user’s context, carrying out complex interactions with multiple services are expected to be realized [20]. Web service discovery and synthesis have been considered as crucial for successful implementation of agent-based web services [5,7].

Automated business transaction is another vision of web services. To do so, the web services may want to share common concepts with each other for better communication. To avoid obtrusive interaction with users, the web service should also be autonomous with delegation allowed. These naturally require some emerging technologies such as semantic web and agent technology in conjunction with web services such as semantic web service and agent-oriented web service. Semantic web services are frequently addressed to make dynamic Enterprise Integration (EI) and Virtual Enterprises (VE) [31]. Semantic service descriptions is a meaningful research issue [1,2,21]. Agent-oriented semantic web services are also an interesting field of research [34].

Consequently, web services will make it easier to build systems such as the one we propose. At the same time, existing web services fall short when it comes to supporting context-aware elements.

## 3. Multi-agent system approach to context-aware coordinated web services

## 3.1. Framework

A multi-agent intelligent system is utilized in this paper for modeling coordinated web services. It is suitable for describing the coordinating and negotiating nature of sellers in a market. Negotiation is a process that takes place between two or more agents who are attempting to achieve goals when they cannot achieve their own original goals. Since these goals may conflict, they have to communicate between themselves to achieve the goals [37]. Multi-agent systems offer a new dimension for coordination and negotiation in an enterprise. Incorporating autonomous agents into the problem-solving process allows improved coordination of different functional unitdefined tasks, both independent of the user and of the functional units under control [6,8,17,19,28,31,40– 42,45,48,49]. Under a multi-agent system, the problem-solving tasks of each functional unit become populated by a number of heterogeneous intelligent agents with diverse goals and capabilities [23,24, 29,45,49].

In this paper, we have assumed a system that consists of multiple buyer agents (B-agents), multiple coordinating sellers (Coordinating Web Services), multiple non-coordinating sellers, one web service coordinator (WSC), and one negotiator (Negotiator). The agents are defined by the following set of characteristics (1–6).

$D _ { j } { \mathrm { - } } \mathrm { V }$ ector of offerings provided by Coordinating

$$
\text { Web   Service } j = \langle e _ {j 1}, e _ {j 2}, \dots , e _ {j n} \rangle\tag{1}
$$

where $e _ { j k }$ , 1VkVn denotes kth element to advertise by Coordinating Web Service j.

For example, a web service may have a vector of offerings like hproduct<sup>\_</sup>name, price, selling <sup>\_</sup>location, shipping<sup>\_</sup> condition, year <sup>\_</sup> produced, user <sup>\_</sup> ratingi, which instance might be h(DigitalCamera#200, \$299, TX, buyer<sup>\_</sup>pays, 2003, \*\*\*\*i, h(DigitalCamera#201, \$249, TX, buyer<sup>\_</sup>pays, 2001, \*\*\*i, etc.

$$
\begin{array}{l} C _ {j} \text {- - - Vector of contextual information of Buyer} \\ i = \langle c _ {i 1}, c _ {i 2}, \dots , c _ {i m} \rangle \end{array}\tag{2}
$$

where $c _ { i l } ,$ 1VlVm denotes lth contextual data of Buyer i. For example, current contextual information of a buyer might be like hclimate, temperature, zip<sup>\_</sup>code, current<sup>\_</sup>activityi: e.g. hsunny, 45F, 15213, freei.

$$
\begin{array}{l} U _ {i} \text {- - Buyer i^{\prime} s utility function about Coordinating} \\ \text { Web Service j = u_{i} (D_{j}, C_{i})} \end{array}\tag{3}
$$

In this paper, we assume that any sellers and buyers do not know the utility function. However, they are allowed to collect the past transaction history.

$$
\begin{array}{l} U P _ {j} \text {- - - - - Seller j^{\prime} s unit profit function of current} \\ \text { offerings } = p _ {j} - U C _ {j} \end{array}\tag{4}
$$

$$
\begin{array}{l} U C _ {j} \text {- - - - - Seller j^{\prime} s unit cost function of current} \\ \text { offerings } = \text { unit\_cost\_of\_last\_offering} _ {j} \\ \quad + \sum_ {k = 1} ^ {n} \left(\text { charge\_of\_cost} _ {j} (\Delta e _ {k})\right) \end{array}\tag{5}
$$

Regarding Eq. (5), the unit cost function is a sum of the unit cost of last offered product and the change of cost by changing the n elements from last offering to current offering. Remember that the coordinated web services are delegated to change the current offerings such as price, quality, and condition autonomously.

The overview of our framework is shown in Fig. 1. The Web Service Coordinator (WSC) is always listening to any B-agent, which wants to find comparative goods that are proposed through the web services. The B-agent can be downloaded and resides in the buyer’s mobile device. When the buyer goes shopping and finds a candidate product for purchase, he/she may get a personal B-agent that will assist him/her in finding other similar products at competing stores/merchants with a competitive condition exist in other shops. The B-agent then subscribes a new request to the WSC so that it may introduce some other agents who are interested in proposing the same or similar goods with a better condition. The WSC first selects a set of Coordinating Web Services by querying a self-contained information repository. Secondly, the request from the B-agent is streamed to the selected Coordinating Web Services.

We started from adopting the price tatonnement process, which is a steepest descent search method to reach a general equilibrium, for distributed search for a general equilibrium [30], and revised it to fit our assumption:

(1) The consumer’s utility is a function of the producers’ price and quality, where quality is an association of some features such as installment program, brand power, etc. The function is assumed not to be predefined.

![](/api/attachments/ZV6GXU4S/fulltext/images/c4157fc78ad4677eb5ddfe2ee172b20703f7c7f2ce50b572482617b091b25ebd.jpg)  
Fig. 1. Overview of the General Framework.

(2) Contextual data, such as distance between consumer and producer, affect the consumer’s utility as already described above in Eq. (3).

The ultimate goal of the negotiation in this system is to realize win–win situations between the B-agent and the Coordinating Web Service. The B-agent may get more competitive goods than what the buyer is actually seeing at that time. The Coordinating Web Service can increase total sales and profits by encompassing new buyers by a WSC. The WSC will also maximize the rate of successful contracts between the B-agent and the Coordinating Web Service via the Negotiator. To do so, the WSC should:

– provide information on what a buyer wants as specifically and accurately as possible;

– encourage the Coordinating Web Services to make more attractive offers;

– select a best offer in terms of user preference, total profit and rate of wins among the offers from coordinating web services;

– forward the best offer to the B-agent via the Negotiator.

The first goal is closely related to how correctly the Coordinating Web Service fits buyers’ preferences. The Coordinating Web Services, though, do not know the correct buyers’ utility function because it is nearly impossible to have a considerable number of the buyers profiles ahead of time. However, it would be reasonable that the agents may remember the previous bidding results. Therefore, we put a case base to the WSC. Table 1 shows a representative subset of the property features that are used in our architecture. Among these features, contextual information such as location, weather, and calendar is acquired from a context database, the context of which is arriving externally.

The similarity between a new problem and a case in memory is computed is as follows Eq. (6):

$$
\text { Similarity } (t, c) = \sum_ {i = 1 \dots n} w _ {i} ^ {*} \text { sim } (t _ {i}, c _ {i}),\tag{6}
$$

where t indicates a target advertisement, c stands for case and w denotes the weight of the ith element of an advertisement. Hence, sim $( t _ { i } , ~ c _ { i } )$ is a similarity of the ith element of an advertisement.

Subset of the property features in case base

<table><tr><td colspan="2">Attribute</td><td>Value type</td></tr><tr><td>Case No</td><td></td><td>Integer</td></tr><tr><td>Product ID</td><td></td><td>Integer</td></tr><tr><td>Product Description</td><td></td><td>Text</td></tr><tr><td>Seller ID</td><td></td><td>Integer</td></tr><tr><td>Price</td><td></td><td>Integer</td></tr><tr><td>Level of quality</td><td></td><td>Integer, range(1..7)</td></tr><tr><td>Level of condition</td><td></td><td>Integer, range(1..7)</td></tr><tr><td>Preference</td><td></td><td>Integer</td></tr><tr><td>Customer description</td><td></td><td>Text</td></tr><tr><td>Contextual information</td><td>Location of buyer</td><td>Vector of integer</td></tr></table>

To reach the second goal, each of the Coordinating Web Services which receives the request is encouraged to start a cost/benefit analysis to optimize its own unit profit by changing some decision parameters involved in its own cost function:

Maximize Total<sup>\_</sup>Profit=Sales Volume\*(Unit Price Unit Cost)

subject to:

Suggesting condition must be within the delegation area.

Suggesting condition must be better than any other conditions made by any other Coordinating Web Services and initial condition.

For autonomous negotiation, each Coordinating Web Service is delegated to some extent by its own user. For example, the lowest price allowed by the user is informed and the corresponding Coordinating Web Service can negotiate by modifying its own price condition unless it violates the allowable price level.

## 3.2. Negotiator

As shown in Fig. 2, the Negotiator consists of the interface, the ACL parser, a message encoder/ decoder, and a negotiating processor with working memory. We adopted standard Knowledge Query and Manipulation Language (KQML) as the agent-toagent communication language (ACL) to represent a speech act. An agent communication support tool such as JATLite provides the functionality to autonomously send and receive messages via TCP/IP. The ACL parser parses incoming messages which contain the receiver’s name, ontology, language used, and message content. The message encoder/decoder interprets the contents of the incoming message or encodes the outgoing message’s content in ACL language format.

![](/api/attachments/ZV6GXU4S/fulltext/images/adbd1ea8bca71bcf7630da43bf6a0378304b391a2f95d8dbcf74cb0dd58c04d9.jpg)  
Fig. 2. Architecture of Negotiator.

The negotiating processor receives the original advertisement from user agents, and multicasts the advertisement to every web service in a federation. Until the best advertisement is selected and announced to the user agent, whole advertisements are stored in the working memory. The working mechanism of negotiating processor is as follows:

Here is the logic outline for the negotiator algorithm:

Get an initial offer $D _ { 0 }$ from a B-agent i, where i is an ID of it’s owner

## Repeat

Broadcast $D _ { 0 }$ to all sellers participating: simple web services and WSC

Receive the offers $\scriptstyle D = \langle D _ { 1 } , D _ { 2 } , \dotsc , D _ { n } \rangle$ from the sellers

Broadcast the offers D to the B-agent i

Receive a consumption plan $x _ { i }$ from the B-agent i Until $\textstyle | \sum _ { i } { \big ( } x _ { i } - e _ { i } { \big ) } - \sum _ { i } D _ { j } | < \varepsilon$

Inform the B-agent and sellers that an equilibrium has been reached.

## 3.3. Web service coordinator (WSC)

The WSC communicates with coordinating web services so that they may gain maximum profit. To do so, the WSC provides case-base and contextual information to the coordinating web services, and determines which advertisement of web service will be returned to the Negotiator. As shown in Fig. 3, the WSC consists of the interface, the context parser, the ontology parser, the ACL parser, and a global optimization module with a case-based reasoning function. Assuming the original shop’s location is acquirable on the web, which is another kind of web service, the context parser acquires the location information and passes it to the global optimization module. The ontology parser may be necessary in order to understand the meaning of terms contained in an incoming ACL message, which is parsed by the ACL parser. The global optimization module compares the advertisement that is suggested by the coordinating web services, and waits until there is only one best advertisement remaining.

![](/api/attachments/ZV6GXU4S/fulltext/images/ba962f56d2cf5cdb0c8a99719ef04c9d45f6cc5c706db17e4dd755226df8a4e2.jpg)  
Fig. 3. Architecture of WSC.

When the Negotiator asks the WSC if it can produce a better deal than the original advertisement, the WSC estimates the buyer’s current preference for the product by case-based reasoning. Then the WSC retrieves the data set of those buyers who also treat the same or similar products from the buyer table in the information repository. Then WSC initializes a set of candidates who will participate with the deal. The communication between the WSC and Coordinating Web Services is continued until only one candidate remains. The algorithm for WSC is described as follows:

Here is the logic outline for the WSC algorithm:

## Repeat

Receive $D _ { 0 }$ from the negotiator

Compute approximate utility, u˜ , of the consumer i using case base and $D _ { 0 }$

Let $D _ { L } ^ { * } { = } D _ { 0 } .$ , where L is an ID of WSC

Repeat

Broadcast $D _ { L } ^ { * }$ to member Coordinating Web Services

Receive offer $D _ { j }$ from each Coordinating Web Service j

Compute approximate utility to $D _ { j }$

Determine current optimal advertisement as $D _ { L } ^ { * }$

Until no other advertisement from member Coordinating Web Services

outperforms $D _ { L } ^ { * }$

Announce to the negotiator an advertisement $D _ { L } ^ { * }$

Until informed that an equilibrium has been reached

Exchange and produce.

## 3.4. Case-based reasoning

Case-based reasoning (CBR) is an AI methodology that provides the foundation for intelligent systems technology. It has been used to develop multiple systems applied in a variety of domains, including manufacturing, design, law, and battle planning [18]. CBR is recommended to developers who are challenged to reduce the knowledge acquisition task, to avoid repeating mistakes made in the past, to reason in domains that have not been fully understood or modeled, to learn over time, and to reason with incomplete or imprecise data and concepts [25]. These are some of the challenges faced by developers of weather forecasting systems [12].

The most important functionality of CBR is retrieval. Retrieval is based on the similarity between the descriptions of the target query and those of case included the case base. For CBR, we have developed our prototype system based on Fagan and Bloor’s model [15]. The similarity factor is as follows:

$$
\text { Similarity } (t, c) = \frac {\sum_ {i = 1 , \dots , n} w _ {i} ^ {*} \operatorname{sim} \left(t _ {i} , c _ {i}\right)}{\sum_ {i = 1 , \dots , n} w _ {i}}
$$

where t is target query, c is case, w is weight, and

$$
\begin{array}{c} \operatorname{sim} (t _ {i}, c _ {i}) = \operatorname{mmw} (t _ {i}, c _ {i}) + \frac {\operatorname{msf} (t _ {i} , c _ {i})}{\operatorname{tsf} (t _ {i} , c _ {i})} (\operatorname{mw} (t _ {i}, c _ {i}) \\ - \operatorname{mmw} (t _ {i}, c _ {i})) \end{array}
$$

where mw, mmw, msf, and tsf denotes match weight, mismatch weight, the number of matching subfeatures of feature (target), and the total number of subfeatures, respectively. The vector of target query and case is: hproduct information, context, user ratingi. For example, price, brand, and color would be a set of product information. Current user location is a useful context to calculate the perceived distance from the user, and a shop that sells a product that the user wishes to purchase.

## 3.5. Web services

## 3.5.1. Simple web service

In general, a producer or seller receives a buyer’s needs and then determines a production plan that may maximizes total profit. The algorithm of the Simple Web Service behavior is shown in Fig. 4.

The algorithm is shown as follows:

Algorithm for Simple Web Service k:

Repeat

Receive $D _ { 0 }$ from the negotiator

Announce to the negotiator an offer $D _ { k } ^ { * }$ that maximizes $\scriptstyle \pi _ { k } = p _ { k } - U C _ { k }$

Until informed that an equilibrium has been reached

Exchange and produce.

## 3.5.2. Coordinating web service

According to the value of method derived from the WSC, those relevant methods in Coordinating Web Service and B-agent begin to work. The algorithm of the Coordinating Web Service behavior is shown in Fig. 5. A Coordinating Web Service first gets delegation data from the individual database. By fixed interval or special request from its owner, the delegation data may be updated for the time being.

![](/api/attachments/ZV6GXU4S/fulltext/images/bf40fcc70c96a908af244dd514989a0fbee19380683afff6f75c481f40bb125a.jpg)  
Fig. 4. Architecture of a simple web service.

![](/api/attachments/ZV6GXU4S/fulltext/images/d794cbfe853e784b9afefe7de27bf80071477cd5ee621ed3d0eb88d946818046.jpg)  
Fig. 5. Architecture of Coordinating Web Service.

The main role of the Coordinating Web Service is to provide better conditions for a new subscription from the WSC. The Coordinating Web Service can autonomously change price or quality level while satisfying given delegation constraints. If a better condition is found, then a new suggestion is prepared and then sent to the WSC. If not, a quitting sign is issued for withdrawal.

Algorithm for Coordinating Web Service k:

Repeat

Receive $D _ { L } ^ { * }$ from the WSC

Apply fast search algorithm

Announce to the WSC an advertisement $D _ { k }$ that maximizes

$$
\pi_ {k} = p _ {k} - U C _ {k}
$$

Until informed that an equilibrium has been reached

Exchange and produce

Fast search algorithm for Coordinating Web Service k:

Estimate preference of best advertisement

If the preference is better than the preference of $D _ { L } ^ { * }$ proceed to next

Otherwise, give up offering

Repeat

Set quality and condition as best

Acquire estimated preference by changing price only

Until estimated preference becomes higher than the preference of $D _ { L } ^ { * }$

![](/api/attachments/ZV6GXU4S/fulltext/images/ebf6cd1b53d395c24db32d7d76ce2c8f0212d324ff6fb662c33d6f244c52245d.jpg)  
(d) Interactivity of the agents  
Fig. 6. Example screenshot.

## 3.6. B-agent

The main contribution of the B-agent is to keep the current best condition, compare it with a new condition that arrives from the WSC, and finally, to select the best condition on behalf of the user from among a sequence set of conditions. Since the objectorientation has encapsulation capability, the agents do not need to know each other’s internal algorithms. They only pass input and output messages to each other. Similarly, the B-agent stands for its client and conducts a pursuit of the client’s preference. Its algorithm is depicted as follows:

Algorithm for consumer i:

Initiate initial offer $D _ { 0 }$ and send it to the negotiator Repeat

Receive D form the negotiator

Announce to the negotiator a consumption plan $\boldsymbol { x } _ { i } { \in } \boldsymbol { R } _ { + } ^ { n }$ that

maximizes $u _ { i } ( x _ { i } ) { = } u _ { i } ( p , ~ q , ~ c , ~ d )$ given the budget constraint, where $\begin{array} { r l } { p , } & { { } q , \ c } \end{array}$ and d denotes price, quality, condition, and distance, respectively

Until informed that an equilibrium has been reached

Exchange and consume.

## 4. Implementation

Our proposed prototype, CAMA-WS (Context-Aware Multi-Agent-Based Web Service system), was implemented using Java under JDK1.4.1 and tested on several networked PC platforms. The case base and other data tables are made in Microsoft AccessR 2000 and linked using ODBC/JDBC connections. The agent communication module is implemented in JATLite and ACL-LITE. JATLite is a package of programs in Java that allow quick creation of agent systems that communicate robustly over the Internet. JATLite consists of four layers: abstract, base, KQML, and router. We embedded coordination logic within a method in the RouterClientAction class of the router layer. Using JATLite, we perform agent-to-agent communication with diverse services. JATLite provides message sending, message queuing, agent naming service, agent security, etc. The JATLite directly supports a KQML parser. The JATLite provides various templates for creating agent clients. Reusing the same template, therefore, we created the Negotiator, WSC, Coordinating Web Services agents.

Fig. 6 shows some sample screen shots of the prototype system. In this scenario, the user may stop by a traditional brick-and-mortar shop that is offline, and eventually be motivated to buy items in the category <sup>b</sup>clothes-women<sup>Q</sup>. The user clicks <sup>b</sup>Request $\mathrm { \ A d s ^ { \circ } }$ on the PDA, and the user interface program on behalf of the user visits the relating URI to get ontology information on <sup>b</sup>clothes-women<sup>Q</sup>. Then the system dynamically displays the item vector: it is not hard-coded but generated according to the property data in the ontology (Fig. 6a). When the user types values of the product that he/she is looking at and clicks on the <sup>b</sup>get recommendation<sup>Q</sup> button, the interface program calls the Negotiator to address the user’s request (Fig. 6b). The lower-right window of Fig. 6d shows the Negotiator agent program. The Negotiator gets client information and an original advertisement. The client information that came from the B-agent consists of customer ID, location, and arrival time. In the current version, the B-agent only generates user information. The user gets information that may be directly obtained from his or her mobile device, such as a PDA. The arrival time is generated by the Java function: System.currentTimeMillis(). The product information consists of product ID, price, level of quality, and level of condition. Then KQMLformatted ACL messages are generated and delivered to all web services. An example of the ACL message is as follows:

<sup>b</sup>ask-one

:sender Negotiator :receiver WSC :language KQML :content (1 1 0 21 103 1024 2 4)<sup>N</sup>

Once the message is constructed, it is then sent to the web services through the router. The router is a built-in program that runs constantly in JATLite, and administers the agent communication. The two upperright windows are simple web services and the lowerleft window is the WSC. The WSC recognizes the message, and if the message comes from a negotiator, it immediately generates ACL messages and then sends them out to the coordinating web services, which are shown in upper-left windows. The coordinating web service confirms whether the message has arrived safely, and then finds the best advertisement to arrive at a local optimum. When all responses have been collected from coordinating web services, the WSC compares and chooses an advertisement that can reach a global optimum. Once this phase is complete, the WSC sends an ACL message to Negotiator as follows:

<sup>b</sup>reply:sender WSC :receiver Negotiator :language KQML :content (1 1 5 20 100 2000 1 6 6 131 582 719 0)<sup>N</sup>

Finally, the Negotiator returns a winner’s ads to the interface program (Fig. 6c).

To successfully provide an advertisement suitable enough to sell its own products, we have used two technologies: ontology and case-based reasoning. First, features that affect the user purchasing behavior are articulated by marketing experts, and our system enables the marketers to put the purchasing behavior information into an ontology file. This ontology file can now be shared by federated agents so that they can communicate with each other automatically. Second, WSC, which has the case-based reasoning capability, provides the federating agents (CWSs) with a set of advertisement and anticipated user ratings. Hence, the federating CWSs can figure out the best advertisement among a set of advertisements which might be relatively competitive enough to win the game.

The intelligent agents used in our prototype system have two core capabilities: intelligence and autonomy. First, the agents are intelligent because they can adjust to the user’s purchase history using the case-based reasoning. If a new case comes into the case base from the user, the case can then be used from the next reasoning activity. Second, the agents are autonomous because they communicate with each other using a dedicated message coded in an agent communication language, KQML. JATLite is a good tool to let the agents autonomously collaborate or negotiate without the user/agent interaction. The only thing the user should do is to initiate the delegation conditions and store them into the database or ontology file.

The prototype system of the current version adopts Java application. However, for better user interface, the system will be migrated to a Java applet. The current system response time is not quite optimal. Especially as the number of cases increases, the time to get the most similar case increases proportionally. The average system response time was within the range of 30 s to 2 min, based on the assumption that there are four seller agents and one buyer agent. Even though this performance could be disappointing, some application domains will allow asynchronous transactions, which may not consider the waiting time.

## 5. Experiments

## 5.1. Experimental design

The main goal of our experiment is to investigate the performance of our mechanism. To facilitate our experiment, we assume that the selling agents have been delegated to some extent by corresponding shops, and hence may vary their own price level and level of quality to negotiate with the customer.

To show the feasibility of the idea of our architecture, let’s give an example. A customer is attending a conference and now needs a dinner. He/ she has a wireless terminal and will look around at some restaurants within an area ranged from (0,0)\~(120,120). We will assume that there are total of fifteen restaurants, four of which have their own selling agents (Coordinating Web Services) that can be accessed by the customer’s wireless terminal. The shops are tagged as Simple1, Simple2, CWS1, and CWS2, and they are selling at location (50,80), (100,60), (40,20), and (90,100), respectively. The locations are shown in Fig. 7.

As the instances of agent characteristics defined in Eqs. (1) through (3), the agents are defined by the following set of characteristics (Eqs. (7) and (8)).

$$
\begin{array}{r l} D _ {j} - \text { Vector   of   offerings   provided   by   a   web   service } j & = \langle p _ {j}, q _ {j} \rangle \\ & (7) \end{array}
$$

![](/api/attachments/ZV6GXU4S/fulltext/images/f1cae775f78b0a8463837d3df51d935d7c2a0ef1a3eb7d34a3f06d0ffd86c4cb.jpg)  
Fig. 7. Illustrative Example: the map has been imported from maps.yahoo.com originated from NavTechR.

where $p _ { j }$ is price level proposed by a web service $j ,$ and $q _ { j }$ is level of service proposed by a web service j.

$$
\begin{array}{l} C _ {i} \text {- - - Vector of contextual information of Buyer i} \\ = \langle l _ {i} \rangle \end{array}\tag{8}
$$

where $l _ { i }$ is user i’s current location.

$$
U _ {i} - \text { Buyer   } i ^ {\prime} \text {   s   utility   function } = f (p _ {j}, q _ {j}, d _ {i j})\tag{9}
$$

where $d _ { j t }$ is distance between $l _ { i }$ and seller j’s location.

The utility function is unknown to the Coordinating Web Services and even the WSC. In this paper, we have chosen buyer’s payoff, sellers’ total payoff, sellers’ total sales, and rate of win as the performance measures.

To analyze the performance of our prototype system, we formulated four types of coordination: (1) simple web services (Type 1), (2) intelligent web services (Type 2), (3) coordinated web services (Type 3), and (4) intelligent and coordinated web services (Type 4). Type 1 means that there is neither coordinator nor case bases, which reflects the current web service environments. In Type 2 services, some of the web services contain their own case base with reasoning capability, as well as an optimization module. WSC in Type 3 coordinates some web services to let them arrive at global optimum. However, the WSC does nothing but simply deliver requests from the B-agent to the Coordinating Web Services and then the Coordinating Web Services suggest their own conditions to reach at local optimum state. Under Type 4, WSC contains a case base on behalf of the Coordinating Web Services to estimate customers’ utilities more precisely and adaptively and the Coordinating Web Services may vary their own condition autonomously.

Each coordination type was simulated 100 times and the time span of each simulation was 30 periods. At each period, the location of a user and an advertisement of a product that is provided by an arbitrary off-line shop are produced by random number generation with uniform distributed functions.

![](/api/attachments/ZV6GXU4S/fulltext/images/5a97cb293ac061c93445cfc5b3ce1f4b8d4bbf8a7a82a394faf5f39901eb8104.jpg)  
Fig. 8. Types of experiments (1).

The following four hypotheses are raised through multi-agents based experiments:

Hypothesis 1. The result by Type 2 will outperform that by Type 1.

Hypothesis 2. The result by Type 3 will outperform that by Type 1.

Hypothesis 3. The result by Type 4 will outperform that by Type 2.

Hypothesis 4. The result by Type 4 will outperform that by Type 3.

As shown in Figs. 8 and 9, Hypothesis 1 evaluates whether the case-based reasoning capability is worth considering to increase the performance. Hypothesis 2 evaluates whether the coordination mechanism is good for the prototype system. With Hypothesis 3, the intelligent system, which also has coordination capability, will be justified. Finally, Hypothesis 4, in contrary to Hypothesis 3, tests if the coordinating system, which has casebased reasoning, is better than that without the capability.

![](/api/attachments/ZV6GXU4S/fulltext/images/508b7c1d4a911308951f8688cd0e8c55fd320a1c9fc284d533efbb3ed05b9c8d.jpg)  
Fig. 9. Types of experiments (2).

![](/api/attachments/ZV6GXU4S/fulltext/images/a3e1c74631287d4cfcaa010fc78e444bf88facc4c031e7bbcb9766011305436a.jpg)

![](/api/attachments/ZV6GXU4S/fulltext/images/17312b86909fa36b1f278231a0ca88b2c5799f879fb0067ab2b5accf63feab06.jpg)

![](/api/attachments/ZV6GXU4S/fulltext/images/b6bba168b761fb2697df5886f1c663090cce5747c90102a70a067428d479dbde.jpg)

![](/api/attachments/ZV6GXU4S/fulltext/images/dd16ea809f4d285f4917e6c831a0328428edd8df8c843a7252baae30562542a2.jpg)  
Fig. 10. Rough shape of item in preference function.

In this paper, we have chosen preference, total profit, relative profit, and rate of win as the performance measures. Each of the performance measure is as Eq. (9):

$$
\begin{array}{r l} \text { Preference } & = \text { price   preference } \\ & + \text { quality   preference } \\ & + \text { condition   preference } \\ & - \text { distance   penalty } \end{array}\tag{9}
$$

The rough shape of each item is shown in Fig. 10.

$$
\begin{array}{r l} \text { Total   profit } & = \text { price } - \text { unit   cost } \\ & - \text { marginal   cost   of   quality } \\ & * \text { quality   change } \\ & - \text { marginal   cost   of   condition } \\ & * \text { condition   change } \end{array}\tag{10 - 1}
$$

In case of Type 3 and Type 4, we assume that the coordinating web services in one WSC federation share the total profit equally. Therefore, the total profit of each coordinating web service is as follows:

$$
\begin{array}{r l} \text { Total   profit   of   each   coordinating   web   service } \\ & = \text { total   profit / number   of   web   services   in   one } \\ & \quad \text { WSC   federation } \end{array} \tag {10-2}
$$

$$
\begin{array}{r l} \text { Relative   profit } & = \text { my   total   profit } \\ & - \text { other's   save   rage   total   profit } \end{array}\tag{11 - 1}
$$

In case of Type 3 and Type 4, the relative profit of each coordinating web service is as follows:

Relative profit of each coordinating web service

¼ my relative profit

others<sup>0</sup> average relative profit

ð11  2Þ

Rate of win ¼ % of wins maximum preference ð Þ

ð12Þ

A web service wins when its advertisement gets maximum preference from the user.

## 5.2. Results

Fig. 11 shows the comparison of preferences of the original product, advertised by WSC, and simple web services. As expected, the preferences suggested by WSC look very similar to the buyer’s original preferences, although generally a bit more than the original preferences to maximize seller’s profit, and at the same time, win the game by successfully matching the user’s preference. On the other hand, the preferences of the simple web services are nearly independent of the original preference. It is because the WSC has case-based reasoning capability, and hence anticipates the original preferences more correctly than simple web services. When it comes to rate of wins, if the original preference level is low, the simple web services have more chances to win since the WSC will focus on the anticipated original preference and do not know the competitors’ strategies. The left side of Fig. 11 (Run<sup>b</sup>15) shows this tendency. However, in terms of profit, the simple web services may not gain more profits than WSC since they put in too much investment to win the game. On the right side of Fig. 11 (Run<sup>N</sup>15), the simple web services are more efficient than the WSC because the simple web services yield lower preferences than WSC—but they fail to win.

![](/api/attachments/ZV6GXU4S/fulltext/images/b9fdf786e50482f51e596abc2380edbdbdfb8c471637f14ba1f3dd0afb070ea7.jpg)  
Fig. 11. Comparison of preferences

Table 2  
Mean and standard deviation of performances of each type

<table><tr><td></td><td>Preference</td><td>Total Profit</td><td>Relative Profit</td><td>Rate of Wins</td></tr><tr><td>Type 1</td><td>1782.227 (85.3778)</td><td>-272.958 (703.2736)</td><td>44.92495 (606.3674)</td><td>11.4266% (4.426%)</td></tr><tr><td>Type 2</td><td>1893.658 (588.9904)</td><td>163.729 (656.5564)</td><td>965.920 (980.4385)</td><td>17.9695% (5.7577%)</td></tr><tr><td>Type 3</td><td>1796.172 (115.7063)</td><td>75.474 (192.1098)</td><td>801.183 (1,204.293)</td><td>17.2181% (14.2583%)</td></tr><tr><td>Type 4</td><td>1889.856 (618.3007)</td><td>168.156 (183.4541)</td><td>978.835 (1,138.330)</td><td>33.0537% (22.1357%)</td></tr></table>

Number in ( ) denotes standard deviation.

As a result, according to Fig. 11, WSC seems to obtain more profits than simple web services with similar rate of wins.

We now investigate the experimental results, which compare the four alternatives shown in Figs. 8 and 9. We adopted preferences, total profit, relative profit, and rate of wins as a performance measure of the multi-agents based on the above coordination. To illustrate the performance difference of each type more clearly, we summarize and compare the performance in Table 2.

Fig. 12 depicts the preferences of four types. In the figure, m and s denote mean value and standard deviation, respectively. Preferences of Types 2 and 4 are somewhat higher than those of Types 1 and 3. This result may be caused by case-based reasoning capability. Case-based reasoning enables the web services to catch up with the users’ expected preference level very well. Since they adapt themselves to the user’s original preferences, which are changed in each run, the standard deviations of the preference of Types 2 and 4 are greater than other types.

![](/api/attachments/ZV6GXU4S/fulltext/images/5fa4a26085aaa3a38add438b6b47c560a097f44bc285fd5811c71e52a9c8e8c9.jpg)  
Fig. 12. Comparison of preferences of each type.

Fig. 13 shows the total profits of four types. Preferences of Types 2, 3 and 4 are definitely much higher than that of Type 1. Among the three types, preferences of Types 2 and 4 are higher than that of Type 3. It is mainly because the case-based reasoning capability lets the web services have more chances to win the game. Meanwhile, the standard deviations of Types 3 and 4 are much smaller than those of Types 1 and 2. This may be caused by the coordination mechanism. The coordination mechanism can choose the best advertisement to arrive at a global optimum, which will reduce to lose the game. Even in a case of losing, because the coordinating web services share the costs, the risks tend to be reduced, too.

Fig. 14 compares the relative profits of each type. Similar to the comparison results of total profits, the preferences of Types 2, 3 and 4 are higher than that of

![](/api/attachments/ZV6GXU4S/fulltext/images/4c66f90edca44a7910ceb7ac6ac3bb8d015681d8705c7c68fef25a2e88f1210c.jpg)  
Fig. 13. Comparison of total profit of each type.

![](/api/attachments/ZV6GXU4S/fulltext/images/17380f6ec4de1287f4263f0a72f8542d64e0b66e3097447b96bfa97ad1e26c9d.jpg)  
Fig. 14. Comparison of relative profit of each type.

Type 1, and among the former three types, preferences of Types 2 and 4 are a bit higher than that of Type 3.

Finally, Fig. 15 shows the rate of wins of each type. Preferences of Type 4 are definitely second to none.

To test the four hypotheses, we carried out F-tests between two types in each pair. The results are shown in Table 3.

If p-value is greater than 0.05 or 0.01, then the null hypothesis cannot be rejected statistically. Based on such a principle, we can conclude that the statistical test results for Hypotheses 1 and 2 indicate that the null hypothesis is strongly rejected statistically: less than 1% significance levels. We deduced that using case-based reasoning capability and coordination mechanism apparently outperform simple web services that do not adopt the capabilities.

In case of Hypothesis 3, in which the coordinated and intelligent web services by WSC is compared to intelligent web services, the null hypothesis is rejected for total profit, relative profit, and rate of wins. Unexpectedly, however, the preference does not support the hypothesis. This would be caused by the fact that the intelligent web services are not supported by contextual information. The fact results in suggesting, sometimes unnecessarily, more aggressive advertisement to win the game: more chances to win but less profit. Hence, the preference of Type 2 can be higher than Type 4, but this causes lower profit. Moreover, the exceeding preference of intelligent web service does not affect rate of wins. As a result, we can conclude that Hypothesis 3 is supported.

To test Hypothesis 4, comparing the coordinated and intelligent web services by WSC (Type 4) and coordinated web services (Type 3), all measures show that Type 4 outperforms Type 3. Therefore, Hypothesis 4 is supported.

Therefore, we conclude that the method of negotiation with compound parameters yields a better performance than negotiation with single parameter, or no negotiation.

## 6. Concluding remarks

In this paper, we have described a new multi-agent web service framework with CBR and coordination capabilities under the assumption of general market: multiple users and multiple web services. According to the experimental results, as expected, the coordination mechanism and case-based intelligent advertisement yield a better performance than the mechanisms of those that have neither. These show that web services can be more effective when they adopt the coordination feature and the intelligence to autonomously adjust offerings to the buyer’s preference, by searching for past cases that may represent similar negotiations and anticipating the best condition within the delegation boundary.

The main contribution of this paper is the attempt to change the passive role of Web Services into a more active one. The multi-agent system with a contextaware coordinated mechanism and a case based intelligent mechanism has been proposed to improve the performance. The ideas of case based reasoning system and the coordination system are not new. However, the creativity of this paper is to combine them together into the application of Web Services and show the improvement experimentally. To do so, we have fully implemented the multi-agent based comparative shopping system in a mobile commerce setting. Moreover, experiments are performed to prove that the underlying information technologies used in the prototype system, such as coordinating multi-agent and case-based reasoning, are useful by statistical test. Second, agent-based semantic web services which use ontology for automatic coordination and negotiation are successfully tested. In particular, using the agent-based web service concept implies that we have more possibilities to overcome one of the main limitations of the current agent community: lack of scalability. Last, context information is considered during the coordination and negotiation. We have found that contextual information such as location affects results. This implies that an ever-changing environment plays an important role in implementing mobile web services. Context-awareness does matter and should be considered. In the near future, context-awareness may contribute to agile or ubiquitous electronic commerce since the sensing technologies have adequately developed to unobtrusively collect the user’s context.

![](/api/attachments/ZV6GXU4S/fulltext/images/7a2f7adae46fd884a411ffc047cab465e9d5ed1e7214c801089f74e2fb973ca2.jpg)  
Fig. 15. Comparison of rate of win of each type.

Table 3  
Results of statistical test

<table><tr><td>Hypotheses</td><td>Performance Measures</td><td>Difference</td><td>F-value</td><td>p-value</td></tr><tr><td rowspan="4">Hypothesis 1</td><td>Preference</td><td>111.4307</td><td>0.021012</td><td>0.0000***</td></tr><tr><td>Total profit</td><td>436.6872</td><td>1.147373</td><td>0.0001***</td></tr><tr><td>Relative profit</td><td>920.9952</td><td>0.3825</td><td>0.0000***</td></tr><tr><td>Rate of wins</td><td>6.5429%</td><td>0.76872</td><td>0.0001***</td></tr><tr><td rowspan="4">Hypothesis 2</td><td>Preference</td><td>13.94416</td><td>0.54473</td><td>0.0000***</td></tr><tr><td>Total profit</td><td>348.4311</td><td>13.40139</td><td>0.0000***</td></tr><tr><td>Relative profit</td><td>756.2584</td><td>0.253517</td><td>0.0000***</td></tr><tr><td>Rate of wins</td><td>5.7915%</td><td>0.310419</td><td>0.0000***</td></tr><tr><td rowspan="4">Hypothesis 3</td><td>Preference</td><td>-3.80253</td><td>0.907438</td><td>0.0041***</td></tr><tr><td>Total profit</td><td>4.42643</td><td>12.80444</td><td>0.0000***</td></tr><tr><td>Relative profit</td><td>12.91476</td><td>0.741829</td><td>0.0001***</td></tr><tr><td>Rate of wins</td><td>15.0841%</td><td>0.260109</td><td>0.0000***</td></tr><tr><td rowspan="4">Hypothesis 4</td><td>Preference</td><td>98.68401</td><td>0.05502</td><td>0.0000***</td></tr><tr><td>Total profit</td><td>92.68254</td><td>1.096264</td><td>0.0063***</td></tr><tr><td>Relative profit</td><td>177.6516</td><td>1.119251</td><td>0.0011***</td></tr><tr><td>Rate of wins</td><td>15.8356%</td><td>0.644132</td><td>0.0000***</td></tr></table>

\*\*\*p<sup>b</sup>0.01, \*\*p<sup>b</sup>0.05, \*p<sup>b</sup>0.1.

We are now fully implementing our agent system from the simulation level into more realistic settings. Some restrictions are left in the proposed system so that it might be accepted in a more realistic setting. For example, the decision-making criteria must be refined. The system response time was not quite satisfactory so far. As far as we know, since our approach is new under mobile comparative shopping setting, we could not find a prototype system to benchmark. Moreover, we have used a computer simulation method for experiments because we have focused how case-based reasoning, web services, and agent concepts can be applied in a mobile commerce setting. For the actual user experiment, we had to consider many more factors such as cultural issues, personal characteristics, and technology acceptance; which, while beyond the scope of the main purpose of this paper, are keys for future research and development. However, the proposed mechanism will be expected to open new application areas in context-aware mobile commerce.

## References

[1] W. Aalst, Don’t go with the flow: web services composition standards exposed, IEEE Intelligent Systems 18 (1) (2003) 72– 79.

[2] A. Ankolekar, M. Burstein, J. Hobbs, O. Lassila, D. McDermott, D. Martin, S. McIlraith, S. Narayanan, M. Paolucci, T. Payne, K. Sycara, DAML-S: web service description for the semantic web, Proceedings of the 1st International Semantic Web Conference (ISWC), Heidelberg, Germany, 2002, pp. 348 – 363.

[3] A. Asthana, M. Cravatts, P. Krzyzanouski, An indoor wireless system for personalized shopping assistance, in: L.F. Cabrera, M. Sattyanarayanan (Eds.), Workshop on Mobile Computing Systems and Applications, 1994, pp. 69 – 74.

[4] R. Aumann, Acceptable points in general cooperative n-person games, Col. IV of Contributions to the Theory of Games, Princeton University Press, 1959.

[5] A. Avila-Rosas, L. Moreau, V. Dialani, S. Miles, X. Liu, Agents for the Grid: a comparison with web services (Prt II: Service discovery), Proceedings of the 1st International Workshop on Challenges in Open Agent Systems, AAMAS’02, Bolona, 2002.

[6] A. Bonarini, V. Trianni, Learning fuzzy classifier systems for multi-agent coordination, Information Sciences 136 (1–4) (2001) 215–239.

[7] P.A. Buhler, J.M. Vidal, Towards the synthesis of web services and agent behaviors, Proceedings of the 1st International Workshop on Challenges in Open Agent Systems, AAMAS’02, Bolona, 2002.

[8] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (3) (1999) 225–237.

[9] B. Burg, Agents in the world of active web-services, Second Kyoto Meeting on Digital Cities, 2001.

[10] H.R. Choi, H.S. Kim, B.J. Park, Y.J. Park, A.B. Whinston, An agent for selecting optimal order set in EC marketplace, Decision Support Systems 36 (4) (2004) 371–383.

[11] M. Clark, The birth of the UDDI value added service supplier, Web Service Architect, Dec. 2001.

[12] D. Christopherson, Artificial intelligence in the weather forecast office—one forecaster’s view, Proceedings of the First Conference on Artificial Intelligence, 1998, pp. 136 – 143.

[13] A.K. Dey, G.D. Abowd, Towards a better understanding of context and context-awareness, GVU technical report, GIT-GVU-99-22, College Comp., GATECH., 1999.

[14] T. Erickson, Some problems with the notion of context-aware computing, Communications of the ACM 45 (2) (2002) 102 – 104.

[15] M. Fagan, K. Bloor, Case-based reasoning for candidate list extraction in a marketing domain, Lecture Notes in Computer Science (1997) 426 – 437.

[16] A. Greenwald, N.R. Jennings, P. Stone, Agents and markets, IEEE Intelligent Systems 18 (6) (2003) 12 – 14.

[17] J. Hu, M.P. Weliman, Learning about other agents in a dynamic multiagent system, Cognitive Systems Research 2 (1) (2001) 67 – 79.

[18] J. Kolodner, Case-Based Reasoning, Morgan Kaufmann, San Francisco, 1993.

[19] S. Kraus, J. Wilkenfeld, G. Zlotkin, Multiagent negotiation under time constraints, Artificial Intelligence Journal 75 (2) (1995) 297– 345.

[20] H. Kuno, A. Sahai, My agent wants to talk to your service: personalizing web services through agents, Proceedings of the 1st International Workshop on Challenges in Open Agent Systems, Bolona, 2002.

[21] O.B. Kwon, Meta web service: building web-based open decision support system based on web services, Expert Systems with Applications 24 (4) (2003) 375–389.

[22] S. Long, D. Aust, G.D. Abowd, C.G. Atkeson, Rapid prototyping of mobile context-aware applications: the Cyberguide case study, Proceedings of the 1995 conference

on Human Factors in Computing Systems-CHI’96, 1996, pp. 293 – 294.

[23] C. Lottaz, I.F.C. Smith, Y. Robert-Nicoud, B.V. Faltings, Constraint-based support for negotiation in collaborative design, Artificial Intelligence in Engineering 14 (3) (2000) 261 – 280.

[24] X. Luo, C. Zhang, H.F. Leung, Information sharing between heterogeneous uncertain reasoning models in a multi-agent environment: a case study, International Journal of Approximate Reasoning 27 (1) (2001) 27 – 59.

[25] J. Main, S. Dillon, S.C.K. Shiu, A tutorial on case-based reasoning, in: S.K. Pal, T.S. Dillon, D.S. Yeung (Eds.), Soft Computing in Case Based Reasoning, Springer, London, UK, 2000.

[26] D. Mandato, E. Kovacs, F. Hohl, H. Amir-Alikhani, CAMP: a context-aware mobile portal, IEEE Communications Magazine 40 (1) (2002) 90– 97.

[27] S. Mann, Humanistic intelligence: <sup>d</sup>WearComp<sup>T</sup> as a new framework and application for intelligent signal processing, Proceedings of the IEEE (1998) 2123– 2151.

[28] F.P. Maturana, D.H. Norrie, Distributed decision-making using the contract net within a mediator architecture, Decision Support Systems 20 (1) (1997) 53–64.

[29] P.R. McMullen, An ant colony optimization approach to addressing a JIT sequencing problem with multiple objectives, Artificial Intelligence in Engineering 15 (3) (2001) 309– 317.

[30] H. Nishiyama, W. Yamazaki, F. Mizoguchi, Negotiation protocol for proof of realization of cooperative task in multiagent robot systems, Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics 3, IEE, 2000, pp. 1685– 1690.

[31] M.P. Papazoglou, Web services and business transactions, World Wide Web, Internet and Web Information Systems 6 (1) (2003) 49 – 91.

[32] J.H. Park, S.C. Park, Agent-based merchandise management in business-to-business electronic commerce, Decision Support Systems 35 (3) (2003) 311 – 333.

[33] S. Parsons, C. Sierra, N. Jennings, Agents that reason and negotiate by arguing, Journal of Logic and Computation 8 (3) (1998) 261–292.

[34] T.R. Payne, R. Singh, K. Sycara, Calendar agents on the semantic web, IEEE Intelligent Systems 17 (3) (2002) 84– 86.

[35] I. Praca, C. Ramos, Z. Vale, M. Cordeiro, Mascem: a multiagent system that simulates competitive electricity markets, IEEE Intelligent Systems 18 (6) (2003) 54 – 60.

[36] F. Ramos, M.A. Junco, E. Espinosa, Soccer strategies that live in the B2B world of negotiation and decision-making, Decision Support Systems 35 (3) (2003) 287– 310.

[37] S. Samaras, S. Evripidou, E. Pitoura, A mobile-agent based infrastructure for eWork and eBusiness applications, Proceedings of eWork and eBusiness Conference, Madrid, Spain, 2000, pp. 1092 – 1098.

[38] T.W. Sandholm, Distributed rational decision making, Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence, The MIT Press, Cambridge, 1999.

[39] B.N. Schilit, N. Adams, R. Want, Context-aware computing applications, Proceedings Workshop on Mobile Computing Systems and Applications, IEEE Computer Society, Santa Cruz, CA, 1994, pp. 85– 90.

[40] J.A.A. Sillince, M.H. Saeedi, Computer-mediated communication: problems and potentials of argumentation support systems, Decision Support Systems 26 (4) (1999) 287 – 306.

[41] M.P. Singh, Multiagent systems, Lectures in Artificial Intelligence 799 (1994) 81 – 113.

[42] T.J. Strader, F.R. Lin, M.J. Shaw, Information infrastructure for electronic virtual organization management, Decision Support Systems 23 (1) (1998) 75 – 94.

[43] G. Tewari, J. Youll, P. Maes, Personalized location-based brokering using an agent-based intermediary architecture, Decision Support Systems 34 (2) (2003) 127 – 137.

[44] C. Tsatsoulis, Q. Cheng, H.Y. Wei, Integrating case-based reasoning and decision theory, IEEE Expert 12 (4) (1997) 46 – 55.

[45] M. Ulieru, D. Norrie, R. Kremer, W. Shen, A multi-resolution collaborative architecture for web-centric global manufacturing, Information Sciences 127 (1–2) (2000) 3– 21.

[46] R. Want, A. Hopper, V. Falcao, J. Gibbons, The active badge location system, ACM Transactions on Information Systems 10 (1) (1992) 91 – 102.

[47] G. Weiss, Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence, The MIT Press, Cambridge, 1999.

[48] M. Wooldridge, N.R. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995) 115– 152.

[49] D.J. Wu, Software agents for knowledge management: coordination in multi-agent supply chains and auctions, Expert Systems with Applications 20 (1) (2001) 51– 64.

[50] J. Yang, Web service componentization, Communications of the ACM 46 (10) (2003) 35– 40.

[51] S.T. Yuan, A personalized and integrative comparison-shopping engine and its applications, Decision Support Systems 34 (2) (2003) 139–156.

![](/api/attachments/ZV6GXU4S/fulltext/images/08eb1bf6b02bb24b12a441d3f7a2398801ccf503f2f6c4ac844f20829ce63d1b.jpg)

Ohbyung Kwon is presently an associate professor at Kyunghee University, South Korea, where he initially joined in 2004. In 2002, he joined Institute of Software Research International (ISRI) at Carnegie Mellon University to perform DARPA project on semantic web and context-aware computing. He received the MS and PhD degree in Management Information System at KAIST (Korea Advanced Institute of Science and Technology) in 1990 and 1995,

respectively. His current research interests include ubiquitous computing services, agent technology, mobile commerce, contextaware system development, case-based reasoning, and DSS. He has published various papers in leading information system journals such as Decision Support Systems, Expert Systems With Applications, Simulation, and Behavior and Information Technology.
