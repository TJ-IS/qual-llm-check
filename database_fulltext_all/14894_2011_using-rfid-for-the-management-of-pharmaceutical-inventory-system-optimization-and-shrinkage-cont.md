---
otero_id: 14894
otero_key: "RX3SEVG2"
title: "Using RFID for the management of pharmaceutical inventory — system optimization and shrinkage control"
authors: "Özden Engin Çakıcı; Harry Groenevelt; Abraham Seidmann"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using RFID for the management of pharmaceutical inventory — system optimization and shrinkage control

Özden Engin Çakıcı, Harry Groenevelt, Abraham Seidmann ⁎

William E. Simon Graduate School of Business, University of Rochester, Rochester, NY, United States

a r t i c l e i n f o

Available online 5 February 2011

Keywords: RFID and Barcode Radiology pharmaceuticals Inventory Periodic and continuous review Manual and automatic counting Shrinkage Real-time visibility

## a b s t r a c t

Motivated by a case study at a radiology practice, we analyze the incremental bene<sup>fi</sup>ts of RFID technology over barcodes for managing pharmaceutical inventories. Unlike barcode technology, RFID enables accurate realtime visibility, which in turn enables several process improvements. We analyze the impact of automatic counting and discuss the system redesign critical to optimizing the inventory policy and eliminating shrinkage. We show that continuous review is superior to periodic review whenever accurate real-time information is available at no additional cost. We explain how RFID-enabled strategies vary with inventory parameters and provide a cost-bene<sup>fi</sup>t analysis for the implementation of RFID for the radiology practice.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction and motivation

Motivated by a case study conducted at the radiology practice of a major hospital network in Florida, we analyze the incremental bene<sup>fi</sup>ts of RFID technology over barcodes in the context of pharmaceutical and drug inventory management.

Healthcare has unique and strict guidelines for managing its drug supply chain. E-pedigree requirements and state and federal laws and regulations necessitate that information about the manufacturer, lot numbers, complete shipping information, dosage, etc., be registered in a drug's tag. These regulations seek to protect public health by reducing counterfeiting and facilitating product recalls in the drug industry. Although barcodes help increase security by permitting the tracking of drugs, they are not unique codes that can help pinpoint an item in its distribution network, and they do not have high data storage capacity to provide detailed information about an item; moreover, unless an item's barcode is scanned, its tracking records cannot be updated. Barcodes also have intrinsic scanning problems, creating inaccurate inventory records [11,32].

Within the broad topic of supply chain management, pharmaceutical and drug inventory management also differs from inventory management in other sectors. Drug inventory is closely scrutinized, and drugs are kept in small, locked storage cabinets after delivery.

Moreover, certain pharmaceuticals and drugs are expensive and perishable. While the strict regulations on shipping and delivery increase the administrative costs of ordering, the unique item features and secure storage requirements increase holding costs. Certain drugs or items are also required in particular procedures and surgeries (e.g., contrast media to enhance the picture quality of an MRI or blood units in a surgery). Therefore, since a drug shortage can lead to low utilization of machines, doctors, and technologists or, in extreme cases, harm to a patient, stockouts can be extremely expensive.

Before implementation of RFID, the radiology practice used barcode technology to monitor its inventory of contrast media vials. Most of the process was handled by a technologist who checked medical records, scanned barcodes of vials before administration, manually counted the number of vials in stock, and reordered weekly. These manual processes were creating serious operational problems: (1) exam mismatches (i.e., executing a job on the wrong patient), (2) adverse drug events (e.g., administering the wrong dosage), (3) stock and billing issues, and (4) shrinkage (e.g., content expiration caused by failure to use a previously opened vial).

Unlike barcodes, RFID provides accurate real-time visibility of inventory status at the individual item level, as each item has a unique id tag and hence a corresponding unique inventory record. When inventory records are inaccurate and no real-time visibility exists (i.e., under barcode technology), organizations have to use manual counting and periodic review of items to reconcile the actual inventory on hand and the inventory record. In contrast, when inventory tracking is accurate and timely, managers can implement automatic counting and continuous review of stock levels. Moreover, being able to identify each item uniquely ensures that any change in the state of an item is automatically registered in the inventory record system (e.g., imminent expiration of a partially used drug vial).<sup>1</sup> An inventory manager therefore can additionally bene<sup>fi</sup>t from RFID by employing automatic counting, policy improvement (shifting from periodic to continuous review), and shrinkage tracking. The real life practices of RFID implementation in the healthcare industry, however, show that most appreciate only automatic counting and hence lose the potential for larger savings. Our paper shows how cost savings from policy improvement and shrinkage tracking are more important than automatic counting alone by comparing two scenarios: an inventory manager (1) employs old operational strategies and is content with only reducing the cost of counting inventory, or (2) also leverages the technology by changing the inventory control system from a Periodic Review (PR) to a Continuous Review (CR) policy and reducing shrinkage by tracking expiration. Under option (1) the current operational policy costs less, while option (2) uses Business Process Redesign (BPR) to extract the full bene<sup>fi</sup>t of RFID.

To account for the impact of three additional bene<sup>fi</sup>ts of RFID on inventory management, our paper proposes a model for PR that uses continuous costing to allow a correct and direct comparison between different PR policies and with CR policies. This is not possible with the traditional end-of-period costs used for PR models in the inventory literature. Using this model, we show that the attained optimal service level under shrinkage decreases. Also, assuming no shrinkage, we show analytically that the switch to continuous review (CR) from periodic review (PR) decreases the on-hand inventory, the level of backorders, and the frequency of orders and their corresponding costs, making CR the lower cost alternative. We also show that the optimal average order quantity and the review period length are concave increasing in the <sup>fi</sup>xed cost of ordering for both CR and PR. We further look at the change in the ratio of inventory-related costs (the average inventory cost plus the average backorder cost) to average ordering cost with respect to the optimal average order quantity and <sup>fi</sup>xed ordering cost. We found that this ratio is convex decreasing in the optimal average order quantity (review period), and the <sup>fi</sup>xed ordering cost for CR (PR). Under RFID, manual counting is eliminated due to automatic counting of items, resulting in a lower <sup>fi</sup>xed ordering cost. Hence, these results show that a decrease in the <sup>fi</sup>xed ordering cost as a result of a switch to automatic counting for RFID (or CR) from using manual counting for barcodes (or PR) keeps the operational and economic metrics still lower for RFID (or CR) than for barcodes (or PR). Our results also show that for the optimal CR and PR, a decrease in the <sup>fi</sup>xed ordering cost decreases the average ordering cost more than it does the inventory-related costs.

We conduct a sensitivity analysis by varying inventory parameters to provide additional managerial insights in different operational environments. Through this analysis we also account for the bene<sup>fi</sup>t from shrinkage tracking numerically. We show that the percentage cost savings from RFID (without BPR) decrease with the service level (or, equivalently, the backorder cost), the mean and standard deviation of demand, the lead time, the shrinkage rate, and the cost per order placed under RFID,<sup>2</sup> while the cost savings from employing BPR increase in all these parameters. The total cost savings from RFID combined with BPR therefore also increase in all parameters except in the cost per order placed under RFID. Hence, RFID is more attractive relative to older technologies in environments with high backorder costs (high service levels), high demand rates, high levels of uncertainty, high shrinkage rates, long lead times, and high manual counting costs.

Our case study illustrates that the radiology practice saves 76% of its total inventory management costs by switching from barcodes to RFID and redesigning its business processes. About one quarter of the total savings is attributed to the reduced cost of counting inventory, while business process redesign accounts for three quarters. These signi<sup>fi</sup>cant cost savings result in an internal rate of return (IRR) of over 54% under the assumption that the technology has a life expectancy of ten years.

The rest of the paper is organized as follows. Section 2 contains the literature review. In Section 3 we discuss the operational and economic problems encountered under barcode technology by our case study. We then provide our inventory models and analytical comparisons between periodic and continuous review policies in Section 4. In Section 5 we numerically analyze and quantify the impact of RFID on operational and economic aspects of a single-item (e.g., contrast media) inventory via the two options described brie<sup>fl</sup>y above, and in Section 6 we provide a cost-bene<sup>fi</sup>t analysis for RFID. Section 7 concludes and provides suggestions for future research.

## 2. Literature review and contribution

We analyze the operational and economic impacts of RFID technology and, in particular, the impact of real-time tracking on single-item inventory management in this context. Our paper thus tackles several well-known open issues in RFID and inventory theory literature: (1) we outline an innovative continuous-time approach to account for inventory costs more accurately; (2) we provide analytical justi<sup>fi</sup>cation for the choice of continuous review as the inventory control policy; and (3) we analyze the impact of RFID on the ordering cost.

The current RFID inventory literature (and most of the classical inventory theory literature), uses “end-of-period costing,” which accounts for inventory on hand and backorders at review epochs only. This prevents an unbiased comparison with continuous review models, since they assess these costs continuously. The comparison between PR and CR is discussed by Hadley and Whitin [20] but never analytically analyzed. Freeland and Porteus [16], using end-of-period costing for PR, mention how PR and CR employ different methods for cost accounting, such that a comparison is not correct. Our proposed continuous time cost model accurately accounts for holding and backorder costs and provides a precise way to compare the economic impact of different inventory review policies. Such costing has been used by Hadley and Whitin [20] and Veinott [43], and more recently by Çakıcı et al. [8], Groenevelt [18], Groenevelt and Rudi [19], Jain et al. [23] and Rao [38]. We refer the reader to Rudi et al. [39] for a discussion between end-of-period and continuous time costing.

The literature on RFID technology and its bene<sup>fi</sup>ts for inventory management focuses mostly on the cost reduction resulting from elimination of inaccuracy. Before RFID, inventory records were typically assumed completely accurate in the inventory literature. In reality, prior technologies were often prone to error. Atalı et al. [2], Bensoussan [4], DeHoratius et al. [12], Fleisch and Tellkamp [15], Kang and Gershwin [25], and Kök and Shang [27] model the inaccuracy problem and show the bene<sup>fi</sup>ts of eliminating inaccurate data (e.g., using RFID) from the inventory information system. One of the important factors that affects inventory accuracy is shrinkage. In the studies by Atalı et al. [2], Bensoussan et al. [4], Fleisch and Tellkamp [15], and Kang and Gerschwin [25], shrinkage is included as one of the causes of data inaccuracy. DeHoratius et al. [12] and Kök and Shang [27] study a general error to inventory data that can assume negative and positive values. All of these studies, however, assume either periodic or continuous review without considering which review policy is optimal for RFID technology.

Cheng et al. [10] use both a periodic and a continuous inventory review policy for a three-echelon supply chain and show the economic differences between the two by a simulation study. Çakıcı et al. [7] and Çakıcı and Seidmann [6] use a model with end-of-period costing and Poisson demand to assess the inventory cost savings of RFID. Çakıcı et al. [8] provide a numerical analysis of the bene<sup>fi</sup>ts of RFID that completely ignores the issue of shrinkage. Our paper differs in its emphasis on shrinkage resulting from content expiration. We also combine analytical comparison of periodic and continuous review policies with an empirical study in a radiology practice, identifying the operational problems of the practice that can be addressed by RFID technology.

Part of the RFID inventory literature (e.g., Atalı et al. [2], DeHoratius et al. [12], and Kang and Gershwin [25]) also does not account for a <sup>fi</sup>xed ordering cost, which constitutes a high proportion of the total cost of inventory in some organizations (e.g., hospitals). A cost structure with no <sup>fi</sup>xed ordering cost component is applicable, for instance, in a shelf replenishment problem at a retailer (where, for example, shelves are replenished from the warehouse at almost zero cost). In our case study, however, we observe high <sup>fi</sup>xed ordering costs per order along with high holding and backorder costs per item per unit time. Therefore, in order to truly compare inventory costs under barcode technology and RFID, one needs to consider <sup>fi</sup>xed ordering costs.

Our research is also related to the literature on the single-item, in<sup>fi</sup>nite horizon inventory management problem. Our model is similar to those in Çakıcı et al. [8], Gallego [17], Groenevelt [18], Rao [38], Veinott [43], Zheng [45] and Zipkin [46]. Unlike these studies, our periodic review model includes shrinkage (proportional to inventory on hand). Our shrinkage modeling is an approximation because it does not take into account the age of the products in inventory, but our empirical <sup>fi</sup>ndings demonstrate that this approximation is quite reasonable for the radiology setting.

The pioneer in single-item perishable inventory literature is Van Zyl [42]. The reader can also refer to Nahmias [34] and Raafat [37] for a thorough review of early studies in this <sup>fi</sup>eld. Prastacos [36] looks speci<sup>fi</sup>cally at the management of blood inventory with very short shelf life. Shrinkage in our paper, however, only occurs after a vial is opened for use, since the shelf life for unopened vials is de facto unlimited. There is also a considerable literature that looks at concurrent pricing decisions in retail sectors using a newsvendor setting. Interested readers can consult papers by Cachon and Kök [5], Li et al. [30], Monahan et al. [33], and Petruzzi and Dada [35]. The hospital environment we consider, however, is quite different since it involves repeated orders with <sup>fi</sup>xed costs (vs. a single order in the newsvendor model), and the products are consumables with very high stockout costs (vs. retail items with much more moderate stockout costs).

There is much literature on RFID, considering the value of RFID data for tactical and strategic purposes within a supply chain (Amini et al. [1]), supplier's reaction to mandated RFID implementation (Barratt and Choi [3]), the value of more business intelligence data (Delen et al. [13]), technology (Dutta et al. [14]), bene<sup>fi</sup>ts from RFID adoption (Heese [22]), visibility in the reverse channel (Karaer and Lee [26]), pricing and allocation of retail shelf space under VMI (Szmerekovsky et al. [41]), and factors that affect RFID adoption and its bene<sup>fi</sup>ts (Whitaker et al. [44]). We refer the reader as well to Lee and Özer [29] for a comprehensive review of future applications of RFID.

## 3. Case study

We conducted a case study at the radiology practice of a major hospital network in Florida [6]. The practice has two 1.5T MRIs that image on average 44 patients/day. The quality of an MRI depends on a patient's body characteristics and can be enhanced by injecting contrast media. On average 60% of all patients require contrast media, and a contrast media vial can be used by seven patients on average. An unopened vial has a shelf life of up to two years, but an opened one expires in a day. The practice loses 1.42% of its daily average on-hand inventory (almost two items per week) to shrinkage. The inventory counting was outsourced to a drug supplier who manually counted inventory each Friday and supplied vials according to an already determined order-up-to level of 45 items. On average 20 items are used within a week and therefore ordered. The supplier charged for manual counting by charging 4% of the vial price of \$240 for each vial ordered, which amounted to a <sup>fi</sup>xed cost of almost \$200 per inventory review. The radiology practice was using barcode technology both to tag the vials and to track inventory transactions. After implementation of RFID, the contrast media vials use passive RFID tags (with virtually negligible cost), and the cost of tagging is borne by the supplier.

The management of contrast media vial inventory requires intense human involvement. A radiology technologist checks a patient's medical records and scans the vial's barcode before administering the contrast media. After administration, if there is still media left in the vial, the technologist puts the used vial back in the storage cabinet for further use. During these processes, we observed the following operational issues.

Exam Mismatches: A mismatch occurs when an exam ordered for a patient is administered to another patient. This can lead to adverse drug events and also means that certain procedures must be repeated, which decreases the overall ef<sup>fi</sup>ciency of the practice.

Adverse Drug Events: Some patients show reactions to contrast media and may develop NSF (nephrogenic systemic <sup>fi</sup>brosis), a rare systemic disorder that leads to chronic kidney disease or even death. Such a complication can have very serious <sup>fi</sup>nancial consequences for the practice.

Stock and Billing Issues: Stock and billing issues mostly result from barcode scanning errors. Scanning a vial barcode can be a daunting task when it is partially peeled off or worn. Furthermore, these problems waste time. The scanning problems create inaccuracies in billing that lead to lower real reimbursement amounts and cause inaccuracies in inventory records (e.g., items left in an exam room cannot be tracked unless somebody discovers them), creating missing or undesignated stock items, and hence the inventory manager tends to hold excessive inventory to <sup>fi</sup>ght against costly shortages. To illustrate how unreliable barcode readings can be, a simulation study by Merry et al. [32] found that “50% of participants failed to scan a barcode on at least one occasion during a typical surgery.”

Shrinkage: Shrinkage is de<sup>fi</sup>ned as all forms of item losses. Since a contrast media vial can be used by more than one patient and with barcodes these partially <sup>fi</sup>lled vials cannot be tracked by the system, the radiology technologist can easily pick an unused bottle instead of using the already opened one that is ready to expire. As a result, the practice loses a weekly average of almost two vials to shrinkage.

Most of the above problems intrinsically relate to human involvement and to not being able to uniquely track an opened item.

## 3.1. Benefits of RFID

In order to <sup>fi</sup>nd solutions to the aforementioned operational problems in the radiology practice, in this section we discuss the bene<sup>fi</sup>ts of RFID over barcode technology.

Line of Sight and Simultaneous Multiple Reads: The radiology technologist must explicitly scan the barcode of each contrast media vial used so the information about billing, corresponding patient name, etc., can be recorded. Scanning errors and omissions cause inaccurate billing and inaccurate inventory records and may contribute to adverse drug events. RFID technology, on the other hand, is a wireless technology that allows the entire content of the media vial cabinet to be determined at once, so vial use can be logged automatically without human involvement.

Data Storage Capacity: RFID has a large data storage capacity, which permits coding each item uniquely and recording more information about an item. Unique item coding can provide full tracking, which helps in recalls and reduces shrinkage, adverse drug events, and patient injuries. More storage means that information about the exact time, date, and production line of manufacturing; the expiration date; the dosage level; and shipping can be made available in just one RFID tag.<sup>3</sup>

Security, E-pedigree and Product Recalls: The medical sector is prone to counterfeiting, and barcodes can be duplicated easily, whereas RFID tags have encrypted information that is much more dif<sup>fi</sup>cult to forge. There are several state and federal laws, such as the Prescription Drug Marketing Act (PDMA) and the Florida Pedigree $\mathsf { A c t } ,$ requiring that each drug include information about its dosage, lot numbers, and distribution network. RFID tags can register this type of information, which ensures regulatory compliance and increases the safety and security of patients.

Durability: RFID tags can be encased within the caps of vials, giving them almost in<sup>fi</sup>nite durability, whereas barcodes are easily damaged or rendered unusable.

Shrinkage Prevention: RFID can monitor the inventory status of an item in real time through its wireless technology. Hence, expiration times for each unique vial (both unopened and opened and partially used) can be known so that a technologist can be warned to pick an already used vial from the storage cabinet.<sup>4</sup> Barcodes can convey only static information and only do so when scanned.

Automatic Counting and Reordering: RFID increases the accuracy of the inventory records and provides real-time visibility; hence items can be automatically counted and reordered without human involvement when the inventory drops to a certain level. While automatic counting eliminates the cost of manual counting, automatic reordering reduces the administrative costs of ordering.

All in all, RFID technology has many bene<sup>fi</sup>ts over barcodes to help solve the operational issues of the radiology practice in particular and of systems with similar operational issues. Table 1 summarizes the key differences between barcode and RFID technologies described above.

## 3.2. A new technology for pharmaceutical storage

Our study uses a recently introduced technology, an innovative system for contrast-media management designed to support radiology departments in dealing with the complex issues associated with the utilization of contrast media. This technology is an RFID-enabled locked and secured storage cabinet for stocking contrast media. It combines “tagged” vials of contrast agent with a “smart” cabinet and a specially designed interface linked to a patient's electronic medical record (EMR), the job list, and the charge description master (CDM).<sup>5</sup> With the EMR interface, the storage cabinet ensures that the patient's allergies, weight, and kidney functions are taken into account before a contrast media vial is dispensed. It captures, stores, and manages product utilization data easily and reliably while helping to reduce the risk of human error. It also provides valuable operational information about technologist dosing behavior, utilization trends, and automated due-date compliance, which is not otherwise available to radiology administrators today. In particular, the storage cabinet can manage the contrast media inventory by RFID and thus allows us to quantify the bene<sup>fi</sup>ts of RFID over barcode technology.

Note that the same storage cabinet technology can be used in conjunction with barcode technology. However there are two major problems associated with such an application. First, with barcodes the inventory system cannot differentiate one vial from another, since they have identical labels. To support tracking of individual vials, each vial would need a unique barcode. This could in principle be implemented but would require extensive changes in how barcodes are implemented in the industry and for that reason alone would not be practical. Second, in barcode systems inaccurate inventory records need to be reconciled by periodic manual counting. This makes very frequent (or continuous) inventory review uneconomical and precludes automatic ordering based on accurate inventory status. So we view the RFID-enabled cabinet with the supporting software and interfaces as an integral technology and use the term RFID to refer to the entire system.

The key differences between barcode technology and RFID technology. (Source: Çakıcı et al. [7] and Hedgepeth [21]).

<table><tr><td>Feature</td><td>Barcode</td><td>RFID</td></tr><tr><td>Line of sight*</td><td>Needed</td><td>Not needed</td></tr><tr><td>Simultaneous Multiple Reads</td><td>No</td><td>Yes</td></tr><tr><td>Unique Id*</td><td>No</td><td>Yes</td></tr><tr><td>Data Storage Capacity*</td><td>Low</td><td>High</td></tr><tr><td>Security</td><td>Low</td><td>High</td></tr><tr><td>Durability</td><td>Low</td><td>High</td></tr><tr><td>Tracking*</td><td>Periodic</td><td>Real-time</td></tr><tr><td>Human error</td><td>A concern</td><td>No</td></tr><tr><td>Inventory counting and reordering*</td><td>Manual</td><td>Automatic</td></tr><tr><td>Update on expiration date*</td><td>No</td><td>Yes</td></tr></table>

\*The focus of this research is on these features of RFID.

## 4. Inventory models

In this section, we formulate models to analyze periodic and continuous review policies for monitoring the inventory of a single item. While barcode technology forces an inventory manager to use a periodic review policy, RFID renders continuous review possible. We model regular consumer demand as a continuous stochastic process with stationary and independent increments with mean λ and instantaneous standard deviation σ. As barcodes require the use of a periodic review policy, shrinkage (caused by expiration of partially used content) is modeled as an additional source of demand for the periodic review model. Shrinkage demand is assumed to be deterministic at a rate proportional to the average inventory on hand. Alternative assumptions would be a shrinkage rate that is a more general function of average inventory on hand and/or the demand rate. Since we calibrate the model shrinkage demand to match the observed shrinkage under the periodic review policy in use with the barcode system, this assumption does not affect comparisons between models for the RFID-enabled systems (which exhibit no shrinkage at all) and the actual system performance before implementation. We denote the sum of the regular and shrinkage demand rates by <sup>˜</sup>λ and the total demand (regular and shrinkage) during the interval $\left( t _ { 1 } , t _ { 2 } \right]$ by $D ( t _ { 1 } , t _ { 2 } ] .$

The lead time L is a positive constant, and any shortages are backordered. Inventory holding costs are incurred continuously over time at a rate equal to h times the inventory on hand, and backorder costs are incurred continuously at a rate equal to b times the backorder level. Finally, the <sup>fi</sup>xed cost per order placed is g and $g _ { R }$ for barcode and RFID, respectively where $g _ { B } - g _ { R }$ can be interpreted as the manual counting cost avoided by the use of RFID. We assume that the inventory manager is risk neutral and hence aims to minimize the long-run average inventory cost. In the next two subsections, we discuss the periodic review base stock (R,S) policy and the continuous review order point-order quantity (s,Q) policy.

## 4.1. Periodic review base stock (R,S) policy (PR)

The periodic review base stock policy has two parameters: R is the time between two consecutive inventory reviews, and S is the orderup-to or base stock level. At an inventory review instance τ, an order is placed for $S - I P ( \tau )$ units of product, where $I P ( \tau )$ is the inventory position (=inventory on hand plus the amount on order minus outstanding backorders) at time τ.

For the order placed at time $\tau ,$ the demand during its lead time is $D _ { L } = D ( \tau , \tau + L ]$ . To the order placed at time τ we assign the inventory holding and backorder costs incurred during the interval $[ \tau + L , \tau + L + R )$ . Let t be an arbitrary moment in this interval. Since every order placed at or before time τ will have arrived by time $\tau { + } L$ and no order placed after time τ arrives before time $\tau + L + R ,$ the inventory level at time $t , I ( t ) ,$ , is equal to $S - D ( \tau , t ) = S - D _ { L } - D _ { \theta } ,$ where $D _ { \theta } { = } D ( \tau { + } L , \tau { + } L { + } \theta ] ,$ , and $\theta { = } t { - } \left( \tau { + } L \right)$ is uniformly distributed over $( 0 , R ) .$ . Note that $D _ { L }$ and $D _ { \theta }$ are independent random variables since they represent the random demands over disjoint intervals of time. Fig. 1 illustrates the behavior of I(t) under the periodic review policy.

Now let $\tilde { D } = D _ { L } + D _ { \Theta } ,$ . The expected values of the inventory on hand and the backorder level are then $E { \left( S - \tilde { D } \right) } ^ { + }$ and $E \big ( \tilde { D } - S \big ) ^ { + }$ respectively. We assume that an order is placed after every inventory review, so the order frequency is 1/R. We assume that shrinkage is roughly proportional to inventory on hand and de<sup>fi</sup>ne the proportionality constant as γ. So, assuming that shrinkage is deterministic, its rate is $\gamma E \big ( S - \tilde { D } \big ) ^ { + }$ , and the effective demand rate $\tilde { \lambda } = \lambda +$ $\gamma E \Big ( S - \tilde { D } \Big ) ^ { + }$ and the direct cost from shrinkage is $\gamma c E { \bigl ( } S - { \tilde { D } } { \bigr ) }$ + , where c is the cost of a vial. Therefore, we can write the total long-run average cost as

$$
P R C (R, S) = (h + \gamma c) E (S - \tilde {D}) ^ {+} + b E (\tilde {D} - S) ^ {+} + (1 / R) g _ {B}.
$$

Note, however, that evaluating $E \big ( S { - } \tilde { D } \big ) ^ { + }$ involves solving an equation, since the mean and standard deviation of $\tilde { D }$ are functions of $\tilde { \lambda } = \lambda + \gamma E \Big ( S - \tilde { D } \Big ) ^ { + }$ <sup>þ</sup>. In our numerical work we assume that D<sup>˜</sup> is normally distributed, with mean $\tilde { \mu } ( R ) = E ( D _ { L } + D _ { 6 } ) = \tilde { \lambda } ( L + R / 2 )$ and variance $\tilde { \sigma } ^ { 2 } ( R ) = \nu a r ( D _ { L } + D _ { 6 } ) = \sigma ^ { 2 } L + \sigma ^ { 2 } R / 2 + \tilde { \lambda } ^ { 2 } R ^ { 2 } / 1 2 .$ Note that ${ \tilde { \mathbf { O } } } ^ { 2 } ( R )$ is also the variance of I(t) for PR. Our experience shows that a simple iterative scheme with initial estimate $E \Big ( S - \tilde { D } \Big ) ^ { + } = 0$ works quite well in evaluating PRC(R,S). Theorem 1 characterizes the convexity properties of PRC(R,S) assuming no shrinkage.

Theorem 1. Assume $\gamma = 0 . \ I f \ \wedge L > 0 . 7 5 \frac { \mathrm { { g } } ^ { 2 } } { \lambda }$ then PRC(R,S) is jointly convex in S and R.

The condition in Theorem 1 states that the lead time demand must be larger than 75% of the variance to mean ratio of the demand process. This condition is generally satis<sup>fi</sup>ed except for very slow moving items. Thus, when demand is Poisson, $\sigma ^ { 2 } = \lambda$ and $\lambda L { > } 0 . 7 5$ ensure that Newton's algorithm will converge to $R ^ { * }$ very quickly.

![](/api/attachments/RX3SEVG2/fulltext/images/4b3b75275c5f8deba0103f3ef1e0cf58ed44e317b2a3e5130743c4c2f7470778.jpg)  
Fig. 1. Inventory level distribution, I(t), for PR.

## 4.2. Continuous review order point-order quantity (s,Q) policy (CR)

In the continuous review order point-order quantity policy, the inventory position (again de<sup>fi</sup>ned as inventory on hand plus the amount on order minus backorders) is monitored continuously. Whenever the inventory position drops to the order point s an order for the order quantity $Q$ is placed. It is well known (see, e.g., Hadley and Whitin [20]) that under this policy the inventory position at an arbitrary point in time $t - L$ is uniformly distributed between s and $S = s + Q .$ . Hence the inventory level at time t, I(t), when all replenishment orders placed up to and including time $t - L$ but none of the orders (if any) placed after time t−L has been delivered, is distributed as $S - U - D _ { L }$ , where $U { \sim } U n ( 0 , Q )$ is independent of $D _ { L } = D ( t - L , t ] .$ Fig. 2 illustrates the behavior of $I ( t )$ under the continuous review policy.

Let $\dot { \cal D } = { \cal D } _ { \cal L } + U .$ In order to simplify the analysis, we assume that $\dot { D }$ is normally distributed, with mean $\dot { \mu } ( Q ) = E \dot { D } = \lambda L + Q / 2$ and variance $\dot { \sigma } ^ { 2 } ( Q ) = \nu a r \dot { D } = \sigma ^ { 2 } L + Q ^ { 2 } / 1 2$ . Note that $\dot { \sigma } ^ { 2 } ( Q )$ is also the variance of I(t) for CR. The expected values of the inventory on hand and the backorder level at an arbitrary point in time are then $E { \left( S - \dot { D } \right) } ^ { + }$ and $E \Big ( \dot { D } - S \Big ) ^ { + }$ , respectively, and the order frequency is given by λ/Q [20]. Hence, we can write the total long-run average cost as

$$
C R C (S, Q) = h E \Big (S - \dot {D} \Big) ^ {+} + b E \Big (\dot {D} - S \Big) ^ {+} + (\lambda / Q) g _ {R}.
$$

Since continuous review is only practical after RFID is implemented and RFID reduces shrinkage to negligible amounts, evaluating $C R C ( S , Q )$ is straightforward. Moreover, since $C R C ( S , Q )$ is jointly convex in S and Q (see Lemma 1 in Zheng [45]), <sup>fi</sup>nding the optimal continuous review order point-order quantity policy is easy.

## 4.3. Comparison of periodic review and continuous review policies

In this section, we analytically compare the periodic and continuous review policies when there is no shrinkage $( \mathrm { i } . \mathsf { e } . , \gamma = 0 )$ . We will consider the impact of shrinkage numerically in the next section. Proposition 1 below summarizes the important economic and operational differences between the two policies.

Proposition 1. Assume $\gamma { = } 0 ~ ( i . e .$ ., no shrinkage) and $g _ { B } = g _ { R }$ (i.e. the fixed cost of ordering is the same for barcode technology and RFID). All the following performance measures are larger for the optimal periodic review policy than for the optimal continuous review policy: the average inventory on hand, the average backorder level, the variability of the inventory level, the order frequency, and the total long-run average cost.

All the proofs in this paper are given in Çakıcı et al. [9]. Proposition 1 provides important managerial insights. It shows that RFID is best leveraged when it is used with continuous review. Moreover, if the reorder frequency before RFID was set exogenously (and therefore likely sub-optimally), the cost savings achievable with RFID go up even more. In fact, in many cases inventory managers do not optimize the review period in order to follow a regular schedule of reviewing and reordering items. Proposition 1 shows that switching from a periodic to a continuous review policy reduces the total long run average cost by reducing all three cost categories (inventory holding costs, backorder costs, and ordering costs). Hence, Proposition 1 illustrates that to achieve the full bene<sup>fi</sup>ts from a new technology (such as RFID), the supporting inventory policy should be redesigned.

![](/api/attachments/RX3SEVG2/fulltext/images/efcc5c4119a25312d21ebab9dcb59517a18db59911d2c137b718bff1fc819ed2.jpg)  
Fig. 2. Inventory level distribution, I(t), for CR.

In practice, the introduction of RFID has two additional consequences. First, the <sup>fi</sup>xed cost of placing an order is likely to be lower with RFID than with barcode technology. Hence under RFID one would tend to place more frequent orders, leading to a reduction in both average inventory and backorders. Second, shrinkage is likely to be greatly reduced under RFID, which decreases the effective cost of holding inventory, so more inventory will be carried and the service level improved. Proposition 2 below shows the impact of the <sup>fi</sup>xed cost of ordering to account for the bene<sup>fi</sup>t of automatic counting under RFID.

Proposition 2. Assume $\gamma { = } 0 ~ ( i . e .$ , no shrinkage). Then the following holds for the optimal continuous and periodic review policies:

a) The optimal average ordering quantity is concave increasing in the fixed cost per order.

b) The ratio of average inventory (backorder) costs to the average ordering cost is convex decreasing in the optimal average order quantity and in the fixed cost per order.

According to Proposition 2, when the system uses automatic counting (i.e., the <sup>fi</sup>xed cost per order decreases), the optimal average order quantity decreases, decreasing the total inventory related costs. Furthermore, a decrease in the <sup>fi</sup>xed cost per order increases the ratio of the inventory-related costs to the average ordering cost, which means that the average ordering cost also decreases, and this decrease is proportionally larger than the decrease in the inventory-related costs. All in all, a decrease in the <sup>fi</sup>xed ordering cost decreases the average holding, backorder, and ordering costs, so the results in Proposition 1 still hold after switching from barcode (manual counting and PR) to RFID technology (automatic counting and CR), except that the optimal order frequency increases.

Proposition 2 shows that a change in the <sup>fi</sup>xed ordering cost affects PR as it does CR. Note that RFID technology enables the use of both PR and CR, so PR results in performance improvements that are similar but slightly smaller than those provided by CR.

## 5. Numerical analysis

We analyze the radiology inventory system under three scenarios: (1) barcode technology with optimal periodic review base stock policy; (2) RFID with unchanged processes (this means the <sup>fi</sup>xed cost of ordering is reduced to $g _ { R } ,$ but the inventory control policy and shrinkage are as in (1)); and (3) RFID with BPR (this means that the <sup>fi</sup>xed cost of ordering is reduced to $g _ { R } ,$ shrinkage is eliminated, and the optimal continuous review order point-order quantity policy is used). These scenarios are summarized in Table 2.

The radiology practice serves an average of 44 patients daily and operates 7 days/week. On average, 60% of these patients need a contrast media injection. The practice uses 100 cc (pharmacy bulk pack) contrast media vials, each of which can be used on average for seven images. The cost of a vial is \$240, and it has a shelf life of up to two years. Once a vial is opened, however, it expires within a day. When the practice uses barcode technology, it loses 1.42% of its daily average inventory on hand to shrinkage. Note that the two-year shelf life almost guarantees that shrinkage does not occur unless a vial is opened. We therefore assume that shrinkage from an unopened vial is zero.

Table 2  
Scenarios analyzed.

<table><tr><td>Scenario</td><td>Counting</td><td>Shrinkage</td><td>Inventory policy</td></tr><tr><td>Barcode</td><td>Manual</td><td>Yes</td><td>Periodic review</td></tr><tr><td>RFID alone</td><td>Automatic</td><td>Yes</td><td>Periodic review</td></tr><tr><td>RFID + BPR</td><td>Automatic</td><td>No</td><td>Continuous review</td></tr></table>

Table 3  
Parameter values in the practice.

<table><tr><td>L=3 days</td><td>h=$0.34/vial/day</td><td>gB=$500/order</td></tr><tr><td>λ=3.8/day</td><td>b=$142.86/vial/day</td><td>gR=$300/order</td></tr><tr><td>σ=√λ(≈1.95)</td><td>c=$240/vial</td><td>γ=1.42%/day</td></tr></table>

When it used barcode technology, the practice reviewed its inventory and reordered vials every Friday (i.e., every $R { = } 7 \mathrm { d a y s } )$ with delivery on the following Monday $( { \mathrm { i . e . , } } L = 3 { \mathrm { d a y s } } )$ . The practice used a base stock level of $S = 4 5$ vials. Our model shows that the optimal values are $R = 7 . 0 3$ days and $S = 4 5 . 0 2$ vials. Therefore, the practice followed the optimal policy when it used barcode technology.

Regulations require that contrast media be held in locked storage cabinets with limited space, which leads to an annual inventory holding cost of 52%. Hospitals and similar facilities face exceedingly high shortage costs. When the radiology practice is out of stock, it incurs a \$1000 backorder cost per vial per week. This cost is an estimate of the managerial effort of expediting a shipment and a potential loss of income due to an unused imaging slot. Ordering costs are also typically high in hospitals. The practice incurs \$500/order placed to cover manual counting, reordering, shipping and receiving, replenishment, paying the invoice, and all the transportation from the receiving dock to the pharmacy onto the hospital <sup>fl</sup>oor. RFID technology, however, eliminates the manual counting cost, which amounts to \$200 on average, and hence decreases the ordering cost per order placed to \$300. Therefore, we have $g _ { B } = \$ 500$ and $g _ { R } = \$ 300$ We assume that the standard deviation of demand $\begin{array} { r } { \sigma = \sqrt { \lambda } \ ( \mathrm { e . g . } } \end{array}$ demand follows a Poisson process). The parameters and their values are summarized in Table 3.

The parameter $z = b / ( b + h ) = 0 . 9 9 7 6$ gives the optimal fraction of time that the system has no backorders when there is no shrinkage, and can be seen as a measure of the service that the system needs to provide, while $z _ { S } = b / ( b + h + \gamma c ) = 0 . 9 7 4 4$ is an approximation to the optimal fraction of time that the system has no backorders when there is shrinkage. Clearly, one of the consequences of shrinkage is to reduce the optimal service level provided.

![](/api/attachments/RX3SEVG2/fulltext/images/a673bfb73705d649c8b92abe12b407be26dbd863833d2142a186d2e42d7a4093.jpg)  
Fig. 3. Long-run average cost of inventory w.r.t. b.

![](/api/attachments/RX3SEVG2/fulltext/images/de53d53a4bd766c7b0630f8887736bdd859e09a4f778546c3a3208351766df25.jpg)  
Fig. 4. % cost savings w.r.t. b.

## 5.1. Sensitivity analysis with respect to b

In this section, we illustrate the sensitivity of the long-run average cost of inventory with respect to the backorder cost b. We vary b from h to \$145/day while keeping h constant. We take this approach rather than varying h $_ { 0 \Gamma z }$ because b is generally more dif<sup>fi</sup>cult to measure than h. Fig. 3 shows the long-run average inventory cost for the three scenarios in Table 2, while Fig. 4 shows the savings (expressed as a percentage of the total cost in the barcode scenario) that can be achieved by moving from barcode technology to RFID, from RFID to RFID+BPR, and from barcode technology to RFID+BPR. For all three scenarios, the total cost increases in a concave manner, roughly corresponding to the concave increase in z and $z _ { S }$ as b increases. The percentage saved over barcode technology by implementing RFID is (slightly) decreasing in a convex manner, while the savings from also implementing BPR at <sup>fi</sup>rst rapidly increase and then largely level out.

We also see that total cost increases faster in the barcode and RFIDalone scenarios. This is caused by the additional shrinkage, which is a function of the average inventory on hand. Therefore, as inventory on hand is increased in order to reduce the average backorder level when b increases, increased shrinkage occurs unless BPR is implemented as well. This fact and the fact that continuous review can achieve the same service level as periodic review with lower average backorder levels and less inventory lead to larger savings with BPR, as the service level increases (Fig. 4). Moreover, as b increases, the savings from automatic counting become less important than the bene<sup>fi</sup>ts of BPR. The importance of implementing BPR in addition to investing in RFID is illustrated by the fact that about 75% of the total achievable savings are due to BPR.

Fig. 5 illustrates how the average inventory on hand, backorder level, and order frequency vary with the optimal service level $z = b / ( b + h )$ when b is varied from h to \$142.86/vial/day (=the prevailing backorder cost per vial per day) for the optimal periodic review and continuous review policies, assuming there is no shrinkage and <sup>fi</sup>xed order costs are equal to $g _ { R } .$ For both policies, the order frequency decreases when b increases to lower uncertainty, especially when using the periodic review policy, but the difference is quite small. The largest difference between the periodic and the continuous review policy is in the holding cost incurred. Fig. 5 illustrates some of the results in Proposition 1, viz. CR holds less inventory, incurs less backorders, and orders less frequently.

5.2. Sensitivity analysis with respect to lead time, fixed cost of ordering under RFID, demand rate, and demand variability

In this section, we illustrate the behavior of the percentage cost savings in the long-run average cost due to RFID and BPR for different values of L in Fig. $6 , g _ { R }$ in Fig. 7, λ in Fig. 8, and σ in Fig. 9. The values of the other parameters are given in Table 3.

In Fig. 6, we vary the lead time L from 0 to 15 days. As the lead time increases, we see that the percentage savings in total cost from RFID alone decreases, while that from RFID+BPR increases. Overall, the percentage savings are relatively insensitive to a change in the lead time, though.

In Fig. 7, we vary the <sup>fi</sup>xed cost of ordering under RFID, $g _ { R } ,$ from 0 to 500. The increase in $g _ { R }$ corresponds to a decrease in the manual counting cost. The savings from RFID alone vanish as $g _ { R }$ reaches $g _ { B } =$ \$500 as the manual counting cost falls to zero. Since the optimal policy and its cost in the barcode scenario do not depend on $g _ { R } ,$ while the cost of the optimal policy under RFID and RFID+BPR increases with $g _ { R } ,$ the cost savings from RFID and RFID+BPR decrease with g . Interestingly, the bene<sup>fi</sup>t of adding BPR when RFID has already been implemented does increase signi<sup>fi</sup>cantly with the <sup>fi</sup>xed cost of ordering under RFID. Overall, a switch to RFID technology with BPR is more likely to pay off when manual counting costs are high (i.e., when g is low).

![](/api/attachments/RX3SEVG2/fulltext/images/b96c1812994eac9ac89d54da2fb0f88c4f6b07090346a41488075849962251ab.jpg)  
Fig. 5. Average inventory on hand, backorder level, and order frequency under optimal periodic and continuous review policies, assuming no shrinkage and <sup>fi</sup>xed order costs equal to g<sub>R</sub>.

![](/api/attachments/RX3SEVG2/fulltext/images/22fc1fe7a91a71d7e7a81b6afaa16df9201ebe65a2d7bc784ae1b5439c99f4dc.jpg)  
Fig. 6. % cost savings w.r.t. L.

In Fig. 8, we set $\sigma { = } 0 . 5 \lambda$ while varying λ from 1 to 20 vials/day. We <sup>fi</sup>x the coef<sup>fi</sup>cient of variation of demand in order to eliminate the effect of the relative decrease in σ while λ increases that occurs under Poisson demand since $\sigma = \sqrt { \lambda }$ . Clearly, the demand rate now has a relatively small impact on the savings achieved by RFID alone and by RFID+BPR.

In Fig. 9, we vary σ from 0 to 10 while keeping mean demand <sup>fi</sup>xed. Since an increase in the standard deviation of demand requires more inventory to be carried to meet a given service level, shrinkage will increase at the same time with barcode technology and with RFID alone, and the bene<sup>fi</sup>cial impact of BPR grows with increasing demand uncertainty. A comparison with Fig. 8 shows that the impact on savings of an increase in the coef<sup>fi</sup>cient of variation while keeping mean demand <sup>fi</sup>xed is somewhat stronger than the impact of increasing the mean demand while keeping the coef<sup>fi</sup>cient of variation <sup>fi</sup>xed.

![](/api/attachments/RX3SEVG2/fulltext/images/a045183a25b3fd713159e22d1b26a7c7d915d95f4466cea289170b990e2780ec.jpg)  
Fig. 7. % cost savings w.r.t. g<sub>R</sub>.

![](/api/attachments/RX3SEVG2/fulltext/images/e965140223b349eb527240fc29831f9a863b6b1000ef54055021647d815cdc42.jpg)  
Fig. 8. % cost savings w.r.t. λ for constant c.v

Overall, the bene<sup>fi</sup>t of RFID+BPR increases with both the demand volume and the demand uncertainty.

## 5.3. Sensitivity analysis with respect to the shrinkage rate

Fig. 10 shows the long-run average inventory cost for the three scenarios in Table 2 for different values of the shrinkage rate γ, while Fig. 11 shows the savings achieved with RFID alone, RFID+BPR and the change from RFID alone to RFID+BPR. In both <sup>fi</sup>gures, we change γ from 0 to 20%/day. For the values of the other parameters whose values do not change, please refer to Table 3.

Clearly, the shrinkage rate has a huge impact. In Fig. 10, costs for barcode technology and for RFID alone increase rapidly when the shrinkage rate increases. The cost for RFID+BPR is constant, since it does not incur shrinkage costs. In Fig. 11, the savings due to RFID alone are small and slowly decreasing in the shrinkage rate. On the other hand, as the shrinkage rate increases, the bene<sup>fi</sup>cial impact of BPR in addition to RFID increases rapidly and approaches 100%. All in all, the shrinkage rate is probably the most signi<sup>fi</sup>cant determinant of the savings that can be achieved with RFID and BPR combined.

## 6. Cost-bene<sup>fi</sup>t analysis of RFID technology

Using the values in Table 3, we <sup>fi</sup>nd that the daily cost of the barcode technology (Barcode) is \$155.31, and the daily cost of RFID+ BPR is \$37.85. Assume that the practice operates for 365 days a year;

![](/api/attachments/RX3SEVG2/fulltext/images/e30df623c29f8ca44b85c12593c297bb2f1b0e46dc51fd6d686272d7314a63e1.jpg)  
Fig. 9. % cost savings w.r.t. σ.

![](/api/attachments/RX3SEVG2/fulltext/images/8c042d0d8274e999d3b132df45e76e6077567733de2114e34ab106c4cb356044.jpg)  
Fig. 10. Long-run average cost of inventory w.r.t. γ.

![](/api/attachments/RX3SEVG2/fulltext/images/a9bc4b3b68377cd170bcfd56492fa70eb658a5f80692bf002dba48cbdb67c4b3.jpg)  
Fig. 11. % cost savings w.r.t. γ.

Table 4 then summarizes the annual values of these costs and also provides the annual value of RFID.

From Table 4 we see that the cost savings for technology improvement (switching from barcodes to RFID alone) amount to 18.33% of the annual cost of the barcode system, while the savings from the business process redesign (switching from RFID alone to RFID+BPR) are 75.63% 18.33%=57.30%.

The radiology practice incurs a one-time installation cost of \$45,000; the computerized storage cabinet and the integration of the software system with local hospital's EMR and Radiology Information Systems (RIS) cost an extra \$15,000. Maintenance and software support services costs amount to approximately \$10,000 annually. The additional cost of labeling the contrast media vials with an RFID tag is typically borne by the vendor. Assuming a technological life expectancy of ten years for the storage cabinet and excluding any costs in support of the old barcode system, we calculate the net present value (NPV) under three discount rates (5%, 10%, and 15%) as well as the internal rate of return (IRR) for the RFID technology. These values are summarized in Table 5. As the NPVs are positive and the IRR value is 54.06%, we can say that investment in RFID technology is very pro<sup>fi</sup>table for the radiology practice.

Table 4  
The annual value of RFID (\$).

<table><tr><td>Barcode</td><td>RFID alone</td><td>RFID + BPR</td><td>Savings from RFID alone</td><td>Savings from RFID + BPR</td></tr><tr><td>$56,687</td><td>$46,299</td><td>$13,815</td><td>$10,388</td><td>$42,872</td></tr></table>

Table 5  
Financial criteria for the RFID technology.

<table><tr><td>Discount rate (%)</td><td>NPV($)</td><td>IRR(%)</td></tr><tr><td>5%</td><td>$193,827.25</td><td>54.06%</td></tr><tr><td>10%</td><td>$141,983.92</td><td></td></tr><tr><td>15%</td><td>$104,975.91</td><td></td></tr></table>

## 7. Discussion and conclusion

Our case study of a radiology practice reveals some very important operational problems that could exist in any hospital setting. RFID technology can eliminate manual inventory processes and hence solve operational problems that exist under barcode technology. More speci<sup>fi</sup>cally, we show that the inventory manager can bene<sup>fi</sup>t from RFID by leveraging automatic counting and continuous review and by tracking shrinkage actively. We analytically show that without shrinkage, the switch to continuous review achieves savings in all three inventory cost categories: inventory holding, backorder, and ordering costs. The long-run average cost of inventory therefore is always lower under continuous review than under periodic review. Moreover, since all three cost components decrease, their corresponding operational metrics, the average inventory on hand, backorder level, and order frequency, respectively, are also lower under continuous review than under periodic review.

The percentage of cost saved by RFID without business process redesign (BPR) decreases in all parameters: service level, backorder cost per item per unit time, lead time, mean and standard deviation of demand, shrinkage rate, and ordering cost per order placed under RFID. The decrease occurs because the inventory policy is not optimal with respect to the new technology and shrinkage is not addressed, and as the parameters increase, these two effects become stronger. In other words, the value of BPR increases in all policy parameters.

The value of RFID combined with BPR increases in all policy parameters except for cost per order under RFID. A switch to RFID therefore should always be accompanied by BPR, as it is then more likely to pay for itself in an environment with high service levels, high shortage costs, high uncertainty, high demand, long lead times, high shrinkage rates and high manual counting costs.

We <sup>fi</sup>nd that, for the radiology practice, the value of RFID combined with BPR is 75.63%, where the major part, 57.30%, is a result of business process redesign and the remaining 18.33% stems from elimination of the cost of manual counting. Hence, optimizing operational policies after implementing RFID provides the major cost savings. Clearly, a redesign of operational processes should always accompany a new technology to get the full bene<sup>fi</sup>ts. Our cost-bene<sup>fi</sup>t analysis shows that hurdle rates of 5%, 10%, and 15% give highly positive net present values and the internal rate of return (IRR) of the investment in RFID and BPR is 54.06%. The RFID technology therefore is highly pro<sup>fi</sup>table for the radiology practice.

The bene<sup>fi</sup>ts of RFID are more pronounced every day, but there are still many concerns for RFID implementation: high installation and maintenance costs, the network effect of barcodes, technical problems (e.g., less than 100% readability), lack of industrial standards, privacy and data security issues, lack of management support, etc. [22,28,31,40]. Nevertheless, as more companies start to use the technology, the cost of implementation should decline due to economies of scale. Moreover, as common standards and regulations take hold, compatibility issues among different systems used by different companies should be resolved, and this will further facilitate adoption. Also, particular sectors such as healthcare that require tracking and monitoring of high-value items have more opportunity to reap bene<sup>fi</sup>ts from RFID technology since costs and potential savings are relatively high in these sectors.

While our research identi<sup>fi</sup>es and quanti<sup>fi</sup>es some important bene<sup>fi</sup>ts of using RFID, there are many other areas that also require signi<sup>fi</sup>cant attention. Consider, for example, the shipping and delivery problems distributors face. These problems mostly occur because existing systems cannot detect errors in the delivery system and identify a package sent to the wrong customer, or because employees experience barcode scanning problems and thus record inaccurate information, yielding discrepancies in delivery data. When items are tagged by RFID, they can be tracked easily, and warning systems can be implemented to ensure correct shipments. Another area where RFID can be useful is manufacturing. According to a recent study (Kalorama [24]), “The approximate cost of launching a particular drug (in a period of more than 12 years) is approximately \$800 million.” RFID can help reduce clinical trial times by minimizing data errors, increasing timely information, eliminating paper work, and decreasing inventory-related problems. We expect to address some of these areas and relevant issues in our future research.

## Appendix A. Notation

λ mean demand per unit time.

$\sigma$ instantaneous standard deviation of demand.

$\tilde { \lambda }$ effective mean demand per unit time (includes shrinkage demand).

$\gamma$ shrinkage rate.

b backorder cost per item per unit time.

h holding cost per item per unit time.

g<sub>i</sub> ordering cost per order placed for technology i=B or R, where B = Barcode and $R = \mathbb { R } \mathbb { F } \mathbb { D }$

$D ( t _ { 1 } , t _ { 2 } ]$ random demand between time $t _ { 1 }$ and $t _ { 2 } ,$ where demand at time $t _ { 1 }$ is not included.

z service level without shrinkage = fraction of time with stock on hand without shrinkage.

IP(t) inventory position (=amount in inventory plus amount on order minus backorders) at time t.

R the time between two consecutive inventory review-andorder epochs in the periodic review model.

S order up-to-level or base stock level (periodic review model) or $s + Q$ (continuous review model).

$\tau$ a review instance in the periodic review model.

Q <sup>fi</sup>xed reorder quantity in the continuous review model.

s the reorder point in the continuous review model.

PRC(R,S) long-run average cost of inventory under a periodic review policy with given R and S.

CRC(S,Q) long-run average cost of inventory under a continuous review policy with given Q and S.

## References

[1] M. Amini, F.O. Otondo, B.D. Janz, M.G. Pitts, Simulation modeling and analysis: a collateral application and exposition of RFID technology, Production and Operations Management 16 (5) (2007).

[2] A. Atalı, H.L. Lee, Ö. Özer, If the Inventory Manager Knew: Value of RFID under Imperfect Inventory Information, Social Science Research Network, September 2009.

[3] M. Barratt, T. Choi, Mandated RFID and institutional responses: cases of decentralized business units, Production and Operations Management 16 (5) (2007).

[4] A. Bensoussan, M. Cakanyildirim, S.P. Sethi, Partially observed inventory systems: the case of zero balance walk, SIAM Journal on Control and Optimization 46 (1) (2007).

[5] G. Cachon, A.G. Kök, Implementation of the newsvendor model with clearance pricing: how to (and how not to) estimate a salvage value, Manufacturing Service Operations Management 9 (2) (2007).

[6] Ö.E. Çakıcı, A. Seidmann, Using RFID in Medical Imaging, Hospital Management (2008), Available at: http://www.hospitalmanagement.net/features/feature1762/. Accessed on 02/28/2010.

[7] Ö.E. Çakıcı, H. Groenevelt, A. Seidmann, A case inquiry: can r<sup>fi</sup>d help reduce costs in medical imaging? Radiology Business Journal 2 (2) (2009) 50–52

[8] Ö.E. Çakıcı, H. Groenevelt, A. Seidmann, Ef<sup>fi</sup>cient inventory management by leveraging RFID in service organizations, proceedings of the 43th Hawaii International Conference on System Sciences, HICSS, Kauai, Hawaii, 2010.

[9] Ö.E. Çakıcı, H. Groenevelt, A. Seidmann, The impact of RFID on radiology pharmaceuticals management—modeling framework and case study, Working Paper, University of Rochester, Feb 2010.

[10] F. Cheng, Y.M. Lee, Y.T. Leung, Exploring the impact of RFID on supply chain dynamics, Proceedings of the Winter Simulation Conference, Volume 2, Washington DC, 2004.

[11] N. DeHoratius, A. Raman, Inventory record inaccuracy: an empirical analysis, Management Science 54 (4) (2008).

[12] N. DeHoratius, A. Mersereau, L. Schrage, Retail inventory management when records are inaccurate, Manufacturing and Service Operations Management 10 (2) (2006).

[13] D. Delen, B.C. Hardgrave, R. Sharda, RFID for better supply-chain management through enhanced information visibility, Production and Operations Management 16 (5) (2007).

[14] A. Dutta, H.L. Lee, S. Whang, RFID and operations management: technology, value, and incentives, Production and Operations Management 16 (5) (2007).

[15] E. Fleisch, C. Tellkamp, Inventory inaccuracy and supply chain performance: a simulation study of a retail supply chain, International Journal of Production Economics 95 (3) (2005).

[16] J.R. Freeland, E.L. Porteus, evaluating the effectiveness of a new method for computing approximately optimal (s, S) inventory policies, Operations Research 28 (2) (1980).

[17] G. Gallego, New bounds and heuristics for (Q, r) policies, Management Science 44 (2) (1998).

[18] H. Groenevelt, Simple inventory heuristics, Working Paper, University of Rochester, Feb. 2010.

[19] H. Groenevelt, N. Rudi, A base stock inventory model with possibility of rushing part of order (unabridged version), Technical Report, University of Rochester, 2002.

[20] G. Hadley, T.M. Whitin, Analysis of Inventory Systems, Prentice Hall Inc., New Jersey, 1963.

[21] W.O. Hedgepeth, RFID Metrics: Decision Making Tools for Today's Supply Chains, CRC Press, Boca Raton, FL, 2006

[22] H.S. Heese, inventory record inaccuracy, double marginalization, and RFID adoption, Production and Operations Management 16 (5) (2007).

[23] A. Jain, H. Groenevelt, N. Rudi, Continuous review inventory model with dynamic choice of two freight modes with <sup>fi</sup>xed costs, Manufacturing and Service Operations Management 12 (1) (2010).

[24] Kalorama Information, RFID in Pharmaceutical Manufacturing, Kalorama Information, Company Report, 2008.

[25] Y. Kang, S.B. Gershwin, Information inaccuracy in inventory systems—stock loss and stockout, Working Paper, MIT, 2004

[26] O. Karaer, H.L. Lee, Managing the reverse channel with RFID-enabled negative demand information, Production and Operations Management 16 (5) (2007).

[27] A.G. Kök, K.H. Shang, Inspection and replenishment policies for systems with inventory record inaccuracy, Manufacturing and Service Operations Management 9 (2) (2007).

[28] C.H. Kuo, H.G. Chen, The critical issues about deploying RFID in healthcare industry by service perspective. Proceedings of the 41st Annual Hawaji International Conference on System Sciences. Hawaii, 2008

[29] H.L. Lee, Ö. Özer, Unlocking the value of RFID, Production and Operations Management 16 (1) (2005).

[30] Y. Li, A. Lim, B. Rodrigues, Note — Pricing and Inventory Control for a Perishable Product MANUFACTURING & SERVICE OPERATIONS MANAGEMENT8 published online before print October 7, 2008, doi:10.1287/msom.1080.0238.

[31] V. Matta, C. Moberg, The development of a research agenda for RFID adoption and effectiveness in supply chains, Issues in Information Systems 7 (2) (2006).

[32] A. Merry, C. Webster, J. Weller, S. Henderson, B. Robinson, Evaluation in an anaesthetic simulator of a prototype of a new drug administration system designed to reduce error, Anaesthesia 57 (2002).

[33] G.E. Monahan, N.C. Petruzzi, W. Zhao, The dynamic pricing problem from a newsvendor's perspective, Manufacturing Service Operations Management 6 (4) (2004).

[34] S. Nahmias, Perishable inventor theory: a review, Operations Research 30 (4) (1982).

[35] N.C. Petruzzi, M. Dada, Pricing and the newsvendor problem: a review with extensions, Operations Research 47 (2) (1999).

[36] P.G. Prastacos, Blood inventory management: an overview of theory and practice, Management Science 30 (7) (1984).

[37] F. Raafat, Survey of literature on continuously deteriorating inventory models, The Journal of the Operational Research Society 42 (1) (1991).

[38] U. Rao, Properties of the periodic review (R, T) inventory control policy for stationary, stochastic demand, Manufacturing and Service Operations Management 5 (1) (2003).

[39] N. Rudi, H. Groenevelt, T.R. Randall, End-of-period vs. continuous accounting of inventory-related costs, Operations Research 57 (6) (2009).

[40] A. Sharma, A. Citurs, B. Konsynski, Strategic and institutional perspectives in the adoption and early integration of Radio Frequency Identi<sup>fi</sup>cation (RFID), Proceedings of the 40th Hawaii International Conference on System Sciences, Hawaii, 2007.

[41] J.G. Szmerekovsky, V. Tilson, J. Zhang, Pricing and allocation of retail space with one RFID enabled supplier and one non-RFID enabled supplier, International Journal of Revenue Management 3 (1) (2009).

[42] G.J.J. Van Zyl, Inventory Control for Perishable Commodities, Unpublished Ph.D. dissertation, University of North Carolina, Chapel Hill, N.C. (1964)

[43] F.A. Veinott Jr., The optimal inventory policy for batch ordering, Operations Research 13 (3) (1965).

[44] J. Whitaker, S. Mithas, M.S. Krishnan, A <sup>fi</sup>eld study of RFID deployment and return expectations, Production and Operations Management 16 (5) (2007).

[45] Y. Zheng, On properties of stochastic inventory systems, Management Science 38 (1) (1992).

[46] H.P. Zipkin, Foundations of Inventory Management, McGraw-Hill Higher Education, New York, 2000.

![](/api/attachments/RX3SEVG2/fulltext/images/f3851adb0be61b95df5639559a49eeb860cf0dc5c3e9e96df8c06c6b5308571b.jpg)

![](/api/attachments/RX3SEVG2/fulltext/images/1388cfefbc47428bda6c60b5f8a93098422bf50c4e1133a8900f2d7ab5f5251d.jpg)

Abraham Seidmann is Xerox Professor of Computers and Information Systems and Operations Management at the William E. Simon Graduate School of Business Administration, University of Rochester. He is the author of over 100 research articles, which appear in many of the leading scienti<sup>fi</sup>c journals, and has been the founding department editor on interdisciplinary management research and applications in Management Science for 10 years. He is also an associate or area editor for IIE Transactions, the International Journal of Flexible Manufacturing Systems, Production Planning and Controls, the Journal of Intelligent Manufacturing, the Journal of Management Information Systems, and Production and Operations Management.

Özden Engin Çakıcı is a Ph.D. Candidate in Operations Management and Information Systems at the W. E. Simon Graduate School of Business Administration at the University of Rochester, Rochester, NY, USA. A native of Turkey he completed his undergraduate studies in Industrial Engineering with a minor in Production at the Middle East Technical University in Ankara, Turkey. After graduation, he worked as a sales engineer for a Danish company and then graduated with an MBA from Bogazici University, Istanbul, Turkey. After joining as a PhD student in University of Rochester, he completed his M.S. in Management Science. He presented his papers in well-known conferences such as Informs, MSOM, RSNA and the Hawaii

International Conference on System Sciences and he also published his papers in the Hawaii International Conference on Systems Sciences and healthcare journals. His research interests include healthcare operations, supply chain management, inventory theory and queuing systems.

![](/api/attachments/RX3SEVG2/fulltext/images/c82b5cd625dc080dec5575564d43270405e391afca792f81d3a77eb45f71605c.jpg)

Harry Groenevelt is Associate Professor of Operations Management at the Simon School of Business, University of Rochester. He holds B.S. and M.S. degrees in Econometrics from the Vrije Universiteit, Amsterdam, and a Ph.D. in Operations Research from Columbia University. His research interests include logistics and supply chain management (including closed loop supply chains, revenue management and contracting), service system management and design, health care operations, and quality management. He has been a consultant on Operations Management issues for numerous manufacturing and service organizations (including hospitals and other health care providers). His articles have been published in

Management Science, Operations Research, MSOM, Transportation Science, EJOR, Production and Operations Management and elsewhere. He is also the author of QMacros and IMacros, Excel add-ins to analyze queueing systems and inventory systems, respectively. He currently serves as co-Chair of the Faculty Senate at the University of Rochester.
