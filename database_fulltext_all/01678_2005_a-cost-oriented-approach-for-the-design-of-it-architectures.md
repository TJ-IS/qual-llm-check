---
otero_id: 1678
otero_key: "EFYC5ZKB"
title: "A Cost-Oriented Approach for the Design of IT Architectures"
authors: "Danilo Ardagna; Chiara Francalanci"
year: "2005"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000032"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A cost-oriented approach for the design of IT architectures

Danilo Ardagna, Chiara Francalanci

Dipartimento di Elettronica e Informazione, Politecnico di Milano, Milano, Italy

Correspondence:

C Francalanci, Dipartimento di Elettronica e Informazione, Politecnico di Milano, Piazza Leonardo Da Vinci, 32, 20133, Milano, Italy.

Tel: þ 39 2 23993457

Fax: þ 39 2 23993411

E-mail: francala@elet.polimi.it, ardagna@elet.polimi.it

## Abstract

Multiple combinations of hardware and network components can be selected to design an information technology (IT) infrastructure that satisfies organizational requirements. The professional criterion to deal with these degrees of freedom is cost minimization. However, a scientific approach has been rarely applied to cost minimization and a rigorous verification of professional design guidelines is still lacking. The methodological contribution of this paper is the representation of complex infrastructural design issues as a single cost-minimization problem. The approach to cost-minimization is empirically verified with a database of costs that has also been built as part of this research. The paper shows how an overall cost-minimization approach can provide significant cost reductions and indicates that infrastructural design rules previously identified by the professional literature can lead to sub-optimal solutions.

Journal of Information Technology (2005) 20, 32–51. doi:10.1057/palgrave.jit.2000032 Keywords: IT Costs; Distributed systems; Distributed networks

## Introduction

he information technology (IT) infrastructure is comprised of the hardware and network components of a computer system (Menasce´ and Almeida, 2000). Since hardware and network components cooperatively interact with each other, the design of the IT infrastructure is a systemic problem. The systemic objective of infrastructural design is the minimization of the costs required to satisfy the computing and communication requirements of a given group of users (Jain, 1987). In most cases, multiple combinations of infrastructural components can satisfy requirements and, accordingly, each combination satisfies requirements with infrastructural components of different individual capacity (Menasce´ and Almeida, 2000). These degrees of freedom generate two infrastructural design steps: the selection of a combination of hardware and network components and their individual sizing. Cost analyses are executed at both steps (Lazowska et al., 1984; Menasce´ and Almeida, 2000).

This paper proposes an approach to support the selection of a combination of hardware and network components that minimizes overall infrastructural costs. Cost analyses have been primarily addressed by the professional literature, which evaluates selected infrastructural choices to provide cost benchmarks and practical design rules (Redman et al., 1998; Vijayan, 2001). In contrast, a scientific approach has been rarely applied to cost analyses and a rigorous methodological support to the cost side of the infrastructural design process is still lacking. A likely reason for this lack of attention is the empirical nature of costs (Willcocks, 1992, Alter et al., 2000). Each infrastructural component is characterized by a specific cost function which, furthermore, is subject to substantial change over a short period of time. This makes the scientific verification of methodological approaches to cost minimization particularly cumbersome, as it requires empirical data.

A methodological contribution of this paper is the representation of complex infrastructural design issues as a single cost-minimization problem. The approach is empirically verified with a database of costs that has also been built as part of this research. Multiple sources of cost data have been combined, including previous professional literature, vendors’ documentation and ad hoc surveys with companies to enable the statistical estimate of specific cost functions. With respect to the past, this methodological contribution is enabled by a greater standardization and corresponding interoperability of infrastructural components. On one hand, standardization has increased the number of compatible design alternatives and, as a consequence, has made an overall optimization effort meaningful and potentially advantageous. On the other hand, it has decreased the data collection effort, by reducing the variance of costs across hardware and network components. The paper shows how an overall costminimization approach can provide significant savings and indicates how corresponding infrastructural solutions can substantially differ from those obtained by applying professional design rules.

The next section reviews the literature and highlights the main organizational and technical variables of interest. The subsequent section presents the phases of our design approach and the corresponding design models. The section thereafter discusses the experimental results of cost analyses for different infrastructural design choices. Conclusions are drawn in the last section.

## Research background and motivation

Infrastructural costs represent about 20% of the overall cost of a computer system (Alter et al., 2000). To minimize these cost figures, the professional literature focuses on the selection of a combination of infrastructural components, while the cost-minimizing design of individual components is considered less consequential (Zachman, 1999). A generally accepted rule of thumb is that over-sizing a component has a minor cost impact and, in fact, is recommended whenever performance requirements are subject to uncertainty or variability (Alter et al., 2000).

At a system level, two design alternatives are studied, related to the selection of hardware and network components, respectively (see Table 1). The first alternative is how to distribute the overall computing load of a system onto multiple machines (Gavish and Pirkul, 1986; Jain, 1987; Aue and Breu, 1994). The second is where to locate machines that need to exchange information in order to minimize network costs (Ingham et al., 2000). Design decisions on both alternatives are strongly inter-related. Intuitively, different allocations of computing load can change the communication patterns among machines and modify the economics of corresponding network structures. Costs have been consistently found to be highly dependent on overall decisions on these two alternatives, both historically and currently.

The historical design principle was centralization, which was advocated to take advantage of hardware scale economies according to Grosch’s law (Ein-Dor, 1985). In the late 1970s, Grosch’s law was controverted by Parkinson’s law (Parkinson, 1955), introducing a critical capacity level above which scale economies are not verified and centralization becomes cost inefficient. As a consequence of Parkinson’s findings, neither centralization nor decentralization could be considered a general design principle to obtain cost minimization. However, a further attempt to formulate a general design principle has been made in the mid-1980s, when Grosch’s law has been revised as ‘It is most cost effective to accomplish any task on the least powerful type of computer capable of performing it’ (Ein-Dor, 1985). Decentralization and its operating rule, referred to as downsizing, became the methodological imperative for cost-oriented infrastructural design. The corresponding infrastructural design guideline, which has been effectively summarized as ‘think big, but build small’, is still considered valid (Scheier, 2001). Although academic studies have challenged the generality of the decentralization principle (Gavish and Pirkul, 1986; Jain, 1987), the empirical recognition of the cost disadvantages of decentralization has only occurred in the 1990s with the observation of client–server costs. From an infrastructural perspective, client–server can be seen as an application paradigm that allows personal computers (PCs) to share computing load with mainframes. This sharing has reduced mainframes’ computing load and has facilitated their replacement with cheaper mini-computers, in compliance with the downsizing principle. But the expected reductions of infrastructural costs have not been verified. It has been observed that while decentralization reduces acquisition and, thus, investment costs, it increases management costs, due to a more cumbersome administration of a greater number of infrastructural components. The concept of ‘Total Cost of Ownership’ (TCO) has therefore been introduced and defined as the summation of investments and management costs, including acquisition, installation, maintenance and retirement costs of any infrastructural component (Redman et al., 1998; Vijayan, 2001). Hence, decentralization may result in an increase, as opposed to a reduction of TCO, depending on the overall trade-off between the investment and management costs of all components.

Recentralization has been thereafter considered to reduce management costs since the management of a centralized infrastructure is simplified and personnel can be further reduced by exploiting scale economies (Nortel Networks, 2001). The rationale for recentralization is that the client– server paradigm can be extended to allow multiple machines to share computing load (Ingham et al., 2000). Applications can be splitted into multiple modules, called tiers, each of which can be allocated on a different machine (Ingham et al., 2000; Menasce´ and Almeida, 2000). Multitier applications give rise to multi-tier infrastructures that offer greater flexibility to implement the most convenient load sharing among multiple machines.

Thin clients are currently proposed as a less expensive alternative to personal computers that can be exploited through a recentralization initiative (Molta, 1999a). Thin clients have lower computing capacity than PCs, which is sufficient for the execution or the emulation of the presentation tier, but require the recentralization of the application logic on a server. It has been empirically verified that thin clients have management costs 20–35% lower than PCs (Molta, 1999b). Furthermore, the Independent Computing Architecture (ICA) and Remote Desktop Protocol (RDP) standards allow remote access to the application logic by traditional PCs as well as new hand-held devices. This translates into hybrid configurations of PCs that execute only a subset of client applications, called hybrid fat clients. It is reported that the remote execution of applications can significantly reduce TCO even if PCs are adopted and can represent an interesting infrastructural solution when one or multiple applications require a PC and prevent the use of thin clients (Molta, 1999b). In these cases, the management cost of each application that is executed remotely is reduced by 20–35% (Molta, 1999b).

Table 1 Infrastructural design alternatives that generate cost trade-offs and research hypotheses

<table><tr><td>Design alternative</td><td>Sub-alternative</td><td>Description</td><td>Professional guidelines - research hypotheses</td></tr><tr><td rowspan="5">How to distribute the overall computing load of a system onto multiple machines.</td><td>Client typology, thin vs fat vs hybrid fat client (HFC)</td><td>Thin clients manage the user interface of applications stored and executed remotely, while fat clients store and execute applications locally. Hybrid fat clients (HFCs) behave both as fat and thin clients depending on the specific application.</td><td>Thin clients and HFCs should be adopted whenever possible to minimize hardware and management costs.</td></tr><tr><td>Number of tiers</td><td>The client-server paradigm organizes applications in multiple tiers. Each application tier can be allocated on a separate machine and responds to service requests from lower tiers, while sending service requests to higher tiers.</td><td>Server farms should be implemented whenever possible and designed by selecting the smallest server that can support applications, to minimize hardware acquisition costs and favour system scalability.</td></tr><tr><td>Total number of servers</td><td>The required computing capacity can be allocated on one or multiple servers, organized as server farms, whose total number represents an architectural alternative.</td><td>Applications should be allocated with the maximum number of tiers allowed by constraints, to minimize hardware acquisition costs.</td></tr><tr><td>Allocation of applications</td><td>Different applications (or application tiers) can be allocated on separate computers and, vice versa, multiple applications can be allocated on the same computer.</td><td>Applications that can be executed on the same computer should be centralized on a single server/server farm, to minimize management costs.</td></tr><tr><td>Disk sharing</td><td>Servers can share a common set of disk arrays through storage networking technologies.</td><td>SANs should be implemented if the additional hardware acquisition costs that they involve are lower than savings on server management costs.</td></tr><tr><td rowspan="2">Where to locate machines that need to exchange information.</td><td>Location of servers</td><td>Servers can be located in different sites, although all servers within the same server farm must be located in the same site.</td><td>Servers that are not constrained to a specific location should be centralized in the site that minimizes VPN bandwidth requirements, to minimize both network costs and hardware management costs.</td></tr><tr><td>Network topology and standards</td><td>Sites can be connected through different logical and physical communication standards.</td><td>Long-distance connections should be implemented with VPNs or leased lines. Short-distance connections should be implemented with MANs, either owned or outsourced.</td></tr></table>

An application tier can also be simultaneously allocated on multiple coordinated machines, known as server farm (Menasce´ and Almeida, 2000). Each computer within a server farm autonomously responds to a subset of service requests, thus sharing the overall computing load with other computers within the same farm. This load sharing allows greater downsizing and reduces acquisition costs. Furthermore, it has limited negative effects on management costs, since server farms are equipped with software tools that allow the remote management and simultaneous administration of all servers (Scheier, 2001).

Technology also supports recentralization from a data standpoint through storage networking (Nortel Networks, 2001), which, contrary to server farms, is reported to increase hardware costs, but to reduce management costs and enable the design of large-scale centralized systems (Nortel Networks, 2001; Alvarez et al., 2002; Ward et al., 2002). Through storage networking, which includes Storage Area Network (SAN) and Network Attached Storage (NAS) technologies, disks, tapes and optical drives can be shared among multiple servers and accessed through optical networks extending over a metropolitan area. Practitioners forecast that centralization can reduce data management costs by a factor of 5, primarily due to personnel reduction, increasing fault tolerance and a less cumbersome disaster recovery (Nortel Networks, 2001).

Communication expenses are likely to increase as either data or applications are centralized and could favour decentralization to position data sources and applications close to users (Nec, 2002). However, current trends in network technologies represent an enabling factor for a more centralized infrastructural design, through broadband networks, such as Metropolitan Area Networks (MANs) and their connection with SAN and NAS systems. On the other hand, they also favour network scalability, as Internet-based virtual private networks make all-to-all connections straightforward (Yuan and Strayer, 2001). Since, over time, the ratio of communication costs to capacity has experienced continuous reductions, centralization is broadly encouraged in the professional literature also from a network standpoint (Ishizuka et al., 1999).

Table 1 summarizes the infrastructural design alternatives that have been found to generate centralization– decentralization cost trade-offs and related research hypotheses to be empirically verified. Current professional guidelines generally recommend solutions to individual design alternatives that translate into an overall recentralization of hardware components (Molta, 1999b; Scheier, 2001; Betts, 2002; IBM, 2002). However, most research efforts addressing centralization–decentralization issues lack scientific rigour. Only a few academic studies have attempted a more systematic analysis of cost issues in infrastructural design (Gavish and Pirkul, 1986; Jain, 1987). It is interesting to note that previous academic contributions have been initiated by the first wave of professional studies challenging the initial centralization design paradigm and promoting decentralization as a cost-minimizing alternative. In the past, both Gavish and Pirkul (1986) and Jain (1987) have found that infrastructural design raises complex cost trade-offs that are difficult to provide general solutions. Similarly, the goal of this paper is to support cost-oriented infrastructural design with a scientific approach and verify current professional design guidelines suggesting recentralization as a general paradigm for cost minimization. Professional design guidelines will be considered as the research hypotheses of this paper to be empirically verified (Table 1).

## A cost-oriented design approach

From a methodological standpoint, revisiting centralization–decentralization trade-offs requires the representation of design alternatives in Table 1 as a single costminimization problem. This paper’s model draws from Jain (1987) the approach to the representation of infrastructural design alternatives as a single cost-minimization problem (see the section ‘Cost-minimization algorithm’). However, design variables and steps have been significantly extended to account for the complexity of modern computer systems. Furthermore, this paper’s model provides variables with a more complete representation that allows the empirical evaluation of infrastructural costs, as discussed in the remainder of this section.

In this paper, LANs that connect different buildings within the same site are constrained to the extended-star topology and WANs are constrained to be connected through an IP-based Virtual Private Network (VPN) (Yuan and Strayer, 2001). In this way, network design is performed by sizing link capacity and taking into account corresponding costs. This provides a necessary input for the evaluation of overall infrastructural costs and allows preliminary analyses of the impact of network costs on hardware design choices.

The goal of the cost-oriented design is to select a combination of infrastructural components that minimizes costs while satisfying requirements. This involves an initial specification of requirements and a subsequent costminimizing design phase. Figure 1 shows the design steps of this paper’s cost-minimization approach. Each step produces a corresponding model, which is transformed at the subsequent design step. First, organizational requirements are specified by building the technology requirements’ model. Costs are associated with physical infrastructural components, which typically have a discrete distribution over requirements’ dimensions. For example, commercial personal computers have a discrete distribution over computing capacity. Requirements have instead a continuous distribution, just like users’ behaviour (Lazowska et al., 1984; Menasce´ and Almeida, 2000). Therefore, the second design step produces the virtual infrastructural model, which is composed of virtual components that can meet requirements with no approximation. Third, a physical infrastructural model is built by accessing a database of physical (commercial) components and corresponding costs. Then, total costs are calculated on the physical model. Costs constitute the input of an optimization algorithm that iterates steps two and three to identify the minimum-cost infrastructure. Note that the separation between physical and virtual models makes the overall design process more independent of changes in the information technology market, in terms of both components and prices.

The next three sections present the requirements, virtual and physical models and discuss corresponding specification activities. The evaluation of total costs and the optimization algorithm are discussed in the later subsections, respectively.

## The technology requirements mode

Technology requirements are expressed by means of the following fundamental variables:

\- Organization sites $\boldsymbol { S } _ { i } ,$ defined as sets of organizational resources (users, premises and technologies) connected by a LAN.

\- User classes $C _ { i } ,$ defined as a group of n(C ) users using the same subset of applications, with common capacity requirements. User classes are located in an organization site and are characterized by a think-time (high or low).

\- Applications $A _ { i } ,$ defined as a set of functionalities that can be accessed by activating a single computing process. Applications are classified as client and server and are characterized by computing and memory (primary and secondary) requirements.

![](/api/attachments/EFYC5ZKB/fulltext/images/8e3e03faf637330001fb6d577aeff91b15ab833ef8b02ac6bcbb83511233cbef.jpg)  
Figure 1 Design steps of the cost-minimization process.

\- Requests $R _ { i } ,$ defined as interactions among applications aimed at exchanging services according to the client– server paradigm. Requests are characterized by their frequency, the set of supporting server applications, corresponding CPU and disk demanding times and data exchanged for each request. Demanding times (i.e. the overall time required to serve a single request) are supposed to be evaluated on a tuning system (Lazowska et al., 1984). This allows the estimate of demanding time on a different system by means of benchmarking data (Menasce´ and Almeida, 2000). Requests can be initiated from or directed to applications that do not belong to the organization and, in this case, are called external requests, (for example a request directed to a server application of a business partner connected through an Extranet).

\- Databases $D _ { i } ,$ defined as separate sets of data that can be independently stored, accessed and managed. Note that DBMSs are supposed to be specified as server applications and, accordingly, databases are simply described by the size of secondary memory that they require.

A formal specification of technology requirements can be found in Ardagna and Francalanci (2002) and Ardagna et al.

(2003). The specification of sites and user classes is critical to select network components during optimization.

Application tiers abide by the same technical definition as applications and, accordingly, are specified as a set of applications exchanging requests and characterized by the same operating system. Similarly, commercial programs mapping into multiple processes can be specified by means of multiple applications.

Applications and requests are the main drivers of design choices related to client and server computers. All users in a user class are supposed to use the same set of applications with a common think-time. Think-time is a qualitative indicator of the frequency with which users interact with their client computers and is used in subsequent sizing activities (see the following subsection and Microsoft, 2000). Applications are classified as client, server or external. A server application can also play the role of client and convey requests to other server applications. Computing capacity requirements for client applications are expressed in MIPS (Jain, 1987; Francalanci and Piuri, 1999). Irrespective of their allocation on a personal computer or on a server, client applications do not require the specification of secondary memory’s performance requirements, since disks rarely represent a capacity bottleneck (Microsoft, 2000). MIPS and memory requirements depend on the operating system and, in some cases, on the remote protocol and users’ think time (if think time is low, usage of client applications is high and, accordingly, computing and memory requirements are also high). On the contrary, server applications require the evaluation of response time (Lazowska et $a l . ,$ , 1984; Menasce´ and Almeida, 2000) and, accordingly, requests are characterized by CPU and disk demanding times. Demanding times are defined for a reference tuning system (see Appendix A). Note that in the physical model, applications will be assigned to physical machines belonging to the same family of tuning systems, which are machines with the same operating system, processor and disk technology. This allows the prediction of demanding time from benchmarking data.

Requests are initiated by a client or external application and are answered by one or multiple server applications. If multiple server applications are involved, they coordinate by triggering one another in a sequence and build the response incrementally according to the client–server paradigm. The first server application directly triggered by the client or external application is in charge of conveying the response to the requesting application.

Overall our technology requirements is grounded on performance evaluation models (Lazowska et al., 1984; Menasce´ and Almeida, 2000), but introduces a broader set of variables, specifically user classes and sites, in order to evaluate the TCO of the system. The details of the model are reported in Tables A1 and A2 of Appendix A.

## The virtual infrastructural model

The goal of this design step is to build a virtual infrastructure satisfying technology requirements under the assumption that infrastructural components can meet requirements with no approximation. The following virtual components are considered during infrastructural design:

1. Virtual servers (VS<sub>i</sub>) – These servers represent computers that execute at least one server application for one user class. They are described by their primary and secondary memory and by the frequency of requests that they serve. The frequency of requests is used to evaluate the computing capacity of servers during physical design.

2. Virtual thin servers (VTS<sub>i</sub>) and virtual HFC servers (VHFCS<sub>i</sub>) – These servers represent computers that execute at least one client application for one user class assigned to thin or HFC clients. They are described by their computing capacity, primary and secondary memory.

3. Virtual thin clients (VTC<sub>i</sub>) – These represent client computers that execute or emulate only the presentation component of applications. For the sake of simplicity thin clients are not sized, but simply associated with users.

4. Virtual fat clients (VFC ) and HFCs (VHFC ) – These represent client computers that execute at least one client application. They are described by their computing capacity, primary and secondary memory.

5. Virtual Storage Area Networks (VSAN ) – A VSAN represents a virtual SAN fabric, that is a set of optical switches and hubs, and a corresponding set of virtual storage devices which allow virtual servers located in the same site to share disks (Ward et al., 2002).

An infrastructural model is built by associating technology requirements with virtual components. In general, a technology requirements’ model can be associated with multiple virtual infrastructural models depending on design choices on infrastructural alternatives. For example, different groups of applications can be assigned to the same virtual server and different groups of user classes can be assigned to the same virtual thin/HFC server. If the cardinality of a group is $n , ~ 2 ^ { n } - 1$ different allocations of applications or user classes can be created (that is, the group’s power set, excluding the empty set) and accordingly 2<sup>n</sup>1 virtual infrastructural models can be defined.

An initial virtual infrastructural model is built and then transformed into a physical model that represents the initial solution of the optimization algorithm (see ‘Costminimization algorithm’ section). The initial virtual infrastructural model is built according to the following rules:

1. Each user class $C _ { i }$ is assigned n(C<sub>i</sub>) virtual clients of the lightest type, according to the following order: thin clients, HFCs and PCs. Thin clients are considered lighter than HFCs and PCs since they have lower computing capacity. HFCs are considered lighter than PCs since they delegate the execution of a subset of applications to servers. Each fat client is assumed to execute all client applications used by $C _ { i } .$ Each class $C _ { i }$ that has been assigned thin clients is also assigned a VTS , which is assumed to execute all client applications used by $C _ { i } .$ . Each class $C _ { i }$ that has been assigned a hybrid fat client is also assigned a virtual HFC server and client applications that can be indifferently executed on clients or servers are assigned to HFCs.

2. Requests are implemented with the highest number of tiers, that is by assigning a virtual server to each application involved in responding to the request, without introducing server farms.

3. Virtual servers are located at the site of the user class $C _ { i }$ that maximizes the total frequency of both inbound and outbound requests of the corresponding application tier.

4. All VTS ’s and HFC servers are located at the same site, within the same building and on the same floor as their user class.

5. All virtual servers have a local disk, that is, SANs are not introduced.

Intuitively, rules 1–5 implement the professional design guidelines discussed in an earlier section. The optimization algorithm discussed in ‘Cost-minimization algorithm’ section is in charge of changing these initial design decisions to reduce costs.

Both the initial virtual infrastructural model and subsequent models generated by the optimization algorithm are sized by accounting for the computing requirements of all user classes, as described in Appendix B. Sizing rules of Appendix B generate infrastructural components that meet requirements with no approximation (see also (Ardagna and Francalanci, 2002; Ardagna et al., 2003)).

## The physical infrastructural model

Physical design transforms the virtual infrastructural model into the physical model by associating commercial components with virtual computing resources. A physical server is associated with each virtual server. Physical servers should provide a computing and storage capacity that guarantee a utilization of their CPU and disk lower than 60% (Menasce´ and Almeida, 2000) (with values of utilization greater than 60%, small variations of throughput would cause a substantial growth of response time and, overall, performance would become unreliable (Abdelzaher et al., 2002; Ardagna, 2004)). For example, the CPU utilization of the physical server associated with a virtual server $\mathrm { V S _ { i } }$ is calculated as follows:

$$
C P U - u t i l i z a t i o n = \sum_ {j} f (R _ {j}) \frac {C P U - t i m e (R _ {j} , A _ {k})}{n _ {k}},
$$

where the summation is extended to all the requests $R _ { j }$ executed by the physical server, $f ( R _ { j } )$ indicates the frequency of $R _ { j } , A _ { k }$ is the server application supporting $R _ { j } ,$ $C P \bar { U } \ – t i m e ( R _ { j } , A _ { k } )$ is R ’s CPU demanding time and $n _ { k }$ is the performance ratio of the physical server to $\boldsymbol { A _ { k } } ^ { \prime } \boldsymbol { s }$ tuning system.

In the same way, a commercial personal computer is associated with each virtual fat or hybrid client and a commercial server is associated with each thin and HFC server. Both commercial clients and servers should provide a computing capacity (MIPS) and a primary and secondary storage capacity greater than or equal to that of corresponding virtual resources. Vice versa, a commercial thin client of minimum cost is associated with each virtual thin client.

In order to size WANs, each site is associated with its total input and output bandwidth requirements, calculated as the summation of input and output bandwidth requirements of all requests exiting or entering the site and of thin clients and HFCs accessing remote servers. The capacity of the physical WAN, referred to as physical bandwidth, is then calculated according to Kleinrock’s (1976) model:

$$
\text { Physical } - \text { bandwidth } = \text { Total } - \text { bandwidth } + \frac {l}{T}
$$

where T is the time latency and l is the average packet size, which for IP-based VPNs can be empirically set to 200 ms and 550 bytes, respectively (Yuan and Strayer, 2001).

Finally, SANs are designed according to the models presented in Alvarez et al. (2002) and Ward et al. (2002). The design of SANs is organized in two steps: storage devices are designed first and then connected to servers by designing the configuration of switches and hubs, that is the SAN fabric. A greedy algorithm has been implemented for the selection of storage devices, by extending the approach of (Alvarez et al., (2002)) with a greedy selection of a set of storage devices. The Quickbuilder costminimization algorithm presented in Ward et al. (2002) has been implemented for the design of SAN fabrics.

## Evaluation of total infrastructural costs

Physical components are associated with multiple cost categories, which are summarized in Table 2. Total infrastructural costs are calculated as the summation of all cost categories for all physical components.

Support personnel costs represent the economic value of per-year man hours required to manage hardware components and corresponding software applications. Empirical benchmarks of per-year management man hours are discussed in ‘Data sample of physical components and costs’ section.

Licenses of client applications are supposed to be associated with client computers (PCs and HFCs) if they are executed locally, and with servers if they are executed remotely. Both remotely executed client applications and server applications can involve a single license for each physical server where they are installed or multiple licenses, which, in turn, can be a function of the total number of users or of the overall computing load on each server. This one-toone relationship between license cost functions and applications is accounted for within the database of costs described in ‘Data sample of physical components and costs’ section.

Note that software implementation costs are excluded from the evaluation of total infrastructural costs. For packaged software, which represents the bulk of current implementation projects (Ochs et al., 2001), infrastructural design alternatives listed in Table 1 either are or are not supported. Packages that support a broader range of infrastructural alternatives typically involve higher license costs (Bertoa and Vallecillo, 2002; Martin, 2003). Designers can evaluate the impact of license costs on infrastructural design by reiterating the cost-minimization process with different infrastructural constraints and assessing the variation of design choices and costs. For custom software, the variation of development costs with infrastructural alternatives can only be assessed by applying software cost estimation methodologies (Pressman, 2001).

## Cost-minimization algorithm

The cost-minimization problem is computationally complex, as the degrees of freedom in building an infrastructural model satisfying technology requirements grow exponentially with the number of optimization variables. For example, a technology requirements model including a group of n server applications can generate 2<sup>n</sup>1 virtual infrastructural models, which merge and centralize server applications in different ways. As alternatives combine, the degrees of freedom grow accordingly.

Table 2 Summary of cost categories

<table><tr><td>Physical component</td><td>Investment costs</td><td>Management costs</td></tr><tr><td>Server</td><td>Acquisition and installation costsOperating system licensesLicenses and installation costs of server applicationsLicenses and installation costs of remotely executed client applications</td><td>Hardware support personnel costsSoftware support personnel costs</td></tr><tr><td>Fat client</td><td>Acquisition and installation costsOperating system licensesLicenses and installation costs of client applications</td><td>Hardware support personnel costsSoftware support personnel costs</td></tr><tr><td>Hybrid fat client</td><td>Acquisition and installation costsOperating system licensesClient access licenses (CAL)Licenses and installation costs of locally executed client applications</td><td>Hardware support personnel costsSoftware support personnel costs</td></tr><tr><td>Thin client</td><td>Acquisition and installation costsClient access licenses (CAL)</td><td>Hardware support personnel costs</td></tr><tr><td>SAN</td><td>Acquisition and installation costs of storage devices, switches and hubs</td><td>Support personnel costs</td></tr><tr><td>LAN</td><td>Acquisition and installation costs of switches and hubs</td><td>Support personnel costs</td></tr><tr><td>WAN</td><td>Acquisition and installation costs of backbone link nodesFixed cost of the VPN contract</td><td>Annual feeSupport personnel costs</td></tr></table>

Due to this complexity, optimization is based on the tabu search meta-heuristic algorithm (Glover and Laguna, 1997). Meta-heuristic approaches can be seen as a generalization of the local search strategy. The basic idea of the local search is to define a neighbourhood of an admissible solution x, referred to as N(x), and explore it searching for a solution x’ that improves the objective function f(x). The neighbourhood is defined by applying to x basic ‘moves’ (for example a neighbourhood of a scheduling problem can be defined by the move which swaps two items in the schedule). If x<sup>0</sup> is found in N(x), the local search will explore N(x<sup>0</sup>). On the contrary, if N(x) does not contain any solution improving the objective function, the local search algorithm terminates returning x as a local optimum. The pitfall of this basic local search is that the objective function f(x) of most real problems has multiple local optima, which can be significantly different from the global optimum. Meta-heuristic approaches have been proposed as extensions of the local search algorithm that do not stop at the first local optimum. The basic idea of the tabu search metaheuristic algorithm is that if a solution x is found to be a local optimum with no x<sup>0</sup>AN(x) improving f(x), a solution $x ^ { \prime \prime } { \in } N ( \hat { x } )$ worsening f(x) can be selected. N(x<sup>00</sup>) is then explored, excluding x and a predefined number of previously explored solutions in order not to cycle around the same local optimum. The set of previously explored solutions that are excluded in case of worsening moves is referred to as tabu list, which is usually managed as a FIFO queue (Glover and Laguna, 1997). Note that tabu moves are inspected at each step and, in case they are found to improve the current optimum, they can be overruled.

This paper’s implementation of the tabu search is aimed at the minimization of the total cost of the physical model, which represents the objective function. The initial solution is a virtual infrastructural model designed as discussed in previously.

The neighbourhood of a solution is defined by applying the moves summarized in Table 3. The modified infrastructural model is then transformed into the corresponding physical model whose total cost represents the new value of the objective function. Note that moves in Table 3 correspond to design alternatives in Table 1. The results of this implementation of tabu search have been compared with those of an exhaustive algorithm limited to singlealternative infrastructural design problems, which allow the application of only one move in Table 3. In these cases, the tabu search has proved to identify the global optimum. Future work will evaluate the quality of the heuristic solution for more complex design problems.

## Empirical verifications

The design approach proposed in this paper is verified to assess the magnitude of cost reductions and, thus, the potential benefits of a systematic methodological approach to cost issues of infrastructural design. Results will also be compared with current guidelines in the professional literature reported in Table 1. Empirical verifications have been supported by infrastructure systems integrated design environment (ISIDE), a prototype tool that implements the cost-minimizing approach. The tool includes a database of commercial infrastructural components and related cost data, which is described in the next section. Results are then presented in the subsequent section.

Table 3 Moves applied to the virtual infrastructural model by the tabu search optimization algorithm

<table><tr><td>Move</td><td>Description</td></tr><tr><td>Change in the type of client computers for a user class</td><td>1. From PC to HFC, or vice versa2. From PC to thin, or vice versa3. From HFC to thin, or vice versa</td></tr><tr><td>Change of the allocation of a client application for a user class that has been assigned HFCs</td><td>An application that can be indifferently executed by client or server computers is shifted from HFCs to the corresponding remote server, or vice versa</td></tr><tr><td>Change in the number of tiers of requests</td><td>The number of tiers of a request is either increased (a new server is introduced) or decreased (an existing server may be eliminated)</td></tr><tr><td>Introduction of a server farm</td><td>A server is replaced by two servers managed as a server farm</td></tr><tr><td>Change in the number of computers in a server farm</td><td>The number of computers in a server farm is either increased or decreased (if the number of remaining servers is one, this move eliminates the server farm)</td></tr><tr><td>Server aggregation and server split</td><td>Two servers (or server farms) are aggregated or, conversely, a server (or server farm) is split into two servers (or server farms). In this case, applications are randomly allocated on the new servers (in compliance with constrains)</td></tr><tr><td>Change in the location of a server</td><td>A server (or server farm) is moved to a different site</td></tr><tr><td>Introduction/removal of a SAN</td><td>A SAN is introduced/removed within a site</td></tr></table>

## Data sample of physical components and costs

Empirical verifications have been based on the following sample of physical components and related cost data:

\- 80 thin client configurations from five vendors;

\- 1100 PC configurations from four vendors;

\- 9000 server configurations from four vendors;

\- 1000 switch configurations from three vendors;

\- 10 hubs (fixed configuration) from three vendors;

\- 50 optical switch configurations and 20 optical hubs (SAN fabric components) from three vendors;

\- 100 storage array device configurations from three vendors;

\- 50 backbone link node router configurations form three vendors.

Configurations of computers have been considered distinct if they have a different number or type of CPUs, or different RAM and disk capacities.

Acquisition costs and operating system licenses of physical components have been collected from vendors’ Internet sites, hardware technical documentation and configuration tools. Vendors provide free installation upon acquisition for the majority of their components. However, for less expensive components, acquisition does not include installation and installation costs have been estimated as 5% of acquisition costs (Bajaj, 2000).

Ad hoc surveys have been necessary to obtain VPN setup and management costs and annual fees. The cost of broadband connections are mostly confidential and are rarely published. A questionnaire has been submitted to four international carriers. The questionnaire has surveyed persite annual fees and related setup and support personnel costs of always-on VPN access technologies, that is leased lines, ADSL and HDSL. Costs on 80 VPN configurations between 64 kbit/s and 64 Mbit/s have been obtained from each carrier. Empirical verifications have considered the mean value of costs across the four carriers for each VPN configuration.

LAN support personnel costs are empirically estimated as 20% of the total cost of network components (Nortel Networks, 2001; Rocco, 2002). Management costs of SANs and servers connected to SANs are estimated to range between 15% and 25% of the management costs of the same set of servers when equipped with disks (Nortel Networks, 2001; Rocco, 2002).

Management costs of hardware components have been evaluated as a percentage of acquisition costs (Redman et al., 1998). Numerous benchmarks of PCs’ annual management costs have been published in the literature, ranging between 5 and 15% of acquisition costs (Redman et al., 1998; Molta, 1999b). The average value of these professional benchmarks, that is 10%, has been considered for empirical verifications. Management costs of thin clients are evaluated as described in Molta (1999b), who has empirically estimated the percent reduction in thin clients’ management costs compared to PCs. Cost reductions are reported to range between 20 and 35%, depending on contextual variables. The average value of Molta’s benchmarks has been considered for empirical verifications (see also Schlegel, 2002). In the case of hybrid fat clients, this reduction percentage is supposed to decrease as the fraction of locally executed applications increases. Annual management costs of servers have been estimated as in Meta Group (1999) and Redman et al. (1998), ranging from 15 to 25%. Once again, the variability across empirical benchmarks has been resolved by considering the average 20% benchmark for empirical verifications. Note that management costs have been corrected for inflation and measured at the same time (year 2003).

The database of costs also includes license, installation and management costs of the following applications:

\- Client applications: Lotus Notes, Office 2000, Wordperfect suite. License costs have been obtained from public sources of information, mostly vendors’ Internet sites. Installation and management costs have been estimated as 5 and 15% of total license costs, respectively, as in (Redman et al., 1998, see also Groupe Tecna, 2002).

\- Server applications: Apache, DB2, Internet Information Server, iPlanet Application and Web servers, Oracle, SQL Server, Stronghold Web server, Tomcat, Web Sphere, Zeus Web server.

For this sample of server applications, Table 4 shows how vendors calculate license costs as a function of infrastructural components. When licenses can be associated with different infrastructural components, the minimum-cost function is selected. Installation and management cost benchmarks have been estimated as in Rocco (2002), where they are reported to range from 5 to 10% and from 20 to 50% of license costs, respectively. The average value of benchmarks has been considered for empirical verifications.

Table 4 License costs of server applications

<table><tr><td>Server application</td><td>License costs</td></tr><tr><td>Apache 1.3</td><td>Free</td></tr><tr><td>Bea Tuxedo 8.0</td><td>Per number of clients/ per CPU</td></tr><tr><td>DB2</td><td>Per server/per number of concurrent users</td></tr><tr><td>Internet Information Server 5.0</td><td>Free</td></tr><tr><td>iPlanet Application server</td><td>Per type and number of CPUs</td></tr><tr><td>iPlanet Web server</td><td>Per number of CPUs</td></tr><tr><td>Oracle 9i</td><td>Per number of clients/ per CPU</td></tr><tr><td>SQL Server 2000</td><td>Per number of CPUs/ per number of clients</td></tr><tr><td>Stronghold Web server 4.0</td><td>Per server</td></tr><tr><td>Tomcat 4.0</td><td>Free</td></tr><tr><td>Web Sphere 4.0</td><td>Per server</td></tr><tr><td>Zeus Web server 4.2</td><td>Per server/per type and number of CPUs</td></tr></table>

Empirical results of cost-oriented infrastructural design

This section provides empirical evidence of the cost reductions that can be obtained with the cost-minimization process proposed in this paper. Results are compared with the professional guidelines discussed in Table 1. Cost reductions are evaluated by comparing the TCO obtained by applying the cost-minimization process with the TCO obtained by applying professional guidelines.

In the next section, individual design alternatives listed in Table 1 are analysed by separately modifying corresponding technology requirements variables. The robustness of results is evaluated through sensitivity and scalability analyses in the subsequent section.

## Cost reductions

The tests performed to evaluate cost reductions have required an average 70-min computation time on a 2-way Xeon 700 IBM Netfinity Linux server with 1GB of RAM. Minimum and maximum computation times have been 40 s and 2 h, respectively. The tabu search algorithm always terminates providing a solution as long as the optimization space is not empty, that is requirements are consistent.

Client typology: To evaluate the cost reductions that can be obtained from the optimization of the type of client computers (thin, fat or hybrid), a single-site and singleuser-class infrastructure is considered. The technology requirements of a data entry worker (DEW), structured task worker (STW) and knowledge worker (KW) user classes are specified as described in Microsoft (2000). DEW, STW and KW represent typical user classes with increasing think time and corresponding computing requirements. The target operating system and remote protocol are Windows 2000 and RDP 5.0, respectively. Client applications are those included in the Office 2000 suite. The percentage of concurrent users is 25% for STW and KW and 80% for DEW (Mathewson, 1999). Thin clients and HFCs are constrained to be supported by an application server farm. In the HFC scenario, Word2000 and Excel2000 can be indifferently executed by the HFC or by the application server. The infrastructure is also supposed not to communicate with the external environment and, thus, not to require a WAN connection. The total number of users in different user classes is increased from 1 to 1000 (step 5).

Professional guidelines suggest the adoption of thin clients and HFCs whenever possible in order to minimize clients’ hardware investments and management costs. Results show that for a low number of users (1–6), PCs are selected as the cost-minimizing type of client. For a number of users higher than 6, the cost-minimizing solution switches to thin clients and does not further modify as the number of users grows. A server farm is introduced for the thin-client solution above 180 STW and KW users, and above 400 DEW users. These results are consistent with the lower acquisition and management costs of thin clients, which can be expected to compensate for the investment in the thin server above a break-even number of users. As the number of users increases, the implementation of a server farm reduces the scale diseconomies that would be associated with large servers and makes the thin-client solution steadily convenient. Break-even values are consistent with the professional literature (Precision Group, 2002). As a consequence, cost reductions from the application of the design approach are low, 2% on average and, overall, the professional guideline for the client typology alternative is confirmed (Table 1).

It is interesting to note that TCO savings from the adoption of HFCs as opposed to PCs range between 2 and 5%. This low value contradicts previous results in the professional literature, which presents HFCs as a potential source of significant cost reductions, related to management savings from the remote execution of applications (Molta, 1999b). On the contrary, results from the methodological solution show that TCO reductions for the remote execution of applications are marginal (the bulk of TCO is due to hardware and management costs of client applications installed on HFCs).

Total number of servers in a server farm: Application servers and thin-client servers are separately analysed. Both analyses refer to a single-site infrastructure. In both cases, a single server application and a single thinclient server is considered, in order to avoid the server sharing alternative and focus on a single server farm. Professional design guidelines indicate to implement server farms whenever possible and to select the smallest server that can support applications in order to minimize hardware acquisition costs (‘build small’ paradigm, see Table 1).

In the optimization of application server farms, two types of server applications are considered: Internet Information Server on a Windows 2000 system and Apache on a Sun system. Requests are supposed to be external. The frequency of requests increases from 0.01 to 37.0 req/s, with step 0.01, demanding times are 0.5 and 0.4 s evaluated on a PIII 550 Raid-5 Ultra SCSI and on an Ultra SparcII 450 Raid-0 Ultra SCSI tuning system. Average cost reductions are 29.51 and 53.15%, in the IIS and Apache case, respectively. The empirical design rule, which suggests the selection of smallest server supporting applications, is a cost-minimizing criterion in only 5% of all tests. The solutions provided by the tabu-search algorithm adopt mid-range servers with powerful processors which reduce the number of installed computers and operating system costs.

Thin-client server farms are analysed for STW, KW and DEW users. The number of users is increased from 5 to 2000, with a 5-user step. The optimization process delivers a low average cost reduction, 1.77, 0.65 and 0.24% for STW, KW and DEW, respectively, since the bulk of TCO is due to client management costs, which cannot be further reduced through optimization. However, these low percent savings on TCO correspond to a 94.4, 61.05 and 20.6% reduction of server hardware costs. Results suggest the implementation of server farms according to the ‘build mall’ paradigm only for DEW users while STW and KW should be supported by mid-range servers.

Number of tiers: A single-site infrastructure is considered. Users generate requests (R) from a browser and dynamic HTML pages are generated through the cooperation among four server applications: a Web server (IIS), a Servlet engine (Tomcat), an application server (WebSphere 4) and a DBMS (SQL Server). Demanding times are evaluated on a W2000, PIII 550, RAID-5 Ultra SCSI tuning system. Requirements for RAM and demanding times are typical for Internet/Intranet applications (Fiser, 2000).

Two different scenarios are analysed. In the first scenario, computing load is hypothesized to be uniformly distributed among applications serving the same request (0.5 s CPU demanding time), while in the second scenario, the DBMS and the application server are supposed to be CPU-bounded (1 s CPU demanding time), which is a likely situation for Internet/Intranet applications. In both scenarios, the total frequency of requests is increased from 0.01 to 37.0 req/s, with a 0.01 frequency step. The optimization domain is defined by the allocation of applications on two, three, four or five tiers. Two distinct four-tier solutions exist, labelled four-tier(a) and four-tier(b) in Figure 2, corresponding to a different grouping of the Web server, the Servlet engine and the application server.

Professional design guidelines suggest the allocation of server applications with the maximum number of tiers, in order to minimize hardware acquisition costs (Ingham et al., 2000; Sonderegger et al., 2002). For example, in 1995, Web services were reported to be implemented with 2–3 tiers (Kwan et al., 1995), while current e-business sites are implemented by seven to nine tiers (Sonderegger et al., 2002). Intuitively, the number of tiers minimizing costs should increase with the frequency of requests since, when the load is light, the two-tier solution, implemented in the first wave of web applications (Kwan et al., 1995) minimizes costs, as it requires a single server. As load increases, a growing server size would involve diseconomies of scale and a three-tier solution can reduce costs by partitioning load on two smaller servers/server farms. The costminimizing solutions for different values of frequency are summarized in Table 5. The average cost reduction from optimization compared to professional design guidelines is 26.33 and 17.30% for the first and second scenario, respectively. A lower percent reduction in the second scenario can be expected, since in the first scenario load balancing among applications can be exploited to optimize infrastructural design. However, the number of tiers minimizing costs is found not to increase with frequency, as shown in Table 5. These findings indicate that general design guidelines are difficult to obtain and increasing the number of tiers as suggested in the professional literature may result in a cost disadvantage. Methodological results show that sometimes a lower number of tiers can be cost effective by implementing multiple-tiers on a single farm built from mid-range or high end servers reducing the number of installed components, operating systems and management costs. This anyway depends on system load and on the discrete distribution of commercial components.

![](/api/attachments/EFYC5ZKB/fulltext/images/d65d1185dd8b154a79541f71c70cd04d69e80e377386b7af29f7612f5886f0ec.jpg)  
Figure 2 Design alternatives on the number of tiers.

Table 5 Optimization results for the number of tiers alternative

<table><tr><td colspan="2">Scenario 1</td><td colspan="2">Scenario 2</td></tr><tr><td>Frequency range</td><td>Minimum cost infrastructure</td><td>Frequency range</td><td>Minimum cost infrastructure</td></tr><tr><td>0–0.54</td><td>2-tiers</td><td>0–0.37</td><td>2-tiers</td></tr><tr><td>0.55–0.62</td><td>3-tiers</td><td>0.38–0.55</td><td>3-tiers</td></tr><tr><td>0.63–0.66</td><td>2-tiers</td><td>0.56–0.63</td><td>2-tiers</td></tr><tr><td>0.67–0.73</td><td>3-tiers</td><td>0.64–1.14</td><td>3-tiers</td></tr><tr><td>0.74–0.93</td><td>2-tiers</td><td>1.15–1.27</td><td>4-tiers</td></tr><tr><td>0.94–1.54</td><td>3-tiers</td><td>1.28–1.34</td><td>4-tiers</td></tr><tr><td>1.55–2.32</td><td>4-tiers</td><td>1.35–1.40</td><td>4-tiers</td></tr><tr><td>2.33–2.51</td><td>3-tiers</td><td>1.41–2.31</td><td>4-tiers</td></tr><tr><td>2.52–4.63</td><td>5-tiers</td><td>2.32–2.80</td><td>4-tiers</td></tr><tr><td>4.64–5.65</td><td>4-tiers</td><td>2.81–4.63</td><td>5-tiers</td></tr><tr><td>5.66–37</td><td>5-tiers</td><td>4.64–5.65</td><td>4-tiers</td></tr><tr><td></td><td></td><td>5.66–30.14</td><td>5-tiers</td></tr><tr><td></td><td></td><td>30.15–30.39</td><td>2-tiers</td></tr><tr><td></td><td></td><td>30.40–31.00</td><td>3-tiers</td></tr><tr><td></td><td></td><td>31.01–31.39</td><td>4-tiers</td></tr><tr><td></td><td></td><td>31.40–31.61</td><td>2-tiers</td></tr><tr><td></td><td></td><td>31.63–32.83</td><td>4-tiers</td></tr><tr><td></td><td></td><td>32.83–33.91</td><td>4-tiers</td></tr><tr><td></td><td></td><td>33.92–34.04</td><td>2-tiers</td></tr><tr><td></td><td></td><td>34.05–34.65</td><td>3-tiers</td></tr><tr><td></td><td></td><td>34.66–35.16</td><td>4-tiers</td></tr><tr><td></td><td></td><td>35.17–35.26</td><td>2-tiers</td></tr><tr><td></td><td></td><td>35.27–36.48</td><td>4-tiers</td></tr><tr><td></td><td></td><td>36.49–37.00</td><td>5-tiers</td></tr></table>

Allocation of applications (or server sharing): Similar to server farms, server sharing is separately analysed for application servers (scenario 1) and thin-client servers (scenario 2). Two Web-server applications are considered, representing two different instances of Internet Information Server responding to external requests $R _ { 1 }$ and $R _ { 2 } ,$ respectively. Each request is characterized by 0.5 s. demanding time for CPU and 0.1 s demanding time for disk on a W2000, PIII 550, Raid-5 Ultra SCSI tuning system.

Two infrastructural models can be associated with technology requirements, distinguished by the allocation of applications on a single shared server/server farm or two dedicated servers/server farms. Professional guidelines recommend the centralization of applications on a single farm to minimize management costs and exploiting hardware scale economies (Table 1). The frequency of requests is increased from 0.05 to 16.5 req/s with a 0.05 step. All combinations of frequency for $R _ { 1 }$ and $R _ { 2 }$ are analysed. The average cost reduction is 45.5%. It is important to note that centralizing applications on a single server/server farm is cost effective in only 8% of all tests, usually when the load of the two request classes are significantly different (for example, 1:10 ratio). In this situation, a single server farm can exploit hardware scale economies and the number of physical components can be reduced. Vice versa, if the load is balanced across request classes, the optimum sizing of two independent farms, often built from mid-range servers, can reduce TCO.

To analyse server sharing among thin-clients (scenario 2), two STW user classes are specified, $C _ { 1 }$ and $C _ { 2 } .$ Two infrastructural models can be defined, distinguished by the allocation of user classes $C _ { 1 }$ and $C _ { 2 }$ on a single shared server/server farm or two dedicated servers/server farms. The number of users in $C _ { 1 }$ and $C _ { 2 }$ varies from 5 to 1000 with a 5-user step. All combinations of the number of users in $C _ { 1 }$ and $C _ { 2 }$ are analysed. The average TCO reduction is 2.18%, although server costs decrease by 75%. Centralizing client applications on a single server is cost effective in 81% of all tests. Again the reduction of TCO is low, since the bulk of TCO is caused by hardware and management costs of clients. Tabu solutions centralize user classes on a single farm built from mid-range servers, disconfirming professional guidelines.

Location of servers: Similar to previous alternatives, the location of servers alternative is separately analyzed for thin-client servers (scenario 1) and application servers (scenario 2). In the first scenario, four KW user classes, $C _ { 1 } ,$ $C _ { 2 } , C _ { 3 }$ and $C _ { 4 }$ located in four different sites, $S _ { 1 } , S _ { 2 } , S _ { 3 }$ and $S _ { 4 }$ are considered. All user classes are supposed to access the same Web server application located at site $S _ { 1 } .$ . Each user class is assigned a thin-client server. According to professional guidelines, thin-client servers should be centralized in a single site in order to minimize both network costs and hardware management costs. It is assumed that the percentage of concurrent users is 25% and each active user accesses a Web page every 4 min. Each request sends 10 kbytes and receives 220 kbytes. Bandwidth requirements to connect thin clients with thin-client servers are 10 kbit/s, in compliance with the RDP protocol (Microsoft, 2000).

The number of users is increased from 10 to 500 with step 10 (simultaneously applied to all user classes). The average cost reduction is 6.03%. It can be observed that centralizing servers in a single site is a methodological choice in only 42% of all tests. In this respect, professional guidelines generally supporting the centralized solution, do not seem confirmed by a systematic algorithmic testing (IBM, 2002), The optimization process takes advantage of reductions of network costs that can be obtained by searching for the optimal location of thin-client servers.

To analyse the location of application servers (scenario 2), two user classes are supposed to access a dedicated Web server (IIS on W2000 and Apache on a Sun system) which, in turn, conveys requests to a common database server located at site $S _ { 1 }$ . The number of users ranges from 10 to 500 with (step 10 simultaneously applied to both classes), demanding times are 0.5 and 0.4 s evaluated on a PIII 550 Raid-5 Ultra SCSI and on an Ultra SparcII 450 Raid-0 Ultra SCSI tuning system.

The average cost reduction is 32.36%. It can be observed that centralizing servers in a single site is a cost-minimizing solution in 54% of all tests. Once again, the tabu search can reduce the TCO by reducing network costs whenever their reduction compensates for the higher management costs of decentralized servers.

## Sensitivity and scalability analyses

The robustness of optimization results is evaluated through sensitivity analyses. Sensitivity measures the magnitude of output changes as a consequence of variations in input parameters. The sensitivity of the optimization function is measured as a percent change in the solution’s TCO as a consequence of a variation in empirical estimates of costs, which can be subject to uncertainty. Sensitivity is analysed both for the solution of the tabu search algorithm and for the infrastructural solution obtained by applying professional guidelines. In this way, the comparison between tabu and professional results is complemented by an assessment of their robustness.

As discussed in the section on Data sample of physical components and costs, professional cost benchmarks vary within a range. In previous section, TCO is evaluated for the average value of all cost benchmarks within their range. Sensitivity is calculated as a percent change of TCO as cost benchmarks are set to their minimum and maximum values. The tabu and professional solutions show similar values of sensitivity across all analyses. On average, a 740% variation of cost benchmarks corresponds to a 710% variation of TCO for both solutions (detailed results can be found in Ardagna, 2004). Tests show a sensitivity of TCO lower than corresponding cost reductions reported in the previous section. This suggests that uncertainty on empirical benchmarks does not significantly affect the magnitude of cost reductions and, thus, the robustness of results is sufficient to support an algorithmic approach to cost analyses.

From a cost perspective, an infrastructural solution is scalable if it can be upgraded to satisfy growing capacity requirements with low additional expenses. As capacity requirements increase, corresponding upgrades involve a cost which can be measured as:

$$
\begin{array}{l} \% \text {cost - of - upgrades} \\ = \frac {T C O _ {\text {upgraded - tabu - solution}} - T C O _ {\text {initial - tabu - solution}}}{T C O _ {\text {initial - tabu - solution}}} \times 1 0 0 \end{array}
$$

where TCO<sub>upgrade-tabu-solution</sub> indicates the total cost of ownership of the upgraded infrastructural solution satisfying new requirements and TCO<sub>initial-tabu-solution</sub> indicates the total cost of ownership of the methodological solution that is upgraded. The corresponding operating definition for the infrastructural solution obtained by applying professional guidelines is (see Figure 3):

![](/api/attachments/EFYC5ZKB/fulltext/images/0b541e416d6174c1d6b8fad2fed5ff56afa49a83f8aa33f3ee5c3a322c987a20.jpg)  
Figure 3 Cost-related measures of scalability.

$$
\begin{array}{l} \% \text {cost - of - upgrades} \\ = \frac {T C O _ {\text {upgraded - professional - solution}} - T C O _ {\text {initial - professional - solution}}}{T C O _ {\text {initial - professional - solution}}} \\ \times 100 \end{array}
$$

Upgrades also involve a loss, as it can be expected that the TCO of the upgraded solution is higher than the TCO of the corresponding optimum. This loss can be measured as:

$$
\begin{array}{l} \% \text {loss - of - upgrades} \\ = \frac {T C O _ {\text {upgraded - tabu - solution}} - T C O _ {\text {new - tabu - solution}}}{T C O _ {\text {new - tabu - solution}}} \times 1 0 0 \end{array}
$$

where TCO<sub>new-tabu-solution</sub> indicates the total cost of ownership of the tabu solution satisfying new requirements. The corresponding operating definition for the professional solution is (see Figure 3):

$$
\begin{array}{l} \% \text {loss - of - upgrades} \\ = \frac {T C O _ {\text {upgraded - professional - solution}} - T C O _ {\text {new - tabu - solution}}}{T C O _ {\text {new - tabu - solution}}} \times 1 0 0 \end{array}
$$

From a cost perspective, scalability increases as both parameters decrease. Both the tabu and the professional upgraded solutions are designed by applying the following rules (Gillmann et al., 2000):

\- New client computers are added according to increases in the number of users.

\- Network capacity is expanded according to increases in communication requirements.

\- Servers are upgraded as follows:

1. new processors are added until new computing requirements are satisfied;

2. if new requirements cannot be satisfied by adding new processors, a server farm is created adding new servers with the same configuration of existing ones.

Scalability is evaluated for a 100% growth of capacity requirements, which corresponds to the uncertainty that characterizes long-term predictions of workload (Vialta et al., 2002) for both professional and tabu solutions.

Table 6 Scalability to capacity requirements of client applications

<table><tr><td rowspan="2"></td><td colspan="2">Average cost variation</td></tr><tr><td>%cost-of-upgrades</td><td>%loss-of-upgrades</td></tr><tr><td>Scalability with the tabu initial solution100% increase of capacity requirements (MIPS)</td><td>38.13</td><td>11.22</td></tr><tr><td>Scalability with the professional initial solution100% increase of capacity requirements (MIPS)</td><td>42.34</td><td>13.42</td></tr></table>

Table 7 Scalability to capacity requirements of server applications

<table><tr><td rowspan="2"></td><td colspan="2">Average cost variation</td></tr><tr><td>%cost-of-upgrades</td><td>%loss-of-upgrades</td></tr><tr><td>Scalability with the tabu initial solution100% increase of capacity requirements (frequency of requests)</td><td>23.22</td><td>12.51</td></tr><tr><td>Scalability with the professional initial solution100% increase of capacity requirements (frequency of requests)</td><td>31.91</td><td>29.65</td></tr></table>

Results (Tables 6 and 7) show that the tabu solution involves significantly lower losses than the professional solution, which tends to diverge from new cost-minimizing solution. Infrastructures designed according to professional guidelines are also more costly to upgrade. The ‘think big, but build small’ professional principle seems cost effective to support limited increases of requirements, as the infrastructure can grow in ‘small’ steps. Conversely, tabu solutions accommodate large increases of requirements by taking advantage of greater scale economies.

## Discussion and conclusions

In this work, we have presented a design approach to support the cost-oriented design of IT architectures for multi-site distributed systems. The design of IT infrastructures constitutes a complex, top-down process that identifies the set of IT components that satisfies performance requirements and at the same time minimizes costs. The efficiency of the design process and the cost-effectiveness of the resulting infrastructure are bound to a correct and complete understanding of organizational requirements and to the fit between requirements and technology. Modern IT architectures involve a number of design choices with significant cost implications. The professional literature often focuses on specific techniques for the optimization of individual design phases, usually leading to sub-optimal solutions. Practitioners usually tackle individual design issues and refer to previous sizing experiences to guide overall design. The aim of our approach is to evaluate a large number of alternative solutions and find a candidate minimum-cost infrastructure that can be fine tuned by applying traditional performance analyses techniques.

Professional guidelines have been tested by applying the design approach proposed in this paper to several case studies and preliminary results indicate that cost reductions can be significant, ranging between 20 and 50% of total infrastructural costs. Table 8 summarizes results and compares them with professional guidelines. On average, professional guidelines have been found to be verified in only 33% of all tests, suggesting that the recentralization principle does not represent a general cot-minimization criterion. Scalability analyses have shown that the solution of a rigorous design process involves significantly lower losses than the professional solution, which is also more costly to upgrade. The ‘think big, but build small’ professional principle seems cost effective only if limited increases of requirements must be accommodated over time.

The analysis of the client typology design alternative has confirmed how the adoption of thin-clients is cost effective even for a low number of users (the break even is as low as six users) and has shown that the design of server farms is not critical, since the bulk of TCO is due to hardware and management costs of clients. For this reason, the cost savings associated with the adoption of HFCs, which are presented as a potential source of significant cost reductions by the professional literature (Molta, 1999), are marginal. It can be argued that if thin clients cannot be adopted since one or multiple applications cannot be executed remotely, then companies should adopt PCs as opposed to HFCs and continue to install all client applications locally.

The analysis of the second design alternative (Table 1) has shown that the type of servers in a server farm and their total number have a significant cost impact and require rigorous design. The minimum-cost server farm seems difficult to design by following experience-driven rules that suggest a higher number of servers as a general costminimization criterion (Scheier, 2001). Results have highlighted how adopting mid-range instead of entry-level servers can reduce the number of components and, thus, TCO by decreasing operating system costs and, in some cases, software license costs.

The analysis of the number of tiers alternative has shown that the number of tiers of the minimum-cost infrastructure does not increase systematically with computing load, while design guidelines in the professional literature recommend a higher number of tiers as a reliable source of savings (Sonderegger et al., 2002). Results have shown that allocating multiple tiers on a single farm may or may not be cost effective depending on system load and on the discrete distribution of commercial components.

The analysis of the allocation of applications alternative has shown that general design rules are difficult to infer.

Table 8 Summary of research hypotheses results

<table><tr><td>Sub-alternative</td><td>Average savings from the optimization approach (%)</td><td>Percentage of tests verifying research hypotheses (%)</td><td>Research approach findings</td></tr><tr><td>Client typology</td><td>2</td><td>100</td><td>The adoption of thin-clients is cost effective even for a low number of users (≥6 users). The design of thin server farms is not critical. The adoption of HFCs does not provide significant cost savings.</td></tr><tr><td>Number of tiers</td><td>22</td><td>81</td><td>The allocation of applications with the maximum number of tiers may or may not be cost effective depending on system load and on the discrete distribution of commercial components.</td></tr><tr><td>Total number of servers</td><td>36</td><td>18</td><td>The type and number of servers in a server farm have a significant cost impact and require rigorous design. The adoption of mid-range servers can reduce the number of components and TCO by reducing operating system costs and software license costs.</td></tr><tr><td>Allocation of applications</td><td>33</td><td>27</td><td>The centralization of applications can be cost-effective, depending on application requirements and system load.</td></tr><tr><td>Location of servers</td><td>19</td><td>48</td><td>The centralization of servers in a single site can be cost effective, but, in some cases, decentralization can reduce network costs and compensate for higher management costs of servers.</td></tr></table>

The centralization of web servers has resulted cost effective in only 8% of all tests; however, when thin client users are centralized, the centralization of thin servers is the minimum cost solution in almost 80% of all tests. Finally, the analyses of the location of servers alternative show that the geographical centralization of servers into large-scale systems can reduce management costs, but cannot be assumed as a universal cost-minimizing paradigm (Betts, 2002; IBM, 2002).

Preliminary results encourage future research to both extend the approach and improve the support tool. From a methodological standpoint, the range of design alternatives will be completed by extending the model to include network design alternatives on both topology and standards and to extend SAN design to metropolitan areas. In the current version of the design approach, WANs are constrained to be connected through an IP-based Virtual Private Network (VPN). WAN design will be extended in order to introduce ad hoc meshed connections among enterprise sites through leased lines.

From a hardware standpoint, the main limitations of the design approach are that NUMA (Non Uniform Memory Access) architectures cannot be accurately designed, due to the adoption of the simplified sizing rules. Bus memory access conflicts are not considered and the request scheduling policy is hypothesized to be balanced among processors. These limitations are accepted since the goal of this approach is to support cost analyses and the focus is on system-level design choices (Jain, 1987; Blyler and Ray, 1998; Zachman, 1999). Note that performance analyses should follow cost analyses to refine sizing (Ardagna et al.,

2003). The design approach will be extended to consider web services and grid environments that are characterized by high variability of system load (Menasce´ and Almeida, 2000). This will require a more accurate representation of system workload.

Future research should also consider legacy systems, by formalizing the reallocation of physical servers and empirically verifying their impact on the cost-minimization process. Current work is concerned with describing the optimization algorithm with operating research formalisms, to improve its performance and possibly identify original structures of optimization problems.

## Acknowledgements

This work has been partly supported by Nortel Networks and is part of Nortel’s project to provide frameworks to support feasibility analyses. Hardware benchmarking has also been supported by IBM as part of Equinox international project. Particular thanks are expressed to Riccardo Gallo, Andrea Molteni, Michele Terzaghi and Roberto Urban for their assistance in data collection and development activities.

## References

Abdelzaher, T.F., Shin, K.G. and Bhatti, N. (2002). Performance Guarantees for Web Server End-Systems: A control-theoretical approach, IEEE Transaction on Parallel and Distributed Systems 13(1): 80–96.

Alter, S., Markus, M.L., Scott, J., Ein-Dor, P. and Vessey, I. (2000). Does the trend toward e-business call for changes in fundamental concepts of information systems? (Debate). ICIS 2002 Proceedings.

Alvarez, G.A., Borowsky, E., Go, S., Romer, T.H., Becker-Szendy, R., Golding, R., Merchant, A., Spasojevic, M., Veitch, A. and Wilkes, J. (2002). Minerva: An automated resource provisioning tool for large-scale storage systems, ACM Transaction on Computer Systems 19(4): 483–518.

Ardagna, D. (2004). A Cost-Oriented Methodology for the Design of Information Technology Architectures, Ph.D. Dissertation, Politecnico di Milano, Italy.

Ardagna, D. and Francalanci, C. (2002). A Cost-Oriented Methodology for the Design of Web based IT Architectures, SAC2002 Proceedings (17th ACM Symposium on Applied Computing), Madrid, March 2002, pp 1127–1133.

Ardagna, D., Francalanci, C. and Trubian, M. (2003). A multi-model algorithm for the cost-oriented design of the Information Technology Infrastructure, ECIS 2003 Proceedings (11th European Conference on Information Systems); Napoles, June 2003.

Aue, A. and Breu, M. (1994). Distributed Information Systems: An advanced methodology, IEEE Transaction on Software Engineering 20(8): 594–605.

Bajaj, A. (2000). A Study of Senior Information Systems Managers’ Decisions Model in Adopting New Computing Architectures, Journal of the Association of Information Systems 1(4): 1–58.

Bertoa, M.F. and Vallecillo, A. (2002). Quality Attributes for COTS Components, In: Proceedings of the sixth ECOOP Workshop on Quantitative Approaches in Object Oriented Software Engineering (QAOOSE 2002), Ma´laga, Spain, June 2002, pp. 54–66.

Betts, M. (2002). The next chapter. The Future of Hardware. ComputerWord (WWW document)http://www.computerworld.com/hardwaretopics/ hardware/story/0,10801,75887,00.html (accessed 9 Nov 2004).

Blyler, J.E. and Ray, G.A. (1998). What’s Size Got to Do with It? Understanding Computer rightsizing. IEEE Press, Understanding Science & Technology Series. ISBN 0-7803-1096-9.

Ein-Dor, P. (1985). Grosch’s Law Revisited: CPU power and the cost of computing, Management Communication of the ACM 28(2): 142–150.

Fiser (2000). The Premiericon Scaling test. Scalable e-commerce solution for Internet bankers, A White Paper from Fiser and Microsoft.

Francalanci, C. and Piuri, V. (1999). Designing Information Technology Architectures: A cost-oriented methodology, Journal of Information Technology 14(2): 181–192.

Gavish, B. and Pirkul, H. (1986). Computer and Database Location in Distributed Computer Systems, IEEE Transactions on Computers 35(7): 583–590.

Gillmann, M., Weissenfels, I., Weikum, G. and Kraiss, A. (2000). Performance and availability assessment for the configuration of distributed workflow management systems, Proceedings of the 7th International Conference on Extending Database Technology, pp. 183–202.

Glover, F.W. and Laguna, M. (1997). Tabu Search, Dordrecht: Kluwer Academic Publishers.

GROUPE TECNA (2002). Cost comparison advantage, http://www.gtechna.com/ e/software/advantage.Accessed on 9th November 2004.

IBM. (2002). Improve the return on your IT investment with Server Consolidation (WWW document)http://www-1.ibm.com/servers/eserver/ iseries/australia/serv.htm (accessed 8th June 2002).

Ingham, D.B., Shrivastava, S.K. and Panzieri, F. (2000). Constructing dependable Web services, IEEE Internet Computing 4(1): 25–33.

Ishizuka, M., Kawakatsu, M., Asai, Y., Ebisu, T., Hashizume, K. and Matsushita, M. (1999). Market and Technical Trend on Computer Communication, Oki (WWW document)http://www.obd.com/oki/otr/ downloads/otr-162-26.pdf (accessed 10th June 2000).

Jain, H.K. (1987). A Comprehensive Model for the Design of Distributed Computer Systems, IEEE Transaction on software engineering 13(10): 1092–1104.

Kleinrock, L. (1976). Queueing Systems, Vol. 2: Computer Applications, New York: John Wiley & Sons.

Kwan, T.T., McGrath, R.E. and Reed, D.A. (1995). NCSA’s World Wide Web Server: Design and performance, IEEE Computer 28(11): 68–74.

Lazowska, E.D., Zahorjan, J., Graham, G.S. and Kenneth, C.S. (1984). Quantitative System Performance Computer System Analysis using Queueing Network Models, Englewood Cliffs, NJ: Prentice-Hall.

Martin, A. (2003). What Drives the Configuration of Information Technology Projects? Exploratory research in 10 organizations, Journal of Information Technology 18(1): 1–15.

Mathewson, M. (1999). Microsoft’s TSE Licensing Model. Thin Planet.www.thinplanet.com/opinion/overview-TSE-licensing.asp.

Menasce´, D. and Almeida, V. (2000). Scaling for E-business. Technologies, models, performance and capacity planning, Englewood Cliffs, NJ: Prentice-Hall.

Meta Group (1999). Next-Millennium Platform Infrastructure Strategies: Evaluation, Consolidation, and Costing. http://www.metagroup.de/Accessed on 6th December 1999.

Microsoft (2000). Windows 2000 Terminal Services Capacity and Scaling, www.microsoft.com/windows2000/library/technologies/terminal/ tscaling.asp.

Molta, D. (1999a). Thin Client Computers Come of Age. Network Computing, www.networkcomputing.com/1009/1009buyers1.html.

Molta, D. (1999b). For Client/Server, Think Thin. Network Computing.www.networkcomputing.com/1013/1013f1.html.

Nec (2002). Network Market Trends. (WWW document)http:// www1n.mesh.ne.jp/cnpworld/english/solution/s01.html (accessed 10th December 2002).

Nortel Networks (2001). Storage Networking Solution. Data storage networking is key to business success.http://www.jiortel.com/Accessed on 12th November 2001.

Ochs, M., Pfahl, D., Chrobok-Diening, G and Nothhelfer-Kolb, B. (2001). A method for efficient measurement-based COTS assessment and selection method description and evaluation results, Proceedings of the seventh Symposium of Software Metrics, METRICS, 2001: 285–296.

Parkinson, C.N. (1955). Parkinson’s Law, The Economist, November 1955.

Precision Group (2002). http://precisionit.co.in/HomePage.html (accessed on 5th June 2002).

Pressman, R.S. (2001). Software Engineering: A Practitioner’s Approach, New York: McGraw-Hill.

Redman, B., Kirwin, B. and Berg, T. (1998). TCO: A Critical Tool for Managing IT. Gartner Group. http://www4.gartner.com/Init (accessed on 3rd August 2002).

Rocco, E. (2002). Benchmarking Hardware Service Operations. Gartner Group. http://www4.gartner.com/Init (accessed on 3rd August 2002).

Scheier, R.L. (2001). Scaling up for e-Commerce. Computerworld. (WWW document)http://www.computerworld.com/softwaretopics/software/appdev/ story/0,10801,59095,00.html (accessed 9th November 2004).

Schlegel, K. (2002). PC Prices Falling as Percentage of TCO. Meta Group. (WWW document)www.metagroup.com (accessed 3rd August 2002).

Sonderegger, P., Manning, H., Gardiner, K.M. and Dorsey, M. (2002). Best Practices For Web Site Reviews, Forrest Research. http://wwwl.forrester.com/ ER/Research/Report/Summary/0,1338,14594,FF.html (accessed on 9th November).

Vialta, R., Apte, C.V., Hellerstein, J.L., Ma, S. and Weiss, S.M. (2002). Predictive Algorithms in the Management of Computer Systems, IBM System Journal 41(3): 461–474.

Vijayan, J. (2001). The New TCO Metric. Computerworld (WWW document)http://www.computerworld.com/managementtopics/ management/story/0,10801,61374,00.html(accessed 9th November 2004).

Ward, J., O’Sullivan, M., Shahoumian, T. and Wilkes, J. (2002). Appia: Automatic storage area network fabric design, Proceedings of the Conference on File and Storage Technologies 203–217.

Willcocks, L. (1992). Evaluating Information Technology Investments: Research, Findings, and Reappraisal, Journal of Information Systems. 2: 243–268.

Yuan, R. and Strayer, W.T. (2001). Virtual Private Networks: Technologies and Solutions, Reading, MA: Addison Wesley.

Zachman, J.A. (1999). A Framework for Information System Architecture, IBM System Journal 26(3): 276–292.

## About the authors

Chiara Francalanci is an associate professor of information systems at Politecnico di Milano. She has a Master’s degree in Electronic Engineering from Politecnico di Milano, where she has also completed her Ph.D. in Computer Science. As part of her postdoctoral studies, she has worked for 2 years at the Harvard Business School as a Visiting Researcher. She has authored articles on the economics of information technology and on feasibility analyses of IT projects, consulted in the financial industry, both in Europe and the US, and is a member of the editorial board of the Journal $o f$ Information Technology.

cost minimization, quality of service, capacity planning and scalability.

Danilo Ardagna is a postdoc at Politecnico di Milano, where he also graduated in Computer Engineering in December 2000 and completed his Ph.D. in May 2004. He has worked for a 6-month period at IBM T.J. Watson Research Center in the System Optimization Department. His research interests include IT infrastructural design and

## Appendix A

Summary of technology requirements’ model variables Requirement variables have been summarized in Tables A1 and A2.

Table A1 Requirement variables and corresponding characteristics

<table><tr><td>Requirement variable</td><td>Symbol</td><td>Characteristics</td></tr><tr><td rowspan="4">Organization site Class of users</td><td> $S_i$ </td><td>type( $S_i$ ): it indicates whether  $S_i$  represents an organizational or an external site</td></tr><tr><td> $C_i$ </td><td>n( $C_i$ ): number of users in class  $C_i$ </td></tr><tr><td></td><td>think-time( $C_i$ ): average think time of users in class  $C_i$ , which can be either high or low</td></tr><tr><td></td><td>p( $C_i$ ): average percentage of concurrent users in class  $C_i$  that execute client applications</td></tr><tr><td rowspan="4">Application</td><td> $A_i$ </td><td>type( $A_i$ ): it indicates whether  $A_i$  represents a client, a server or an external application</td></tr><tr><td></td><td>D( $A_i$ ): required size of secondary memory</td></tr><tr><td></td><td>If type( $A_i$ ) = client, the following characteristics should be specified: MIPS( $A_i$ , OS): computing capacity needed to support the execution of application  $A_i$  on a client computer with operating system OS RAM( $A_i$ ,OS): primary memory needed to support the execution of application  $A_i$  on a client computer with operating system OS MIPS( $A_i$ , OS, RP, TT): computing capacity needed to support the execution of application  $A_i$  for a single user with think time TT, on a server computer with operating system OS and remote protocol RP Base-RAM( $A_i$ , OS, RP, TT): fixed amount of primary memory needed to support the execution of application  $A_i$  for users with think time TT, on a server computer with operating system OS and remote protocol RP User-RAM( $A_i$ , OS, RP, TT): per-user amount of primary memory needed to support the execution of application  $A_i$  for users with think time TT, on a server computer with operating system OS and remote protocol RP</td></tr><tr><td></td><td>If type( $A_i$ ) = server the following characteristics should be specified: tuning-system( $A_i$ ) = (OS, processor, disk): tuple of operating system OS, processor, and disk technology of the reference tuning system for application  $A_i$  Base-RAM( $A_i$ ): fixed amount of primary memory required to support the execution of application  $A_i$ </td></tr><tr><td>Request</td><td> $R_i$ </td><td>f( $R_i$ ): average frequency of request  $R_i$  for a single user or external application Server( $R_i$ ) =  $\{A_i\}$ : set of server applications involved in the execution of  $R_i$  Request-data( $R_i$ ,  $A_j$ ,  $A_k$ ): data exchanged from the triggering application  $A_j$  and the responding application  $A_k$  to support the execution of  $R_i$  Response-data( $R_i$ ,  $A_j$ ,  $A_k$ ): data exchange from the responding application  $A_k$  and the triggering application  $A_j$  to support the execution of  $R_i$  CPU-time( $R_i$ ,  $A_j$ ): CPU demanding time of server application  $A_j$  to support the execution of  $R_i$  on  $A_j$ &#x27;s tuning system Disk-time( $R_i$ ,  $A_j$ ): Disk demanding time of server application  $A_j$  to support the execution of  $R_i$  on  $A_j$ &#x27;s tuning system Request-RAM( $R_i$ ,  $A_j$ ): per-request amount of primary memory needed to support the execution of request  $R_i$  by application  $A_j$ </td></tr><tr><td>Database</td><td> $D_i$ </td><td>d( $D_i$ ): size of secondary memory required by database  $D_i$ </td></tr></table>

Table A2 Relationships among requirement variables

<table><tr><td>Relationship among requirement variables</td><td>Symbol</td><td>Characteristics</td></tr><tr><td>Location of user classes</td><td> $\{ (S_i, C_j) \}$ </td><td>Set of tuples  $(S_i, C_j)$  indicating that user class  $C_j$  is located at site  $S_i$ </td></tr><tr><td>Location of external applications</td><td> $\{ (S_i, A_j) | type(S_i) = external \land type(A_j) = external \}$ </td><td>Set of pairs  $(S_i, A_j)$  indicating that application  $A_j$  is located in site  $S_i$  where both  $S_i$  and  $A_j$  are external</td></tr><tr><td>Use of applications</td><td> $\Theta = \{ (A_i, C_j) \}$ </td><td>Set of pairs  $(A_i, C_j)$  indicating that application  $A_i$  is used by user class  $C_j$ </td></tr><tr><td>Concurrency among users of server applications</td><td> $\{ p(A_i, C_j) | type(A_i) = server \}$ </td><td>Set of average percentages of concurrent users of server application  $A_i$  in user class  $C_j$ </td></tr><tr><td>Data management</td><td> $\Delta = \{ (D_i, A_j) \}$ </td><td>Set of pairs  $(D_i, A_j)$  indicating that database  $D_i$  is managed by application  $A_j$ </td></tr></table>

## Appendix B

Summary of virtual computing resources and sizing rules

Requirement variables have been summarized in Tables A1 and A2.

Virtual computing resources summarized in Table B1.

Table B1 Virtual computing resources and sizing rules

<table><tr><td>Virtual component</td><td>Symbol</td><td>Association with technology requirements</td><td>Technical characteristics</td></tr><tr><td>Virtual server</td><td> $VS_i$ </td><td> $SA_i = \{A_j | type(A_j) = server\}$ , set of server applications executed by the virtual server  $VS_i$  $DA_i = \{D_k | \exists A_j \in SA_i: (D_k, A_j) \in \Delta\}$ , set of databases stored on the virtual server  $VS_i$ </td><td>Request load: $RL_i = \{R_h | \exists A_j \in SA_i: A_j \in Server(R_h)\}$ Primary memory: $RAM_i = \sum_{A_j \in SAi} Base - RAM(A_j)$  $+ \sum_{Ak \in SAi, Ak \in Server(Rj)} Request - RAM(R_j, A_k)$ Secondary memory: $Storage_i = \begin{cases} 0 & \text{if } VS_i \text{ is connected to a} \\ \sum_{Aj \in SAi} d(A_j) + \sum_{D_j \in DAi} d(D_j) & \text{otherwise} \end{cases}$ </td></tr><tr><td>Virtual thin server</td><td> $VTS_i$ </td><td> $UC_i = \{C_j\}$ , set of user classes supported by the virtual thin server  $VTS_i$  $RA_i = \{A_k | type(A_k) = client \exists C_j \in UC_i | (A_k, C_j) \in \Theta\}$ , set of client applications executed by the virtual thin server  $VTS_i$ </td><td>Computing capacity: $MIPS_i = \sum_{C_j \in UCi} n(C_j) \cdot p(C_j) \cdot \max_{Ak \in RAi \land (Ak, C_j) \in \Theta} (MIPS(A_k, OS, RP, think - time(C_j)))$ </td></tr></table>

Primary Memory:

$$
\begin{array}{l} R A M _ {i} = \sum_ {C j \in U C i} n (C _ {j}) \cdot p (C _ {j}) \cdot \\ \sum_ {A k \in R A i \wedge (A k, C j) \in \Theta} (B a s e - R A M (A _ {k}, O S, R P, t h i n k - t i m e (C _ {j})) \\ + U s e r - R A M (A _ {k}, O S, R P, t h i n k - t i m e (C _ {j}))) \end{array}
$$

Secondary memory:

Virtual VHFCS $U C _ { i } = \{ C _ { j } \} ,$ set of user classes HFC server supported by the virtual HFC server VHFCS $R A _ { i } = \left\{ A _ { k } \right| { \mathrm { t y p e } } ( A _ { k } ) = { \mathrm { c l i e n t } }$ $\wedge \ \exists C _ { j } \in { \cal { \dot { U } } } C _ { i } { \dot { \big | } } \ { \mathrm { \hat { ( } } A _ { k } , \ C _ { j } \mathrm { ) } } \in \Theta$ $\land A _ { k } \not \in P C ( C _ { j } ) \}$ , set of client applications executed by the virtual HFC server $\mathrm { { V H F C S } } _ { i }$

$$
\text { Storage } _ {i} = \sum_ {A j \in R A i} d (A _ {j})
$$

Virtual fat $\mathrm { { V F C } } _ { i }$ $C _ { j } { \mathrm { : } }$ user class of the user client supported by the virtual fat client $\mathrm { { V F C } } _ { i }$ $L A _ { i } { = } \{ A _ { k } | \mathrm { t y p e } ( A _ { k } ) { = } { \mathrm { c l i e n t ~ } } \land$ $( A _ { k } , C _ { j } ) \in \tilde { \Theta } \}$ , set of all client applications used by the user class $C _ { j }$

Computing capacity:

Primary memory:

$$
\begin{array}{l} M I P S _ {i} = \sum_ {C j \in U C i} n (C _ {j}) \cdot p (C _ {j}) \cdot \\ \max _ {A k \in R A S i \wedge (A k, C j) \in \Theta} \left(M I P S (A _ {k}, O S, R P, t h i n k - t i m e (C _ {j}))\right) \end{array}
$$

Secondary memory:

$$
\begin{array}{l} R A M _ {i} = \sum_ {C j \in U C i} n (C _ {j}) \cdot p (C _ {j}) \cdot \\ \sum_ {A k \in R A i \wedge (A k, C j) \in \Theta} (B a s e - R A M (A _ {k}, O S, R P, t h i n k - t i m e (C _ {j})) \\ + U s e r - R A M (A _ {k}, O S, R P, t h i n k - t i m e (C _ {j}))) \end{array}
$$

$$
\text { Storage } _ {i} = \sum_ {A j \in R A i} d (A _ {j})
$$

Computing capacity:

$$
M I P S _ {i} = \max _ {A k \in L A i} (M I P S (A _ {k}, O S))
$$

Primary memory:

$$
R A M _ {i} = \sum_ {A k \in L A i} R A M (A _ {k}, O S)
$$

Secondary memory:

$$
\text { Storage } _ {i} = \sum_ {A k \in L A i} d (A _ {k})
$$

Table B1 Continued

<table><tr><td>Virtual component</td><td>Symbol</td><td>Association with technology requirements</td><td>Technical characteristics</td></tr><tr><td>Virtual HFC</td><td> $VHFC_i$ </td><td> $C_j$ : user class supported by  $VHFC_i$  $LA_i = \{A_k | type(A_k) = client \land (A_k, C_j) \in \Theta \land A_k \notin Server(C_j)\}$ , set of locally executed client applications</td><td>Computing capacity: $MIPS_i = \max_{Ak \in LAi} (MIPS(A_k, OS))$ Primary memory: $RAM_i = \sum_{Ak \in LAi} RAM(A_k, OS)$ Secondary memory: $Storage_i = \sum_{Ak \in LAi} d(A_k)$ </td></tr><tr><td>Virtual SAN</td><td> $VSAN_i$ </td><td> $S_j$ : site where the virtual SAN is installed $SA_i = \{A_j | type(A_j) = server\}$ , set of server applications supported by the virtual SAN  $VSAN_i$ </td><td> $Storage_i = \sum_{Aj \in SAi} d(A_j) + \sum_{(Dj, Ak) \in \Delta, Ak \in SAi} d(D_j)$ </td></tr></table>
