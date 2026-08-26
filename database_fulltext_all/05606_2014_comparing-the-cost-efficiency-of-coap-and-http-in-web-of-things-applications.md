---
otero_id: 5606
otero_key: "CKP4QC2P"
title: "Comparing the cost-efficiency of CoAP and HTTP in Web of Things applications"
authors: "Tapio Levä; Oleksiy Mazhelis; Henna Suomi"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications

Tapio Levä <sup>a,</sup>⁎, Oleksiy Mazhelis <sup>b</sup>, Henna Suomi <sup>a</sup>

<sup>a</sup> Aalto University, Department of Communications and Networking, P.O. Box 13000, 00076 Aalto, Finland

<sup>b</sup> University of Jyväskylä, Department of Computer Science and Information Systems, P.O. Box 35, FIN-40014, Finland

## a r t i c l e i n f o

Available online xxxx

Keywords: CoAP HTTP Web of Things Total cost of ownership Adoption

## a b s t r a c t

Constrained Application Protocol (CoAP) has been introduced as a simpler alternative to the Hypertext Transfer Protocol (HTTP) for connecting constrained smart objects to the Web. The adoption of the protocol depends on its relative advantage, and the cost–bene<sup>fi</sup>t associated with the use of the protocol is a signi<sup>fi</sup>cant factor affecting a protocol adoption decision. This paper aims at deepening the understanding of the cost–bene<sup>fi</sup>ts of CoAP and identi<sup>fi</sup>es the application scenarios where its use is likely to be economically justi<sup>fi</sup>able. The paper analyzes the costs of using CoAP and HTTP in the Web of Things (WoT) applications, by identifying the components of the total cost of ownership (TCO) model for these applications and by studying the factors affecting individual costs. The use of the model is then demonstrated by means of comparing the TCO of CoAP and HTTP in an environment monitoring application scenario. The results of the analysis suggest that the simpler hardware requirements of CoAP smart objects, as well as the lower communication overhead of the protocol and the resulting reduced power consumption lead to cost advantages in the application scenarios where the smart objects i) are large in volume and/or are deployed in the <sup>fi</sup>eld, ii) engage in frequent communications with the Web that are charged for on the basis of the volume of the data being transferred and jii) are sleeping between the communication sessions. The obtained results may be utilized both by the decision-makers considering the adoption of CoAP in speci<sup>fi</sup>c solutions, as well as by the academics and practitioners involved in the protocol development. © 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Proliferation of Internet technologies has resulted in an immense growth of the Web, which in 2012 exceeded 900 million Internet hosts<sup>1</sup> and 200 million active web sites.<sup>2</sup> To date, the growth of the Web has been predominantly attributed to the increase in the number of conventional static and dynamic web sites. However, the Web of Things (WoT) vision predicts the future evolution of the Web towards the state where the everyday objects equipped with computing and communication capabilities – the smart objects – are interconnected with the Web by applying standard web protocols [17,18]. Interconnecting such smart objects with the Web promises a number of bene<sup>fi</sup>ts to the users, varying from faster and more accurate sensing of our environment to more cost-ef<sup>fi</sup>cient tracking of industrial processes [16,37].

One of the main paradigms in the WoT applications is the utilization of the well-established architectural principles and protocols of the Web in order to seamlessly interconnect smart objects [17]. These include the Representational State Transfer (REST), de<sup>fi</sup>ned by Fielding and Taylor [15], as the primary architectural interaction pattern, and using Hypertext Transfer Protocol (HTTP) as the application layer protocol [37]. In RESTful WoT applications, a smart object (which is often running an embedded web server) usually interacts with the counterparts in the Web by exchanging requests and responses over HTTP. While being a standard and well-known application layer protocol, it may be too heavy and inef<sup>fi</sup>cient for implementation on constrained, battery-powered devices [26].

In order to cope with the limitations of the HTTP in the WoT applications on constrained devices, the Internet Engineering Task Force (IETF) has introduced the Constrained Application Protocol (CoAP) — a web transfer protocol optimized for the constrained power and processing capabilities of WoT smart objects [27]. Compared to HTTP, CoAP offers numerous potentially bene<sup>fi</sup>cial features when implementing WoT applications, among which are a compact binary header, UDP-based transport with simple reliability provisions, built-in resource discovery, and a push mechanism with subscriptions to information [7,26]. At the time of writing, CoAP standardization is still being <sup>fi</sup>nalized, and the use of the protocol in industrial products and solutions is still due. Therefore, the competition is still upcoming between the CoAP-based and other solutions for the position of the new dominant design in future WoT applications. The economic forces towards cost minimization, along with social and political forces, will determine whether CoAP will become a part of the new dominant design for WoT applications [31].

The company's choice of a technology, including protocols, is justi<sup>fi</sup>ed by the need to support its value disciplines of operational excellence, product leadership, or customer intimacy [30]. From the perspective of the WoT applications, the role of CoAP and other protocols is to enable communication between smart objects and their counterparts in the Web. Given the similar functionality offered by the protocols, the use of a particular protocol is unlikely to bring an advantage in terms of product leaderships or customer intimacy. Rather, the protocol choice will contribute to the operational excellence of the company, and therefore, the attainable cost savings due to the use of a protocol are crucial for the protocol adoption decisions. This justi<sup>fi</sup>es the analysis of the costs of the WoT applications based on different protocols, in order to identify i) the source of the cost-differences and ii) the magnitude of the cost savings affected by the choice of the protocol as the key factors affecting its adoption [19]. Minimizing the total cost of a connected smart object is also one of the main objectives of CoAP [3] and thus deemed crucial for its successful adoption. However, to the best knowledge of the authors, no publicly available works have focused on systematically studying the cost savings attainable through the use of CoAP.

The objective of this paper is to deepen the understanding of the cost advantages of CoAP, and to investigate scenarios where its application is likely to be economically justi<sup>fi</sup>able. The paper focuses on the Internet-connected, battery-powered smart objects with constrained communications and processing capabilities, and limited random access memory (RAM). Further, the analysis in the paper assumes that openly standardized protocols are the most promising candidates for the future dominant design position [32]. Therefore, the paper evaluates the cost advantages of using CoAP as compared with HTTP, which is the state-of-the-art standard for conventional RESTful web services. On the other hand, the proprietary, domain-speci<sup>fi</sup>c, and other non-IETF protocol stacks available for constrained devices, such as Z-Wave, KNX, and ZigBee, are excluded from the analysis. Also, any other factors than costs that may potentially affect the adoption decisions – such as the security implications, the architectural choices made, and the organizational policies – are excluded from the analysis for the sake of simplicity.

The research questions addressed in the paper can be formulated as follows:

• How to compare two or more protocols, such as CoAP and HTTP, in terms of their costs?

• What are the factors determining the cost-efficiency of CoAP vs. HTTP?

• In which WoT application scenarios is the use of CoAP cost-advantageous as compared with HTTP?

The cost analysis in this paper follows an analytical approach. First, a generic total cost of ownership (TCO) model for WoT applications is created by identifying the individual cost components of TCO. Then, the created TCO model is used for comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP protocols in the context of an exemplary environment monitoring application scenario. The values for the individual cost components and the parameters affecting them are estimated using multiple sources of information, including academic and trade sources, own measurements, as well as expert interviews. To mitigate possible inaccuracies of individual estimates, a sensitivity analysis has been performed and its results are reported in the paper.

The results of the TCO analysis suggest that:

• CoAP is generally more cost-ef<sup>fi</sup>cient than HTTP for applications with a high number of smart objects, each engaged in frequent communications sessions, whereas for infrequent interactions, the cost difference between the protocols is insigni<sup>fi</sup>cant.

• CoAP is also more cost-ef<sup>fi</sup>cient in case the smart objects are deployed in the <sup>fi</sup>eld, thereby incurring signi<sup>fi</sup>cant costs of battery replacements.

• The use of CoAP allows the cost of the applications to be decreased dramatically in case the charging for the data communications is volume-based, since the small overhead of the protocol and its reliance on the UDP enable a manifold reduction in the transferred data volume.

• Finally, the use of CoAP is found to be economically more bene<sup>fi</sup>cial in case the smart objects are awake only for occasionally initiating the communication sessions (push mode of communication) as opposite to the case when the smart object is periodically awake in a listening mode awaiting for incoming communication requests (pull mode).

The paper contributes both to the scienti<sup>fi</sup>c community and to the community of practitioners. First, the paper contributes by applying the TCO analysis, typically used for supplier selection, into a new context of technology selection between alternative technologies. Second, the article makes a methodological contribution by introducing a generic TCO model that can be used to analyze the TCO of various WoT application scenarios and technological options not limited to IETF standards. Arguably, the model is suf<sup>fi</sup>ciently generic to be used also outside of WoT applications, as the architectural elements considered in the model can be identi<sup>fi</sup>ed in a variety of IT systems. Moreover, whereas the cost components of IT systems have been identi<sup>fi</sup>ed in earlier works, this paper elaborates on how to estimate these costs. Finally, the paper makes a practical contribution by deepening the understanding of the factors that make CoAP a more cost-ef<sup>fi</sup>cient alternative to HTTP in WoT applications. These results are expected to be advantageous to the CoAP standardization and deployment, by providing an early feedback about its strong and weak sides, as seen from the cost perspective.

The remainder of the paper is organized as follows: Section 2 describes the constraints of contemporary smart objects, introduces the CoAP for connecting these objects to the Web, and discusses the potential bene<sup>fi</sup>ts of using CoAP as opposite to HTTP in constrained environments. Section 3 introduces the TCO as an analytical tool employed in the paper for systematically comparing the costs of the solutions based on CoAP and HTTP. Section 4 identi<sup>fi</sup>es the individual cost components and creates a generic TCO model for WoT applications based on a generic technical architecture. In Section 5, the individual costs are further elaborated, estimated, and compared for different application scenarios. The results of the cost comparison are discussed in Section 6. Finally, Section 7 summarizes the paper and provides the directions for future work.

## 2. Constrained devices: current evolution phase

The Web of Things is envisioned to bring web services costef<sup>fi</sup>ciently into smart objects, for which the bene<sup>fi</sup>t of Internet connectivity has earlier been too low, as compared with the investments needed. Using standard protocols and interfaces, the WoT technologies are expected to reduce the costs, thereby making some of the business cases pro<sup>fi</sup>table. Due to the emphasis on reducing costs, as well as on minimizing the physical size and enabling an autonomous operation, these smart objects are often constrained in their computing and communications capabilities. Often these objects employ batteries as their power source, and are expected to run unattended for many months or years. The limited power supply places restrictions on the energy consumption, and hence on the computing and data communication tasks the smart object is capable of executing. Even when the smart objects (e.g., white goods) are powered by the electricity grid, the costef<sup>fi</sup>ciency requirements lead to the use of microcontrollers with very small code and memory sizes.

## 2.1. Current state of WoT — proprietary solutions in separate verticals

At present, the WoT technologies are applied in many vertical appli cation domains, varying from automotive and machinery to home automation and consumer electronics. Traditionally, these technologies are implemented as a part of industrial in-house solutions based on machine-to-machine communications and embedded systems. More recently, some products also within the consumer electronics domain have started to appear in the market, with wellbeing devices (e.g.,

Please cite this article as: T. Levä, et al., Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.009

Withings<sup>3</sup>) and smart home solutions (e.g., GreenWave Reality<sup>4</sup>) being among the most prominent examples. In many application domains, proprietary standards have been designed to better meet the domainspeci<sup>fi</sup>c requirements and the limitations of constrained devices. Examples of these include BACnet, LonWorks, and KNX for industrial and building automation and Z-Wave and Insteon for home automation.

The current solutions are thus dominated by a variety of proprietary and standard platforms, protocols, and interfaces, making the components of solutions provided by different vendors barely compatible, while keeping the prices of the components high. For instance, Z-Wave – a short range wireless technology for home automation – represents a vertically integrated protocol stack that only works on top of Z-Wave proprietary radio. Moreover, it does not specify the interoperability with the Internet protocols, and thus a dedicated gateway is needed to convert the Z-Wave application protocols into a convenient presentation format [24]. In a similar manner, the KNX protocols for building automation specify the layers from the link layer up to the application layer, with a dedicated gateway device needed to perform the conversion to TCP/IP. The ZigBee protocol stack, running on top of IEEE 802.15.4 radio, takes a notably different approach. The network (originally non-IP) and application layer protocols are complemented by the so-called public application pro<sup>fi</sup>les that enable cross-vendor interoperability within speci<sup>fi</sup>c application domains, such as home automation, smart energy, and healthcare. The universality and <sup>fl</sup>exibility of ZigBee come at the cost of greater complexity, thus making it less attractive for constrained smart objects (in addition to some other problems, such as crowded frequency band and compatibility issues<sup>5</sup>).

## 2.2. Towards standardization — constrained application protocol (CoAP)

One of the main paradigms of the WoT vision is the utilization of the well-established architectural principles and protocols of the Web in order to seamlessly interconnect smart objects [18,37]. These include the Representational State Transfer (REST), de<sup>fi</sup>ned by Fielding and Taylor [15], as the primary architectural interaction pattern, and using HTTP as the application layer protocol. In addition to HTTP, which represents the de facto standard for information transfer in the Web, other protocols have been designed to deal with speci<sup>fi</sup>c type of information and/ or speci<sup>fi</sup>c types of applications, such as the Extensible Messaging and Presence Protocol (XMPP) for instant messaging and presence information exchange, or the Session Initiation Protocol (SIP) and the Real-time Transport Protocol (RTP) for audio and video streaming.

Although HTTP is the de facto standard protocol well-suited to RESTful applications, it is considered as suboptimal for the applications targeting smart objects, especially whenever these objects are batterypowered. A lengthy header and the implied need to establish TCP connections, as well as the reliance on the request/response pull as the only interaction model, result in a low power ef<sup>fi</sup>ciency of HTTP implementations, while also increasing requirements for the available memory and processing capabilities of the smart objects' hardware and thus in<sup>fl</sup>ating the related hardware costs. In other words, the HTTP seems to represent a relatively poor match for the WoT applications when implemented on constrained devices [26].

In order to address the limitations of the HTTP in the WoT applications on constrained devices, the IETF established the Constrained RESTful environments (CoRE) Working Group. Its primary goal is to coordinate the design and speci<sup>fi</sup>cation of the Constrained Application Protocol (CoAP) that represents an alternative web transfer protocol optimized for the constrained power and processing capabilities of the WoT smart objects [27]. CoAP speci<sup>fi</sup>es a minimal subset of REST requests including GET, POST, PUT, and DELETE, supports resource caching and built-in resource discovery, and relies on UDP as a transport protocol while providing reliability with a simple built-in retransmission mechanism.

As compared with HTTP, CoAP's characteristics are expected to bring the following bene<sup>fi</sup>ts when implementing WoT applications [7,26,33]:

• A more compact binary header of 10–20 bytes in total, along with the UDP-based transport, reduces the volume of overhead data that needs to be transmitted along with the payload, thus reducing the delay and minimizing the battery drainage due to data transmission;

• The support for the asynchronous information push (the observe option) enables the smart objects to send information about the resource only when it changes, thus allowing the objects to be asleep most of the time and further reducing their power consumption;

• The use of a minimal subset of the REST requests allows the protocol implementations to be less complex as compared with HTTP, thus lowering the hardware requirements for the smart objects on which it executes.

Due to the compact header and use of UDP-based transport, the communications overhead of CoAP is notably smaller as compared with HTTP. As a result, depending on the payload size and the client– server set-up, the CoAP/UDP transaction may require 8–10 times less bytes to be transferred, as compared with the same transaction using HTTP/TCP [8,11]. Due to its similarity with HTTP, the HTTP-CoAP mapping is relatively easy to realize [6].

Although a promising alternative to the proprietary or prohibitively complex WoT protocols, CoAP is just leaving the research labs and making its way into the industrial products and solutions while the protocol standardization is still being <sup>fi</sup>nalized. The proponents of CoAP, such as Ericsson, INRIA, Lulea, NXP, Sensinode, SICS, STMicroelectronics, Watteco, and Wisenet, are testing their CoAP implementations and their interoperability.<sup>6</sup> However, only few reported examples of using the protocol in commercial products, such as Sensinode's NanoService, can be found. Therefore, the competition is still upcoming between the HTTP, CoAP and proprietary solutions for the position of the new dominant design in future WoT applications. If CoAP provides only minor bene<sup>fi</sup>ts as compared with HTTP, requires signi<sup>fi</sup>cant investments that are unlikely to pay off, or is complex to implement, its adoption and subsequent emergence as a new dominant design is likely to be hindered, similarly to the failure of the WAP protocol in the past [28].

## 3. Cost analysis based on the total cost of ownership

The total cost of ownership (TCO) analysis represents a systematic analytical tool for understanding the total costs associated with acquiring and using goods or services. As opposite to a simplistic cost analysis based on the acquisition price only, the TCO analysis covers the key cost constituents of pre-acquisition, acquisition and possession, use, and disposal [12,13]. Multiple approaches exist for developing an understanding of the costs. The approach followed in this study is known as the monetary-based approach, where the costs are allocated to different components based on true costs. Alternatively, the cost-ratio or valuebased methods can be applied, in case the monetary costs need to be combined with qualitative performance information, which is more dif-<sup>fi</sup>cult to express in monetary terms [5,13].

A number of potential cost constituents are identi<sup>fi</sup>ed in literature [9,14]. According to David et al. [9], the IT-related cost factors can be categorized into the acquisition, operations, and control costs — with the latter being optional costs aimed at improving the IT centralization and standardization, which in turn result in reduced operational costs. The relevance of a particular cost factor depends on the particular application. For instance, transportation costs may be ignored as minor or absent in the case of IT services: however, in the case of WoT solutions

T. Levä et al. / Decision Support Systems xxx (2013) xxx–xxx

involving thousands of devices to be serviced in the <sup>fi</sup>eld, these costs may be crucial for the analysis.

A signi<sup>fi</sup>cant challenge to the implementation of TCO analysis is the lack of readily available data [22]. A TCO model requires detailed information about the costs, which may be dif<sup>fi</sup>cult to <sup>fi</sup>nd or estimate. In this paper, the individual cost components, and the parameters affecting them are estimated using multiple sources of information, including:

(i) Academic and trade literature, e.g., for retrieving the pricing schemes and reference prices applicable today, as well as technical characteristics of the solution components;

(ii) Own measurements, for estimating the power consumption of the smart objects; and

(iii) Semi-structured interviews with domain experts focusing especially on the cost factors that differentiate the solutions based on the CoAP and HTTP protocols.

Further, in order to mitigate the effect of possible inaccuracies of individual estimates and generalize beyond the speci<sup>fi</sup>c hardware platform used for assessing the energy footprint of the protocols, a sensitivity analysis was performed, whereby the effect of the variation in individual cost components and other parameters on the TCO is studied.

The TCO analysis is further complicated by the fact that the costs are often situation-speci<sup>fi</sup>c [13] and may change over time. Consequently, a well-de<sup>fi</sup>ned TCO model is often more valuable than a very detailed analysis of a single case, because the model can be re-used for other applications with different cost values and characteristics. Therefore, this paper focuses more on analyzing the properties and borderline conditions of the cost model than giving de<sup>fi</sup>nite answers about the technology choice in speci<sup>fi</sup>c application scenarios.

It should be noted that, in some works, the time-value of money is taken into account in the analysis, by using the net present value (NPV) instead of non-discounted values. This is relevant when the costs realize at different times during the product lifecycle for different options. Buy or lease decision exempli<sup>fi</sup>ed by Walker et al. [34,35] for the cloud computing related decision-making is one of these cases. In this study, the time-value of money analysis is expected to provide little additional value, because the compared technical alternatives induce costs at roughly the same time. Therefore, the NPV analysis has been omitted. Likewise, the other factors potentially affecting the TCO – such as the declining pricing trends, the quantity discounts, the cost of disposing and the salvage value of the components, and the control costs – have been excluded from the TCO analysis for the sake of simplicity.

Because the TCO approach has been developed for purchasing-related decision-making of well-speci<sup>fi</sup>ed products, it has mainly been used in supplier evaluation and selection at the operational and tactical level (e.g., [10,22]). To the best of our knowledge, TCO has not been widely applied to strategic decision-making concerning technology investments with multiple options. NPV-based techno-economic modeling efforts related to large-scale network investments [23,29] and Multipath TCP adoption [36] represent the closest match, with the distinction that they also take into account revenues to calculate the repayment period and pro<sup>fi</sup>tability of the investments. These studies also lack the comparison perspective, which is in the core of this paper. Therefore, this paper applies TCO approach to a new context of technology selection.

## 4. Total cost of ownership of WoT applications

WoT applications can be realized with different alternative communication technologies. The choice depends on the suitability of the technology to each application scenario, where suitability can be measured by the net bene<sup>fi</sup>t for the relevant stakeholders. This paper focuses on the applications where both HTTP and CoAP can be used to implement the application without signi<sup>fi</sup>cant difference in the end-user experience. In other words, the application layer protocol choice has cost impact only. In these cases, the cost analysis is an integral part of the decision-making process. Calculating TCO assures fair comparison between different technologies since it covers the costs accumulated through the entire lifecycle of the application. To formulate a generic TCO model for WoT applications, this section <sup>fi</sup>rst speci<sup>fi</sup>es the technical architecture and the value network under study, and then identi<sup>fi</sup>es the cost components of the TCO model and the factors affecting their magnitude for the speci<sup>fi</sup>ed architecture. Finally, the sources for potential cost differences between CoAP and HTTP are discussed.

## 4.1. Technical architecture

The paper focuses on WoT applications utilizing Internet-connected, constrained devices, i.e., battery-powered smart objects with constrained communications and processing capabilities, and limited RAM. Fig. 1 depicts the studied architecture that consists of smart objects, access points and web servers.

Smart objects (sensors or actuators) communicate through access points with web servers residing in the public Internet. The smart objects are located in the proximity of access points so that they can be connected using license-free short-range radio technologies, such as IEEE 802.15.4. The access points are not resource-constrained and they connect to the web server over long-range radio or <sup>fi</sup>xed links. In some application scenarios, the smart objects are distributed across a wide geographic area, in which case they form multiple sites with their corresponding access points. A CoAP–HTTP proxy is an optional software component in the architecture, which can be used to translate between CoAP and HTTP if the smart objects use CoAP but the server understands only HTTP. Depending on the architectural choice, the proxy is implemented either in the access points or in the web servers. The protocol stack in the bottom of Fig. 1 assumes the latter approach, but the cost impact of both options is discussed in Section 4.3.4.

The depicted architecture enables three deployment alternatives using CoAP and HTTP:

1) CoAP end-to-end (CoAP),

2) HTTP end-to-end (HTTP), and

3) CoAP between smart objects and proxy, and HTTP between proxy and web servers (CoAP-proxy).

The paper further differentiates two modes of communication:

\- In the pull mode, a smart object acts as a server awaiting the requests from a remote node, and responds to the requests with the information required, e.g., by delivering the instant sensor reading. The smart object is non-sleeping or frequently awaking, as it shall always be ready to promptly respond to an incoming request.

\- In the push mode, a smart object acts as a client and periodically sends the information to a remote web server. The smart object is mainly sleeping and awakes only when it needs to (sense and) communicate the information. In addition to periodic communication, CoAP also provides the Observe option [20] that allows the smart objects to communicate only when a speci<sup>fi</sup>ed condition is met.

The implementation details may blur the distinction between the two modes. For instance, in the pull mode, the smart object may be asleep for a portion of time if a short delay in responding is tolerated, or if a cached response by the proxy is suf<sup>fi</sup>cient until the next communication time. Still, for the analysis in this paper, it is important to distinguish the mode where the smart object is constantly “on duty” (pull) from the mode where the smart object may be of<sup>fl</sup>ine for a relatively long period of time (push), as it impacts the smart objects' energy consumption and hence their battery lifetime.

The protocol stacks are different between the CoAP and HTTP cases. CoAP uses UDP as the transport layer protocol, whereas HTTP uses TCP. This has implications for the CoAP-proxy case as well since the protocol translation is required both at the transport and application layers. Ad ditionally, the communication mode affects the protocol stack implementation on smart objects. In the push scenario the smart object requires only a client module, whereas in the pull scenario both client

Please cite this article as: T. Levä, et al., Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.009

T. Levä et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/CKP4QC2P/fulltext/images/936956ba8fc0247229256d345e12fa1c7cf97e56bf2da7c43527e028aad16138.jpg)  
Fig. 1. Technical architecture for all of the cases under comparison.

and server modules are needed. The access points and web server have both client and server modules.

Moreover, the following simplifying assumptions concerning the technical architecture are made:

• The 6lowPan IPv6 header compression format [21] is used to transmit IPv6 packets between the smart objects and the access points, and the translation to regular IPv6 or IPv4 is performed by the access points;

• The smart objects connect directly to access points (i.e., no routing over the smart objects);

• The battery-powered smart objects do not harvest energy (i.e., battery replacements are needed);

• The transmitted messages are short and generally <sup>fi</sup>t into a single IEEE 802.15.4 frame.

## 4.2. Value network

In order to succeed, the business case of a protocol needs to be positive for each stakeholder of the value network. In the most challenging cases, the deployment of a WoT application may require actions from multiple stakeholders. This paper, however, assumes that a single stakeholder – the end-user (company) of the WoT application – controls the whole WoT application, including all the components presented in Fig. 1. This simpli<sup>fi</sup>es the analysis and allows focusing on the total cost of ownership from the perspective of a single potential adopter.

The potential adopters are not necessarily the ones who choose the protocols; they often just buy what technology providers sell to them. However, this does not cause problems to the analysis as the incentives of technology providers and their customers are aligned, and the costs to the technology providers (plus some margin) are included in the prices paid by the customers.

## 4.3. Generic TCO model for a WoT application

This section presents a generic TCO model for a WoT application using the introduced technical architecture and describes the factors that affect the different cost components. The costs are calculated separately for each group of technical components: smart objects (S), access points (A), web servers (W), and the optional proxy component (P). System level costs that cannot be naturally assigned to technical components are listed as other costs (O). The total cost of ownership can be expressed as the sum of the costs for the separate cost components:

$$
T C O = n * S + m * A + l * W + P + O,\tag{1}
$$

where n, m and l denote the number of smart objects, access points and web servers in the installation.

Following David et al. [9], the costs of each main cost category are divided into acquisition $\left( C _ { A c } \right)$ and operating costs $( C _ { O p } ) .$ . The acquisition costs covering the purchase and installation of the technical components are further divided into hardware $( C _ { H W } )$ , software $( C _ { S W } )$ and connectivity setup $\left( C _ { C S } \right)$ costs. The operational costs include hardware and software maintenance $( C _ { M } ) .$ , connectivity $\left( C _ { C F } \right)$ and supply $\left( C _ { S u } \right)$ costs. As a result, the cost function for each of the cost categories can be expressed as:

$$
C = C _ {H W} + C _ {S W} + C _ {C S} + C _ {M} + C _ {C F} + C _ {S u},\tag{2}
$$

where C is replaced with S, A, W, P and O. In the following subsections, each cost component is described with the factors affecting the magnitude of the costs.

## 4.3.1. Costs of smart objects $( n * S )$

Volume discounts ignored, the hardware acquisition costs $( S _ { H W } )$ increase linearly when the number of smart objects (n) increases. The same applies to the software development costs $( S _ { S W } ) ,$ , if the software is a standardized offering and the software costs are incorporated into smart object prices. However, with custom-made software developed speci<sup>fi</sup>cally for the particular application installation, the software development costs are <sup>fi</sup>xed, i.e., they do not depend on the number of smart objects. In this case, the relative share of software costs in the smart object total costs decreases when the number of smart objects increases. The installation of the smart objects incurs personnel costs and potentially also costs for traveling to the sites. However, these initial installation costs are included in the access point installation costs (considered in the next subsection) and are thus excluded here. Finally, since the connectivity between smart objects and the access points uses unlicensed spectrum, the smart object connectivity costs (S , $S _ { C F } )$ can be excluded from the model. Consequently, the acquisition costs of a smart object can be calculated simply as:

$$
S _ {A c} = S _ {H W} + S _ {S W}.\tag{3}
$$

The operating of smart objects incurs only maintenance costs, because the connectivity uses unlicensed spectrum, and because the battery-based operation and small size allow the electricity and facility costs to be avoided. The maintenance costs consist of periodical battery replacement $\left( S _ { M , b } \right)$ and software update $\left( S _ { M , s w } \right)$ costs, as well as occasional hardware replacement costs $( S _ { M , h w } ) . S _ { M , b }$ is a function of i) the number of battery replacements during the lifetime of the application, calculated as a function of the application lifetime (T) and battery lifetime $( t _ { b } ) ; \mathrm { i i } )$ the price of a new battery $( p _ { b } ) ;$ and iii) the labor and travel costs of visiting the sites and carrying out the replacements $( C _ { s i t e - v i s i t } )$ that are divided among all the smart objects on a site $( n _ { s i t e } )$

$$
S _ {M, b} = \frac {T}{t _ {b}} * \left(p _ {b} + \frac {C _ {\text { site - visit }}}{n _ {\text { site }}}\right).\tag{4}
$$

The battery lifetime depends on the capacity of the battery and the average energy consumption of the smart object:

$$
t _ {b} = \frac {\text { Energy   stored   in   a   battery }}{\text { Energy   consumption }} = \frac {\text { Capacity } * \text { Voltage }}{\text { Power }} = \frac {Q * U}{P},\tag{5}
$$

where energy consumption depends on the application speci<sup>fi</sup>c factors, such as the used communication mode (push vs. pull), communication frequency, complexity of parsing, and transferred data volume.

The need for occasionally replacing the smart objects due to malfunctioning causes hardware maintenance costs $\left( { { S _ { M , h w } } } \right)$ . These are incorporated in the TCO model by de<sup>fi</sup>ning the average lifetime of a smart object $\left( t _ { S , h w } \right)$ . Due to the unpredictable nature of hardware failures, smart object replacement incurs an additional site visit:

$$
S _ {M, \mathrm{hw}} = \frac {T}{t _ {S , \mathrm{hw}}} * (S _ {\mathrm{HW}} + C _ {\text { site - visit }}).\tag{6}
$$

Software update costs $\left( S _ { M , s w } \right)$ can be calculated similarly to the hardware maintenance costs by de<sup>fi</sup>ning the average time interval for software updates $( t _ { S , S w } )$ , the development cost of a SW update $\left( S _ { M , s w - u p d a t e } \right)$ divided among all the smart objects, and the installation costs $\left( S _ { M , s w - i n s t a l l } \right)$ . Depending on the application scenario, the software update installation can be either provisioned over the air, which causes connectivity costs, or by visiting the sites as in the case of hardware maintenance.

$$
S _ {M, s w} = \frac {T}{t _ {S , s w}} * \left(\frac {S _ {M , s w - u p d a t e}}{n} + S _ {M, s w - i n s t a l l}\right).\tag{7}
$$

4.3.2. Costs of access points $( m * A )$

The number of access points (m) depends on the number of sites and the number of access points per site. The number of sites can be calculated as a function of the number of smart objects (n) and the number of smart objects per site $( n _ { s i t e } )$ , whereas the number of access points per site depends on the relation between $n _ { s i t e }$ and the maximum number of smart objects an access point can support $( n _ { A P } )$

$$
m = \frac {n}{n _ {\text {site}}} * \frac {n _ {\text {site}}}{n _ {A P}}.\tag{8}
$$

An access point is a wireless router, where the hardware and software costs are bundled into the access point price $\left( { \cal A } _ { H W + S W } \right)$ . The initial installation of the access point (and the smart objects connecting to it) in the sites causes installation costs $( A _ { H W , i n s t a l l } )$ that consist of the personnel costs and costs for travelling to the site. Additionally, equipping each access point with data subscription causes connectivity setup costs $( A _ { C S } )$ . The function for the access point acquisition costs $\left( { { A _ { A c } } } \right)$ can be expressed as:

$$
A _ {A c} = A _ {H W + S W} + A _ {H W, i n s t a l l} + A _ {C S}.\tag{9}
$$

Maintenance costs $\left( A _ { M } \right)$ are calculated similarly as with smart objects as de<sup>fi</sup>ned in Eqs. (6) and (7):

$$
A _ {M, \mathrm{hw}} = \frac {T}{t _ {A , \mathrm{hw}}} * (A _ {\mathrm{HW}} + C _ {\text { site - visit }});\tag{10}
$$

$$
A _ {M, s w} = \frac {T}{t _ {A , s w}} * \left(\frac {A _ {M , s w - u p d a t e}}{m} + A _ {M, s w - i n s t a l l}\right).\tag{11}
$$

The connectivity costs $\left( A _ { C F } \right)$ depend on the pricing model [4] of the long-range connectivity. Simple, <sup>fl</sup>at-rated connectivity pricing schemes are common today and deemed important for boosting the adoption of WoT technologies.<sup>7</sup> Also, when WoT applications are used in domestic deployments, e.g., as a part of a smart home solution, a landline broadband Internet connectivity is usually available, for which <sup>fl</sup>at-rate is a common charging approach [1]. The cost function for the <sup>fl</sup>at-rate pricing scheme can be expressed simply as the function of the application lifetime (T) and the monthly price $\left( A _ { C M F , f l a t } \right)$

$$
A _ {\mathrm{CF,flat}} = T * A _ {\mathrm{CMF,flat}}\tag{12}
$$

On the other hand, a wide range of volume-based pricing schemes is also available. Subscriptions of this type are common in case the smart objects are mobile, potentially even roaming between multiple cellular networks. In the simplest version of volume-based pricing,<sup>8</sup> the price per data unit remains constant irrespective of the transferred data volume. However, some communication service providers $( \mathsf { C S P } ) ^ { \mathfrak { g } }$ offer M2M subscriptions where a tiered pricing is applied, with the price per data unit depending on the data volume, and where pooling data among devices is allowed. With such tiered schemes, the price is subject to a volume discount and decreases as the transferred data volume grows. Due to the large variation in the pricing schemes, the exact connectivity cost function needs to be formulated separately for each application scenario.

Supply costs consist of electricity cost and the rent for premises. The monthly electricity cost is a simple function of the average monthly power consumption of an access point $\left( P _ { A } \right)$ and the unit price of energy (u), whereas the rent for premises $\left( A _ { S u , P r } \right)$ is a constant monthly fee. To obtain the total costs, monthly costs are multiplied with the application lifetime (T):

$$
A _ {S u} = T * \left(P _ {A} * u + A _ {S u, P r}\right).\tag{13}
$$

## 4.3.3. Costs of web servers $( l * W )$

In this model, web servers are assumed to be leased from a hosting provider that charges a monthly fee $( W _ { h o s t i n g } )$ covering all the hardware, connectivity and supply costs. The fee is based on the features of the leased server and the allowed maximum traf<sup>fi</sup>c volume per month. This approach simpli<sup>fi</sup>es the cost function signi<sup>fi</sup>cantly, since only the software acquisition $( W _ { S W } )$ and update costs $( W _ { M , s w } )$ have to be calculated separately. $W _ { S W }$ consists of both the development costs for the protocol stack and the web application. $W _ { M , s w }$ is calculated by de<sup>fi</sup>ning the update interval $\left( t _ { W , s w } \right)$ and the development cost of a single update $( W _ { M , s w - u p d a t e } )$ per web server. Consequently, the cost function of a web server is:

$$
W = T * W _ {\text { hosting }} + W _ {S W} + \frac {T}{t _ {W , s w}} * \left(\frac {W _ {M , s w - u p d a t e}}{l}\right).\tag{14}
$$

## 4.3.4. Costs of a CoAP–HTTP proxy (P)

A CoAP–HTTP proxy is an optional software component that allows CoAP smart objects to communicate with HTTP web server by translating between CoAP and HTTP. The proxy can be implemented either in the access points or in the web server. Based on the selection between these two architectural options, the communication over long-range wireless access link uses either CoAP or HTTP, which may have signi<sup>fi</sup>- cant cost impacts, as discussed later in Section 4.4.

For the sake of simplicity, the proxy costs are calculated as additional costs on top of the normal access point or web server costs. Most importantly, a new software component increases the software development $( P _ { S W } )$ and related software update costs $( P _ { M , s w } )$ . Furthermore, the requirement for more ef<sup>fi</sup>cient hardware may increase the hardware acquisition $( P _ { H W } )$ and related maintenance costs $\left( P _ { M , h w } \right)$ , especially in case the proxy is implemented in access points. All the other costs remain unchanged, thus leading to the following cost function for the proxy:

$$
P = P _ {H W} + P _ {S W} + P _ {M, h w} + P _ {M, s w}.\tag{15}
$$

## 4.3.5. Other costs (O)

Other costs cover the costs related to the acquisition $( O _ { A c } )$ and the operation $( O _ { O p } )$ ) of the WoT application that cannot be naturally assigned to separate technical components. $O _ { A c }$ include time-consuming activities, such as searching for components and providers, asking for tenders, and testing the system, which can partly be outsourced to consultants. ${ { O } _ { O p } }$ consist of the personnel costs related to administering the WoT application, training the personnel, and providing support for the users of the application. Both of these cost components are simply calculated as personnel costs by de<sup>fi</sup>ning the required person months $P M _ { A c } , \ P M _ { O p }$ and the average salary of an employee (Sal , Sal ):

$$
O = O _ {A c} + O _ {O p} = P M _ {A c} * S a l _ {A c} + P M _ {O p} * S a l _ {O p}.\tag{16}
$$

## 4.4. Cost comparison between CoAP and HTTP

Table 1 summarizes the cost components and the notation of the TCO model introduced in the previous section. N/A denotes that the cost component in question is non-applicable (i.e., the cost is zero). The TCO model is generic and can be applied to assess the costs of various WoT solutions, as well as to compare the cost implications of using different communication protocols, software interfaces, and other technical alternatives that a designer of the WoT solution may need to analyze. Furthermore, the TCO model is suf<sup>fi</sup>ciently generic to be used also outside of WoT applications, because the technical architecture of IT systems consists typically of clients (S), middle-boxes (A, P) and servers (W), which are the key components of the model.

This paper focuses on comparing the costs of WoT applications based on CoAP and HTTP. Therefore, the potential sources for cost differences between CoAP and HTTP are highlighted with boldface in Table 1 and discussed further in the following subsections.

## 4.4.1. Smart object costs

As CoAP has been developed speci<sup>fi</sup>cally for constrained devices, the largest reduction in costs is expected with smart objects. The more modest memory and processor requirements likely allow the use of cheaper hardware. Furthermore, the simplicity of CoAP speci<sup>fi</sup>cation as compared with HTTP may lead to savings in software development costs due to faster and easier implementation. In the early stages of CoAP adoption, however, the case may be the opposite, because HTTP as the incumbent protocol may be more familiar to developers and existing software may be reused. This difference should not be very large, though, since CoAP is seen as very “HTTPish” [3]. The differences in hardware and software acquisition costs may also affect the related maintenance costs.

Due to the smaller number of bits transferred, CoAP smart objects consume less energy than HTTP smart objects. This difference becomes more evident in the push mode of communication where the time when the receiver is active can be reduced signi<sup>fi</sup>cantly. As a consequence, the batteries last longer, resulting in a smaller number of possibly costly battery replacements. Due to its potentially signi<sup>fi</sup>cant cost impact, the difference in energy consumption and battery lifetime between HTTP and CoAP is considered in detail in Appendix A for both pull and push modes of communication by aggregating the available literature sources with the results of our own measurements.

## 4.4.2. Access point costs

Since access points only route packets between the local area and wide area networks, they do not care about the application or transport layer protocols used by the smart objects. Therefore, the selection between CoAP and HTTP does not affect the acquisition costs. However, the protocol stack of smart objects might affect the number of access points needed, because every bit of traf<sup>fi</sup>c makes a difference in the 802.15.4 networks that are strongly limited in channel capacity. The larger number of packets due to TCP and larger overhead due to HTTP impede the network scalability as compared with CoAP + UDP. Consequently, an access point may support a larger number of CoAP than HTTP smart objects, which matters in those application scenarios where the number of smart objects in the coverage area of an access point exceeds the number of smart objects that a single access point can serve. The increase in the number of access points affects also the number of connectivity subscriptions and replaceable access points.

The selection between CoAP and HTTP may create signi<sup>fi</sup>cant difference in connectivity costs in case the long-range connectivity is based on transferred data volume, because CoAP uses up to 10 times fewer bits in communication. Additionally, CoAP can also use SMS as a carrier [2], which may prove to be cheaper than cellular data in some application scenarios.

## 4.4.3. Web server costs

Similarly to the smart objects, the development costs of the CoAP protocol stack may be higher than those of HTTP due to the better

## Table 1

Generic TCO model for a WoT application: technical components and related cost components, The sources of potential cost differences between CoAP and HTTP are highlighted with boldface.

<table><tr><td>Cost component</td><td>Smart object (S)</td><td>Access point (A)</td><td>Web server (W)</td><td>CoAP–HTTP proxy (P)</td><td>Other (O)</td></tr><tr><td>Acquisition cost – HW ( $C_{HW}$ )</td><td>Purchase, install</td><td>Purchase, install</td><td>Purchase, install</td><td>Purchase</td><td rowspan="3">Transaction costs</td></tr><tr><td>Acquisition cost – SW ( $C_{SW}$ )</td><td>Develop, install</td><td>Develop, install</td><td>Develop, install</td><td>Develop</td></tr><tr><td>Acquisition cost – connectivity setup ( $C_{CS}$ )</td><td>N/A</td><td>Subscription setup fee</td><td>Subscription setup fee</td><td>N/A</td></tr><tr><td>Operational cost – maintenance ( $C_M$ )</td><td>Battery, HW, SW</td><td>HW, SW</td><td>HW, SW</td><td>HW, SW</td><td rowspan="3">Admin, training, support</td></tr><tr><td>Operational cost – connectivity fee ( $C_{CF}$ )</td><td>N/A</td><td>Monthly fee</td><td>Monthly fee</td><td>N/A</td></tr><tr><td>Operational cost – supplies ( $C_{Su}$ )</td><td>N/A</td><td>Electricity, premises</td><td>Electricity, premises</td><td>N/A</td></tr></table>

Please cite this article as: T. Levä, et al., Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.009

availability of software implementations, documentation, and knowledgeable developers for the latter. On the other hand, CoAP can provide cost savings over HTTP in the monthly hosting fee due to the signi<sup>fi</sup>cantly smaller data volume, which may allow use of a cheaper hosting service subscription. Furthermore, a single server may be able to support a larger number of CoAP smart objects and concurrent UDP communication sessions, as compared with HTTP + TCP combination.

## 5. Cost-ef<sup>fi</sup>ciency of CoAP and HTTP in WoT applications

In order to populate the cost-comparison of CoAP and HTTP with actual numbers, a TCO calculation and comparison model was developed on the basis of the mathematical formulation presented in Section 4. The use of the developed model is demonstrated by analyzing an environment monitoring application, where a large number of environmental sensors regularly transmit the measurements of temperature, humidity, solar radiation, air quality, etc. to the web server. After introducing this baseline scenario, a sensitivity analysis is conducted where the descriptive parameters of the application scenario are varied in order to identify the characteristics that make a particular application scenario more or less attractive for CoAP.

For the purposes of the cost comparison, the values for different parameters and cost components need to be estimated. When considering the values of the cost components, the Western European and US markets are taken as the focal market for the WoT application deployment. Other regions, e.g., the Asia-Paci<sup>fi</sup>c countries, also represent a promising market for WoT applications. However, for the practical reason of the unavailability of pricing information, they were left outside of the scope of this paper.

Since the paper focuses on comparing the costs of CoAP and HTTP, the attention in the quantitative analysis is devoted to de<sup>fi</sup>ning the values for those cost components that are affected by the application layer protocol. However, the costs that do not differ between CoAP and HTTP are also included in the TCO model in order to estimate the relative signi<sup>fi</sup>cance of the cost differences. When de<sup>fi</sup>ning the values for these cost components, relatively high, though realistic values are chosen, so that the relative cost difference between CoAP and HTTP would not be over-estimated.

## 5.1. Baseline scenario

This scenario considers a deployment of autonomous stations for environment monitoring – such as Adcon Dust Monitoring Stations<sup>10</sup> – that regularly transmit the measurements of temperature, humidity, solar radiation, wind and precipitation, and air quality to the web server. Contemporary stations are working autonomously, owing to internal batteries. The companies specializing in environmental sensing may need to operate hundreds or thousands of stations that are spread across a wide area. Due to this, also the number of sites is high. To limit the number of access points needed, the smart objects use 2.4 GHz radio with range up to 1 km to connect with access points. The communication model is push, meaning that the smart objects occasionally wake up from sleep to conduct measurements and communicate the results, before going to sleep again. In the base setup, this happens once per minute. Being deployed in a remote place, the access point is assumed to rely on cellular network to provide connectivity. The <sup>fl</sup>at-rate pricing scheme is assumed in the baseline scenario, since the resulting communication costs are likely to be an order of magnitude lower than the costs accrued by using a typical volume-based pricing. However, the impact of volumebased pricing schemes is also analyzed.

Table 2 lists the descriptive scenario parameters. The other parameter values used in the calculation are introduced in Appendix B with relevant justi<sup>fi</sup>cations.

## Table 2

The descriptive parameters of the baseline scenario.

<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td></tr><tr><td>Mode of communications</td><td></td><td>Push</td></tr><tr><td>Connectivity pricing scheme</td><td></td><td>Flat-rate</td></tr><tr><td>Number of smart objects in one installation</td><td>n</td><td>10,000</td></tr><tr><td>Number of smart objects per site</td><td> $n_{site}$ </td><td>50</td></tr><tr><td>Lifetime of the application</td><td>T</td><td>20 years</td></tr><tr><td>Frequency of communication</td><td>f</td><td>1/min</td></tr><tr><td>Site visit cost</td><td> $C_{site-visit}$ </td><td>€129</td></tr></table>

The TCO comparison calculation for the baseline scenario is presented in Table 3. With the chosen values, the CoAP-based solution is 6.5% (i.e., €495,800) less expensive than HTTP-based. This is explained by three key reasons:

i. The acquisition costs of smart objects are smaller with CoAP due to cheaper HW (€50 vs. €55), which also affects the hardware maintenance costs.

ii. The lower energy consumption of CoAP smart objects (see Appendix A for details) translates into smaller number of battery replacements (2 vs. 7) during the lifetime of the application, which reduces the maintenance costs signi<sup>fi</sup>cantly.

iii. The notably smaller traf<sup>fi</sup>c volume of CoAP allows the use of a cheaper hosting service, even though the absolute difference in web server costs is relatively minor. The higher development costs of the CoAP stack reduce this difference.

Although Table 1 listed the smart object software costs as a potential differentiator between CoAP and HTTP, they are assumed to be the same for both CoAP and HTTP in the baseline scenario. On the one hand, CoAP speci<sup>fi</sup>cations are simpler, making its implementation more compact and hence making it simpler to <sup>fi</sup>t the software to the constrained memory of the smart object. On the other hand, the use of CoAP demands from the developers the knowledge of the protocol and the libraries implementing it. Thus, when using CoAP instead of HTTP, the software development efforts <sup>fi</sup>rst increase due to the need to learn the protocol, but later decrease due to the more compact implementation. As a result, according to the domain experts, the overall smart object software development time is similar for CoAP and HTTP.

## 5.2. Baseline scenario with volume-based pricing

Access point costs account for a signi<sup>fi</sup>cant share of the TCO in the baseline scenario, but there is no difference between CoAP and HTTP in this cost component, since a single access point per site suf<sup>fi</sup>ces in both cases and since the connectivity is <sup>fl</sup>at-rated. The situation changes, however, if the pricing for the 3G connectivity is volume-based. Together, 10,000 smart objects require 62 GB and 434 GB of data to be transferred monthly by a CoAP-based and HTTP-based solution, respectively. In particular, applying the tiered M2M pricing scheme of Sprint<sup>11</sup> will induce circa €225,000 and €1,577,000 in data communication costs over the lifetime of the application.<sup>12</sup> In this case, the communication costs become the most in<sup>fl</sup>uential cost differentiator between the protocols, making the use of CoAP economically clearly justi<sup>fi</sup>able, as shown in Table 4. Thus, a fourth reason for choosing CoAP over HTTP emerges:

iv. The notably smaller traf<sup>fi</sup>c volume enabled by CoAP translates into signi<sup>fi</sup>cant savings in connectivity costs in the case of volume-based pricing.

## 5.3. The cost impact of CoAP–HTTP proxy

A CoAP-proxy implementation introduces an alternative approach to end-to-end CoAP for realizing the web server side of the CoAP application.

Table 3  
TCO comparison between CoAP and HTTP for the baseline scenario.

<table><tr><td colspan="2">Cost component</td><td>Symbol</td><td>CoAP (€)</td><td>HTTP (€)</td><td>Difference(€)</td><td>Difference(%)</td></tr><tr><td colspan="7">Smart object costs</td></tr><tr><td>Eq. (3)</td><td>Acquisition</td><td> $n * S_{Ac}$ </td><td>540,000</td><td>590,000</td><td>-50,000</td><td>-8.5%</td></tr><tr><td>Eq. (4)</td><td>Maintenance,battery</td><td> $n * S_{M,b}$ </td><td>123,600</td><td>432,600</td><td>-309,000</td><td>-71.4%</td></tr><tr><td>Eq. (6)</td><td>Maintenance,hardware</td><td> $n * S_{M,hw}$ </td><td>3,580,000</td><td>3,680,000</td><td>-100,000</td><td>-2.7%</td></tr><tr><td>Eq. (7)</td><td>Maintenance,software</td><td> $n * S_{M,sw}$ </td><td>100,000</td><td>100,000</td><td>-</td><td>-</td></tr><tr><td></td><td></td><td> $n * S$ </td><td>4,343,600</td><td>4,802,600</td><td>-459,000</td><td>-9.6%</td></tr><tr><td colspan="7">Access point costs</td></tr><tr><td>Eq. (9)</td><td>Acquisition</td><td> $m * A_{Ac}$ </td><td>152,600</td><td>152,600</td><td>-</td><td>-</td></tr><tr><td>Eq. (10)</td><td>Maintenance,hardware</td><td> $m * A_{M,hw}$ </td><td>251,600</td><td>251,600</td><td>-</td><td>-</td></tr><tr><td>Eq. (11)</td><td>Maintenance,software</td><td> $m * A_{M,sw}$ </td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Eq. (12)</td><td>Connectivity(flat-rate)</td><td> $m * A_{CF}$ </td><td>720,000</td><td>720,000</td><td>-</td><td>-</td></tr><tr><td>Eq. (13)</td><td>Supply</td><td> $m * A_{Su}$ </td><td>161,959</td><td>161,959</td><td>-</td><td>-</td></tr><tr><td></td><td></td><td> $m * A$ </td><td>1,286,159</td><td>1,286,159</td><td>-</td><td>-</td></tr><tr><td colspan="7">Web server costs</td></tr><tr><td>Eq. (14)</td><td></td><td> $l * W$ </td><td>317,600</td><td>354,400</td><td>-36,800</td><td>-10.4%</td></tr><tr><td colspan="7">Other costs</td></tr><tr><td>Eq. (16)</td><td></td><td>O</td><td>1,220,000</td><td>1,220,000</td><td>-</td><td>-</td></tr><tr><td colspan="2">Total cost of ownership</td><td>TCO</td><td>7,167,359</td><td>7,663,159</td><td>-495,800</td><td>-6.5%</td></tr></table>

n\*S = Total web server costs m\*A=Total access point costs l\*W=Total web server costs O=Total other costs.

As explained in Section 4.3.4, the smart object side remains unchanged and the cost difference between CoAP and CoAP-proxy cases depends solely on the cost ratio between the CoAP server implementation (€20,000) and the combination of HTTP server (€0) and proxy module implementation (€5000). Even though the proxy implementation should be favored on the basis of this calculation, the cost difference is minor as compared with the difference in the TCO. From the cost perspective, the implementation location of the proxy has a larger cost impact than the implementation itself has. In case the connectivity pricing is volumebased, the proxy should namely be implemented in the web server in order to bene<sup>fi</sup>t from the cost savings described in Section 5.2. Finally, the end-to-end implementation may provide performance bene<sup>fi</sup>ts over the proxy implementation that are not taken into account in the calculation. As a consequence, the decision between CoAP and CoAP-proxy implementation is likely to be based on architectural requirements related to, e.g., security, performance or caching, rather than on cost-ef<sup>fi</sup>ciency.

## 5.4. Sensitivity analysis

Typically, a sensitivity analysis is conducted to control the uncertainties related to the estimated parameter values, with the objective to study how sensitive the results are to the changes in the estimated values. In this paper, however, the focus is not on the TCO itself, but on the absolute and relative cost difference between CoAP and HTTP. Therefore, it is more interesting to identify the characteristics of the more and less attractive application scenarios. In order to accomplish that, the descriptive parameters of the baseline scenario listed in Table 2 are varied to analyze how the difference in TCO between the CoAP- and HTTP-based solutions behaves. Generally, CoAP becomes more attractive when the relative difference (%) increases. The relative difference is calculated by dividing the absolute difference (€) in the TCO by the TCO of HTTP. It shall be remembered that, if the TCO is high, even a small relative difference translates into substantial absolute difference. As a consequence, both the absolute and relative cost differences need to be understood for the purpose of evaluating the attractiveness of CoAP in different application scenarios.

Comparison of the <sup>fl</sup>at-rate and volume-based pricing schemes in the baseline scenario.

<table><tr><td></td><td>CoAP (€)</td><td>HTTP (€)</td><td>Difference(€)</td><td>Difference(%)</td></tr><tr><td colspan="5">Connectivity costs</td></tr><tr><td>Flat-rate</td><td>720,000</td><td>720,000</td><td>-</td><td>-</td></tr><tr><td>Volume-based, tieredpricing of Sprint</td><td>225,271</td><td>1,576,898</td><td>-1,351,626</td><td>-85.7%</td></tr><tr><td colspan="5">Total cost of ownership</td></tr><tr><td>Flat-rate</td><td>7,167,359</td><td>7,663,159</td><td>-495,800</td><td>-6.5%</td></tr><tr><td>Volume-based, tieredpricing of Sprint</td><td>6,672,630</td><td>8,520,057</td><td>-1,847,426</td><td>-21.7%</td></tr></table>

## 5.4.1. Frequency of communications (f)

In the case of <sup>fl</sup>at-rate connectivity pricing, the communication frequency affects only the energy consumption of smart objects. With the push mode of communication, the battery lifetime is de<sup>fi</sup>ned by self-discharge for both CoAP and HTTP, when the communication frequency is smaller than 25/h. With values larger than 25/h, the battery replacement costs of CoAP and HTTP start to diverge step-wise due to additional battery replacements required by HTTP smart objects. The battery replacement costs of CoAP smart objects remain unchanged until the communication frequency reaches 144/h. As a result, also the relative cost difference increases, as shown in Fig. 2. A similar pattern is visible with the pull mode of communication, because the difference in the number of battery replacements between CoAP and HTTP evolves similarly in both the push and pull modes.

In the case of volume-based connectivity pricing, the increasing communication frequency increases the absolute and relative cost difference between CoAP and HTTP. The step-wise pattern of battery replacements is still visible, but the volume-based pricing makes CoAP signi<sup>fi</sup>cantly more attractive.

It should be noted that, for the sake of simplicity, the hosting fee of web servers $( W _ { h o s t i n g } )$ is not modeled as a function of the communication volume. As a consequence, the web server costs remain unchanged even though the changing frequency (and the changing number of smart objects analyzed in Section 5.4.2) affects the communication volume. However, this simpli<sup>fi</sup>cation does not have signi<sup>fi</sup>cant impact on the results, because the data volume in the baseline scenario is rather high, and still the impact of the web-server hosting fee on the TCO is minor due to the generally low hosting fees.

## 5.4.2. Number of smart objects (n)

The number of smart objects largely de<sup>fi</sup>nes the scale of a WoT application — including also the number of sites since the number of smart objects per site $( n _ { \mathrm { s i t e } } )$ is kept constant at 50 objects. The TCO of both CoAP and HTTP, and the absolute cost difference between them, increase linearly with the number of smart objects. However, as illustrated in Fig. 3, the relative cost difference between CoAP and HTTP increases logistically from 2.1% (n = 1) to 7.7% until n reaches approximately 110,000. The difference is small in the beginning as the costs that do not depend on the number of smart objects dominate. However, the relative cost difference grows fast with the number of smart objects and reaches 6.5% already with 10,000 smart objects. After 110,000 smart objects, the marginal cost for adding one smart object is €550 for CoAP and €596 for HTTP, where the €46 cost difference originates from the difference in smart object hardware and battery replacement costs.

![](/api/attachments/CKP4QC2P/fulltext/images/9ac52cbcefe976336a05443942ffa790a8d4ba919d2b7dc6251c64458ecbbba0.jpg)  
Fig. 2. Impact of communication frequency on the relative cost difference between CoAP and HTTP.  
Please cite this article as: T. Levä, et al., Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.009

The communication mode does not affect the behavior of the cost difference function but lowers the upper limit from 7.7% to 6.0%. In the case of the volume-based pricing, the behavior stays similar, but the upper limit increases signi<sup>fi</sup>cantly (to 26.6% in push mode, and to 19.5% in pull mode) since the increasing number of smart objects affects the transferred data volume directly.

It should be noted that, in the TCO model used, the scale of the application does not automatically affect the level of other costs (O), even though a dependency may exist between them. This limitation, however, concerns only the cases with a very small number of smart objects, where the potentially high other costs mask the relative cost difference between CoAP and HTTP. On the other hand, the other costs may be underestimated with a high number of smart objects; however, even after an order of magnitude increase they remain negligible as compared with the TCO.

## 5.4.3. Number of smart objects per site $( n _ { s i t e } )$

The distribution of smart objects across the sites has a potentially large cost impact. In the TCO model, this is controlled with the number of smart objects per site, which also affects the number of access points per site. With a constant number of smart objects, the number of sites, as well as the related access point costs, decrease when the number of smart objects per site increases. The battery replacement costs also decrease, because the number of sites to visit decreases. In consequence, the TCO decreases exponentially with the increasing number of smart objects per site. In the most extreme case of only one smart object per site, which effectively means that each smart object would be equipped with a cellular modem, the TCO of CoAP and HTTP are 72.7 and 79.5 million euros, respectively. With <sup>fi</sup>ve objects per site, the TCO is only one fourth of that, and with 100 objects the TCO already approaches the lower boundary of 6.2 and 6.7 million euros.

The relative cost difference between CoAP and HTTP, however, does not depend signi<sup>fi</sup>cantly on the distribution of smart objects across the sites. The small, stepwise variation is caused by the difference in the scalability of access points, which starts to have an impact on the costs when $n _ { s i t e }$ becomes larger than $n _ { A P }$ for HTTP $( n _ { s i t e } > 1 0 0 )$ . After this point, the difference in the access point costs depends heavily on how ef<sup>fi</sup>ciently the smart objects are distributed across the sites in relation to $n _ { A P * }$ For example, when $n _ { s i t e } \mathrm { i } s 2 0 0$ , the number of access points needed is 50 for CoAP and 100 for HTTP. However, if $\dot { n } _ { s i t e }$ is 120, the number of APs grows to 84 and 168 for CoAP and HTTP, respectively, since each site requires two APs in the case of HTTP, even though they are underutilized. This is visible in Fig. 4 as a stepwise increase in the relative TCO difference when $n _ { s i t e } > 1 0 0$ , after which the difference starts to decrease again. When n grows over 200, the step goes in the opposite direction since both HTTP and CoAP require additional access points per site, which leads to a large increase in TCO.

![](/api/attachments/CKP4QC2P/fulltext/images/62f11db176b8fe4b702c61d71e516aed23b03ca8c359efc3b6d686ae5a729ff6.jpg)  
Fig. 3. Impact of the number of smart objects on the relative cost difference between CoAP and HTTP Please note the logarithmic scale on x-axis

With volume-based pricing, the relative cost difference behaves similarly to the <sup>fl</sup>at-rate pricing. This is due to the fact that, no matter whether volume-based or <sup>fl</sup>at-rate pricing is used, the related charges for the data communications remain unchanged or increase insigni<sup>fi</sup>- cantly along with $n _ { s i t e } ,$ , as long as the overall number of smart objects or APs, respectively, is kept constant. The only exception is the growth of the relative difference for $n _ { s i t e } < 1 0 0 .$ . This can be attributed to the rapidly increasing contribution of CoAP to the reduction in the communication costs in the case of volume-based pricing, which is especially notable when the number of sites grows.

## 5.4.4. Site visit cost $\left( C _ { s i t e - v i s i t } \right)$

In the TCO model, the site visit cost incurs during the initial installation and maintenance of smart objects and access points. It is effectively used as a proxy for the distance between the smart objects and the headquarters and can thus be seen as a descriptive parameter. In the <sup>fi</sup>eld installations distributed over a wide geographic area, the cost is naturally higher than in the local installations.

In the baseline scenario, most site visits relate to battery replacements, where the cost is divided among all the smart objects in the site. Therefore, the sensitivity of the TCO to the level of site visit cost depends heavily on the number of objects per site. If the site visit cost is divided among a large number of objects, the impact to the TCO remains low. This is exactly the case in the baseline scenario, where both the absolute and relative cost differences (Fig. 5) are very insensitive to the changes in the site visit cost. With a small number of objects per site (which also leads to a large number of sites), the increase in site visit cost signi<sup>fi</sup>cantly increases the relative cost difference between CoAP and HTTP. With a higher number of smart objects per site, the impact is the opposite.

## 5.4.5. Lifetime of application (T)

The lifetime of the application has a direct impact on the volume of op erational costs and thus on the TCO. The absolute cost difference between CoAP and HTTP also increases along with the application lifetime. However, the relative cost difference is rather robust to the changes in lifetime,

![](/api/attachments/CKP4QC2P/fulltext/images/4240abf52704391c1230053840ea4957866c2f8c1c1b73906ba2b0b32040eb04.jpg)  
Fig. 4. Impact of the distribution of smart objects across the sites on the relative cost difference between CoAP and HTTP

Please cite this article as: T. Levä, et al., Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.009

![](/api/attachments/CKP4QC2P/fulltext/images/8c655c7e13ea5815f691381dd44827b43dc0c31473df5ed8e2fc1a74364553df.jpg)  
Fig. 5. Impact of the site visit cost on the relative cost difference between CoAP and HTTP with differing number of smart objects per site.

even though the different timing of the battery replacements creates minor <sup>fl</sup>uctuation visible in Fig. 6. The <sup>fi</sup>gure illustrates again that CoAP is more attractive in applications that use the push mode rather than the pull mode, especially if the connectivity pricing is volume-based.

## 6. Discussion

In the previous section, the cost-ef<sup>fi</sup>ciency of CoAP was assessed by comparing the total costs of the solutions based on CoAP against the costs of alternative solutions relying on HTTP. The results of the TCO analysis indicate several areas where the use of CoAP is justi<sup>fi</sup>able in terms of costs.

First, the use of CoAP is cost-ef<sup>fi</sup>cient in the applications where its use enables a noticeable reduction in the battery replacement costs by prolonging the battery lifetime. The difference between the CoAP and HTTP protocols in the battery lifetime grows along with the frequency of communication sessions. Further, the difference is greater in the applications where the push mode of communication can be used. Still, similar battery lifetime improvements may be attained in the pull mode of communication, if delays in responding to requests or responding with a cached result are tolerated. However, often the power consumption of the solution is so low that the battery lifetime is limited by the selfdischarge of the batteries rather than by the application layer protocols. Also, the use of higher-capacity batteries could often mitigate the battery lifetime limitations. Thus, in summary, the battery lifetime differences make CoAP cost-bene<sup>fi</sup>cial only in the scenarios with frequent communications, high battery replacement costs, and limited battery capacity.

![](/api/attachments/CKP4QC2P/fulltext/images/dd8b5683830f996faf3de9b8d9e9490feeb8f1ae70d28d04e890adec6ad7ebbc.jpg)  
Fig. 6. Impact of the lifetime of the application on the relative cost difference between CoAP and HTTP

Second, the use of CoAP is bene<sup>fi</sup>cial cost-wise when the number of smart objects is high, since simpler and less expensive (class 1) smart objects are suf<sup>fi</sup>cient for the CoAP implementations, as compared with the more powerful and more expensive (class 2) smart objects needed in the HTTP solutions [3]. While the cost difference of a single object is small in absolute value, the difference in the total cost of a solution grows quickly along with the number of the smart objects used.

Third, the use of CoAP allows the cost of the applications to be decreased dramatically in case the charging for the data communications is volume-based, since the small overhead of the protocol and its reliance on the UDP enable a manifold reduction in the transferred data volume. This impact is particularly signi<sup>fi</sup>cant when both the communication frequency and the number of smart objects are high.

Finally, CoAP is expected to bring cost advantages in the scenarios where the number of smart objects per site is high. This can be attributed to the fact that CoAP relies on UDP as a transport layer protocol whereas TCP is commonly used with HTTP. UDP transmissions incur lighter load on the constrained 802.15.4 network as compared with the use of TCP, so a single access point can handle a larger number of CoAP than HTTP smart objects. As a result, in the application scenarios with a high number of objects per site and the need for simultaneous communications with them (more likely in the pull mode of communication), the use of CoAP will allow for the number of access points to be reduced, resulting in smaller access point costs.

This paper has some limitations that need to be taken into account when interpreting the obtained results. First, the analysis is limited to comparing only CoAP with HTTP. In future work, proprietary solutions currently dominating the market could also be included in the comparison. Arguably, in certain solutions involving highly constrained smart objects, the IETF protocol stack, including IPv6, UDP, and CoAP, can be seen as too heavy as compared with the proprietary protocols. Second, the estimates for some of the cost values provided by the experts rely on their knowledge and experience, and may not be fully accurate. Likewise, the measurements of the protocol energy footprint were made for a single hardware platform and using a small payload in the transmitted messages. Therefore, the results should be cautiously generalized to the other constrained platforms and message sizes. To mitigate the problem of possible inaccuracies in individual estimates, a sensitivity analysis was conducted. In the future work, it shall be complemented with further <sup>fi</sup>eld measurements or expert estimates.

Although the paper has studied the costs of using CoAP vs. HTTP as a factor affecting the adoption of CoAP, other factors may in<sup>fl</sup>uence adoption decisions as well. From the technical perspective, HTTP cannot be used in all application scenarios, because it lacks some functionality (e.g., the subscription mechanism) provided by CoAP. On the other hand, CoAP has yet to see the attempts at breaking its security provisions, which may make the security cautious vendors to delay their adoption decisions until they see that the protocol security is mature enough. CoAP may also require some changes in the vendor or communication service provider infrastructure, such as allowing the UDP traf<sup>fi</sup>c, and some of the companies may be reluctant to do that.

From the economic perspective, a large installed base resulting in higher network effects may cause inertia in the adoption of an emerging protocol that is technically superior. HTTP is currently well established in the market, and thus has better availability of tools, platforms and knowledgeable experts. In this analysis, the network effects have been taken into account by considering the cost of a proxy and the cost of developing software for CoAP-based solutions. Finally, some of the vendors may be satis<sup>fi</sup>ed with their proprietary systems giving them more control over the ecosystem than open standards would give. These and other factors shall be taken into account when analyzing the overall potential of CoAP.

## 7. Conclusion

CoAP has been recently introduced by the IETF Core working group as a simpler alternative to HTTP for enabling Web applications to interact with constrained smart objects. The expected adoption of the protocol depends, among other factors, on its cost advantage as compared with HTTP and other alternatives. In this paper, the costef<sup>fi</sup>ciency of CoAP has been studied by introducing a total cost of ownership (TCO) model for WoT applications, and by comparing the cost differences between CoAP and HTTP in an exemplary application scenario. In this generic TCO model, the costs were calculated for each group of technical components – smart objects, access points, web servers, and optional protocol-translation proxy module – and divided into acquisition and operational costs related to hardware, software, data communications, electricity and facilities. The important factors affecting the TCO include the number of technical components, the installation location and distribution of smart objects, communication mode in use, frequency and data volume of transactions, charging model for data communications, and lifetime of application.

The results of the analysis indicate several application scenarios where the use of CoAP is more cost-ef<sup>fi</sup>cient than HTTP for the purpose of connecting constrained smart objects to the Web. In particular, using CoAP is more cost-ef<sup>fi</sup>cient in the applications with high frequency of communications, where the use of the protocol decreases the power consumption of the smart objects, thus allowing the operational cost of battery replacement to be reduced. This is especially notable in the applications where the smart objects are deployed in distant places and thus the cost of replacing the batteries is relatively high. The use of CoAP was also found to be more cost-ef<sup>fi</sup>cient in the scenarios where the smart objects are kept asleep between the communications sessions, as opposed to the applications where the smart objects need to awake frequently. Further, in case the charging for the data communications is volume-based, the use of CoAP allows the cost of the applications to be decreased dramatically, since the small overhead of the protocol and its reliance on the UDP enable a manifold reduction in the transferred data volume. Finally, since less powerful and hence less expensive smart objects can be used in the CoAP-based solutions, the use of the protocol was found to be more cost-ef<sup>fi</sup>cient in the applications involving a large number of smart objects, where the cost difference becomes signi<sup>fi</sup>cant along with the growing number of smart objects.

The results of the paper aim to support the organizations assessing whether CoAP or HTTP shall be used as a cost-ef<sup>fi</sup>cient application layer protocol in their solutions. This is achieved by identifying the critical factors to be taken into account in the assessment and by explaining the likely effects of these factors. The analysis in the paper may also bene<sup>fi</sup>t the working groups involved in CoAP standardization activities, by indicating the economic bene<sup>fi</sup>ts and limitations of the protocol. In future work, the analysis presented in the paper may be expanded in several ways. Firstly, some of the cost estimates relying on the expert judgment could be complemented with measurement experiments, which could include other hardware platforms, patterns of communication, and payload sizes as well. Secondly, the comparison could be expanded to include also proprietary protocols. Various CoAP intermediaries, such as proxies, caches and access points, and their functionality, placement, and role in the total CoAP solution cost could also be investigated. Finally, not only costs but also the expected bene<sup>fi</sup>ts, roadblocks, and other factors affecting the adoption of CoAP could be included in the analysis.

## Acknowledgments

The authors wish to thank Heikki Hämmäinen, Lea Heinonen-Eerola, Ari Keränen, Kalevi Kilkki, Salvatore Loreto, and Zach Shelby for their constructive comments and suggestions. The authors also thank the anonymous reviewers for their insightful comments and critique.

The research reported in this paper was supported by the Finnish Funding Agency for Technology and Innovation (TEKES) as part of the Internet of Things program of DIGILE (Finnish Strategic Centre for Science, Technology and Innovation in the <sup>fi</sup>eld of ICT and digital business). The work has also been supported by the Graduate school in Electronics,

Telecommunications and Automation (GETA), and the Future Internet Graduate School (FIGS).

## Appendix A. Energy consumption of CoAP vs. HTTP

One of the main promises of the CoAP protocol is the reduced energy footprint of the applications. The expected reduction in the consumption depends on whether the communication is carried out in the pull mode (implying a smart object always ready to respond to an incoming request) or in the push mode (implying a mainly sleeping smart object periodically sending the information to a remote end-point).

## A.1. Pull mode

As reported by Colitti et al. [7,8] for the pull mode of communication, given the request inter-arrival time of t = 10 s, the use of CoAP allows the energy consumption to be cut roughly by 50%, as compared with HTTP. However, the energy saving becomes practically negligible as soon as the inter-arrival interval increases to t = 120 s [8]. This is attributed to the fact that, due to the pull mode, the smart object spends a signi<sup>fi</sup>cant portion of time in the listening mode, in which the energy consumption is similar for both CoAP and HTTP.

Also, it was found that, already for a 120 s interval, the power consumption of both protocols stabilizes at the level of circa 0.72– 0.75 mW. This can be explained by the radio duty cycling whereby the radio transmitter and CPU are (periodically) turned on to make the smart object responsive in the pull mode. Consequently, with the increase of the interval, the constant energy drainage due to reception E and CPU cycles $E _ { C P U }$ starts to dominate the overall energy consumption pro<sup>fi</sup>le. Therefore, it is assumed that for longer intervals (t ≥ 5 min), the power consumption in pull mode stays at the level of 0.72 mW, as summarized in Table A.1 based on the <sup>fi</sup>ndings by Colitti et al. [8].

Table A.1  
The power consumption P (mW) in pull mode.

<table><tr><td>Interval t</td><td>5 s</td><td>10 s</td><td>30 s</td><td>60 s</td><td>120 s</td><td>≥5 min</td></tr><tr><td>P(HTTP), mW</td><td>1.9</td><td>1.4</td><td>0.96</td><td>0.81</td><td>0.76</td><td>0.72</td></tr><tr><td>P(CoAP), mW</td><td>0.83</td><td>0.76</td><td>0.71</td><td>0.72</td><td>0.72</td><td>0.72</td></tr></table>

## A.2. Push mode

In order to estimate the difference in the energy consumption for the push mode, a set of experiments was carried using Advanticsys CM5000 (Tmote Sky-compatible) motes running Contiki OS as smart objects. A simple client was implemented on the smart object. The client was sending the lightness and energy consumption measurements from the embedded sensor to the server every 10, 30, or 120 s using either the CoAP or HTTP protocol. Thus, in total, six experiment runs were conducted: three for CoAP and three for HTTP. In each experiment run, 50 measurements and communication sessions were executed, and the recorded energy measurements were averaged. To reduce the energy consumption, radio duty cycling was disabled between the communication sessions. The content of the response message was slightly shorter for HTTP than for CoAP. It shall be also noted that the battery consumption by sensor circuits and <sup>fl</sup>ash memory circuits was not included in the estimation. Besides, the experiments were conducted in the environment where the loss of packets was relatively infrequent. Therefore, the obtained values are underestimating the power consumption in the <sup>fi</sup>eld.

To measure the energy consumption of the smart object, the Energest tool built in the Contiki OS [11] was used. This tool enables the estimation of the energy consumption during the reception, the transmission, the CPU cycles, and in the low power mode, based on time spent in the modes $t _ { R X } , t _ { T X } , t _ { C P U } ,$ and $t _ { L P M } ,$ respectively, as:

$$
E = U I _ {R X} t _ {R X} + U I _ {T X} t _ {T X} + U I _ {C P U} t _ {C P U} + U I _ {L P M} t _ {L P M},\tag{A.1}
$$

where the voltage (U) and the values of the currents (I) in different modes are obtained from the technical speci<sup>fi</sup>cations by summing up the currents of the microcontroller and the radio frequency transceiver,<sup>14</sup> as shown in Table A.2.

Table A.2  
The voltage and combined currents of the microcontroller and the radio frequency transceiver used in the different modes of operation.

<table><tr><td>U, V</td><td> $I_{RX}$ , mA</td><td> $I_{TX}$ , mA</td><td> $I_{CPU}$ , mA</td><td> $I_{LPM}$ , mA</td></tr><tr><td>3</td><td>18.8</td><td>17.4</td><td>0.926</td><td>0.00022</td></tr></table>

The essence of the push mode allows the smart objects to be put to a full sleep between the sessions. However, for practical reasons (i.e., the need to maintain the state of the energy measurements between the sessions), only the radio part of the smart object was switched off, while the clocks on the microcontroller were kept on, and the CPU state was managed by the Contiki OS. Therefore, in order to emulate the push mode, only the time of using radio $\left( \begin{array} { l l } { t _ { R X } , } & { t _ { T X } } \end{array} \right)$ was measured directly in the experiments, and it was found invariant for different values of t. The value of $t _ { C P U }$ was found by <sup>fi</sup>rst measuring the CPU usage time for different values of t and then using simple linear regression to identify the value corresponding to the communication session alone. Finally, the time in the low power mode was approximated as:

$$
t _ {L P M} = t - t _ {C P U}.\tag{A.2}
$$

The results of the measurements with 10 s interval are shown in $\mathrm { F i g . A . 1 }$ for different modes of mote operation. As can be seen, the energy footprint of CoAP in the reception mode is approximately six times smaller, as compared with HTTP.

The power consumption in the push communication mode for different values of the interval is shown in Table A.3. For the interval values up to $^ { 1 2 0 s , }$ the power estimates are derived from the measurements, whereas for the longer intervals, the power values are estimated by assuming constant time of using radio (t , $t _ { T X } )$ and CPU (t ) per communication session. As can be seen from the table, CoAP consumes signi<sup>fi</sup>cantly less power than HTTP also for the intervals longer than 120 s. For example, even for the hourly intervals, the COAP consumption is only 40% of the HTTP consumption. Only for very long intervals, e.g., daily communications, the difference between CoAP and HTTP becomes insigni<sup>fi</sup>cant.

Table A.3  
The power consumption P (mW) in push mode.

<table><tr><td>Time t, sec</td><td>10</td><td>30</td><td>120</td><td>600</td><td>3600</td><td>86,400</td></tr><tr><td>P(HTTP), mW</td><td>0.664</td><td>0.222</td><td>0.056</td><td>0.0117</td><td>0.0025</td><td>0.0007</td></tr><tr><td>P(CoAP), mW</td><td>0.115</td><td>0.039</td><td>0.010</td><td>0.0026</td><td>0.0010</td><td>0.0007</td></tr></table>

## A.3. Pull mode vs. push mode

Table A.4 compares the measurement results for the push mode against the results for the pull mode, as reported by Colitti et al. [8], by translating the power consumption estimates into the estimates of the battery replacement time. As can be seen, CoAP provides clear bene<sup>fi</sup>ts in terms of the battery replacement time as compared with HTTP. The difference diminishes along with the inter-communication interval due to the fact that, as the inter-communication intervals get longer, the greatest portion of energy is spent in the low power mode, in which the energy consumption does not depend on the application layer protocol. It is worth noting that the difference diminishes at a signi<sup>fi</sup>cantly slower rate in the push mode, due to the possibility to disable radio duty cycling and to put the smart object in the sleep mode during a greater portion of time than in the pull mode.

![](/api/attachments/CKP4QC2P/fulltext/images/38a929af7c381c0e993e5f55162f925a178a94a8c374c54cee6b59988f798d59.jpg)  
Fig. A.1. Energy consumption of the motes using push communication mode with 10 s inter-arrival time over HTTP vs. CoAP in different mote operation modes: reception (RX), transmission (TX), CPU processing (CPU), and low power mode (LPM).

Battery replacement time $t _ { b a t } ,$ days (assuming the use of a pair of AA zinc–carbon batteries).

<table><tr><td></td><td>Interval t, s</td><td>10</td><td>30</td><td>120</td><td>3600</td><td>86,400</td></tr><tr><td rowspan="2">Pull</td><td> $t_{bat}$  (HTTP), days</td><td>80</td><td>117</td><td>148</td><td>156</td><td>156</td></tr><tr><td> $t_{bat}$  (CoAP), days</td><td>148</td><td>158</td><td>156</td><td>156</td><td>156</td></tr><tr><td rowspan="2">Push</td><td> $t_{bat}$  (HTTP), days</td><td>170</td><td>508</td><td>2013</td><td>44,978</td><td>152,704</td></tr><tr><td> $t_{bat}$  (CoAP), days</td><td>976</td><td>2893</td><td>11,013</td><td>114,971</td><td>167,095</td></tr></table>

Note that with infrequent communications in push mode, the estimated battery replacement time is measured in decades and thus greatly exceeds the typical battery lifetime, which, due to self-discharging, is unlikely to be more than seven years. Therefore, in practice, the estimated battery replacement time shall be capped using the battery selfdischarging time as the upper limit.

The above observations could be summarized as follows:

• For pull mode of communication, HTTP consumes up to two times more energy than CoAP.

• For push mode of communication, HTTP consumes up to six times more energy than CoAP.

The difference in the energy footprint depends on the intervals between communications, as well as on the ef<sup>fi</sup>ciency of the LPM implementation in the smart object (for longer intervals between communications). The energy footprint is also likely to increase nonlinearly with the payload size. However, since a typical payload in machine type communication is relatively small, it is assumed to <sup>fi</sup>t into a single packet, and this dependency can be excluded from the analysis for the sake of simplicity.

Further reduction of RX footprint of CoAP is possible by using noncon<sup>fi</sup>rmable CoAP messages. Moreover, using UDP instead of TCP as a transport layer protocol can reduce the energy footprint of HTTP as found by Kuladinithi et al. [25]. However, HTTP over UDP is not supported by standard Web application platforms. Furthermore, HTTP over UDP does not provide the same packet delivery guarantees as HTTP over TCP and CoAP over UDP do. Therefore, it is excluded from consideration in this paper.

## Appendix B. Parameter values of the baseline scenario

Table B.1 provides the values of the non-monetary parameters and Table B.2 the monetary cost values used in the baseline scenario introduced in Section 5.1. Abbreviations S, A, W, P, and O refer to smart object, access point, web server, proxy, and other costs, respectively.

Table B.2  
Table B.1  
The values of the non-monetary parameters used in the TCO calculation.

<table><tr><td>Parameter</td><td>Symbol</td><td>CoAP</td><td>HTTP</td><td>Justification</td></tr><tr><td>S: energy stored in a battery</td><td> $E = Q * U$ </td><td>2700 mWs</td><td></td><td>Assuming 2 × AA batteries (900 mAh/1.5 V), similar to [7].</td></tr><tr><td rowspan="2">S: power consumption</td><td rowspan="2"> $P_S$ </td><td rowspan="2">0.02 mW</td><td rowspan="2">0.11 mW</td><td>Based on own measurements, as described in Appendix A.</td></tr><tr><td>Contemporary batteries based on lithium iron disulfide can operate in temperatures from -40 °C to +60 °C and support the self-discharge time of 10-15 years and abovea. To accommodate the effect of varying environmental conditions, a shorter self-discharge time of 7 years is assumed.</td></tr><tr><td>S: battery self-discharge time</td><td> $t_{b,sd}$ </td><td>7 years</td><td></td><td rowspan="2">Industrial grade smart objects, such as the ones used in outdoor lighting controls, have the expected lifetime of 10-15 years and the mean time between failures (MTBF) of 10-23 yearsb. Based on this, for simplicity, the average smart object replacement time is assumed to be 10 years.</td></tr><tr><td>S: lifetime of a smart object</td><td> $t_{S,hw}$ </td><td>10 years</td><td></td></tr><tr><td>S: average time interval for software updates</td><td> $t_{S,sw}$ </td><td>1 year</td><td></td><td>It is assumed, without a loss of generality, that the smart object software is updated periodically throughout the lifetime of the application, with the interval of one year between the updates.</td></tr><tr><td>A: maximum number of smart objects supported by an access point</td><td> $n_{AP}$ </td><td>200</td><td>100</td><td>As discussed in Section 4.4.2, an access point can support a greater number of CoAP-based smart objects than HTTP-based ones. This is due to the smaller number of packets and smaller size of the messages in CoAP-based transactions that impede less the 802.15.4 network bandwidth. The estimates are based on the interviews with domain experts.</td></tr><tr><td>A: monthly volume of the data transferred</td><td> $v$ </td><td>317 MB</td><td>2221 MB</td><td>Based on [7], the volume of data transferred in each CoAP transaction with a small payload below 80 bytes is assumed to be 154 bytes. Furthermore, according to the CoAP-HTTP comparison in [11], HTTP-based transactions, depending on the payload and implementation, require up to 10 times more data to be transferred. To be on the conservative side, the 7-fold HTTP-to-CoAP difference in volume is assumed.</td></tr><tr><td>A: lifetime of an access point</td><td> $t_{A,hw}$ </td><td>10 years</td><td></td><td>Based on the expected lifetime and MTBF of industrial grade access points for outdoor lighting applicationsb that are estimated to be in the range of 10-15 and 7-20 years, respectively, the average access point replacement time has been assumed to be 10 years.</td></tr><tr><td>A: average time interval for software updates</td><td> $t_{A,sw}$ </td><td>1 year</td><td></td><td>Similar to the smart object software updates, the one-year interval between periodical software updates is assumed.</td></tr><tr><td>A: power consumption</td><td> $P_A$ </td><td>6.21 W</td><td></td><td>The Libelium&#x27;s Meshlium router - a ZigBee-3G access point - reportedly consumes the power in the range between 4.86 W and 8.1 Wc. The average value of 6.21 W is taken as the reference value.</td></tr><tr><td>W: average time interval for software updates</td><td> $t_{W,sw}$ </td><td>1 year</td><td></td><td>Similar to the smart object software updates, the one-year interval between periodical software updates is assumed.</td></tr><tr><td>W: number of web servers</td><td> $l$ </td><td>4</td><td></td><td>It is assumed that the web-server site will be comprised of a load balancing front-end, two application servers and a database server.</td></tr></table>

<sup>a</sup> http://data.energizer.com/PDFs/lithiuml91l92\_appman.pdf, http://www.farnell.com/datasheets/9583.pdf.  
<sup>b</sup> Energy Solutions (2011). NEEA Study: Technology and Market Assessment of Networked Outdoor Lighting Controls, Northwest Energy Ef<sup>fi</sup>ciency Alliance, 2011, available at https:// conduitnw.org/\_layouts/Conduit/FileHandler.ashx?RID=389.  
<sup>c</sup> http://www.libelium.com/uploads/2013/02/meshlium-datasheet\_eng.pdf.

The monetary cost values in euros (€) used in the TCO calculation.

<table><tr><td>Parameter</td><td>Symbol</td><td>CoAP</td><td>HTTP</td><td>Justification</td></tr><tr><td>S: hardware price</td><td> $S_{HW}$ </td><td>50</td><td>55</td><td>It is assumed that the smart object is based on a system-on-chip (SoC, such as TI CC2530a). CoAP can use Class 1 SoC, whereas more resource-consuming HTTP requires Class 2 SoC [3]. The cost of the SoC, along with the other elements of the smart object (sensors, controllers, smart card antennas, etc.), totals €50 for the Class 1 SoC and €55 for the Class 2 SoC according to the domain experts.</td></tr><tr><td>S: software cost</td><td> $S_{SW}$ </td><td>40,000</td><td></td><td>On the one hand, CoAP specifications are simpler, making its implementation more compact and hence making it simpler to fit the software in the constrained memory of the smart object. On the other hand, the use of CoAP demands from the developers the knowledge of the protocol and the libraries implementing it. Thus, when using CoAP instead of HTTP, the software development efforts first increase due to the need to learn the protocol, but later decrease due to more compact implementation. As a result, according to the domain experts, the overall smart object software development time is similar for CoAP and HTTP.</td></tr><tr><td>S: battery price</td><td> $p_b$ </td><td>3.6</td><td></td><td>The price of a pair of lithium iron disulfide batteries is used as a referenceb.</td></tr><tr><td>S: cost of site visit</td><td> $C_{site-visit}$ </td><td>129</td><td></td><td>It is assumed that, within a day, a field service engineer with a yearly salary of €44,000 is able to visit, on average, two neighboring sites situated at an average distance of 100 km from the headquarters.</td></tr><tr><td>S: SW update development cost</td><td> $S_{M,sw-update}$ </td><td>5000</td><td></td><td>It is assumed that the yearly software updates require two person-weeks of efforts that can be ordered from a subcontractor specializing in software development and charging €10,000 for person-month equivalent of work.</td></tr><tr><td>S: SW update installation cost</td><td> $S_{M,sw-install}$ </td><td>0</td><td></td><td>It is assumed that the software update delivery takes place over-the-air, and requires a small size of update packet to be sent. Given the assumed flat rate for the access point connectivity (see below), the software update installation is assumed not to generate any additional costs.</td></tr><tr><td>A: acquisition cost</td><td> $A_{HW+SW}$ </td><td>500</td><td></td><td>The prices for an IEEE 802.15.4 router with cellular connectivity vary from $146 for the Rexense ZigBee/GPRS Wireless Gatewayc to €800 and above for Libelium&#x27;s Meshlium ZigBee/3G access pointsd. Based on these, a middle value of €500 is taken as a reference value.</td></tr><tr><td>A: installation costs per access point (includes also smart object installation costs)</td><td> $A_{HW,install}$ </td><td>258</td><td></td><td>Assuming that, within a day, a field service engineer with a yearly salary of €44,000 is able to visit a site situated (on average) at a distance of 100 km from the headquarter and install the access points and smart objects belonging to the site.</td></tr><tr><td>A: connectivity setup</td><td> $A_{CS}$ </td><td>5</td><td></td><td>Telecom operators typically charge a setup fee for opening an M2M subscription; for instance, TeliaSonera charges €1.24 and €8.02 when opening the Control and Control Plus subscriptions, respectivelye. Based on these, the value of €5 is taken as the reference value.</td></tr></table>

Please cite this article as: T. Levä, et al., Comparing the cost-ef<sup>fi</sup>ciency of CoAP and HTTP in Web of Things applications, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.009

Table B.2 (continued)

<table><tr><td>Parameter</td><td>Symbol</td><td>CoAP</td><td>HTTP</td><td>Justification</td></tr><tr><td>A: monthly connectivity fee</td><td> $A_{CMF,flat}$ </td><td>15</td><td></td><td>Some telecom operators in the regions considered in the paper (e.g., TeliaSonera, Elisa) offer the flat rate 3G subscriptions with unlimited traffic charging €10 to €20 per month $^{f}$ . The middle value of €15 is used as the reference value.</td></tr><tr><td>A: unit price of electricity [€/kWh]</td><td>u</td><td>0.0492</td><td></td><td>SPOT price of Nordpool on 20.2.2013 $^{g}$ .</td></tr><tr><td>A: monthly rent for premises</td><td> $A_{Su,Pr}$ </td><td>3.15</td><td></td><td>Being relatively light, the AP is assumed to be deployed on a light pole whose yearly lease is estimated to cost circa $50 $^{h}$ . This translates into a monthly fee of €3.15 used as a reference value in the calculations.</td></tr><tr><td>W: protocol stack development</td><td> $W_{SW,stack}$ </td><td>20,000</td><td>0</td><td>It is assumed that open-source CoAP software (such as Californium $^{i}$ ) cannot be used, and thus own components need to be implemented and integrated with the application logic and database layers in the back-end. It is assumed that component implementation and integration require two person-months of efforts-based on the interviews with domain experts. It is also assumed that HTTP server software is available at no additional cost, e.g., as a part of a commercial web application platform.</td></tr><tr><td>W: application development</td><td> $W_{SW,app}$ </td><td>120,000</td><td></td><td>It is assumed that 12 person-month of efforts, with a charge of €10,000 per month, will be sufficient for developing the web application.</td></tr><tr><td>W: SW update development cost</td><td> $W_{M,sw-update}$ </td><td>6000</td><td>5000</td><td>It is assumed that the yearly software updates of the web server require two person-weeks of efforts that can be ordered from a subcontractor specializing in software development and charging €10,000 for person-month equivalent of work. For CoAP, slightly higher charges are assumed, to account for the lower installed base of CoAP and hence for the scarcity of the experts knowledgeable in this protocol.</td></tr><tr><td>W: rented server</td><td> $W_{hosting}$ </td><td>60</td><td>140</td><td>For simplicity, the pricing of virtual web servers offered by Sigmatic $^{j}$ is used as a reference. The type of the servers and their prices depend on the expected monthly volume of traffic: in case of HTTP, Extreme V4 servers allowing up to 300GB of data transfer need to be rented for €140/month, whereas the use of CoAP reduces the traffic volume dramatically, thus allowing the rent of Basic V4 servers for €60/month.</td></tr><tr><td>P: software cost</td><td> $P_{SW}$ </td><td>5000</td><td></td><td>It is assumed that two person weeks of efforts are needed for implementing protocol translation proxy for existing proxy platform-based on the interviews with domain experts. Note that the proxy component is present only in deployment scenario 3 where CoAP is used by the smart object, but the web-server supports only HTTP. In the cases of end-to-end CoAP or end-to-end HTTP, this cost is absent.</td></tr><tr><td>O: acquisition</td><td> $O_{Ac}$ </td><td>20,000</td><td></td><td>It is assumed that an external consultant working for two months with a charge of €10,000 per month is hired to design and compare alternative technical solutions prior to acquiring, implementing, and integrating the necessary components.</td></tr><tr><td>O: operation, monthly</td><td> $O_{Op}$ </td><td>5000</td><td></td><td>It is assumed that administrating the WoT application, providing support, and other supporting tasks are outsourced to a subcontractor who monthly devotes half a person-month efforts to these tasks and charges €10,000 for person-month equivalent of work.</td></tr></table>

<sup>a</sup> http://www.ti.com/product/cc2530.  
<sup>b</sup> http://cpc.farnell.com/energizer/633471/battery-ultimate-lithium-aa-10pk/dp/BT04600.  
<sup>c</sup> http://rexense.en.alibaba.com/product/501823273-212955212/ZigBee\_GPRS\_Wireless\_Gateway.html  
<sup>d</sup> The price list can be requested from Libelium by <sup>fi</sup>lling a form at http://www.libelium.com/contact/#buy.  
<sup>e</sup> http://www.sonera.<sup>fi</sup>/yrityksille/asiakastuki/laskutus%20ja%20asiakkuuden%20hallinta/hinnasto?pricelist=413.  
<sup>f</sup> TeliaSonera's prices can be found at http://www.sonera.<sup>fi</sup>/yrityksille/asiakastuki/laskutus%20ja%20asiakkuuden%20hallinta/hinnasto?pricelist=413 and http://www.sonera.<sup>fi</sup>/ nettiyhteydet/liikkeelle/mika+yhteys+minulle; Elisa's prices are available at http://oma.elisa.<sup>fi</sup>/yrityksille/verkkokauppa/#!/internet and http://saunalahti.<sup>fi</sup>/mobiililaajakaista/. Note that the prices differ depending on whether the target segment is businesses or consumers. Note also that some of the rates have restrictions on the monthly volume of traf<sup>fi</sup>c to be transferred. <sup>g</sup> http://www.sahkonhinta.<sup>fi</sup>/summariesandgraphs.  
<sup>h</sup> Sean Heath (2006), Smart lightpoles: The next logical step in the evolution of cell sites, Right of Way, May/June 2006, available at https://www.irwaonline.org/eweb/upload/ ROW%20Archives%207-05%20thru%207-06/506/SmartLightpoles.pdf.  
http://people.inf.ethz.ch/mkovatsc/californium.php

<sup>j</sup> http://www.sigmatic.<sup>fi</sup>.

## References

[1] B. Anderson, C. Gale, M. Jones, A. McWilliam, Domesticating broadband — what consumers really do with <sup>fl</sup>at-rate, always-on and fast internet access, BT Technology Journal 20 (1) (2002) 103–114.

[2] M. Becker, K. Li, K. Kuladinithi, T. Pötsch, Transport of CoAP over SMS, USSD and GPRS (draft-becker-core-coap-sms-gprs-04), work in progress, Available at: http://datatracker.ietf.org/doc/draft-becker-core-coap-sms-gprs (retrieved October 1, 2013).

[3] C. Bormann, A.P. Castellani, Z. Shelby, CoAP: an application protocol for billions of tiny internet nodes, IEEE Internet Computing 16 (2) (2012) 62–67.

[4] Capgemini, The price is right: pricing strategies for mobile broadband services, Available at: http://www.<sup>fi</sup>.capgemini.com/the-price-is-right-pricing-strategies for-mobile-broadband-services2012 (retrieved May 22, 2013).

[5] L.P. Carr, C.D. Ittner, Measuring the cost of ownership, Journal of Cost Management 6 (3) (1992) 42–51.

[6] A. Castellani, A. Rahman, T. Fossati, E. Dijk, Best practices for HTTP-CoAP mapping implementation (draft-castellani-core-http-mapping-07), work in progress, Available at: https://datatracker.ietf.org/doc/draft-castellani-core-http-mapping (retrieved May 22, 2013).

[7] W. Colitti, K. Steenhaut, N. De Caro, B. Buta, V. Dobrota, Evaluation of constrained application protocol for wireless sensor networks, Proc. of 18th IEEE Workshop on Local & Metropolitan Area Networks (LANMAN), 2011, pp. 1–6.

[8] W. Colitti, K. Steenhaut, N. De Caro, Integrating wireless sensor networks with the web Proc of Extending the Internet to Low power and Lossy Networks (IP + SN 2011), 2011.

[9] J. David, D. Schuff, R. St. Louis, Managing your total IT cost of ownership, Communications of the ACM 45 (1) (2002) 101–106.

[10] Z. Degraeve, F. Roodhooft, Improving the ef<sup>fi</sup>ciency of the purchasing process using total cost of ownership information: the case of heating electrodes at Cockerill Sambre S.A. European Journal of Operations Research 112 (1) (1999) 42–53.

[11] A. Dunkels, F. Osterlind, N. Tsiftes, Z. He, Software-based on-line energy estimation for sensor nodes, Workshop on Embedded Networked Sensors (EmNets '07), ACM. New York, NY. USA. 2007. 28–32.

[12] L. Ellram, A framework for total cost of ownership, International Journal of Logistics Management 4 (2) (1993) 49–60

[13] L. Ellram, Total cost of ownership: an analysis approach for purchasing, International Journal of Physical Distribution and Logistics Management 25 (8) (1995) 4–23.

[14] B. Ferrin, R. Plank, Total cost of ownership models: an exploratory study, Journal of Supply Chain Management 38 (3) (2006) 18–29.

[15] R.T. Fielding, R.N. Taylor, Principled design of the modern web architecture, ACM Transactions on Internet Technology 2 (2) (2002) 115–150.

[16] E. Fleisch, What is the Internet of Things? An Economic Perspective, Auto-ID Labs White Paper, WP-BIZAPP-053, Available at: http://www.autoidlabs. org/publications, 2010 (retrieved May 22, 2013).

[17] D. Guinard, V. Trifa, Towards the web of things: web mashups for embedded devices International World Wide Web Conferences Madrid. Spain. 2009

[18] D. Guinard, V. Trifa, F. Mattern, E. Wilde, From the internet of things to the web of things: resource-oriented architecture and best practices, in: D. Uckelmann, M. Harrison, F. Michahelles (Eds.), Architecting the Internet of Things, Springer, 2011, pp. 97–129.

[19] B. Hall, B. Khan, Adoption of new technology, in: D.C. Jones (Ed.), New Economy Handbook, Academic Press, 2003, pp. 229–249.

[20] K. Hartke, Observing resources in CoAP, draft-ietf-core-observe-10, work in progress, Available at: http://datatracker.ietf.org/doc/draft-ietf-core-observe (retrieved October 1, 2013).

[21] J. Hui, P. Thubert, Compression Format for IPv6 Datagrams over IEEE 802.15.4-Based Networks, RFC 6282 (Proposed Standard). 2011.

[22] K. Hurkens, W. van der Valk, F. Wynstra, Total cost of ownership in the services sector: a case study, Journal of Supply Chain Management 42 (1) (2006) 27–37.

T. Levä et al. / Decision Support Systems xxx (2013) xxx–xxx

[23] D. Katsianis, I. Welling, M. Ylönen, D. Varoutas, T. Sphicopoulos, N.K. Elnegaard, B.T. Olsen, L. Burdry, The <sup>fi</sup>nancial perspective of the mobile networks in Europe, IEEE Personal Communications 8 (6) (2001) 58–64.

[24] C. Gomez, J. Paradells, Wireless home automation networks: a survey of architectures and technologies, IEEE Communications Magazine 48 (6) (2010) 92–101.

[25] K. Kuladinithi, O. Bergmann, T. Pötsch, M. Becker, C. Görg, Implementation of CoAP and its application in transport logistics, Proc. of Extending the Internet to Low power and Lossy, Networks (IP + SN 2011), 2011.

[26] Z. Shelby, Embedded web services, IEEE Wireless Communications 17 (6) (2010) 52–57.

[27] Z. Shelby, K. Hartke, C. Bormann, B. Frank, Constrained Application Protocol (CoAP), draft-ietf-core-coap-18, work in progress, Available at: https://datatracker.ietf.org doc/draft-ietf-core-coap (retrieved October 1, 2013).

[28] J. Sigurdson, WAP OFF — origin, failure, and future, Prepared for the Japanese– European Technology Studies, 2001. Available at: www2.hhs.se/eijswp/135.PDF, (retrieved October 1, 2013).

[29] T. Smura, A. Kiiski, H. Hämmäinen, Virtual operators in the mobile industry: a techno-economic analysis, NETNOMICS 8 (1–2) (2008) 25–48.

[30] M. Treacy, F. Wiersema, The Discipline of Market Leaders: Choose Your Customers, Narrow Your Focus, Dominate Your Market, Perseus, New York, 1997.

[31] M.L. Tushman, J.P. Murmann, Dominant designs, technology cycles, and organizational outcomes, in: R. Garud, A. Kumaraswamy, R.N. Langlois (Eds.), Managing in the Modular Age: Architectures, Networks, and Organizations, Blackwell Publishers, Oxford, 2003, pp. 231–266.

[32] P. Tyrväinen, J. Warsta, V. Seppänen, Evolution of secondary software businesses: understanding industry dynamics, in: G. Leon, A. Bernardos, J. Casar, K. Kautz, J. DeGross (Eds.), Open IT-based Innovation: Moving Towards Cooperative IT Transfer and Knowledge Diffusion, Springer, Boston, 2008, pp. 381–401.

[33] B.C. Villaverde, D. Pesch, R. de Paz Alberola, S. Fedor, M. Boubekeur, Constrained application protocol for low power embedded networks: a survey, Proc. of Innovative Mobile and Internet Services in Ubiquitous Computing (IMIS), 2012, pp. 702–707.

[34] E. Walker, The real cost of a CPU hour, Computer 42 (4) (2009) 35–41.

[35] E. Walker, W. Brisken, J. Romney, To lease or not to lease from storage clouds, Computer 43 (4) (2010) 44–50.

[36] H. Warma, T. Levä, L. Eggert, H. Hämmäinen, J. Manner, Mobile Internet in Stereo: an End-to-End Scenario, Incentives, Overlays and Economic Traf<sup>fi</sup>c Control, Springer, Berlin.2010.64-75

[37] D. Zeng, S. Guo, Z. Cheng, The web of things: a survey, Journal of Communication 6 (6)(2011) 424–438

![](/api/attachments/CKP4QC2P/fulltext/images/0e4e32b7d3420fc3118350169a4cc8810061121d6acfb05d1b5a010875882ab5.jpg)

![](/api/attachments/CKP4QC2P/fulltext/images/a76b9b2e3a8901a9a1f24a6efcf7d923622f962946e011eed7664edf7be541c4.jpg)

![](/api/attachments/CKP4QC2P/fulltext/images/49f676cc004901e0915ea05d331e1a0778710c1d00d468dfe755f3da2010fe00.jpg)

Tapio Levä received his M.Sc. in Communications Engineering from Helsinki University of Technology (TKK), Finland, in 2009 with major in Networking Technology and minors in Telecom munications Management and Interactive Digital Media. He is currently doing postgraduate studies in the Department of Communications and Networking at Aalto University. His research interests include techno-economics of Internet architecture evo lution, Internet standards adoption and information-centric networking.

Oleksiy Mazhelis is a post-doc researcher at the Department of Computer Science and Information Systems, University of Jyväskylä, Finland. He received a degree of MSc (Specialist) from Kharkov National University of Radio-Electronics Ukraine in 1997, and received his licentiate and doctoral degrees from the University of Jyväskylä in 2004 and 2007, respectively, on the subject of masquerader detection in mobile phone environment. Starting from 2004. he was working in various research projects conducted in collaboration with industrial partners. His current research interests encompass techno-economics, systems analysis, machine learning, and pattern recognition, applied to the domains of software industry evolution, internet-of-things, telecommunications and cloud software, as well as intelligent transportation systems.

Henna Suomi received her M.Sc. in Communications Engineering from Helsinki University of Technology (TKK), Finland, in 2009 with major in Telecommunications Management and minor in Networking Technology. After working as a visiting researcher at McGill University she started doing her doctoral studies in the Department of Communications and Networking at Aalto University Her current research interests include techno-economics of Internet architecture evolution, adoption of multipath protocols and economic effects of multihoming
