---
otero_id: 2502
otero_key: "XMA4KHVB"
title: "RFID-enabled item-level retail pricing"
authors: "Wei Zhou; Yu-Ju Tu; Selwyn Piramuthu"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# RFID-enabled item-level retail pricing

Wei Zhou <sup>a</sup>, Yu-Ju Tu <sup>b</sup>, Selwyn Piramuthu <sup>c,</sup>⁎

<sup>a</sup> Information Systems and Technologies, ESCP Europe, 75543 Paris cedex 11, France

<sup>b</sup> Information Systems, University of Illinois at Urbana-Champaign, Champaign, IL 61820, USA

<sup>c</sup> Information Systems and Operations Management, University of Florida, Gainesville, FL 32611, USA

## a r t i c l e i n f o

Article history: Received 6 October 2008 Received in revised form 2 May 2009 Accepted 26 July 2009 Available online 5 August 2009

Keywords: RFID Item-level information Knowledge-based learning system Dynamic pricing Item-level pricing EDLP Hi-Lo Pricing strategy

## a b s t r a c t

A major advantage that online retailers possess that their brick-and-mortar counterparts do not is their ability to continually vary item price. Given the competition among these retailers, it is increasingly becoming a necessity for brick-and-mortar retailers to develop a coherent and pro<sup>fi</sup>table pricing strategy. Recent advances in RFID technology can be bene<sup>fi</sup>cially utilized in this context. We develop a knowledgebased adaptive learning framework for item-level dynamic pricing in retail stores. Speci<sup>fi</sup>cally, we consider retail stores that issue membership cards that the members may use to receive promotions and other bene<sup>fi</sup>ts. Instantaneous snapshots of customers in the store and their characteristics are used to dynamically vary retail store item-level prices. Using simulation, we illustrate the dynamic of the proposed framework. Preliminary results con<sup>fi</sup>rm the bene<sup>fi</sup>cial aspects of such a framework for item-level dynamic pricing in a retail store environment.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Online retailers and their brick-and-mortar counterparts possess different advantages over each other. An online retailer has the ability to continually vary item pricing as conditions dictate, whereas a brickand-mortar (B&M) retailer is unable to do the same due to physical constraints, etc. i.e., it is extremely resource intensive, if not impossible, to manually update the price on each price tag at high frequency. However, given the low margin and the highly competitive environment faced by most retailers, it is increasingly becoming a challenging task for retailers to develop a coherent and pro<sup>fi</sup>table pricing strategy. Every Day Low Price (EDLP) and Hi-Lo, as widely used B&M pricing strategies, have been studied extensively and have their own strengths and weaknesses. The general consensus of this debate is that no single strategy works perfectly well under all circumstances. Facing additional competition from emerging online retailers with their <sup>fl</sup>exible pricing strategies, B&M retailers are urgently in need of a more competitive and ef<sup>fi</sup>cient pricing mechanism. We propose a framework for B&M retailers to dynamically vary item-level pricing using recent advances in RFID item-level tagging technology.

EDLP and Hi-Lo are currently the most widely used retail store pricing strategies. An EDLP strategy entails offering consistently low prices. It is practiced by some supermarket chains (e.g., Food Lion,

Lucky) as well as Wal-Mart. A Hi-Lo strategy is characterized by steep temporary price discounts with higher regular prices. It is practiced by supermarkets such as Publix and Safeway [2]. Investigate the shopping behavior and consumer preference for store price format and show that small basket shoppers prefer HILO stores, even at higher average prices [9]. Draw a conceptual distinction between ‘value pricing’ at the Back Door and EDLP pricing at the Front Door and conclude that there is a need for more targeted micro-market merchandizing and promotions at the front-end combined with improved logistics at the back-end [7]. Observe that consumer expenditures respond more to varying levels of assortment and promotion than price.

In reality, while some retailers such as Wal-Mart have successfully implemented EDLP, other merchants like Von's Pavilion, Publix, Fresh Fields, and Gelson's have been successful in providing high quality, full service value-added grocery store environments. To be competitive, retailers must learn to manage a portfolio of retail formats, each targeting different segments of customers [1]. Examined the seasonal, temporal and regional attributes in retail patronage and found signi<sup>fi</sup>cant changes in a single market over time and signi<sup>fi</sup>cant differences in different regions. Consumer market is so diversi<sup>fi</sup>ed and complex that no single theory or model is able to capture and explain the entire spectrum of its dynamics.

Consumers' knowledge on a diverse set of products differ and so do their preference. A customer may be very sensitive to the price of a purchase while being totally indifferent to another purchase [5]. Note that “what is clear is that shoppers are very heterogeneous in terms of their attention and reaction to price and price promotions [11].”

Explain some of this heterogeneity by offering further delineations of the perception of price in its positive and negative roles. A uniformly designed static pricing strategy, such as EDLP and Hi-Lo, is clearly not able to fully differentiate the market and maximize <sup>fi</sup>rm's revenue. Given the heterogeneity in customer perceptions of price for the exact same item, a static pricing scheme is incapable of effectively capturing these differences. We attempt to incorporate this heterogeneity by designing a dynamic pricing scheme, made possible by recent advances in item-level RFID tag technology, that focuses on readily available consumer preference information.

Dynamic pricing is indeed not a new idea. Extensive published literature exists in dynamic online pricing ever since the emergence of the Internet. Due to the disparity in consumers' shopping behavior in online-store versus B&M store as well as the many fundamental differences in how they operate, the business practice and strategies are consequently very different for stores on the Internet and those with physical presence close to the customer [10]. Investigate dynamic pricing on the Internet and its implications for consumer behavior [6]. Review dynamic pricing in the presence of inventory considerations [12]. Develops a dynamic pricing model with endogenous inter-temporal demand and demonstrates that valuation and patience are the two key aspects that jointly determine the structure of optimal pricing policies [13]. Design a dynamic pricing model by combining three separate approaches including cost-plus, competitor-referenced, and demand-driven models.

We develop a dynamic pricing decision support system that observes variations in consumers' preference and seasonal demand to learn the underlying patterns and determine a good pricing scheme. We speci<sup>fi</sup>cally consider B&M retail stores that issue membership cards that are carried by customers who wish to take advantage of promotions. The proposed framework differs from those in existing literature in its utilization of information provided by recent innovations in RFID-embedded retail price tagging technology. This work differs from literature on Internet dynamic pricing for different consumer shopping behavior (large basket in a B&M store versus small basket in an online store) and for different operation methods (several chain stores with decentralized inventory management versus one online interface with centralized inventory control). Consumer preference is dynamic and an immediate response to consumers' change in taste is critically important to any retail business practitioner. We are interested as well in considering a retail store's inventory management and front <sup>fl</sup>oor shelf arrangement according to changing consumer preference. We develop an intelligent mechanism that automatically determines a near-optimal shelf arrangement considering the back room warehouse as a buffer that communicates with other chain stores in different regions with dynamic consumer demand. We simulate the model and illustrate its potential bene<sup>fi</sup>t.

This research is complementary to literature in marketing information system (MkIS) that focus on marketing strategy decisions rather than pricing. We provide a front-end tool that transfers timely marketing data as well as an executing machine for a marketing information system. We analyze consumer preference and shopping behavior through store membership data and operationalizing automatic dynamic pricing based on the characteristics of customers present in the store at any point in time. RFID is a natural <sup>fi</sup>t in this mechanism because of its ability to aid in instantaneously determining the inventory and front shelf status as well as its capability to help locate consumer movement and individual items thus rendering a low-cost automated system feasible. This research differs from online dynamic pricing system in that it focuses on B&M retailers. The bene<sup>fi</sup>t analysis also utilizes existing literature on B&M shopper behavior. The proposed marketing support system can be integrated in existing marketing information systems in assisting corporate-wide strategic marketing decision making. The following are the primary contributions of this paper: (1) We propose a new pricing scheme: Consumer

Targeted Dynamic Pricing (CTDP) that is different from static pricing strategies such as EDLP & Hi-Lo, and (2) we introduce a knowledgebased adaptive self-learning marketing decision support system framework that aids in automating pricing decisions in a retail store.

The remainder of this paper is organized as follows. We begin with a motivating example in Section 2. We present the dynamic retail store item-level pricing framework in Section 3. We model the bene<sup>fi</sup>t of dynamic pricing in Section 4. Section 4 also includes simulation results to illustrate the presented model and its effectiveness. Section 5 concludes the paper with a brief discussion on the insights garnered and their implications.

## 2. Motivating example

Consider an example retail store scenario presented in Fig. 1 where the quantity sold varies depending on the price. In a store without pricing strategy, assuming 2 pizzas, a watermelon, and bottle of milk were sold, the total pro<sup>fi</sup>t is $( 5 . 9 9 - 3 ) \times 2 + ( 7 . 9 9 - 3 . 5 ) \times 1 + ( 4 . 8 9 -$ $2 . 8 9 ) \times 1 = 1 2 . 4 7 .$ . In an EDLP store, where the items are regularly priced 10% lower than MSRP, the price structure is {5.39,7.19,4.40}. Assuming 2 pizzas, 2 watermelons, and 2 bottles of milk were sold, the store makes a total pro<sup>fi</sup>t of $( 5 . 3 9 - 3 ) \times 2 + ( 7 . 1 9 - 3 . 5 ) \times 2 + ( 4 . 4 -$ $2 . 8 9 ) \times 2 = 1 6 . 3 8 .$ . In a Hi-Lo store, assuming that milk is on promotion for 3.2 and that pizza and watermelon are priced 5% higher than MSRP, the price structure is {6.29,8.39,3.2}. Assuming 2 pizzas, one watermelon, and two bottles of milk were sold, the total pro<sup>fi</sup>t for this Hi-Lo store thus is $( 6 . 2 9 - 3 ) \times 2 + ( 8 . 3 9 - 3 . 5 ) \times 1 + ( 3 . 2 - 2 . 8 9 ) \times$ $2 = 1 3 . 6 9$

In a store with dynamic pricing, the price is determined according to the preference of those customers currently in the store. Considered over all customers throughout the lifetime of the store, the problem of <sup>fi</sup>nding the optimal price is combinatorial. The price structure found by the search algorithm without consumer surplus control is {8.00, 7.50,7.00} and the total pro<sup>fi</sup>t is $( 8 - 3 ) \times 2 + ( 7 . 5 -$ $3 . 5 ) \times 2 + ( 7 - 2 . 8 9 ) \times 1 = 2 2 . 1 1$

In a simpli<sup>fi</sup>ed case, the optimal price of a single product can be found by a general discrete optimization problem:

$$
\max _ {P} \sum_ {i = 1} ^ {n} (P - C) V _ {i} (P)\tag{1}
$$

subject to

$$
(1) V _ {i} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {i} = R _ {i} - P \geq 0 \\ 0 & \text { otherwise } \end{array} \right.\tag{2}
$$

$$
(2) P - C \geq 0\tag{3}
$$

where $R _ { i }$ indicates customer i's reservation price on this product, P the MSRP and C the cost. When more than one product is considered, the interactions of a consumer's preference on different goods makes this simpli<sup>fi</sup>ed problem more complex. The problem becomes worse with the presence of multiple consumers.

If the population of interest is large enough with reference to variances in consumer reservation, the optimal price is relatively stable and is consistent with traditional supply–demand relationship.

<table><tr><td></td><td>Pizza</td><td>Watermelon</td><td>Milk</td></tr><tr><td>Cost</td><td>3.00</td><td>3.50</td><td>2.89</td></tr><tr><td>MSRP</td><td>5.99</td><td>7.99</td><td>4.89</td></tr><tr><td>Customer A</td><td>8.00</td><td>10.00</td><td>7.00</td></tr><tr><td>Customer B</td><td>10.00</td><td>4.00</td><td>1.00</td></tr><tr><td>Customer C</td><td>4.80</td><td>7.50</td><td>4.4</td></tr></table>

Fig. 1. An example.

If the population of customers is not large, however, we <sup>fi</sup>nd that the optimal price remains more volatile depending on consumer pro<sup>fi</sup>le. We can explain this by examining the dynamics associated with consumer pro<sup>fi</sup>les. For example, in general, the pro<sup>fi</sup>le of consumers who usually do grocery shopping on Monday mornings is different from those who shop on Monday nights and can be very different from those who shop only on Saturday afternoons. Current static pricing schemes do not take these differences into account to vary the prices at different points in time during the day or even week. This may be because it is not feasible to differentiate the customers when they are considered as one big aggregate. However, we only consider a small set of customers who are present in the retail shop <sup>fl</sup>oor at any given point in time. Because of this relatively small set of customers, it becomes feasible for the proposed framework to dynamically vary item-level prices in response to the ever-changing nature of characteristics of customers who are present in the store over different times of the day, week, and month.

Traditionally it has been rather dif<sup>fi</sup>cult and practically impossible to observe individual customer's shopping preference and behavior in a retail store setting with a <sup>fi</sup>ne level of granularity. Thanks to modern tracking and tracing technology such as RFID and data mining techniques, it is relatively easier to track consumer's shopping behavior and analyze their preferences and reservation prices. In the framework that we propose, traditional economic theories that are based on statistical analysis of are relatively large population sample do not apply. Instead, we claim that since the item-level pricing decision is able to focus on a speci<sup>fi</sup>c point in time rather than a long time period, we are able to target retailer's pricing structure based just on the customers present on the retail shop <sup>fl</sup>oor. In a retail store that usually carries tens of thousands of items, <sup>fi</sup>nding the itemlevel optimal pricing structure is indeed a combinatorial problem. Although economic theories do still explain certain phenomena in the <sup>fi</sup>eld of retail pricing, the realistic problem of <sup>fi</sup>nding the optimal retailing price can not be accomplished by utilizing a single economic theory or even a combination of economic theories simply because none (or a combination) of them dominate under all circumstances. In the next section, we introduce an innovative concept of customer targeted item-level dynamic pricing scheme that is based on a knowledge-based adaptive learning system.

## 3. Dynamic item-level pricing framework

## 3.1. Traditional pricing mechanism

The pricing of an item usually involves two stages, with the <sup>fi</sup>rst being the manufacturer's suggestion (MSRP) and the second being the retailer's executing price (including periodic promotions). Fig. 2 presents a framework for pricing decision process for a new product from a manufacturer, adapted from [4].

Retail price promotion is generally decided based on past promotional experience and current business environment (Fig. 3). Most promotional events are well planned and carefully arranged. Most retailers in the U.S. actively maintain a calendar of all planned and actual promotions. Periodically, manufacturers offer price discounts and such discounts are passed on to the retailer as manufacturer's promotion. Traditional retail price promotion lasts from a day to several weeks and price is usually static during this period. As opposed to the traditional promotion process, we propose a framework for item-level dynamic pricing that focuses on the current set of consumers on the shop <sup>fl</sup>oor and their characteristics, preferences, etc. Unlike existing literature on dynamic pricing in B&M stores, the concept of item-level dynamic pricing makes it possible to change (item/instance-level or category-level) price on every item in the store as frequently as it is deemed necessary thanks to technology such as RFID and Electronic Shelf Labeling Systems.

![](/api/attachments/XMA4KHVB/fulltext/images/4c3498dd5fe3304351b69028104d2b4f2ba73dd535068b5e87242575dc3d353d.jpg)  
Fig. 2. Manufacturer's price decision process.

## 3.2. Retailing with dynamic item-level pricing

The proposed knowledge-based adaptive learning framework for item-level dynamic pricing has two major modules: localized dynamic pricing module and global marketing strategy module (Fig. 4). Localized dynamic pricing module considers instantaneous information on local business environment, including current customers on the retail shop <sup>fl</sup>oor and available knowledge of their shopping behavior, temporal and spatial demand dynamics and available information on regional marketing environment such as competitor's activities. Instantaneous regional sales information is fed into an adaptive learning component that analyzes the sales data and updates the knowledge repository component. Accumulated local sales data from different regions are fed into a corporate level learning component for the <sup>fi</sup>rm to further develop its global marketing strategy.

This dynamic pricing framework is <sup>fl</sup>exible and sensitive to changes in demand and other related dynamics. RFID tags are a natural <sup>fi</sup>t in this application since they not only provide a way to trace customers' shopping behavior and to infer consumer preference but also makes real-time pricing possible via wireless-controlled itemlevel electronic pricing tags. We de<sup>fi</sup>ne a customer as either a store member (i.e., one who has signed-up to receive a store card that this customer carries when visiting the store) or a guest (i.e., one who doesn't register as a member and shops without membership privilege). A store member is identi<sup>fi</sup>ed by an RFID tag that is embedded in the membership card. Guest's general shopping behavior can be observed by an automated shopping basket system [8]. Instant temporal–spatial consumer information in the store is gathered and analyzed by the problem solver to determine an optimal pricing strategy. The item-level price at any given point in time is determined by the pro<sup>fi</sup>le of current customers in the store including both members and guests. The price remains unchanged until the characteristics of current customers trigger a request for an updated price structure. Revenue and pricing scheme are evaluated and are transmitted to the adaptive learning module for further analysis. In the adaptive learning module, consumer pro<sup>fi</sup>le during this period along with input information such as pricing, revenue, and shelf arrangement are analyzed to update the knowledge-base.

![](/api/attachments/XMA4KHVB/fulltext/images/ddb29ba6e5b834a9b81f3c039e0aecfe5637b6b0cc76301d7f9e681613b1056a.jpg)  
Fig. 3. Schema of retailer static pricing process.

Fig. 5 provides an example of an RFID-embedded price tag with electronic display. This tag communicates with a wireless receiver and is able to change the item-level pricing information at any time. Other electronic pricing technology such as Electronic Shelf Labeling Systems is similar in providing the ability to continually update item price. However, the latter only allows for price update at the categorical level while the RFID-embedded price tag allows for continually updating price at the item-level. This difference may be critical when the store manager requires different item instances (e.g., with different expiry dates) that belong to the same item class (e.g., a 1 liter pack of brand X milk) to be priced differently.

The proposed knowledge-based learning framework supports adaptive decision-making with changes in the store preferences, revenue, consumer preference and the economic environment. The dynamics of such a change may be such that some are amenable to a proactive stance or even a reactive stance from a decision-making perspective. In the next subsection we explain the dynamic pricing component followed by the knowledge-based adaptive learning component.

## 3.2.1. Dynamic pricing

Fig. 6 shows an expanded view of the store-level dynamic pricing module comprising a problem solver and four operational submodules that include item-level dynamic pricing, shelf arrangement, inventory management and inter-store merchandize balancing. Information on current customer pro<sup>fi</sup>le, spatial/temporal demand and updated domain knowledge are input to this module to generate revenue. The problem solver analyzes customer preference and current demand trend with domain knowledge to generate a good pricing structure.

The Problem Solver comprises a set of decision support tools that compute and deliver solutions to routine structured problems where all necessary inputs are deterministically known to fairly sophisticated ‘intelligent’ tools that pro-actively seek to provide appropriate support for making decisions in semi-structured or even unstructured environments. Even in the simpli<sup>fi</sup>ed scenario where only the customers' preference is fed into the system, <sup>fi</sup>nding the optimal pricing structure that maximizes revenue is indeed a combinatorial problem (Fig. 7). This <sup>fi</sup>gure illustrates the topology of the combinatorial problem faced by the retailer. Here, $X _ { i j }$ refers to the price of item j in store i and f is the frequency at which review takes place.

The Problem Solver sub-component interacts with other subcomponents in the framework including Inventory Management, Inter-store Merchandize Balancing, Shelf-Space Management, and Item-level Dynamic Pricing to coordinate decision-making processes. These sub-components are incorporated in the Dynamic Pricing component, and they receive external input information about regional knowledge, customers, and spatial–temporal dynamics. The output from the Dynamic Pricing component include sales information and input information for the Adaptive Learning component. Problem-solving capability is an essential characteristic of an adaptive knowledge-based system since it is a requirement for supporting decision-making situations. The Problem Solver sub-component further includes two components: the knowledge-base and the Problem-solving component. The Adaptive Learning component provides the knowledge that is incorporated in the knowledge-base, which is a part of the problem-solving component. The operationalization of this sub-component can be accomplished through basic rule-chaining or complex knowledge processing.

As knowledge in the knowledge-base becomes stale or when new knowledge or updates to existing knowledge become available, the Adaptive Learning component provides necessary knowledge input to bring the knowledge-base current.

## 3.2.2. Dynamic pricing mechanism

A schematic of the proposed dynamic pricing mechanism is presented in Fig. 8. The proposed mechanism operates by <sup>fi</sup>rst observing the pro<sup>fi</sup>les of current shoppers who are either store

![](/api/attachments/XMA4KHVB/fulltext/images/d2941be8780fcb226b278aebf5e20cd1622d05b00fbbd4a0697cbedb0639429c.jpg)  
Fig. 4. Item-level dynamic pricing.

![](/api/attachments/XMA4KHVB/fulltext/images/4b4608fee009bc1016e220489ed6a94a363e9a68bb3a1190e858146f232b8121.jpg)  
Fig. 5. Example RFID-embedded price tag with display.

members or guests. The system extracts knowledge about these shoppers and transfers this information to the Problem Solver. Customers' shopping behavior include non-members' statistical characteristics and members' unique individual shopping behavior that can be distinguished by whether the customer is informed, price preference, brand preference, budget, etc. The decision variables include the price structure for the set of current customers, shelf arrangement, inventory management and the frequency with which to change these parameters. Knowledge is learned through examining (1) the number of consumers in the store, (2) individual consumer's shopping information (if available, otherwise consumers are generally considered as guests), (3) spatial–temporal demand information from the past τ time periods and (4) seasonal demand information. The output is revenue that should be considered in both the short term (as instant revenue) and the long-term (as accumulated revenue). There is clearly a balance between boosting instantaneous revenue and maintaining relatively uncertain long-term pro<sup>fi</sup>tability. The decision on balancing between short-term and long-term pro<sup>fi</sup>tability can be modi<sup>fi</sup>ed using a dummy variable that controls allowed consumer surplus. If the retailer has a long-term plan, current customers will be

![](/api/attachments/XMA4KHVB/fulltext/images/27e0f2c6a2a20044a2f5e51fb8d30317410d29a7ec30583535079e8b92a2a236.jpg)  
Fig. 7. Pricing system.

![](/api/attachments/XMA4KHVB/fulltext/images/4ed56bebfa9c8ccbd5f8f0984779ed4f23ef121b846c3f615c6af8c1dbce00c1.jpg)  
Fig. 6. Dynamic pricing.

![](/api/attachments/XMA4KHVB/fulltext/images/abd8a6fa8c226bf7d43439b0474984e374d49c31f59fe6f1e915a8ec529a0ced.jpg)  
Fig. 8. Schematic of retail dynamic pricing.

offered lower price and higher current surplus to encourage them to keep coming back. If the retailer is not certain about its long-term pro<sup>fi</sup>tability and thus has a focus on maximizing short-term pro<sup>fi</sup>t, it will set the dummy variable that controls allowed consumer surplus to its minimum.

## 3.2.3. Knowledge-based adaptive learning

There are literally dozens of economic theories that purport to explain the diverse complex phenomena that occur in a retailing setting. Although these theories hold merit under restricted conditions, no single theory dominates in being able to explain the entire spectrum of dynamics associated with retail pricing. We argue that the retail pricing problem is indeed a combinatorial problem, and it is possible to learn the pricing structure to increase pro<sup>fi</sup>t when customers' preference are learned. Consequently, a knowledgebased adaptive learning system is a natural <sup>fi</sup>t to address this problem.

Dynamic pricing necessitates its operationalizing system to have the capability of being current in terms of the customer characteristics as well as the retail store's cost structure, constraints, and overall strategy. Given the dynamic environment under which retail stores operate, keeping everything current is not a trivial task since changes in one may trigger associated changes in another. The knowledgebased adaptive learning component is perfect for such an environment because of its ability to continually monitor its environment and quickly learn to adapt to any changes as they occur. In the modeled system, this component comprises two main sub-components, namely the one for performance evaluation and the one for learning (Fig. 9). These two sub-components work in concert to iteratively learn by continually evaluating itself based on the quality of its actions, thus avoiding inappropriate responses due to stale knowledge.

3.2.3.1. Performance evaluation sub-component. Using input on retail store and customer characteristics such as customers' favorite products, reservation price, cost of goods sold, store inventory levels, etc., the Performance Evaluation sub-component either assigns appropriate internal credit when the performance of the system was as expected or identi<sup>fi</sup>es de<sup>fi</sup>cits when the system performance is worse than expected. In the former case, the system identi<sup>fi</sup>es the parts of the knowledge-base that was used in the decision-making process and assigns (reinforcement) credit, which can then be used to ef<sup>fi</sup>ciently <sup>fi</sup>ne-tune the knowledge-base for effective performance. In the latter case, it identi<sup>fi</sup>es the source of the de<sup>fi</sup>cits. Speci<sup>fi</sup>cally, the best course of action for a given decision-making scenario is identi<sup>fi</sup>ed. This is then incrementally learned and incorporated in the knowledge-base and later used in making decisions at the retail shop <sup>fl</sup>oor environment on arrival of the next set of customers.

The knowledge-base in any dynamically changing environment such as a retail shop <sup>fl</sup>oor quickly becomes stale as frequent changes occur in customer tastes, item inventory levels, among others. The primary responsibility of this sub-component is to pro-actively ensure that the knowledge-base is appropriately updated and maintained to prevent it from becoming stale. This is primarily done by indirectly monitoring the quality of the knowledge-base through the overall performance of the system. A poor system performance indicates incomplete or stale knowledge in the knowledge-base. When the knowledge-base is found to be incomplete, there is a need to identify and generate the ‘missing pieces’ of knowledge. If the knowledge-base is found to have necessary knowledge albeit stale, either a complete overhaul of that part of the knowledge-base can be done or additional knowledge can be added to refresh the knowledge-base.

As input, this sub-component receives solution to the decisionmaking problem which is essentially the information on retail store sales, and relevant associated information such as price, quantity, and customer characteristics. These inputs are mapped to identify characteristics that are addressable through modi<sup>fi</sup>cations to the knowledge-base. The knowledge-base is then incrementally modi<sup>fi</sup>ed to re<sup>fl</sup>ect this updated knowledge. When the deviations are due to a freak circumstance (e.g., weather related event), a solution addressing this deviation may or may not be incorporated in the knowledge-base.

The rationale behind this is simply the fact that the knowledge-base needs to be compact for it to respond instantaneously, and any irrelevant or unnecessary information only aids in slowing down the system and does not warrant being incorporated in the knowledgebase. However, seasonal variations are common in a retail setting and necessary information re<sup>fl</sup>ecting this are therefore incorporated in the knowledge-base.

3.2.3.2. Learning sub-component. Learning is an important characteristic and the Learning component constitutes the core of the considered adaptive knowledge-based system framework. The initial content of the knowledge-base of any dynamic system is bound to be incomplete. However, this is really not of major concern in the proposed framework due to its capability to learn from experience. The ability to learn over time is an important characteristic of any intelligent system. Learning from experience over time has several advantages, including its ability to incrementally build and improve its knowledge-base when and where de<sup>fi</sup>cits are identi<sup>fi</sup>ed through continual feedback from the environment. It is rather challenging to maintain completeness of a knowledge-base that operates in a dynamic environment. The ability to learn alleviates this issue since the burden on beginning with and maintaining a knowledge-base that is complete is reduced to a considerable extent.

In addition to reducing the need to begin with a complete knowledge-base, learning has other advantages. For example, without learning a system is bound to repeat mistakes, which can prove to be expensive in monetary terms as well as in terms of resources including time, manpower, and materials. The knowledge-base of a system that does not have learning capability is bound to be static and hence become quickly stale in terms of knowledge in most dynamic environments. Static knowledge-bases are appropriate only in static environment scenarios where the knowledge-base contains the complete domain knowledge from the beginning, and this domain knowledge does not change with time. Nevertheless, it is hard to envision an application area where a static knowledge-base is appropriate.

The Learning sub-component extensively interacts with the Performance Evaluation sub-component, and these interactions between them are iterative as they are both synergistically related together. Output from the Performance Evaluation sub-component determines and triggers, to a great extent, the timing and extent of the Learning sub-component to accomplish its goals of learning the most appropriate knowledge in a timely manner. Essential characteristics of the Learning sub-component include the ability to (1) concisely, accurately, and quickly learn the concepts of interest, (2) accept necessary input data, and (3) generate learned concepts in a form that is required of the next component in the framework. Moreover, the Performance Evaluation sub-component is useless without the

![](/api/attachments/XMA4KHVB/fulltext/images/947ae15add04dacf8362e1ff0c49fc9f74e10d322b743013eb809565a45afb2b.jpg)  
Fig. 9. The adaptive knowledge-based Learning framework

![](/api/attachments/XMA4KHVB/fulltext/images/748cb2b89e954313b6b4945e1aaff2d7b040fc6b6a205c8efdfc9f888a59b5a1.jpg)  
Fig. 10. Pricing and store pro<sup>fi</sup>t.

Learning sub-component since the latter identi<sup>fi</sup>es and takes necessary actions in response to the former's evaluation. Similarly, the learning sub-component cannot perform to its fullest extent without continual feedback on the system's performance (e.g., revenue) which implicitly measures the quality of the knowledgebase.

## 4. Analysis and results

Consider a retail store pricing scenario comprising S different items, where each pricing instance s corresponds to a case in which the unit price is $P _ { s } .$ For illustration purposes, we assume that there are n customers with membership card, and the store is interested in learning their shopping behavior. We assume that there are 100 products, all of which have a suggested retail price of \$12.5. We randomly assign a product preference for each product to every customer. We simulate this scenario and illustrate the proposed framework for item-level pricing using RFID tags.

At the beginning of the simulation, the store prices the products at the suggested retail price. The system learns the shopping behavior and preference of the customers over time, and continually updates the knowledge-base with relevant information as they become available. At the next stage, the store randomly adjusts the price of all products using pre-de<sup>fi</sup>ned increments. At the end of sale period, the system calculates the revenue and pro<sup>fi</sup>t. If the new pricing strategy results in increased pro<sup>fi</sup>t, the characteristics of the system (e.g., customer preferences) and the pricing strategy are learned and reinforced. This (successful) strategy will be re-used at the beginning of the next sale period. If not, the previous pricing scheme will be kept for the next period. We consider three different price increment (\$0.10, \$0.50, and \$1.0) steps.

![](/api/attachments/XMA4KHVB/fulltext/images/f35b8b73c56446693913841b021825969ddd04066284db52b1f90b24d531dd54.jpg)  
Fig. 11. Chart of consumer surplus.

Preliminary results based on simulation of the proposed framework are provided in Figs. 10 and 11, where pro<sup>fi</sup>t from dynamic pricing are compared to pro<sup>fi</sup>t from static pricing (the base case). From these <sup>fi</sup>gures (Figs. 10 and 11), we observe that dynamic pricing generates more pro<sup>fi</sup>t compared to static pricing; during the training phase, price changes in large increments results in more pro<sup>fi</sup>t than smaller increments; once customers' preferences are learned, small volatilities in price change results in more pro<sup>fi</sup>t than large volatilities although the difference is minimal; customers with membership cards indeed generate more surplus for themselves. This observation is counter-intuitive because in general consumer surplus would be driven to zero when their preference is learned in a purely microeconomic setting. However, we consider a complex retail store scenario with several customers, each with individual preferences on goods which results in a combinatorial problem. Increasing pro<sup>fi</sup>t further can be accomplished only when the retailer can tailor the pricing structure to completely extract consumer surplus from every customer. This is not feasible in practice since it is nearly impossible (even if it is within legal limits) to modify the item price for every item purchased based on who purchases it simply because it is hard to control the number of interested customers who are in the immediate vicinity of an item, i.e., everyone near an item will see the same price, and this cannot be used to extract overall surplus from every customer. The overall surplus that can be extracted at any given point in time can, of course, be <sup>fi</sup>ne-tuned in the system.

The primary reason for the gain in utility for member customers is that the store is able to target promotions for this group of customers who have relatively low reservation price on these promoted items. Consequently, these consumers are willing to shop more due to these customized promotions meeting their expectations. Simultaneously, the store is able to charge more on products with high reservation prices. As a result, consumers will obtain more utility from shopping at a retail store with dynamic pricing than otherwise. If the customer does not use the membership card, then the price displayed does not include this customer's preferences, etc. and would more than likely not increase this customer's surplus.

![](/api/attachments/XMA4KHVB/fulltext/images/d6646d7543c176f10a12a8ce6d6bded66f46bbc38326789f6e2e5eb93a995e55.jpg)

Fig. 12 compares the store pro<sup>fi</sup>t and consumer surplus with respect to the number of current customers, which varies from 10 to 300, and the size of incremental price steps which is \$0.1 and \$0.5. Fig. 13 compares the store pro<sup>fi</sup>t and consumer surplus on a per sold item basis. Based on these simulation results we observe the following:

Observation 1. In any time period, revenue generated using dynamic pricing is greater than or equal to the revenue generated with a comparable static pricing scheme.

A simple explanation of this observation (Fig. 10) is that if the initial price structure of dynamic pricing is set to be the same as the targeted static price, pricing structure will evolve from it only if the new price scheme is more pro<sup>fi</sup>table than the previous one. Observations 2, 3, and 4 are based on Fig. 13. These observations stem from the fact that the law of large numbers applies as the number of customers in the shop <sup>fl</sup>oor increases beyond a threshold. The plots in Fig. 13 represent dynamic pricing. Static pricing can be represented by a <sup>fl</sup>at surface in these <sup>fi</sup>gures.

Observation 2. There exists an n̂ such that when the number of current customers $n { \sim } \{ n { > } \hat { n } \}$ , dynamic pricing will be relatively stable and the pricing structure will be similar to traditional static retailing price.

We observe from our simulation results that the pricing structure tends to be stable when the number of customers is large. Observation 2 states that the optimal dynamic price scheme will converge to a static price scheme when there are a large number of customers on the shop <sup>fl</sup>oor.

![](/api/attachments/XMA4KHVB/fulltext/images/dce40f8301aa7b0ba5d7f27e7bea5cb0ea3d51fd0d1f8035e2eb3fc7cf02888f.jpg)

![](/api/attachments/XMA4KHVB/fulltext/images/ae4d948b857a31305661045ac79b46116adbd65c03ead7cf12cfb2f0023cc7df.jpg)

![](/api/attachments/XMA4KHVB/fulltext/images/1e649cd7df7a8138cb51c42a216b4d2d2c1ee3d8350f7dee3582d7a8e2254b62.jpg)  
Fig. 12. Comparison of accumulated store pro<sup>fi</sup>ts, consumer surplus.

![](/api/attachments/XMA4KHVB/fulltext/images/7e6088ce9a31f196b4dcc3f44c356bcc9c81a295593adfb7df804cbe5d489b2e.jpg)

![](/api/attachments/XMA4KHVB/fulltext/images/837257a1b497577058b8e5efeb37d97c811e82fb718723993a7e9b4fdbaadc93.jpg)

![](/api/attachments/XMA4KHVB/fulltext/images/38903f3b7f3c2089ae463cc1975577157e7fb515e24ff87277d02a978ab84a99.jpg)

![](/api/attachments/XMA4KHVB/fulltext/images/1564d1457a5e854d13df87b24f38dcb5809c5760c78df58b135e0abd2dbeb378.jpg)  
Fig. 13. Comparison of average store pro<sup>fi</sup>ts, consumer surplus

Observation 3. There exists an ň such that when the number of current customers $n { \sim } \{ n { < } \tilde { n } \}$ , average consumer surplus is smaller under dynamic pricing than static pricing.

Traditional economic wisdom states that if a customer's preference is perfectly observed by the store, this store would price the items at a point such that this customer's surplus is close to zero. It is clearly true when there is only one consumer. In a scenario where there are multiple customers, each with different personal preferences on items and their price, the store will generally not be able to price the items to drive every customer's surplus to zero. Instead, the store would raise the price of items for which their customers have a high average reservation price and would provide customized promotions on those goods for customers with low average reservation price.

Observation 4. When $n { \sim } \{ \check { n } { < } n { < } \check { n } \}$ , both store pro<sup>fi</sup>t and consumer surplus are larger under dynamic pricing than under static pricing.

The managerial insight from this Observation is in reference to the conditions that favor a potentially successful implementation of the proposed dynamic item-level pricing mechanism. For instance, small stores with fewer number of customers would be able to squeeze their customers' surplus close to zero without setting the surplus threshold. Volatility in price change may also be large depending on the frequency with which changes in customer pro<sup>fi</sup>le occur. Very large retailers might <sup>fi</sup>nd it unnecessary to change the price often because of their large customer base. Finding ň and ň for a retailer may be dif<sup>fi</sup>cult without a trial run or test implementation and it may also depend on the type of store and its location.

Without dynamic pricing based on observing and understanding customers' preferences, the price of merchandize is traditionally set as the one that maximizes the overall pro<sup>fi</sup>t for a population Ω from a region comprising a selected few stores, a city, a county, a state, a country, etc. Price is therefore set as P(Ω). As discussed earlier, even at a speci<sup>fi</sup>c retail store at various points in time (e.g., hours in a day, days, weeks, months), disparate pro<sup>fi</sup>les of customers on the shopping <sup>fl</sup>oor may be observed. For instance, customers who only shop in the evening may possibly indicate that they are at work during day time, which differentiates them from those who usually shop during day time. Other occasions including those related to weather conditions, local festivals, holidays, etc., may dramatically in<sup>fl</sup>uence consumer preferences for the local store involved during those times. By utilizing knowledge about the pro<sup>fi</sup>le of customers currently on the shop <sup>fl</sup>oor ømega, price is dynamically set as $P ( \omega )$ in our proposed framework. While ω <sup>fl</sup>uctuates from time to time, Ω is considered relatively stable. As a result, a more intuitive explanation of the retail dynamic pricing's pro<sup>fi</sup>tability can be found as the difference between the two pricing strategies at time t:

$$
\Pi_ {t} = \max _ {P (\omega_ {t})} \sum_ {i = 1} ^ {m} (P (\omega_ {t}) - C) V _ {i} (P (\omega_ {t})) - \sum_ {i = 1} ^ {m} (P (\Omega) - C) V _ {i} (P (\Omega))\tag{4}
$$

subject to

$$
(1) P (\Omega) \sim \max _ {P (\Omega)} \sum_ {i = 1} ^ {n} (P (\Omega) - C) V _ {i} (P (\Omega))\tag{5}
$$

$$
(2) V _ {i} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {i} = R _ {i} - P \geq 0 \\ 0 & \text { otherwise } \end{array} \right.\tag{6}
$$

$$
(3) P (\cdot) \geq C\tag{7}
$$

where m is the number of shoppers currently at the store (or, when considered at a <sup>fi</sup>ner granularity, only those who are in close proximity to an item of interest), n is the regional population size for the product of interest, C is the cost of this product, and $R _ { i }$ is customer i's reservation price for this product. Clearly, by considering the characteristics of customers at the individual level, the proposed customer targeted dynamic pricing is able to guarantee improvement in pro<sup>fi</sup>t over traditional static retail pricing schemes that are based on average data from a large number of customers.

The expression for each of the customers would be similar as well. Here, the focus is on a given customer whose reservation prices are higher than the average (of all sales of that item in that store) on some items and lower on others. By targeting promotions at the individual level, the individual customer overall surplus would be larger for the customer to continue to shop at this store. At time t, in a store with k different kinds of products and m customers, the overall aggregated consumer surplus from dynamic pricing mechanism can be described as:

$$
U _ {\delta} = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {k} \Big (\big (R _ {i j} - P _ {j} (\boldsymbol {\omega} _ {t}) \big) V _ {i j} \big (P _ {j} (\boldsymbol {\omega} _ {t}) \big) - \big (R _ {i j} - P _ {j} (\Omega) \big) V _ {i j} \big (P _ {j} (\Omega) \big) \Big)\tag{8}
$$

subject to Eqs. (5)–(7) and

$$
P _ {j} \left(\omega_ {t}\right) \sim \max _ {P _ {j} \left(\omega_ {t}\right)} \sum_ {i = 1} ^ {m} \left(P _ {j} \left(\omega_ {t}\right) - C _ {j}\right) V _ {i j} \left(P _ {j} \left(\omega_ {t}\right)\right)\tag{9}
$$

Linked by $V _ { i j } ,$ which is a common interest for both retailer and customer, expressions (4) and (8) are in a form of duplexity such that a solution that optimizes one also optimizes the other.

## 5. Discussion

We considered one of the problems faced by B&M retailers with respect to dynamically modifying item-level pricing using a knowledgebased system framework. This process can be automated to the same extent they are in an online retailing environment and operationalized in a seamless fashion through RFID-embedded price tags on individual items. In fact, the B&M scenario lends itself to item-level pricing that is generally not attempted by large online retailers. This is achieved through item-level RFID-embedded price tags. These RFID-embedded price tags also enable the retailers to continually modify price at the item-level as is deemed necessary. We illustrated the proposed knowledge-based framework using a retail store example and compared it to a similar setting where the item price is kept constant. Preliminary results indicate that the store would bene<sup>fi</sup>t by such a framework and setup using RFID-enabled price tags. Preliminary results, surprisingly, also indicate that the customer surplus could also increase in such a setting due to the complex interactions and dynamic at play in that environment.

One of the major issues with respect to the proposed dynamic item-level pricing mechanism may be directed towards customers' perception of fairness [3]. Observes that customers do not necessarily feel that they were treated unfairly if they are charged different prices for the same item. We believe that our proposed item-level pricing procedure would be perceived to be fair by customers since at any given point in time the price remains <sup>fi</sup>xed to all customers at the store. I.e., two customers interested in buying the same item instance at the same point in time would see the same price on their item's price tag.

Item-level retail pricing strategy clearly is of bene<sup>fi</sup>t to the store. Although counter-intuitive, we have shown that this process is like a double-edged sword from the customer's perspective. It bene<sup>fi</sup>ts the customers by offering customized promotions that address their individual reservation price in a focused manner. The store can afford to charge more on items for which any given customer has high reservation price and less on those where the reservation price is lower. The key difference here is that the mechanism operates at the individual level rather than at the overall average level as is the case in almost all retail (B&M) market settings today. The proposed framework accomplishes this by managing individual consumer surplus in a controlled manner.

## References

[1] S.J. Arnold, T.H. Oum, D.J. Tigert, Determinant attributes in retail patronage: seasonal, temporal, regional, and international comparisons, Journal of Marketing Research 20 (2) (1983) 149–157.

[2] D.R. Bell, J.M. Lattin, Shopping behavior and consumer preference for store price format: why “large basket” shoppers prefer EDLP, Marketing Science 17 (1) (1998) 66–88.

[3] J.L. Cox, Can differential prices be fair? Journal of Product and Brand Management 10 (5) (2001) 264–275.

[4] D.W. Cravens, Strategic Marketing, Irwin, Homewood, lll., 1982.

[5] P.R. Dickson, A.G. Sawyer, The price knowledge and search of supermarket shoppers, Journal of Marketing 54 (3) (1990) 42–53.

[6] W. Elmaghraby, P. Keskinocak, Dynamic pricing in the presence of inventory considerations: research overview, current practices, and future directions, Management Science 49 (10) (2003) 1287–1309.

[7] E.J. Fox, A.L. Montgomery, L.M. Lodish, Consumer shopping and spending across retail formats, Journal of Business 77 (S2) (2004).

[8] D.T. Hajec and M.G. Lee, Automated shopping basket system with accounting and article tracking functions, United States Patent 5637847 (1997).

[9] S.J. Hoch, X. Dreze, M.E. Purk, EDLP, Hi-Lo, and margin arithmetic, Journal of Marketing 58 (4) (1994) 16–27.

[10] P.K. Kannan, P.K. Kopalle, Dynamic pricing on the Internet: importance and implications for consumer behavior, International Journal of Electronic Commerce 5 (3) (2001) 63–83.

[11] D. Lichtenstein, N.M. Ridgeway, R.G. Netemeyer, Price perceptions and consumer shopping behavior: a <sup>fi</sup>eld study, Journal of Marketing Research 30 (May 1993) 234–245.

[12] X. Su, Intertemporal pricing with strategic customer behavior, Management Science 53 (5) (2007) 726–741.

[13] N.H. Sung, J.K. Lee, Knowledge assisted dynamic pricing for large-scale retailers, Decision Support Systems 28 (4) (2000) 347–363.

Wei Zhou received his Ph.D. in Information Systems from the University of Florida in 2008. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in European Journal of Operational Research, IEEE Transactions on Geosciences and Remote Sensing, International Journal of Electronic Commerce, and Optical Engineering

Yu-Ju Tu is a graduate student in Information Systems at the University of Illinois at Urbana-Champaign. His research interests include RFID systems.

Selwyn Piramuthu is Professor in the Information Systems and Operations Management department at the University of Florida. His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis
