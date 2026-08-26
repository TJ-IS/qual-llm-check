---
otero_id: 26489
otero_key: "H2JFGQXE"
title: "Decentralized Mechanism Design for Supply Chain Organizations Using an Auction Market"
authors: "Ming Fan; Jan Stallaert; Andrew B. Whinston"
year: "2003"
journal: "Information Systems Research"
doi: "10.1287/isre.14.1.1.14763"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/H2JFGQXE/fulltext/images/de8cfd347f3ba3594e8af8105ce93584709202fbd758f885ac81adacdcea678b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Decentralized Mechanism Design for Supply Chain Organizations Using an Auction Market

Ming Fan, Jan Stallaert, Andrew B. Whinston,

To cite this article:

Ming Fan, Jan Stallaert, Andrew B. Whinston, (2003) Decentralized Mechanism Design for Supply Chain Organizations Using an Auction Market. Information Systems Research 14(1):1-22. http://dx.doi.org/10.1287/isre.14.1.1.14763

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2003 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/H2JFGQXE/fulltext/images/5be4af98f3d3a41bd5610ee7eae037a71bc337f0d879620cc3bfa0e41f7eae02.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Decentralized Mechanism Design for Supply Chain Organizations Using an Auction Market

Ming Fan • Jan Stallaert • Andrew B. Whinston

Management Science Department, University of Washington Business School, Seattle, Washington 98195

Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, Connecticut 06269

Center for Research in Electronic Commerce, Department of Management Science and Information Systems,

University of Texas at Austin, Austin, Texas 78712

mfan@u.washington.edu • stallaert@sba.uconn.edu • abw@uts.cc.utexas.edu

raditional development of large-scale information systems is based on centralized information processing and decision making. With increasing competition, shorter product life-cycle, and growing uncertainties in the marketplace, centralized systems are inadequate in processing information that grows at an explosive rate and are unable to make quick responses to real-world situations. Introducing a decentralized information system in an organization is a challenging task. It is often intertwined with other organizational processes. The goal of this research is to outline a new approach in developing a supply chain information system with a decentralized decision making process. Particularly, we study the incentive structure in the decentralized organization and design a market-based coordination system that is incentive aligned, i.e., it gives the participants the incentives to act in a manner that is beneficial to the overall system. We also prove that the system monotonically improves the overall organizational performance and is goal congruent.

(Decentralized Information System; Coordination Mechanism; Incentive; Auction; Complementarity; Supply Chain)

## 1. Introduction

Information technology (IT), especially the recent explosive growth of the Internet and electronic commerce, has a profound impact on how businesses are organized. How IT affects organization structure and design is one of the most important frontiers of current Information Systems (IS) research (Bakos and Kemerer 1992, Nault 1998). One key issue to improve organizational efficiency is to bring information and decision rights together (Hayek 1945, Nault 1998). Brynjolfsson and Mendelson (1993) suggested two approaches to colocate information and decision rights: (1) the MIS solution, which transfers the information required for the decision to the decision makers using information systems, and (2) the organization redesign solution, which requires the redesign of organizational structure so that the decision making authority is where the pertinent information is. The MIS solution is usually associated with centralization. There are certain limitations for this approach because IT can reduce the cost to transfer general knowledge, such as data, but has done little to improve the transfer of more specific knowledge such as analytical skills and problem solving capabilities. As the marketplace becomes increasingly uncertain and requires quick responses, it has become impossible for a centralized organization with limited information processing capability at the top of the hierarchy to keep up with the explosive growth of information. Firms try to push down decision rights to lower levels to improve performance and encourage innovation (King 1983).

The purpose of this research is to design a decentralized information system that supports decentralized decision making in a supply chain organization. We realize that introducing a new information system in an organization is often intertwined with the organization design process. The growing use of IT in organizations is both a cause and an effect of the organization’s transition to new organizational structures (Brynjolfsson and Mendelson 1993). Modern computer and communication technologies, the Internet, and electronic marketplace innovations are the catalyst of the changes of organizational structures and processes. Meanwhile, an organization that promotes crossfunctional teamwork and decentralized decision making requires a compatible information system to support the ever-growing needs of organizational communication and coordination.

Introducing a decentralized information system deeply affects how different subunits or agents<sup>1</sup> in an organization interact and coordinate with each other. The study of coordination has been a growing area across different disciplines including organization theory, economics, computer science, and IS (Mintzberg 1979, Malone and Crowston 1994, Anand and Mendelson 1997, Sikora and Shaw 1998). Coordination is the process that manages interdependencies among activities. The concept of coordination has not been incorporated in information system design until recently. As the cost of communication is being significantly reduced, the framework of computer system design is shifting from computing to communication. A growing function of information systems today is to allow people across the organization to share information and coordinate their respective activities. The latest innovations of information systems such as electronic mail, computer conferencing, groupware, group decision making systems, and collaborative authoring systems are essentially tools that coordinate complex activities in organizations (Winograd and Flores 1986, DeSanctis and

Gallupe 1987, Ellis et al. 1991, Orlikowski and Hofman 1997).

One of the most challenging problems in using information systems to coordinate organizational activities is that some data necessary for making decisions are not objectively verifiable and require expert knowledge to get accurate estimates. For instance, annual production plans need estimates about future projected sales and customer demands, commodity prices, transportation costs, etc. Managers, if asked, may have incentives to misrepresent information about such figures. As an example (Honczarenko 1993), a national candy manufacturer observed that the sales forecasts submitted by the marketing department consistently overestimated actual sales because they always overestimated the effectiveness of their planned marketing campaigns. By submitting low sales forecasts, the marketing department would acknowledge that the effect of their campaign would be substandard. If the figures submitted by the marketing department were actually used for decision making, the resulting decision would be flawed.

In a decentralized organization, the requirement to provide information system users the right incentives to truthfully reveal their knowledge is called the incentive alignment problem (Ba et al. 2001). It is our objective here to design a decentralized information system that is incentive aligned for making decisions in supply chains. Demonstrating incentive alignment amounts to showing that (i) the system will yield a solution equivalent to the one obtained by a well-established model that by itself may not satisfy the requirements of incentive alignment, and (ii) the decision makers who participate in the decision making are provided the right incentive to truthfully reveal their knowledge. The well-established model we use for solving supply chain problems is a linear programming (LP) model, or more precisely, a multicommodity network flow problem (MCNFP). We use such a model because of the frequent reports of success with this approach in the literature (Geoffrion and Graves 1974, Brown et al. 1987, Dogan and Goetschalckx 1999). Hence, the procedure we propose will use the MCNFP model as a benchmark, but we do not intend to create a new operational research (OR) tool or algorithm. New OR algorithms are evaluated based on speed, memory requirements, or problem sizes that are solvable, assuming that all input data are given and correct, i.e., objectively observable. Our procedure is independent of the latter assumption, which in practice is often violated. It is possible that sacrifices (e.g., in solution speed) will have to be made when it comes to evaluating our method from a pure OR standpoint. However, the main contribution of this research is on the issues of incentive alignment, which are absent in the OR literature and are important IS research problems. Because the MCNFP model is an accurate representation of the activities in a supply chain provided that the input data are correct, we evaluate the decisions and actions in the decentralized information system in light of the model. Therefore, the analysis will sometimes draw upon LP theory; but the technical details are moved to the appendix.

This paper presents a methodological design of a market-based coordination system for a distributed information system. The decentralized organization design and information structure follows the decomposition of the MCNFP model. Hence, each individual agent’s incentive is clearly defined. The resourceallocation process in the organization is coordinated through a bundle auction, or combinational auction— a market where organizational resources can be auctioned simultaneously. Using this mechanism, multiple resources with complementarities can be allocated to agents who have the highest valuations for those bundles of resources and the collective behavior of business units is proven to be congruent with the goal of the overall organization.

The rest of the paper is organized as follows. In §2, we review prior literature and outline our research motivations and contributions. Section 3 provides the design model of a decentralized supply chain organization and analyzes the distributed decision problems facing each agent. In §4, we discuss the design of the auction market, which serves as the coordination mechanism for the organization. Section 5 analyzes the performance of the overall system. Section 6 discusses the limitations and extensions.

## 2. Prior Literature and Research Motivation

Organization structure and its information processing capacity are areas actively studied in organization theory, economics, and recent IS research. Organizations have been frequently modeled as primarily information processing institutions (Galbraith 1973, Hayek 1945). According to Galbraith (1973), the greater the uncertainty, the greater the amount of information that has to be processed between decision makers during its execution. A traditional organization is defined as a hierarchy with goals, rules, programs, and formal procedures. But as uncertainties increase, a hierarchical structure becomes overloaded and its performance is reduced. Therefore, it requires the organization to employ new design strategies. Galbraith suggested several design strategies: (1) create slack resources, (2) create self-contained tasks, (3) invest in vertical information systems, and (4) create lateral relations. The first and second strategies can be regarded as ways to reduce the need for information processing. Strategies (3) and (4) are approaches similar to the MIS solution and organization redesign solution discussed earlier, and both require increased use of IT in organizations. The basic problem is to create an organization structure that matches the demand for information processing with the information processing capability. If a company’s overall strategy involves introducing new products, entering new markets, then its information processing ability should be increased. Lateral mechanisms such as direct contact, liaison, and teams are organization-design innovations that can move decisions down toward the points of information origin and improve organization performance (Galbraith 1973, Mintzberg 1979, Nadler and Tushman 1988).

Economists have contributed to the understanding of organizations by studying the incentive problem. Adverse selection and moral hazard are two examples of the incentive problem (Akerlof 1970). In the former case, different units in an organization have their own objectives and may choose to hide or misrepresent their private information if they can be better off in doing so. In the latter case, different units may choose to act differently from their defined goals because it is often difficult to verify whether those units have fulfilled their obligations. For example, a division executive may adopt policies that lead to high current performance that will be rewarded by bonuses and promotions, even though these policies will ultimately hurt the long-term profitability of the division (Milgrom and Roberts 1992).

In the 1990s, IS researchers studied business process redesign (BPR), also known as reengineering or process innovation (Davenport and Short 1990, Davenport 1993). BPR involves radical change in a company and has enabled an organization to realize radical process improvements using IT. Many studies show IT is both a strategic catalyst and an enabler of BPR. IT is usually a necessary but insufficient factor in achieving business process redesign. Successful reengineering projects stress the importance of a partnership between IS and business managers because organizational issues including changes to structure, training, role definition, and culture, must facilitate a new process (Davenport and Stoddard 1994, Stoddard and Jarvenpaa 1995). The recent implementation experiences of enterprise systems, or enterprise resource planning (ERP) system, reconfirm that point. To a large degree, enterprise systems follow simple design rules such as a maximum integration of information flows and standardization (Davenport 1998). These systems are more consistent with firms that have centralized, hierarchical structures and uniform cultures. But for some companies that are operating in fast-moving markets and in different geographical regions in the world, they may want to introduce a new information system to break down hierarchical structures and make their workforce more responsible and innovative (Fan et al. 2000). How do these IT implementation lessons affect the design philosophy and methodology of information systems? What are the principles an information system design should follow to facilitate organizational changes? How should one reengineer a decision making process so that it mirrors the decentralized governance structure found in practical supply chains? What are the requirements that guarantee coordinated decisions? These are the issues that are still unclear and are the motivation for this research.

The two key determinants of using IT in organizations, particularly the issue of introducing a new information system, are the firm’s information structure and its decision makers’ incentives. While organization theorists have studied the first issue and stress the importance of aligning a firm’s information processing capacity with its information processing, economists focus on incentive problems in organizations. Our research centers on the interactions of these two determinants and their joint effects. First of all, introducing a new information system has a tremendous impact on an existing organization. It is important that the design of an information system considers the potential organization impact. For example, while enterprise systems may be suitable for organizations with hierarchical structures, studies have shown that decentralized information processing and decision making are valuable for organizations that have to deal with multiple markets and local knowledge is indispensable in the decision making process (Anand and Mendelson 1997, Davenport 1998). In those situations, it becomes costly and nearly impossible for a hierarchical organization to gather and communicate timely information from the local office to the central headquarters (Tan and Harker 1999).

Second, creating a new information structure is inseparable with the task of designing a new incentive system for its users. One of the major problems in a decentralized organization is that the goals of the agents are not aligned with the overall goal of the organization (Dirickx and Jennergren 1979, Milgrom and Roberts 1992). Different business subunits have their own objectives. To pursue their private interests, these units may choose to send false, or biased, information to headquarters and other departments (Jennergren and Muller 1973). For example, in a manufacturing firm, the sales department, which is rewarded for its sales volume, may inflate the demand to induce the operations division to over-produce to a certain extent in case the demand will increase. On the other hand, the operations division may under-report its capacity to inflate production costs because a lower production plan is easy to accomplish. Both cases may benefit individual departments but will hurt the overall profitability of the firm. Therefore, designing the right incentive system to coordinate the behavior of the agents, who have different objective functions, is equally crucial as the organization’s information structure changes. One important, desirable feature of a decentralized system is incentive compatibility (Hurwicz 1973), or incentive alignment as mentioned earlier. It is such a configuration that all agents find it is to their own best interests to tell the truth. Another measure of an efficient system design is goal congruence. Milgrom and Roberts (1992) define goal congruence as a situation in which the objectives of the organization and its individuals are aligned so that they pursue common goals.

We see electronic markets powered by the Internet and World Wide Web (WWW) as a catalyst for further process improvement in organizations. Malone et al. (1987) suggest that as the cost of communication goes down by growing use of IT, markets become a superior coordination mechanism compared to hierarchies. There is some evidence that growing use of IT has led to smaller firms (Brynjolfsson et al. 1994). Recently, we’ve seen the creation of electronic markets where manufacturing capacity can be traded (Capacityweb. com 2000) and plants put up their excess capacity for auction. Now, firms not only have created electronic markets to connect directly with their customers and business partners, but also begin to use internal markets and pricing to coordinate their internal operations and services (Halal 1993). In the past, companies often mandated the use of internal providers. But some internal providers today must compete for another division’s business, offer their services at market rates, and even make a profit while doing so. For example, at Merck’s R&D unit, individual project managers must attract and bid for the talent to staff the projects. Resource allocation is decentralized to users, professionals, and project managers rather than determined by a management-led decision process (Galbraith and Lawler 1993). Essentially, the indepen dent units function autonomously as profit centers. The services or intermediate/finished goods they provide are sold to the units downstream while the units are responsible for the costs associated with their production. They eventually get rewarded for how “lean” they operate. This “internal economy” can function with real dollars or with an artificially created internal currency. Electronic markets with novel mechanisms for internal organizations are not a researcher’s dream any more. For example, starting in the 1990s, Sears Logistics Services (SLS), a subsidiary of Sears, Roebuck and Co., implemented a combined-value-auction market to allocate services to its carriers. SLS manages logistics for different companies that require transporting products from manufacturer plants to distribution centers and retail stores. The combined value market allows a carrier to offer a single price for multiple-route services, e.g., \$1 million for the service of both Chicago-St. Louis and St. Louis-Los Angeles lanes. The idea behind the market is to encourage a carrier to consolidate its services and generate cost savings. The initial auction would involve 854 lanes throughout the country with a service cost of approximately \$190 million per year. The combined value auction that was implemented reduced the cost to \$165 million per year (Ledyard et al. 2002). Recently, software and consulting companies, such as i2 Technologies and Charles River Associates (CRA) are active in developing electronic marketplace solutions that use novel market mechanisms for businesses (i2 Technologies 2000, CRA 1998).

Developing novel electronic markets to improve current organizational processes is an important research area (Malone and Crowston 1994). A critical item on the research agenda is to create, identify, and analyze alternative coordination processes. One of the major tools that can be employed to study the problem is to develop formal models of coordination processes and analyze their effectiveness. This approach is especially valuable when empirical data are not available.

The purpose of this research is to design a decentralized, market-based coordination mechanism to improve information processing and decision marking for supply chain organizations that operate in fast moving markets with short product cycles. We will describe the design principles of such a system and theoretically prove to what extent the aforementioned criteria are satisfied. The following are the goals of the research:

• Develop an organizational model that clearly maps the overall objective function of the organization to a series of subgoals for agents. In this way, we can study the incentives of the agents and evaluate the performance of the decentralized system.

• Design a robust market-based mechanism to coordinate resource allocation and decision making among agents. We want to make sure this mechanism is goal congruent and encourages truth telling.

• The model enables actual implementation and experimentation. This is the reason the design of the decentralized organization is based on a more realistic operational model.

## 3. Decentralized Supply Chain Organization Design

In this section, we first present the basic model of a supply chain organization. Then, we outline how the centralized model can be decomposed into pieces. These pieces can be solved by individual decision makers myopically, i.e., without considering the impact of their actions on the rest of the supply chain. We present the local decision problem that an agent faces and outline the solutions.

## Background

A global supply chain organization is a world-wide network of suppliers, manufacturing facilities, warehouses, distribution centers, and transportation systems that transforms raw materials into final products and delivers them into the hands of millions of consumers (Figure 1). We model a supply chain problem following a multicommodity network flow problem (MCNFP). The model of MCNFP arises in a wide variety of important applications. Many logistics, manufacturing, and transportation problems can be formulated as large MCNFPs (Ahuja et al. 1993). It is usually presented as having the following form:

## Problem O

$$
\min _ {x \geq 0} c x,
$$

such that

$$
A x \leq h\tag{1}
$$

$$
B x \leq S,\tag{2}
$$

Figure 1 A Global Supply Chain  
![](/api/attachments/H2JFGQXE/fulltext/images/16ffee71326bfa91a4db39a5a7aa306db06dcfd1148aace004770ea12dee1c0a.jpg)

where the objective function is to minimize costs. The network constraints $( 1 ) , A x \leq h ,$ ensure that supply, demand, and shipping-route requirements are met for each commodity. The model assigns a separate network flow for each commodity. The network part of the problem can be decomposed into K disjoint networks, where K is the number of commodities. The matrix A then has the form

$$
A = \left[ \begin{array}{c c c c} A _ {1} & & & \\ & A _ {2} & & \\ & & \ddots & \\ & & & A _ {K} \end{array} \right],
$$

where $A _ { k }$ is the network for the kth commodity. A commodity can be a raw material, intermediate good or subassembly, or a final good. Constraints (2) are the joint capacitation constraints that limit the total amount of flow between certain origin-destination pairs. These joint capacitation constraints describe the limitations of inventory-storage, loading dock, or trucks and railroad cars that are shared among various commodities. The vector $\boldsymbol { S } = ( S _ { 1 } , . . . , S _ { m } , . . . , S _ { M } ) ^ { T }$ denotes the resource constraint in the supply chain. It should be noted that the available capacity of these shared resources is not necessarily exogenously given and the MCNFP allows for a very flexible supply chain model. For example, in Figure 1, there are two subassembly operations and one final assembly, i.e., there are three “product networks,” and the outputs of the two subassembly networks become the input of the final assembly. So, the subassembly components become shared resources, created in the subassembly part of the network and “consumed” in the final assembly stage. The creation of such a “shared resource” m in the system is modeled by setting $b _ { m k } = - 1$ in all networks $( \mathrm { e . g . }$ different facilities) that create the subassembly and $b _ { m k } > 0$ for the networks that use the subassembly, with the right-hand side $S _ { m } = 0 .$ . There will be a network for every subassembly component expressing its flow through the subassembly plant, and a separate network for the final assembly of the product in the final assembly stage. The different networks are linked by the constraints in constraint set (3.2). More details of how to formulate supply chain problems as multicommodity flow problems can be found in Brown et al. (1987) and McBride (1998).

Problem O represents a centralized information processing and decision making. In a global supply chain, the model includes factors such as production and distribution capacities at different locations, production and distribution flows, operational costs, and consumer demand. The output of the production should be the input for the distribution process, and the input for the transshipment process should equal the output. Meanwhile, different operational processes may share common facilities or resources.

Early applications of the MCNFP in manufacturing and distribution started in the 1970s. In their seminal work, Geoffrion and Graves (1974) introduced a multicommodity logistics network design model for optimizing annualized finished product flows from factories and vendors via distribution centers (DC) to customers. Brown et al. (1987) developed a MCNFP for Nabisco to manage complex problems involving facility selection, equipment utilization, and manufacturing and distribution of various products. Practitioners now have to deal with extremely large MCNFPs with more than 600,000 constraints and seven million variables for large-scale practical production and logistic problems (McBride 1998). The common drawbacks of the existing solutions are that they are all centralized solutions. Divisions or agents do not participate in the decision making process. Instead, they relinquish their decision authority to the algorithm at the headquarters. Solving the centralized optimization problem provides the first-best solution for the organization if we assume all the information for the model is available and accurate. But that assumption rarely holds.

## The Centralized Model

Here we introduce an expanded version of the MCNFP so that it can easily be broken up into smaller decision problems. The setup of the supply chain is as follows:

• The supply chain is composed of production (possibly with subassemblies) and distribution networks with multiple nodes (e.g., manufacturing facilities and DCs) and arcs (e.g., transportation routes and modes).

• The supply chain has M “shared” resources, which could either be raw materials, intermediate parts, machines, or production and distribution facilities.

• The vector x from Problem O is partitioned as $x =$ $( x _ { 1 } , \ldots , x _ { k } , \ldots , x _ { K } )$ , which represents the decision variables for the whole supply chain. Agent k has the control over $x _ { k } \in \Re ^ { L _ { k } }$ with $L _ { k }$ the number of decision variables agent k controls. Every $x _ { k }$ is a vector that expresses the decisions within one network.<sup>2</sup>

• A supply chain activity $b _ { k }$ is a vector of technological coefficients $b _ { k } = ( b _ { 1 k } , \ldots , b _ { m k } , \ldots , b _ { M k } ) ^ { T } , b _ { m k } \geq$ $0 , m = 1 , \ldots , M .$ . The $b _ { k }$ denotes the amount of resource k required to produce or distribute one unit of product k. We write $B _ { k } = [ b _ { k } ^ { j } ] , j = 1 , \ldots , L _ { k }$ as the matrix containing all columns for the activities under the control of agent k.

• There are penalties for both backlogs and shortages. q (k(x)) is the penalty function, where q is the penalty and k is the violation from the target. The penalty function is assumed convex and can be piecewise linear, which means the more severe the violation the higher the per-unit penalty.

The overall planning model for the supply chain is the following Problem C:

## Problem C

$$
\min C = \sum_ {k = 1} ^ {K} (c _ {k} x _ {k} + \rho_ {k} \lambda_ {k}),
$$

such that

$$
A _ {k} x _ {k} - \lambda_ {k} \leq h _ {k}, k = 1, \ldots , K,\tag{3}
$$

$$
\sum_ {k = 1} ^ {K} B _ {k} x _ {k} \leq S,\tag{4}
$$

$$
x _ {k} \geq 0, k = 1, \dots , K,\tag{5}
$$

where the objective function is to minimize the total cost (C), which comprises the cost of production and/ or distribution (c), and the penalty (q). The first set of constraints (3) ensures that demand at destination nodes is met and that shipment-in equals shipmentout at transshipment nodes. If these conditions are not met, there will be a shortage $\lambda _ { k } .$ , which results in a penalty of $\rho _ { k } \lambda _ { k }$ . The $A _ { k }$ denotes the relationship in commodity flows in the supply chain network. Every row in a node-arc incidence matrix corresponds to a node in the network. The matrix $B _ { k }$ contains the technological coefficients of the supply chain activities.

## The Decentralized Model

For a linear system, there are two known methods that decompose the optimization problem: dual and primal decomposition. Decomposition techniques have originated as algorithms to solve large-scale linear programming problems. Although they have strong implications in decentralized organizational design, there are practical problems when using them to implement decentralized information systems (Dirickx and Jennergren 1979). In dual decomposition, also referred as Dantzig-Wolfe decomposition (Dantzig and Wolfe 1960), the headquarters set prices on the common resources that have to be shared by multiple divisions. Each division then develops a corresponding production plan, optimized with respect to its individual objective function, and thus determines the optimal way of using these resources, given all other local restrictions (e.g., the production technology, availability of local resources, etc.). Then, the headquarters collect information from all the divisions and update the prices so as to globally optimize the usage of the common resources. For the resources with an excess demand, the prices are increased, while the prices will decrease for resources with excess supply. However, the optimal solution for the divisions is a mix—dictated by the headquarters— of a set of proposed plans, limiting the practical use of the technique.

Primal decomposition, also called Benders decomposition (Benders 1962), divides the overall problem into a set of subproblems. Under primal decomposition, the headquarters decide the initial allocation of shared resources between divisions. Then, divisions find their best solutions by solving the local problems and supply the shadow prices (marginal costs) for the common resources to the headquarters. The headquarters collect all price information and send back updated resource allocation through iterative information exchanges with the divisions. The primal decomposition has some very desirable properties in terms of implementation (Brown et al. 1987). At the end of each iteration, the resulting decisions are feasible but not necessarily optimal. Therefore, the iterative information exchange could be terminated before an optimal solution is found, and a feasible plan would still be available. This is important for a real-time decision problem in which a near-optimal solution has to be found within a certain time limit. But headquarters dictate the resource allocation, and hence divisions have every incentive to misrepresent shadow prices to obtain their desired resource allocation. Jennergren and Muller (1973) showed that it was possible and advantageous for a given subunit to cheat, assuming all other subunits do not cheat, following the decomposition approach.

In this research, we use an auction-based market instead of the classical decomposition algorithm as a computing system to coordinate the resource-allocation process. It has many advantages. First, a marketoriented approach is more flexible and has better adaptability and scalability than the decomposition algorithm (Hinkkanen et al. 1997). In a market system, the setup cost for the arrival of a new agent is low. A new business division can easily gain access to the market and buy and sell resources. In contrast, using a decomposition algorithm, a proprietary communication protocol has to be set up between the division and the headquarters. As agents enter or leave the supply chain, the whole system has to be reconfigured. Second, information is disseminated more efficiently in a market system where spot and futures prices are available to all agents. Collectively, these prices contain crucial information about the supply chain, including the demand, facility usage, and bottlenecks. Divisions and agents can extract information reflected in resource prices. More importantly, coordination mechanisms could be designed in a market to encourage agents to submit their true valuations to the market.

To do so, we can break the constraints of Problem C into a master problem and multiple subproblems. We denote by the vector $s _ { k } \in \Re ^ { M }$ the resource availability for agent k. Problem C is the equivalent to the following problem:

Problem H

$$
\min \sum_ {k = 1} ^ {K} C _ {k} ^ {*} (s _ {k}),
$$

subject to

$$
\sum_ {k = 1} ^ {K} s _ {m k} \leq S _ {m}, m = 1, \dots , M,\tag{6}
$$

where $s _ { m k } ( m = 1 , \ldots M )$ is the capacity of resource m preallocated resource to agent k and $C _ { k } ^ { * } ( s _ { k } )$ is the optimal value of Problem K defined below. The master problem minimizes the overall cost of the supply chain with a set of organizational resource constraints. Every subproblem is solved with the current allocation of resources given, which is essentially a primal decomposition approach. But, our master problem will not be a dual or primal master problem. Instead, we will introduce a market-based solution to reallocate shared resources, which will be discussed in detail later.

Each individual agent’s subproblem is

## Problem K

$$
C _ {k} ^ {*} (s _ {k}) = \min c _ {k} x _ {k} + \rho_ {k} \lambda_ {k},
$$

subject to

$$
A _ {k} x _ {k} - \lambda_ {k} \leq h _ {k},\tag{7}
$$

$$
B _ {k} x _ {k} \leq s _ {k},\tag{8}
$$

$$
x _ {k} \geq 0,\tag{9}
$$

where the vector $s _ { k }$ represents the allocated resources to agent k (Equation 8) and $B _ { k } x _ { k }$ are the resources required for the agent.

## The Agent’s Decision Problem

Under our new organizational structure, the headquarters are no longer responsible for allocating common resources (as in primal decomposition) to minimize the total production costs, but merely run a market of shared resources where sell and buy orders are traded. Individual divisions or agents first solve their individual optimization problems and then construct “bundle orders” for shared resources to be submitted to the market.

To find these trade orders for resources using the decentralized approach, we first analyze each agent’s problem (Problem K). The following proposition states in what proportion the shared resources can be used such that there is no waste. The space of all possible wasteless uses of the resources is called the efficient operation set.

Proposition 1. Assume that agent k manages product k by operating activities $B _ { k } = ( b _ { k } ^ { 1 } , \ldots , b _ { k } ^ { j } , \ldots , b _ { k } ^ { L _ { k } } )$ Then. the efficient operation set for the agent k is

$$
\Phi_ {k} = \{s _ {k} ^ {*}: s _ {k} ^ {*} = B _ {k} \varphi , \forall \varphi \in \Re_ {+} ^ {L _ {k}} \}\tag{10}
$$

and $\varPhi _ { k }$ is a polyhedral cone spanned by the rays of the activities $\{ b _ { k } ^ { 1 } , \ldots , b _ { k } ^ { j } , \ldots , b _ { k } ^ { L _ { k } } )$

Proposition 1 formally states that the efficient input of resources for an agent should be in proportion with the technological coefficients defined in the agent’s activity model. Hence, when an agent requires resources $s _ { m } , m = 1 , \ldots , M ,$ they should be expressible as a mix of resource requirements for the optimal product mix that the agent produces. Let us look at two activities with two input resources. Figure 2 shows the unit isoquant of the agent as the set $\{ ( s _ { 1 } , s _ { 2 } ) \colon x = \operatorname* { m i n } ( s _ { 1 } , s _ { 2 } /$ $2 ) \ : = 1 \}$ . The efficient operation set for Activity 1 is on the ray: $s _ { 2 } = 2 s _ { 1 } ( s _ { 1 } \geq 0 , s _ { 2 } \geq 0 )$ , for Activity $2$ it is on the ray $\begin{array} { r } { s _ { 2 } = \frac { 1 } { 2 } s _ { 1 } ( s _ { 1 } \geq 0 , s _ { 2 } \geq 0 ) } \end{array}$ . Every product mix that lies in the cone spanned by the two activity rays is in the efficient operation set.

Figure 3 shows a feasible operation set for our example with fixed resource availabilities $( \bar { s } _ { 1 } , \ \bar { s } _ { 2 } )$ . The cone representing the efficient operation set is now a polyhedron because it is bounded by the hypercube $( \bar { s } _ { 1 } , \bar { s } _ { 2 } )$ and the constraint set (7), which is shown here in thick solid lines.

Definition. A resource allocation s¯ is said to be optimal for a production plan $x ^ { * } i f$ there does not exist another $\bar { s } ^ { \prime } \leq$ s¯ with $\bar { s } \ne \bar { s } ^ { \prime }$ that still supports the plan $x ^ { * }$

Figure 2 The Unit Isoquant of Two Activities Without Resource Substitutions  
![](/api/attachments/H2JFGQXE/fulltext/images/05ea7b3aad570761c61c8d00e609c741b17c67b50cdad2d59a2429db6d0e35d4.jpg)

![](/api/attachments/H2JFGQXE/fulltext/images/e414d74031f94c2ebe726d1174c24d53a12060f426fde9dd396a310b4fe4c2b8.jpg)

Proposition 2. Let $x _ { k } ^ { * } ( s _ { k } )$ be the optimal solution to Problem K. Then the current allocation $s _ { k }$ is optimal for $x _ { k } ^ { * }$ if and only if $B _ { k } x _ { k } ^ { * } = s _ { k }$

Proposition 2 follows directly from the definition of an optimal resource allocation, and is merely a restatement of it. It says that the optimal solution is efficient only if it does not waste any of the acquired resources. Depending on the cost coefficients and the penalties, a different operational plan $x ^ { * }$ will be chosen by the agent. In our example (Figure 2), there are five possible outcomes when solving Problem K: A, B, C, D, and E. Only point C corresponds to an optimal resource usage point. Points B and D both have slack of one resource (respectively, Resource 1 and 2), and points A and E have slack of both resources. Point F is a production plan that is not feasible with respect to constraint set (Equation 7), and thus violates a target, i.e., $\lambda \geq 0$ for that constraint. Note that point $G ,$ although feasible with respect to constraint set (7) cannot be an outcome of solving Problem K with the current resource allocations.

Solving for $x _ { k } ^ { * } ( s _ { k } )$ amounts to solving a simple linear program. Proposition 2 states that if the allocation $s _ { k }$ is not optimal, then there is slack equal to the amount $s _ { k ^ { - } }$ $B _ { k } x _ { k } ^ { * }$ . The slack for those resources can be sold by the agent that acquired them. The valuation for the slack resources is zero because the agent can still maintain the same production plan. Every positive price the agent can get for their sale will make him better off.

Proposition 2 shows how slack resources can be sold without changing the production level $x ^ { * }$ when a resource allocation is not optimal. The next question is how does the agent acquire shared resources, and what is the maximum price he is willing to pay for them when his current allocation is optimal. The motivation for doing that is agents will make a gain if the desired resource combination can indeed be traded with prices that are better than the maximum reservation price of the agent. This will result in a different resource availability and will thus affect the current production plan $x ^ { * } ,$ . First, we have to determine the weights, or bundle composition, of the different resources. Then we will define a method for agents to value their resource combinations, i.e., what is the break-even point such that the agent is indifferent between selling off the resources and incurring a higher production cost. Let $C _ { k } ^ { * } ( s )$ be the optimal value of the cost function of agent k when the amount of resources available is $s , \infty _ { k }$ the composition of the bundle order, D the amount of the bundle acquired, and $v _ { k } ^ { + }$ and ${ v } _ { k } ^ { - }$ the value for acquiring and disposing of bundle k, respectively. Intuitively, shared resources should be allocated where they are most valuable. This requires that an agent can compute the value for buying and selling (bundles of) resources. The computation method for those private valuations is given in the next proposition.

Proposition 3. (1) If agent k’s current resource allocation is not optimal, then the agent’s valuation for the slack resource is zero. (2) If agent k’s current operation set is $e f -$ ficient, the order composition is $\omega _ { m k } = b _ { m k } ( m = 1 , \ldots ,$ M). The valuation and limit quantity that support the valuation are

$$
v _ {k} ^ {+} (\omega_ {k}) = \lim _ {\Delta \downarrow 0} \frac {C _ {k} ^ {*} (s _ {k}) - C _ {k} ^ {*} (s _ {k} + \Delta \omega_ {k})}{\Delta} \geq 0,\tag{11}
$$

$q _ { k } ^ { + } ( \omega _ { k } ) \ = \ \mathrm { m a x } ( \Delta ) ,$ , subject to:

$$
\frac {C _ {k} ^ {*} (s _ {k}) - C _ {k} ^ {*} (s _ {k} + \Delta \omega_ {k})}{\Delta} = v _ {k} ^ {+} (\omega_ {k}),\tag{12}
$$

$$
v _ {k} ^ {-} \left(\omega_ {k}\right) = \lim _ {\Delta \downarrow 0} \frac {C _ {k} ^ {*} \left(s _ {k}\right) - C _ {k} ^ {*} \left(s _ {k} + \Delta \omega_ {k}\right)}{\Delta} \leq 0,\tag{13}
$$

$$
q _ {k} ^ {-} (\omega_ {k}) = \max (\Delta), \text {   subject   to:   }
$$

$$
\frac {C _ {k} ^ {*} (s _ {k}) - C _ {k} ^ {*} (s _ {k} + \Delta \omega_ {k})}{\Delta} = v _ {k} ^ {-} (\omega_ {k}).\tag{14}
$$

The value $v _ { k } ^ { + } ( \omega _ { k } ) { \mathbf \Omega } ( v _ { k } ^ { - } ( \omega _ { k } ) )$ is a limit price that an agent . is willing to pay (offer), i.e., at those prices the agent makes a zero profit from the transaction. The actual limit order that the agent will submit for the acquisition or disposal of the (bundle of) resources might be different. The agent’s trading strategy is the subject of §4. Formulae (11)–(14) can be evaluated using parametric programming techniques (e.g., Gal 1979).

The implication of using an LP model for the supply chain is that it gives rise to strong complementarities among the resources. Mathematically, this means, that $v _ { 1 2 } ^ { + } ( \omega _ { 1 } \mathrm { ~ + ~ } \omega _ { 2 } ) \geq v _ { 1 } ^ { + } ( \omega _ { k } ) \mathrm { ~ + ~ } v _ { 2 } ^ { + } ( \omega _ { 2 } )$ An example imme- . diately clarifies this. If a product has to go through two operations on two different machines, then acquiring machine time on any machine without acquiring time on the other, is worthless; the value is obtained only by getting the correct combination of resources—acquiring only a subset may be of little value. The strong complementarity between resources will have a tremendous impact on how the markets for shared resources will operate. Usual markets are run as Walrasian markets, i.e., there is a separate market for each good and prices are determined for this good only. But, agents can only determine what they’re willing to pay for one resource, depending on what price they can acquire the other resource, introducing dependencies between products and market prices. Indeed, Walrasian markets assume gross substitutability between goods, i.e., the absence of complementarities. When this assumption is not satisfied, Walrasian markets fail (see Mas-Colell et al. 1995). In §4, we use a novel market mechanism, called a bundle market, where such complementarities between goods do not cause problems.

The meaning of the three propositions now becomes clear. Proposition 1 defines an efficient operation set based on the supply chain activity model. Proposition 2 shows how to sell off slack resources when the production plan $x ^ { * }$ can be supported with fewer resources. Proposition 3 illustrates how to acquire or dispose of resources when the current allocation is optimal and how the agent can still make a profit by changing its production plan and selling or acquiring resources. The bundle composition $\omega \ = \ b _ { k }$ and the maximum bundle amount q used in Proposition 3 together with the result of Proposition 1 shows that the new resource availability (assuming a trade would take place) will still be in the efficient operation set $\Phi _ { k } .$ . If the agent would not be allowed to make bundle trades, then the bundle orders would have to be $\omega = \pm e _ { m }$ (a unit vector), and it would be possible that the newly acquired resources would push the agent outside his efficient operation set.

With uncertainties in production, distribution, and the marketplace, the initial resource allocation is hardly optimal. For example, the agent may have planned its activities for a demand of $h _ { k } ,$ but the demand now seems to have changed to $h _ { k } ^ { \prime } .$ Therefore, the agent may not need the same resource allocation anymore, and will trade to improve its production plan. Following Propositions 2 and 3, agents can make resource acquisition or disposal requests to improve their cost (or profit) function in light of the changing conditions. The headquarters manage a resource market and reallocate common resources following the market mechanism.

## 4. The Bundle Auction Market

## Auction as a Decentralized Solution

Compared to other market mechanisms such as bilateral negotiation, an auction is more scalable and stable (Lu and McAfee 1996). Economists have long proposed using auctions to allocate resources to reveal demand and supply information. Examples of such problems include airport time slot allocation, job shops scheduling, and computer resources allocation. Only recently have economists and game theorists begun to take a direct role and designed different kinds of new market mechanisms, e.g., the auction of spectrums for telecommunication services (McAfee and McMillan 1996), which would not be possible without the use of IT.

Rassenti et al. (1982) developed a sealed-bid combinatorial auction mechanism for the allocation of airport time slots to competing airlines. Airlines can submit various bids for an airport’s landing or take-off slots. They used an integer programming algorithm to allocate resources and to determine prices for those resources. Banks et al. (1989) developed and analyzed several mechanisms that arise from auctions to allocate single-dimensional goods. Their results showed that an administrative process and a simple market as introduced by Debreu (1959) performed with low efficiencies. They designed two mechanisms: an adaptive user selection mechanism and an iterative Vickrey-Groves mechanism, both of which performed better than the simple market.

Our work in auction design differs in three ways. First, our mechanism is a double auction market in which agents can exchange resources while in Rassenti et al. (1982) the mechanism is a one-sided auction with a monopoly seller. Second, many “combinatorial auctions” (Nisan and Ronen 2000, Parkes and Ungar 2000, Rothkopf et al. 1998, Vohra and Vries 2000) solve for integer values, while our mechanism allows orders to be partially filled. An <sub>NP</sub>-hard problem results for a combinatorial auction mechanism requiring integer values, whereas our market problem can be solved in polynomial time. Third, in markets studied by Rassenti et al. (1982) theoretical market clearing prices do not exist, because of the integer requirements imposed on the trade quantities (Bikhchandani and Mamer 1997), whereas in our markets we can derive prices for individual resources as well as bundles.

Bertsekas (1990) developed an auction algorithm to solve the classical assignment problem. The algorithm intuitively resembles an “auction” where the nodes set tentative prices (as in an economic tatoˆnnement process) and it outperforms other solution methods. However, as a linear network flow problem, the assignment problem is a much simpler problem compared to MCNFP, for which no auction solutions have been developed. In addition, in an assignment market each agent has an independent valuation for each object whereas in our model an agent has interdependent values over several resources. Our bundle market mechanism is thus quite different from Bertsekas’ auction algorithm.

## Bundle Auction Market

As discussed earlier, our market needs to accommodate trades of bundles or combinations of assets, because of the complementarities between the shared resources. Our bundle market (or combinational market)

is a double auction sealed-bid call market. This means that we have sellers as well as buyers submitting trade offers (double auction), that they cannot see others buy and sell offers (sealed-bid) and that we match the orders at prespecified times (when the market is “called”).<sup>3</sup> The market displays the last-traded prices as well as the volumes for all the assets.

Agents can, but are not required $^ { \mathrm { t o , } }$ submit bundle orders. The bundle order is in the following format: $\{ \boldsymbol { \omega } _ { j } ^ { T } , \ \boldsymbol { w } _ { j } , \ \boldsymbol { q } _ { j } \}$ . The vector $\mathfrak { o } _ { j } ^ { T }$ represents the composition of the bundle $j .$ The $w _ { j }$ is the limit price, and $q _ { j }$ represents order quantity. For example, in a bundle order {(2, 1, 1), \$20, 100}, the composition vector (2, 1, 1) specifies the proportion of the bundle. It means the bundle has three resources with two units of Resource 1 and one unit for both Resources 2 and 3. A positive number in the bundle composition vector means buy and a negative number means sell. The limit price is \$20 per bundle and the total quantity is 100 bundles (200 units for Resource 1 and 100 units for both Resources 2 and 3). Traders do not have to submit pure buy or sell orders. Rather, they can submit mixed buy-sell orders. For example, order {(2, 1, 1), \$15, 100} means that the agent is willing to trade 100 units of the bundle, which contains buy orders for Resources 1 and $^ { 3 , }$ and sell orders for Resource 2, for a limit price of \$15 per bundle. But to simplify the discussion, we call an order a buy order if $w _ { j } \geq 0$ and an order a sell order if $w _ { j } < 0$ So, a buy order $\{ \boldsymbol { \omega } _ { j } ^ { T } , \boldsymbol { w } _ { j } , \boldsymbol { q } _ { j } \}$ means that an agent is willing to pay up to w per unit of bundle $j$ with composition $\omega _ { j }$ for a quantity up to $q _ { j } .$ The bundle trading matching program does the matches by solving a mathematical programming problem. The model is:

## Problem M

$$
\max w ^ {T} y,
$$

subject to

$$
\omega y \leq 0,\tag{15}
$$

$$
0 \leq y \leq q.\tag{16}
$$

The vector w denotes the limit prices for the n bundle orders. The objective function maximizes the total trade surplus, i.e., the difference between what an agent is willing to pay for the bundle and what the seller wants as payment to trade his resources. The solution vector y represents the trade volume of the submitted n orders. The vector y should be nonnegative because if someone wants to buy resources at a price $w _ { j } ,$ it does not necessarily mean that he wants to sell those resources at a price $- w _ { j }$ . The matrix $\omega \ = \ \left[ \omega _ { 1 } , \right.$ $\mathbf { \omega } _ { \mathbf { \omega } _ { 2 } } , \ldots , \mathbf { \omega } _ { n } ]$ contains n vectors, each of which represents the composition of a bundle order. The first set of constraints denotes that, for a bundle order to be matched for trade, each buy order for a resource in the bundle should be matched with one sell order or orders of the same asset from another bundle(s). Constraint (16) is the condition on maximum trade quantity.

The bundle matching program also provides a price discovery mechanism. The dual of Problem M can be written as:

Problem D

$$
\min \pi^ {T} q
$$

subject to:

$$
[ p ^ {T} \pi^ {T} ] \left[ \begin{array}{c} \omega \\ I \end{array} \right] \geq w
$$

$$
p, \pi \geq 0.
$$

The most important function of the market is to establish the price vector $p = ( p _ { 1 } , \cdot \cdot \cdot , p _ { M } ) ,$ which contains the market prices of the Resources $1 , \ldots , M$ . The vector p contains the individual trade surpluses, i.e., $\pi _ { j }$ measures how much lower than its limit price $w _ { j }$ the order was executed.

The transaction price for a bundle is the summation of the prices p for the different assets that compose the bundle. Assume that order j is traded. Then, the transaction price for order j is

$$
t _ {j} = \sum_ {m = 1} ^ {M} \omega_ {m j} p _ {m},\tag{17}
$$

where $p _ { m }$ is the imputed price for asset $m ( m = 1 , \ldots ,$ M ).

Proposition 4. The transaction price $t _ { j }$ for the matched bundle j is no worse than the submitted limit price $w _ { j } ,$ i.e., $t _ { j } \leq w _ { j }$

The proposition implies that the trade will almost always generate a surplus. So the agent who wants to buy (sell) a bundle of resources can be sure that it will never be traded at a price worse than what they are willing to pay (or want to receive). This is an important characteristic of the bundle market. To manage a decentralized supply chain effectively, the true information about resource valuation needs to be revealed by the various users. Ensuring a trade execution at a price better than an agent’s valuation provides incentives to truthfully compute and submit the resource valuation (as computed in Proposition 3). In the next section, we will prove this price mechanism is asymptotically incentive compatible, i.e., the dominant strategy for an agent is to reveal his true valuation.

The bundle market we propose here is related to mechanism design for computerized agents (Varian 1995) and the combinatorial auctions that have recently appeared in the literature of multiagent systems in artificial intelligence (Sandholm 1993, 2000). The auctions considered there are usually one-sided $( \mathrm { i . e . , }$ only buyers submit bids) and they restrict the trade quantities to take on integer values resulting in <sub>NP</sub>- complete problems. But in Problem M, the decision variables can take on fractional values, and we assume that the shared resources traded $( \mathrm { e . g . }$ , machine time, etc.) are divisible such that our bundle market can be executed by solving continuous LP problems, which are known to be solvable in polynomial time.

## Agents’ Trading Strategies

The purpose of the bundle market is to allow agents to trade resources so that they can reach their optimal production point. There are two trading strategies in the market. Agents can trade a single resource at a time and eventually get the whole resource bundle. The alternative is to buy or sell a bundle order, which is composed of multiple resources. Here, we demonstrate that trading in bundles is a dominant strategy over trading individual assets.

Proposition 5. Assume that agent k’s efficient operation set is (10) and it needs a resource bundle $( \omega _ { 1 k } , \omega _ { 2 k } , \ldots ,$ $\omega _ { M k } ) ,$ in which at least two elements are nonzero. Then, trading in bundle orders is a dominant strategy over trading in single-asset orders.

As discussed earlier, strong complementarities are present in a supply chain. Hence, Proposition 5 states that a novel market mechanism—a bundle market—is preferred when trading such assets with complementarities. Section 3 showed how agents can compute valuations for bundle orders. But in practice, agents may choose a bidding strategy that is not always truth telling. Here, we derive the optimal agents’ trading strategy, given that they know the exact valuation of the resources (described in Propositions 2 and 3), and the market mechanism. Agents are, of course, assumed to be self-interested and profit maximizing.

Previously, we defined $w _ { j }$ to be the bid submitted to the market, so that we explicitly allowed $w _ { j } \neq v _ { j } .$ . Here, we set $w _ { j } = v _ { j } - \delta ( \delta \geq 0 )$ , so d is the amount by which the agent misrepresents its true valuation of bundle j.

Proposition 6. A rational, profit-maximizing agent sets its bid $w _ { j }$ as $w _ { j } \leq v _ { j }$

Propositions $6 , 7 ,$ and 8 are the core of our research. At the outset, we intended to design a decentralized information system where users’ inputs truly reflect their (local) knowledge. Propositions 2 and 3 state how the true resource valuation can be computed by an agent. Proposition 6 states that in a supply chain where resources are acquired and disposed off through bundle markets, an agent never gains by submitting buy (sell) bids with a limit price higher (lower) than his valuation (cost). Corollary 8 will state that the more agents are in the market, the less incentive there is to understate (overstate) the valuation (cost) of the buy (sell) offers.

Proposition 7. Define the following quantities:

: Probability that order j is filled completely

$E [ \pi _ { j } ] \colon$ Expected per-unit trade surplus in case j is completely matched

$E l ( \delta \mathrm { ~ - ~ } \pi _ { j } ) ^ { + } ] :$ Expected per-unit trade surplus from misrepresenting the valuation of order j by d in case j is completely matched

$\varDelta ^ { + } .$ : Smallest value for d such that order j will not be executed (a random variable)

P (d): Marginal gain from misrepresentation for order $j ,$ i.e., the difference between the gain from trade when revealing the true valuation and misrepresenting the true valuation by an amount d

The expected marginal gain $E [ { \cal { I } } _ { j } ( \delta ) ]$ from misrepresenting the value of bundle j by $\delta ( \delta \geq 0 )$ is bounded by:

$$
\begin{array}{c} E [ \Pi_ {j} (\delta) ] \leq \frac {m}{n} q _ {j} \delta \operatorname{Prob} (\Delta^ {+} \geq \delta) + \alpha q _ {j} [ E [ (\delta - \pi_ {j}) ^ {+} ] \\ \operatorname{Prob} (\Delta^ {+} \geq \delta) - E [ \pi_ {j} ] \operatorname{Prob} (\Delta^ {+} <   \delta) ]. \end{array}
$$

Proposition 7 computes the gain that a user of the decentralized information system can expect by misrepresenting his knowledge by an amount d when there are n traders and M resources. From the result, it can be seen that for small values of d and n, an agent can expect a positive gain by understating his true valuation. However, when the competition increases (n grows bigger and Prob $( \Delta ^ { + } \geq \delta )  0 )$ , this expected gain disappears, and the agent can expect a negative consequence from misrepresenting his bids.

Corollary 8. When the number of orders submitted to the market becomes large, a rational profit-maximizing agent’s dominant strategy is to reveal its true valuation, or: $E l I _ { j } ( \delta ) J \le 0$ when $n \to \infty$ and $\delta \geq 0$

The result of Corollary 8 states that there is no expected gain by misrepresenting information when the number of traders—participants in the decision making process—is large. Now, what if it is known that there are only a small number of agents, i.e., when it is known that, e.g., one resource is only being used by, say, two agents? In that case, Meyerson and Satterthwaite (1983) have shown that there does not exist a mechanism that is ex post efficient,<sup>4</sup> i.e., where a trade can be guaranteed when the (potential) buyer’s valuation is higher than the (potential) seller’s. This is one issue we intend to tackle in future research, and one feasible approach is briefly outlined in §6.

The result from Corollary 8 is quite important and nonexistent for other decisionmaking approaches. In large-scale optimization problems, one always assumes that the objective function coefficients are exogenously given and perfectly accurate. But those figures have to be submitted and calculated by divisions or agents who will very likely be affected by the outcome of the decision process. In other words, there exists an incentive to misrepresent certain cost figures to influence the decisions for an agent’s own benefit in a central optimization approach. Our overall mechanism is shown to be robust against such misrepresentations.

## 5. Analysis

One of the problems in a decentralized organization is that the goals of the divisions are not aligned with the overall goal of the organization. The myopic behavior of individual agents may benefit the agents but hurt the overall organization. For example, if agents are evaluated based on their performance and there is no mechanism for them to exchange corporate resources, agents would like to possess as much resource as possible because that will guarantee a smooth operation. But this may cause resource shortage problems for other agents who are producing high-profit-margin products. In this case, the behavior of self-interested agents is not congruent with the designed organization goal.

In the decentralized system we designed, agents are rewarded based on how much they drive down costs (the objective function in Problem K), as well as how much money they make from trades. The access to shared resources is gained by acquiring them through an internal market. Propositions 3 and 4 derive the agent’s correct valuations for the resources. Propositions 6–8 determine an agent’s optimal trading strategy and demonstrate that the dominant strategy is to truthfully reveal the valuation knowledge when submitting trade offers to the market. So a decentralized system for managing the supply chain gives the right incentives for agents to transfer their local knowledge. However, does this mechanism also guarantee that the overall organizational goal of cost minimization in the supply chain (as stated in Problem O) is reached? Proposition 9 answers this question.

Proposition 9. If traders submit trade orders valued as described in Proposition 3, then each trade monotonically improves the objective function of the overall supply chain.

Not only will the goal of each agent align with that of the organization, but each transaction taken place in the market will result in an improvement in the overall objective function of the supply chain. A trade occurs only when there is a surplus, which is split between the agents involved in the trade, and the trade improves the overall objective function at the same time.

One measure of an efficient organizational design is goal congruence. Milgrom and Roberts (1992) define goal congruence as a situation in which the objectives of different individuals and organizations are aligned so that they pursue common goals.

Proposition 10. In a supply chain as described in Problem H and K, if agents trade using the bundle market mechanism, then the decentralized mechanism achieves goal congruence.

Proposition 10 is the culmination of our system. According to this result, we can effectively manage the supply chain in a decentralized fashion. Assuming that agents are self-interested and rewarded based upon how they manage their separate pieces of the supply chain, the agents will not find it advantageous to misrepresent their local knowledge about the supply chain. In the process, the supply chain will be optimized as it would be when using a centralized system that—as discussed before—has serious problems by not providing users the correct incentives to share critical (local) information about certain aspects of the supply chain. This concludes our theoretical development of the decentralized information system that supports the management of a supply chain within an organization.

## 6. Conclusion

## Limitations and Extensions

Our paper shows that a decentralized information system can be implemented that is goal congruent, and thus participants are provided the right incentives such that their myopic actions contribute to the effective management of the overall supply chain. However, one result (Corollary 8) was dependent upon a large number of agents using the same shared resources. One extension will relax this assumption, and the question will be whether Groves-Clarke mechanisms (Mas-Colell et al. 1995) can be implemented when a small number of traders are present, at the expense of “internal subsidies” to the traders. It is known that for Groves-Clarke double auctions budget balance is not guaranteed, i.e., the payments from the buyers do not suffice to cover the receipts for the seller and a “company subsidy” will have to be provided.

Another limitation of the present paper is the assumption of divisibility of production quantities, inputs, and outputs, which arises from the multicommodity-flow paradigm. Even though the divisibility assumption generally yields results that can be rounded to provide practical problem solutions, future research will investigate how our approach can be extended to explicitly deal with indivisibilities. Another line of research will investigate how a decentralized information system can be designed when the supply chain model is not a multicommodity-flow problem but a network of queues. The research questions are whether the system can still be implemented with a market for coordinating decisions and what the incentive structure is in such a situation.

Finally, the next step in our research will be to implement the proposed model in a lab experiment, with both human and automated agents. The system can be implemented by using a distributed object model such as Java RMI or CORBA. A distributed financial trading system was designed using this technology (Fan et al. 1998, 1999), and our future implementation will follow a similar, Web-based architectural design. In addition, decision support modules (Figure 4) will help agents to make the right trade decisions, i.e., calculating the right order quantity and price using Equations (11) through (14).

Figure 4 displays the information system architecture and information flow between the different decision making modules. Generally, implementing largescale supply chain systems correctly requires much effort, and this is even more true for a decentralized system. Future research will include the actual implementation of the supply chain organization, the auction market, and simulation studies to observe how quickly the system adapts to changing conditions, such as demand changes, disruptions in the delivery of raw material, and sudden machine downtimes.

Figure 4 The Distributed System Architecture and Information Flow of the Distributed Information System  
![](/api/attachments/H2JFGQXE/fulltext/images/b3308a3634735341c4da9fa4b4608d5e68e9f227174df05650084437b6c5e418.jpg)

## Summary

In this paper, we theoretically designed an information system that could plan the operations in a supply chain. The emphasis was on designing a system that was flexible and scalable, which we handled by developing a system as an agent organization, where individual agents can just be plugged into the whole system with minimum impact.

We coordinated distinct operations in the supply chain by introducing a bundle market where shared resources can be acquired or sold. We derived the computations necessary for enabling such trades and showed how the individual agents’ decision problems can be solved, based on their local and private information without revealing it. When the reward functions of the agents depend on their local profit maximization (or cost minimization), we are guaranteed that they have every incentive to (1) maximize their local profit, and (2) submit trades if they are better off selling shared resources than using them for their own production.

We design the bundle market as a sealed-bid doubleauction call market. As a by-product of matching the trades for the shared resources, we generate prices for the individual resources, imputed from their value in different combinations of resource usage. We then analyzed the optimal trading behavior of the agents and showed that, except when the expected number of trades is very small, the agent does not have an incentive to misrepresent his resource valuation to the market. This in turn caused the agent’s behavior to be congruent with the organizational goal.

## Acknowledgments

The authors thank the Associate Editor and the anonymous reviewers for their insightful comments and suggestions.

## Appendix

Proof of Proposition 1. U<sub>k</sub> is by definition a polyhedral cone because it is spanned by a finite number of rays. B u is efficient because $x _ { k } = \varphi$ uses exactly $B _ { k \Phi }$ of the shared resources. What remains to be proved, though, is that when $s _ { k } ^ { o } \notin \Phi _ { k } ,$ then there does not exist a mixture of activities $x _ { k } ^ { o }$ that does not dispose of any of the resources. We proceed by contradiction. Suppose there is such $x ^ { o } ,$ but then $s ^ { o } = B _ { k } x _ { k } ^ { o }$ with $x _ { k } ^ { o } \geq 0$ and by Minkowski’s Theorem, $s ^ { o } \in$ $\Phi _ { k } ,$ , which contradicts the assumption. ▫

Proof of Proposition 2. Proof omitted. ▫

Proof of Proposition 3. (1) Proof omitted. (2) From $\mathrm { L P }$ theory, we know that $C _ { k } ^ { * } ( s _ { k } ~ + ~ \Delta \omega _ { k } )$ is a nonincreasing, piecewise linearconvex function of $\Delta .$ Thus,  ${ \cdot } v _ { k } ^ { + }$ is the slope of $C _ { k } ^ { * } ( s _ { k } + \Delta \omega _ { k } )$ when $\Delta \downarrow 0 ,$ and ${ v } _ { k } ^ { - }$ is the slope of $C _ { k } ^ { * } ( s _ { k } \mathrm { ~ - ~ } \Delta \omega _ { k } )$ when D <sup>F</sup> 0 (Figure A1). The slope $v _ { k } ^ { + }$ remains valid in the interval $( 0 , q _ { k } ^ { + } ] ,$ and $v _ { k } ^ { - }$ valid in the interval $[ - q _ { k } ^ { - } , 0 )$ , and the $C _ { k } ^ { * } ( s _ { k } + \Delta \omega _ { k } )$ can be expressed as:

$$
C _ {k} ^ {*} (s _ {k} + \Delta \omega_ {k}) = \left\{ \begin{array}{l} C _ {k} ^ {*} (s _ {k}) + \Delta v _ {k} ^ {-} \text {for} \Delta \in [ - q _ {k} ^ {-}, 0) \\ C _ {k} ^ {*} (s _ {k}) \qquad \qquad \qquad \text {for} \Delta = 0 \\ C _ {k} ^ {*} (s _ {k}) - \Delta v _ {k} ^ {+} \text {for} \Delta \in (0, q _ {k} ^ {+} ] \end{array} \right..
$$

Therefore, acquiring $\Delta \mathfrak { o } _ { k }$ of the resource results in a lower operating cost of $\Delta v _ { k } ^ { + }$ so the agent is willing to pay up to, $v _ { k } ^ { + }$ per unit of ${ \mathfrak { O } } _ { k } ,$ as long as $\Delta \leq q _ { k } ^ { + }$ The same holds for selling resources. ▫.

Proof of Proposition 4. See Fan et al. (1999). ▫

Proof of Proposition 5. Suppose there is a surplus w if the bundle can be traded. First, let us look at the case that the agent is able to trade some resources individually but not the whole bundle. Because the agent technology requires a bundle of resources to operate, the trade does not add value to the agent, and the surplus cannot be realized. The acquired resources will then mainly be slack resources and will have to be disposed of at an unknown price later. So clearly, in this case, trading resources individually is no better than trading the bundle. Next, consider the case that the agent will acquire the whole bundle of resources by using either single-asset order or bundle order. The condition that the single-asset trading is able to acquire the whole bundle is $w _ { m } \geq p _ { m } , m = 1 , \ldots t ,$ M. The condition that the bundle trading for bundle j can be executed is

$$
w _ {j} = \sum_ {m = 1} ^ {M} \omega_ {m} w _ {m} \geq \sum_ {m = 1} ^ {M} \omega_ {m} p _ {m}.
$$

Figure A1 The Slope of the Cost Function

![](/api/attachments/H2JFGQXE/fulltext/images/41c3f03cafb36fcf0a922ace2700f392b364cf3eea1eccece01c477d5e54efe5.jpg)  
Information Systems Research Vol. 14, No. 1, March 2003

We have

$$
\left\{p _ {m} \colon w _ {m} \geq p _ {m}, m = 1, \dots , M \right\} \subseteq \left\{p _ {m} \colon \sum_ {m = 1} ^ {M} \omega_ {m} w _ {m} \geq \sum_ {m = 1} ^ {M} \omega_ {m} p _ {m} \right\},
$$

and thus

$$
\operatorname{Prob} (\{p _ {m} \colon w _ {m} \geq p _ {m}, m = 1, \dots , M \})
$$

$$
\leq \operatorname{Prob} \left(\left\{p _ {m}: \sum_ {m = 1} ^ {M} \omega_ {m} w _ {m} \geq \sum_ {m = 1} ^ {M} \omega_ {m} p _ {m} \right\}\right).
$$

If all the single-asset orders can be executed, the bundle order can also be executed. But when the bundle order is executed, single-asset orders may not all be executed. Therefore, the expected trading surplus $( \psi ^ { \cdot }$ Prob(Trading)) using bundle trading is at least as high as trading using single-asset orders. ▫

Proof of Proposition 6. We have the following assumptions:

(1) $f ( w , \bar { \boldsymbol { \omega } } ) > 0$ for w $\in [ \underline { { w } } , \bar { w } ] \times \times \times _ { i = } ^ { m }$ [x,<sub>1</sub> $\bar { \omega } _ { i } ] f$ is the joint density

(2) $\begin{array} { r } { \lvert C \mathcal { F } \rvert \simeq \alpha n , } \end{array}$ , and $\vert \mathcal { N F } \vert \simeq ( 1 ~ -$ )n with $0 < \alpha < 1 ( \mathrm { i . e . } ,$ —the proportion of matched orders — is independent of n) and for ease of exposition:

(3) $| \mathcal { P F } | = m$ (no primal degeneracy in the L.P.)

(4) Solution to Problem M unique (no dual degeneracy in the L.P.)

To prove Proposition $6 ,$ we have to make use of the dual problem of the bundle market (Problem D). After solving the market problem (Problem $M ) _ { ☉ }$ , the set of n orders can be partitioned into three disjoint subsets:

$\mathcal { N F } = \{ j \mid y _ { j } ^ { o } = 0 \}$ (the nonfilled orders),

$\mathcal { P F } = \{ j \mid 0 < y _ { j } ^ { o } < q _ { j } \}$ (the partially filled orders),

$C \mathcal { F } = \{ j \mid y _ { j } ^ { o } = q _ { j } \}$ (the completely filled orders).

By complementary slackness and duality theory, we have:

$$
p \cdot \omega^ {j} \geq w _ {j} \text {   and   } \pi_ {j} = 0 \quad \forall j \in \mathcal {N F},\tag{A.1}
$$

$$
t _ {j} = p \cdot \omega^ {j} \leq w _ {j} \text {   and   } p \cdot \omega^ {j} - w _ {j} = \pi_ {j} \forall j \in C \mathcal {F},\tag{A.2}
$$

$$
t _ {j} = p \cdot \omega^ {j} = w _ {j} \text {   and   } \pi_ {j} = 0 \quad \forall j \cap \mathcal {P F},\tag{A.3}
$$

where p are the imputed resource prices:

$$
p = w ^ {\mathcal {P F}} Q,
$$

with $Q = T ^ { - 1 } = [ \omega ^ { j } ] ^ { - 1 } ( j \in \mathcal { P F } )$ and $w ^ { \mathcal { P F } }$ the $1 \times m$ vector [w ] for every $j \in { \mathcal { P F } } .$ Therefore, the resource prices (and thus the transaction prices $t _ { j } )$ are completely determined by the bids of the partially filled orders. $\pi _ { j }$ is the per-unit gain from trade for bundle j. The total gain from trade is $\pi _ { j } \ q _ { j }$ for $j \in C \mathcal { F } ,$ zero otherwise. We also know that because Problem M is a linear program with m constraints and n upper-bound constraints, that $| \mathcal { P F } | \leq$ m (by Assumption $^ { 2 ) , }$ , the fraction of orders that are completely matched stays constant with n (the total number of submitted orders), $\mathrm { i . e . , ~ } | C \mathcal { F } | / n = \alpha$ for $n > >$ m. Using LP sensitivity analysis, we know that there exists a range for each bid w<sub>j</sub>: $[ w _ { j } - \delta _ { j } ^ { - } , w _ { j } + \delta _ { j } ^ { + } ]$ with $8 _ { j } ^ { - } , 8 _ { j } ^ { + } \geq 0 ,$ , such that the matched orders and quantities $y ^ { 0 }$ remain exactly the same. Assuming that the true valuation is $v _ { j \prime }$ we investigate for which value of d with $w _ { j } = v _ { j } - \delta$ the agent benefits from misrepresentation.

Now we prove that a rational trading strategy has $w _ { j } \leq v _ { j }$ for a rational, profit-maximizing agent.

Proof by contradiction. Suppose $w _ { j } > v _ { j }$ or $w _ { j } - v _ { j } = \delta > 0 .$ . We consider three cases depending on whether the agent’s order would have been nonfilled, partially filled, or completely filled if we were to bid $w _ { j } = v _ { j } .$ . Let $y _ { j } ^ { 0 }$ be the matched quantity when bidding $w _ { j } = v _ { j }$ and the matched quantity when biddingy $w _ { j } = v _ { j } - \delta \neq v _ { j }$

Case $\begin{array} { r } { 1 . j \in \mathcal { P F } f o r \ : w _ { j } = v _ { j } . } \end{array}$ Ceteris paribus, when bidding 18 $w _ { j } = v _ { j }$  d with $0 < - 8 \leq \delta _ { j } ^ { + } .$ we would still have, $0 < y _ { j } ^ { \prime } < q _ { j } , \thinspace \thinspace \mathrm { s o } \ j \in \mathcal { P F } .$ But from Assumption 3 we see that $t _ { j } = v _ { j } - \delta$ (so, now $t _ { j } > v _ { j } ) .$ ; so the trade results in a per-unit loss of |d| because of an overpayment in the amount of |d|. If  $\delta > \delta _ { j } ^ { + }$ then , $y _ { j } ^ { \prime } > y _ { j } ^ { 0 } ,$ and because of the dual-feasibility conditions $t _ { j } = p \cdot w _ { j } \geq v _ { j } + \delta _ { j } ^ { + }$ resulting in a total loss from trade of at least y <sub>j</sub> $8 _ { j } ^ { + }$ or a per-unit loss of at least , ${ \delta } _ { j } ^ { + }$

Case $2 . j \in C \mathscr { F } f o r w _ { j } = v _ { j } .$ . By increasing w<sub>j</sub> t $\boldsymbol { \ v } _ { j } - \delta ( > \boldsymbol { v } _ { j } )$ , the true gain from trade, (p ) remains invariant for all values of d. So, no gain is obtained from setting $w _ { j } > v _ { j }$

Case $3 . j \in \mathcal { N F } f o r \ : w _ { j } = v _ { j } .$ Ceteris paribus, when $- 8 \leq 8 _ { j } ^ { + }$ we still , have $y _ { j } ^ { \prime } \ = \ 0 ,$ so nothing is gained. When $w _ { j } = v _ { j } - \delta > v _ { j } + \delta _ { j } ^ { + }$ then $y _ { j } ^ { \prime } > 0$ and the per-unit loss from trade is at least ${ \delta } _ { j } ^ { + }$ In none. of the cases is a gain possible when setting $w _ { j } = v _ { j } - \delta > v _ { j } ,$ so a dominant strategy must have $\delta \geq 0 ,$ or equivalently $, w _ { j } \leq v _ { j } .$ ▫

Proof of Proposition 7. We analyze the trader’s ex post “regret” when he could have been better off following the strategy to underrepresent valuation as compared to submitting the true valuation as its trade offer. Again, we distinguish three cases depending on whether the “truth-revealing” strategy $( \mathrm { i . e . , }$ setting $w _ { j } = v _ { j } )$ would have resulted in (a) a nonmatched order, (b) a partially matched order, or (c) a completely matched order. We write $y _ { j } ( \delta )$ as the matched quantity of order j when bidding $w _ { j } = v _ { j } - \delta .$

Case $\begin{array} { r } { 1 . \ j \in \mathcal { N F } \ f o r \ w _ { j } \ = \ v _ { j } } \end{array}$ . Bidding $w _ { j } = v _ { j } - \delta$ will still yield $y _ { j } ( \delta ) = 0 ,$ so there is still no trade for all $\delta \geq 0 .$

Case 2. $\mathbf { \nabla } . j \in \mathcal { P F } f o r \mathbf { \nabla } w _ { j } = v _ { j } .$ Let’s assume that the trader would have known that $j \in \mathcal { P F }$ for $w _ { j } \ = \ v _ { j } .$ . Then, the dual constraints Assumption 3 are binding, and in case the agent would have revealed its true valuation, he would not have realized any gains from trade because $t _ { j } = \mathbf { \omega } _ { \mathbf { { \omega } } } ^ { j } p = w _ { j } .$ So, the agent would have every incentive to misrepresent its bid.

From LP sensitivity analysis, we know that there exists a threshold value ${ \delta } _ { 1 } ^ { + }$ such that the matched amounts remain the same (or technically, the basis doesn’t shift). If the agent would have complete knowledge of all orders submitted to the market, it would compute this value as:

$$
\begin{array}{l} \delta_ {1} ^ {+} = \min \Bigl \{\frac {w ^ {\mathcal {P F}} [ \omega ] _ {\mathcal {P F}} ^ {- 1} \omega^ {k} - w _ {k}}{e ^ {j} [ \omega ] _ {\mathcal {P F}} ^ {- 1} \omega^ {k}} \Bigr | k \in \mathcal {N F} \text {and} e ^ {j} [ \omega ] _ {\mathcal {P F}} ^ {- 1} \omega^ {k} <   0 \Bigr \} \cup \\ \Bigl \{\frac {w ^ {\mathcal {P F}} [ \omega ] _ {\mathcal {P F}} ^ {- 1} \omega^ {k} - w _ {k}}{e ^ {j} [ \omega ] _ {\mathcal {P F}} ^ {- 1} \omega^ {k}} \Bigr | k \in C F \text {and} e ^ {j} [ \omega ] _ {\mathcal {P F}} ^ {- 1} \omega^ {k} > 0 \Bigr \}, \end{array}
$$

where $w ^ { \mathcal { P F } } \in \Re ^ { m }$ is the portion of w $\mathbf { \Delta } \in \Re ^ { n }$ corresponding to the orders in ${ \mathcal { P F } } ,$ and $[ \omega ] _ { \mathcal { P F } } \in \Re ^ { m \times m }$ is the submatrix of ${ \mathfrak { o } } \in \Re ^ { m \times m }$ consisting of all columns of the orders in ${ \mathcal { P F } } .$

When underrepresenting bid j by an amount over ${ \delta } _ { 1 } ^ { + }$ the , matched quantities will change. If the agent would have complete knowledge of all offers submitted to the market, he could construct the complete function $y _ { j } ( \delta )$ as in Figure A2 and compute its gain from misrepresentation as in Figure A2. It is not realistic to assume complete knowledge of all trade offers, but we can still only conclude that, given the information that the order would be partially filled, an upper bound on the gain from under representing the true valuation by an amount d is $q _ { j } \delta .$ The agent also knows that there exists an upper bound on the misrepresentation, which we call $\Delta ^ { + } ,$ such that $y _ { j } ( \delta ) = 0$ for $\delta > \Delta ^ { + }$ (see Figure $\mathsf { A } 2 \mathsf { a } ) . \mathsf { S } \mathsf { o } ,$ if the trader under represents its bid by $\delta > \Delta ^ { + }$ , there would be no trade anymore, and the agent’s gain from trade would be zero, exactly the same as when the trader uses the strategy $\delta \ = \ 0 .$ When the agent does not have complete information about all other trade offers, $\Delta ^ { + }$ is a random variable and the expected gain from misrepresentation is bounded by (the uppermost dashed line in Figure A2b):

$$
E [ \Pi_ {j} (\delta) \mid j \in \mathcal {P F} ] \leq q _ {j} \delta \operatorname{Prob} (\Delta^ {+} \geq \delta).
$$

Figure A3 gives an example of the relationship between $y _ { j } ( \delta )$ and P<sub>j</sub>(d) for a single-asset market using demand and supply curves. Without loss of generality, order j can be a sell order.

Figure A2 Trade Quantities (a) and Marginal Gain (b) as a Function of Misrepresentation by an Amount d  
![](/api/attachments/H2JFGQXE/fulltext/images/92013383ff06b08734876831e320552ce78742a61ed673b7929baae759896f91.jpg)

Figure A3 Illustration of Trade Quantities and Marginal Gain in a Single Asset Market  
![](/api/attachments/H2JFGQXE/fulltext/images/cc93f600f925c996414ab728ee9020c707d2c569379173eeb6a21b747baa8d23.jpg)  
Information Systems Research Vol. 14, No. 1, March 2003

Case $3 . j \in C \mathcal { F } f o r \ : w _ { j } = v _ { j }$ . Next we assume that the trader would have known that its order would get completely matched. In that case, the dual constraints Assumption 2 would be binding and $\pi _ { j } \geq$ $0 ,$ where $\pi _ { j }$ is the per-unit gain from trade, and the total gain from trade in this case is $q _ { j } \pi _ { j } .$ The question is: Could the trader do better when using the strategy to under represent its bid? For now, we assume that the trader has complete knowledge of all orders submitted to the market. We also know from LP sensitivity analysis that when $w _ { j } = v _ { j } - \delta ,$ then as long as $\delta \le \pi _ { j } , y _ { j } ( \delta ) = q _ { j }$ and the same dual constraints remain binding. So the asset prices and, hence, the transaction prices of all orders remain the same. Thus, there is no gain from misrepresenting the order by an amount $\delta \leq \pi _ { j } .$ However, the trader may try to misrepresent by $\delta > \pi _ { j }$ so that the order becomes partially filled, dual constraint j then becomes part of the constraints in condition Assumption 2 and the trader would effectively be capable of influencing (i.e., lowering) its transaction price. Of course, now not the whole order would be filled, but depending on the other orders in the market, the agent may still be able to make a gain, as compared to submitting a bid with its true valuation. This is illustrated again in Figures A4a and A4b. The marginal gain from misrepresenting is 0 for $0 \leq \delta \leq \pi _ { j }$ (it stays $q _ { j } \ \pi _ { j } ,$ so nothing can be gained from misrepresenting). But when $\delta > \pi _ { j \prime }$ the total gain from trade becomes $y _ { j } ( \delta ) \left( \pi _ { j } + \delta \right)$ , and hence the marginal gain when using the strategy to misrepresent is

$$
\Pi_ {j} (\delta) = \left\{ \begin{array}{c c} 0 & \delta <   \pi_ {j} \\ (\pi_ {j} + \delta) y _ {j} (\delta) - \pi_ {j} q _ {j} & \pi_ {j} \leq \delta <   \Delta^ {+}, \\ - \pi_ {j} q _ {j} & \delta \geq \Delta^ {+} \end{array} \right.
$$

or because $y _ { j } ( \delta ) \leq q _ { j }$ we can write

$$
\Pi_ {j} (\delta) \Bigl \{ \begin{array}{l l} \leq (\delta - \pi_ {j}) ^ {+} q _ {j} & \quad \delta <   \Delta^ {+} \\ = - \pi_ {j} q _ {j} & \quad \delta \geq \Delta^ {+}, \end{array}
$$

where $( \delta - \pi _ { j } ) ^ { + } =$ max $\{ \delta \mathrm { ~ - ~ } \pi _ { j } , 0 \}$ . Because $\Delta ^ { + }$ is a random variable that depends on the other persons’ offers, we get $( \pi _ { j }$ itself is a random variable):

$$
\begin{array}{l} E [ \Pi_ {j} (\delta) \mid j \in C \mathcal {F} ] \leq E [ (\delta - \pi_ {j}) ^ {+} ] q _ {j} \operatorname{Prob} (\Delta^ {+} \geq \delta) \\ - E [ \pi_ {j} ] q _ {j} \operatorname{Prob} (\Delta^ {+} <   \delta) \end{array}
$$

When the trader has ex post knowledge about the execution of

Figure A4 Trade Quantities (a) and Marginal Gain (b) as a Function of Misrepresentation by an Amount d  
![](/api/attachments/H2JFGQXE/fulltext/images/28bd9452ac18ca30aaba8944abcd9ed3480df96caa1c8e9480d4ec8383422525.jpg)

![](/api/attachments/H2JFGQXE/fulltext/images/6b2152f880170ec182c275df6b9d2868ffc08bb0d9456cb8b6df4f6621e8bc15.jpg)

Information Systems Research Vol. 14, No. 1, March 2003

the order (i.e., not-executed, partially, and completely filled orders), the expected gain from misrepresenting its true valuation is given by the formulas derived above. Because the trader ex ante does not know whether its order is going to be partially or completely executed, our assumptions yield that:

Prob { j  <sub>PF</sub>} - m/n

$$
\text { Prob } \{j \in C \mathcal {F} \} = \alpha (0 <   \alpha <   1).
$$

${ \mathrm { S o } } ,$ the expected gain $E [ \Pi _ { j } ( \delta ) ]$ from under representing its bid when the execution status is unknown is bounded as follows:

E[P (d)] - E[P (d)| j  <sub>PF</sub>] Prob(<sub>j j</sub> $j \in \mathcal { P F }$

$$
\begin{array}{l} + E [ \Pi_ {j} (\delta) | j \in C \mathcal {F} ] \operatorname{Prob} (j \in C \mathcal {F}) \leq \frac {m}{n} q _ {j} \delta \operatorname{Prob} (\Delta^ {+} \geq \delta) \\ + \alpha \bigg [ q _ {j} E [ (\delta - \pi_ {j}) ^ {+} ] \operatorname{Prob} (\Delta^ {+} \geq \delta) - q _ {j} E [ \pi_ {j} ] \operatorname{Prob} (\Delta^ {+} <   \delta) \bigg ]. \square \end{array}
$$

Proof of Corollary 8. The following Lemmas A and B are required before proceeding to the proof of Corollary 8.

Lemma A. The quantity $y _ { j } ^ { 0 } - y _ { j } ( \delta _ { 1 } ^ { + } )$ is independent of n.

Proof of Lemma $\mathsf { A } . \boldsymbol { y } ^ { 0 }$ is the optimal solution to Problem M with objective function w, and is the optimal solution toy(d<sup></sup>) Problem M with objective function $w \mathrm { ~ - ~ } \delta _ { 1 } ^ { + } e _ { j } .$ For convenience, we write $y ( \delta _ { 1 } ^ { + } )$ $\boldsymbol { \mathbf { \mathit { \Sigma } } } = \boldsymbol { \mathbf { \mathit { y } } } ^ { \prime }$ . From the theory of parametric programming in LP (e.g., Gal 1979 and Stallaert 2001), it is known that

$$
y ^ {\prime} = y ^ {0} + \lambda p ^ {*},
$$

with $p ^ { * } \in \mathfrak { R } ^ { n }$ an n-dimensional vector that is represented by the column of the “next-best order” in the LP tableau, i.e., an order currently in or $C { \mathcal { F } } ,$ with k defined as:<sup>†</sup>

$$
\lambda = \min _ {i \in \mathcal {P F}} \left\{\frac {y _ {i} ^ {0}}{d _ {i} p ^ {*}} \right\},
$$

and the arrays $d _ { i }$ are the rows from a submatrix of the matrix X consisting of all m rows, but only the columns of the orders that are in ${ \mathcal { P F } } .$ Because $p ^ { * }$ is not a function of $n ,$ and k (the step length) is not a function of n either (it is solely determined by the m orders in $\mathcal { P } \mathcal { F } ) , y ^ { \prime }$ and thus $y _ { j } ^ { 0 } - y _ { j } ( \delta _ { 1 } ^ { + } )$ are independent of $n .$

Lemma B. The number of different partial matches for j before it becomes nonfilled are independent of n.

Proof of Lemma B. Because $y ^ { o }$ is independent of $n ,$ and by Lemma $\mathrm { ~ A ~ } y _ { j } ^ { 0 } ~ - ~ y _ { j } ( \delta _ { 1 } ^ { + } )$ is independent of n, a recursive argument shows that the number of steps before $y _ { j } ( \Delta ^ { + } )$ hits zero, is independent of n.

Now we prove Corollary 8: as $n  \infty ,$ Prob( $\begin{array} { r } { \mathcal { A } ^ { + } \geq \delta )  0 } \end{array}$ for every $\delta > 0$

Let $\xi$ be the number of steps before j becomes nonfilled. (By Lemma $\mathtt { B } , \xi$ is independent of n.)

<sup>†</sup>Because of the nondegeneracy assumption, there exists a nonsingular matrix B and $P ~ = ~ - B ^ { - 1 }$ where B consists of the m balance constraints of Problem M, plus the n-m orders in $\mathcal { N F }$ and <sub>CF</sub>. The vector $p ^ { * }$ is a column of P.

Define the random variable

$$
\tilde {z} = \left\{ \begin{array}{l l} \frac {\bar {w} [ \bar {\omega} ] ^ {- 1} \tilde {\omega} - \tilde {w}}{e ^ {j} [ \bar {\omega} ] ^ {- 1} \tilde {\omega}} & \text { when } (\bar {w} [ \bar {\omega} ] ^ {- 1} \tilde {\omega} - \tilde {w}) (e ^ {j} [ \bar {\omega} ] ^ {- 1} \tilde {\omega}) > 0, \\ \infty & \text { otherwise }, \end{array} \right.
$$

for a randomly chosen order with valuation w˜ and order composition ${ \tilde { \omega } } ,$ and a randomly chosen linearly independent set of m orders with valuation vector $\bar { w }$ and order composition matrix Then,[ ¯x]. from Assumption 1 it follows that there exists an interval  $\cdot \infty < a$ $< b < \infty$ such that $g ( \tilde { z } ) > 0$ for a $\leq \tilde { z } \leq$ b with $g ( \cdot )$ the density of z˜ and G(z) its distribution and $\bar { G } ( z ) = 1 - G ( z ) . { \Delta } ^ { + }$ is a random variable that depends on z˜, and we know that $\Delta ^ { + } \geq \delta$ if and only if there are exactly $( \xi - 1 )$ “better” orders, i.e., for which $\widetilde z \leq \Delta ^ { + }$ . The probability that there are no more than $\xi - 1$ orders out of n is given by the order statistics.

$$
\begin{array}{l} \operatorname{Prob} (\Delta^ {+} \geq \delta) = \sum_ {k = 0} ^ {\xi - 1} \binom {n - m} {k} [ G (\delta) ] ^ {k} [ \bar {G} (\delta) ] ^ {n - k} \\ = [ \bar {G} (\delta) ] ^ {n} \sum_ {k = 0} ^ {\xi - 1} \binom {n - m} {k} [ G (\delta) / \bar {G} (\delta) ] ^ {k}. \end{array}
$$

When $n  \infty , [ { \bar { G } } ( \delta ) ] ^ { n }  0$ and the second term becomes constant, as $\xi$ is independent of n. ▫

Proof of Proposition 9. Let $s _ { k } ^ { 0 }$ be the initial resource allocation and the performance of the supply chain is thus:

$$
\sum_ {k = 1} ^ {K} C _ {k} ^ {*} (s _ {k} ^ {0}).
$$

Let’s suppose that trade offers have been valued as described in Proposition 3 and there are trades $y ^ { o }$ such that

$$
w y ^ {0} > 0.
$$

Thus, there exists $j$ such that $y _ { j } ^ { 0 } > 0$ . Defining $\Gamma _ { k }$ as the set of orders of agent $\mathbf { k } ,$ then the new allocation yields an overall objective function value of

$$
\begin{array}{l} \sum_ {k = 1} ^ {K} C _ {k} ^ {*} \left(s _ {k} ^ {0} + \sum_ {j \in \Gamma_ {k}} \omega^ {j} y _ {j} ^ {0}\right) \\ = \sum_ {k = 1} ^ {K} C _ {k} ^ {*} (s _ {k} ^ {0}) - \sum_ {k = 1} ^ {K} \sum_ {j \in \Gamma_ {k}} w _ {j} y _ {j} ^ {0} (\text { by   Proposition   3 }) \\ <   \sum_ {k = 1} ^ {K} C _ {k} ^ {*} (s _ {k} ^ {0}) (\text { by   Proposition   4   and   since } \sum_ {k = 1} ^ {K} \sum_ {j \in \Gamma_ {k}} w _ {j} y _ {j} ^ {0} > 0). \square \end{array}
$$

Proof of Proposition 10. By Proposition $^ { 9 , }$ each trade results in a monotonic improvement in Problem (H). Therefore, if an agent maximizes its gain from trade, it contributes to improving the operations in the whole supply chain. ▫

## References

Ahuja, R. K., T. L. Magnanti, J. B. Orlin. 1993. Network Flows. Prentice Hall, Englewood Cliffs, NJ.

Akerlof, G. A. 1970. The market for “lemons”: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3) 488–500.

Anand, K. S., H. Mendelson. 1997. Information and organization for horizontal multimarket coordination. Management Sci. 43(12) 1609–1627.

Arntzen, B. C., G. G. Brown, T. P. Harrison, L. L. Trafton. 1995. Global supply chain management at Digital Equipment Corporation. Interfaces 25(1) 69–93.

Arrow, K., H. D. Block, L. Hurwicz. 1959. On the stability of the competitive equilibrium, II. Econometrica 27(1) 82–109.

Ba, S., J. Stallaert, A. B. Whinston. 2001. Introducing a third dimension in decentralized information systems design: The case for incentive alignment. Inform. Systems Res. 12(3) 225–239.

Bakos, J. Y., C. F. Kemerer. 1992. Recent applications of economic theory in information technology research. Decision Support Systems 8(5) 365–386.

Banks, J., J. O. Ledyard, D. P. Porter. 1989. Allocating uncertain and unresponsive resources. Rand J. Econom. 20(1) 1–20

Benders, J. F. 1962. Partitioning procedures for solving mixed variables programming problems. Numerische Mathematik 4 238– 252.

Bertsekas, D. P. 1990. The auction algorithm for assignment and other network flow problems: A tutorial. Interfaces 20(4) 133– 149.

Bhatnagar, R., P. Chandra, S. K. Goyal. 1993. Models for multi-plant coordination. Eur. J. Oper. Res. 67(1) 141–160.

Bikhchandani, S., J. W. Mamer. 1997. Competitive equilibrium in an exchange economy with indivisibilities. J. Econom. Theory 74(2) 385–413.

Brown, G. G., G. W. Graves, M. C. Honczarenko. 1987. Design and operation of a multicommodity production/distribution system using primal goal decomposition. Management Sci. 33(11) 1469–1480.

Brynjolfsson, E., H. Mendelson. 1993. Information systems and the organization of modern enterprises. J. Organ. Comput. 3(3) 245– 255.

——, T. W. Malone, V. Gurbaxani, A. Kambil. 1994. Does information technology lead to smaller firms? Management Sci. 40(12) 1628–1644.

Capacityweb.com. 2000. Company overview. See www.capacity web.com.

CRA. 1998. Simultaneous ascending auction with package bidding. Report (CRA No. 1351–00), Charles River Associates, Boston, MA.

Crowston, K., T. Malone. 1988. Information technology and work organization. Handbook of Human-Computer Interaction. M. Helander, ed. Elsevier, Amsterdam, The Netherlands.

Dantzig, G. B., P. Wolfe. 1960. Decomposition principles for linear program. Oper. Res. 8(1) 101–111.

Davenport, T. H. 1993. Process Innovation. Harvard Business School Press, Boston, MA.

——. 1998. Putting the enterprise into the enterprise system. Harvard Bus. Rev. (July–August) 121–131.

——, J. E. Short. 1990. The new industrial engineering: Information technology and business process redesign. Sloan Management Rev. 31(4) 11–27.

——, D. B. Stoddard. 1994. Reengineering: Business change of mythic proportions? MIS Quart. 18(2) 121–127.

Debreu, G. 1959. Theory of Value. Wiley, New York.

DeSanctis, G, B. Gallupe. 1987. A foundation for the study of group decision support systems. Management Sci. 33(5) 589–609.

Dirickx, Y. M., L. P. Jennergren. 1979. Systems Analysis by Multilevel Methods. John Wiley, Chichester, New York.

Dogan, K., M. Goetschalckx. 1999. A primal decomposition method for the integrated design of multi-period productiondistribution systems. IIE Trans. 31(11) 1027–1036.

Ellis, C. A., R. Gibbons, P. Morris. 1991. Groupware, some issues and experiences. Comm. ACM 34(1) 38–57.

Fan, M., J. Stallaert, A.B. Whinston. 1998. Creating electronic markets. Dr. Dobb’s J. 23(11) 52–57.

—, ——. 1999. The design and development of a financial cybermarket with a bundle trading mechanism. Internat. J. Electronic Commerce 4(1) 5–22.

, ——. 2000. The adoption and design methodologies of component-based enterprise systems. Eur. J. Inform. Sys. 9(1), 25–35.

Gal, T. 1979. Postoptimal Analyses, Parametric Programming, and Related Topics. McGraw-Hill International, New York.

Galbraith, J.R. 1973. Designing Complex Organizations. Addison-Wesley, Reading, MA.

——, E. E. Lawler. 1993. Organizing for the Future. Jossey-Bass, San Francisco, CA.

Geoffrion, A. M., G. W. Graves. 1974. Multicommodity distribution system design by Benders decomposition. Management Sci. 20(5) 822–844.

Halal, W. 1993. The New Capitalism. Wiley, New York.

Hayek, F. A. 1945. The use of knowledge in society. Amer. Econom. Rev. 35(4) 519–530.

Hinkkanen, A., R. Kalakota, P. Saengcharoenrat, J. Stallaert, A. B. Whinston. 1997. Distributed decision support systems for realtime supply chain management. Readings in Electronic Commerce. R. Kalakota, A. B. Whinston, eds. Addison Wesley, Reading, MA.

Honczarenko, M. 1993. Private communication.

Hurwicz, L. 1973. The design of resource allocation mechanisms. Amer. Econom. Rev. 63(2) 1–30.

i2 Technologies, Inc. 2000. TradeMatrix sell solution. White paper. i2 Technologies, Inc., Dallas, TX.

Jennergren, L. P, W. Muller. 1973. Simulation experiments of resource-allocation decisions in two-level organizations. Soc. Sci. Res. 2 333–352.

King, J. L. 1983. Centralized and decentralized computing: Organizational considerations and management options. Comput. Surveys 15(4) 319–349.

Ledyard, J. O., M. Olson, D. Porter, J. A. Swanson, D. P. Torma. 2002. The first use of a combined value auction for transportation services. Interfaces 32(5) 4 –12.

Lu, X., R. P. McAfee. 1996. The evolutionary stability of auctions over bargaining. Games Econom. Behavior 15(2) 228–254.

Malone, T. W., K. Crowston. 1994. The interdisciplinary study of coordination. ACM Comput. Surveys 26(1) 87–119.

——, J. Yates, R. I. Benjamin. 1987. Electronic markets and electronic hierarchies. Comm. ACM 30(6) 484–497.

Mas-Colell, A., M. D. Whinston, J. R. Green. 1995. Microeconomic Theory. Oxford University Press, New York.

McAfee, R. P., J. McMillan. 1996. Analyzing the airwaves auction. J. Econom. Perspectives 10(1) 159–75

McBride, R. D. 1998. Advances in solving the multicommodity-flow problem. Interfaces 28(1) 32–41.

Meyerson, R. B., M. A. Satterthwaite. 1983. Efficient mechanisms for bilateral trading. J. Econom. Theory 28 265–281.

Milgrom, P. J. Roberts. 1992. Economics, Organization & Management. Prentice Hall, Upper Saddle River, NJ.

Mintzberg, H. 1979. The Structure of Organations. Prentice Hall, Englewood Cliffs, NJ.

Mohrman, S. A., J. R. Galbraith, E. E. Lawler. 1998. Tomorrow’s Organization. Jossey-Bass, San Francisco, CA.

Nadler, D. A., M. L. Tushman. 1988. Strategic Organization Design: Concepts, Tools and Processes. Scott, Foresman and Co., Glenview, IL.

Nault, B. R. 1998. Information technology and organization design: Locating decisions and information. Management Sci. 44(10) 1321–1335.

Nisan, N., A. Ronen. 2000. Computationally feasible VCG mechanisms. Proc. 2nd ACM Conf. Electronic Commerce, Minneapolis, MN, 242–252.

Orlikowski, W. J., J. D. Hofman. 1997. An improvisational model for change management: The case of groupware technologies. Sloan Management Rev. 38(2) 11–21.

Parkes, D. C., L. H. Ungar. 2000. Iterative combinatorial auctions: Theory and practice. Proc. AAAI-2000, Austin, TX, 74–81.

Rassenti, S. J., V. L. Smith, R. L. Bulfin. 1982. A combinatorial auction mechanism for airport time slot allocation. Bell J. Econom. 13(2) 402–417.

Rothkopf, M. H., A. Pekec, R. M. Harstad. 1998. Computationally manageable combinational auctions. Management Sci. 44(8) 1131–1147.

Samuelson, P. A. 1974. Complementarity: An essay on the 40th anniversary of the hicks-allen revolution in demand theory. J. Econom. Literature 12(4) 1255–1289.

Sandholm, T. 1993. An implementation of the contract net protocol based on marginal cost calculations. Proc. 11th National Conf. Artificial Intelligence (AAAI-1993), Washington, D.C., 256–262.

——. 2000. Approaches to winner determination in combinatorial auctions. Decision Support Systems 28(1–2) 165–176

Sikora, R., M. J. Shaw. 1998. A multi-agent framework for the coordination and integration of information systems. Management Sci. 44(11) S65–S78.

Stallaert, J. 2001. Shadow prices and post-optimality analysis for degenerate linear programs using a pivoting algorithm. Working paper, Electronic Economy Laboratory, University of Southern California, Los Angeles, CA.

Stoddard, D. B., S. L. Jarvenpaa. 1995. Business process redesign: Tactics for managing radical change. J. Management Inform. Systems 12(1) 81–107.

Tan, J. C., P. T. Harker. 1999. Designing workflow coordination: centralized versus market-based mechanisms. Inform. Systems Res. 10(4) 328–342.

Varian, H. 1995. Mechanism design for computerized agents. Presented at the Usenix Workshop on Electronic Commerce, New York.

Vohra, R. V., S. Vries. 2000. Combinatorial auctions: A survey. Working paper, Kellogg Graduate School of Management, Northwestern University, Evanston, IL.

Winograd, T., F. Flores. 1986. Understanding Computers and Cognition: A New Foundation for Design. Ablex, Norwood, NJ.

Michael Shaw, Associate Editor. This paper was received on May 1, 2000, and was with the authors 4 months for 2 revisions.
