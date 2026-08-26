---
otero_id: 9820
otero_key: "NQW83VRY"
title: "Misplaced product detection using sensor data without planograms"
authors: "Andreas Solti; Manuel Raffel; Giovanni Romagnoli; Jan Mendling"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.06.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Misplaced product detection using sensor data without planograms

ELSEVIE Decision Support Systems

Andreas Solti, Manuel Raffel, Giovanni Romagnoli, Jan Mendling

![](/api/attachments/NQW83VRY/fulltext/images/2bcb5725efc630afb92f4061a578c98d4d3163250d6dc56435bde95e6d82f520.jpg)

PII: S0167-9236(18)30103-9

DOI: doi:10.1016/j.dss.2018.06.006

Reference: DECSUP 12964

To appear in: Decision Support Systems

Received date: 13 February 2018

Revised date: 19 June 2018

Accepted date: 20 June 2018

Please cite this article as: Andreas Solti, Manuel Raffel, Giovanni Romagnoli, Jan Mendling , Misplaced product detection using sensor data without planograms. Decsup (2018), doi:10.1016/j.dss.2018.06.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Misplaced Product Detection Using Sensor Data Without Planograms

Andreas Solti<sup>a</sup>, Manuel Rafel<sup>a</sup>, Giovanni Romagnoli<sup>b</sup>, Jan Mendling<sup>a</sup>

<sup>a</sup>Vienna University of Economics and Business. Welthandelsplatz 1, 1020 Vienna, Austria <sup>b</sup>Universit\`a di Parma. via Universit\`a 12, Parma, Emilia-Romagna, 43121,Italy

## Abstract

Accurate and timely provisioning of products to the customers is essential in retail environments to avoid missed sales opportunities. One cause for missed sales is that products are misplaced in the store. This can be addressed by fast and accurately detecting those misplacements. A problem of current detection methods for misplaced products is their reliance on up-to-date planogram information, which is often missing in practice. This paper investigates the efectiveness and eficiency of outlier detection methods for finding misplaced products without planograms. To that end, we conduct simulation studies with realistic parameters for diferent store parameters and sensor infrastructure settings. We also evaluate the detection methods in a real setting with an RFID inventory robot. The findings indicate that our proposed MiProD aggregation of individual detection methods consistently outperforms individual techniques in detecting misplaced products.

Keywords: Data analysis, Sensors, Outlier detection, Inventory management

## 1. Introduction

A central challenge of daily operations in brick-and-mortar retail shops is the timely and accurate provision of products to the customers. Retailers try to avoid store execution errors, such as out-of-stock and inventory record inaccuracy that jeopardize their performance due to low on-shelf availability and lost sales [13]. Ironically, there are also missed sales opportunities when products are not truly out-of-stock but only out-of-shelf. A product is defined as out-of-shelf when it exists inside the store, thus not out-of-stock, but it cannot be found by a customer willing to purchase it [38]. The out-of-shelf condition has two main causes: (i) replenishment errors, i.e. the product is available in the backroom and not in the sales floor area, and (ii) placement errors, i.e. the product is misplaced somewhere in the sales floor area and it is not where it ought to be [42]. Scientific literature agrees that misplaced items have a nontrivial impact on store performance, as identifying and relocating misplaced items is a dificult and time-consuming activity [1 , 42]

One way to manage the misplaced product detection problem is to set up real-time location systems (RTLS). RTLS continuously infer product positions and movements in real time [50]. Even though diferent RTLS technologies are available, it is often radio frequency identification (RFID) that is used as a locating system technology [15, 44]. However, issues such as misplacements cannot be readily observed in RTLS, but they need to be extracted from raw data. For this knowledge extraction, it is often assumed that complementary information is available, such as planograms [46]. Planograms are layout plans that specify in detail where specific product types shall be placed in a retail store. Although the benefits of planograms have been demonstrated in [11, 7], planograms are hardly systematically and continuously maintained in practice. This means that misplaced product detection with sensor data is required to work even without planogram information. Currently, research into misplacement detection without planograms is missing and it is unclear whether it is feasible with the required level of accuracy.

In this paper, we address the research challenge of detecting misplaced products without planogram information. The proposed approach is called MiProD (Misplaced Products Detection). The goal of MiProD is to detect products misplacements by relying only on potentially noisy RFID sensor readings. To achieve this goal, MiProD systematically compares four diferent analytical methods, namely (i) kNN – k-Nearest Neighbors [22]; (ii) LOF – Local Outlier Factor [6]; (iii) GLOSH - Global-Local Outlier Scores from Hierarchies [9]; (iv) distance [18, p. 538f]. We investigate the accuracy of each of these methods using simulation and a case study from a European fashion retailer. Our results demonstrate the feasibility of misplaced product detection without planograms, both in the simulated environment and in the industrial case. Also, results from the case study suggest that MiProD can achieve a suitable level of accuracy in everyday fashion and apparel retail operations.

The remainder of this paper is structured as follows. Section 2 describes the background of misplaced product detection and relevant technologies. Section 3 describes our conceptual contribution of misplaced product detection without planograms. Section 4 evaluates the method based on simulation experiments and an application in a real-world fashion store. Section 5 critically discusses the implications of this work. Section 6 concludes the paper.

## 2. Background

In this work, we define that a product that is not out of stock, but misplaced in the wrong aisle or location is called misplaced product, cf. Raman et al. [42]. The problem of misplaced product detection can be formulated as an unsupervised classification problem. Given a set of products and their sensed locations, classify each product into (i) misplaced or (ii) not misplaced.

## 2.1. The Problem of Misplaced Product Detection

The problem can be illustrated using the planogram examples shown in Figure 1. To organize its inventory, a retailer groups its assortment according to classes. These classes are ordered such that customers can browse products by class on the sales floor. Assume that there are three product classes on the sales floor: t-shirts, pants, and shoes. In Figure 1a, they are illustrated using triangles, circles, and boxes arranged at diferent locations. Note that products of one class can potentially have multiple positions on the sales floor, where they are displayed (i.e., they can form multiple clusters). When using a sensor infrastructure to locate products, the real positions are not known to the system. In case of RFID-based sensing, reflections from metallic objects, occlusions of other tags, and other disturbances can cause errors in location accuracy and even missingness of tag reads [19]. Figure 1b illustrates that the natural grouping of product classes from the system’s perspective can be blurry at the boundaries of the product groups.

![](/api/attachments/NQW83VRY/fulltext/images/d8becb87d22ddedade20e37535a4b50707000450ccf7f7bc4f28d118bf792121.jpg)  
(a) Original inventory

![](/api/attachments/NQW83VRY/fulltext/images/47481e35d528634131b013132da30bf37ffb830b75cc28c885885b3080ef9f18.jpg)  
(b) Sensed inventory

![](/api/attachments/NQW83VRY/fulltext/images/fe86ddca013308a84cd90ded8ed53d6526546a28cbb4cb977557404027a5e6fe.jpg)  
(c) Inventory with 3 misplacements

![](/api/attachments/NQW83VRY/fulltext/images/904f051ce39c571479668f4645a5ccbc3873259c70d6d8c26e0becedadcae7c3.jpg)  
(d) Sensed inventory w. misplacements  
Figure 1: Conceptual illustration of the misplaced product detection problem.

The identification of the product classes as clusters becomes more dificult when the initial order of products is disturbed, i.e., when some products are misplaced. In Figure 1c, the arrows depict (customer induced) misplacements of three products. Figure 1d shows how the RTLS might sense the inventory with misplacements. Here, the problem is to identify that products 1, 2, and 3 are misplaced from the sensed information in Figure 1d. We identify the following challenges: (i) missing reads (e.g., misplaced product 3 ), (ii) inaccuracies in the sensing infrastructure that blur the product group boundaries, (iii) product groups can have multiple distinct areas where they are placed.

Next, we describe RFID technology as an example that enables sensing of products and look at general purpose solutions for outlier detection. These foundations serve as building blocks for our proposed detection system.

## 2.2. Location Sensing Technologies

RFID and RTLS belong to a rich spectrum of sensor technologies that can be used for location sensing. We refer to the survey by Farid et al. for an overview on indoor localization techniques [20]. We focus on passive RFID tags, which are the most accessible and afordable examples of location sensing technologies.

## 2.2.1. Radio Frequency Identification.

RFID [26, 28] is an acronym for radio frequency identification, a technology for wireless communication that allows us to unequivocally identify objects or people with an assigned tag. It has several applications. For instance, management of supply chains, access control systems or tracking of animals [21].

A system using passive RFID technology is composed of three components: (i) tags with a semiconductor chip and an antenna, (ii) readers that power the tags and read their response signals and relay that data to a (iii) server. Servers connect several RFID readers and centralize the gathered information for processing. We assume that an RFID system is used to monitor the inventory by location sensing. The readers can be fixed, hand-held, or mounted on robots.

## 2.2.2. Location Sensing Methods

Location sensing with RFID can be achieved by multiple means, the most common of which are trilateration [39], fingerprinting (also known as scene analysis) [36], or triangulation [35]. In case of trilateration, multiple readers with known positions receive a signal from the same tag. Typically the received signal strengths would reflect the distance to the tag from the respective readers. Thus, we can find a position on the map corresponding to the signal strengths. In case of fingerprinting, the signal strengths of the readers are memorized as fingerprints at multiple known positions. This is a preliminary calibration step, also known as the of-line stage. In the on-line stage, when a new measurement is gathered from a tag at an unknown position, this new signal strength fingerprint will be compared to the known patterns. Finally, in case of triangulation, we need to know the angles from at least three reading points to a tag to find the best matching location. Some RFID-equipped robots can perform the latter when their sensing antennas are directional, cf. [45]. This increases the accuracy and can save the costs of installing and maintaining a large array of readers. In practice, the trade-of between RTLS and inventory robots is between timeliness and accuracy of the product positions.

## 2.3. Outlier Detection

Outlier detection is the process by which elements that do not share the characteristics of their population are identified. There exists a large body of research dealing with the problem of outlier detection in various domains like spatial data [12, 6, 1] or wireless sensor networks [52]. Here, we limit the discussion to clustering and k-nearest neighbors approaches, because these two approaches are popular and non-model based (i.e. they do not assume or estimate a model that explains data) [52].

• Clustering: Clustering refers to dividing a set of elements into disjoint sets, which are called clusters. Elements are assigned to clusters in such a way that they are more similar to one another (intra-cluster similarity) than to other elements outside of the cluster. Clustering can be used for outlier detection, as elements that are dissimilar to the elements in the identified clusters will not be assigned to a cluster, but remain as outliers.

• k-Nearest Neighbors: Based on a number (k) of the nearest neighbors, we can classify elements as being outliers or not. In the case that the knearest neighbors of an element have another class than the element itself, it can be considered an outlier.

Outlier detection bears the potential to identify misplaced products when they are too far away from products of the same group. We will pursue this idea to investigate if misplaced products can be detected without planograms.

## 2.4. Prior research on misplaced product detection

The topic of misplaced products belongs to the problem areas of out-ofstock situations in retail [16], but on a more general view also applies to other domains, where it is important that certain products are ordered for easier localization, e.g., warehouse management [40]. Prior research on the topic relates to misplaced products, out-of-stock detection, and misplaced product detection.

Managerial considerations of misplaced products. The efects of misplaced products have been captured in mathematical models that show the trade-ofs of adopting RFID sensor systems to avoid misplaced products and other inventory inaccuracies. Examples of such research are [30, 43, 3, 8]. These papers do not focus on actually detecting single misplaced products, but rather investigate the relationships between aggregates like inventory count frequency, profit, RFID tag costs, and others. Kang and Gershwin investigate how small stock loss impacts the replenishment process [30]. Rekik et al. [43] analyze three scenarios: (i) where the retailer is unaware of inventory errors, (ii) where a retailer is aware of inventory errors and optimizes operations to take that into account, and (iii) where the retailer knows through RFID-based systems about the errors and is able to eliminate these. Atali et al. [3] specifically separate the sources of inventory inaccuracies in their model into misplacements, shrinkage, and transaction errors. Camdereli and Swaminathan investigate economic considerations of the players involved in RFID adoption to remove ineficiencies by misplaced inventory [8]. In these works the simplifying assumption is mostly that inventory inaccuracies can be avoided with the introduction of RFID. In reality, the RFID technology is prone to inaccuracies that impact the replenishment process [49].

Out-of-stock detection. Products being out of stock is a pressing problem causing missed sales opportunities. Several researchers have addressed detection of out-of-stock situations [38, 34, 37]. Papakiriakopoulos et al. [38] rely on a heuristic rule based approach to detect missing products, as at that time they judged RFID to be not yet operational for this purpose. Li et al. [34] focus on improving the detection rate of RFID systems on a technical sensor level to identify missing products and distinguish those from products that are there, but hidden to the system through the problem of tag collisions during read. Papakiriakopoulos and Georgios [37] investigate classification accuracies of machine learning models trained with data collected from RFID systems to detect out of shelf situations. Out of shelf situations are inferred from only limited RFID-enabled interaction points such as the replenishment gate or the point of sales. In contrast, we assume that a location sensing system is in place and we are interested in finding concrete misplaced products.

Table 1: Overview of prior research on misplaced product detection

<table><tr><td rowspan="2" colspan="2">Category:</td><td rowspan="2">Focus:</td><td rowspan="2">decision making[43, 3, 8]</td><td rowspan="2">operational (OOS)[38, 34, 37]</td><td colspan="4">operational(mispl. prod. detection)</td></tr><tr><td>[7]</td><td>[11]</td><td>[46]</td><td>This work</td></tr><tr><td rowspan="2">decision level</td><td>managerial operational</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>store-level product-level</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>information level</td><td>No location RFID location visual</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td></tr><tr><td colspan="5">independence of planograms</td><td></td><td></td><td></td><td>✓</td></tr></table>

Misplaced product detection.. Bu et al. describe a protocol to locate misplaced products [7]. They make the assumption that all predefined positions of all products are known. Chaves et al. [11] use a heuristic separation of products to classify them as belonging to certain RFID antennas in smart shelves. Based on information from planograms for shelves, they can identify products that are located in diferent shelves violating the planogram. More recently, Saran et al. investigated how planogram compliance can be ensured with visual analytics [46] by analyzing pictures of shelves. Planogram-based approaches difer from our approach, as they assume that planograms describing the planned assortment of goods exist, while we compare and present generally applicable methods.

Table 1 summarizes the related approaches and highlights the positioning of our work. The key contribution of this paper is an accurate misplaced product detection technique, that is able to work without planograms. In this way, it is able to cope with the noisy nature of RFID sensor streams, product categories that are spread to multiple locations, while being agnostic of planograms.

## 2.5. Requirements for Misplaced Product Detection

Based on the state of the art and the noisy nature of sensor systems, we formulate the following requirements for the misplaced product detection problem.

R1 Accuracy. The misplaced product detector should be able to yield a robust

R2 No planogram. Due to ever changing layouts and seasonal assortment rearrangements, planograms are hardly kept up to date. The misplaced product detection should be able to detect misplaced products without detailed plans of where each product should be.

R1 is motivated by the fact that sensor based systems (e.g. RFID) are subject to inaccuracies. That is, we cannot simply compare the sensed location of a product with a fixed boundary of an area, where that product should be. Even when the product is orderly in its designated position, the sensing infrastructure could still detect it outside that area and falsely classify it as misplaced. R2 means that we need to rely on methods that do not take into account location plans of products and are able to work only with the sensor data itself. In the following, we discuss how we address these requirements.

## 3. MiProD: Misplaced Product Detection

In this section, we formalize the problem of misplaced product detection and present a general system architecture to deploy diferent algorithms in the context of misplaced product detection.

## 3.1. Problem statement

Let $P = \{ p _ { 1 } , . . . , p _ { n } \}$ be a set of n products in store. Further, let $C =$ $\{ c _ { 1 } , \ldots , c _ { l } \}$ be a set of l product classes, and $l \leq n$ . Each product is assigned to its class through the function $\gamma : P  C$ . For example, let $c _ { 1 }$ denote the class of pants. Then, $\gamma ( p _ { 1 } ) = c _ { 1 }$ means that the product $p _ { 1 }$ is of class pants. The set of products $P$ is partitioned into the disjoint sets of misplaced products M and non-misplaced products M $( { \mathrm { i . e . , ~ } } P = M \cup { \overline { { M } } }$ , and $M \cap { \overline { { M } } } = \emptyset )$ . Each product has a real location in three dimensional space captured by the function λ : $P $ $\mathbb { Q } ^ { 3 }$ . We assume that a noisy sensing infrastructure estimates the positions of products. Therefore, each product has a sensed location in three dimensional space, captured by $\widetilde { \lambda } : P \to \mathbb { Q } ^ { 3 } \cup \bot$ . Note that the sensing infrastructure can assign the empty position ⊥ (missing read) to a product. Especially, the inaccuracy of the sensing system afects the discrepancy between actual locations λ and sensed locations $\widetilde { \lambda }$ of products. Provided these notions, we define the static version of the misplaced product detection problem.

Problem 1 (Static Misplaced Product Detection). Given a set of products $P _ { \cdot }$ , their classes $\gamma$ and their sensed locations $\widetilde { \lambda } ,$ , decide which products are misplaced and return the set of estimated misplaced products $M ^ { \prime }$

Given the static misplaced product detection problem, we can also define the dynamic version as follows.

Problem 2 (Dynamic Misplaced Product Detection). Given a set of products $\smash {  { P _ { \perp } } }$ , their classes γ and their sensed locations at two consecutive sensor readings $\lambda _ { 1 }$ , and $\bar { \lambda } _ { 2 } ,$ find the misplaced products at the last sensor reading and return them in the set $M ^ { \prime }$

In either variant of the problem, we can define the quality of the detection classifier if we know the true set of misplaced products M. Then, the quality of the misplaced product detection can be measured by the recall $\big ( \frac { | M ^ { \prime } \cap M | } { | M | } \big )$ that captures the fraction of correctly detected misplaced products over all misplaced products and the precision $\big ( \frac { | M ^ { \prime } \cap M | } { | M ^ { \prime } | } \big )$ that captures the fraction of correctly detected misplaced products over the result set [4].

Besides these basic quality measures, we can analyze the trade-of incurred by adjusting the discrimination threshold of the classifier. That is, we analyze the efect of increasing the number of returned products according to the ordering by a classifier. The receiver operating characteristic (ROC) curve plots the true general, the area under the curve (AUC) is a good overall measure to compare the accuracy of classifiers. The trade-of between precision and recall is also of interest. That means, we can plot how precise the result is over varying degrees of recall. We report these curves and graphs because outlier detection methods are threshold-based, and ROC curves and precision/recall graphs show how management decisions can achieve an adequate balance between efectiveness (recall) and eficiency (precision).

![](/api/attachments/NQW83VRY/fulltext/images/cc2c12f223bbcc0ecf2ca827c24288f56bd5ee24593a14eff7bf28c94b5a96a8.jpg)  
Figure 2: Overview of the approach. Sensor events are turned into products and their locations. Misplaced product detection is applied and a ranked list of products is generated. The discrimination threshold separates products into misplaced and not misplaced.

## 3.2. Misplaced product detection method

Figure 2 shows the overview of the approach. We assume that a sensor event stream exists and captures RFID data (or other sensor data) from products in a store. Then, we define aggregate and convert raw sensor reads of tagged products to locations of products, cf. [25]. Based on the product information and their estimated locations, we use classifiers to separate misplaced products $M ^ { \prime }$ from non-misplaced products ${ \overline { { M } } } ^ { \prime }$ . We can select any classification method in this misplaced product detection architecture. Each classifier produces a ranked result set, that is based on a score $\sigma : P \to \mathbb { Q } ^ { + }$ function. The classifiers produce a ranking $\rho : P \to \mathbb { N } .$ , where the expected outliers (misplaced products) are on top of the ranking. We implemented the following classifiers:

kNN. A solution to the static misplaced product detection is the k-nearest neighbors classifier. Given the k-nearest neighbors of a product p in the store as $N _ { k } ( p )$ , we assign the outlier score $\sigma _ { \mathrm { k N N } }$ of a product p as follows:

$$
\sigma_ {\mathrm{kNN}} (p) = \frac {| \{p _ {i} \in N _ {k} (p) | \gamma (p) \neq \gamma (p _ {i}) \} |}{k}
$$

Note that $\sigma _ { \mathrm { k N N } }$ assigns a value between 0 and 1 to each product, and the more neighbors of a product have a diferent class, the higher the outlier score $\sigma _ { \mathrm { k N N } }$ Intuitively, this measure reflects the idea that based on the class of the nearest neighbors, we can decide whether a product is in distribution or not [22].

LOF. This spatial outlier detector uses the local outlier factor (LOF), as defined by Breunig et al. [6]. The LOF depends on the density of the cluster and the distance of individual elements to the nearest elements and their density. We separately apply the LOF to the products of one class in isolation.

GLOSH. Furthermore, we implemented the spatial outlier detector called ”Global-Local Outlier Scores from Hierarchies” (GLOSH), which was recently proposed by Campello et al. [9]. It computes a range of density based clusterings and analyses them to derive the final outliers.

distance classifier. A solution to the dynamic misplaced product detection is to consider the distance $\sigma _ { \mathrm { d i s t } }$ between the two consecutive sensed locations $\lambda _ { 1 }$ and $\lambda _ { 2 }$ of a product [18, p. 538f]. Formally, this is: $\sigma _ { \mathrm { d i s t } } ( p ) = \delta \big ( \lambda _ { 2 } ( p ) , \lambda _ { 1 } ( p ) \big )$

Here, δ represents any distance metric (e.g., the Euclidean distance between two points in Cartesian space). Considering two points $( x _ { 1 } , y _ { 1 } )$ and $( x _ { 2 } , y _ { 2 } )$ in a two dimensional space, yields the distance:

$\sqrt { ( x _ { 2 } - x _ { 1 } ) ^ { 2 } + ( y _ { 2 } - y _ { 1 } ) ^ { 2 } }$ . Note that if any of the two sensor readings failed for product $p \left( \mathrm { i . e . , } \lambda _ { 1 } ( p ) = \perp \lor \lambda _ { 2 } ( p ) = \perp \lor \lambda _ { 1 } ( p ) \right)$ ), the distance classifier fails to produce a score for that product $( \sigma _ { \mathrm { d i s t } } ( p ) = 0 )$

MiProD classifier. The misplaced product detection method presented in this work. It aggregates the ranked result lists of three perspectives: i) local neighborhood (kNN), ii) spatial relation to same class $( \mathrm { L O F } ) .$ , and iii) dynamic (distance). The aggregation is chosen to be sensitive to either perspective, that is, we use a maximum aggregation of the resulting ranks.

Given two ranking functions that order products according to their outlier scores $\rho _ { 1 } : P \to \mathbb { N }$ and $\rho _ { 2 } : P \to \mathbb { N }$ , the maximum aggregation assigns the scores: $\rho _ { \mathrm { m a x } } ( p ) = \operatorname* { m a x } ( \rho _ { 1 } ( p ) , \rho _ { 2 } ( p ) )$ . This concept naturally translates to more than two rankings.

We provide a brief motivation for aggregating ranked lists with a maximum rank. Consider the example of four products $\{ p _ { 1 } , p _ { 2 } , p _ { 3 } , p _ { 4 } \}$ that are ranked by two diferent classifiers that yield ranks $\rho _ { 1 }$ and $\rho _ { 2 }$ as described in Table 2. We see that for product $p _ { 3 }$ and $p _ { 4 }$ the two rankings agree, but one classifier $p _ { 1 }$ $p _ { 2 }$ at position three, while the other does the opposite. Further, in $\mathrm { T a b l e ~ 2 , }$ we see the resulting ordering by using a maximum rank $( \mathrm { i . e . , }$ preferring products that any classifier preferred), a minimum rank $( \mathrm { i . e . , }$ penalizing products that any classifier penalized), and an average rank (i.e., mixing the two rankings equally).

Results in the context of aggregating outliers [32, 47] suggest that there is no general optimal way of aggregating diferent outlier detectors. It depends on the application, how ranking methods should be aggregated. In our case, we want to find products that moved a distance and ended up in a neighborhood unlike their class, $o r$ were already misplaced in the first place. Following this line of reasoning, we selected $\rho _ { \mathrm { m a x } }$ . We checked multiple combinations of normalization and aggregation of outlier scores and report the results in the online appendix to this paper [48]. The summary of those experiments is that occasionally the average of outlier scores yields better results than the maximum of the ranked scores. However, the maximum of the ranked scores is robust w.r.t. the selection of diferent outlier detectors and on average outperforms score based methods.

Table 2: Two example rankings of four products $\{ p _ { 1 } , p _ { 2 } , p _ { 3 } , p _ { 4 } \}$ and the aggregate maximum, minimum, and average rankings. Ties in the aggregate ranking are highlighted. The table is sorted with the outliers at the top. Rankings are indicated in brackets.

<table><tr><td> $\rho_1$ </td><td> $\rho_2$ </td><td> $\rho_{\text{max}}$ </td><td> $\rho_{\text{min}}$ </td><td> $\rho_{\text{avg}}$ </td></tr><tr><td> $p_1 (4)$ </td><td> $p_2 (4)$ </td><td> $p_1 (4)$ </td><td> $p_3 (3)$ </td><td> $p_3 (3)$ </td></tr><tr><td> $p_3 (3)$ </td><td> $p_3 (3)$ </td><td> $p_2 (4)$ </td><td> $p_1 (2)$ </td><td> $p_1 (3)$ </td></tr><tr><td> $p_2 (2)$ </td><td> $p_1 (2)$ </td><td> $p_3 (3)$ </td><td> $p_2 (2)$ </td><td> $p_2 (3)$ </td></tr><tr><td> $p_4 (1)$ </td><td> $p_4 (1)$ </td><td> $p_4 (1)$ </td><td> $p_4 (1)$ </td><td> $p_4 (1)$ </td></tr></table>

## 4. Evaluation

To evaluate the approaches, we first conceptually test the accuracy in an artificial setting. This way, we can test a high number of configurations that would be infeasible to explore in real settings. To also validate the approach in

## 4.1. Generating artificial data - Variables

In order to generate a suficient amount of test data to validate our algorithm, we developed $\mathrm { a }$ software application to simulate arbitrary retail store setups based on various parameters. We analyzed the literature to ensure realistic parameter ranges. Table 3 summarizes our findings for realilstic parameters. We found that the references agree on an inaccuracy between 0 and 5 meters, while contradicting ranges for missingness were reported in diferent studies. Latter extremes for missingness occur in settings such as trying to read RFID tags behind water basins. Thus, a range between 0 percent and 50 percent seems to be worthy to investigate in our setup.

Table 3: Summary of reported accuracy values in meters and missingness in percent.

<table><tr><td>Parameter</td><td>Range</td><td>Ref.</td></tr><tr><td rowspan="3">Accuracy</td><td>0.5 to 4.5 m</td><td>[33]</td></tr><tr><td>0.07 to 0.91 m</td><td>[23]</td></tr><tr><td>1.92 to 4.69 m</td><td>[5]</td></tr><tr><td rowspan="4">Missingness</td><td>Read rate drops to 0 after 18m / 16dB of attenuation</td><td>[41]</td></tr><tr><td>Between 60 and 100%</td><td>[14]</td></tr><tr><td>Up to 13%</td><td>[44]</td></tr><tr><td>Between 33 and 95%</td><td>[10]</td></tr></table>

These parameters are used in the evaluation. Figure 3 gives an overview of the structure of our evaluation. Within the developed “RTLS-Simulator”, three subsequent steps can be identified. First, the initial store setup (Inventory I) is generated based on the following four parameters:

• Products $[ \# ] !$ The number of individual products, which are placed in the store. We explore the range between 1 000 products and 50 000 products (1 000, 2 000, 5 000, 10 000, 20 000, 50 000).

• Classes [#] : The number of classes (i.e. groups of products in a shop) to be generated. Each product is randomly assigned to one class out of configurable overlap at the boundaries. We investigate situations from 10 classes to 200 classes with steps at multiples of 50 (10, 50, 100, 150, 200).

• Clusters per Class $[ \# ]$ : A factor which determines the number of areas that will be generated within a shop (#Areas = #Classes · #Clusters per Class). A factor of 1.0 will generate one area for each class, while a higher factor will allocate the areas such that some classes will have two or more distinct areas on the floor. This means that even in an ordered store, there might be certain classes that are displayed at multiple positions. We vary the clusters per class between 1 and 3 (1, 1.5, 2, 2.5, 3).

• Dispersion [m] : The amount of spatial overlap between adjacent class areas. When we look at a 2D-projection of a shop in which shirts are placed above pants, the classes of shirts and pants overlap in their floor area. Dispersion is a means to allow for fuzzy boundaries between classes by extending the class boundaries. Dispersion ranges between 0 and 5 meters (0m, 1m, 2m, 3m, 4m, 5m).

![](/api/attachments/NQW83VRY/fulltext/images/de5c32050f37b663fb656f5745ff1794a6d6ba8e51e34361fab3ef12a9a06e0a.jpg)  
Figure 3: Structure of the performed evaluation.

• Misplaced initially [clean/dirty]: If set to dirty, 10 percent of the products is randomly misplaced in the initial inventory. Misplacement means relocation of a product to a random point on the sales floor. This is a logical parameter and we denote it as ”clean” (i.e., not misplaced initially) and ”dirty” (i.e., misplaced initially).

In a second step, the generated inventory I is manipulated based on the given parameter Misplaced Products [%]. In general, the given percentage of all products is randomly taken and moved to arbitrary positions within the store’s boundaries resulting in inventory I<sup>0</sup>. A product is misplaced, if it is misplaced initially in inventory $I ,$ or if it is misplaced in inventory I<sup>0</sup>. Formally, let $M _ { 1 }$ be the products initially misplaced (note that $M _ { 1 }$ is empty in the clean experiment) and let $M _ { 2 }$ be the products misplaced according to the parameter Misplaced Products [%]. Then, the set of misplaced products M is the set union of $M _ { 1 }$ and M<sub>2</sub> (i.e., $M = M _ { 1 } \cup M _ { 2 } )$

The third step simulates physical sensor hardware by taking the following two parameters into account. We select the variable ranges based on the literature findings in Table 3, and on our own experiences with sensing hardware.

• Inaccuracy [m]: The maximum deviation between a product’s actual position in the store and the detected position (in meters). We explore inaccuracy values between 0m (perfect) and 5m (low accuracy) in steps (0m, 1m, 2m, 3m, 4m, 5m).

• Missingness [%] : The percentage of products that are not sensed in one sensor reading due to reading collision [19], reflection, or other reasons [17]. We cover the range between 0% and 50% in steps (0%, 5%, 10%, 20%,

I and I<sup>0</sup> go through this last step separately, resulting in potentially diferent reading positions for the products based on the specified sensor inaccuracies.

## 4.2. Experiment Results

Given the number of variables and their ranges, an exhaustive exploration of the parameter space yields a combinatorial explosion of settings. Therefore, we set realistic default values for all parameters except for the controlled variable that is varied in its range. This way, we can isolate the efects of individual variables on the accuracy of the misplaced product detection methods.

Figure 4 shows the results for the diferent types of scenarios (indicated in the legend of each figure). The resulting scores depict the area under the curve (AUC) of the receiver operating characteristic (ROC) curve [27].

Varying number of products. We can see in Figure 4a that the kNN and distance approaches deliver constant results with respect to the number of products in products, while delivering worse results on the ends of the spectrum. This result is surprising as it indicates that these two approaches are tuned to work well at a particular density of products. The proposed rank average MiProD between kNN, LOF and distance outperforms the other approaches on average.

Varying number of classes. In Figure 4b, we see that distance and the MiProD approaches are not afected by the variation of class numbers. The kNN sufers from an increasing number of classes, as the chances that the neighbor is of the same class gets lower with an increased number of classes. The LOF and GLOSH approaches gain from an increased variation and a relatively smaller area per class that is entailed by a growing number of classes. However, we see that at 200 classes, there is a drop in performance for GLOSH, as the number of products per class is reduced as well, which apparently reduces the accuracy of the hierarchical classifiers.

Varying clusters per class. We can see in Figure 4c similar trends as in Figure 4b, but less pronounced. Also here, the local clusters of products become smaller, as they are increasingly spread throughout the area. In both cases (varying the classes and the clusters per class), the aggregate classifier MiProD yields the best overall performance.

Varying dispersion of class areas. In Figure 4d we can see that most of the classifiers are not much afected by dispersion. However, the kNN based approach shows a decreasing accuracy with increasing dispersion. This is expected, as with increasing dispersion products at the boundaries can become surrounded by neighboring products of other classes. This leads to false positives.

Missingness [%]  
Clusters Per Class [#]  
![](/api/attachments/NQW83VRY/fulltext/images/6ecbe44c70c35412c96b6e4aedcf09896e0869e32ce4a46b0e88e77b9560500f.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/da3c4df8dfd8ff5b7221d11572d853f6f283271d511a182287f889f5104d929b.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/18165ef39231950f7a0dc6cb31ca5209d7a82b23200111040b72f9c485bd017d.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/f514d5eec712b1cb0852577325ff09aafa453801cddaa0644a651b3797bc5864.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/9cee024aca9e5ce355385630b3ec2b9feabdd5d014b829fc28eaba09359acd1f.jpg)  
Experiment: clean Δ· dirty

(a) Number of products 1000 - 50 000 [default: 10 000] (log-scale).  
![](/api/attachments/NQW83VRY/fulltext/images/84e7f76d6ddf56011fbd22d9b0564f0151ce956c6d871978efc05c3c4d37ae5e.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/58d777877882ced271634aff0cea8255125b3c7fd394d2750f8383494cec4195.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/ddf8da80e4c12cf72e0823309635edd99dcffb71af1eaf57d6cb87cbdb9909b6.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/0037c525822cfe30a8fc11347b8ba5420748209f64091986120077a91844447a.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/8be07098d87869a43ca5caf745c4ccf0472a74345a1427cc233d8a31f20e3389.jpg)  
Experiment: clean -Δ· dirty

(b) Classes 10 to 200 [default: 100].  
![](/api/attachments/NQW83VRY/fulltext/images/b2b47ee2de718b911268813f8624b500ecc3a08fadcde66348e8b6ae1cf51891.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/a5d95dc2474bdaf7fa8ff689d72cefbe35bc3d2983be2a09f1612b2d5238961d.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/79285b06457ca5a2b95545f4e4bf10f9baf4ed1d405da759b8949a2788c7e10e.jpg)  
(c) Clusters per class 1.0 - 3.0 [default: 1.5].

![](/api/attachments/NQW83VRY/fulltext/images/1e9ab86cfb363d9a284c14502d6b1547633b687dc5b0a880bd2528c62c152cf9.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/6f34b6d30faae4d76c342a220a7dc8a29408f4d57a39182f5fcbcdb103ff01a4.jpg)  
Experiment: clean -Δ· dirty

![](/api/attachments/NQW83VRY/fulltext/images/f0b09109ecee16ab4d14a773f8f4205c8640154fd2b29c37d06dedbaa8e6c8b0.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/a18bb035cd5a2cf3739e5e0434a59b9828ccefcdc432d2a9162d1d5c2f6198f4.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/4c986ac4ea5598ddf26429355bfd2bfb0a46966cfc78ca2672ebd85fa005af10.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/1fe369a85e5093bc8bbc3e0f4170332446bb296e8eec445d423772649130e6a3.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/11487076a60d8f62ab5969b5986485d70639074866ed177ad7d2915db7334a1a.jpg)  
Experiment: clean -· dirty

(d) Dispersion 0m - 5m [default: 1m].  
![](/api/attachments/NQW83VRY/fulltext/images/1d940f422895cbf06464803807df0945eca9c6f5045ebc299f4d72bc98fbf1ac.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/a8ae73067a67a2245e3dfd3f8bb632cfa11d74aa55ae562b3df4411acbe7a193.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/8c3f93ed72cdd5f9496215269e7af05f18c7d0fc728158d9e8f7caf6964b6f4b.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/73e1c1697aedaac87893808930ccc25aad3fe6394c3665f3e403b76dc41e2f4d.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/09016730f8b717e9644224a0270277186370b9a67e0701ba3a0de618e378ca20.jpg)  
(e) Misplaced products 1% - 90% [default: 10%].  
Experiment: clean -· dirty

![](/api/attachments/NQW83VRY/fulltext/images/1ae043ea2681b22ff6cb9d755ab870e13e182d1fed6ecebbb14b9edec15fdcdd.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/f0dcabbe6dd10b1b11d1ba9fb20739f21585db4e04a449bffbb1a221a9f32fd6.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/003f6976905bf44d7d18def8441e865133721e0dbd6146db49b5424049621fa0.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/12b805628fc71b9d5f6de6e70f9c948e5daef9ad50a107c1c284e28e4181fa9b.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/ba6dfa6b7b9f0c10fc450c8e22e9d6d0582d8a878712364b3acae2a5d49c4589.jpg)  
Experiment: clean -Δ· dirty

(f) Inaccuracy of reading position 0m - 5m [default: 3m].  
![](/api/attachments/NQW83VRY/fulltext/images/9bd6963ca8be0f05a7de37c6a5e60d0ead6e2dfd2b90396848692b4b78ed2d62.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/ddb6f6aba8480061d9f66fcdb3e2a291a0ab36ed25d42db4d70de6c6eb66fab3.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/f82ee7a16d7131cf99c38fa4876fa8526dd7d1a496682d1f5a1d94990bcc3a9a.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/3779820c36200b3f6abce3121eab33e5cb7ed253c43ac870bad0ed217a8fa934.jpg)  
(g) Missingness 0% - 50% [default: 10%].

![](/api/attachments/NQW83VRY/fulltext/images/f9c732e9a0772cf1a9deb88b376c8a352085edafe380206100aa8b4114484c91.jpg)  
Experiment: clean Δ· dirty  
Figure 4: Resulting area under the curve values for two experiments: (◦) clean at start, and (4) dirty with 10% initially misplaced products. All parameters are set to their default value except for the variable varied on the x-axis. Ranges are noted in the caption and the default value is noted in square brackets.

Varying percentage of misplaced products. Figure 4e depicts the number of misplaced products in percentage of the total number of products. The performance of all classifiers decreases rapidly, as the number of misplaced products increases. Only the distance classifier shows an increasing trend for the dirty case. The distance measure helps distinguishing truly moved products from stationary inaccurate readings. If we limit our attention to values between 1% and 30%, we observe that MiProD outperforms the other approaches.

Varying inaccuracy of the sensor system. We see in Figure 4f that the approaches kNN and indirectly also MiProD slightly sufer in their classification accuracy with increasing sensor inaccuracy. The trends are comparable to the dispersion experiment. The kNN based approach that looks at immediate neighbors of a product is most afected, as with lower accuracy, the chances increase that the sensed position of a product is within a neighborhood of a diferent class, which renders it a false positive. The combination of classifiers in MiProD outperforms the individual classifiers.

Varying missingness of reads of the sensor system. Last, in Figure 4g, we see that the percentage of missing reads severely impacts the classification accuracy of the compared methods. The distance classifier sufers the most, as it depends on having two consecutive reads for each product. In a clean state with no missingness issues, however, this is the best method. When some products are already misplaced, or there is at least a 5% chance for missed sensor readings per product, the MiProD approach yields the best results.

Table 4: Average AUCs for the two scenarios and the diferent methods.

<table><tr><td>Experiment</td><td>kNN</td><td>LOF [6]</td><td>GLOSH</td><td>distance [9]</td><td>MiProD</td></tr><tr><td>clean</td><td>0.769</td><td>0.757</td><td>0.784</td><td>0.802</td><td>0.855</td></tr><tr><td>dirty</td><td>0.759</td><td>0.684</td><td>0.743</td><td>0.675</td><td>0.810</td></tr><tr><td>both</td><td>0.764</td><td>0.720</td><td>0.763</td><td>0.739</td><td>0.832</td></tr></table>

Summary of the experiment. Table 4 summarizes the experiment results and shows the competing methods’ aggregate AUC values. We can see that the proposed rank-aggregate method MiProD yields the overall best results in finding misplaced products. In a clean state, the distance classifier detects the misplaced products second best, while yielding the worst results in a dirty state, where 10% of the products are initially misplaced. The kNN based approach is the least susceptible to a dirty state and is overall second best, directly followed by GLOSH, and then distance. The local outlier factor LOF yields the overall lowest scores in this experiment.

## 4.3. Robot-based case study in retail

We performed a controlled experiment in a retail store, where inventory counting and locating is done by a robot. The inventory robot collects the positions of the products on the sales floor by triangulation of a product’s RFID tag. To this end, the robot has directed antennas that have a characteristic signal strength depending on the angle of a tag to it. Readings can be collected at multiple known positions, at which the robot is passing, and aggregated to an estimated location, e.g. the way it is described in [45]. The setting is similar to the experiments we reported above. We start with a rather clean state, as we specifically advised the store staf to diligently clean up the store before the experiment. In this clean state, we took the first sensor reading of the products and their location over night with the help of an inventory robot.

We simulated customer behavior by misplacing 55 products M (the set M is the ground truth for evaluation). Then, we took a second sensor reading of the products and their location with the help the inventory robot. At this point at least the products in M are misplaced. The two readings are input to the classification task of finding the misplaced products M.

![](/api/attachments/NQW83VRY/fulltext/images/bd6b3068aefa65d0984b5acf2350d2094a15b27cea835a3fa03140e0d5846228.jpg)  
(a) Box plot of products per class before preprocessing (average products per class 656, standard deviation 796).

![](/api/attachments/NQW83VRY/fulltext/images/49c49aa15a372da820a8f31bc1c0fab5dd8cbccfd5a2e23a4defdff60cb7caf1.jpg)  
(b) Box plot of products per class after preprocessing (average products per class 121, standard deviation 45).  
Figure 5: Box plots of products per original (a) and preprocessed (b) classes

Estimated parameters.. The number of products in this setting is 25,570. The initial state can be considered clean. The inaccuracy of the robot is low, as the median diference of the products’ estimated location between the two reads is 0.4 meters. Also, the two subsequent sensed product sets’ overlap is 94% (based on the first reading R and second reading R<sup>0</sup>, the overlap is $\frac { | R \cap R ^ { \prime } | } { | R \cup R ^ { \prime } | } )$ . Assuming a completely random missingness process, this yields an estimated missingness of less than 3 percent per read. The number of classes as organized by the retailer is 39 with a heterogeneous distribution.

The inspection of the classes showed that the distribution areas of some classes are spread throughout the entire shop. This is expected to impact the outlier detection quality of spatial outlier detection methods like LOF and GLOSH. Furthermore, the classes are rather imbalanced in size, as depicted in Figure 5. Therefore, we applied a preprocessing step to better split the products into logical classes.

Table 5: AUCs for the diferent methods in the robot experiment. The two rows capture the results for 39 original classes, and for the 210 preprocessed classes.

<table><tr><td>Experiment</td><td>kNN</td><td>LOF [6]</td><td>GLOSH</td><td>distance [9]</td><td>MiProD</td></tr><tr><td>original classes</td><td>0.706</td><td>0.806</td><td>0.802</td><td>0.946</td><td>0.987</td></tr><tr><td>preproc. classes</td><td>0.706</td><td>0.990</td><td>0.994</td><td>0.946</td><td>0.998</td></tr></table>

Preprocessing the product classes. We applied a hierarchical clustering [29] on compared products, and the distance of products to one another on the map. The hierarchical clustering produces a dendrogram tree. Each node in the tree is annotated with the number of contained products. We extracted the classes from that tree by trying to split large nodes that have a product count larger than 200, and request that splitting does not result in classes smaller than 50 products. In this clustering, we respected the initial categorization of the retailer and only partitioned the larger classes further. The resulting class count after preprocessing is 210, as shown in Figure 5b.

## 4.3.1. Case study results

The area under the curve for the misplacement with and without preproproduct classes, we can increase the quality of the spatial outlier detectors.LOF and GLOSH significantly benefit from this step. For brevity, we only investigate the better results based on preprocessed classes. In this case, most outlier detectors yield already very high areas under the curve, with the MiProD rank aggregate method showing top performance at 0.998, while GLOSH and LOF closely follow with AUC values of 0.994 and 0.990, respectively. The distance classifier yields an AUC of 0.946 although it outperforms the other outlier classifiers in the clean setup, as we can see in the results in Table 4.

Next, we discuss the results on a disaggregated level. Figure 6 shows the shape of the ROC curves and also the corresponding trade-of between recall and precision. Note that the count of positives (55 misplaced products) is only a small subset of the total number of products (25570 products on the sales floor). Therefore, not only recall is interesting, but precision is equally important.

The kNN method (Figure 6a) turns out to be unreliable in this particular case. The precision is around 0.004 at best, which means that an employee would need to check 250 products to find a single misplaced product. Latter

The local outlier factor (LOF) [6] shown in Fig. 6b is the only one that correctly positions the first few misplaced products on the top of its ranking (the precision/recall graph starts at 1 and stays there for a few of the 55 misplaced products). After that however, the precision rapidly decreases and a recall of 0.5 (identifying 50 percent of the misplaced products) entails browsing through five times the number of misplaced products at a precision of 0.2. The precision gets only worse with increasing the result set, but this approach is able to rank some of the products higher, which the distance method did not discover. The ROC curve reaches 1 at a false positive rate of around 0.1, while with the distance method we need to check almost every product to find all outliers.

The GLOSH [9] method’s performance in Figure 6c displays a more steady precision graph over the entire set of misplaced products. However, it fails to single out the misplaced products at the start of the list. The best precision/recall trade-of is perhaps at 0.55 recall with 0.2 precision, which is comparable to the result achieved by the LOF method. However, it shows more consistent results over the entire set of misplaced products and is able to locate the last misplaced products sooner than the LOF which yields a superior AUC.

The distance method depicted in Figure 6d shows good precision, which is to be expected, as misplaced products tend to have moved a larger distance than the not-misplaced counterparts. We see in the precision/recall graph that

![](/api/attachments/NQW83VRY/fulltext/images/064e1a544893f4dd14eb26166fd5fdc5b28f94d03d570d67ddf5e6322b29443d.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/f183f085077aeda760027be4e09dd0bea4c6a2678f754383c52025e2c34599f5.jpg)  
(a) kNN method.

![](/api/attachments/NQW83VRY/fulltext/images/d04e819be3221f932842cb8cdad553489a0892c07e82a2ba8c0521e8806904f9.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/8a17d648a905820de8b30b667ca983dcfe6d2638c68d5feb4047397bdeb16ccc.jpg)  
(b) LOF method.

![](/api/attachments/NQW83VRY/fulltext/images/543938b02fca1928d81a07e390f6d7deb7f221907c9d79d65eca3e32a67514c1.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/75c2a88e4a78f13aae6565a78a9388345bee84d23273a8326407b3aad247b8f4.jpg)  
(c) GLOSH method.

![](/api/attachments/NQW83VRY/fulltext/images/7a91e3c68096cf7f5420b8f4bb52fe364da2c79305fde3d92c0ecaa6fa80fd39.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/81821307254aaabb4fb841c99b1ea9c6944a3a14508a79899f6a6c151db0d5f0.jpg)  
(d) Distance method.

![](/api/attachments/NQW83VRY/fulltext/images/1376fb7bf3ebf0f57e5386120199df309d86f917d0b7d26474b80b45a07da3f4.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/e17d017e7008e4934c7d4897e07410a58d05bd11178a58505645df10d4490f60.jpg)  
(e) MiProD method.

Figure 6: ROC curves for the diferent methods with the inventory robot experiment, and their performance in terms of trade of between precision and recall (PR space).

a high recall (about 0.9) can be achieved with a still high precision (close to 0.4). This means that a shop employee working through the ordered list of potential outliers would find 90 percent of misplaced products with an average of 3 non-misplaced products per five products checked in this case.

Finally, we propose a rank aggregate method based on the maximum ranking of kNN, LOF and distance. From the spatial detectors LOF and GLOSH, we picked LOF based on extensive experiments, as it yields overall slightly better results than GLOSH, cf. the online appendix [48]. Note that adding GLOSH as fourth method, worsens performance, regardless of the aggregation. We interpret latter as over-representation of spatial detectors in the aggregation. The MiProD approach depicted in Figure 6e yields a remarkable AUC of 0.998, which is close to the optimal score of 1.0. We see in the precision/recall graph that while the precision sufers a little in comparison with the distance method, it is able to find all misplaced products with a precision of around 0.25. This means that an employee can find all 55 misplaced products by checking around 220 products.

## 5. Implications

Our experiment investigated in how far misplaced products can be detected using outlier detection techniques without having a planogram available. Our results demonstrate that this problem can be tackled using outlier detection techniques [2] in an accurate way. The best results were achieved using our MiProD aggregation technique. Our results have implications for research into sensor based locating systems [35, 31], misplaced product detection [24, 42], and for their joint application in practice [8, 11, 7].

The important implication of our work for research is that machine learning techniques can be efectively used to harness sensor systems for improved operational use cases. More specifically, this finding is important for research into misplaced products—a stream of research that up until now assumed that planogram information was required [11, 7]. In our experiments, we observed diverging strengths and weaknesses of existing techniques, which we managed to balance using our MiProD aggregation technique.

Some observations can be made on the applicability of the existing techniques. We found that in our simulated setting with the collected parameters, the kNN method [22] performed mostly better than the spatial outlier detectors LOF [6] and GLOSH [9]. However, in a more intricate store layout as observed in the real-world experiment, its performance deteriorated. This deterioration implies that products projected on a 2D plane are more heterogeneous in reality than in the generated clusters, where initially most areas are exclusively filled with products of a single class. The proposed MiProD rank aggregation method works well within the scope of the investigated real-world setting, as it is able to compensate the flaws of one classifier by the strengths of another. Furthermore, we saw that some spatial outlier detection methods can be improved by preprocessing the data before applying the anomaly detection methods.

In the context of misplaced product detection, we first note that the outlier detection problem can be tackled in a binary setting. From the retailer’s point of view, in fact, items are either misplaced, or they are not, and it makes not much sense for store managers to assign to each item a degree or measure of being an outlier. On the contrary, it is more interesting for retailers to investigate the precision of the result set. Thus, we investigated the precision/recall graphs as well. We found that even though the distance method was outperformed by the spatial outlier detectors in the AUC values, its precision for the largest part of the resulting misplaced items was higher. Therefore, for a successful implementation, the distance classifier might be preferable in the trade-of between precision and recall, when one is willing to compromise on the (hopefully) few products that are missing in either of two consecutive sensor reads.

Our work has also implications for practice. The results clearly demonstrate the potential of improving the analysis of the raw data provided by RTLS. Vendors of such systems might be better advised in fine-tuning their analytical software than investing in more powerful hardware. The results also show that accuracy (Requirement 1) can be achieved without having to rely on planogram information (Requirement 2). This aspect substantially extends the applicability of misplaced product detection using RFID sensor systems to settings in which planograms are not available or not continuously kept up to date.

Furthermore, an accurate insight into the misplaced products can yield operational benefits on the managerial level [51]. The number of product misplacements per product become visible to the decision makers of the stores and indirectly relate to customer interactions with the products. An investigation of the ratio of the number of misplacements and the number of sales per product looks promising. For example, knowing that a product is often misplaced but rarely sold would indicate a discrepancy between customer interest in a product and the willingness to buy it. This valuable knowledge can be used to optimize sales strategies and also inventory assortments.

Also some notes on potential limitations are warranted. The results cover bread ranges of plausible characteristics of retail shops and common sensor technology. Nevertheless, we need to be careful when extrapolating the results to settings in other domains with characteristics beyond the ranges that we investigated. Sensor systems significantly vary in their reading accuracy, missingness rate and other characteristics like the time interval between sensor readings.

## 6. Conclusion

In this work, we investigated the problem of detecting misplaced products without planogram data in order to reduce the amount of missed sales opportunities in retail stores. We investigated methods of spatial outlier detection, and also a means of misplaced product detection based on consecutive sensor readings based on the distance. In extensive experiments, we investigated the influence of diferent parameters in the setup of a store and sensing environment on misplaced product detection and also proposed a novel aggregation method for misplaced product detection (MiProD) that outperformed individual methods. Our results emphasize that misplaced product detection is accurately feasible in practice even if planogram information is not available.

## Acknowledgments

We thank David Riob´o Barba and Manuel Stochlinski for their assistance in implementing the prototypes and simulators. We thank Alexander Weinhard, and Matthias Hauser for helping with conducting the experiments on site. This work was supported by the European Union’s Seventh Framework Programme (FP7/2007-2013) grant 612052 (SERAMIS).

## References

[1] Elke Achtert, Ahmed Hettab, Hans-Peter Kriegel, Erich Schubert, and Arthur Zimek. 2011. Spatial outlier detection: data, algorithms, visualizations. In International Symposium on Spatial & Temporal Databases. Springer, 512–516.

[2] Charu C. Aggarwal. 2017. Outlier Analysis (2nd ed.). Springer International Publishing.

[3] Aykut Atali, Hau L Lee, and Ozalp <sup>¨</sup> Ozer. 2009. <sup>¨</sup> If the inventory manager knew: Value of visibility and RFID under imperfect inventory information. Technical Report. Graduate School of Business, Stanford University.

[4] R.A. Baeza-Yates and B.A. Ribeiro-Neto. 1999. Modern Information Retrieval. ACM Press / Addison-Wesley.

[5] Paramvir Bahl and Venkata N. Padmanabhan. 2000. RADAR: An In-Building RF-Based User Location and Tracking System. In Proceedings IEEE INFOCOM 2000, Tel Aviv, Israel, 2000. 775–784.

[6] Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng, and J¨org Sander. 2000. LOF: Identifying Density-Based Local Outliers. In Proceedings of the 2000 ACM SIGMOD. ACM Press.

[7] Kai Bu, Bin Xiao, Qingjun Xiao, and Shigang Chen. 2012. Eficient Misplaced-Tag Pinpointing in Large RFID Systems. IEEE Transactions on Parallel Distribited Systems 23, 11 (2012), 2094–2106.

[8] Almula Z Camdereli and Jayashankar M Swaminathan. 2010. Misplaced Inventory and Radio-Frequency Identification (RFID) Technology: Information and Coordination. Production and Operations Management 19, 1 (2010), 1–18.

[9] Ricardo J. G. B. Campello, Davoud Moulavi, Arthur Zimek, and J¨org Sander. 2015. Hierarchical Density Estimates for Data Clustering, Visualization, and Outlier Detection. ACM Transactions on Knowledge Discovery from Data 10, 1, Article 5 (2015), 51 pages.

[10] Leonardo Weiss Ferreira Chaves, Erik Buchmann, and Klemens B¨ohm. 2008. Tagmark: reliable estimations of RFID tags for business processes. In Proceedings of ACM SIGKDD’08. 999–1007.

[11] Leonardo Weiss Ferreira Chaves, Erik Buchmann, and Klemens B¨ohm. 2010. Finding misplaced items in retail by clustering RFID data. In Proceedings of EDBT 2010, Lausanne, Switzerland. 501–512.

[12] Sanjay Chawla and Pei Sun. 2006. SLOM: a new measure for local spatial outliers. Knowledge and Information Systems 9, 4 (2006), 412–429.

[13] Howard Hao-Chun Chuang. 2015. Mathematical modeling and Bayesian estimation for error-prone retail shelf audits. Decision Support Systems 80 (2015), 72–82.

[14] Robert H Clarke, Diana Twede, Jefrey R Tazelaar, and Kenneth K Boyer. 2006. Radio frequency identification (RFID) performance: the efect of tag orientation and package contents. Packaging Technology and Science 19, 1 (2006), 45–54.

[15] Cosmin Condea, Fr´ed´eric Thiesse, and Elgar Fleisch. 2012. RFID-enabled shelf replenishment with backroom monitoring in retail stores. Decision Support Systems 52, 4 (2012), 839–849.

[16] Daniel Corsten and Thomas Gruen. 2003. Desperately seeking shelf availability: an examination of the extent, the causes, and the eforts to address retail out-of-stocks. International Journal of Retail & Distribution Management 31, 12 (2003), 605–617.

[17] Daniel M Dobkin and Steven M Weigand. 2005. Environmental efects on RFID tag antennas. In IEEE Microwave Symposium. 135–138.

[18] Richard O Duda, Peter E Hart, and David G Stork. 2012. Pattern classification (2nd ed.). John Wiley & Sons.

[19] Daniel W Engels and Sanjay E Sarma. 2002. The reader collision problem. In Systems, Man and Cybernetics, 2002 IEEE International Conference on, Vol. 3. IEEE, 6–pp.

[20] Zahid Farid, Rosdiadee Nordin, and Mahamod Ismail. 2013. Recent advances in wireless indoor localization techniques and system. Journal of Computer Networks and Communications 2013 (2013).

[21] Klaus Finkenzeller. 2010. RFID handbook: fundamentals and applications in contactless smart cards, radio frequency identification and near-field communication. John Wiley & Sons.

[22] Evelyn Fix and Joseph L Hodges Jr. 1951. Discriminatory analysisnonparametric discrimination: consistency properties. Technical Report. California Univ Berkeley.

[23] Andre Gleser and Oldrich Ondracek. 2014. Real time locating with RFID: Comparison of diferent approaches. In Proceedings Radioelektronika’14. IEEE, 1–4.

[24] Tahi J Gnepa. 1996. An empirical investigation of deliberate shopper misplacement of products on grocery store shelves. Journal of Food Products Marketing 3, 3 (1996), 3–21.

[25] Hector Gonzalez, Jiawei Han, Xiaolei Li, and Diego Klabjan. 2006. Warehousing and analyzing massive RFID data sets. In Proceedings of International Conference of Data Engineering’06. IEEE, 83–83.

[26] Jefrey Hightower, Roy Want, and Gaetano Borriello. 2000. SpotON: An indoor 3D location sensing technology based on RF signal strength. Technical Report. UW CSE.

[27] D.W. Hosmer and S. Lemeshow. 2000. Applied Logistic Regression (2nd ed.). John Wiley & Sons.

[28] V Daniel Hunt, Albert Puglia, and Mike Puglia. 2007. RFID: a guide to radio frequency identification. John Wiley & Sons.

[29] Stephen C Johnson. 1967. Hierarchical clustering schemes. Psychometrika 32, 3 (1967), 241–254.

[30] Yun Kang and Stanley B Gershwin. 2005. Information inaccuracy in inventory systems: stock loss and stockout. IIE transactions 37, 9 (2005), 843–859.

[31] Hakan Koyuncu and Shuang Hua Yang. 2010. A survey of indoor positioning and object locating systems. International Journal of Computer Science and Network Security 10, 5 (2010), 121–128.

[32] Hans-Peter Kriegel, Peer Kr¨oger, Erich Schubert, and Arthur Zimek. 2011. Interpreting and Unifying Outlier Scores. In Proceedings of SDM’11, Mesa, Arizona, USA. 13–24.

[33] Nan Li and Burcin Becerik-Gerber. 2011. Performance-based evaluation of RFID-based indoor location sensing solutions for the built environment. Advanced Engineering Informatics 25, 3 (2011), 535–546.

[34] Tao Li, Shigang Chen, and Yibei Ling. 2010. Identifying the missing tags in a large RFID system. In Proceedings of ACM International Symposium on mobile ad hoc networking and computing. ACM, 1–10.

[35] Hui Liu, Houshang Darabi, Pat Banerjee, and Jing Liu. 2007. Survey of wireless indoor positioning techniques and systems. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 37, 6 (2007), 1067–1080.

[36] Lionel M Ni, Yunhao Liu, Yiu Cho Lau, and Abhishek P Patil. 2004. LANDMARC: indoor location sensing using active RFID. Wireless networks 10, 6 (2004), 701–710.

[37] Dimitris Papakiriakopoulos and Georgios Doukidis. 2011. Classification performance for making decisions about products missing from the shelf. Advances in Decision Sciences 2011 (2011).

[38] Dimitrios Papakiriakopoulos, Katerina Pramatari, and Georgios Doukidis. 2009. A decision support system for detecting products missing from the shelf based on heuristic rules. Decision Support Systems 46, 3 (2009), 685– 694.

[39] Luis Peneda, Ab´ılio Azenha, and Adriano Carvalho. 2009. Trilateration for indoors positioning within the framework of wireless communications. In

[40] TC Poon, King Lun Choy, Harry KH Chow, Henry CW Lau, Felix TS Chan, and KC Ho. 2009. A RFID case-based logistics resource management system for managing order-picking operations in warehouses. Expert Systems with Applications 36, 4 (2009), 8277–8301.

[41] Karthik Moncombu Ramakrishnan and Daniel D. Deavours. 2006. Performance benchmarks for passive UHF RFID tags. In Proceedings of MMB’06. 137–154.

[42] Ananth Raman, Nicole DeHoratius, and Zeynep Ton. 2001. Execution: The missing link in retail operations. California Management Review 43, 3 (2001), 136–152.

[43] Yacine Rekik, Evren Sahin, and Yves Dallery. 2008. Analysis of the impact of the RFID technology on reducing product misplacement errors at retail stores. International Journal of Production Economics 112, 1 (2008), 264 – 278.

[44] Antonio Rizzi and Giovanni Romagnoli. 2016. Testing and deploying an RFID-based Real-Time Locating System at a fashion retailer: A case study. In Workshop on Business Models and ICT Technologies for the Fashion Supply Chain. Springer, 201–214.

[45] Samer S. Saab and Zahi S. Nakad. 2011. A standalone RFID indoor positioning system using passive tags. IEEE Transactions on Industrial Electronics 58, 5 (2011), 1961–1970.

[46] Anurag Saran, Ehtesham Hassan, and Avinash Kumar Maurya. 2015. Robust visual analysis for planogram compliance problem. In Proceedings of MVA’15. IEEE, 576–579.

[47] Erich Schubert, Remigius Wojdanowski, Arthur Zimek, and Hans-Peter Kriegel. 2012. On Evaluation of Outlier Rankings and Outlier Scores. In Proceedings of SIAM International Conference on Data Mining. 1047– 1058.

[48] Andreas Solti, Manuel Rafel, Giovanni Romagnoli, and Jan Mendling. 2018. Supplementary Material to the Experiments of Miplaced Product Detection. Technical Report.

[49] Fr´ed´eric Thiesse and Thomas Buckel. 2015. A comparison of RFID-based shelf replenishment policies in retail stores under suboptimal read rates. International Journal of Production Economics 159 (2015), 126–136.

[50] Dieter Uckelmann and Giovanni Romagnoli. 2016. RF-based locating of mobile objects. In Proceedings of the 6th International Conference on the Internet of Things. ACM, 147–154.

[51] Ilias P Vlachos. 2014. A hierarchical model of the impact of RFID practices on retail supply chain performance. Expert Systems with Applications 41, 1 (2014), 5–15.

[52] Yang Zhang, Nirvana Meratnia, and Paul J. M. Havinga. 2010. Outlier Detection Techniques for Wireless Sensor Networks: A Survey. IEEE Communications Surveys and Tutorials 12, 2 (2010), 159–170.

# ACCEPTED MANUSCRIPT

## Bibliographic Notes

Andreas SOLTI is a post doctoral researcher with the Institute for Information Business at the Vienna University of Economics and Business (Austria). His research interests are in the area process mining, process analytics, optimization, and sensor data analytics. He is also interested in adaptive learning technologies that can be supported with machine learning.

Manuel RAFFEL is a Master student of Information Systems at the Wirtschaftsuniversität Wien (WU Vienna), Austria. There he also worked as a student assistant at the Institute for Information Business. His main responsibility was software development in the area of Business Process Management. Recently, he returned to his professional career as an IT Project Manager.

Giovanni ROMAGNOLI received his Master Degree (with honours) in Mechanical Engineering for the Food Industry at the University of Parma, Italy. In 2013, he completed his PhD course in Operations and Project Management at the Department of Industrial Engineering of Parma, defending the thesis entitled “Hybrid production planning and control systems: towards an application of lean manufacturing to the Make-To-Order sector”. Since 2013, Giovanni Romagnoli is employed as Research Fellow at the same Department.

His research interests include RFID and supply chain management, production planning & control systems, improvements and applications of lean manufacturing, designing and managing food plants and processes; and led to the realization of more than 25 works published on International Journals or presented at International Conferences.

He is member of the editorial board of the International Journal of Industrial Engineering Computations (www.growingscience.com/ijiec/ijiec.html), and he acts as a referee for some International Journals. He is also an active volunteer in two not-for-profit charities.

Prof. Dr. Jan Mendling is a Full Professor with the Institute for Information Business at Wirtschaftsuniversität Wien (WU Vienna), Austria. His research interests include various topics in the area of business process management and information systems. He has published more than 300 research papers and articles, among others in ACM Transactions on Software Engineering and Methodology, IEEE Transaction on Software Engineering, Information Systems, Data & Knowledge Engineering, and Decision Support Systems. He is member of the editorial board of six international journals, member of the board of the Austrian Society for Process Management (http://prozesse.at), one of the founders of the Berlin BPM Community of Practice (http://www.bpmb.de), organizer of several academic events on process management, and member of the IEEE Task Force on Process Mining.

## Highlights

 Locating misplaced products without planograms

 Combination of outlier detection methods that outperforms individual techniques

 Evaluated in realistic simulation environments and a real-world case study

![](/api/attachments/NQW83VRY/fulltext/images/3b27ac3c1c27cabc00d2479128b169ca1baac658ec927456ab7d21363bdc7c94.jpg)  
(c) Inventory with 3 misplacements  
(d) Sensed inventory w. misplacements  
Figure 1

![](/api/attachments/NQW83VRY/fulltext/images/c6fcdcae6e31da3479a6af9e58101be3b384d94ffbb36442b48f7440e76d43be.jpg)  
Figure 2

![](/api/attachments/NQW83VRY/fulltext/images/3c8165e91655e5fcee3d1f4a2d070b0984d06bfc0e295355505e3be5d8a799a4.jpg)  
Figure 3

![](/api/attachments/NQW83VRY/fulltext/images/f88e29b5c30f6f9541e3fbabc56a4670e53bd8106144389aa96184f2ae2ced2f.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/2e38c0063be18b6fa75de808a83adf6dbc951f6ba9924c0d1cd3238177269a91.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/4144030febf15a62e1733894925cdee0124f8f01e73dc1e9d65329f01beeb6c9.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/f6e1538de91d462efec89898af65803da1abac53b3a7377c424f896a3832c66d.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/44910aba21a3d94c92b44399a048ccb9c1c4cf1daa9c6ff0e9735e71425d312a.jpg)

(a) Number of products 1000 - 50 000 [default: 10 000] (log-scale).  
![](/api/attachments/NQW83VRY/fulltext/images/693475cb2864b3906381b50975242ce5aa40143eb7401b97aaf98a4f5683cab1.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/1dcb12e3d792d828fb530163593b8a5dcf5c6fb826ca85fde21b032030f31527.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/58b5d63f17ad87a0eb657e541eb351db61d81ec0f885575666a4dc61e2cb5f8f.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/44099c2ee1a8b35eb52c9fe8ed45d06570839dd856a6d6e4466f168c1ee4c9e1.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/0837d8d4054d7d3310177bc18934c787b6f9c5d81e1a9c3955c888045cbb6eb7.jpg)  
(b) Classes 10 to 200 [default: 100].

![](/api/attachments/NQW83VRY/fulltext/images/7b690c313a99a817bf7b4be56e380cb5f43be864a89f9f3b4684163321422726.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/0894a9bdf438457d704ba5ecb66a533e903a0fde150ddad245ec31eb072339ef.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/65c16e7679e781145034328fc63380c157c6f816f465104c22abf7989cdd3419.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/646509aa6da0b53b42e3072871b8eb2297c40ef5a41a02254f78afee813c1314.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/2c37f95acdc2de3819f5d67d995a4fde4ab6c4667346c507bde0e5d06ba9f422.jpg)  
(c) Clusters per class 1.0 - 3.0 [default: 1.5].

![](/api/attachments/NQW83VRY/fulltext/images/460a0d1e1a08aa3c96cc37fdf5cbe0e6fa9c514b23f92bcd29a169e69ba34f96.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/8b46f1fe0448be0eaa5a2aba4ede2504ca2dc8ec2bf0595c7c8d892233cf196a.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/997fd15bd10173b2f8a6b83923038860ad186e990bad81924ff02704b582ad43.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/11ddc13cfa92ebca1af2d6c5faab6e9b89aeb2626023b32e04a64f0c2afa90b5.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/60fb68ed975dd612b4944075c02e49bd2708704bbd8a9c9b65699889378afb8e.jpg)  
(d) Dispersion 0m - 5m [default: 1m].

![](/api/attachments/NQW83VRY/fulltext/images/34dcfd5ebe1517db6ec6bcba34c12b3ad3d69fc2eb943f5e90146d3941163c20.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/12e437e5328f8a7d97a281d52ea891d97b2d1cbf246c7983712e78f40f63c40a.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/8fd219a705ef1782fabc6dd3c8a24b50019f3a749f6e401147fc6b4f25e46d93.jpg)  
Misplaced Products [%]

Experiment: clean -· dirty

![](/api/attachments/NQW83VRY/fulltext/images/10994f24e85236871bbe067713b792c90d5969799f833fe50d383522cd84c7eb.jpg)  
(e) Misplaced products 1% - 90% [default: 10%].

![](/api/attachments/NQW83VRY/fulltext/images/7d809ebfb8a9d26df2df3241823444b3f183002f7b19cd7cdd6312b5cb901f46.jpg)

Experiment: clean dirty

![](/api/attachments/NQW83VRY/fulltext/images/72ddbc0caad544379e15dda61265a4f657144d807973ec92e57612d6653684ed.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/3f38a1ca584cb59f80270496dec179ba732c3b13316d0c789466f9312200bd5e.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/1566ba8ad95564df6bc9851beb7ef0aee2b20c15134c16323d9758a234253e27.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/f8df701d2c844455e644844d5d4750bea6fcac41989279c9891fc1d0c3147a81.jpg)

Experiment: clean - dirty

(f) Inaccuracy of reading position 0m - 5m [default: 3m].  
![](/api/attachments/NQW83VRY/fulltext/images/83334d0fd497846cbeb348c32d0d7487fa8ebefd9fcc365255afcea5dc0de66d.jpg)

Experiment: clean dirty

![](/api/attachments/NQW83VRY/fulltext/images/27def5e53f50c7978d0676dd594e845e4401869a803311a015fbc7015866f8e8.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/c392db2938a49e991e69297fe7b6b0e96b2eaf313978290f50207706b9342ceb.jpg)

Experiment: clean dirty

![](/api/attachments/NQW83VRY/fulltext/images/fecb59c3ebe8e94e04209bbac5c42200ed0bf89a6e157b67cda01adbb60999ef.jpg)

![](/api/attachments/NQW83VRY/fulltext/images/9941940d75b019252b0d517ae3549f8e9df72cf2c43255ab1c0c9ab3339fbc1f.jpg)  
(g) Missingness 0% - 50% [default: 10%].

![](/api/attachments/NQW83VRY/fulltext/images/a57f93ba3a5fb755f3904cfbbac58b74fd9f384184c1a7f6263db66e18e7038f.jpg)

210 preprocessed classes  
39 original classes  
![](/api/attachments/NQW83VRY/fulltext/images/43d2647b664bcc832d311c09abe83854b78cbd89720f68350bd66967c2065e66.jpg)

(a) Box plot of products per class before preprocessing (average products per class 656, standard deviation 796).

![](/api/attachments/NQW83VRY/fulltext/images/029857dfc7f963582d1254aa2d5453c06cd46a28c4461e5457b8242f9eaf6cfd.jpg)

(b) Box plot of products per class after preprocessing (average products per class 121, standard deviation 45).

Figure 5

![](/api/attachments/NQW83VRY/fulltext/images/73d73a03d05becda0cd40cc5e8b18583bf7eb0d68d242a1bfd3c83337a6c5924.jpg)  
(e) MiProD method.  
Figure 6
