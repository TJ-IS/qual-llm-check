---
otero_id: 11530
otero_key: "KKQMSV8U"
title: "Preventing ticket-switching of RFID-tagged items in apparel retail stores"
authors: "Wei Zhou; Selwyn Piramuthu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.03.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Wei Zhou <sup>a,c</sup>, Selwyn Piramuthu <sup>b,c,</sup>⁎

<sup>a</sup> Information & Operations Management, ESCP Europe, Paris, France

<sup>b</sup> Information Systems and Operations Management, University of Florida, USA

<sup>c</sup> RFID European Lab, Paris, France

## a r t i c l e i n f o

Article history: Received 25 July 2012 Received in revised form 9 January 2013 Accepted 26 March 2013 Available online 10 April 2013

Keywords: RFID authentication protocol Ticket-switching Retailer Identi<sup>fi</sup>cation

## a b s t r a c t

When a retail store places an item for sale at a set price, the expectation is that the customer pays this price for the item. However, the ‘customer’ may not necessarily pay this amount due to any number of legitimate (e.g., price promotion) as well as illegitimate (e.g., theft) reasons. We consider ticket-switching, a scenario whereby the customer pays a lower amount for the purchased item by switching its price identi<sup>fi</sup>er. We propose the use of item-level RFID tags to address ticket-switching in apparel retail stores. We then develop authentication protocols that are directed at reducing the occurrence of ticket-switching incidents as well as identifying them when they occur. We evaluate the security properties of the proposed protocols.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

RFID (Radio-Frequency IDenti<sup>fi</sup>cation) provides a unique way to identify as well as to track and trace products. Automated identi<sup>fi</sup>cation [14] facilitates more accurate and faster services in real-time and consequently reduces operational and transactional costs and lead time. It is known that neither automated nor traditional (manual) identi<sup>fi</sup>cations are 100% accurate [10]. Along with other causes such as inventory misplacement (e.g., [15,19]) and theft [20], identi<sup>fi</sup>cation errors resulting from natural detachment or intentional separation of identi<sup>fi</sup>- cation and/or price tags contribute to inventory shrinkage in retail stores. Moreover, identi<sup>fi</sup>cation loss can result in a much larger problem than just inventory shrinkage and can extend to issues related to marketing, customer relationship management and supply chain coordination.

A majority of shrinkage in retail stores are not witnessed but established by audit. According to the Global Retail Theft Barometer, which is an annual study that is underwritten by a grant from Checkpoint Systems, retail shrinkage in 2011 cost the industry an estimated \$119 billion, which is about 1.45% of overall sales. Among different retail categories, apparel and accessories experienced the highest shrinkage, with outerwear experiencing a shrinkage of 2.94%. While these percentages appear to be rather small, it should be noted that even a 2 to 3% loss of sales can amount to about 25% loss in pro<sup>fi</sup>t in this industry with tight pro<sup>fi</sup>t margins [23]. Several earlier studies conclude with similar numbers (e.g., [3,4]).

Several means to combat shrinkage are widely used in apparel retail stores, including ink tags and electronic article surveillance (EAS). There are several different types of EAS, which include magnetic, acousto-magnetic, radio-frequency, and microwave systems. Ink tags are reusable tags that contain a few (e.g., three) embedded glass vials <sup>fi</sup>lled with indelible ink meant to soil the garment and the tamperer's hands. These tags can be easily removed from the tagged item by store personnel at the point-of-sale using a special tool. However, when removed improperly, the glass vials are designed to break and the garment with an ink stain can neither be worn nor sold. Clearly, ink tags and a majority of existing EAS target shrinkage due to external sources (vs. store personnel).

The ideal scenario is one in which there is no shrinkage (e.g., items lost to theft or process errors, items that are misplaced within the store and are therefore unavailable for sale to potential customers) [18] and every item is sold at its full-price within a reasonable time duration. However, this is not always the case and a few of the items that arrive at the store are invariably lost either temporarily (e.g., misplaced at the store) or permanently (e.g., theft, destroyed during handling) while at the store. Such incidents result in preventable unnecessary monetary and other (e.g., customer goodwill) loss to the retailer.

We consider a speci<sup>fi</sup>c type of shrinkage [18] known as ticketswitching, which is the illegitimate act of switching the price identi<sup>fi</sup>er on an item that results in the customer paying less than the item's retailer-set selling price. Speci<sup>fi</sup>cally, the price identi<sup>fi</sup>er on an item is switched with one (from another item) that represents a lower price. In the simplest case, the price identi<sup>fi</sup>er could be just the price tag in a scenario where the seller manually looks at the (hand-written or printed) price tag(s) to note the price for each item and tallies the total transaction amount. To our knowledge, statistics on retailer loss due to ticket-switching is hard to get simply because of its nature as well as the simultaneous presence of other types of shrinkage.

Ticket-switching is most likely here to stay. It happened and continues to happen with simple price stickers, it happens with bar codes, and will most likely happen with the placement of item-level RFID tags in retail stores. With the increasing trend toward item-level RFID tags (e.g., Wrangler jeans in Wal-Mart, entire American Apparel store, entire Trasluz store) in retail stores and related automation of processes such as inventory management and check-out, there is an increased potential to exacerbate this situation due to reduced human interaction in the process. There is, therefore, an urgent need to <sup>fi</sup>nd a solution to address ticket-switching of RFID-tagged items. We consider ticketswitching in apparel retail stores that occurs as a direct result of a customer deliberately switching the price identi<sup>fi</sup>er on an item in order to pay a lower price for that item. Speci<sup>fi</sup>cally, we assume the presence of item-level RFID tags and develop cryptographic authentication protocols that help address ticket-switching in a retail store environment.

Authentication protocols [16] for RFID tags have been developed for a wide variety of scenarios including ownership transfer (e.g., [11,26]), mutual authentication (e.g., [17]), among others. However, to our knowledge, there is a lack of published research that speci<sup>fi</sup>cally addresses ticket-switching in retail stores with item-level RFID tags. We purport to address this gap by considering a few related scenarios and developing authentication protocols that help reduce ticketswitching incidents in apparel retail stores. Our choice of these scenarios is based on our previous experience with similar issues in retailing in that they depict likely issues and possible solutions to address ticketswitching. Speci<sup>fi</sup>cally, we consider (a) the scenario where a reusable active RFID tag, with no item-level information, embedded in an ink tag is used along with an item-level passive RFID tag with itemspeci<sup>fi</sup>c information to prevent theft and ticket-switching, (b) a scenario where a third tag is used for store-speci<sup>fi</sup>c promotional information and (c) accidental or intentional separation of a tag. While we consider apparel retail store as an example application domain for the proposed authentication protocols, the proposed protocols are readily applicable to retail store applications where any type of EAS or ink tag is used.

The purpose of this paper is two-fold and includes (a) raising awareness among researchers toward the overlooked issue of ticketswitching and (b) providing item-level RFID-based solutions through cryptography to a few selected possible scenarios in the context of ticket-switching. The remainder of this paper is organized as follows: we brie<sup>fl</sup>y discuss the concept of item identi<sup>fi</sup>cation and its related consequences from the perspective of ticket-switching in Section 2. We then consider three different scenarios related to ticket-switching and develop authentication protocols for these scenarios in Section 3. In addition to developing authentication protocols, we provide security analysis of the authentication protocols. We conclude the paper with a brief discussion in Section 4.

## 2. Item identi<sup>fi</sup>cation

An item's identi<sup>fi</sup>cation is critical in environments where instances of several different types of items are simultaneously present. Similar to DNA, the item's identi<sup>fi</sup>er generally holds necessary item-speci<sup>fi</sup>c information. In an apparel retail store environment, an item can possibly have anywhere from one (Fig. 1) to several (Fig. 2) identi<sup>fi</sup>ers.

When multiple identi<sup>fi</sup>ers are present, necessary information about the item are distributed among these identi<sup>fi</sup>ers and when only a single identi<sup>fi</sup>er is present, it has all the necessary information on the item of interest.

The loss of identi<sup>fi</sup>cation of an item at a retail store could signify the (even if temporary) inability of the retailer to locate its selling price which could, in the worst case, precipitate in the item not being sold to an interested customer. The identi<sup>fi</sup>cation of an item can be lost at a retail store due to several reasons including (a) natural loss, whereby the item's identity (e.g., price tag, label) accidentally gets separated from the item, or the deliberate removal by someone or (b) ticket-switching. We consider these in turn in this section.

![](/api/attachments/KKQMSV8U/fulltext/images/2735800456c10842d4fc9ce28b558febbb3c758b5728e698fb7b927ba04235c1.jpg)  
Fig. 1. Item-level identi<sup>fi</sup>cation.

## 2.1. Identification loss

At an apparel retail store, the identi<sup>fi</sup>ers (e.g., bar codes, RFID tags) contain the identi<sup>fi</sup>cation information on the item. Without these identi<sup>fi</sup>ers, especially at an apparel retail store that deals with thousands of items, it is dif<sup>fi</sup>cult to identify the item. Clearly, therefore, the retail store has no incentive to separate an item from its identi<sup>fi</sup>er. Nevertheless, incidents where an item is separated from its identi<sup>fi</sup>er(s) in an apparel retail store environment are not unheard of (Fig. 3). Such an incident could be the result of (a) intentional or deliberate separation or (b) unintentional or accidental loss or separation of an item from its identi<sup>fi</sup>er.

While unintentional or accidental loss or separation of an item from its identi<sup>fi</sup>er cannot be prevented under all circumstances, this is an operational issue and the number of such occurrences can therefore be reduced through appropriate measures. For example, one such measure could be the use of identi<sup>fi</sup>ers that are dif<sup>fi</sup>cult to separate from the item or those that can withstand rough handling by store personnel and customers. On the other hand, intentional or deliberate separation of an item from its identi<sup>fi</sup>er can be prevented or at least the number of such incidents can be reduced through (a) reduction or elimination of incentives for the perpetrator, (b) implementation of mechanisms whereby such incidents are immediately identi<sup>fi</sup>ed, or (c) rendering it extremely dif<sup>fi</sup>cult to separate an item from its identi<sup>fi</sup>er (e.g., ink tags).

## 2.2. Ticket-switching

To our knowledge, while it may be possible to separate shrinkage cases that are intentional from those that are unintentional, there is no publicly available statistics on the exact amount of loss associated with ticket-switching due to the dif<sup>fi</sup>culty in (a) identifying which item was switched for which, (b) measuring related loss due to excess inventory (inventory cost) and stock-outs (opportunity cost), and (c) differentiating ticket-switching from theft and other types of shrinkage. Nevertheless, only a few of the ticket-switching cases that involve relatively expensive items that are caught are reported in the news media. For example, a customer at a San Francisco Bay Area Target store was caught af<sup>fi</sup>xing home-made bar codes to packages of LEGOs that allowed him to purchase expensive sets at substantial discounts [21,22]. He apparently then sold these items on eBay and made about \$30,000 from these sales. Two couples were charged with defrauding Wal-Mart stores in 19 states of \$1.5 million over the last decade where a home computer was used to print bar codes for cheaper items which were then placed on expensive items before check-out. The suspects then allegedly sold the merchandize, or returned them for refund or store gift cards. These suspects apparently avoided detection in part by visiting stores during the busiest periods. A Colorado University freshman used home-printed bar codes in his dorm room using ‘Barcode magic’ to buy big-ticket electronic gadgets cheap at a local Target store. For example, he made a bar code for a CD player that cost \$24.99 to buy a system for using iPods valued at \$249.99. A customer at a Leclerc supermarket in Trélisssac, Dordogne was caught for replacing the labels on two €2300 bottles of Petrus with €2.50 labels [1].

![](/api/attachments/KKQMSV8U/fulltext/images/c87aa47326541835c22ff82c530171c12ba7af159310910bb898485e6e2076b0.jpg)  
Fig. 2. Item-level identi<sup>fi</sup>cation with multiple tags.

![](/api/attachments/KKQMSV8U/fulltext/images/98a7043ba74bb45df2b63c9bd7300bef43a9185dac4d3f47c85848ab82081734.jpg)  
Fig. 3. Loss of item identi<sup>fi</sup>cation information.

It is reasonable to assume that ticket-switching (Fig. 4) has existed since the advent of ‘price tags’, which could in the simplest case just be a hand-written price on the item of interest. It is also relatively dif<sup>fi</sup>cult to catch such ticket-switching behavior with an increase in the sheer number of items that are for sale at any given location.

While enabling faster inventory-taking and check-out, the introduction of bar codes rendered it relatively easy to successfully ‘purchase’ a ticket-switched item since the check-out person may not necessarily double-check to ensure that the item indeed matches the information associated with the scanned bar code. Among different priceidenti<sup>fi</sup>cation technologies, price stickers are the easiest to switch since they don't have any information on the associated item. On the other hand, bar codes have relevant information (e.g., the items' identity) stored in database(s) that are readily accessible to the retail store checkout personnel.

Regardless of the price identi<sup>fi</sup>er (e.g., price sticker, bar code, RFID tag), a ‘customer’ removes the one from a lower priced item and switches this with that from an item that sells for a higher price which is then ‘purchased’ at the lower price. From the customer's perspective, a simple (sticker) price tag is the easiest to switch but dif<sup>fi</sup>cult to check-out while an RFID tag is the most dif<sup>fi</sup>cult to switch and easiest to check-out of the store. In the former case (i.e., simple price tag), the price tag is af<sup>fi</sup>xed or attached on the item and is therefore easy to switch but the priceswitched item has a positive probability of being discovered by the check-out personnel with any knowledge of the item's actual selling price. In the latter case, ticket-switching is dif<sup>fi</sup>cult to accomplish since (a) it is dif<sup>fi</sup>cult to copy/clone [13] the content of the RFID tag and (b) the tag may be embedded in the item. Moreover, the ‘customer cannot switch the RFID tag from an already-purchased ‘cheap’ item since the system knows (because of unique item-level information) that that tagged item was already purchased from the store — i.e., can't buy an item more than once. However, it is relatively easy to remove an RFIDtagged ticket-switched item from the store when there's automated check-out. In the case of bar code, it is relatively easy to ticket-switch since bar codes are always af<sup>fi</sup>xed on the item. However, it is relatively dif<sup>fi</sup>cult to pay the ticket-switched price for this item since the checkout personnel could check to ensure that the bar code scan refers to the exact physical object being purchased. For the rest of the paper, we use ‘cheap’ and ‘expensive’ to refer to the items that are targets for ticket-removal and ticket-switching respectively.

![](/api/attachments/KKQMSV8U/fulltext/images/35ffc244a21dc358b8ac37f9a00c05ef952dcedaedca98107b6dbcf6be267ccd.jpg)  
Fig. 4. Ticket-switching.

Ticket-switching is not uncommon in reality, although not all such incidents are identi<sup>fi</sup>ed when they occur and the retailer suffers the consequences of related loss in several ways. When ticket-switching occurs, the retail store's information system incorrectly shows the presence of more expensive items and fewer cheap items than the actual state of its inventory. When several ticket-switching incidents occur at the same retail store, this mismatch between actual and information-system-based inventory levels could wreak havoc on effective inventory management. Moreover, its consequences could include stock-outs (e.g., of the expensive items that generally have larger marginal revenue to the retail store), excess inventory of the ‘cheap’ item (which could lead to increased storage for these items and loss of perishables) and increased inventory costs related to ‘cheap’ items.

## 3. The proposed authentication protocols

In apparel retail stores, it is common to use ink tags to prevent item theft since these tags (a) are dif<sup>fi</sup>cult to remove without necessary equipment and (b) have security features that include breakage of glass vials containing permanent ink when a tag is removed improperly and triggering an alarm when removed from the store. These ink tags have been repeatedly shown to be quite effective in drastically reducing apparel theft in retail stores (e.g., [3,4] and the references therein). Since these ink tags are rather generic in that any of these can be placed on any apparel, they are not unique to any speci<sup>fi</sup>c item instance at the store. To place item-speci<sup>fi</sup>c information, or rather class-/SKU-speci<sup>fi</sup>c information, retail stores place a printed price tag with a bar code that can then be used to retrieve additional information (e.g., price, brand) from an associated database. While this ink-tag&price-tag combination works quite well in an honest environment, these price tags can be easily switched by a dishonest customer.

As mentioned in Section 1, we <sup>fi</sup>rst consider a retail store scenario where an active RFID tag that can initiate conversation with another RFID tag or an RFID reader is embedded in the ink tag. Along with a passive RFID ‘price tag,’ this active RFID tag can be used to drastically reduce theft as well as ticket-switching incidents. We then consider a scenario where a retail store has item-speci<sup>fi</sup>c promotions perhaps due to exceptional circumstances. Currently, when apparel retail stores discount speci<sup>fi</sup>c items, they have several options: (a) place a new (possibly of a different color) bar code over an existing bar code on the price tag with the discounted price printed on the price tag, (b) place a sticker with the discounted price on an existing price tag with no change to the bar code. While in the former, the information system should be modi<sup>fi</sup>ed to recognize this bar code and its associated item and price, the latter case requires the check-out person to manually over-ride the item's price when processing the transaction. In chain retail stores, it is generally not possible to locally modify the price of one instance of an SKU (say, a shirt with a missing button) in the information system since the database with price information are designed, developed and updated in a centralized manner and are then (periodically as the situation dictates) distributed to all the retail stores belonging to this chain. This distribution of periodic updates (as per the requirements that are generated based on the time and duration of promotions in that region) are generally accomplished simultaneously in all the stores belonging to this retail chain and the essential (e.g., price) information in the store's computers are write-protected and cannot be locally modi<sup>fi</sup>ed. This necessitates resorting to option (b) mentioned above and allowing the check-out personnel to manually over-ride the price in the system.

To complete possible related scenarios, we also consider the case where a passive tag is accidentally or intentionally detached from the item.

## 3.1. System model

## 3.1.1. Principals

Our system comprises the following three principals: customers, RFID-tagged items, and retailer (Fig. 5).

The RFID-tagged item contains two RFID tags: an active tag that is embedded in the ink tag and a passive RFID price tag that contains item-level information. When the item is scanned, either manually using a hand-held reader or by a check-out person or automatically by a shelf-based reader or an automated check-out system, both the tags are read by the reader. The active tag is primarily used together with the ink tag as an anti-theft device and the passive price tag is primarily used to facilitate in-store processes such as inventory management and automated-checkout as well as reduce shrinkage due to theft, misplacement, missing identi<sup>fi</sup>er (i.e., an item that is devoid of any identi<sup>fi</sup>er such as price tag or label), and processing errors. Together, the two tags help authenticate the tagged item.

## 3.1.2. Adversary model

Based on its environment (i.e., an apparel retail store), possible threats to the authenticity of the RFID-tagged item can come from manipulated active tag or passive tag or both. Other forms of threats include any form of attack (e.g., replay attack) that would enable a dishonest ‘customer’ to pay less for the item than its retailer-intended price.

## 3.1.3. Assumptions

We assume the adversary ( ) to follow the Dolev–Yao intruder model [5]. The adversary has complete control over the communication between the RFID-tagged item and the retail store system whereby can eavesdrop, block, modify, and inject messages anytime from/to any entity.

![](/api/attachments/KKQMSV8U/fulltext/images/48940fc18cc47dc1aa7a7ec4f61b9f5d4285267fedd8c87d00616cb5f8a7b357.jpg)  
Fig. 5. The relationship among principals.

We are interested in ensuring that the customer pays exactly the retailer-set price and receives the exact item as promised in the transaction. Reduction in price due to discounts (e.g., coupons) is irrelevant for this study. We also do not consider the scenario where the retailer erroneously enters a wrong price for an item in the system.

We assume that when the active-tag-embedded-ink-tag is placed on the item, it is synchronized with the passive tag placed on that item. From this time onward until the ink tag is separated from the item upon the item's purchase, the active-tag/passive-tag pair for an item remains the same. When the ink tag is separated from the item, the passive tag's secret key is modi<sup>fi</sup>ed by a trusted third party and the active tag will no longer be able to communicate with this passive tag.

## 3.2. Security properties

The proposed protocols should have the following security properties:

Correctness: The customer pays exactly the retailer-set price for an item.

Prevention of identification information loss: Since the passive tag(s) contain(s) item-level information (e.g., brand, price), the loss of a passive tag could potentially lead to loss of the item's identi<sup>fi</sup>cation information. However, the proposed protocols must ensure that the item's identi<sup>fi</sup>cation information cannot be lost — i.e., it should be possible with relative ease to locate the item's identity even with the loss of its passive tag(s).

Accountability: It should be possible to recognize if/when separation of a passive tag from the item occurs. With this information, it should be possible to determine whether this event is accidental or due to intentional act on the part of someone. When it is intentional, it should be possible to identify the party responsible for this act.

## 3.3. Notations

We use the following notations throughout the rest of the paper:

$r _ { A } , r _ { T } ,$ , r : l-bit nonce

• $k _ { A } ,$ k , k′: active and passive tags' shared secret keys

$I D _ { A } , I D _ { P } ,$ ID′: active and passive tag IDs

• f<sub>k</sub>: keyed (with key k) encryption function

• auth: authentication request

• PTIreq: request for passive tag(s) identi<sup>fi</sup>cation information

$x \gets y \colon$ assign y's value to x

## 3.4. Authentication protocol for regular items

We <sup>fi</sup>rst develop the protocol to authenticate regular (i.e., those not associated with exception handling situations) items at an apparel retail store. Since the active tag that is embedded in the ink tag is reused and is independent of the item on which it is placed and the passive tag is item-speci<sup>fi</sup>c and is not reused, these two tags need to be synchronized before the tagged item can be authenticated. We split the process into two main stages. During the <sup>fi</sup>rst stage, the active and passive tags are synchronized. The protocol for this stage is given in Fig. 6.

Coordination of this stage is handled by a trusted third party (TTP). The process begins with the active tag generating a fresh nonce $\left( r _ { A } \right)$ and sending this, along with its identi<sup>fi</sup>er $\left( I D _ { A } \right)$ encrypted using its shared key $\left( k _ { A } \right)$ , to the TTP. From this message, the TTP identi<sup>fi</sup>es the active tag and proceeds to communicate with and identify the passive tag. To this end, it generates a fresh nonce $\left( r _ { T } \right)$ and sends it to the passive tag, which upon receipt of this nonce generates its own nonce $\left( r _ { P } \right)$ and sends its identi<sup>fi</sup>er $\left( I D _ { P } \right)$ encrypted using its shared secret (k ) to the TTP. The TTP is now able to identify and match the two (i.e., active and passive) tags that belong to this item. The TTP then sends $I D _ { P }$ and k to the active tag. The active tag now possesses its counterpart's identi<sup>fi</sup>er $( \mathrm { i } . { \mathrm { e } } . , I D _ { P } )$ and shared secret key (i.e., k ).

The tagged item's authentication proceeds as given in Fig. 7. The veri<sup>fi</sup>er, which could be a hand-held reader, a reader mounted on the shelf or wall at the retail store, or the reader at the check-out, initiates the process by generating a fresh nonce $( r _ { V } )$ and sending it to the active tag. This request is accompanied with a request for authentication (i.e., auth). Upon receipt of this nonce from the veri<sup>fi</sup>er, the active tag generates its own nonce $\left( r _ { A } \right)$ and sends the passive tag's identi<sup>fi</sup>er $\left( I D _ { P } \right)$ encrypted with its own shared secret key $\left( k _ { A } \right)$ . The veri<sup>fi</sup>er now has enough information to identify the active–passive tag pair. The veri<sup>fi</sup>er then forwards a part of the message from the active tag (i.e., $r _ { A } , f _ { k _ { P } } ( r _ { A } , I D _ { P } ) )$ ) to the passive tag. In response, the passive tag generates a fresh nonce (r ) and sends its identi<sup>fi</sup>er $\left( I D _ { P } \right)$ encrypted using its shared secret (k ) to the veri<sup>fi</sup>er. The veri<sup>fi</sup>er validates the tag based on this message.

To avoid race conditions and denial of service (DoS) attacks, the originators of all messages that require a response from the recipient wait for a pre-determined period of time for a response before regenerating and re-sending their earlier message with a fresh nonce. Moreover, to prevent replay attacks, all such messages are also randomized by the use of freshly-generated nonce to avoid predictability of response.

<table><tr><td>Active Tag $ID_A, k_A$ </td><td></td><td>TTP $ID_A, k_A, k_P, ID_P$ </td><td></td><td>Passive Tag $ID_P, k_P$ </td></tr><tr><td> $r_A \leftarrow \{0,1\}^l$ </td><td> $\xrightarrow{r_A, f_{k_A}(r_A, ID_A)}$ </td><td rowspan="2">identify activetag from  $ID_A$  $r_T \leftarrow \{0,1\}^l$ identify passive tag from  $ID_P$ match ( $ID_A, ID_P$ ) pair</td><td rowspan="2"> $\xrightarrow{r_T}$  $\xleftarrow{r_P, f_{k_P}(r_T, r_P, ID_P)}$ </td><td rowspan="2"> $r_P \leftarrow \{0,1\}^l$ </td></tr><tr><td>retrieve  $ID_P, k_P$ </td><td> $\xleftarrow{r_T, ID_A \oplus k_P, ID_P \oplus k_A, f_{k_P}(ID_P, r_T)}$ </td></tr></table>

Fig. 6. Sharing passive tag's keys with the active tag.

W. Zhou, S. Piramuthu / Decision Support Systems 55 (2013) 802–810

<table><tr><td>Active Tag $ID_A, k_A$ </td><td></td><td>Verifier $ID_A, k_A, k_P, ID_P$ </td><td></td><td>Passive Tag $ID_P, k_P$ </td></tr><tr><td> $r_A \leftarrow \{0,1\}^l$ </td><td> $\xrightarrow{r_V, auth}$  $\xrightarrow{r_A, f_{k_P}(r_A, ID_P), f_{k_A}(r_V)}$ </td><td> $r_V \leftarrow \{0,1\}^l$ identify  $(ID_A, ID_P)$  pairvalidate passive tag</td><td> $\xrightarrow{r_A, f_{k_P}(r_A, ID_P)}$  $\xleftarrow{r_P, f_{k_P}(r_A, r_P, ID_P)}$ </td><td> $r_P \leftarrow \{0,1\}^l$ </td></tr></table>

Fig. 7. Simultaneous authentication of active and passive tags.

Once both the tags are authenticated, item-speci<sup>fi</sup>c information such as the brand, price, etc. are retrieved from the item-level passive RFID price tags.

## 3.5. Authentication protocol for exception items

Unlike the scenario in Section 3.4 where we considered a regular item that is for sale (at a class-level) in the entire store or even the entire set of stores belonging to this chain that sell this item, we now consider an exception handling scenario. By exception we refer to the items that are not considered regular or normal due to existing de<sup>fi</sup>cits (e.g., missing button, tear, minor to major damage) or even those that were returned by a customer. These de<sup>fi</sup>cits most likely would have occurred since the item initially arrived at the retail store due to any number of reasons such as accidental mishandling by customers or store employees. Since the retail store does not consider these items as perfect and new in such situations, their prices are generally marked down to re<sup>fl</sup>ect the extent of the present de<sup>fi</sup>cit. While this works perfectly in manual environments with a simple price tag whereby the items' price information are manually entered in the system during check-out, it is somewhat complex when any automation (e.g., bar codes, RFID) is used. For example, when bar codes are used to scan the item for information on the item and its sale price, it is necessary for the system to accurately retrieve the item's correct price. The stores generally use a different bar code on such items, possibly in a different color (e.g., red), to highlight the fact that this item is not being sold at its regular (full) selling price. Similarly, when RFID tags are used as price tags, there is a need to re<sup>fl</sup>ect the fact that an item belongs to an exception case.

Note that when there is a promotion and the selling price of an entire class of items (say, all shirts from brand B) is discounted by a certain percentage, it is relatively straight-forward to handle this in the information system (e.g., in the database) by taking the discount whenever shirts from brand B are scanned. However, it is not the case when an exception shirt (say, shirt S) from brand B is scanned — it is rather dif<sup>fi</sup>- cult for a system that is programmed to handle items at a class level to deal with items at an instance level.

We suggest the use of a simple second passive tag that has the discount information. The rationale for this additional passive tag are two-fold: (1) accidental or intentional removal of this second passive tag that presumably has the discounted price would not result in the customer paying less, and (2) it is easy for the system to deal with the original two tags (i.e., the active RFID-embedded ink tag and the original passive tag) in a consistent manner and place any additional information in the second passive tag.

A schematic for synchronization and authentication of the two passive tags and the active ink tag is given in Fig. 8. The sequence in the beginning is the same as that for the scenario presented in Section 3.4. However, once an exception situation occurs and is identi-<sup>fi</sup>ed by the store personnel as such, the conditional branching scenario occurs whereby the need for price discount is determined by the store personnel. When price discounting is determined to be required, a second passive (exception) tag is placed on the item and the activetag-embedded ink tag is synchronized with this second passive tag (Fig. 6). Authentication of this pair (the active tag and the passiveexception tag) proceeds similar to that of the other passive tag and the active tag (Fig. 7).

## 3.6. Item authentication with accidental loss of a passive tag

In retail stores, it is not uncommon for a price sticker or a bar code price tag to be accidentally (and permanently) separated from the item. When this happens, the most common response is to look for an identical item in the store to decide on the item's price. While this procedure works perfectly when an identical item can be readily located in the store, it becomes cumbersome when this is the last item of its type in the store. It is rather dif<sup>fi</sup>cult to look up an item's identi<sup>fi</sup>cation (e.g., SKU number) or price in the store's computer system based solely on the item's visible characteristics when the item's identi<sup>fi</sup>cation information is permanently lost. Under such circumstances, given their time and other resource constraints, the best the store personnel can do is to look for a similar item (i.e., an item that matches on as many characteristics as possible with that of the item with missing identi<sup>fi</sup>cation information) and charge that item's price. While this may seem reasonable, it is possible for this to precipitate in the customer having to over- or under- pay for the item. The situation is even worse when a similar item cannot be located in the store. Note that even though the clothing item may still have the ink tag <sup>fi</sup>rmly attached, this ink tag generally does not have any item- or even class- speci<sup>fi</sup>c information that would help in identifying this tagged item.

![](/api/attachments/KKQMSV8U/fulltext/images/a51e20f6ac03aaa27f7d6be0d264bc75136ba37f79b44fce3984406a5272fe71.jpg)  
Fig. 8. A schematic for synchronization and authentication of tags in the presence of exception

![](/api/attachments/KKQMSV8U/fulltext/images/056c89e8f69037ab301085f17889470c04524254f94da67f4ee58e9b781cc4f8.jpg)  
Fig. 9. Retrieving identi<sup>fi</sup>cation information on associated passive tag(s).

Similar to the case when price stickers or bar codes are used, the use of RFID tags also leaves open the possible occurrence of situations when the passive tag may accidentally get separated from the item. Note that the probability of the active-tag-enabled ink tag accidentally separating from the item is close to zero since it is securely attached to the item with a locking mechanism. However, when the passive tag in the scenario mentioned in Section 3.4 gets accidentally (or even possibly intentionally) separated from the item, all is not lost since the active tag has essential information about its paired passive tag(s) for the item of interest.

The proposed protocol for retrieving identi<sup>fi</sup>cation information on passive tag(s) that are associated with a given active-tag-enabled ink tag for an item of interest is given in Fig. 9. Here, k′ and ID′ are respectively the shared secret key and identi<sup>fi</sup>er of the second passive tag on an item. We represent the secret key and identi<sup>fi</sup>cation (k′, ID′) information for the second passive tag in square brackets since not all items have this optional second tag. A trusted third party (TTP) initiates this protocol with the generation of a fresh nonce (r ) and sending this to the active tag that is attached to the item with the missing passive tag(s). The nonce is sent along with an explicit request for the passive tag(s) identi<sup>fi</sup>cation information (i.e., PTIreq). Upon receipt of this message, the active tag generates its own nonce (r ) and sends the identi<sup>fi</sup>cation information (i.e., ID(s)) of associated tag(s) encrypted with its own shared secret key (k ). The TTP is now able to retrieve the ID(s) of the missing passive tag(s). Since the IDs are unique among passive tags in the system, it is now easy to retrieve other information (e.g., brand, price) for this item.

When an item has two passive tags, the loss of any one of them would be handled in a similar manner. The active tag contains the identi<sup>fi</sup>ers for both the tags and the protocol provided in Fig. 9 can be used to locate the missing identi<sup>fi</sup>er.

## 3.7. Security analysis of the authentication protocol

We provide security analysis of the authentication protocol presented in Fig. 7 (Section 3.4). Since the other two protocols (Figs. 6 & 9) are similar in structure, their security properties are identical to the protocol presented in Fig. 7. We <sup>fi</sup>rst consider a few different possible attacks on this authentication protocol and then use GNY logic [8] to complement the analysis.

## 1. Secrecy/data integrity and authenticity:

The cryptographic methods used (e.g., the encryption function f ) and not sending any private information such as keys in clear text reasonably guarantees the secrecy of the message. The authenticity of the communicating parties is guaranteed by the keyed hash functions.

## 2. DoS/synchronization problem:

For every message that initiates a conversation between two entities, we ensure that the initiating entity receives a response for each message it sends. If a response or acknowledgment is not received in a pre-determined amount of time, the message is repeated with a freshly-generated nonce as appropriate. Therefore, instances where adversaries block messages between two entities are easily addressed. Moreover, since we do not update any entity-speci<sup>fi</sup>c (e.g., keys, ID) secure information after or during an authenticationround, there are relatively fewer opportunities for desynchronization attacks.

## 3. Passive replay:

Since we use freshly generated random nonce in all the messages, it is rather dif<sup>fi</sup>cult for an adversary to mount a passive replay attack. In spite of this randomness, an active adversary may be able to mount an attack only when this randomness is somehow canceled or eliminated when multiple messages are combined. However, we believe that such an opportunity to combine several messages to retrieve secure information or mount replay attacks do not exist in the proposed authentication protocol.

We now verify the correctness of the assumptions with respect to message source as well as the beliefs of the sender and recipient of messages using GNY logic [8]. In GNY logic, the principals are not assumed to be trustworthy and redundancy is always explicitly present in encrypted messages. GNY logic distinguishes between what a principal can possess and what it can believe in. It enables expressing different trust levels and implicit conditions behind protocol steps. GNY logic addresses the following properties: (a) that all entities learn what they should learn, and (b) what the entities learn is indeed true.

We proceed by including the individual messages in the protocol followed by inherent explicit assumptions and then the goals. We then present proofs of these goals using GNY logic. In the following, we use $T _ { A } , T _ { P } ,$ and V respectively to represent active tag, passive tag, and veri<sup>fi</sup>er (Fig. 7).

Protocol messages:

M1: $T _ { A } \triangleleft \star ( r _ { V } )$

$$
\mathrm{M} 2: V \triangleleft \star (r _ {A}), \star \left(f _ {k _ {P}} (r _ {A}, I D _ {P})\right), \star \left(f _ {k _ {A}} (r _ {V})\right)
$$

M3: $T _ { P } \triangleleft \star ( r _ { A } ) , \star \big ( f _ { k _ { P } } ( r _ { A } , I D _ { P } ) \big )$

$$
\mathrm{M} 4: V \triangleleft \star (r _ {P}), \star \big (f _ {k _ {P}} (r _ {A}, r _ {P}, I D _ {P}) \big)
$$

Assumptions:

A1: $V \ni r _ { V }$

A2: $T _ { A } \ni r _ { A }$

A3: $T _ { P } \ni r _ { P }$

$$
T _ {A} | \equiv T _ {A} \xrightarrow {k _ {P} , k _ {A} , I D _ {P}} V
$$

$$
\text { A5: } V | \equiv V \xrightarrow {k _ {P} , I D _ {P}} T _ {P}
$$

$$
\text { A6: } T _ {P} | \equiv T _ {P} \xleftarrow {k _ {P} , I D _ {P}} V
$$

A7: $V | \equiv \# r _ { V }$

A8: $T _ { A } \ln \equiv \# r _ { A }$

A9: $T _ { P } | \equiv \# r _ { P }$

Goals of the correctness proof: the primary goals of the proposed protocol are belief $( | \equiv )$ , and the freshness (#), of the messages between each pairs of $V , T _ { P } , T _ { A } .$ Belief ensures that the message is from a trusted source. Freshness ensures that the message was not sent earlier during the same session.

$$
T _ {A} | \equiv V | \sim \# r _ {V}
$$

G2: $V | \equiv T _ { A } | \sim \# r _ { A }$

G3: $V | \equiv T _ { A } | { \sim } f _ { k _ { P } } ( r _ { A } , I D _ { P } )$

G4: $V | \equiv T _ { A } | { \sim } f _ { k _ { A } } ( r _ { V } )$

G5: $T _ { P } | \equiv V | \sim \# r _ { A }$

G6: $T _ { P } | \equiv V | { \sim } f _ { k _ { P } } ( r _ { A } , I D _ { P } )$

G7: $V | \equiv T _ { P } | \sim \# r _ { P }$

$$
\mathrm{G8:} V | \equiv T _ {P} | \sim f _ {k _ {P}} (r _ {A}, r _ {P}, I D _ {P})
$$

Proof:

The logical postulate numbers (e.g., M1, T1,..) referred to in the following are from [8]

<table><tr><td>[D1:]  $T_A \triangleleft r_V$ </td><td>/* M1,T1 */</td></tr><tr><td>[D2:]  $T_A \ni r_V$ </td><td>/* D1,P1 */</td></tr><tr><td>[D3:]  $T_A \mid \equiv \# r_V$ </td><td>/* D2,F10 */</td></tr><tr><td>[D4:]  $T_A \mid \equiv V \mid \sim \# r_V$ </td><td>/* D3,I1 */</td></tr><tr><td>[D5:]  $V \triangleleft r_A, f_{k_p}(r_A, ID_P), f_{k_A}(r_V)$ </td><td>/* M2, T1 */</td></tr><tr><td>[D6:]  $V r_A, f_{k_p}(r_A, ID_P), f_{k_A}(r_V)$ </td><td>/* D5, P1 */</td></tr><tr><td>[D7:]  $V \mid \equiv r_A, f_{k_p}(r_A, ID_P), f_{k_A}(r_V)$ </td><td>/* D6, F10 */</td></tr><tr><td>[D8:]  $V \mid \equiv T_A \mid \sim \# r_A$ </td><td>/* A4, D7, I1 */</td></tr><tr><td>[D9:]  $V \mid \equiv T_A \mid \sim f_{k_p}(r_A, ID_P)$ </td><td>/* A4, D7, I1, P2 */</td></tr><tr><td>[D10:]  $V \mid \equiv T_A \mid \sim f_{k_A}(r_V)$ </td><td>/* A4, D7, I1, P2 */</td></tr><tr><td>[D11:]  $T_P \triangleleft r_A, f_{k_p}(r_A, ID_P)$ </td><td>/* M3, T1 */</td></tr><tr><td>[D12:]  $T_P r_A, f_{k_p}(r_A, ID_P)$ </td><td>/* D11, P1 */</td></tr><tr><td>[D13:]  $T_P \mid \equiv r_A, f_{k_p}(r_A, ID_P)$ </td><td>/* D12, F10 */</td></tr><tr><td>[D14:]  $T_P \mid \equiv V \mid \sim \# r_A$ </td><td>/* A5, D13, I1 */</td></tr><tr><td>[D15:]  $T_P \mid \equiv V \mid \sim f_{k_p}(r_A, ID_P)$ </td><td>/* A5, D13, I1, P2 */</td></tr><tr><td>[D16:]  $V \triangleleft r_P, f_{k_p}(r_A, r_P, ID_P)$ </td><td>/* M4, T1 */</td></tr><tr><td>[D17:]  $V r_P, f_{k_p}(r_A, r_P, ID_P)$ </td><td>/* D16, P1 */</td></tr><tr><td>[D18:]  $V \mid \equiv r_P, f_{k_p}(r_A, r_P, ID_P)$ </td><td>/* D17, F10 */</td></tr><tr><td>[D19:]  $V \mid \equiv T_P \mid \sim \# r_P$ </td><td>/* A6, D18, I1 */</td></tr><tr><td>[D20:]  $V \mid \equiv T_P \mid \sim f_{k_p}(r_A, r_P, ID_P)$ </td><td>/* A6, D18, I1, P2 */</td></tr></table>

The proof of goals 1–8 are shown by the veri<sup>fi</sup>cation steps D4, D8, D9, D10, D14, D15, D19, and D20 respectively.

## 4. Discussion

Shrinkage, in both its intentional and unintentional form, is bound to remain in retail store settings as long as it carries positive incentives for the perpetrators and insuf<sup>fi</sup>cient motivation or the lack of means for the store management to see its complete elimination. In reality, it is a mix of both of these that facilitates the continued occurrence of shrinkage. In a majority of shrinkage scenarios including stealth (by both internal and external parties), misplacement, among others, only one item is affected — the item that is either misplaced or lost for whatever reason. In these cases, there is a mismatch between the actual inventory on the store shelf and that in the store's information system for this item class. However, in the case of shrinkage caused by ticket-switching, a minimum of two items are affected and there is a mismatch of the actual and the information system-based inventory for both these items. The interesting dynamic here is that, compared to the inventory level indicated by the store's information system, the actual inventory is more for the ‘cheap’ item and less for the ‘expensive’ item. In pure monetary terms based on the purchase cost and sale price of these items, from the store's perspective, ticket-switching is not as bad as outright theft of an item since the customer pays for the ‘cheap’ item. The damage occurs primarily in inventory management since the actual inventory now has more ‘cheap’ and fewer ‘expensive’ items vs. what is stored in the store's information system. This discrepancy could lead to unnecessary inventory cost and possible ‘staleness’ of the ‘cheap’ item and lost sales due to stock-outs of the ‘expensive’ item. Given that the effect of ticket-switching is different for the two items affected by ticket-switching from an inventory management perspective, it is easy to mistake one ticket-switching incident for two independent incidents whereby there's a missing item and a mysteriously appearing item. The mysterious appearance of the (cheap) item can be misconstrued as one that was previously misplaced in the store. It is, therefore, not surprising that there is a lack of published statistics on ticket-switching incidents.

During the past few decades, various forms of EAS have been used to prevent or reduce incidents of shrinkage in retail stores. Since these technologies are used primarily to target individuals from outside the store, they are not as effective in dealing with shrinkage caused by store personnel. We propose the use of item-level RFID tags to address shrinkage from both these sources. Given that item-level RFID tags can be read continually while the item is inside the store, it is relatively easy to locate the item within the store as well as to identify any exceptions as they occur.

RFID tags are increasingly being used in supply chains to improve their effectiveness. Currently, a majority of RFID implementations in retail supply chains are at the pallet-level. However, there is a trend (e.g., American Apparel, Trasluz) toward placing item-level RFID tags in the entire retail store to enable complete real-time visibility of all the items in the store. According to IDTechEx [9], the largest and fastest application of RFID is in retailing, the retail supply chain, and associated industries with about 100 organizations currently tagging apparel that are undergoing trials or roll-out. They estimate the demand for RFID tags to be more than 500 million units per year. Frost and Sullivan [6] estimate that the RFID market in apparel supply chain could reach \$1478 million in 2017 (up from \$421 million in 2010).

We considered ticket-switching, a form of shrinkage, at an apparel retail store in the presence of item-level RFID tags. It should be noted that the protocols and the general ideas presented in this paper are applicable to any retail setting where EAS (vs. ink tags in this study) is used. Our choice of item-level RFID tags is due to their well-known advantages such as batch readability, local storage of detailed itemlevel information, among others, as well as the relative dif<sup>fi</sup>culty of tampering with these tags when they are embedded in the tagged object. We proposed a suite of authentication protocols for the considered scenario and veri<sup>fi</sup>ed that they are secure through GNY logic. We did not consider issues related to the cost of item-level RFID adoption and read-rate accuracy since there are excellent papers that have already studied this in greater detail (e.g., [2,7,12,24,25]).

Our goals for this paper are to raise awareness for ticket-switching among researchers and to propose authentication protocols that help prevent or detect ticket-switching incidents in apparel retail stores. To our knowledge, this is the <sup>fi</sup>rst work of its type that attempts to address ticket-switching incidents, which are not that uncommon in retail store settings. Given that item-level RFID tags are increasingly being implemented in retail stores, there is an urgent need to develop authentication protocols that address various forms of shrinkage. This paper is a step in this direction.

Since ticket-switching is new to research literature, to our knowledge, we foresee several possible studies that consider the dynamics associated with this phenomenon. For example, we have explored the effect of ticket-switching on inventory management, and our results from this study are under consideration for publication elsewhere. We hope that awareness to the ticket-switching phenomenon and its uncommon dynamics would generate interest among researchers in the area so we can gain a deeper understanding of shrinkage in general and ticket-switching in particular.

## References

[1] Agence France Press, http://www.intothewine.fr/tags/trelissac-vin 2011.

[2] A.G. de Kok, K.H.v. Donselaar, T.v. Woensel, A break-even analysis of RFID technology for inventory sensitive to shrinkage International Journal of Production Economics 112 (2008)521–531.

[3] R.L. DiLonardo, The economic bene<sup>fi</sup>t of electronic article surveillance, in: R.V. Clarke (Ed.). Situational Crime Prevention: Successful Case Studies, vol. 2. Harrow and Heston, Guilderland, NY, 1997, pp. 122–131.

[4] R.L. DiLonardo, R.V. Clarke, Reducing the rewards of shoplifting: an evaluation of ink tags, Security Journal 7 (1) (1996) 11–14.

[5] D. Dolev, A.C.-C. Yao, On the security of public key protocols, IEEE Transactions on Information Theory 29 (2) (1983) 198–207.

[6] Frost, Sullivan, RFID market in apparel supply chain, May 2012.

[7] G.M. Gaukler, R.W. Seifert, W.H. Hausman, Item-level RFID in the retail supply chain, Production and Operations Management 16 (1) (2007) 65–76.

[8] L. Gong, R. Needham, R. Yahalom, Reasoning about belief in cryptographic protocols, Proceedings of the IEEE Symposium on Security and Privacy, 1990, pp. 234–248. [9] IDTechEx, Apparel RFID 2013–2023, June 2012

[10] G. Kapoor, W. Zhou, S. Piramuthu, Challenges associated with RFID tag implementations in supply chains, European Journal of Information Systems 18 (2009) 526–533.

[11] G. Kapoor, W. Zhou, S. Piramuthu, Multi-tag and multi-owner RFID ownership transfer in supply chains, Decision Support Systems 52 (1) (2011) 258–270.

[12] H. Lee, O. Özer, Unlocking the value of RFID, Production and Operations Management 16 (1) (2007) 40–64.

[13] S. Mauw, S. Piramuthu, A PUF-based authentication protocol to address ticket-switching of RFID-tagged items, Proceedings of the 8th International

Workshop on Security and Trust Management (STM), Springer LNCS 7783, Pisa, 2012, pp. 209–224.

[14] D.C. McFarlane, Y. Shef<sup>fi</sup>, The impact of automatic identi<sup>fi</sup>cation on supply chain operations, International Journal of Logistics Management 14 (2003) 1–17.

[15] D. Papakiriakopoulos, K. Pramatari, G. Doukidis, A decision support system for detecting products missing from the shelf based on heuristic rules, Decision Support Systems 46 (3) (2009) 685–694

[16] S. Piramuthu, Protocols for RFID tag/reader authentication, Decision Support Systems 43 (3) (2007) 897–914.

[17] S. Piramuthu, RFID mutual authentication protocols, Decision Support Systems 50 (2) (2011) 387–393.

[18] Y. Rekik, Inventory inaccuracies in the wholesale supply chain, International Journal of Production Economics 133 (2011) 172–181.

[19] Y. Rekik, E. Sahin, Y. Dallery, Analysis of the impact of the RFID technology on reducing product misplacement errors at retail stores, International Journal of Production Economics 112 (2008) 264–278.

[20] Y. Rekik, E. Sahin, Y. Dallery, Inventory inaccuracy in retail stores due to theft: an analysis of the bene<sup>fi</sup>ts of RFID, International Journal of Production Economics 118 (2009) 189–198.

[21] B. Schneier, Schneier on Security — UPC Switching Scam, http://www.schneier. com/blog/archives/2008/10/upc-switching-s.html 2008.

[22] B. Schneier, Schneier on Security — Bar Code Switching, http://www.schneier. com/blog/archives/2012/05/bar-code-switch.html 2012.

[23] J. Shapland, Preventing retail-sector crimes, in: M. Tonry, D. Farrington (Eds.), Building a Safer Society: Strategic Approaches to Crime Prevention, Crime and Justice, vol. 19, University of Chicago Press, 1995.

[24] Y.-J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2) (2009) 586–593.

[25] S. Whang, Timing of RFID adoption in a supply chain, Management Science 56 (2) (2010) 343–355.

[26] W. Zhou, E.J. Yoon, S. Piramuthu, Simultaneous multi-level RFID tag ownership & transfer in health care environments, Decision Support Systems 54 (1) (2012) 98–108.

Wei Zhou is an Associate Professor of Information Systems at ESCP-Europe in Paris and a member of the RFID European Lab in Paris. He received his Ph.D. in Information Systems from the University of Florida. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in Decision Support Systems, European Journal of Information Systems, European Journal of Operational Research, IEEE Transactions on Geosciences and Remote Sensing, International Journal of Electronic Commerce, and Optical Engineering.

Selwyn Piramuthu is a Professor of Information Systems at the University of Florida. He is a member of the RFID European Lab in Paris and an Associate Researcher of Information Systems and Technologies at ESCP-Europe (Paris). His research interests include RFID systems, pattern recognition and its application in supply chain management, computeraided manufacturing, and <sup>fi</sup>nancial credit-risk analysis.
