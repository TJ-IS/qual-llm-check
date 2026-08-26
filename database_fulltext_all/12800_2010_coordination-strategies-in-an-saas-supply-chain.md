---
otero_id: 12800
otero_key: "56QMF6Y8"
title: "Coordination Strategies in an SaaS Supply Chain"
authors: "Haluk Demirkan; Hsing Keneth Cheng; Subhajyoti Bandyopadhyay"
year: "2010"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222260405"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Coordination Strategies in an SaaS Supply Chain

Haluk Demi rkan , Hsin g Ken th Chen g, and Subh ajyo ti Band yo padh yay

Haluk Demirkan is a Clinical Associate Professor of Information Systems and a Research Faculty member of the Center for Services Leadership at the W.P. Carey School of Business at Arizona State University. He has a Ph.D. in Information Systems and Operations Management from the University of Florida. His research in service science and service-oriented management and technology solutions has included recent industry-sponsored research projects with American Express, Intel, IBM, MicroStrategy, and Teradata. His research appears in a number of journals, including Journal of the AIS, European Journal of Operational Research, IEEE Transactions on Systems, Man, and Cybernetics, Electronic Commerce Research and Applications, Information Systems Frontiers, Communications of the ACM, Information Systems and E‑Business Management, International Journal of Services Science, and other leading journals. He has 15 years of consulting experience in the areas of service-oriented solutions, information supply chain, business intelligence, and strategic business engineering with Fortune 100 companies. He is the recent recipient of the IBM Faculty Award for a research project titled “Design Science for Self-Service Systems.”

Hsing Kenneth Ch eng is an Associate Professor of Information Systems and Walter J. Matherly Professor in the Department of Information Systems and Operations Management of Warrington College of Business Administration, the University of Florida, Gainesville. He received his Ph.D. in Computers and Information Systems from the William E. Simon Graduate School of Business Administration, University of Rochester, in 1992. Prior to joining the University of Florida, he served on the faculty at The College of William and Mary from 1992 to 1998. His research interests focus on modeling the impact of Internet technology on software development and marketing and on the national debate on Net neutrality. Dr. Cheng has coedited several special issues in various information systems journals. He has served on the program committee of many information systems conferences and workshops and was the program cochair for the 2003 Workshop on E‑B usiness.

Subh ajyoti Band yopadh yay is an Assistant Professor in the Department of Information Systems and Operations Management at the University of Florida, Gainesville. He received his Ph.D. in MIS from Purdue University in 2002. His work has been published in several journals in the area of information systems and operations management. His current research interests include economics of information systems and information systems policy issues, especially in the area of Net neutrality and health informatics.

Abstrac t: The computing industry is gradually evolving to cater to the demand for software-as-a-service (SaaS). Two core competencies that have emerged over the past few years are that of the application service providers (ASPs) and the application infrastructure providers (AIPs). The arrangements between them result in system dynamics that is typical in supply chain networks. We examine the performance of an SaaS set up under different coordination strategies between these two players. Our analysis indicates that coordination between the monopoly ASP and the AIP can result in an outcome with the same overall surplus as can be achieved by a central planner. Even though the players have an incentive to deviate, it is possible to create the right incentives so that the economically efficient outcome is also the Nash equilibrium. The results of the analysis have significant implications for the coordination strategies for providers in the burgeoning business model of delivering software services over the Internet.

Key word s and ph rases: cloud computing, economic analysis, information sharing, infrastructure-as-a-service, service science, services, services management, softwareas-a-service, strategy, supply chain coordination.

Th e emergenc e of th e ph enomenon commonly known as software-as-a-service (SaaS) is the result of the confluence of various factors that add up to a seeming paradox. On one hand, computers continue to become exponentially more powerful and the per unit cost of computing continues to fall rapidly, so much so that computing power is nowadays considered to be largely a commodity [4]. On the other hand, as computing becomes more pervasive within the organization, the increasing complexity of managing the whole infrastructure of disparate information architectures and distributed data and software has made computing more expensive now than ever before to an organization. With the advent of globalization and its accompanying effects of cost cutting and speed to market, businesses today have to cope with rapidly changing information technology (IT) even as they have fewer resources to manage that technology [30].

As a result, businesses are increasingly looking to outsource activities that are deemed to be “noncore.” For many companies, IT and its management is one such noncore activity, but one that has been traditionally hosted in-house. This is because applications were often developed internally, and accessing those applications if they were hosted externally was very inconvenient [11].

The advent of the Internet, high-speed connectivity, communications security, and open standards is now beginning to challenge the notion of in-house hosting of applications. Application service providers (ASPs) such as Salesforce.com have witnessed record growth as businesses have grown more comfortable with the idea of accessing and managing their information over the Internet. To appreciate the magnitude of this change, consider the enterprise services computing company SAP , whose enterprise resource planning (ERP ) software traditionally was hosted on mainframes and which is now planning to provide an SaaS offering in 2010 for its small and mid-sized markets. This market segment, which makes up almost 30 percent of SAP ’s revenue, or about \$1 billion annually [29, 30], has witnessed rapid growth over the past few years. Customers in these market segments lack the wherewithal to make the level of IT investment that is typical of large organizations, but would be receptive to a service that would allow them to get the benefits of ERP software and be charged on an ongoing basis; in other words, allowing them to treat IT as an expense rather than as an asset. The rise of the SaaS model is essentially the result of catering to such a demand. The typical functions of the providers of this service—with the ASP typically serving as the “front-end” of the service—include providing structure and network services, data center and operations, application management and maintenance and integration and marketing and channel management [24]. Examples of ASPs include Salesforce.com, NetSuite, Google, Microsoft, and Oracle.

Application infrastructure providers (AIPs) complete the “back-end” of this arrangement by providing the infrastructure for the on-demand execution of the computing jobs. With an ASP hosting thousands of customers—perhaps logging into the application simultaneously—it would require a substantial investment in computing infrastructure (including servers, networking equipment, etc.) for satisfactory response times for all users, not to mention the requisite investment in human resources to manage this infrastructure. These AIPs offer the service of hosting the applications of the ASPs in their dedicated infrastructure by managing customer workloads to ensure quality of service to end customers and taking care of a variety of technical responsibilities such as server security and reliability, account compartmentalization, backup, version control, and support for e-mail systems, domain name system (DNS) hosting, and database systems. Some of the major AIPs are IBM, Computer Associates, Hewlett-Packard, and Sun Microsystems.

The arrangement described above creates a setup that is typical in supply chains in logistical networks, insofar as end customers get their services from providers who in turn depend on other providers to efficiently provide that service. It also results in system dynamics that is typical in supply chain networks, as the two providers try to gain control of the network to their advantage.

Given the complexity of this business model and the need for a network-centric infrastructure for the Web services, there is a need to study coordination strategies, pricing models, and capacity management issues between the involved parties [13]. Although the benefits of communication between the functional boundaries of the ASP and the AIP may be relatively easy to identify, realizing these benefits, and defining a coordination strategy under the influence of queuing effects, is a nontrivial problem.

In logistical terms, the demand from the end users comes in the form of packets over the Internet. If the SaaS business model is to be successful, these packets need to be delivered to the end users fast enough so that the delays in accessing the ASP’s services are not too onerous when compared to an in-house system. This time delay translates into a disutility for the end users, which detracts from the overall utility that the users get from consuming the ASP’s services.

Several observations about our SaaS model are in order. First, our model framework explicitly frames the coordination problem as a result of consumer choice, which in turn is affected by the queuing delays associated with the jobs that are requested by the end customers. Second, our model focuses on those ASPs specializing in a single application. Examples of such ASPs include NetSuite, which offers integrated ERP solutions all within a browser, and NetAbacus, which specializes in online purchasing solutions. Finally, the ASP’s capacity acquisition problem is framed as a single-period decision. The customer contracts with an ASP are typically long term in nature as a result of high switching costs, the costs associated with moving data out, recovering data, searching for another business partner, and so forth, and hence a single-period decision is a justifiable assumption.

We develop and evaluate four different coordination strategies involving various mechanisms of information sharing between the ASP and the AIP. Some of the research questions that we answer are:

RQ1: What are the coordination strategies and associated policies that would improve the SaaS coordination design and performance?

RQ2: What are the coordination strategies that would maximize the combined expected profit as well as each party’s profit level?

As our analysis indicates, the party who coordinates this service-centric computing supply chain has significant implications on the rent that the players extract and the total surplus generated. However, and importantly, our results also indicate that it is possible to create the right incentives so that the economically efficient outcome is also the Nash equilibrium. Finally, we offer some strategy directions for the players in this marketplace, including possibilities of strategic tie-ups.

From a research methodological perspective, our contribution lies in establishing the similarities of the SaaS model, which is an emerging new paradigm in computing, with some of the well-known issues of coordination in the supply chain literature in operations management. However, we fully understand that any analogy only goes so far—the SaaS supply chain is different in its realization from that of a physical supply chain. The operations management literature stream in the area of supply chain coordination concerns itself with pricing and inventory management decisions. The fundamental considerations of our model do include pricing issues, but there are no equivalent inventory management issues. Conversely, traditional supply chain literature does not consider the effects of congestion, which is a fundamental consideration in the SaaS business model: a consumer’s utility changes as congestion increases, and as a result the consumer has to wait longer in order to get his or her jobs serviced. Not only that, congestion has an externality effect—every new arrival in the queue affects the congestion of every other job that is already in the queue. Our model explicitly models this congestion and its externality effects.

## Literature Review

Bec ause SaaS is such a new ph enomenon, there has been relatively little research conducted that studies the coordination strategies between the ASP and the AIP. However, our research does have several points of contact and similarities with research in supply chain logistics that discusses pricing and capacity decisions, coordination issues, and information sharing. One of the earliest studies on an ASP’s strategy is from Cheng and Koehler [9], who analyze the optimal pricing and capacity decisions for a monopoly

ASP. By taking into account the impact of congestion cost, they model the economic dynamics between the ASP and its potential customers and identify a family of optimal pricing policies for the ASP. Our current research builds on this model by introducing a new player—the AIP—to form a complete SaaS supply chain.

From a methodological standpoint, our analysis draws on the model of Mendelson [20], who studies the effects of queuing delays and the user’s delay costs on the management of computer systems to maximize the expected net value of services from a profit center. In such a setting, congestion leads to delay, which deters additional users from joining the system—every new arrival inflicts more delay cost for itself and for others. In this paper, we analyze the impact of queuing delays in relation to SaaS coordination strategies. There are two private parties—the ASP and the AIP—and the goal of each is to maximize its own profits.

To understand the issues involved in the coordination issues between supply chain agents, we have drawn upon the significant amount of literature in this area. Ellinger [14] reviews the role of cross-functional collaboration between organizations in a supply chain and finds that success in today’s competitive marketplace relies on the merging of traditional functional boundaries in order to provide better customer service. Significantly, he finds that coordination and communication are extremely important in achieving this goal.

Ballou et al. [3] also stress the need for proper communication; they find that if in a supply chain the benefits are distributed unequally between the various agents as a result of the agents’ private incentives, there needs to a mechanism to support an outcome that is beneficial for the entire supply chain. Communication is the major mechanism to support this desired outcome of supply chain coordination. Conversely, mistrust leads to the breakdown of supply chain coordination; it increases the likelihood that agents will act to preserve self-interest, which may be at odds with the interests of the other agents. Following their lead, we assume that the ASP and AIP share information (the details of which are provided in the next section) in order to decide on their respective supply chain coordination strategies.

Several papers in supply chain management deal with the issue of the flow of information between the agents. Gavirneni et al. [16] measure the benefit to the retailer by sharing the market’s information with the supplier, with the assumption that there exists a perfectly reliable source of inventory and that information sharing has no impact on the retailer. Cachon and Fisher [6] study how information can be useful to the manufacturer when retailers use a batch ordering policy and assume that the supplier’s capacity is unrestricted. They conclude that accelerating the physical flow of goods through the supply chain is significantly more important than expanding the flow of information by utilizing IT. Lee et al. [19] show that sharing information reduces the manufacturer’s demand variance. Even though these studies point out how the manufacturer benefits from the retailer’s information, none of them focuses on how the information is shared between the manufacturer and the retailer, or how the benefit is shared among players.

Another paper that is of interest to us is by Weng [31], who first specifies a supply chain service-level requirement and then reviews the information sharing, but he does not consider the queuing effects. This service-level requirement and the order/ production quantity in turn determine the distributor’s unit sales price. In our model, however, we use the delay cost as a measure of performance and quality, rather than analyzing the delivery time and quality as separate components. Further, the price and capacity become key decision variables for the ASP.

For the sake of analytical closure, our model assumes a single ASP interacting with a single AIP (the complexity arises because we have to consider the interaction between the two agents as well as the effect of the external demand that modifies this interaction in turn). This assumption is equivalent to a single manufacturer and a single retailer, an assumption with wide precedence in the supply chain literature, especially among those that deal with coordination issues between different agents in the supply chain (see, e.g., [5, 7, 8, 15, 16, 18, 19, 22, 23, 28]).

As we stated in the introduction, our results show that the agents in the SaaS setup can achieve the socially optimal equilibrium through proper coordination (i.e., the decentralized coordination strategy has the same effect as if the whole supply chain were coordinated by a central planner). We end this section by mentioning several papers whose findings have philosophical similarities with our results. The first paper is by Cachon and Lariviere [8], who study supply chain coordination with revenuesharing contracts. They compare revenue sharing to buy-back and quantity-flexibility contracts and find that revenue sharing can coordinate systems with multiple retailers and that it induces the retailers to order a quantity that is optimal for the entire supply chain. Because our research looks at coordination strategies that can be dictated by one player in an SaaS supply chain, it also has some points of contact with Bakos’s [1, 2] pioneering work on electronic marketplaces, where he studies independent and buyerand supplier-controlled marketplaces. Finally, we mention the findings of Ha [17], who shows that under certain conditions a decentralized decision-making process can coordinate complex queuing systems.

## The Model

Consid er an SaaS supply ch ain th at c onsists of an AIP who provides the computer capacity to an ASP at price w per unit of capacity, and who in turn sells his or her value-added service to the market at price $p$ per transaction of processing. The AIP’s marginal cost for providing the computer capacity is c. The market in need of ASP services is characterized by a class of isoelastic demand function D(l) specified by Mendelson [20]:

$$
D (\lambda) = \frac {k}{\sqrt {\lambda}},\tag{1}
$$

where l is a Poisson rate of transactions per unit of time arriving at the ASP facility for processing and k is an arbitrary constant. The arriving transactions have a homogeneous service requirement as they access the same software hosted at the ASP. The ASP service system is modeled as an M/M/1 queue with processing capacities m in transactions per unit of time. Let $T ( \lambda , \mu )$ denote the expected time each transaction spends in the service system, including actual processing and waiting time. A stable queuing system requires

$$
\lambda \geq 0 \text {   and   } \mu > \lambda .\tag{2}
$$

In addition to the per transaction price $p$ charged by the ASP, consumers incur a congestion cost per transaction due to the queuing delay. This congestion cost equals the delay cost parameter per transaction per unit of time represented by v multiplied by the expected time spent in the ASP system $T ( \lambda , \mu )$ . The total expected marginal cost per transaction to a customer is thus the sum of the price and the expected delay cost per transaction. As the demand function $D ( \lambda )$ corresponds to consumer’s marginal value of the ASP service, the market equilibrium is achieved when the marginal value is equated with the marginal cost per transaction. Thus, one has

$$
D (\lambda) = p + v \cdot T (\lambda , \mu).\tag{3}
$$

From Equation (3), the equilibrium arrival rate $\lambda$ is a function of the per transaction price $p$ charged by the ASP, the $\mathbf { A S P ^ { \prime } s }$ s service capacity $\mu { _ { i } }$ , and consumer’s delay cost parameter v. Specifically, $\lambda$ is the single real root of following cubic equation in $\lambda$ (by combining Equations (1) and (3)):

$$
p ^ {2} \lambda^ {3} - (2 p ^ {2} \mu + 2 p v + k ^ {2}) \lambda^ {2} + (p ^ {2} \mu^ {2} + v ^ {2} + 2 p \mu v) \lambda - k ^ {2} \mu^ {2} = 0.
$$

Ceteris paribus, a higher price $p$ leads to a lower arrival rate l—that is, $\lambda = f ( p )$ . The goal of the ASP is to determine an optimal price $p ^ { * }$ to charge the market, and the optimal capacity $\mu ^ { * }$ to acquire from the AIP, while the objective of the AIP is to set an optimal capacity price $w ^ { * }$ to charge the ASP. Figure 1 shows a schematic of this model, and Table 1 summarizes notation used in this paper.

The AIP faces a derived demand function in the form of the capacity purchased by the ASP. The cost structure of AIP has two components: the marginal cost of computer capacity denoted by the parameter $^ { c , }$ and a diseconomy of scale cost parameter, $e ,$ related to the management of infrastructure. The parameter c reflects the constant economy of scale in computing power [21], whereas the diseconomy of scale in infrastructure management results from the increasing costs of managing capacity and user access [10, 26] and rising complexity of the business model of ASPs [25]. Thus, the profit function of the AIP is described by

$$
H P (\mu) = w \mu - (c \mu + e \mu^ {2}),\tag{4}
$$

where the first term in the right-hand side of Equation (4) is the revenue of the AIP.

The revenue of the ASP equals the quantity of the services sold by the ASP, represented by the market arrival rate, l, multiplied by the per transaction price, $p .$ This per transaction charge is the most common way of charging the ASP services in industry [12]. The cost to the ASP is the capacity cost paid to the AIP in order to acquire the required capacity $\mu .$ . Hence, the ASP’s expected profit function is defined as

$$
A P (p, \mu) = p \lambda - w \mu .\tag{5}
$$

When one of the two partners “coordinates” the SaaS supply chain, that partner takes into account the pricing and capacity decision rule disclosed by the other partner. In general, the ASP has better information regarding the behavior of the market because it is closer to the market. If the AIP is in charge of coordinating the whole SaaS setup, the ASP discloses to the AIP the information regarding the customer arrival rate and how it will set the price p. Alternatively, if the ASP is in charge, it approaches the AIP for a quote of the price-capacity schedule (i.e., w as a function of $\mu )$ and then coordinates the SaaS supply chain. The $\mathrm { A S P } \boldsymbol { \mathrm { s } }$ objective is to maximize its expected profit by deciding how much capacity, m, to buy from the AIP and the price, $p ,$ to charge to the market. The AIP is concerned with setting an appropriate per unit capacity price, w, to charge the ASP in order to maximize its profit.

![](/api/attachments/56QMF6Y8/fulltext/images/509d2da76ed026594d88aafc31e52dffd24a0241fd4431eb421c88e3427862c5.jpg)  
Figure 1. The SaaS Supply Chain with Queuing Delay

Table 1. Summary of Notation

<table><tr><td colspan="2">ASP market parameters</td></tr><tr><td>D(λ)</td><td>Market demand function of the ASP</td></tr><tr><td>λ</td><td>Customer&#x27;s arrival rate to ASP, a Poisson stream of transactions requiring ASP services</td></tr><tr><td>μ</td><td>Capacity of the ASP service system (μ &gt; λ)</td></tr><tr><td>ρ</td><td>Utilization ratio of the ASP system, defined as ρ = λ/μ</td></tr><tr><td>ν</td><td>Customer&#x27;s delay cost (per transaction, per unit of time)</td></tr><tr><td>T</td><td>The expected time a transaction remains in the system from arrival to completion of service</td></tr><tr><td colspan="2">Revenue and costs</td></tr><tr><td>w</td><td>AIP&#x27;s unit capacity sale price</td></tr><tr><td>c</td><td>AIP&#x27;s internal marginal cost for the capacity</td></tr><tr><td>p</td><td>ASP&#x27;s price per transaction</td></tr><tr><td>e</td><td>Diseconomies of scale cost parameter for AIP (e &gt; 0)</td></tr><tr><td>HP</td><td>AIP&#x27;s profit function</td></tr><tr><td>AP</td><td>ASP&#x27;s profit function</td></tr><tr><td>SP</td><td>Profit function of the entire SaaS supply chain</td></tr><tr><td>HP/SP</td><td>AIP&#x27;s share of profit against the entire SaaS supply chain</td></tr><tr><td>AP/SP</td><td>ASP&#x27;s share of profit against the entire SaaS supply chain</td></tr></table>

## Analysis of Coordination Strategies

In th is sec tion, we c onsid er four c oord ination strategies between the ASP and the AIP: (1) an overall SaaS coordination strategy, (2) the AIP-as-coordinator strategy, (3) the ASP-as-coordinator strategy, and (4) the aligned coordination strategy. The objective of the AIP and ASP as private agents is to maximize their individual expected profit, possibly at the expense of that of the global optimum that maximizes the total surplus of the two agents.

## Scenario 1: Overall SaaS Coordination Strategy

In this scenario, a central planner<sup>1</sup> plays the role of optimizing the SaaS setup as a whole by providing vertically integrated hardware and software hosting services. Alternatively, the same objective can be achieved by the AIP and the $\mathrm { { A S P } { \bar { s } } }$ forming a joint venture that maximizes the expected profit of the merged firm. The whole SaaS’s expected profit is the sum of the expected profits of the AIP and the ASP. This scenario has properties similar to a typical news vendor profit-maximization problem [23, 27]:

$$
S P _ {1} (p, \mu) = H P (\mu) + A P (p, \mu),\tag{6) \( ^{2} \}
$$

where $A P ( p , \mu )$ and $H P ( \mu )$ are as defined in Equations (4) and (5) (in other words, the total profit of the “system” is equal to the sum of the profit of the two agents). Equation (6) then reduces to

$$
S P _ {1} (p, \mu) = p \lambda - c \mu - e \mu^ {2}.\tag{7}
$$

When the price of the ASP’s service is greater than the AIP’s marginal capacity cost $( p > c )$ , the objective function in Equation (7) is strictly concave in both p and m, thereby ensuring the existence of a unique optimal solution (see the Appendix for proof).

The price w serves the role of internal transfer price and has no effect on the overall profit. This profit, which is the maximum profit for the combined firms, will be used as the benchmark to compare with other coordination strategies.

The first-order conditions of Equation (7) lead to

$$
k ^ {2} = 4 v \left(c + 2 e \mu_ {1} ^ {*}\right) \frac {1}{\left(1 - \rho_ {1} ^ {*}\right)}\tag{8}
$$

and

$$
k ^ {2} = 4 \mu_ {1} ^ {*} (c + 2 e \mu_ {1} ^ {*}) ^ {2} \frac {1}{\rho_ {1} ^ {*}}.\tag{9}
$$

Solutions to Equations (8) and (9) provide us the optimal capacity, $\mu _ { 1 } ^ { * }$ , the optimal arrival rate, $\lambda _ { _ { 1 } } ^ { \ast }$ , the optimal market price, $\boldsymbol { p } _ { 1 } ^ { * }$ , and the corresponding utilization ratio, $\boldsymbol { \rho } _ { 1 } ^ { * } ( = \lambda _ { 1 } ^ { * } / \mu _ { 1 } ^ { * } )$ , and economic profits.

## Scenario 2: AIP Coordinates the SaaS

In this coordination strategy, the ASP’s pricing information and the corresponding market demand (in arrival rate of transactions to the ASP)—both potentially sensitive information—are shared by the ASP with the AIP. The AIP then coordinates the SaaS decisions by setting a unit capacity price. Given this unit capacity price charged by the AIP, the ASP then determines an optimal unit sales price that maximizes his or her expected profit.

Proposition 1 (The ASP’s Pricing and Capacity Decisions When AIP Coordinates the SaaS Proposition): When the AIP coordinates the SaaS decisions, the ASP will order the maximum available capacity

$$
\mu_ {2} ^ {*} = \frac {\rho_ {2} ^ {*} k ^ {2}}{4 w ^ {2}} = \frac {k ^ {2}}{4 w ^ {2}} \left(1 - 2 \sqrt {\frac {v w}{k ^ {2}}}\right)
$$

from the AIP and charge the price

$$
p _ {2} ^ {*} = \frac {k \left(\frac {k}{w} \sqrt {\frac {v w}{k ^ {2}}}\right) - v}{\frac {k}{2 w} \left(1 - 2 \sqrt {\frac {v w}{k ^ {2}}}\right) \left(\frac {k}{w} \sqrt {\frac {v w}{k ^ {2}}}\right)}
$$

to the market and have the utilization ratio

$$
\rho_ {2} ^ {*} = 1 - 2 \sqrt {\frac {v w}{k ^ {2}}}.
$$

Proof: See the Appendix.

Proposition 1 states that when the AIP coordinates the SaaS, the ASP always orders the maximum available capacity. Because $p _ { 2 } ^ { * }$ is an increasing function of $w ,$ the higher the AIP charges the ASP for unit capacity, the higher will the ASP charge the market.

Under this scenario, the capacity that the ASP will order from the AIP and the ASP’s pricing formula will be communicated to the AIP. Utilizing this information, the AIP determines the optimal per unit capacity price $w _ { 2 } ^ { * }$ that maximizes its own profit. Notice that the $\mu _ { 2 } ^ { * }$ derived from Proposition 1 is a function of w. When it is substituted into Equation (4), $H P _ { 2 } ( \mu )$ effectively becomes $H P _ { 2 } ( w )$ , a function of w:

$$
\begin{array}{c} H P _ {2} (w) = \left(\frac {k ^ {2} w ^ {- 1}}{4} - \frac {k v ^ {1 / 2} w ^ {- 1 / 2}}{2} - c \frac {k ^ {2} w ^ {- 2}}{4} + c \frac {k v ^ {1 / 2} w ^ {- 3 / 2}}{2}\right) \\ - e \left(\frac {k ^ {2} w ^ {- 2}}{4} - \frac {k v ^ {1 / 2} w ^ {- 3 / 2}}{2}\right) ^ {2}. \end{array}\tag{10}
$$

To find the optimal expected profit for the AIP, the first-order condition requires that

$$
\begin{array}{c} \frac {d H P _ {2} (w)}{d w} = \left(- \frac {k ^ {2} w ^ {- 2}}{4} + \frac {1}{2} \frac {k v ^ {1 / 2} w ^ {- 3 / 2}}{2} + 2 c \frac {k ^ {2} w ^ {- 3}}{4} - \frac {3}{2} c \frac {k v ^ {1 / 2} w ^ {- 5 / 2}}{2}\right) \\ - e 2 \left(- 2 \frac {k ^ {2} w ^ {- 3}}{4} + \frac {3}{2} \frac {k v ^ {1 / 2} w ^ {- 5 / 2}}{2}\right) = 0. \end{array}\tag{11}
$$

Let $w _ { 2 } ^ { * }$ be the optimal price for the AIP derived from Equation (11). We denote $H P _ { 2 } ( w _ { 2 } ^ { * } )$ and $A P _ { 2 } ( p _ { 2 } ^ { * } , \mu _ { 2 } ^ { * } ) = p _ { 2 } ^ { * } \lambda _ { 2 } ^ { * } - w _ { 2 } ^ { * } \mu _ { 2 } ^ { * }$ as the optimal profits for the AIP and ASP for this scenario. Hence, the total SaaS profit in Scenario 2 equals

$$
S P _ {2} ^ {*} = H P _ {2} \left(w _ {2} ^ {*}\right) + A P _ {2} \left(p _ {2} ^ {*}, \mu_ {2} ^ {*}\right).\tag{12}
$$

Consequently, the expected profit shares of the AIP and ASP are

$$
\frac {H P _ {2} \left(w _ {2} ^ {*}\right)}{S P _ {2} ^ {*}}
$$

and

$$
\frac {A P _ {2} \left(p _ {2} ^ {*} , \mu_ {2} ^ {*}\right)}{S P _ {2} ^ {*}}.
$$

## Scenario 3: ASP Coordinates the SaaS

In this coordination strategy, the ASP does not communicate any capacity requirement and pricing decisions with the infrastructure capacity provider—the AIP. Instead, the ASP approaches the AIP for a quote of price-capacity schedule (i.e., w as a function of m) and coordinates the SaaS decisions. This leads to our second proposition:

Proposition 2 (The AIP’s Capacity Pricing Rule Proposition): When approached by the ASP, the AIP announces the price-capacity schedule, $\boldsymbol { w } _ { \scriptscriptstyle 3 } = \boldsymbol { c } + 2 e \boldsymbol { \mu } _ { \scriptscriptstyle 3 }$ , to the ASP.

Proof: When approached by the ASP, the AIP derives the price-capacity schedule by finding the optimal capacity that maximizes its profit function described by Equation (4). The first-order condition leads to $\mu _ { _ 3 } = ( w - c ) / 2 e$ . Thus, the AIP will announce the following price-capacity schedule to the ASP:

$$
w _ {3} = c + 2 e \mu_ {3}.\tag{13}
$$

Q.E.D.

The ASP then substitutes the price-capacity schedule of Equation (13) into the objective function, Equation (5), to determine the optimal price to charge to the market and optimal capacity to acquire from the AIP. The objective function facing the ASP in this scenario is described by $A P _ { 3 } ( p , \mu ) = p \lambda - ( c + 2 e \mu ) \mu$ . The first-order conditions lead to

$$
k ^ {2} = 4 v \left(c + 4 e \mu_ {3} ^ {*}\right) \frac {1}{\left(1 - \rho_ {3} ^ {*}\right) ^ {2}}\tag{14}
$$

and

$$
k ^ {2} = 4 \mu_ {3} ^ {*} (c + 4 e \mu_ {3} ^ {*}) ^ {2} \frac {1}{\rho_ {3} ^ {*}}.\tag{15}
$$

Let ${ \boldsymbol { \mu } } _ { 3 } ^ { * }$ be the optimal capacity, ${ p } _ { 3 } ^ { * }$ be the optimal price to the market, and $\boldsymbol { \lambda } _ { 3 } ^ { * }$ be the optimal arrival rate derived from Equations (14) and (15). Define $H P _ { 3 } ( w _ { 3 } ^ { * } , \mu _ { 3 } ^ { * } ) =$ $w _ { 3 } ^ { \ast } \mu _ { 3 } ^ { \ast } - c \mu _ { 3 } ^ { \ast } - e \mu _ { 3 } ^ { \ast 2 }$ and $A P _ { 3 } ( p _ { 3 } ^ { * } , \mu _ { 3 } ^ { * } ) = p _ { 3 } ^ { * } \lambda _ { 3 } ^ { * } - w _ { 3 } ^ { * } \mu _ { 3 } ^ { * }$ as the optimal profits for the ASP and AIP in this scenario. The total profit is now given by

$$
S P _ {3} ^ {*} = A P _ {3} \left(p _ {3} ^ {*}, \mu_ {3} ^ {*}\right) + H P _ {3} \left(w _ {3} ^ {*}, \mu_ {3} ^ {*}\right).\tag{16}
$$

## Scenario 4: Aligned Coordination Strategy

In this scenario, both the ASP and the AIP determine their own optimal policies individually. Then the ASP and AIP coordinate and optimize their own profits according to their own best-response functions. Specifically, for a given per unit capacity price, w, the AIP maximizes its profit function of Equation (4) and finds the following optimal capacity it wants to sell:

$$
\mu_ {4, A I P} (w) = \frac {(w - c)}{2 e}.\tag{17}
$$

Given the per unit capacity price of w, the ASP in this scenario finds the optimal capacity it wants to buy from the AIP by solving Equation (5) subject to the market equilibrium condition Equation (3). It follows that

$$
\mu_ {4, A S P} (w) = \frac {\rho_ {4} ^ {*} k ^ {2}}{4 w ^ {2}} = \frac {k ^ {2}}{4 w ^ {2}} \left(1 - 2 \sqrt {\frac {v w}{k ^ {2}}}\right).\tag{18}
$$

A mutually agreeable policy will ensure that the capacity the ASP wants to buy wil be the same as the capacity the AIP desires to sell by equating Equation (17) with Equation (18). Thus,

$$
\mu_ {4, A S P} (w) = \mu_ {4, A I P} (w).\tag{19}
$$

Scenarios 1 and 4 have several distinctive differences that set them apart as two dif ferent coordination strategies.<sup>3</sup> First, the price of the computing capacity, w, serves the role of “internal transfer price” and has no effect on the overall profit in Scenario 1 as it is canceled out in the objective function of Scenario 1, Equation (7). However, this price w is the key mechanism of coordination in Scenario 4. To see this, Equation (17) signifies the quantity of capacity the AIP is willing to sell at the given price w, while Equation (18) represents the quantity of capacity the ASP is willing to buy. In essence, Equation (19) reflects the market clearing of equating supply with demand of capacity through the market price w. Hence, Scenario 4 mimics a decentralized coordination mechanism of a market economy. Second, Scenario 1 involves a simultaneous joint optimization of both decision variables p and m. On the other hand, the problem in Scenario 4 is a sequential optimization problem involving m. It is well known that they generally do not lead to the same optimal solutions. In the next section, we show that both Scenarios 1 and 4 generate the same results through computational experiments. (An analytical proof for this result unfortunately is intractable.) Finally, the following proposition ensures that there exists a unique equilibrium of Scenario 4:

Proposition 3 (Aligned Optimal Capacity Proposition): There exists a unique solution in the aligned coordination strategy described by Equation (19).

Proof: See the Appendix.

The proof follows from the fact that $\mu _ { _ { 4 , A S P } } ( w )$ is a strictly decreasing function of w, while $\mu _ { _ { 4 , A I P } } ( w )$ is a strictly increasing function of w.

Proposition 3 shows that the ASP and AIP can establish a mutually agreeable equilibrium instead of reverting to opportunistic behavior. This particular outcome is an example of a cooperative game, when players choose the strategies by a consensus decision-making process. As we show in the next section, the firm that is in a position to coordinate the SaaS supply chain will have the incentive to do so, but because such an outcome is suboptimal from a global perspective, a mutually agreed upon profitsharing strategy can result in an enforceable coordinated behavior.

## Computational Exploration

Th e c losed -form solutions for some of th e equilibria d isc ussed in the previous section are too involved to allow for any meaningful analytical insights. We therefore conducted computational analyses of the four coordination strategies and present a set of numerical simulation experiments to illustrate the behavior of the equilibrium pricing and capacity decisions as predicted by our model. The extensive simulations suggest that the major observations drawn from this numerical analysis should probably be applicable in more general settings.

In our computational analyses, we explore the impact of the three key parameters on SaaS performance under the different scenarios: (1) the customer’s delay cost per transaction per unit of time, v; (2) the marginal capacity cost of the AIP, c; and (3) the diseconomy of scale parameter of providing the infrastructure, e. To conduct the computational analysis, we first selected a set of baseline parameter values, which we summarize in Table 2.

Table 2. Baseline Parameters for Computational Explorations

<table><tr><td>Parameters</td><td>Baseline values</td></tr><tr><td>Marginal capacity cost of AIP, c</td><td>1.00</td></tr><tr><td>Customer&#x27;s delay cost, v</td><td>0.20</td></tr><tr><td>Demand function parameter, k</td><td>1.00</td></tr><tr><td>Diseconomy of scale parameter, e</td><td>1.00</td></tr></table>

The baseline value of the parameter k was chosen to be 1.00 following Mendelson [20]. To ensure that the effect of the diseconomy of scale parameter e did not affect the various parameters of interest disproportionately with respect to k, we set it to be 1.00. Finally, when it came to the cost parameters, what was really of interest to us was their relative effect on the profit function, and hence we set the marginal capacity cost of AIP, c, at 1.00, and somewhat arbitrarily assumed that the effect of the customer’s delay cost, v, would be about an order of magnitude lesser, and hence kept it at 0.2.

Then for each scenario, we varied one parameter at a time over a range of values and calculated 10 key measures: (1) the combined SaaS profit, (2) the AIP’s profit, (3) the ASP’s profit, (4) the AIP’s profit as a fraction of the entire SaaS, (5) the ASP’s profit as a fraction of the entire SaaS, (6) the computing infrastructure capacity that the ASP acquires from the AIP, (7) the market demand in arrival rate of transactions, (8) the utilization ratio, (9) the ASP’s market price, and (10) the AIP’s unit capacity price. Figures 2–6 graphically illustrate these results.

The analysis highlights several important results. First, for all possible combinations of parameter values, the aligned coordination strategy (i.e., Scenario 4) generates the same performance for the combined SaaS setup (i.e., the combined surplus of the ASP and the AIP) as in the case where the SaaS is coordinated by a central planner (Scenario 1). In the decentralized (but aligned) coordination strategy, the computer capacity that the ASP agrees to buy and the AIP agrees to sell becomes the capacity that maximizes the whole SaaS’s performance. This mutually agreed upon capacity corresponds to the market equilibrium of supply and demand, as if the whole SaaS were coordinated by a central planner (or, equivalently, if the AIP and the ASP formed a joint venture that optimizes the entire SaaS).

The overall SaaS expected profit, utilization ratio, capacity ordered, and arrival rate are at their highest levels when the SaaS is coordinated as in the aligned coordination strategy. In other words, coordination pays: if organizations establish long-term alignment strategies instead of resorting to short-term opportunism, their overall welfare increases. From the perspective of the whole SaaS setup, as shown in Figure 2, the overall surplus is higher for the entire SaaS when it is coordinated by the ASP instead of the AIP. Thus, in the absence of a coordinated strategy or a central planner, it is better to let the player who is closer to the market—that is, the ASP—coordinate the SaaS. However, the lack of coordination results in some loss of economic efficiency, regardless of who ends up managing the SaaS.

![](/api/attachments/56QMF6Y8/fulltext/images/0f5d02b11d292118a8e2029a9e492f2ca09016d3e753f6fea6639be367636423.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/ef7a941b432e84846d59db31eed48d72bfc83eda1c48ee815743ab05a7e37b8f.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/0cbf6ae8a6325a8f601d3b6299894bdb92680599ec203c7228fbf6cc1e83b641.jpg)  
Figure 2. The SaaS’s Performance

Consider next the set of graphs in Figure 3. We observe that whoever coordinates the SaaS setup receives a higher profit than if the other partner were coordinating the chain, with the expected profit of either player in the aligned scenario being in between these two values. The implication is that whoever coordinates the SaaS exploits the information shared from the other partner by including that information in its own objective function. Thus, if either of the agents has the market power to coordinate the “supply chain,” it would prefer to do so. This might happen if only one of the two agents has more brand recognition or is thought to be trusted by the end customers. In such a situation, that agent would have the incentive to exert its market power to coordinate the supply chain rather than arriving at a mutually aligned market equilibrium. As the results from the previous set of graphs (Figure 2) indicate, in such an eventuality, a tie-up between, say, the ERP vendor SAP and a lesser-known AIP would be preferable from an economic efficiency viewpoint than a tie-up between IBM and the cloud-based ERP provider NetSuite.

However, the levels of the optimum profit under the four scenarios point to the possibility of reaching at the socially efficient level of profit even though it may seem that the agent with market power has the incentive to act selfishly and coordinate the supply chain. To see this, consider a contract for aligned coordination designed by the agent with market power, in which the other agent, as part of the profit-sharing arrangement, gets to keep at least as much as he or she would if the agents had not collaborated with the first agent coordinating the supply chain. Because the aligned strategy yields a higher cumulative surplus, the former agent will then get more from this profit-sharing arrangement than he or she would through his or her “myopic” strategy of coordinating the supply chain. Thus, an agent with market power in the SaaS model can credibly enforce an equilibrium that is socially as well as individually preferable, by offering a profit-sharing mechanism to the other agent that is just enough to deter deviation to any selfish strategy.<sup>4</sup> However, such an outcome needs to be carefully cultivated, as it involves sharing of potentially sensitive information between the partners who need to trust each other, mirroring the observations of Ballou et al. [3].

![](/api/attachments/56QMF6Y8/fulltext/images/86b388c01bf88cfb3117896efcd89ed2acac3cbd931e521341dbb642b46731c6.jpg)  
Figure 3. The Welfare of Firms (AIP and ASP)

Note that ordinarily there would be an incentive for either player to coordinate the supply chain, and therefore the Nash equilibrium would be the globally suboptimal selfish coordination strategy. However, if the ASP and the AIP coordinate and optimize their profits according to their best-response functions, the globally optimal solution is achieved whereby the combined surplus is higher than the selfish strategies. This, however, results in a lower profit than what a firm (either the ASP or the AIP) could achieve by coordinating the supply chain by itself, but the gain of the coordinating firm is less than the loss of the other firm. Thus, the “gainer” firm could suggest a coordinated strategy to the other firm, whereby the “loser” firm would make at least as much by coordinating as it would by not coordinating. In a one-shot game, the latter would resort to not coordinating, but in a repeated game, such behavior would be punished by the firm with market power.

From Figures 2a, 3a, 3b, and 4a, we find that the expected profits and utilization for all scenarios decrease as the delay cost increases. When customers place more value on the responsiveness of the service, there are fewer arrivals to the system at the equilibrium. That is, there is an inverse relationship between the delay cost and the utilization ratio. This in turn causes the ASP to reduce service capacity, which in turn results in an increase of the market price (Figure 4d).

![](/api/attachments/56QMF6Y8/fulltext/images/64b3fafd98760d135dbb3b19527adb5a26e32ce085c99610fb4ec3d9ec35a622.jpg)  
Figure 4. The Impact of Delay Cost

In Figure 5, we show the effect of the $\mathrm { A I P } ^ { \prime } \mathrm { s }$ unit capacity cost parameter, c, on the various performance metrics, and in general the effects are similar to those observed with changes in delay costs. Surprisingly, the impact of the delay parameter and capacity costs on the overall performance of the agents is greater when the strategies of the players are coordinated or aligned than when the strategies are not coordinated. We also find that the impact of the delay cost is higher on the agent who is closer to the market—that is, the ASP. Conversely, the impact of the capacity cost is higher on the AIP. The impact of the delay parameter and the capacity costs to the ASP is the lowest when the AIP coordinates the SaaS, but is the highest when the ASP coordinates the SaaS setup (Figure sets 3a, 3b, 3c, and 3d). We note that even as the expected profit of the AIP becomes lower in the presence of a higher customer’s delay cost, the AIP’s share of the combined profit increases. Another important observation is that the system with the higher capacity enjoys a higher arrival rate of transactions, and that too with a lower market price.

Finally, from Figure 6, we conclude that the expected profits of the whole SaaS and the ASP under all coordination scenarios will decrease as the diseconomy of scale parameter, e, increases. The AIP, however, would prefer such an outcome, because its expected profit actually increases when the diseconomy of scale parameter increases under the aligned mechanism, as well as when the ASP coordinates the SaaS, as shown in Figure 3e. Table 3 presents the comparative statics, summarizing key findings of Figures 2 to 6.

![](/api/attachments/56QMF6Y8/fulltext/images/a6bd4afdf2ae33596bd95e117eac80093f202d788c57b1c817793e4acbfcd71c.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/f96d60d126007821afdce4466ed6f2cae6c8ff901eacf8baa3edec976ad073d3.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/767063cc4e846204cadf121c828dd5616dc2ddc2d1218ec185e3721acf26c7f0.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/7284234d6d434862bf7135371bb00e42983c281971491af6c95b6bcb4fa1310c.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/42c0bf0257be8a350bbf723cf4f75b5fcaccafc099dd5b6bceeed88ff662c513.jpg)  
Figure 5. The Impact of Unit Capacity Cost

## Managerial Strategy Insights and Concluding Remarks

One of th e most important c ommerc ial d evelopments in the past few decades, IT, is undergoing a transformation in the corporate marketplace. The confluence of several factors has meant that, for the first time, organizations can realistically consider IT as less of an asset and more as an expense. The phenomenon has been called by various names—software-as-a-service, utility computing, service-centric computing, and cloud computing being some of them—but in its essence, it involves doing away with maintaining a huge corporate IT infrastructure and instead paying for the computing requirements as if it were a utility. With such services becoming increasingly commonplace, the computing industry is gradually evolving to cater to such a demand. To provide this service, two core competencies that have emerged over the past few years are that of the application service provider, who provides the software capabilities, and that of the application infrastructure provider, who provides the hardware capabilities.

![](/api/attachments/56QMF6Y8/fulltext/images/4366f47e88b0c87ce0eaf33b15a717024c87b1362808e8d3bdfc9866b4951034.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/519f448dd0900428ecd4d6a5b7890adbf3f0488122a3ef06f1ce21f9b67382e2.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/59dd27b74ff51f34b49d6cbd43df89f20daebd72f97673e73f1d688c129b769b.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/bfe41802fb6b70c71bf2eed5e6a69c900aa941233045eed588990fb9e37c35e8.jpg)

![](/api/attachments/56QMF6Y8/fulltext/images/397d0df7a86ac39ecc24646135b20eccd4d5b2d20a3bb506d314f1224f79ca39.jpg)  
Figure 6. The Impact of Diseconomy of Scale

In this paper, we use the term software-as-a-service to describe this phenomenon. The arrangement between the ASP and the AIP creates a setup that is typical in supply chains in logistical networks, insofar as end customers get their services from providers who in turn depend on other providers to efficiently provide that service. It also results in system dynamics that is typical in supply chain networks, as the two providers try to gain control of the network to their advantage. The congestion cost due to a queuing delay in the SaaS setup, however, presents a unique challenge not studied in the traditional supply chain literature. It is this system dynamics that we explore in this paper. Given the complexity of this business model and the need for a network-centric infrastructure for the Web services, there is a need to study coordination strategies, pricing models, and capacity management issues between the involved parties to ensure that the services are provided efficiently (in an economic sense) to the end users. The purpose of this paper is to analyze a model that serves these objectives.

We examine the economic performance of an SaaS infrastructure under four different coordination strategies involving information sharing between the ASP and the AIP. In

<sub>3.</sub> <sub>Co</sub>m<sup>parative</sup> <sup>St</sup>

$$
\begin{array}{c c c c c c c c c c c c} & & \mu^ {*} & \lambda^ {*} & \rho^ {*} & P ^ {*} & w ^ {*} & H P ^ {*} & A P ^ {*} & S P ^ {*} & H P ^ {*} / S P ^ {*} & A P ^ {*} / S P ^ {*} \\ \hline \text {Scenario 1: SaaS} \\ v & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow \\ c & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow \\ e & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow \\ \text {Scenario 2: AIP coordinates the SaaS} \\ v & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \downarrow & \downarrow & \downarrow & \downarrow & \uparrow \\ c & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \uparrow & \downarrow & \downarrow & \downarrow & \downarrow \\ e & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow \\ \text {Scenario 3: ASP coordinates the SaaS} \\ v & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \downarrow & \downarrow & \downarrow & \downarrow & \uparrow \\ c & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \uparrow & \downarrow & \downarrow & \downarrow & \downarrow \\ e & \uparrow & \downarrow \\ \text {Scenario 4: Aligned} \\ v & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \downarrow & \downarrow & \downarrow & \downarrow & \uparrow \\ c & \uparrow & \downarrow & \downarrow & \downarrow & \uparrow & \uparrow & \downarrow & \downarrow & \downarrow & \downarrow \\ e & \uparrow & \downarrow & \downarrow \\ \end{array}
$$

the first scenario, a single firm (or a central planner) plays the role of both the AIP and the ASP to achieve the goal of optimizing the whole SaaS. In the second coordination strategy, the information about the market demand and the ASP’s pricing and capacity decisions are disclosed to the AIP, who then coordinates the SaaS decisions. In the third scenario, the ASP approaches the AIP for a quote of the price-capacity schedule and then coordinates the SaaS decisions. Finally, in the “aligned” scenario, both the ASP and the AIP optimize their own profit as a response to the other’s expected strategy and then come back to negotiate a mutually agreeable policy.

Our paper makes several contributions that help us understand the market dynamics in the burgeoning area of SaaS infrastructure providers. While it is expected that coordinated strategies will do better than noncoordinated strategies in maximizing the combined surplus, and that left to themselves the two firms will arrive at a socially suboptimal equilibrium (in other words, a “prisoner’s dilemma” outcome), our computational explorations show that it is possible for the two firms to agree on a profitsharing strategy that can make the socially desired equilibrium also their preferred strategies. Further, we show that the SaaS supply chain that is coordinated by the ASP is better than the one coordinated by the AIP.

The results of our analysis indicate that coordination between the ASP and the AIP can result in an outcome that achieves the same maximum overall surplus that can be achieved by a social planner (or, equivalently, by a combined firm). However, market realities might often result in a tie-up between an ASP and an AIP where only one of them has significant market power, and in such a situation the results of our analysis indicate that the firm that is in a position to coordinate this SaaS supply chain will have the incentive to do so (i.e., there lies a definite incentive for either firm to control the supply chain). The outcome, however, is suboptimal if the objective is to maximize the overall surplus, and more so if it is the AIP who ends up coordinating the supply chain. Therefore, as we point out, a tie-up between a well-recognized ASP and a relatively unknown AIP is preferable over a tie-up to provide the same service by a relatively unknown ASP and a well-recognized AIP.

In terms of the practice of the management discipline, our paper has several contributions, especially in terms of strategy for tie-ups and mergers in the ASP–AIP arena. Our results suggest a possible “strategy direction” in the ASP market, especially for large hardware vendors such as IBM or Hewlett-Packard. Given the explosive growth in this market, our analysis indicates that one possible strategy that hardware vendors might want to pursue is to buy some ASP companies outright, especially those who operate in market segments they (the AIPs) consider as strategic. This will lead to a market condition we envisage in our analysis as Scenario 1, whereby we have one central planner coordinating strategies for the entire SaaS.

Our results also indicate another intriguing strategy direction for the AIPs, whereby they have some kind of a strategic relationship with some of the ASPs, and thereafter take a “hands-off” approach—that is, the operational initiatives are left in the hands of the ASP. Our analysis indicates that such an aligned coordination strategy can lead to outcomes that are as economically efficient as a centrally planned coordination strategy. As we noted earlier, to make such a contract enforceable, the AIP, as part of the profit-sharing arrangement, would need to make at least as much as it would have by controlling the supply chain, and since the coordinated strategy leads to a higher overall surplus, the ASP would also be left with a higher surplus than it would if the AIP were controlling the supply chain (in other words, both the AIP and the ASP would have the incentive to join such an arrangement, and the outcome would lend itself to a Nash equilibrium).

One interesting finding of our study is that delay costs (i.e., the disutility of delay in accessing the service) and capacity costs affect the overall surplus more severely when the ASP and AIP follow coordinated strategies than when they do not.

Our study makes important theoretical and practice-oriented contributions to the literature on the coordination structure, capacity, and pricing decisions in buyer– supplier relationships and the role of queuing delays. It has points of contact with supply chain literature that investigates coordination strategies between manufacturers and retailers in the supply chain. However, unlike a physical supply chain, in our context we need to model the externalities of congestion. For the sake of analytical tractability that has precedent in supply chain literature, we considered the strategic relationship between one ASP and one AIP. Future studies can explore—if not analytically, then at least through simulations—the effect of interactions between multiple ASPs and AIPs with different capabilities. Analytical tractability has also meant that we have considered a single class of customers who are charged the same rental price. In future research, the customers may be differentiated by their requirements for different performance guarantees (and different bandwidth usage capacities) and be allowed to choose from a menu of contracts (e.g., for one that might exist for different market segments).

Acknowledgments: The authors thank the special issue guest editors Indranil Bardhan and P.K. Kannan, the anonymous reviewers, and Robert J. Kauffman for their suggestions on this paper.

## Notes

1. An example of a central planner is Peer 1, one of the largest information systems/technology hosting companies according to Hosting-Review.com.

2. The subscripts 1 through 4 correspond to the four scenarios.

3. We thank an anonymous reviewer for raising this comment.

4. Note that an agent without market power cannot credibly enforce this equilibrium, although it can conceivably suggest this outcome to the other agent.

## Referenc es

1. Bakos, J.Y. Information links and electronic marketplaces: The role of interorganizational information systems in vertical markets. Journal of Management Information Systems, 8, 2 (Fall 1991), 31–52.

2. Bakos, J.Y. A strategic analysis of electronic marketplaces. MIS Quarterly, 15, 3 (September 1991), 295–310.

3. Ballou, R.H.; Gilbert, S.M.; and Mukherjee, A. New managerial challenges from supply chain opportunities. Industrial Marketing Management, 29, 1 (January 2000), 7–18.

4. Bardhan, I.; Demirkan, H.; Kannan, P.K.; Kauffman, R.J.; and Sougstad, R. An interdisciplinary perspective on IT services management and service science. Journal of Management Information Systems, 26, 4 (Spring 2010), 13–64, this issue.

5. Cachon, G.P. The allocation of inventory risk in a supply chain: Push, pull, and advancepurchase discount contracts. Management Science, 50, 2 (February 2004), 222–238.

6. Cachon, G.P., and Fisher, M. Supply chain inventory management and the value of shared information. Management Science, 46, 8 (August 2000), 1032–1048.

7. Cachon, G.P., and Lariviere, M.A. Contracting to assure supply: How to share demand forecasts in a supply chain. Management Science, 47, 5 (May 2001), 629–646.

8. Cachon, G.P., and Lariviere, M.A. Supply chain coordination with revenue-sharing contracts: Strengths and limitations. Management Science, 51, 1 (January 2005), 30–44.

9. Cheng, H.K., and Koehler, G.J. Optimal pricing policies of Web-enabled application services. Decision Support Systems, 35, 3 (June 2003), 259–272.

10. Cotton, I.W. Microeconomics and the market for computer services. Computing Surveys, 7, 2 (June 1975), 95–111.

11. Dai, R.; Narasimhan, S.; and Wu, D.J. Buyer’s efficient e-sourcing structure: Centralize or decentralize? Journal of Management Information Systems, 22, 2 (Fall 2005), 141–164.

12. Davison, D. ASP pricing parameters. White paper, Meta Group, New York, June 12, 2000.

13. Demirkan, H., and Cheng, H.K. The risk and information sharing of application services supply chain. European Journal of Operational Research, 187, 3 (June 2008), 765–784.

14. Ellinger, A.E. Improving marketing/logistics cross-functional collaboration in the supply chain. Industrial Marketing Management, 29, 1 (January 2000), 85–96.

15. Gavirneni, S. Information flows in capacitated supply chains with fixed ordering costs. Management Science, 48, 5 (May 2002), 644–665.

16. Gavirneni, S.; Kapuscinski, R.; and Tayur, S. Value of information in capacitated supply chains. Management Science, 45, 1 (January 1999), 16–24.

17. Ha, A.Y. Optimal pricing that coordinates queues with customer-chosen service requirements. Management Science, 47, 7 (July 2001), 915–930.

18. Jeuland, A.P., and Shugan, S.M. Managing channel profits. Marketing Science, 2, 3 (Summer 1983), 239–272.

19. Lee, H.L.; Padmanabhan, P.; and Whang, S. Information distortion in a supply chain: The bullwhip effect. Management Science, 43, 4 (April 1997), 546–558.

20. Mendelson, H. Pricing computer services: Queuing effects. Communications of the ACM, 28, 3 (March 1985), 312–321.

21. Mendelson, H. Economies of scale in computing: Grosch’s law revisited. Communications of the ACM, 30, 12 (December 1987), 1066–1072.

22. Monahan, J.P. Quantity discount pricing model to increase vendor profits. Management Science, 30, 6 (June 1984), 720–726.

23. Pasternack, B.A. Optimal pricing and return policies for perishable commodities. Marketing Science, 4, 2 (Spring 1985), 166–176.

24. Roddy, D.J. The Internet-Based ASP Marketplace: Renaissance of the Value-Added Network. New York: Deloitte Research, 1999.

25. Rubens, P. IBM, Microsoft and Sun—Just here to help? ASPNews.com (December 6, 2001) (available at www.aspnews.com/trends/article.php/935601).

26. Selwyn, L.L. Economies of scale in computer usage initial tests and implications for the computer utility. Technical Report TR‑ 68, MIT, Cambridge, MA, 1970.

27. Silver, E.A., and Peterson, R. Decision Systems for Inventory Management and Production Planning. Hoboken, NJ: John Wiley & Sons, 1975.

28. Wang, Y.; Jiang, L.; and Shen, Z.J. Channel performance under consignment contract with revenue sharing. Management Science, 50, 1 (January 2004), 34–47.

29. Weir, M.H. SAP launches “new era” with on-demand software. Information Week (September 19, 2007) (available at www.informationweek.com/news/internet/showArticle. jhtml?articleID=201807556).

30. Weir, M.H. SAP readies software-as-a-service offering in 2008. Information Week (April 23, 2007) (available at www.informationweek.com/news/software/hosted/showArticle. jhtml?articleID=199200902).

31. Weng, Z.K. Manufacturing and distribution supply chain management: Alliances and competition. Report 99–117, Marketing Science Institute, Cambridge, MA, 1999 (available at www.msi.org/publications/publication.cfm?pub=531).

## Appendix

Proof of Concavity

$S P _ { \mathrm { 1 } } ( p , \mu )$ in Equation (7) is strictly concave in both $p$ and $\mu$ if and only if

$$
\frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d \mu^ {2}} \leq 0, \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d p ^ {2}} \leq 0,
$$

and the determinant of the Hessian matrix

$$
\Delta_ {1} = \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d \mu^ {2}} \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d p ^ {2}} - \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d \mu d p} \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d p d \mu} \geq 0
$$

is positive.

After some algebra, we find that

$$
\frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d p ^ {2}} = 0, \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d \mu^ {2}} = - 2 e, \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d p d \mu} = \frac {d S P _ {1} ^ {\prime \prime} (p , \mu)}{d \mu d p} = 0,
$$

and $\Delta _ { \scriptscriptstyle 1 } = 0$ . The objective function of Scenario 1 is thus strictly concave in both $p$ and m. Q.E.D.

## Proof of Proposition 1

In this scenario, the ASP solves the following problem to find his or her optimal profit:

$$
\max _ {p, \mu} p \lambda - w \mu
$$

such that

$$
V ^ {\prime} (\lambda) = p + v T (\lambda , \mu)
$$

and $\lambda < \mu$

After some algebra, the first-order conditions lead to

$$
\mu_ {2} ^ {*} = \frac {\rho_ {2} ^ {*} k ^ {2}}{4 w ^ {2}} = \frac {k ^ {2}}{4 w ^ {2}} \left(1 - 2 \sqrt {\frac {v w}{k ^ {2}}}\right), \rho_ {2} ^ {*} = 1 - 2 \sqrt {\frac {v w}{k ^ {2}}},
$$

and

$$
p _ {2} ^ {*} = \frac {k \left(\frac {k}{w} \sqrt {\frac {v w}{k ^ {2}}}\right) - v}{\frac {k}{2 w} \left(1 - 2 \sqrt {\frac {v w}{k ^ {2}}}\right) \left(\frac {k}{w} \sqrt {\frac {v w}{k ^ {2}}}\right)}.
$$

Q.E.D.

Proof of Proposition 3

Because

$$
\frac {d \mu_ {4 , A I P} ^ {*} (w)}{d w} = \frac {1}{2 e} > 0
$$

and

$$
\frac {d \mu_ {4 , A S P} ^ {*} (w)}{d w} = - \frac {k ^ {2}}{2 w ^ {3}} + \frac {3 k \sqrt {v}}{4 w ^ {5 / 2}} <   0,
$$

$\mu _ { 4 , A I P } ^ { * }$ is a strictly increasing function of w and $\mu _ { 4 , A S P } ^ { * }$ is a strictly decreasing function of w. Thus, there exists a unique solution in the aligned scenario described by $\mu _ { 4 , A I P } ^ { * } ( w ) = \mu _ { 4 , A S P } ^ { * } . \mathrm { Q . E . D }$
