---
otero_id: 22364
otero_key: "F8WGSENH"
title: "A conceptual model for virtual markets"
authors: "Huaiqing Wang"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00017-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research

# A conceptual model for virtual markets

Huaiqing Wang $^{*}$

Information Technology Management Centre for Organizational Changes Department of Information Systems, City University of Hong Kong, Tat Chee Ave., Kowloon, Hong Kong

## Abstract

Virtual Markets on the Information Superhighway (VMIS) have provided and will provide new areas of opportunities for retailers, producers, and consumers. The building of such global VMISs, raises important issues of marketing, management, and operation. In this paper, a powerful conceptual framework for such VMISs is presented using the knowledge representation language Telos. This framework is developed and based on careful analysis and abstraction of VMISs, using a real-world virtual market as an example. Capabilities of this integrated hybrid modelling framework include meta-level facilities, constraint enforcement, and inference facilities. By creating rich ontologies, this method provides a comprehensive framework for analysis, design, and investment decisions involving future VMISs. © 1997 Elsevier Science B.V.

Keywords: Electronic commerce; Information superhighway; Conceptual model; Homeshopping; Internet; IS development; On-line information services

## 1. Introduction

The virtual revolution has begun [7, 12]. The most powerful source of our generation is information processing. Powerful information communication channels, such as the Internet (information superhighway), interactive TV, as well as the telephone and fax machine, are continuously changing the relationships among producers, suppliers, retailers, and consumers [3]. Such changes will significantly affect the economics of marketing channels, and patterns of physical distribution. The structuring of distributors may also occur. The rapid construction of the information superhighway raises important issues of ownership, marketing, management, operation, and economics [1].

The vision of futuristic VMISs is overwhelming [6]. A system could involve large numbers of heterogeneous components distributed over large computer and telecommunication networks. Customers would obtain information about the companies and their products on the Internet, and order products electronically [2]. The VMIS components are human beings or computer programs that serve the marketing purpose. Within such a 'Virtual Market,' a large number of orders may occur at any given time, and that a wide variety of goods and services will be provided [18, 8].

Central to the futuristic VMISs will be the way that daily business transactions will be conducted and the vast number of competing choices that will face tomorrow's consumers [17]. It is the goal of this paper to provide a fundamental study of the means of constructing a formal conceptual model of business transactions within VMISs. The model is a formal description of entities and their properties. It forms a shared terminology for the objects of interest in a domain, along with definitions for the meaning of each of the terms. It will be used as the generic blueprint to gain, not only a concise understanding of the key features of VMISs, but also to consider the design and implementation of such systems. The models provide the conceptual basis for thinking about VMIS applications and provide a formal basis for tools and techniques used in developing and using VMISs.

There are several research areas that impact VMIS, such as enterprise modelling and investigations into electronic commerce and virtual enterprises. However, little research has been reported on the construction of formal conceptual models for VMISs and its usefulness towards the design and implementation of such systems.

Recent results by Kangassalo [11] suggest that enterprise modelling is an essential component in defining an enterprise. The goal is to present generic representations of enterprise knowledge that can be reused across a variety of enterprises. The paper presents a logical framework for representing the agents in such IS. It considers the agents in a cooperative information system to be constraint-based problem solvers: given a set of goals and constraints, they search for a solution that optimises the goals and satisfies the constraints.

On the other hand, Benjamin and Wigand [4] suggest that the NII (National Information Infrastructure) will give consumers increased access to a vast selection of goods but will cause a restructuring and redistribution of profits among the stockholders along the chain [13, 14]. There will be an evolution from traditional single source sales channels to electronic markets, which may lower co-ordination costs for producers and retailers, lower physical distribution costs, or eliminate retailers and wholesalers entirely, as consumers directly access manufactures.

Recent research by Hansen contends that information technology practice is far ahead of its corresponding theory; this particularly applies to the recent exponential growth in conducting daily business transactions in a virtual market and the immediate need for the development of conceptual models to guide the design, development, and investment decisions [10].

## 2. Modelling techniques

The development of our conceptual model for VMIS has drawn on results from AI, such as knowledge representation (KR) and KR languages [20, 5]. The basic problem of KR is the development of an expressive presentation notation with which to represent knowledge [9, 19]. In the following sections, we shall refer to such notations as KR schemes.

The scheme to be used to model VMISs is based on the KR language Telos, developed at the University of Toronto [16]. The Telos KR language adopts a representational framework which includes structuring mechanisms analogous to those offered by semantic networks and semantic data models, namely, classification (inverse instantiation), aggregation (inverse decomposition) and generalisation (inverse specialisation). Another important novelty of Telos is its treatment of time. This feature facilitates the natural modelling of dynamically changing domains, including the case where definitions of concepts change over time. The functional operations in Telos are a very powerful feature in which operations ASK, TELL, UNTELL and RETELL allow the user to query and update VMISs and serve as primitives in terms of which VMISs can be defined.

Telos offers an assertional sublanguage that can be used to express both deductive rules and integrity constraints with respect to a given knowledge base. Two novel aspects of Telos are its treatment of attributes (i.e. attributes can be defined in the same manner as entities and can have their own attributes), and the provision of special representational and inferential facilities for temporal knowledge.

Our study uses the Telos KR scheme to represent and model the variety of types of knowledge required by a VMIS within a consistent framework. Using it, each category of knowledge is treated as a class (with its instances being its instantiation). All classes of information contained in a sample VMIS can be organised within a hierarchy.

The concept of agent has become important in both artificial intelligence, computer science and electronic commerce [15]. The term is used to denote a software-based computer system that enjoys the following properties: (1) autonomy (agents operate without the direct intervention of humans); (2) social ability (agents communicate with other agents); (3) reactivity (agents perceive their environment and respond in a timely fashion to changes that occurs in it); and (4) pro-activity (agents do not simply act in response to their environment; they are able to exhibit goal-directed behaviour by taking the initiative).

Within a VMIS, there are a number of components that are able to collect, manipulate, and deliver information. We model these components of a particular VMIS transaction as agents in our formal ontology.

## 3. VMIS systems

Here, industry value chains will be used to demonstrate how virtual markets on information highways can affect selling prices and the informal model of VMISs.

Figure 1 shows a traditional chain of producer, wholesaler, retailer, and consumer. When the values added are summed, the consumer pays \$52.72 for a shirt. However, the growth of value added and selling price are shown in Table 1.

Within the traditional value-added chains, the transportation of physical goods and the transportation of the information about the goods follow the same steps. Such multi-step transportation adds \$32.27 (52.72–20.45 = 32.27), that is, about 62 percent of the price.

Virtual markets try to minimise transportation costs. A typical value-added chain of virtual markets is shown in Figure 2, which indicates the separation of the transportation of physical goods and the transportation of the information. The physical goods can be distributed to the consumers directly via physical distribution networks. On the other hand, information flows via a number of information agents. Such information agents co-operate together to provide services to other agents and to consumers. The major components in a virtual market are:

Table 1

<table><tr><td></td><td>Producer</td><td>Wholesaler</td><td>Retailer</td><td>Consumer</td></tr><tr><td>Valued added</td><td>$20.45</td><td>$11.36</td><td>$20.91</td><td></td></tr><tr><td>Selling price</td><td>$20.45</td><td>$31.81</td><td>$52.72</td><td>$52.72</td></tr></table>

\- Goods producers: produce physical goods, as well as the source information about their goods. For instance, a GE factory produces GE TVs and the basic information (e.g. the factory's selling price, technical description, etc.).

\- Producers of information: produce information about the goods in electronic forms, such as Netscape applications, JAVA applications, interactive TV programs, etc. For instance, HyperEdge may produce a Netscape application for marketing GE TVs.

\- Virtual markets: New kinds of marketing channels that only exists in virtual space; for example, the Internet. Customers are able to navigate the virtual markets to find goods they want to buy.

The main difference between virtual markets and mail-order markets is that virtual markets provide the customers with up-to-date information on the current prices and any new items, while the customers in mail-order markets are faced with out-of-date catalogues and prices. The customers in virtual markets can compare the current prices and goods with those offered by other competitors instantaneously, whereas customers in the department store setting have to decide without the benefit of instant price and goods comparison. Virtual markets do not provide any novel features when it comes to marketing and purchasing. Rather, VMISs combine the best characteristics of both, as they are highly interactive, both in terms of current goods and prices being offered and in their comparison with other products.

![](/api/attachments/F8WGSENH/fulltext/images/a37a25779e373ff96bff12d79e971e75c3457461f6dc338e8dab6b0e8ead64ca.jpg)  
Fig. 1. Value-added chains in current markets.

![](/api/attachments/F8WGSENH/fulltext/images/559d463ae4b243285ac940709cc4aeaf598765c6ab39ddfcb6c199191287aef7.jpg)  
Fig. 2. Value-added chains in virtual markets.

A key feature of virtual markets is the separation of physical goods and information; in a typical virtual market transaction, the information will be transferred from physical good suppliers, information mediators (information producers, and virtual markets) and customers. Such separation provides:

\- Benefits to the consumer. The customer is able to navigate virtual markets very quickly. He/she will have free market access to all suppliers willing to pay an interconnection cost, giving maximum choice at lower price. The consumer may have access to the price without market-maker profits with more efficient pricing due to the single channel suppliers.

\- Lower co-ordination costs through the industry value chain. Electronically linked producers and retailers will be able to lower their costs by reducing intermediary transactions and unneeded coordination.

\- Lower physical distribution costs. Delivery costs will be reduced in two ways. First, information will be transmitted electronically, with lower electronic distribution costs. Second, as elements of the industry value chain are bypassed, physical distribution link and related inventory carrying costs will be reduced.

## 4. Virtual market scenario

While there has been a proliferation of the overall usage of VMIS, it is informative to look at a real example of such transactions.

## 4.1. Scenario description

Let us suppose that a particular hypothetical virtual market customer ('DL') is interested in acquiring a Home Theatre System. OnSale Inc. has been chosen as the virtual market. It is a real-life real-time interactive virtual auction house (see 'http://www.onsale.com/') that specialises in new and closed out computer and electronic equipment. Furthermore, a real-life physical company called SSI intends to sell a batch of Home Theatre Systems via the virtual market.

It is natural for our hypothetical virtual market customer ('DL') to bid on the item in this virtual market transaction.

## 4.2. Virtual market transaction

The entire transaction can be decomposed into three stages that are carried out sequentially. Failure of any of these steps (e.g. the customer refuses to pay for the item) results in an incomplete and therefore aborted virtual market transaction.

## Stage 1: Creation of a virtual auction item

The producer of the physical product, SSI Inc., will initiate contact with the virtual market (OnSale Inc.) about the sale of 10 units of its Home Theatre System for a week (e.g. between Jan. 16, 1996 and Jan. 23, 1996).

Provided the particular virtual auction house of OnSale accepts to sell the batch of items through its auction channel in virtual space, negotiation sessions will be carried out between the goods producer (SSI Inc.) and the virtual market (OnSale Inc.) about the minimum bidding price and the commission fee to be paid (this is analogous to the physical auction process).

## Stage 2: Customer bid

The customer, DL, will discover that there are still a number of units of the Home Theatre System available through OnSale at the price of US \$265.00 minimum bid (see Figure 3). DL will enter a bid for the Home Theatre System at US \$295.00 using the bid form provided by OnSale (as shown in Figure 4).

## Stage 3: Successful bids

Upon completion of the virtual auction process (i.e. after Jan. 23rd, 1996, closing date), DL is assumed to have won one of the ten units available, then the virtual market, OnSale, will transmit the bid information of all successful bids to the physical good producer, SSI.

SSI now contacts DL for confirmation of the virtual bid transaction. DL confirms the transaction and provides the payment (for example, in DigiCash), anticipating the arrival of the Home Theatre System.

The reception of virtual payment by SSI will result in the closing of the virtual market transaction cycle. SSI will ship a unit of Home Theatre System to DL, by the means of some physical distribution channel (such as United Parcel Service). Also, the sales commission will be sent to OnSale for mediating market transaction.

## 4.3. Scenario analysis

This example can be abstracted to the supplier-mediator-customer interdependent relationship that is central to all types of virtual market transactions; it also points out the area of study that remains to be explored, such as transaction security, virtual money and the issue of trust in the virtual market.

It is also interesting to note that there are a number of informal ‘rules of thumb’ and constraints in the virtual auction house. For instance, what if a bad customer bids for an item and then does not pay for it? In OnSale, there is a policy of restricting such ‘bad customers’ from bidding on any items in future. On the other hand, it is financially risky for a person to have the sum of all outstanding bid prices greater than the credit limit of the electronic cash account, therefore OnSale enforces a policy of stopping a customer bidding for an item from the electronic cash account if the new bid will exceed the account limit, even though the local bid transaction by itself may be completely valid $^{1}$ .

## 5. Ontology

An ontology is a specification of some conceptualisation, which is an abstract, simplified view of the world. Usually, ontologies are equated with taxonomic hierarchies of classes, objects, relationships, and other entities.

## 5.1. Structured organisation of concepts

A partial semantic schema for the VMIS is given in Figure 5. Within this figure, the thick closed arrows represent Telos' ISA links (subclass/class relations); while the open arrows represent Telos' IN links (instance/parent class relations); subsequently, the thin arrows represent the Telos ATTRIBUTE links.

This graph is produced in three levels, namely, MetaClass, DomainClass, and Token levels. The enti-

![](/api/attachments/F8WGSENH/fulltext/images/a4a7387dd7cf427ecf424b0cfdef70c23602078e612fd46e5e0e854d4d7af7d3.jpg)  
Fig. 3. A virtual auction item: Home Theatre System.

ties at the Token level corresponds to domain VMIS instances. All classifications of token level objects are presented in the DomainClass level. For instance, the token SSI, which produces Home Theatre Systems, is an instance of the domain class GoodsProducers, which groups all the information producers of VMISs under a common generic description. In Telos, we can carry the classification/generalisation operation much further: to classify common characteristics of domain classes into MetaClass level objects, resulting in all domain classes as instances of meta classes. Similarly, such operation can be reapplied to MetaClass objects, which are in turn instances of metameta classes.

The subset of the overall virtual market schema is sufficient to demonstrate the ontologies of VMIS. It was with the complexity of this figure in mind that many Telos links (i.e. ISA, IN, and ATTRIBUTE links) have been omitted. As an example, the goodsSupply attributes at the Token level are instances of a DomainClass level attribute category GoodsSupply, which in turn is an instance of a metaclass Attribute-Class.

![](/api/attachments/F8WGSENH/fulltext/images/533269797e06956dac6f3ecf3c0e4f0214babca89dee8bbffc1c011101ea151a.jpg)  
Fig. 4. A bid form in the virtual market for Home Theatre System.

The IN keyword signifies that the class InformationAgents is an instance of a metaclass Supplier-Class; this metaclass facility allows the schema to be expressed within the same modelling framework as domain classes. All instances of metaclasses are domain classes.

On the other hand, the WITH keyword introduces class InformationAgents attributes. For example, the class VirtualAuctionDealer has an attribute bid\_form that is a collection of the object BidForms.

For instance, VirtualAuctionDealer class as a specialisation of the VirtualDealer class inherits attributes from the parent class, such as name, physical address, virtual space address, etc.:

![](/api/attachments/F8WGSENH/fulltext/images/eb8b32c8c520d7fa659ddc8dffc8a7c86bc58e1b1696b84b98a711eba2e80ff8.jpg)  
Fig. 5. A partial schema.

Class VirtualAuctionDealer

ISA VirtualDealer
WITH

attribute
    auction\_item: set of VirtualAuctionItem
    bid\_form: set of BidForm
    current\_bids: set of BidForm
    new\_bids: set of BidForm

rule
BadBidWarningRule:
((Forall x/new\_bids
(AcceptableBid(x))

AND BadCustomer(x)
=> WarningManager(x))

AcceptableBidRule:
((Forall x/new\_bids
((x.quantity
< x.bid\_item.quantity\_available) AND
(x.bid\_price > x.bid\_item.minimum\_bid))
=> AcceptBid(x))

AcceptableBidRule:
((Forall x/new\_bids
((x.bid\_item.quantity
= x.bid\_item.quantity\_available) AND

```txt
constraint
SumBidLessThanAccountLimitConstraint:
((Forall x/current_bids
((x.bid_price + SUM_BIDS(
x.bid_customer.bids)
<= x.account.limit))
```

```txt
(x.bid_price > MIN(x.bid_item.bids)))
=> AcceptBid(x))

BadCustomerRule:
((Forall x/new_bids
(Forall y/x.bid_customer.bid_history
((y.successful = True) AND
NOT Payment(y))
=> BadCustomer(x.bid_customer))
```

## END

The rules and the constraints are special objects in the ontology and are attached as attribute values of propositions. For the definition of VirtualAuctionDealer, the deductive rule BadBidWarningRule effectively models the propositional logic that is implicit in the information policy of the virtual auction house, OnSale. Making such concepts explicit allows the designers and implementers of future virtual market agents to understand the informal procedure of the domain as well as gaining an insight into the reasoning behind it.

By defining global consistency constraints as embodied in the VirtualAuctionDealer, we have allowed the system to check the overall integrity of the conceptual model. For instance, the addition of a bid that satisfies the procedure of the virtual auction house, as formalised in deductive rules, may violate the BidExceed-AccountLimit integrity constraint, which in turn would not allow the bid concept to be added. Unlike traditional static models which lack active monitoring and thus will not be able to detect such global inconsistencies, the active Telos modelling framework maintains and monitors such constraints.

The concept of a bid or, more specifically, the use of a form for a bid can be modelled in the modelling framework as:

Class BidForm

ISA VirtualAuctionInfo
WITH

attribute
bid\_customer
: VirtualAuctionCustomer
bid\_price: Price
bid\_item: VirtualAuctionItem
quantity: Integer
account: VirtualAccount

The next definition captures the intuitive understanding of the Items to be auctioned off within the virtual market information mediator; it will only have a limited temporal duration:

Class VirtualAuctionItem

ISA VirtualAuctionInfo
WITH
attribute
    name: String
    producer: GoodsProducer
    quantity\_available: Integer
    minimum\_bid: Price
    bid\_increment: PriceIncrement
    high\_bids: BidForm
    duration: TimeInterval

END

For the supplier–mediator–customer interdependent relationship, the virtual market customer and its specialisation, a virtual auction house customer, will be modelled:

Class Consumer

IN ConsumerClass
WITH

attribute
first\_name: String
last\_name: String
address: String

END

Class VirtualAuctionConsumer

ISA Consumer
WITH

attribute

bids: set of BidForm
bid\_history: set of BidForm

## END

Analogously, the supplier role in the virtual market transaction is played by a producer of physical goods, with the formal representation:

Class GoodsProducer
IN SupplierClass
WITH
attribute
    name: String
    goods: set of Goods
    tobe\_delivered\_goods: set of Goods
    information\_supplier
    : InformationSupplier
    distribution: PhysicalDistributionNetwork

## END

The actual physical goods abstraction is:

Class Goods
IN EntityClass
WITH
attribute
producer: GoodsProducer
serial\_number: Integer
buyer: Consumer
produced\_time: Time

In the example, the particular type of goods to be auctioned through the virtual market is HomeTheaterSystem:

Class HomeTheaterSystem

ISA Goods

The final physical delivery is made by a real-life delivery network, for instance, UPS, represented as:

Class PhysicalDistributionNetwork

IN MediatorClass
WITH
attribute
    name: String
    goods\_tobe\_delivered: set of Goods
    goods\_delivered: set of Goods

END

The definition of such abstract domain classes provides the formal mechanism with which a precise analysis of the dynamic nature of a virtual market transaction can be performed.

## 5.2. Conceptual model of VM transaction

In order to complete a virtual market transaction, there are three distinct stages. Thus a VirtualAuction-Item, in this case a HomeTheaterSystem, is only created after the initial contact between the Goods-Producer, SSI, and the virtual market, OnSale.

A model of the virtual market domain captures the history of objects and their evolution, rather than just the latest snapshot that would be provided by most traditional modelling techniques. As a result, we can accurately capture the objects and their dynamic relationships.

## 5.2.1. Before the virtual market transaction

We now define the initial state of the various Token level objects before the start of the virtual auction transaction. There are some permanent parts, such as OnSale Inc., which do not change either before, during, or after the transaction.

The virtual auction house, OnSale, may have other VirtualAuctionItems independent of the specific transaction under analysis (e.g. it also sells CD players), the formal representation of the virtual auction house is therefore:

Token OnSale

IN VirtualAuctionDealer
WITH
name
: OnSale
auction\_item

```txt
Token DL
IN VirtualAuctionConsumer
WITH
...
address
: Denver, CO
bid_history
....
....
```

```txt
: MediaVisionPortableCDROM
bid_form
:...
current_bids
: JK_CD_Bid1
: YU_CD_Bid1
:...
new_bids
:...
```

Similarly, the particular virtual auction customer, DL, has been in existence long before and long after the completion of the virtual auction transaction.

## END

The definition of the goods producer company in our virtual market transaction is next provided. It already has a relationship with UPS. The set of Home-Theater Systems to be sold is also defined:

## Token SSI

IN GoodsProducer
WITH
name
: Sound Studio International
goods:
: SSI\_HomeTheaterSystem1
: SSI\_HomeTheaterSystem2
...
distribution
: UPS

END

Token SSI\_HomeTheaterSystem1

```txt
IN HomeTheaterSystem
WITH
producer
: SSI
serial_number
: 0353
```

Finally, the physical mediator actor in this virtual market transaction is captured as:

Token UPS
IN PhysicalDistributionNetwork
WITH

## 5.2.2. Establishing an auction item

From this point, an addition or change in an attribute value will be represented by italic letters. Also, the newly created objects and new attribute values will be emphasised in the conceptual diagram using thickened frames and arrows.

Figure 6 outlines the necessary supplier–mediator relationship between SSI and OnSale, that occurs after OnSale is contracted to market 10 units of Home-TheaterSystem in its virtual auction house, a new VirtualAuctionItem with a duration of one week is created, as well as new attribute relationships between SSI and OnSale.

## Token HomeTheaterSystemAuction

IN VirtualAuctionItem WITH

name : SSI Cineplex Home Theater System producer

![](/api/attachments/F8WGSENH/fulltext/images/302edf6b280de0d61c17021be06d88eecfbb4e3776a14e69639cedc643efa69f.jpg)  
Fig. 6. A conceptual model of transaction before bidding.

```yaml
: SSI
quantity_available
: 10
minimum_bid
: 265.00
bid_increment
: 10.00
duration
: 16/01/1996.. 23/01/1996
```

## END

The evolution of OnSale, the virtual auction house, is:

Token OnSale

...
auction\_item

: HomeTheaterSystemAuction
...

## END

The addition of OnSale as an information supplier (virtual market) to SSI is captured by:

Token SSI

```prolog
information_supplier
:...
: OnSale
:...
END
```

## 5.2.3. Ready, set, bid

The addition of the newly created VirtualAuction-Item to its portfolio will prompt the virtual market customer, DL, to bid on the item as shown in Figure 7.

Various new concepts, such as DL's new bid for the particular VirtualAuctionItem, will be created, as well as the augmentation to the attribute relationships of the VirtualAuctionItem and the virtual auction house, OnSale.

Token DL\_SSI\_bid1

IN BidForm
WITH

bid\_customer : DL
bid\_price : 295.00

![](/api/attachments/F8WGSENH/fulltext/images/1370d3d938ac264c19eeac241d8b11b47b0a3fd8f9621e0a20bc45a83e39c220.jpg)  
Fig. 7. A conceptual model of transaction during bidding.

```asm
bid_item
: HomeTheaterSystemAuction
quantity
: 1
account
:......
time:
: Sat Jan 20, 1996, 9:59am
```

Additions to the virtual customer have to be made after he bids on the Home Theater System.

```txt
Token DL
...
bids
: DL_SSI_bid1
...
```

Recording the bid is provided as:

```txt
Token OnSale
...
current_bids
: DL_SSI_bid1
...
END
```

5.2.4. Closing the virtual auction item

The end of the current auction session occurs on Jan. 23, 1996. This requires evolution and modification to the dynamic transaction conceptual model (see Figure 8).

The virtual auction house OnSale will not only remove the VirtualAuctionItem as no longer being active, but will also have to delete all the particular bids relevant to the auctioned item including the commission payment and transfer of all successful information to the goods producer, SSI.

New attribute relationships will be created between the transaction physical distribution network, UPS, the good producer, SSI, and the end virtual customer, DL.

![](/api/attachments/F8WGSENH/fulltext/images/7bb76ebbd92ce3ef9646ab47ed44f2fc8698ccacae01207f35090634e0d96dcb.jpg)  
Fig. 8. A conceptual model of transaction after bidding.

```txt
...
tobe_delivered_goods
: HomeTheaterSystem1
...
END
```

The success of DL's bid on the VirtualAuctionItem will result in the deletion of this particular bid from DL's currently active bid association attribution relation and addition to DL's bid history.

Token DL

END

The particular good, HomeTheaterSystem is to be delivered by UPS.

Token UPS

goods\_tobe\_delivered

: SSI\_HomeTheaterSystem1

END

SSI\_HomeTheaterSystem1 will have a buyer added to it upon the receipt of payment received by the good producer, SSI.

Token SSI\_HomeTheaterSystem1

buyer : DL

END

Thus, construction of the formal model and tracking of the conceptual model through all stages of the dynamic virtual market transaction increases the designer's understanding of the virtual market transaction and provides a balanced view of the design and implementation of futuristic VMIS systems. The ability of our model to adapt to change and evolution over time, along with the active maintenance of the overall consistency of the conceptual model using rules and integrity constraints, provides a comprehensive and useful model for detailed study of such systems.

## 6. Conclusions

In this paper, we have proposed a framework for constructing ontologies focusing on VMISs. We have described a fully functional VMIS conceptual modelling framework, based on careful analysis and abstraction of those VMISs using a real-world virtual market as an example. This conceptual model provides several novel features:

\- An Integrated Hybrid Modelling Framework: Our conceptual framework is based on a powerful knowledge representation language.

\- Meta Level Facilities: MetaClass and meta-attribute facilities are provided for customising the domain classes to a particular application, while still maintaining a generic and reusable modelling framework.

\- Constraint Enforcement: Our VMIS conceptual modelling framework includes well-defined constraint enforcement facilities that can be extended to consistency checking with a particular VMIS.

\- Inference Facilities: The powerful assertional language provides reasoning capabilities within the VMIS. The future VMISs may contain intelligent cooperative information agents that our framework can model.

\- Temporal Dependencies: Ability to commit the life and relationships temporally allows the conceptual model to be dynamic rather than static.

By creating a rich and precise conceptual framework of VMISs, our work provides a solid framework for IT/IS practice. The development of a formal conceptual model provides the basis for formal study of VMISs. The application of our formal VMIS models can lead to unambiguous understanding of the concepts, and pinpoint the likely cause of confusion. Furthermore, such models provide a uniform framework with which different VMISs can be compared in terms of their individual strengths and weaknesses.

## Acknowledgements

This research is supported by the research grants (No. 9040231 and 7000564) from the Hong Kong Government and the City University of Hong Kong. The author is grateful to the Chief Editor, Professor Edgar H. Sibley, for his constructive comments and heavy editing on an earlier draft of this paper.

## References

[1] R. Alt and S. Zbornik, (Eds.) EM: Electronic Markets, Vol. 3, No. 9.

[2] A. Armstrong and J. Hagel III, “The real value of on-line communities,” Harvard Business Review, (1996) pp. 134–141.

[3] Y. Bakos, “Electronic marketplace,” MIS Quarterly, (1991) pp. 295–310.

[4] R. Benjamin and R. Wigand, “Electronic markets and vortual value chains on the information superhighway,” Sloan Management Review, (1995) pp. 62–72.

[5] M. Brodie, J. Mylopoulos and J. Schmidt (Eds.), On Conceptual Modelling, Springer-Verlag, New York, 1984.

[6] M. Brodie, "The promise of distributed computing and the challengers of legacy information systems," Proceedings of 10th British National Conference on Databases, Springer-Verlag, New York and Heidelberg, 1992.

[7] W.H. Davidow and M.S. Malone The virtual corporation, HarperCollins Publishers Inc., 1992.

[8] V. Gurbaxani and S. Whang, “The impact of information systems on organizations and markets,” Communications of the ACM, 34(1) pp. 59–73.

[9] C. Handy, “Trust and the virtual organization,” Harvard Business Review, (1995) pp. 42–50.

[10] H.R. Hansen, “Conceptual framework and guidelines for the implementation of mass information systems,” Information and Management, 28(2) (1995) pp. 125–142.

[11] H. Kangassalo, “COMIC: A system and methodology for conceptual modelling and information construction,” Data and Knowledge Engineering, 9 (1993) pp. 287–319.

[12] W.J. Kettinger, “National infrastructure diffusion and the U.S. information super highway,” Information and Management, 27(6) (1994) pp. 357–368.

[13] T. Malone, J. Yates and R. Benjamin, “Electronics markets and hierarchies,” Communications of the ACM, (1987) pp. 485.

[14] T. Malone, J. Yates and R. Benjamin, “The logic of electronic markets,” Harvard Business Review, (1989) pp. 166–172.

[15] M. Minsky “A conversation with marvin minsky about agents,” Communications of the ACM, 37(7) (1994) pp. 23–29.

[16] J. Mylopoulos, etc., “Telos: A language for representing knowledge about information systems,” ACM Trans. on Information Systems, 8(1) (1990) pp. 325–362.

[17] “Hopes and Fears on new Computer Organisms,” New York Times, January 6, 1994, p. D1.

[18] D. Rosenthal, S. Shah, B. Xiao, “The impact of purchasing policy on electronic markets and electronic hierarchies,” Information and Management, 25(2), pp. 105–117.

[19] Y. Wand, D.E. Monarchi, J. Parsons and C.C. Woo, "Theoretical foundations for conceptual modelling in information systems development," Decision Support Systems, 15 (1995) pp. 285-304.

[20] H. Wang and C. Wang, “Ontologies for universal information systems,” Journal of Information Science, 21(3) (1995) pp. 232–239.

![](/api/attachments/F8WGSENH/fulltext/images/9bb9dbed96b48103cd2922a1ae9434ff38395e2701d9cc29cb1a7ed5ffffc7d7.jpg)

Dr. Huaiqing Wang is an associate professor of the Department of Information Systems, City University of Hong Kong. His research and teaching interests include knowledge-based analysis and systems, conceptual modelling, multimedia, hypermedia, and Internet/Intranet based IS areas in which he has published extensively. He received his Ph.D. in artificial intelligence and knowledge based sys-

tems from the University of Manchester, Institute of Science and Technology in 1987, his MS in Computer Science from Huazhong University of Science and Technology in 1982.
