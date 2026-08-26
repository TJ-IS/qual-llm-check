---
otero_id: 7604
otero_key: "MDFMJGVZ"
title: "A novel means to address RFID tag/item separation in supply chains"
authors: "Yu-Ju Tu; Wei Zhou; Selwyn Piramuthu"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.09.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel means to address RFID tag/item separation in supply chains Yu-Ju Tu<sup>a</sup>, Wei Zhou<sup>b,c</sup>, Selwyn Piramuthu d,⁎

![](/api/attachments/MDFMJGVZ/fulltext/images/1810b0d84cee18811e94b4b3c2df7da5bfa192d0ca9bc6bd68302bf453ca11d3.jpg)

<sup>a</sup> Management Information Systems, National Chengchi University, Taipei, Taiwan

<sup>b</sup> Information & Operations Management, ESCP Europe, Paris, France

<sup>c</sup> MSc Big Data & Business Analytics, ESCP Europe, Paris, France

<sup>d</sup> Information Systems and Operations Management, University of Florida, USA

## A R T I C L E I N F O

Keywords: RFID Tag separation Knowledge-based system Cryptography Mutual authentication

## A B S T R A C T

Automated identi<sup>fi</sup>ers such as barcodes and RFID (Radio-Frequency IDenti<sup>fi</sup>cation) tags help with the quick identi<sup>fi</sup>cation of their associated items. When such an identi<sup>fi</sup>er is associated with an item, it is generally assumed that these two entities (the identi<sup>fi</sup>er and the tagged item) remain inseparable as long as is necessary. However, unintentional or (dishonest party initiated) intentional tag separation may occur, which necessitates an appropriate response before damage is done. We develop a knowledge-based means with cryptography to identify RFID tag damage and/or separation from its associated object. We also consider related security/privacy aspects of the proposed method.

## 1. Introduction

Identi<sup>fi</sup>ers play a signi<sup>fi</sup>cant role in today's automated retail en vironment. From a supply chain perspective, auto-ID (barcode, RFID tag) technology has been used to support logistics services as well as instore retail operations since such automated identi<sup>fi</sup>cation supports fast and accurate service along with the reduction of lead time and opera tional and transaction costs. The most commonly used identi<sup>fi</sup>er in current retail setting is the barcode. It is hard to imagine a retail setting without barcodes since they facilitate a multitude of applications in retail supply chains that include inventory management and customer checkout

Barcodes have been the auto-ID technology of choice in retail applications for more than four decades. While barcodes can be used for instance-level unique identi<sup>fi</sup>cation of items, they are commonly used for class-level identi<sup>fi</sup>cation (e.g., any 1 L bottle of brand X water). Although this has su<sup>fi</sup>ced so far in a majority of retail applications, the trend is shifting with the popularity of sensors, block-chain, and other technologies that are being introduced in the retail supply chain. Barcodes have several drawbacks such as sequential (i.e., slow) read, line-of-sight requirement for readability, inability to have a two-way conversation with a reader, and the di<sup>fi</sup>culty in attaching an associated sensor. Moreover, with the increasing move toward remaining shelf-life for perishables [12], RFID (Radio-Frequency Identi<sup>fi</sup>cation) tags are slowly replacing barcodes in a wide variety of retail applications at the pallet-level, if not at the item-level (e.g., American Apparel, Trasluz). In addition to their capability to store and process data, RFID tags can also have a two-way conversation with a reader. This is critical when authentication of the item is involved. Unlike barcodes, RFID tags readily allow for item-level identi<sup>fi</sup>cation due to their unique identi<sup>fi</sup>ers, and this property facilitates means to track and trace products in a supply chain [4,6]. While barcodes are cheaper to print vs. unit RFID tag cost, both barcode and RFID tag implementations incur back-end systems and reader cost. When all costs and bene<sup>fi</sup>ts are considered, RFID tags come out ahead especially given their ability for two-way conversation, ease of associating sensors, batch read speed, no line-of-sight require ment, local storage and processing capability, copy/switch di<sup>fi</sup>culty, among others [25].

RFID o<sup>f</sup>ers an e<sup>fi</sup>cient and e<sup>f</sup>ective means to automatically identify objects. Since a goal of IoT (Internet of Things), which comprises RFID tags, is to connect the physical and virtual worlds by “sensing” di<sup>f</sup>erent “things” of interest, RFID-based information systems are often considered to be best candidates for IoT-based implementations. This is thanks in part to passive RFID tags that are generally very a<sup>f</sup>ordable and function without an external cable or battery as a required source for power, and can be e<sup>f</sup>ortlessly deployed to track and trace a large number of objects in a relatively fast and reliable manner.

In today's world, while RFID has been extensively and successfully used in various areas such as wireless token, inventory management, asset protection, and Industrial Internet, all of these RFID applications rely on the premise that the target item is tagged as it should be. As long as the communication between RFID reader and tag is secured and uninterrupted, the underlying assumption is that the tagged item wil always be identi<sup>fi</sup>able and traceable. In other words, a strict and ne cessary requirement is that the RFID tag and the tagged item to be identi<sup>fi</sup>ed and traced are constantly bound together. If this condition is not sustainable, almost all contemporary RFID-based information systems will malfunction. However, recent studies have shown that, under many circumstances, RFID tags could be either accidentally or un expectedly separated from the items to which they are supposedly attached [40]. Consequently, a series of problems may thus arise. For example, when a tag is separated (detached) from a tagged item, the association between that tag and that tagged item disappears. The tagged item's information that is stored in the tag becomes useless. The lost identity problem results from auto-ID technology use $( \boldsymbol { \mathrm { e . g . } }$ , barcode, RFID tag) as the item's identi<sup>fi</sup>er. For example, when the tag of a transportation pass card is lost, the card has no use since the tag re presents the identity of the card holder. Relatedly, when an apparel tag is lost, the associated information such as the apparel's normal price and discount information go missing as well. More serious is the faked identity problem, since the separated tag could be easily tampered to impersonate other identities. For example, if the tag of a transportation pass card is pulled out and used to replace the one in another normal transportation pass card, true transportation records with false card holder's identi<sup>fi</sup>cation may thus be forged. In other words, the tag/item separation problem could be addressed with minimal damage to the identi<sup>fi</sup>ed object and with continued trust [15] and reputation [16] for such auto-id technology if there is a general means to immediately detect the tag's separation. From the item-tag combination's perspec tive, when tag separation occurs, the item loses its identi<sup>fi</sup>cation in formation regardless of how or why the separation event occurred. We therefore do not distinguish among the speci<sup>fi</sup>c tag separation causes or processes such as the e<sup>f</sup>ect of temperature on the tag's adhesion to its associated item and accidental tag peeling on contact by an external object. Our focus is only on the tag separation event (yes or no) - ‘how and ‘why’ of tag separation are beyond the scope of this study.

In the retailing context, an item with a damaged or separated bar code necessitates manual identi<sup>fi</sup>cation of its stock keeping unit (SKU) and/or universal product code (UPC) as well as other related information that include the item's unit price. Such manual look-up necessarily causes avoidable process delays that disrupt automation. While it may be possible to manually retrieve associated SKU and/or UPC for a majority of items, it is certainly not a guarantee. When the identi<sup>fi</sup>cation information cannot be retrieved for whatever reason (e.g., last item of that type in the store), it could lead to loss in sale of that item as well as inventory shrinkage where an item is in stock but due to its missing identity the item is invisible to the (inventory management, checkout) system.

To the best of our knowledge, there is only one published research paper on identi<sup>fi</sup>cation separation in a supply chain context. Zhou and Piramuthu [40] consider identi<sup>fi</sup>cation shrinkage from an inventory management perspective with RFID as the identi<sup>fi</sup>er of interest and ticket-switching as the speci<sup>fi</sup>c issue. Ticket-switching [37–39] is the intentional act of switching identi<sup>fi</sup>ers between two items in a retail setting that allows for the possibility of paying the lower item's price for the higher priced item.

Although there exist a few de facto ways to prevent items from being shoplifted, such as the use of electronic article surveillance (EAS) system or ink tag, these means are either unable to detect the unexpected identi<sup>fi</sup>er (e.g., ink tag) separation immediately or limited to only very speci<sup>fi</sup>c separation cases. The primary motivation of this study is to <sup>fi</sup>nd a general solution for addressing the tag/item separation problem. The few existing solutions to the tag separation issue are very application-speci<sup>fi</sup>c which preclude their use in the general context. For example, NASA recently proposed a solution by using a passive RFID tag to detect tag/item separation [19]. However, NASA's approach is mainly designed for detecting whether a given bolt is torqued properly. Moreover, it needs an additional device that can mechanically operate on the tagged item and thus may not be universally suitable for general RFID-tagged items such as apparel or package. Such a solution does not address the issue that is critical to any RFID-based information system that includes security management. These facts re<sup>fl</sup>ect the pressing need and timeliness of this study. Based on our experience addressing related RFID-based issues, we propose the use of ambient conditions and intelligent learning for addressing the tag/item separation problem.

The contributions of this study are three-fold. This is the <sup>fi</sup>rst research study that systematically investigates the problem of RFID tag separation. It is an ongoing trend that many <sup>fi</sup>rms are preparing themselves for making decisions based on the item-level information and the overall value of such information may amount to billions of US dollars [9,11]. However, such a trend and the associated value can hardly be sustained if items are mistakenly identi<sup>fi</sup>ed or tracked due to unexpected separation. This study highlights the importance of constantly watching the state of RFID tag attachment. Second, this study is the <sup>fi</sup>rst to provide a solution to detect RFID tag separation. More importantly, this signi<sup>fi</sup>es that this study is complementary to the entire set of existing literature on RFID identi<sup>fi</sup>cation and tracking since such studies are reliable and valid only when the inseparability of RFID tag and the tagged item is guaranteed. Third, while this study is not the <sup>fi</sup>rst to propose lightweight RFID authentication means, it is the <sup>fi</sup>rst to consider the use of ambient condition to achieve both mutual authen tication and tag separation detection. Moreover, the method proposed in this study is not designed for a very speci<sup>fi</sup>c context such as a customized RFID tag with a rewired antenna, etc. Rather, it is very general because it is based completely on information with no reliance on mechanical means. For instance, the proposed method can be easily applied to any passive RFID tag that follows ISO EPC C1G2 standard.

The remainder of this paper is organized as follows: Since there is really no published research literature that addresses the RFID tag separation issue in a supply chain context [5,14] other than Zhou and Piramuthu [40], we brie<sup>fl</sup>y review this paper along with a few other tangentially related papers and also consider the current state-of-the-art to handle RFID tag separations in Section 2. We consider a few di<sup>f</sup>erent means to address the tag separation issue and discuss these in Section 3. We follow this with a brief discussion on the potential use of sensors in these applications and then present the proposed associated cryptographic protocol in Section 4. We also include security analysis of the proposed protocol. We provide experimental results using the considered frameworks and also discuss performance results using the di<sup>f</sup>erent frameworks in Section 5. We then conclude the paper with a brief discussion in Section 6.

## 2. Literature review and current state-of-the-art

Unexpected RFID tag separation can be a devastating threat in all current RFID-based information systems. Tag separation often denotes the loss of item information and thus in turn incurs additional labor and other (e.g., computational, customer goodwill) costs for recovery only if the tag separation is detected. Moreover, the additional cost could be very hard to tolerate, considering the thin margins in some (e.g., retailing) applications. More seriously, tag separation often signi<sup>fi</sup>es the loss of item control when the tag separation incident goes undetected. Nowadays, some retailers use RFID tags as their items' identi<sup>fi</sup>ers to automatically (e.g., inventory) manage these items. However, when a tag is separated from its tagged item either intentionally or accidentally, its identi<sup>fi</sup>cation information is lost and thus the item would be out of control. For instance, a culprit was caught at a Target store for removing the price tag from a cheap item which was then switched with that from an expensive item in order to pay less for more [18]. In another incident, a student was caught using the tag that is originally meant for a very cheap gadget for checking out with an iPod that costs more [42]. Similarly, several people were caught at a Walmart store fo switching the price tags on many valuable items and returning the items without the tags to the store for refund [27]. There have been several such reported ticket-switching incidents [2,29], although we suspect that a large number of ticket-switching incidents go unnoticed by store system or personnel. Moreover, when the amount involved is small or when it's an isolated case, such incidents often are not reported or do not receive extensive publicity.

While ticket-switching involves intentional (RFID or barcode) tag separation, it is also possible for such separation/damage to occur unintended. We consider only RFID-based systems with item- or other higher-level RFID-tags in this study with the requirement for two-way communication with the RFID tag. We do not distinguish between intended and unintended RFID tag separation from the corresponding item. Unexpected (intended and unintended) RFID tag separation may cause considerable mismatched item records, causing havoc in stock out and call-o<sup>f</sup> processes, and eventually increasing the information uncertainty and discrepancy across both upstream and downstream supply chains [36].

To address the RFID tag separation problem, two streams of studies seem relevant based on existing published literature. The <sup>fi</sup>rst stream attempts to address tag separation through relevant information use, while the focus of the second stream is on mechanical recon<sup>fi</sup>guration. Although there are no prior studies on the use of ambient condition information for tag separation, there are some tangential ones that use ambient condition sensors for tag authentication purposes. Speci<sup>fi</sup>cally, a set of studies apply di<sup>f</sup>erent ambient conditions to help improve RFID identi<sup>fi</sup>cation and tracking. For example, Ma et al. [17] show that by using sensor-generated information to compare ambient conditions, it is possible to di<sup>f</sup>erentiate RFID tags at di<sup>f</sup>erent physical locations from those at the same physical location. Similarly, Halevi et al. [13] indicate that mobile RFID tags may present di<sup>f</sup>erent motion patterns. In addi tion, several recent studies such as Urien and Piramuthu [34], Piramuthu and Doss [26], and Tu and Piramuthu [30] also rely on ambient conditions to help ensure that RFID tag and reader are truly at the same physical location.

A few other publications address the tangentially related RFID tag separation issue in other domains. These are only tangentially related since the means to address such tag separation scenarios cannot be directly applied to RFID tag separation issues in (retail) supply chains. This stream of prior studies primarily depend on mechanical solutions for checking RFID tag displacement due to possible fatigue crack on bridge concrete, buildings, Turn-Over-Cart (TOC), etc. [7,21]. In gen eral, existing literature suggests that detecting the state change when an RFID tag is being separated is one important key to addressing the tag/ item separation problem. For example, a recent stream of studies attempt to check for architectural displacement, such as the occurrence of fatigue crack on concrete bridges, by measuring the change in RFID signal travel time [7,21]. These studies are based on the assumption that when any architectural displacement takes place, a related strong external force that caused it must exist. Consequently, the same force also transforms the structure of the RFID tag that is attached to the bridge. The result of such a transformation can be observed in the changes with respect to how the RFID tag receives and sends signals.

These studies and their experiments show that when an RFID tag's antenna is forced to be stretched or restructured, it is very likely that the signal travel time between the tag and reader would change, as compared to that for a tag with an undamaged antenna. These studies suggest a way to detect tag separation by measuring the tag's round-trip time (RTT). Another stream of studies is committed to crafting mechanical means to customize an RFID tag for meeting special needs. For instance, NASA recently proposed a solution for detecting whether a bolt is torqued appropriately [19]. This solution is based on the as sumption that when su<sup>fi</sup>cient force is applied to the bolt, a specially designed mechanical assembly would trigger the circuit in the tag that is attached to the bolt. In other words, if the bolt is not torqued appropriately, the tag's signal strength is very likely to decrease. This denotes that the state of tag's separation could also be measured by the tag's received signal strength (RSS). However, the measurement of the di<sup>f</sup>erences between RFID-based signal transmission time or strength are still very challenging in general. For example, any tiny measurement bias will inevitably result in false result due to the speed (of light) at which RFID signals are transmitted. In spite of these unique solutions that have been suggested in extant literature, considerable research gaps remain to be <sup>fi</sup>lled in order to address the item/tag separation problems in a more general manner.

As mentioned in Section 1, we are aware of only one publication that considers identi<sup>fi</sup>cation separation in any form in supply chains. Ticket-switching is the primary issue that is addressed in this [40] paper. Speci<sup>fi</sup>cally, the authors consider inventory management in the presence of ticket-switching events. The main contribution of this paper is in the extension of the classical EOQ (Economic Order Quantity) model with the incorporation of dynamics that are associated with ticket-switching incidences. The authors consider inventory shrinkage and its e<sup>f</sup>ect on optimal order quantity, holding cost, ordering cost, total inventory cost, and lead time with or without back-order. They then incorporate the e<sup>f</sup>ects of ticket-switching as a speci<sup>fi</sup>c case of inventory shrinkage and analyze its dynamics. Among the various insights that they uncover through their analysis, they <sup>fi</sup>nd that in the presence of ticket-switching incidents, the inventory manager must pay more attention to relatively ‘cheap’ items to reduce loss. Although the <sup>fi</sup>rst to bring awareness to identi<sup>fi</sup>cation shrinkage in the research lit erature, Zhou and Piramuthu's paper did not propose a solution to address identi<sup>fi</sup>cation shrinkage, which is essentially brought on by tag separation. This remains an open issue that we attempt to address in this paper.

Almost all prior solutions were concentrated on designing a very application-speci<sup>fi</sup>c, hard-wired means, precluding their further use in di<sup>f</sup>erent scenarios. For example, some studies detect either the displacement state change or the torque state change on the tagged item simply by mechanically rewiring the tag. In other words, even if their solutions could be extended to detect item/tag separation, these solu tions function only when a strong external force that is su<sup>fi</sup>cient enough to in<sup>fl</sup>uence the tag's normal operation is applied. Moreover, these prior solutions require additional hardware device that are connected to the tag and the item, such as a circuit conductor in NASA's solution for sensing fastener failure. As a result, these additional pre-conditions and requirements render it di<sup>fi</sup>cult to apply these prior solutions for detecting tag separation from many di<sup>f</sup>erent items.

Existing studies also ignore the use of contextual changes in the ambient environment to help detect tag separation. During the past decade, advances in technology have made it economically feasible to embed a tiny and fully functional sensor inside a regular RFID tag. Recently, several sensor-based solutions have been proposed for mitigating the security concerns related to RFID applications. Among these solutions, the targets are primarily aimed at physical proximity checking. This proximity speci<sup>fi</sup>cally pertains to the distance between the tagged item and reader. In general, identi<sup>fi</sup>cation and authentication of the tagged item can only be permitted when the item is in close physical proximity to the reader. Otherwise, many security concerns such as those related to relay attack may arise. To address issues related to relay attacks in RFID tag authentication, comparison between readings of the item's surface temperature from reader's side and the readings from the tags sides has been proposed for checking the tagged item's proximity to the reader [34]. In the same vein, the reader's de tection of geomagnetic <sup>fi</sup>eld and the tag's detection of geomagnetic <sup>fi</sup>eld can be compared with each other for checking tag-reader physical proximity [30]. Overall, although these recent solutions are aimed at addressing relay attacks, their <sup>fi</sup>ndings suggest that considerable contextual changes can be easily traced and monitored for improving the security of RFID applications. More importantly, these changes can be sensed by very a<sup>f</sup>ordable, compact-sized RFID tag without the need for an internal battery power source. The sensor tags adopted by these recent solutions are all passive RFID tags that comply with the EPC C1G2 standard.

![](/api/attachments/MDFMJGVZ/fulltext/images/a3074b30b58e70a7f7a9d799f719a013c70921debc2588515f4da91e09926381.jpg)  
Fig. 1. Associated tags.

To summarize, RFID tag separation is a serious issue that needs to be addressed for RFID-based systems to perform as expected. Existing studies assume that the tag remains with the (tagged) item until tag separation is intentionally initiated by a process. Existing studies are therefore only tangentially related to our study. For example, several studies use ambient conditions to determine the presence of a tagged item with the implicit assumption that an RFID tag remains attached to its (tagged) item. A few other studies use mechanical means to ensure that an RFID tag is indeed properly a<sup>fi</sup>xed to an item. We explicitly consider the scenario where an RFID tag is separated from its associated item.

## 3. The proposed solution

Tag separation can possibly be addressed through several means. We consider a few such scenarios in this section.

## 3.1. Associated tags

One such is illustrated in Fig. 1. The idea here is to determine the presence of the object of interest with the con<sup>fi</sup>rmed presence of a related object [31]. An example scenario is a case of item-level tagged items that are known to be together. In such a context, if one of the tagged item is known to be present with certainty, a tagged item in that case that is not reachable (i.e., readable tag) or with a separated tag that is no longer in that case can also be con<sup>fi</sup>rmed to be physically present in that case. An issue with this method is that the identi<sup>fi</sup>cation of tag separation is di<sup>fi</sup>cult since it simply assumes that the tag is either se parated and the object and tag are outside of the case or the attached/ separated tag is in the case but is temporarily unreachable. Since this method requires the simultaneous presence of multiple items in the reader's <sup>fi</sup>eld, an item by itself cannot be located using this process.

This method works perfectly to con<sup>fi</sup>rm the presence of items that are temporarily or permanently unreachable through radio-frequency means but are known to be present with another item that is radiofrequency reachable and is also in the <sup>fi</sup>eld of the reader. However, it cannot speci<sup>fi</sup>cally detect tag separation.

## 3.2. Direct

A di<sup>f</sup>erent approach is to somehow sense tag separation through some other means such as the use of an appropriate (e.g., ambient condition) sensor and to con<sup>fi</sup>rm tag separation as it occurs (Fig. 2). In this method, when tag separation is sensed, it is veri<sup>fi</sup>ed through a cryptography-based authentication protocol [24] that uses and then the system determines if this (tag separation) event did indeed occur based on the success or failure of the protocol.

This method directly checks for tag separation and is more reliable for veri<sup>fi</sup>cation of tag separation vs. the previous method which only checks for the item's presence in the presence of a related item but does not really check for tag separation in any form.

## 3.3. Cross verification

A better alternative to just detecting tag separation alone would be to somehow sense tag separation through other means (e.g., cryptography, sensors) and to validate the tag separation event with another related item that is in close physical proximity to the item of interest (Fig. 3). In this scenario, veri<sup>fi</sup>cation is done through two factors - sensor + cryptography and presence of related tagged item in close physical proximity.

An issue with this method is that when the tag is separated from the item and the tag is where it is supposed to be, the separated item could be long gone. In this scenario, the physical proximity check would turn out to be OK since it is done through communication with the (now separated) RFID tag alone. However, under this scenario, if a false negative for tag separation occurs in the cryptography + sensor check for whatever reason, tag separation will not be identi<sup>fi</sup>ed in this set-up. Therefore, the system should check to ensure that the tag is indeed attached to the item when a positive tag separation signal is generated since the signal could be false positive.

## 3.4. Knowledge-based system

To reduce the possibility of false positives or false negatives further, an even better alternative is to complement the above with a knowledge-based system with learning capability (Fig. 4).

In the intelligent knowledge-based system framework, the cryptography + sensor setup is incorporated along with the identi<sup>fi</sup>cation of the existence of a related item when possible and a knowledge-based system that learns from experience. We leave the exact learning mechanism open since it can involve an appropriate learning algorithm (e.g., decision tree, neural network, genetic algorithm) of interest. What is signi<sup>fi</sup>cant is the intelligent aspect, which is essentially the ability of this knowledge-based system to incrementally improve its performance over time. The knowledgebase is <sup>fi</sup>rst created with knowledge of results from cryptography + sensor setup, the associated tag setup, and the cross veri<sup>fi</sup>cation setup. We used simulations from these three setups to generate training data for the learning mechanism in the knowledgebased system. The knowledgebase essentially comprises all knowledge learned through this process. Clearly, the initial knowledgebase thus generated is bound to be incomplete. The system learns as it processes more examples. The measurement and evaluation modules in the framework respectively help determine the performance of the system (e.g., through classi<sup>fi</sup>cation accuracy measurements under heretofore unseen situations) and identify knowledge de<sup>fi</sup>cits, which are then addressed through appropriate training examples to the learning module. With time, the knowledgebase is incrementally updated to re<sup>fl</sup>ect various dynamics that are present in this system setup.

## 4. Ambient condition sensor and the proposed authentication protocol

We <sup>fi</sup>rst brie<sup>fl</sup>y discuss possible ambient condition sensors that could be used for this purpose. We then propose and discuss the authentication protocol for tag separation determination.

## 4.1. Ambient condition sensors

The last decade has witnessed the development of novel RFID tags with embedded sensors that do not require an internal power source (e.g., WISP tags [22]). With increasing demand for various types of RFID-associated sensors, several di<sup>f</sup>erent types of sensors that measure various ambient and other conditions have been introduced in the market over the years. Some of these include [10]:

Fig. 2. Direct method to detect tag separation.  
![](/api/attachments/MDFMJGVZ/fulltext/images/31c3a8ddb66847f86051c11e1ccb4c8dd0b742d2381aed245181bae29aef7583.jpg)  
Fig. 3. Associated tags + direct method to detect tag separation.

Tag with strain sensing capability: these tags provide such reading at an accuracy of ± 0.5 kgf per compression load cell.

Tag with radio-frequency (RF)-<sup>fi</sup>eld sensing capability: these tags can harvest energy from nearby RF <sup>fi</sup>eld and then re<sup>fl</sup>ect the strength of the <sup>fi</sup>eld by lighting up LED(s).

• Tag with light sensing capability: these tags provide such readings at di<sup>f</sup>erent levels of brightness.

Tag with temperature and pressure sensing capability: these sensor tags can provide such readings at an accuracy of ± 2°C in tem perature and ± 0.1 mbar in pressure.

• Tag with temperature and humidity sensing capability: these tag sensors can provide such readings at an accuracy of ± 4.5% in hu midity and ± 0.5°C in temperature.

Tag with acceleration and orientation sensing capability: these tag provide 3-axes readings with selectable ranges between ± 2 g and ± 16 g at an accuracy of ± 40 mg.

• Tag with magnetic <sup>fi</sup>eld sensing capability: these tags provide such reading with strength and direction of selectable ranges between ± 4 gauss and ± 16 gauss at an accuracy of ± 146μ gauss.

As can be seen from the list above, most commonly used ambient conditions can be readily measured through RFID-based sensors. It should be noted that some of these sensors have usage constraints/ drawbacks due to the directional property of the ambient or other condition that is being measured. For example, light and sound are directional whereas temperature is not. Therefore, when measuring these directional conditions through sensors, care should be taken to incorporate the directional component into e<sup>f</sup>ect. Whereas most sensors work both indoors and outdoors, some sensors (e.g., Global Positional System (GPS)) do not function at their full capacity indoors, especially inside concrete or steel structures or under wet foliage coverage. Radio-frequency signals also have di<sup>fi</sup>culty in liquid and metallic environments. For detailed discussion on ambient and other sensors for use in RFID-based applications, the reader is referred to [26,30,34].

A few of the available RFID-based sensors and some of their main strengths and weaknesses are listed in Table 1. As can be seen from this list, all of these considered sensors have their own strengths and weaknesses. The choice of sensor(s) therefore depends entirely on the application context of interest.

![](/api/attachments/MDFMJGVZ/fulltext/images/640cf67ca16f695c404a5b07a5a8a458eb84f36fd66239e913447fecdc4896a5.jpg)  
Fig. 4. Intelligent knowledge-based system + cross veri<sup>fi</sup>cation.

Table 1  
Pro<sup>fi</sup>les of a few ambient condition sensors [adapted from [30]].

<table><tr><td>Type</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>GPS</td><td>Convenient</td><td>Pimarily outdoor use; easy to jam, spoof, disable</td></tr><tr><td>Light</td><td>Hard to replicate</td><td>Directional</td></tr><tr><td>Magnetic field</td><td>Not directional</td><td>Variations due to ferromagnetic interference</td></tr><tr><td>Posture</td><td>Ease of use</td><td>Directional; calibration challenges</td></tr><tr><td>Pressure</td><td>Convenient</td><td>Easy to replicate, directional, invariant across short distances</td></tr><tr><td>Sound</td><td>Hard to replicate</td><td>Directional</td></tr><tr><td>Temperature</td><td>Not directional</td><td>Non-line-of-sight measurement challenges</td></tr></table>

As for the reading of ambient condition to be used in the protocol, there are several options such as light sensor, pressure sensor, and motion sensor. For example, a quick way to di<sup>f</sup>erentiate the attached tags from the separated tags is to measure the change in ambient light reception intensity (i.e., luminosity). This is because most RFID tags are directly attached to their tagged items. As a result, these tags have a surface where ambient light is blocked by the items to which they are attached. In other words, once the attached tags are peeled o<sup>f</sup> and separated from the items, their light reception intensity will change as the shadowed areas vary. In addition, for those tags that are enclosed or contained inside some speci<sup>fi</sup>c items, such as tires and gas pipes, their surrounding air pressure will change when such tags are removed outside of the items. Alternatively, the tags that are separated will present very di<sup>f</sup>erent movement patterns from those of attached tags, such as a speci<sup>fi</sup>c variation of motion orientation or acceleration. Overall, the use of these sensor readings are all very suitable and appropriate, and depend on the context in which separation is most likely to occur.

## 4.2. The authentication protocol

In addition to authentication of tag by reader and reader by tag, the primary purpose of the following protocol is in verifying the simultaneous presence of tag and tagged item in close physical proximity of each other. We use ambient conditions to operationalize the authenti cation protocol. The ambient condition experienced by the tag, reader, and the tagged item are bound to be similar if they are at the same physical location. While some of the ambient condition facets such as light and sound have directional properties, others such as temperature and humidity are non-directional. We assume that the tag is physically attached to the tagged item such as a sticker on an object and when the tag is physically removed from the tagged item, it triggers an alert based on change to the ambient condition (e.g., light exposure to the underside of the sticker). We leave open the exact ambient condition used since it is context-speci<sup>fi</sup>c. In that sense, the proposed authenti cation protocol is independent of the type of ambient sensor used.

We use the following notations for the remainder of the paper.

$A _ { T } , A _ { R } ;$ k-bit tagged item's ambient condition states sensed by the tag and reader respectively

$a , b ,$ c: k-bit secrets that are shared by the tag and reader

• ⊕: Exclusive-OR (XOR) operator

$N _ { 1 } { : }$ k-bit random nonce

$R , N _ { 2 } , N _ { 3 i } , N _ { 4 } , M _ { T } , M _ { R } \colon$ k-bit temporary vectors

$r o t ( A , \rho ) \colon$ The function to rotate elements in vector A by ρ places

$w t _ { H } ( A ) \colon$ : The Hamming weight of vector A

$d _ { H } ( A , B ) ;$ : The Hamming distance between vector A and vector B

$\Delta _ { e r r } \mathrm { : }$ The tolerated di<sup>f</sup>erence in sensing the same ambient condition state, i.e., sensor reading o<sup>f</sup>set tolerance level

$A _ { T i = 1 . . ( n ) \ } .$ set of n possible $A _ { T }$ that are generated based on $A _ { R }$ and $\Delta _ { e r r }$

$\nu _ { R _ { 1 } } , \ \nu _ { R _ { 2 } } , \ \nu _ { T } \mathrm { ; }$ k-bit noise vectors generated by a random mix of $\frac { k } { 2 }$ bits = 1 and ${ \frac { k } { 2 } } \mathrm { ~ b i t s } = 0$

Although with time, even the basic RFID tags will have more memory and processing power, we attempt to keep our proposed au thentication protocol lightweight to facilitate its applicability in most realistic real-world scenarios. The authentication protocol only makes use of computationally lightweight exclusive-OR (XOR) and rotation functions. To alleviate issues with leakage of any of the shared secrets, the RFID tag and reader share three secrets $a , b ,$ , and c with the intention that knowledge of any of these secrets by itself will not compromise the authentication protocol by rendering it vulnerable to attacks by an adversary. We do not concern ourselves with the key distribution problem (here, how the shared secrets between reader and tag are known to the both of them) since there are several fairly standard ways to accomplish this task $( \mathtt { e . g . , a }$ trusted third party generates and securely shares these secrets with the reader and tag or the reader generates these secrets and securely shares them with the tags). Since an adversary can block any of the messages and disrupt the authentication protocol from completion, the reader aborts the process if it fails to receive a response from the tag within a pre-determined amount of time. Note that all communication between reader and tag occur through the wireless medium.

The proposed protocol (Fig. 5) begins with the reader measuring its ambient condition $\left( A _ { R } \right)$ . The reader then generates a nonce $\left( N _ { 1 } \right)$ and a noise vector $\left( \nu _ { R _ { 1 } } \right)$ with exactly half the bits as 1 s and the other half as 0 s.The reader then generates $R ,$ which is sent to the tag. In response, the tag detects its ambient condition $\left( A _ { T } \right)$ and also generates its noise vector $( \nu _ { T } ) ,$ , which it uses to generate $N _ { 2 } .$ It then generates $M _ { T } ,$ which is sent to the reader. Since the ambient condition measurement at the reader and tag ends could involve some error in spite of careful calibrations, we check for this at the least signi<sup>fi</sup>cant bits of the reader and tag sensor readings $( \Delta _ { e r r } ) .$ . We compute several $( n ,$ , which is contextspeci<sup>fi</sup>c) $A _ { T _ { i } }$ values at the reader side since the tag is computational resource-constrained. If the measured sensor values do not fall within a predetermined tolerance range, the protocol execution is aborted. Otherwise, the protocol proceeds with the generation of another noise vector by the reader $( \nu _ { R _ { 2 } } ) .$ . By now, the reader has authenticated the tag. However, the tag has not yet authenticated the reader. To this end, the reader then generates $M _ { R } ,$ which is sent to the tag. The tag generates $N _ { 4 }$ that should match exactly half the bits of $M _ { R } .$ If not, the protocol is aborted. The purpose of the noise vectors is to render it di<sup>fi</sup>cult for an adversary to decrypt $R , M _ { T } ,$ and $M _ { R }$

## 4.3. Security analysis

We believe that the mutual authentication protocol that is proposed in this paper includes several characteristics that help ensure its security properties. We include freshly-generated nonce $\left( N _ { 1 } \right)$ and the three noise vectors $( \nu _ { R _ { 1 } } , \nu _ { R _ { 2 } } , \nu _ { T } )$ during every run of the protocol which incorporates a certain degree of randomness in the messages that are communicated between tag and reader. Moreover, knowledge of any one of the shared secrets $( a , b , c )$ does not expose the protocol to any vulnerability. However, with the knowledge of both a and $^ { b , }$ an adversary can successfully impersonate the tag to the reader. Regardless, it is rather di<sup>fi</sup>cult even for an active adversary to retrieve these secrets based only on the over-the-air messages $( R , M _ { T } , M _ { R } )$ that are passed between tag and reader.

We now consider a few speci<sup>fi</sup>c attacks that could be launched by active or passive adversaries on such RFID-based authentication protocols.

## 4.3.1. Tag/reader anonymity

Care is taken in the authentication protocol to protect the shared secret keys $a , b , c ,$ since these together comprise the identi<sup>fi</sup>cation information for the tag. Knowledge of all three shared secrets is necessary to impersonate the reader to tag and only two $( a , b )$ are necessary to impersonate the tag to reader. Moreover, with knowledge of these secrets, an adversary can easily track or trace the tag or a mobile reader. Knowledge of shared secrets a and b together allows for the possibility of cloning the tag.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Reader
1) detect  $A_{R}$ 
2) generate  $N_{1}, \nu_{R_{1}}$ 
3)  $R \leftarrow a \oplus A_{R} \oplus N_{1} \oplus \nu_{R_{1}}$ 

4) Hello, R

5) detect  $A_{T}$ 
6) generate  $\nu_{T}$ 
7)  $N_{2} \leftarrow a \oplus A_{T} \oplus R$ 
8)  $M_{T} \leftarrow N_{2} \oplus rot(b \oplus A_{T}, wt_{H}(A_{T} \oplus N_{2})) \oplus \nu_{T}$ 

9)  $M_{T} \xleftarrow{\leftarrow}$ 

10) abort if delayed response from tag
11)  $A_{Ti=1..(n)} \leftarrow A_{R} \pm \Delta_{err}$ 
12) Repeat for each i (i = i..n)
12a)  $N_{3i} \leftarrow \nu_{R_{1}} \oplus N_{1} \oplus rot(b \oplus A_{Ti}, wt_{H}(A_{Ti} \oplus N_{1} \oplus \nu_{R_{1}}))$ 
12b) if  $d_{H}(N_{3i}, M_{T}) = \frac{k}{2}$ , go to (14)
13) abort
14) generate  $\nu_{R_{2}}$ 
15)  $M_{R} \leftarrow c \oplus rot(b \oplus A_{Ti}, wt_{H}(A_{Ti} \oplus N_{1} \oplus \nu_{R_{1}})) \oplus \nu_{R_{2}}$ 

16)  $M_{R} \xrightarrow{\rightarrow}$ 

17)  $N_{4} \leftarrow c \oplus rot(b \oplus A_{T}, wt_{H}(A_{T} \oplus N_{2}))$ 
18) verify, if  $d_{H}(N_{4}, M_{R}) = \frac{k}{2}$ , else abort
</div>

Fig. 5. The proposed authentication protocol.

## 4.3.2. Forward security

Even if all the shared secrets (a, b, c) are somehow known to an adversary, these secrets cannot be used to decrypt all earlier messages since other elements such as the ambient conditions $( A _ { R } , A _ { T } )$ and the three noise vectors $( \nu _ { R _ { 1 } } , \nu _ { R _ { 2 } } , \nu _ { T } )$ are still unknown to the adversary and these cannot be generated from knowledge of the shared secrets.

## 4.3.3. Tag/reader location privacy

Since the messages that are passed between tag and reader are seemingly random between any two authentication rounds, it is di<sup>fi</sup>- cult for an adversary to use any of the messages to track the tag and/or the (mobile) reader. It is also di<sup>fi</sup>cult for an active adversary to modify previous messages in order to successfully complete an authentication round.

## 4.3.4. Secrecy/data integrity and authenticity

The integrity of the messages passed between tag and reader is ensured by not sending anything that could compromise the security of the protocol in clear text. For example, no identi<sup>fi</sup>cation information is sent in clear text. Even though the protocol is lightweight, it is designed to be secure and to maintain its secrets regardless of active or passive attacks from adversaries.

## 4.3.5. DoS/desynchronization

Denial of Service (DoS) attacks in RFID-based protocols generally occur when a message is blocked by an adversary or a modi<sup>fi</sup>ed message is not accepted by a recipient $( \mathrm { i . e . }$ , reader or tag). In the proposed protocol, three messages are sent in the open $( R , M _ { T } , M _ { R } )$ . When an adversary blocks either R or $M _ { T } ,$ it e<sup>f</sup>ectively aborts the authentication process since the reader aborts after waiting for a response within a prespeci<sup>fi</sup>ed amount of time. On the other hand, since the tag is assumed to not have an onboard clock, an adversary blocking either $M _ { T } \thinspace { \bf o r } \ M _ { R }$ or both essentially primes the tag to wait for the next authentication round since it can readily distinguish between the reader's <sup>fi</sup>rst message (Hello, R) from the reader's second message (M ) due to their di<sup>f</sup>erent signatures. Desynchronization in such authentication protocols commonly occur when an element (e.g., shared secret key) is updated by one side (reader or tag) and not the other. In the proposed protocol, the shared keys are <sup>fi</sup>xed and are not updated after every authentication round. Therefore, desynchronization is not an issue in this protocol.

## 4.3.6. Passive replay

In addition to the reader-generated nonce $( N _ { 1 } ) _ { : }$ , the ambient condition readings $\left( A _ { R } , A _ { T } \right)$ and the three noise vectors $( \nu _ { R _ { 1 } } , \nu _ { R _ { 2 } } , \nu _ { T } )$ introduce enough randomness in each round that a passive copy and replay of previous messages $( R , M _ { T } , M _ { R } )$ to tag or reader will not lead to successful authentication of tag to reader or reader to tag.

## 4.3.7. Reader/tag impersonation attack

Impersonation of tag to reader or reader to tag involves successful run of the protocol from the reference point (tag or reader). In the proposed authentication protocol, a successful tag impersonation to the reader would result in the reader's acceptance of $M _ { T }$ from tag to be valid. Similarly, successful reader impersonation to the tag would result in the tag's acceptance of both R and $M _ { R }$ from the reader as valid messages. Since the tag does not separate the individual components or validate R, any k-bit R is considered acceptable by the tag. An adversary still needs to send an appropriate $M _ { R }$ for successful impersonation of reader to tag. For the tag, a random $M _ { T }$ will not be successfully authenticated by the reader since $M _ { T }$ depends on $R , a , b ,$ among other elements that need to be strictly incorporated in the authentication protocol.

## 5. Experimental performance evaluation

We now simulate the considered frameworks and discuss the results. Speci<sup>fi</sup>cally, we are interested in the relative performance of the knowledge-based solution (Fig. 4) when compared with the other frameworks that include determining the presence of the tag of interest with knowledge of the presence of a related tag (Fig. 1), direct sensor (Fig. 2), and cross veri<sup>fi</sup>cation (Fig. 3). We summarize the di<sup>f</sup>erent cases and their associated components in Table 2.

Several previous studies adopt a similar methodological approach (e.g., [31,40,41]). To this end, we design four experimental cases (scenarios) corresponding to Case 1 (Associated Tags), Case 2 (Direct), Case 3 (Cross Veri<sup>fi</sup>cation) and Case 4 (Knowledge-based System) re spectively as discussed in Sections 3.1, 3.2, 3.3, and 3.4. In these cases, we observe the behaviors (e.g., read-rate errors) of items and their tags. In our experimental setup, 50% of the items are randomly kept in the same region (e.g., the same detection <sup>fi</sup>eld of a tag reader) and thus authenticated to be present. The rest of the items are not authenticated to be present. Furthermore, each item has a tag separation probability of 1%, 3%, 5%, 8%, or 10%. It is thus possible that, even when a tag is con<sup>fi</sup>rmed to be present by a reader, it could be a separated tag and the reality may be that the associated item has gone ‘missing’ or the item cannot be authenticated to be present. For Case 1, a pair of items wil always move together (e.g., with the same pallet). So, with T1 and T2 representing the two tags, we are interested in T2 with T1 as its related tag. Moreover, when both tags are attached, we con<sup>fi</sup>rm that T2 is present. When T1 is attached and T2 is separated, we con<sup>fi</sup>rm that T2 is present. When T1 is separated and T2 is attached, we con<sup>fi</sup>rm that T2 is present. Lastly, when both T1 and T2 are separated, we con<sup>fi</sup>rm that T2 is absent. For Case 2, we use sensor-generated data to detect tag separation and its accuracy rate is maintained at 70%. This signi<sup>fi</sup>es that when the sensor is operational as intended, we con<sup>fi</sup>rm that T2 is either absent or present based on the reading outcome. For Case 3, we cross reference Cases 1 and 2 to generate the results. For Case 4, we use a knowledge-based method that is integrated with the speci<sup>fi</sup>c methods for Cases 1, 2, and 3. The method is mainly reliant on a fact and its inference that any item with tag cannot be simultaneously present at two di<sup>f</sup>erent regions (i.e., abnormal tag readings). However, such ab normal readings may occur because a separated tag can still be possibly authenticated, even though it has been separated from its associated item. Thus, if either T1 or T2 is con<sup>fi</sup>rmed to be present at two regions, it can be reasoned that some reading errors have occurred and should be corrected appropriately. By design, we ensure that the occurrence of such errors is completely random. After implementing all of these cases (scenarios), we obtain the following results.

Table 2  
The four cases and their components.

<table><tr><td></td><td>Related tag</td><td>Sensor + cryptography</td><td>Knowledge-based system</td></tr><tr><td>Case 1</td><td>X</td><td></td><td></td></tr><tr><td>Case 2</td><td></td><td>X</td><td></td></tr><tr><td>Case 3</td><td>X</td><td>X</td><td></td></tr><tr><td>Case 4</td><td>X</td><td>X</td><td>X</td></tr></table>

We illustrate and discuss the results of the overall reads that include false positives (FP) and false negatives (FN), and their overall com plement reads that include true positives (TP) and true negatives (TN). Such reads are determined by examining whether the con<sup>fi</sup>rmed tag's presence or absence can match its associated item's presence or ab sence. Each of the underlying frequencies is respectively generated by 1000 simulated items' authentications and tags' reads. As presented in Table 3, the p-values are based on frequencies of false positive read because of tag separation. In other words, the reads occur speci<sup>fi</sup>cally when a tag (e.g., T2) is con<sup>fi</sup>rmed to be present, but its associated item is absent. Here, all the p-values represent signi<sup>fi</sup>cant di<sup>f</sup>erences in means (pair-wise two-tailed t-test) between any given pair of cases. The p-values show that the mean values for each of the considered pairs of cases are statistically signi<sup>fi</sup>cant. The mean (standard deviation) values for Cases 1, 2, 3, and 4 are respectively 52.8(29.19), 8(6.16), 35(19.73), and 30.6(15.84).

Table 3  
Pair-wise statistical signi<sup>fi</sup>cance of false positive reads due to tag separation.

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Case 1</td><td></td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>Case 2</td><td></td><td></td><td>0.01</td><td>0.01</td></tr><tr><td>Case 3</td><td></td><td></td><td></td><td>0.07</td></tr><tr><td>Case 4</td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/MDFMJGVZ/fulltext/images/c0cae0dc6bf0fbc16061572f4935b359b1d2d8466ba05117f3fa5e61affb1350.jpg)  
Fig. 6. Comparison results of false positive reads due to tag separation.

The actual frequency values are shown in Fig. 6. As can be seen here, Case 2 has the fewest false positive reads while Case 4 has the second fewest ones, as compared with those of the other cases. This result is not surprising because Case 2 represents a direct sensor-based solution. In the experiment, the solution is completely based on the sensor that is available for only one tag (e.g., T2). In other words, Case 2 is designed to address the tag separation problem without the use of any help from a related tag (e.g., T1), while all of the other solutions including Case 4 are associated with T1. Thus, Case 2 is inherently immune to any reading errors caused by the use of T1. However, thi also suggests that Case 2 could generate more false positive reads when compared with the other cases, considering the possibility that the sensor in Case 2 may not be operational at all times (i.e., accuracy = 70%) during experimental observation and Case 2 cannot use T1 as its related tag for double-check.

Next, in Table 4, the listed p-values correspond to frequencies of false negative reads. Each of the reads speci<sup>fi</sup>cally refers to the situation when a tag (e.g., T2) is con<sup>fi</sup>rmed to be absent, but its associated item is still present. Such a situation is typically a consequence of tag separation. Here, all the cases except Case 2 have similar frequencies. The means (standard deviation) for Cases 1, 2, 3, and 4 are respectively 1.8 (2.05), 32 (19.3), 1.8 (2.05), and 1.8 (2.05).

As presented in Fig. 7, the false negative reads for Case 4 are the fewest as compared with those of the other cases. On the other hand, the false negatives for Case 2 are the most, which is in contrast to the pattern of false positive reads for Case 2 as mentioned earlier. Putting together the results of false positive and negative reads, it is thus clear that Case 4 generates the fewest overall false reads. We now verify thi claim.

We consider the overall false reads that include both false positives and false negatives. The listed numbers in Table 5 are the statistical signi<sup>fi</sup>cance (p-values) results that are obtained through paired twotailed t-test for means of overall tag false reads. Except for the pair that represents Cases 2 and 3, the rest of the pair-wise means comparisons are statistically signi<sup>fi</sup>cant. The means (standard deviations) of the frequencies for Cases 1, 2, 3, and 4 for addressing the tag separation problem along with di<sup>f</sup>erent separation probabilities that take the following values: 1%, 3%, 5%, 8%, or 10% are respectively 54.6(31.09), 40(24.53), 36.8(21.67), and 32.4 (17.73).

As can be seen in Fig. 8, the overall false reads in Case 4 are con sistently lower than those in other cases. This signi<sup>fi</sup>es that the performance of Case 4, which includes a knowledge-based solution (Fig. 4), is generally superior to those of Cases 3, 2, and 1.

Table 4  
Pair-wise statistical signi<sup>fi</sup>cance of false negative reads due to tag separation.

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Case 1</td><td></td><td>0.02</td><td>N/A</td><td>N/A</td></tr><tr><td>Case 2</td><td></td><td></td><td>0.02</td><td>0.02</td></tr><tr><td>Case 3</td><td></td><td></td><td></td><td>N/A</td></tr><tr><td>Case 4</td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/MDFMJGVZ/fulltext/images/fd2b1a72169f97f992dac4b3d4cb3780b2accdc2136adb947a34e3cd04f3648a.jpg)  
Fig. 7. Comparison results of false negative reads due to tag separation.

Table 5  
Pair-wise statistical signi<sup>fi</sup>cance of overall false reads due to tag separation.

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Case 1</td><td></td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>Case 2</td><td></td><td></td><td>0.2</td><td>0.09</td></tr><tr><td>Case 3</td><td></td><td></td><td></td><td>0.07</td></tr><tr><td>Case 4</td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/MDFMJGVZ/fulltext/images/78f4afbb1d8d9f3cc79fbc2070a47f1cb4b875ccac8098baf2f4e0e8b36ca6e7.jpg)  
Fig. 8. Comparison of overall false reads due to tag separation.

Having considered the false reads, we now turn our attention to true reads. Table 6 shows the p-values corresponding to frequencies of true positive reads for Cases 1, 2, 3, and 4. The means (standard deviation) for Cases 1, 2, 3, and 4 are respectively 798.2(23.44), 754.2(20.66), 798.2(23.44), and 798.2(23.44). Each of the reads refers to the situation where a tag is con<sup>fi</sup>rmed to be present and its associated item is truly present. On the other hand, if any tag separation occurs and the situation is mishandled, it may cause these reads to decrease.

As seen in Fig. 9, Case 4 generates the most true positive reads than the other cases. Moreover, the numbers are mostly concentrated around 500. This is because, by our experimental design, 50% of the overall 1000 simulated items are con<sup>fi</sup>gured to be truly present.

The following table illustrates the results of true negative reads (Table 7) that are complementary to the results based on true positive reads. The means (standard deviation) for Cases 1, 2, 3, and 4 are respectively 434.2(41.98), 479(20.59), 452(33.37), and 456.4(30.48). Each of the true negative reads speci<sup>fi</sup>cally refers to the situation where a tag is con<sup>fi</sup>rmed to be absent and its associated item is truly absent. In other words, if there is any tag separation problem that is not appropriately addressed, either true positive reads or true negative reads decrease. As we noted in our discussion of results of true positive reads, the frequencies of these reads are also concentrated around 500 in that

Table 6  
Pair-wise statistical signi<sup>fi</sup>cance of true positive reads due to tag separation.

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Case 1</td><td></td><td>0.02</td><td>N/A</td><td>N/A</td></tr><tr><td>Case 2</td><td></td><td></td><td>0.02</td><td>0.02</td></tr><tr><td>Case 3</td><td></td><td></td><td></td><td>N/A</td></tr><tr><td>Case 4</td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/MDFMJGVZ/fulltext/images/a9a41e1cc82198e03e4912229744bb77cdc32d0220dbb894ddedf545751eb933.jpg)  
Fig. 9. Comparison results of true positive reads due to tag separation.

Table 7  
Pair-wise statistical signi<sup>fi</sup>cance of true negative reads due to tag separation.

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Case 1</td><td></td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>Case 2</td><td></td><td></td><td>0.01</td><td>0.01</td></tr><tr><td>Case 3</td><td></td><td></td><td></td><td>0.07</td></tr><tr><td>Case 4</td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/MDFMJGVZ/fulltext/images/ec62f30494c4741c0214253402d116f079fbca56e6c879de14d4eb46b3ac90d2.jpg)  
Fig. 10. Comparison results of true negative reads due to tag separation

50% of the overall 1000 simulated items are con<sup>fi</sup>gured to be truly absent.

Relatedly, as seen in Fig. 10, Case 4 generates the second most true negative reads and Case 2 generates the most. However, considering that Case 2 generates much fewer true positive reads than Case 4, the overall positive reads for Case 4 are still generally more than the overall positive reads in any of the other cases including Case 2. This denotes that Case 4 outperforms other cases in the experiment with respect to generating more correct reads (i.e., true positive reads plus true negative reads). This is also consistent with the presented results that Case 4 generates the fewest overall incorrect reads (i.e., false positive reads plus false negative reads) as illustrated in earlier tables and <sup>fi</sup>gures.

We can now summarize the overall true reads, as shown in Table 8. Such reads are determined by examining whether the con<sup>fi</sup>rmed tag's presence or absence can truly match its associated item's presence or absence. Each of the underlying frequencies is respectively generated by 1000 simulated items' authentications and tags' reads. Again, the included numbers in this table are the statistical signi<sup>fi</sup>cance (p-values) based on paired two-tailed t-test for means of overall tag true reads. The means (standard deviations) of the frequencies for Cases 1, 2, 3, and 4 for addressing the tag separation problem along with di<sup>f</sup>erent separation probabilities that take the values 1%, 3%, 5%, 8%, or 10% are respectively 945.4(31.09), 960(24.53), 963.2(21.67), and 967.6(17.73).

Table 8  
Pair-wise statistical signi<sup>fi</sup>cance of overall true reads due to tag separation.

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Case 1</td><td></td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>Case 2</td><td></td><td></td><td>0.2</td><td>0.08</td></tr><tr><td>Case 3</td><td></td><td></td><td></td><td>0.07</td></tr><tr><td>Case 4</td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/MDFMJGVZ/fulltext/images/46b96d779595bb64aaeeb0429789b98ee84c0282893076247f53ac274410a6b3.jpg)  
Fig. 11. Comparison of overall true reads due to tag separation.

As can be seen in Fig. 11, the overall true reads in Case 4 are con sistently more than those in the other cases. The second best is Case 3, followed by Case 2, and with Case 1 being the last. These results complement the results for overall false reads. Again, this signi<sup>fi</sup>es that the performance of Case 4 is generally superior to those of Cases 3, 2, and 1.

In sum, these experimental results provide an overall solid support for our proposition to address the tag separation problem. Comparatively speaking, related tag (Case 1), direct sensor (Case 2), and cross veri<sup>fi</sup>cation (Case 3) have their respective weaknesses and strengths in handling di<sup>f</sup>erent tag separation-caused reading errors such as false negatives and false positives. Overall, however, a knowl edge-based solution with learning capability (Case 4) that integrates the major characteristics of the means of related tag, direct sensor, and cross veri<sup>fi</sup>cation, is more likely to mitigate the risk of tag separation and thus generate more correct reads.

## 6. Discussion and conclusion

Retailers are searching for novel solutions to alleviate their in ventory shrinkage su<sup>f</sup>erings as well as to improve their loss prevention strategies [1]. In the U.S., the total cost to deal with such losses has reached more than \$6 Billion a year [8]. A key <sup>fi</sup>nding of the latest survey of the 2018 national retail security by the University of Florida and National Retail Federation [20] is that, as compared to 2017, the adoption rate of RF (Radio-Frequency) electronic security tags for loss prevention has increased from 7.9% to 30.2%. The main causes for such losses include shoplifting (36%), internal theft (30%), and administrative error (21%). In other words, retailers count on RFID for inventory and supply chain management to reduce their shrinkage losses, which amount to billions of dollars per year. From this perspective, the importance of studies like this is very clear, since none of these RFID enabled loss reduction mechanisms would be achievable without en suring that RFID tags remain attached to their associated items.

Relatedly, several recent industrial cases have highlighted that, while RFID-enabled information provides great help for managing retail losses, there is still quite a large room for improving or securing RFID tags. According to an analysis of top 100 U.S. apparel retailers [3], 96% (including Macy's and Target) plan to tag their merchandize with itemlevel RFID tags. Many U.K. retailing enterprises also have concerns that RFID tags are easily separated from items and thus are not very secure for those “would-be” situations including theft [33]. Considering these industrial cases in retailing supply chains where billions of item-level RFID tags are deployed, the importance of detecting and notifying the separation of RFID tags and items cannot be overstated.

In addition, non-intentional tag separation cases are more common in the supply chains for food, produce, livestock, etc. For example, tag loss rate on fresh produce containers is estimated to be up to 70% under an experimental environment where these reusable plastic containers are randomly distributed and cleaned in several rounds [28]. The sur vival rate of the tags on wood products in operations may vary from 91% to 100% [23]. In the cattle supply chain, the annual tag loss rate could reach 10% and amount to an overall loss of 1.94 mil lion GBP per year [32].

Given the above statistics, the primary purpose of this paper is to raise awareness for tag separation in RFID-based systems since all existing RFID-based applications are vulnerable to tag separation. The assumption that once an item is RFID-tagged, the tag remains with the item until it is intentionally separated or deactivated by an honest party, may not always be valid. RFID tag separation or deactivation could be intentionally accomplished by an adversary for any number of reasons (e.g., ticket switching, theft). Unintended RFID tag separation may also occur (e.g., when the tagged item is damaged). When RFID tag deactivation occurs, communication with that tag is no longer possible, with the result that the tagged item goes ‘missing’ in automated systems. When RFID tag separation occurs, authentication of the tag signi<sup>fi</sup>es just that and has nothing to do with the item that is tagged since that item may no longer be in close physical proximity to the tag. In other words, an authenticated (separated) tag does not guarantee that (a) this RFID tag is attached to the corresponding ‘tagged item’ or (b) the item is even in close physical proximity to the RFID tag. Therefore, in addition to defeating its intended purpose of tagged-item identi<sup>fi</sup> cation, RFID tag separation could also engender related resulting consequences of the false conclusion that the item is missing when it really is present and vice versa.

Extensive review of existing published literature revealed that none of the existing RFID-based cryptographic authentication protocols consider the possibility of tag separation. The reason may well be that the primary purpose of these protocols is to ensure proper and secure authentication of the RFID tags and not the object to which the tag of interest is attached. However, since an RFID tag is not meant to be a stand-alone entity, by itself it serves no purpose in almost all of its applications. Minor exceptions include cases where sensor-based RFID tags are randomly distributed to measure ambient conditions. An RFID tag becomes useful only upon holding associated identi<sup>fi</sup>cation and/or other information about the tagged object. Therefore, a stand-alone RFID tag is useless for almost all practical purposes.

We considered this signi<sup>fi</sup>cant issue of tag separation in our study. To the best of our knowledge, there is only one published paper that considers RFID tag separation. However, this paper does not deal with tag separation per se but rather the e<sup>f</sup>ects of tag separation on EOQ, among others. We speci<sup>fi</sup>cally and directly considered RFID tag separation and proposed means to address this issue. We considered a few di<sup>f</sup>erent possibilities and also developed a method to address RFID tag separation with a knowledge-based framework that incorporates a cryptography-based mutual authentication protocol. We discussed some common security aspects of the proposed authentication protocol.

Since this is the <sup>fi</sup>rst study that attempts to directly address RFID tag separation, we cannot compare the proposed method to any existing method. We therefore considered a few di<sup>f</sup>erent possible means and then compared their performance with that of the proposed knowledgebased framework. The performance results obtained with the knowledge-based system seems promising vs. those of other considered methods. Tag separation is a signi<sup>fi</sup>cant issue in RFID-based systems that has so far not received its fair share of attention. We hope that this paper motivates researchers to study tag separation and to develop better means to directly address this issue.

## Acknowledgement

We thank the two anonymous reviewers for carefully reading the previous version of this paper and for taking their time to provide extensive constructive comments, which helped us improve the content and presentation of this paper.

## References

[1] Accenture, https://www.accentureacademy.com/lms/course/1000007724/, (2018).

[2] Agence France Press, http://www.intothewine.fr/tags/trelissac-vin2011.

[3] Auburn University, https://r<sup>fi</sup>d.auburn.edu/papers/2016-state-r<sup>fi</sup>d-adoptionamong-u-s-apparel-retailers/, (2016).

[4] I. Bose, S. Yan, The green potential of RFID projects: a case-based analysis, IEEE IT Prof. 13 (1) (2011) 41–47.

[5] I. Bose, X. Chen, A framework for context sensitive services: a knowledge discovery based approach, Decis. Support. Syst. 48 (1) (2009) 158–168.

[6] I. Bose, C.Y. Lam, Facing the challenges of RFID data management, Int. J. Inf. Syst. Supply Chain Manag. 1 (4) (2008) 1.

[7] J. Cazecaa, J. Meada, J. Chenb, R. Nagarajana, Passive wireless displacement senso based on technology, Sensors Actuators A Phys. (2013) 197–202.

[8] Deloitte, https://deloitte.wsj.com/cio/2018/02/28/stem-retail-loss-with-datascience-advanced-analytics/, (2018).

[9] DTechEx, Apparel RFID 2013–2023, (June 2017).

[10] http://www.farsens.com/en/products/battery-free-r<sup>fi</sup>d-sensors/.

[11] Frost & Sullivan, RFID Market in Apparel Supply Chain, (May 2012).

[12] M. Grunow, S. Piramuthu, RFID in highly perishable food supply chains - remaining shelf life to supplant expiry date? Int. J. Prod. Econ. 146 (2013) 717–727.

[13] T. Halevi, S. Lin, D. Ma, A.K. Prasad, N. Saxena, J. Voris, T. Xiang, Sensing-enabled defenses to RFID unauthorized reading and relay attacks without changing the usage model, Proceedings of the IEEE International Conference on Pervasive Computing and Communications, 2012, pp. 227–234.

[14] X. Hu, X. Li, E. Ngai, V. Leung, P. Krutchen, Multidimensional context-aware social network architecture for mobile crowdsensing, IEEE Commun. Mag. 52 (6) (2014) 78–87.

[15] X. Li, Y. Fan, An approach to testing trustworthiness of web services, J. Chin. Comput. Syst. 9 (2008) 002.

[16] X. Li, Could Deal promotion improve merchants' online reputations? The moderating role of prior reviews, J. Manag. Inf. Syst. 33 (1) (2016) 171 201.

[17] D. Ma, A.K. Prasad, N. Saxena, T. Xiang, Location-aware and safer cards: enhancing RFID Security and privacy via location sensing, Proceedings of the ACM Conference on Wireless Network Security (WiSec), 2012, p. 5162.

[18] R. McMillan, Tech. Exec. Built Stolen ‘Legoland’ in \$2M Home. Wired, 25 May, (2012).

[19] https://technology.nasa.gov/patent/MSC-TOPS-49.

[20] NRF, https://nrf.com/resources/retail-library/national-retail-security-survey-2018, (2018).

[21] C. Paggi, C. Occhiuzzi, G. Marrocco, Sub-millimeter displacement sensing by passive UHF RFID antennas, IEEE Trans. Antennas Propag. (62) (2014) 905–912.

[22] M. Philipose, J.R. Smith, B. Jiang, K. Sundara-Rajan, A. Mamishev, S. Roy, Battery free wireless identi<sup>fi</sup>cation and sensing, IEEE Pervasive Comput. 4 (1) (2005) 37–45.

[23] G. Picchi, M. Kühmaier, J.D.D. Marque, Survival test of RFID UHF tags in timber, Harvesting Oper. 36 (2) (2015) 165–174.

[24] S. Piramuthu, Protocols for RFID tag/reader authentication, Decis. Support. Syst. 43 (3) (2007) 897–914.

[25] S. Piramuthu, S. Wochner, M. Grunow, Should retail stores also RFID-tag ‘cheap’

items? Eur. J. Oper. Res. 233 (2014) 281–291.

[26] S. Piramuthu, R. Doss, On sensor-based solutions for simultaneous presence of multiple RFID tags, Decis. Support. Syst. 95 (March 2017) 102–109.

[27] E. Schuman, Wal-Mart Stung in \$1.5 Million Bar-Code Scam, eWeek, 2005 (January 5).

[28] J. Singh, S.P. Singh, K. Desautels, K. Saha, E. Olsen, An evaluation of the ability of RFID tags to withstand distribution of fresh produce in the RPC pooling system, Packag. Technol. Sci. 23 (4) (2010) 217–226.

[29] Time, Woman tried to get \$1,800 in electronics for \$3.70 by switching price tags at Walmart, http://time.com/money/5017001/woman-switches-tags-electronics/, (November 9, 2017).

[30] Y.-J. Tu, S. Piramuthu, Lightweight non-distance-bounding means to address RFID relay attacks, Decis. Support. Syst. 102 (2017) 12–21.

[31] Y.-J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications. Decis. Support, Syst, 46 (2) (2009) 586–593.

[32] UK EID, https://www.uppernisbet.co.uk/app/download/15627509/Robert-Neillreport-2013.pdf, (2014).

[33] University of Leicester, http://www.industriequattropuntozero.it/<sup>fi</sup>les/2018/07/ Measuring-the-Impact-of-RFID-in-Retailing.pdf. (2018)

[34] P. Urien, S. Piramuthu, Elliptic curve-based RFID/NFC authentication with tem perature sensor input for relay attacks, Decis. Support. Syst. 59 (2014) 28–36.

[36] W. Zhou, RFID and item-level information visibility, Eur. J. Oper. Res. 198 (1) (2009) 252–258.

[37] W. Zhou, S. Piramuthu, Preventing ticket-switching of RFID-tagged items in appare retail stores, Decis. Support. Syst. 55 (3) (June 2013) 802–810.

[38] W. Zhou, S. Piramuthu, E<sup>f</sup>ects of ticket-switching on inventory management: actual vs. information system-based data, Decis. Support. Syst. 77 (September 2015) 31–40.

[39] W. Zhou, S. Piramuthu, E<sup>f</sup>ect of ticket-switching on inventory and shelf-space al location, Decis. Support. Syst. 69 (January 2015) 31 39

[40] W. Zhou, S. Piramuthu, Identi<sup>fi</sup>cation shrinkage in inventory management: an RFID-based solution, Ann. Oper. Res. 258 (2) (2017) 285–300.

[41] W. Zhou, Y.-J. Tu, S. Piramuthu, RFID-enabled item-level retail pricing, Decis. Support. Syst. 48 (1) (2009) 169–179.

[42] A. Zimmerman, As shoplifters use high-tech scams, retail losses rise, Wall Street J. (October 25, 2006) A1.

Yu-Ju Tu is Assistant Professor of Information Systems at the National Cheng Chi University in Taiwan. His research interests include RFID systems.

Wei Zhou is a Professor of Information Systems at ESCP-Europe. His research interests include RFID systems.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida. His research interests include RFID systems.
