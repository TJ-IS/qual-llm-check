---
otero_id: 7304
otero_key: "CPZPE2E7"
title: "Building an automatic e-tendering system on the Semantic Web"
authors: "Timon C. Du"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building an automatic e-tendering system on the Semantic Web

Timon C. Du ⁎

Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Hong Kong

a r t i c l e i n f o

Article history: Received 5 January 2008 Received in revised form 16 December 2008 Accepted 19 December 2008 Available online 12 January 2009

Keywords: Web automation Semantic Web Negotiation P2P e-Tendering system

## a b s t r a c t

Over the years, business-to-business (B2B) e-commerce applications have been well researched, but the degree of automation achieved has been limited. This is probably because the current content of the Web is designed for human comprehension, rather than for computer operations. In B2B, an e-tendering system needs to contact a large number of potential sellers and negotiate deals with them. It would be helpful if this process could be carried out automatically. This study proposes an automatic e-tendering system that implements an automatic negotiation process over the Semantic Web in which Web pages provide information not only through their content, but also through the properties of that content. The e-tendering system integrates a negotiation process that considers bargaining power and risk preference of negotiators. The semantic data then are used to select tenders or to determine negotiation strategies. A system is built in a peer-to-peer (P2P) environment to simulate a two-player negotiation process for demonstration purposes. The system can automatically derive negotiation results for different risk preferences (such as risk neutrality, risk aversion, or risk proneness) and degrees of negotiating power (such as the cost of haggling).

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Many types of dynamic pricing schemes have recently emerged in the electronic marketplace. These systems are built to allow negotiation in various scenarios, such as bargaining between a single buyer and seller, forward auctions between multiple buyers and one seller, reverse auctions between one buyer and multiple sellers, and dynamic exchanges between multiple buyers and multiple sellers. The electronic auctions of eBay and Dell and the reverse auctions of GE and GM provide some successful examples of these systems. Tendering is a kind of reverse auction in which suppliers bid on the services or goods that buyers need [31]. As more applications move to the Web, the need for automated and ef<sup>fi</sup>cient systems will grow correspondingly.

In this study, we propose an automatic e-tendering framework, called the auto-tendering system (ATS), on a peer-to-peer (P2P) platform that allows both buyers and sellers to negotiate a deal automatically by considering the bargaining power of both parties. The ATS is an e-tendering system that manages purchases for a large organizational buyer. The automation is achieved through the use of Semantic Web [4].

The P2P architecture offers a decentralized and distributed network that eliminates coordination bottlenecks [13]. A pure P2P information-sharing network is basically an information directory in which explicit knowledge is maintained on local systems [8,17]. In the ATS, two-party negotiation is conducted in a P2P environment. The system allows negotiation to be carried out in a one-to-one, but concurrent, manner, with the seller who makes the best offer winning the tender. A utility function that represents the anticipated payoff for each party is employed to determine the settlement or the best offer. The bargaining power of the negotiators, as calculated by the relative magnitude of their respective costs of haggling and their risk preference, is determined to achieve the settlement.

We assume that in the automatic negotiation process, the two parties have a common interest in cooperating, but also con<sup>fl</sup>icting interests over exactly how to cooperate [21]. There are many de<sup>fi</sup>nitions of negotiation. Oliver [23] considered negotiation to be simply a search process in a multidimensional problem in which each solution is considered as a dimension. Krovi et al. [16] de<sup>fi</sup>ned negotiation as a way to resolve issues between two or more parties that take opposite positions. Nunes et al. [22] assumed negotiation to be the decision-making process by which a consensus is reached between collaborative parties, rather than between opponents. This study considers negotiation to be a multi-criteria decision-making (MCDM) problem, or a multi-attribute decision-making problem, in which many criteria are taken into account as the attributes of decision-making [32].

Over the past decade, many researchers have investigated negotiation systems. In general, these systems can be categorized into automated negotiation systems (ANSs) and negotiation support systems (NSSs). ANSs emphasize the building of automatic negotiation processes, whereas NSSs provide information and strategies to the negotiators. ANSs mainly employ intelligent agents or mobile agents that travel between computers to simplify the negotiation process using machine-learning techniques such as genetic algorithms [23], rule-driven reasoning [3], game theory [32], fuzzy logic [14], ebXML [26], and probabilistic negotiation agent [18]. In contrast, NSSs mainly suggest solutions or provide process support, and they have been adopted for use in social-judgment theory models, genetic algorithms [20], hyper-game decision models, bargaining models, and multiobjective linear programming [1]. Kromker et al. developed software to support the distribution of processes in a heterogeneous system environment in the preparation of tendering bids that require interdisciplinary cooperation [15]. In [6], a negotiation support system was proposed that uses active documents with embedded business logic or rules that can be adapted for different collaborative strategies. However, the current research on negotiation systems focuses either on system development or machine intelligence, rather than on the negotiation process itself. Its focus on the negotiation process of different risk preferences (such as risk neutrality, risk aversion, or risk proneness) and degrees of negotiating power (such as the cost of haggling) is thus this study's major distinction in relation to the current literature.

In the ATS, semantic information can be used to locate suppliers and estimate the bargaining power of opponents and itself. The negotiators can then choose the negotiating power and different negotiation strategies that consider different risk preferences.

The remainder of this paper is organized as follows. Section 2 reviews the Semantic Web and Web automation, and Section 3 discusses the auto-tendering framework. A demonstration of the system is presented in Section 4, and a conclusion is provided in Section 5.

## 2. Semantic Web

The Semantic Web organizes Web content into information (facts) and the meaning of that information. Like the World Wide Web, the Semantic Web encourages the independent and diversi<sup>fi</sup>ed growth of Web sites while maintaining a high degree of information sharing. However, on the Semantic Web, a Web page provides information not only in terms of content, but also in terms of the properties, known as attributes, of that content. In this way, the use of information is not limited to the exploration of its content, but can be extended to the investigation of its properties. This development has increased the possibility of creating a highly automated and integrated Web service [2,5,7].

Since the W3 Consortium <sup>fi</sup>rst put forward the concept of the Semantic Web in 1999, several applications have been successfully implemented, such as card index information, privacy information (P3P), the association of style sheets with documents, the labeling of intellectual property rights, and multilingual transaction [28]. In the tendering domain, an algorithm has been developed that extracts the ontology from the structured data in an electronic data interchange message [10]. Another successful application is an electronic government procurement system that posts and receives bids via the Internet and carries out vendor registration, certi<sup>fi</sup>cate authorization, contract development tools, bids/requests for proposal (RFP) development, online bidding, and online payment to render government procurement ef<sup>fi</sup>cient, transparent, nondiscriminatory, and accountable [19]. Semantic process templates have been developed that use ontology to capture much richer descriptions of activity requirements to create a more effective way of providing Web services [11,29]. The conceptual architecture of both Semantic Web and traditional HTML Web services enables Semantic Web Service design and composition at the knowledge level in a language-independent manner [9].

## 3. Auto-negotiation process

This study develops an auto-negotiation process for an automatic e-tendering system that considers bargaining power of negotiation parties. The system provides higher degree of automation using Web semantics, integrates negotiation process into e-tendering system, and considers bargaining power and risk preference of negotiators.

## 3.1. An automatic e-tendering system using semantics

The semantics of negotiation are expected to appear in three realms in which there is incomplete information. Here, incomplete information means that one party has some knowledge in common with an opponent, but also has private knowledge that is unknown to the other party.

In the <sup>fi</sup>rst realm, semantic information can be used to select partners or services dynamically [32]. The partners are selected from a community based on preset criteria, whereby in an e-tendering system, a buyer (b) can locate a seller (s). In general, two types of relationships are presented in the ontology: “is-a-kind-of” and “is-apart-of.” The “is-a-kind-of” relationship is normally used to describe product type and to categorize products, and it can be easily determined from product descriptions and catalog keywords. However, gaining knowledge about the “is-a-part-of” relationship requires help from the ontology. For example, knowing that a monitor is a part of a PC can help a company that sells monitors to become a candidate for tenders that are selling PCs if the vendors that sell the other components can be found.

In a P2P environment, each node in a network is known as a peer. As peers may be located behind <sup>fi</sup>rewalls and Network Address Translations (NATs), some of the nodes need to carry out routing and translating work. These peers, also known as relays, include rendezvous peers, router peers, and gateway peers. The ATS <sup>fi</sup>rst searches for suppliers that sell products that exactly match the needs of the buyer, then uses “a-kind-of” information, followed by “a-partof” information to locate additional suppliers.

The negotiation strategies in the ATS are kept at each node, whereas the ontology is maintained in the relay peer. In general, this ontology is not modi<sup>fi</sup>ed frequently, and updates to the relay peer should be conducted only when all of the relay peers have reached a consensus.

The second realm in which the semantics of negotiation appears is the bargaining power of each party, which can be determined by the relative magnitude of the negotiators' respective costs of haggling and their utility, which varies with the degree of risk preference. The costs of haggling include time discounting, deadlines, time constraints (waiting-time costs), and inventory levels, whereas risk preference describes the attitude of the negotiator: whether it is risk neutral, risk averse, or risk prone. A negotiator is considered to be a patient player if the time-discounting rate is small. The information provided on the Web can be used to adapt the negotiation strategies. For example, the price of raw materials or the interest rate can affect the risk preference of a negotiator. In the Semantic Web, as depicted in [4], this information can be retrieved automatically, and the negotiator can change its risk preference setting in the ATS.

Each entity in the ATS that participates in the negotiation process must have a negotiation engine. The engines of the negotiating parties then determine the results, based on their respective bargaining power. Models that assume a constant discount rate of future utilities, such as that of Rubinstein [27], are modi<sup>fi</sup>ed for this purpose.

The third realm is related to the different strategies that can be adopted in the negotiation process. For example, new issues can be created to transform single-issue, <sup>fi</sup>xed-line negotiation into integrative negotiation [30]. An offer can be made either just once or issueby-issue, which unbundles bargaining issues. Alternatively, the weights of the bargaining issues can be changed, or multiple offers can be made simultaneously.

## 3.2. An integrated negotiation process

Formally speaking, a negotiation issue, such as the price that is offered by one negotiator, is denoted in the range of [I , R ], where $i \in \{ b , s \} , \ I$ I is the initial offer, and R is the reserve price. A buyer locates a seller to engage in further bargaining $\begin{array} { r } { \mathrm { i f } \sum _ { j } I _ { s j } \ge \sum _ { j } R _ { b j } , } \end{array}$ where $j = \{ 0 , 1 , . . . , n \}$ if multiple issues are at stake, such as the delivery time, the quantity of items required, the inventory level, and the payment method. Both parties then determine the best alternative to a negotiated agreement (BATNA) by referring to the reservation points. The <sup>fi</sup>rst bid from a seller to a buyer is ${ 0 } _ { s  b } ^ { ~ t } ,$ where $t = 1$ after the request for quotation (RFQ) has been received from buyer $b , t { \in } T ,$ and $T = \{ 0 , 1 , . . . , m \}$ . The buyer will accept the bidding if it is known that the utility value of the next offer may not be better than the current offer, i.e., $U _ { b } ( o _ { s  b } ^ { ~ t } ) \geq U _ { b } ( o _ { s  b } ^ { t } )$ , where U is the utility function of b obtained from the offer of seller s at time t compared with that obtained at time t+1. Similarly, the seller will accept a counter offer if it is known that the utility of the next offer may not be better than the current bid, that is, $U _ { s } ( { \bar { o _ { b } } } ^ { t } { \bf \Pi } _ {  s } ^ { t } ) \ge U _ { s } ( { o _ { b } ^ { t } }  s )$

![](/api/attachments/CPZPE2E7/fulltext/images/63c468b05f92f2b624aa38605a03d6af9d414fc6b23e131d259446bfe288116f.jpg)  
Fig. 1. Framework of the Automatic Tendering System (ATS).

The auto-negotiation process is a type of MCDM problem, in that more than one issue is taken into consideration. The weighted issues are converted into utility values to measure the satisfaction of both negotiating parties. The utility function represents the anticipated payoff to each party that corresponds to that party's selected strategy (http://en.wikipedia.org). A company can make a choice between a certain alternative and a risky alternative to depict its utility function. However, the way in which the utility function of a negotiator (whether an individual or an organization) can be obtained from the semantics of Web pages is beyond the scope of this study. Please refer to [6] for more details.

The multi-attribute utility theory (MAUT) can be adopted to help a decision-maker quantify and derive solutions that have multiple criteria. The total utility can be obtained by summing the weighted issue utilities, that is, $\begin{array} { r } { U = \frac { \sum W _ { i } \times U _ { i } } { \sum W _ { i } } } \end{array}$ , where U is the total utility value and ranges between 0 and 1, i is the negotiation issue, $U _ { i }$ is the utility value of an issue and ranges between 0 and 1, and W is the weight of the issue and ranges between 1 and 9. Applying the Neumann–Morgenstern utility function for modeling [12] gives

$$
U _ {i} \Big (o _ {i \to i ^ {\prime}} ^ {t} \Big) = U _ {i} (o) U _ {i} (t),\tag{1}
$$

where $U _ { i } ( \boldsymbol { o } )$ is the utility function of negotiator i that is derived from the offer of the other negotiator $i ^ { \prime } , U _ { i } ( t )$ is a consideration of the discount factor $f ( \alpha ) ^ { t }$ of issue i at time t, and α is the discount rate. The discount rate can be determined at the beginning of the negotiation if it is a constant. The negotiator is a patient player if $\alpha { > } 1 .$ . This means that the utility value of issue i will not decrease over the time period. In this study, the discount factor is a factor of the cost of haggling, and it can be determined from the semantic data. The utility function is measured in a linear function as follows.

$$
U _ {j} ^ {i} \left(o _ {j, i ^ {\prime} \rightarrow i} ^ {t}\right) = \frac {O _ {j} - R _ {j}}{I _ {j} - R _ {j}}\tag{2}
$$

for the seller for issue $j ,$ and

$$
U _ {j} ^ {i} \left(o _ {j, i ^ {\prime} \rightarrow i} ^ {t}\right) = \frac {R _ {j} - O _ {j}}{R _ {j} - I _ {j}}\tag{3}
$$

for the buyer for issue j.

The interaction of the utility functions of both parties forms a bargaining zone. A positive bargaining zone implies that there is room for both parties to reach an agreement.

The counter-offer consists of a tactic to vary the acceptance value of an issue depending on the remaining negotiation time [12]:

$$
o _ {i \to i ^ {\prime}} ^ {t} (j) = \left\{ \begin{array}{l l} I _ {j} ^ {i} + \mu_ {j} ^ {i} (t) \left(R _ {j} ^ {i} - I _ {j} ^ {i}\right) & \text { if } i = b \\ I _ {j} ^ {i} + \left(1 - \mu_ {j} ^ {i} (t)\right) \left(R _ {j} ^ {i} - I _ {j} ^ {i}\right) & \text { if } i = s \end{array} \right..\tag{4}
$$

Function $\mu _ { j } ^ { i } ( t )$ is called the negotiation decision function for issue j for negotiator i, and is de<sup>fi</sup>ned as

$$
\mu_ {j} ^ {i} (t) = k _ {j} ^ {i} - \left(1 - k _ {j} ^ {i}\right) \left(\frac {t}{T ^ {i}}\right) ^ {1 / \varphi}.\tag{5}
$$

The negotiation decision function should be between 0 and 1 (i.e., $0 \leq \mu _ { j } ^ { i } ( t ) \leq 1 )$ to ensure that a settlement can be reached. At time 0, $\mu _ { j } ^ { i } ( 0 ) = 1$ is a constant value that determines the initial counter proposal. When $t = T ,$ the maximum time is $\mu _ { j } ^ { i } ( T ) = 1$ , and the counter offer will be the reservation value, as the deadline has been reached.

The risk preference can be re<sup>fl</sup>ected through the negotiation decision function, in which a risk-prone attitude leads to the adoption of Boulware behavior [25], a risk-averse attitude leads to the adoption of conceder behavior [24], and a risk-neutral attitude leads to the showing of no preference. The Boulware tactic takes φb1, whereas the conceder tactic takes φN1. By adopting Boulware behavior, the negotiator maintains an offer that is close to the initial offer until the deadline nears. In contrast, a conceder gives way to the reservation value quickly.

![](/api/attachments/CPZPE2E7/fulltext/images/5f4d68970286898557a57496e946c7539181dbe0771e829eb6d1f7ad7d48e98a.jpg)  
Fig. 2. Negotiation process in IDEF (Http//syque.com).

Eq. (5) considers the haggling cost as the constraint. However, many other resources should also be taken into consideration, such as the current inventory level and the consumption rate. Therefore, Eq. (5) can be further revised into

$$
\mu_ {j} ^ {i} (t) = k _ {j} ^ {i} - \left(1 - k _ {j} ^ {i}\right) (X) ^ {1 / \varphi},\tag{6}
$$

where X is the combination of all resources.

## 4. e-Tendering system and demonstration

An e-tendering platform called the ATS framework is developed for demonstration purposes (see Fig. 1). This framework allows a buyer to locate potential suppliers in the P2P community and negotiate a contract, and it enables the negotiators to set different negotiation strategies and risk preferences and to evaluate both their own negotiating power and that of their opponents. The negotiation process can be carried out automatically if the ontology exists and the necessary information can be accessed from the Web. Negotiation is carried out in a one-to-one manner between buyer and seller, but many negotiation processes can be activated concurrently.

As shown in Fig. 2, the auto-tendering process includes four steps. In the <sup>fi</sup>rst step, the system accepts purchasing requests from internal departments. It then refers to the product ontology and activates the supplier selection process. In this process, the multiple negotiation issues are decomposed into different combinations of issues to satisfy the purchase request. For example, information on the bill-ofmaterials and possible substitutes in the product ontology will be referred to decompose and prioritize the negotiation issues. The possible suppliers can be identi<sup>fi</sup>ed by retrieving them from the Semantic Web services based on the product items and the negotiation issues. Then, the possible supplier list becomes the input to the autonegotiation step, in which four sub-processes are included. To determine the negotiating power, the current status of a speci<sup>fi</sup>c negotiation issue is acquired. For example, the current inventory level is used to determine the urgency of acquiring a component. In is common sense that the greater the urgency, the lower the negotiating power can be. The next step is to determine the risk preference. In this step, the decision maker can measure its own risk preference and that of its opponents (suppliers) using the information from the Semantic Web. Together, the negotiating power and the risk preference then determine the <sup>fi</sup>nal deal (experiments are provided later). Negotiations with more than one opponent (suppliers) can be initiated concurrently. During the negotiation process, the utility function is used to describe the satisfaction levels of the two negotiating parties, and the process stops when a satisfactory result has been derived. Acceptable results then become an agreement in the <sup>fi</sup>nal step.

Note that in a multiple-issue negotiation situation, there are two scenarios. In the <sup>fi</sup>rst, the buyer negotiates two or more issues (such as price and delivery time) for the same product with a supplier, and, in the second, it negotiates one issue for two or more products with the same supplier. As has been discussed, the <sup>fi</sup>rst scenario considers the multi-attribute utility by summing the weighted issue utilities, that is, $\begin{array} { r } { U = \frac { \sum \bar { W } _ { i } \breve { \times } \bar { U } _ { i } } { \sum \bar { W } _ { i } } } \end{array}$ , whereas the second scenario is an example of an “a-<sup>i</sup>part-of” relationship, in which the pricing strategy is the same as it would be in a single-issue negotiation, except that the utility is the combination of the utility gained from two or more products. In this case, the utility is de<sup>fi</sup>ned as the sum of the utility of the individual products. For example, the utility can be $\begin{array} { r } { U _ { i } = \sum _ { j } u _ { i j } { ^ { * } b } _ { i j } } \end{array}$ where $u _ { i j }$ is the utility of product i of issue j, and b is the weight of product i of issue j. The negotiator can aggregate the negotiation results that are delivered from the different negotiation processes and select the best combination. Alternatively, the negotiator can also change its negotiation strategy and initiate a new negotiation process.

To demonstrate the ATS, a system has been developed to simulate the automated negotiation process using JXTA™, which was developed by Sun Microsystems. The JXTA technology is a set of P2P open protocols that can connect various devices to a network that ranges from cell phones and wireless PDAs to PC servers. JXTA peers create a virtual network in which a node can interact with other peers or resources directly, even when they are behind a <sup>fi</sup>rewall or have different network transports. Basically, the system includes nine classes: buyer, seller, product, P2PQueryMsg, P2PResponeMsg, P2PNeg, P2PHandler, CustomerInfo, and ResolverService. Brief descriptions of these classes are provided in Table 1. The operation includes peer location and negotiation processes.

## 4.1. Locate peer and negotiate

In a traditional B2B marketplace (such as Alibaba.com and Covisint), there is usually a central server that receives and routes queries and messages (such as RFQs, acknowledgments, or counter offers) between the buying and selling parties. In an e-tendering system, the buyer can contact sellers either actively (by sending an RFQ to solicit sellers) or passively (by posting an RFQ on its own Web page). The communication between the buyer and the sellers is thus primarily managed by the buyer's server. Therefore, the system demand is scalable and <sup>fl</sup>exible, and a centralized marketplace may not be appropriate. It is thus better suited to implementation in a P2P environment.

Description of the e-tendering class diagram.

<table><tr><td>Class</td><td>Method</td><td>Description</td></tr><tr><td>Buyer</td><td>double cal_offer (int cur_time, Product prod, double k, double ini_price, double res_price)</td><td>Generates offers and counter-offers. It first finds the stock of the materials, and then checks the inventory level and turnover rate of the products that it uses. It computes the negotiation deadline based on these figures, and finally calculates the offer price.</td></tr><tr><td>Seller</td><td>double cal_offer (int cur_time, Prodcut prod, double k, double ini_price, double res_price)</td><td>Generates offers and counter-offers. It computes the deadline of the negotiation based on data that it has found on the Semantic Web, and then calculates the offer price.</td></tr><tr><td>Product</td><td>int getStock()</td><td>Obtains the inventory level of products.</td></tr><tr><td>Product</td><td>int getTurnover()</td><td>Finds the turnover rate of products.</td></tr><tr><td>P2PQueryMsg</td><td>P2PQueryMsg (String peer_id, String material_id, int t, String seller_id, double inventory)</td><td>Constructs a query message, with the attributes and values specified.</td></tr><tr><td>P2PQueryMsg</td><td>P2PQueryMsg (InputStream stream)</td><td>Constructs a query message with an XML document.</td></tr><tr><td>P2PQueryMsg</td><td>boolean comUtility (offer_price)</td><td>Compares the utility that the buyer would gain from its proposed price with that which the buyer would obtain from the current price offered by the seller.</td></tr><tr><td>P2PResponseMsg</td><td>P2PResponseMsg (String peer_id, String material_id, int t, String seller_id, double inventory)</td><td>Constructs a response message, with the attributes and values specified.</td></tr><tr><td>P2PResponseMsg</td><td>P2PResponseMsg (InputStream stream)</td><td>Constructs a response message with an XML document.</td></tr><tr><td>P2PResponseMsg</td><td>boolean comUtility (double proposed_price)</td><td>Compares the utility that the seller would gain from its offered price with that which the seller would obtain from the current price proposed by the buyer.</td></tr><tr><td>P2PNeg</td><td>void manageHandler()</td><td>Registers or de-registers the command.</td></tr><tr><td>P2PNeg</td><td>int parseArguments()</td><td>Parses the arguments following the command.</td></tr><tr><td>P2PNeg</td><td>int startApp()</td><td>Starts the application by sending out an initial query.</td></tr><tr><td>P2PHandler</td><td>int processQuery (P2PQueryMsg qmsg)</td><td>Seller peer processes. The price proposed by the buyer is accepted if it is considered reasonable; otherwise, the seller makes a counter-offer.</td></tr><tr><td>P2PHandler</td><td>void processResponse (P2PResponseMsg rmsg)</td><td>Buyer peer processes. The price proposed by the buyer is accepted if it is considered reasonable; otherwise, the buyer makes a counter-offer.</td></tr></table>

With the help of JXTA technology, locating peers becomes simple in the P2P environment. In Fig. 3, Peer 1 (the buyer) searches among suppliers (the sellers) for a product or product components using the following steps.

(1) Peer 1 initiates a search request for suppliers.

(2) As the suppliers are located outside of the company, Peer 1 does not search for peers on the Intranet.

(3) The node locates its associated relay peer <sup>fi</sup>rst, as only relay peers can interact with outside parties in JXTA. In this example, Peer 1 would like to communicate with outside peers, so it sends a query to a relay peer, Peer 3.

(4) Peer 3 has cached information about the other relay peers with which it is associated. In this example, it <sup>fi</sup>nds relay Peers 4 and 10.

(5) Peers 4 and 10 then search for peers that belong to their own local network and obtain responses from Peers 6 and 11, respectively.

(6) A relay peer can forward the query to other relay peers if these relay peers have not yet participated. Here, Peer 4 forwards the query to Peer 5 and receives a new reply from Peer 8.

(7) All of the replies are then sent back to Peer 3 and are eventually sent back to the initiator, Peer 1.

After the peers have been located, the negotiation process starts when the buyer sends an RQF to the suppliers. More than one supplier can be located. Then, a supplier (or buyer) compares the utility that would be gained from the offered price with that which would be obtained from the current price proposed by the buyer (or supplier), and the generation of offers and counter-offers by computing the deadline of the negotiation based on data found on the internal Intranet and the public Web. The system then calculates the offer price and sends it to the buyer (or supplier). A counter-offer from the buyer (or seller) is made by comparing the utility that the buyer (or seller) would gain from its proposed price with that which would be gained from the current price offered by the seller. The system then gauges the inventory level of the product, <sup>fi</sup>nds its turnover rate, obtains the built-in information about the negotiation strategies and risk preferences of the buyer (or seller), and then sends the offer to the supplier (or buyer). This process is repeated until a settlement that satis<sup>fi</sup>es both parties is reached, if one exists. Finally, the seller selects the best <sup>fi</sup>nal offer from among the offers of all of the suppliers and makes a deal with the selected supplier.

This approach has several advantages. First, no centralized server is needed to manage the queries and responses, because in a P2P environment, a peer is both client and server and is thus able to handle all of the necessary transactions. Second, peers share the transaction overheads. Although it seems that the relay peer is handling more work, the workload is not as heavy as it would be in a centralized approach, because the relay peer only forwards queries between outside parties and its own peers. Third, the P2P approach only needs the spare resources of current machines, rather than requiring the installation of new workstations to perform centralized jobs.

## 4.2. Experiments

After identifying suppliers, a buyer can negotiate with many suppliers concurrently. This section demonstrates how a negotiator can change strategies and negotiating power to affect the negotiation results in a one-to-one negotiation process. In this demonstration, the counter-offer considers the risk preference of the negotiators, which means that a Boulware tactic [25], φb1, and a conceder tactic [24], φN1, are adopted. The discount rate determines whether a participant is a patient player or an impatient player. For a buyer, the costs of haggling include time discounting, deadlines, time constraints (waiting time costs), inventory levels, and other costs. For a supplier, these costs may be determined by (1) customer classi<sup>fi</sup>cation, such as size, technology, sales, market share, business quality, market focus, and willingness to partner; (2) product factors, such as pro<sup>fi</sup>tability, competitive offering, the value that customers place on the product, and patent potential; and (3) market segmentation, whether growing, strategically important, <sup>fi</sup>nancially attractive, or responding well to a manufacturer's brands.

We use a single negotiation issue, i.e., the price, to illustrate the proõcess. The reserve price of the buyer is set at 130, and the range of prices that are acceptable to the buyer is [120, 130]. As discussed previously, the negotiation decision function μ<sup>i</sup>(t) is determined by $\begin{array} { r } { \dot { \mu } ^ { i } ( t ) = k ^ { i } - \left( 1 - k ^ { i } \right) \left( \frac { t } { T ^ { i } } \right) ^ { 1 / \varphi } } \end{array}$ , where $0 < k ^ { i } < 1 .$ If the initial offer is derived from $I ^ { i } + \mu ^ { i } ( 0 ) ( R ^ { i } - I ^ { i } )$ , then that from the buyer is 100+ $0 . 2 ^ { * } ( 1 3 0 - 1 0 0 ) { = } 1 0 6 { \mathrm { ~ i f ~ } } k ^ { b } = 0 . 2$ . Similarly, the reserve price of the

![](/api/attachments/CPZPE2E7/fulltext/images/7a86a334b531b28add22c924e5d231cb4a1101f262ff79c4b7fea13d8a924ede.jpg)  
Fig. 3. Example of peer location in a P2P environment.

![](/api/attachments/CPZPE2E7/fulltext/images/7aaf2baa561a4608129151ce8ed6f25193cc73f143d77f6ce3ca0f0be09119e1.jpg)  
Fig. 4. Final prices of <sup>fi</sup>ve types of sellers when the buyer is a linear buyer (X-axis represents the different utility discount rate of a buyer and Y-axis represents the price).

![](/api/attachments/CPZPE2E7/fulltext/images/31b058723e888af0039a29b329005fb6a9bc16652c3303d480bdfaa9f6eb9c30.jpg)  
Fig. 5. Negotiation attempts of <sup>fi</sup>ve types of sellers when the buyer is a linear buyer (X-axis represents the different utility discount rate of a buyer and Y-axis represents the number of attempts).

seller is set at 110, and the price that is acceptable to the seller is [130, 150]. With the same constant, $k ^ { b } = 0 . 2 ,$ , the initial offer from the seller to the buyer is $1 5 0 + 0 . 2 ^ { * } ( 1 1 0 - 1 5 0 ) = 1 4 2$ . Note that the overlapping of the price at [130, 130] creates the possibility that the two parties will reach a settlement. In this demonstration, <sup>fi</sup>ve types of sellers are considered: a Boulware seller $( \varphi = 0 . 0 2 )$ , a conceder seller $( \varphi = 5 0 )$ , a linear seller $( \varphi = 1 )$ , a linear-to-Boulware seller $( \varphi = 0 . 5 )$ and a linear-to-conceder seller $( \varphi = 2 )$ . All of the negotiation scenarios are repeated 30 times. The negotiating power of the buyer is determined by the discount rate α of the negotiator, with a typical inventory level and consumption rate, as sampled from a normal distribution [0, 2], being taken into consideration. If αN1, then the negotiator is said to be patient and its negotiating power strong, whereas at αN1 the negotiator is impatient and has weak negotiating power.

![](/api/attachments/CPZPE2E7/fulltext/images/2525018be12e3b172fd8bc68b62cba6495df3c478f01f52450eda37ba7992e05.jpg)  
Buyer Utility Discount Rate  
Fig. 6. Final settlements with various buyer–seller risk preferences (X-axis represents different utility discount rates of a buyer and Y-axis represents the price).

Fig. 4 shows the negotiation outcomes when the buyer has a linear risk preference and the sellers have various risk preferences. The <sup>fi</sup>gure shows that if the seller is a Boulware seller, then the price stays at that seller's initial offer, regardless of the time sensitivity of the buyer (different utility discount rates, as discussed in Eq. (1)). In contrast, the price goes down immediately if the seller is a conceder seller. If the seller is a linear or neo-linear seller $( \varphi = 0 . 5 \ \mathrm { o r } \ \varphi = 2 )$ then the <sup>fi</sup>nal price drops if the negotiating power (or patience) of the buyer increases.

Fig. 5 shows the number of negotiation attempts made in the experiment. As can be seen, the number of attempts made by the Boulware seller is <sup>fi</sup>xed at 10 (and the price is <sup>fi</sup>xed at 142). This is because the deadline T for the negotiations was set at 20, and thus the average number of negotiation attempts is 10. This clearly shows that if a buyer is patient, then the number of negotiation attempts will increase for all types of sellers.

Fig. 6 shows the results if the buyer and seller have different combinations of risk preferences. If the seller adopts Boulware behavior, then the <sup>fi</sup>nal price is settled at 142, regardless of whether the buyer is a conceder or is linear. This means that no deal will be reached, as the price is higher than the reserve price of the buyer. However, if the buyer switches to a Boulware strategy, then a very successful deal can be achieved if that buyer is patient. Furthermore, as long as the buyer is both patient and aggressive (that is, it does not adopt a conceder strategy), then the <sup>fi</sup>nal deal will normally satisfy its desires, regardless of the seller's strategy.

## 5. Conclusions

This study proposes an automatic e-tendering system for the Semantic Web. An auto-tendering system (ATS) has been developed to demonstrate the automatic negotiation process that considers different risk preferences and degrees of negotiating power. The system is built in a P2P environment to simulate a two-player negotiation process that is conducted in a one-to-one manner, and it results in the selection of the best offer as a tender. In the P2P environment, a peer normally has a negotiation engine with which to carry out the negotiation process, as well as a strategy module that allows the negotiator to change strategies. A relay peer keeps a list of peers to locate partners and maintains an ontology base. In the ATS, the ontology of semantic information can be used to locate suppliers who qualify for further negotiation. The bargaining power of each party is then determined by the relative magnitude of the respective costs of haggling for the negotiators, and the utility varies with their risk preference.

The integration of negotiation process to an e-tendering system allows a higher degree of system automation through the use of Web semantics. The negotiation process considers bargaining powers including the issues of costs of the haggling and risk preference. It has been shown that a negotiator can change negotiation strategies to achieve a better deal when the cost of haggling is known.

This study primarily focuses on a one-to-one tendering environment. However, future research could expand this work to one-tomany (auction), many-to-one (reverse auction), or many-to-many (exchange) negotiation processes. Also, the system can be implemented in the complex environment such as multiple issue negotiations and multi-attribute utility.

## References

[1] M. Barbuceanu, W.K. Lo, A multi-attribute utility theoretic negotiation architecture for electronic commerce, Proceedings of the Fourth Internationa Conference on Autonomous Agents, Barcelona, Catalonia, Spain, June 3–7 2000, pp. 239–246.

[2] B. Benatallah, F. Casati, F. Toumani, Web service conversation modeling: a cornerstone for e-business automation, IEEE Internet Computing 8 (1) (Jan–Feb 2004) 46–54.

[3] M. Benyoucef, H. Alj, R.K. Keller, An infrastructure for rule-driven negotiating software agents, 12th International Workshop on Database and Expert Systems Applications, Munich, Germany, September 3–7 2001, pp. 737–741.

[4] T. Berners-Lee, J. Hendler, O. Lassila, The Semantic Web, Scienti<sup>fi</sup>c American 284 (5) (May 2001) 34–44.

[5] C. Bussler, D. Fensel, M. Sadeh, Introduction to the special section: the role of Semantic Web services in enterprise application integration and e-commerce, International Journal of Electronic Commerce 9 (2) (Winter 2004) 7–11.

[6] T. Du, C.H. Chen, Building a multiple-criteria negotiation support system, IEEE Transactions on Knowledge and Data Engineering 10 (5) (2007) 804–817.

[7] T. Du, E. Li, E. Wei, Mobile agents for a brokering service in the electronic marketplace, Decision Support Systems 39 (3) (2005) 371–383.

[8] S. Goel, S. Talya, M. Sobolewski, Service-based P2P overlay network for collaborative problem solving, Decision Support Systems 43 (2) (March 2007) 547–568.

[9] A. Gomez-Perez, R. Gonzalez-Cabero, M. Lama, ODE SWS: a framework for designing and composing Semantic Web services, IEEE Intelligent Systems 19 (4) (July–Aug. 2004) 24–31.

[10] A. Kayed, R.M. Colomb, Extracting ontological concepts for tendering conceptual structures, Data and Knowledge Engineering 40 (1) (January 2002) 71–89.

[11] S. Kaza, H. Chen, Evaluating ontology mapping techniques: an experiment in public safety information sharing, Decision Support Systems 45 (4) (November 2008) 714–728.

[12] R. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[13] I. King, C.H. Ng, K.C. Sia, Distributed content-based visual information retrieval system on peer-to-peer networks, ACM Transactions on Information Systems 22 (3) (2004) 477–501.

[14] R. Kowalczyk, V. Bui, On fuzzy e-negotiation agents: autonomous negotiation with incomplete and imprecise information, 11th International Workshop on Database and Expert Systems Applications (DEXA'00), Greenwich, London, U.K., September 6–8 2000, pp. 1034–1038.

[15] M. Kromker, BIDPREP — towards simultaneous bid preparation, International Journal of Computer Integrated Manufacturing 11 (1) (1 January 1998) 45–51.

[16] R. Krovi, A.C. Graesser, W.E. Pracht, Agent behaviors in virtual negotiation environments JEEE Transactions on Systems Man and Cybernetics Part C 29 (1999) 15-25.

[17] J.S.H. Kwok, S. Gao, Knowledge sharing community in P2P network: a study of motivational perspective, Journal of Knowledge Management 8 (1) (March 2004) 94–102.

[18] R. Lau, Y. Li, D. Song, R. Kwok, Knowledge discovery for adaptive negotiation agents in e-marketplaces, Decision Support Systems 45 (2) (May 2008) 310–323.

[19] T.S. Liao, M.T. Wang, H.P. Tserng, A framework of electronic tendering for government procurement: a lesson learned in Taiwan, Automation in Construction 11 (6) (October 2002) 731–742

[20] S. Matwin, T. Szapiro, K. Haigh, Genetic algorithms approach to a negotiation support system, IEEE Transactions on Systems, Man and Cybernetics 21 (1) (1991) 102–114.

[21] A. Muthoo, Bargaining Theory with Applications, Cambridge University Press, Cambridge, UK, 1999

[22] P. Nunes, D. Wilson, A. Kambil, The all-in-one market, Harvard Business Review (2000) 19–20.

[23] J.R. Oliver, A machine-learning approach to automated negotiation and prospects for electronic commerce, Journal of Management Information Systems 13(3) (1996-1997)83-112

[24] D.G. Pruitt, Negotiation Behavior, Academic Press, New York, 1981.

[25] H. Raiffa, The Art and Science of Negotiation, Harvard University Press, Cambridge MA, 1982.

[26] M. Rebstock, P. Thun, O. Tafreschi, Supporting interactive multi-attribute electronic negotiation with ebXML, Group Decision and Negotiation (12) (2003) 269–286.

[27] A. Rubinstein, Perfect equilibrium in a bargaining model, Econometrica (50) (1982) 97–110

[28] A. Segev, A. Gal, Enhancing portability with multilingual ontology-based knowledge management, Decision Support Systems 45 (3) (June 2008) 567–584.

[29] K. Sivashanmugam, J. Miller, A. Sheth, and K. Verma, Framework for Semantic Web process composition, International Journal of Electronic Commerce 9(2) (Winter 2004-5) 71-106.

[30] L. Thompson, The Mind and Heart of the Negotiator, 2nd Edition, Prentice Hall, Upper Saddle River, New Jersey, 2001.

[31] E. Turban, D. King, D. Viehland, J. Lee, Electronic Commerce 2006: A Managerial Perspective, Prentice Hall, 2006.

[32] J. Zhu, A buyer–seller game model for selection and negotiation of purchasing bids: extensions and new models, European Journal of Operational Research 154 (1)(2004) 150-156.

![](/api/attachments/CPZPE2E7/fulltext/images/b250e48c1c24d936bc8b7a7717735f848c9d5ed34e6952c5f858557da22b0ff0.jpg)

Timon C. Du received his BS degree in Mechanical Engineering from the National Chung-Hsing University, Taiwan, in 1989. He obtained his Master's and PhD degrees in Industrial Engineering from the Arizona State University. Currently, Dr. Du is a Professor at The Chinese University of Hong Kong, Hong Kong and director of EMBA (Asia Paci<sup>fi</sup>c) Program of Faculty of Business Administration. His research interests are in e-business, data mining, collaborative commerce, and semantics webs. He has published papers in many leading international journals such as Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, Communications of the ACM, IIE Transactions

International Journal of Production Research, International Journal of Computer-Integrated Manufacturing, Omega, Information System Technology, and others. He was the Executive Editor for the International Journal of Internet and Enterprise Management, and is the Executive Editor for the International Journal of Electronic Business now.
