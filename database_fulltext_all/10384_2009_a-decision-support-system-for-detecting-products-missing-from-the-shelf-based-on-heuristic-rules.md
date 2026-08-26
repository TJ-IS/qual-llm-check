---
otero_id: 10384
otero_key: "5B2JPKD8"
title: "A decision support system for detecting products missing from the shelf based on heuristic rules"
authors: "Dimitrios Papakiriakopoulos; Katerina Pramatari; Georgios Doukidis"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for detecting products missing from the shelf based on heuristic rules

Dimitrios Papakiriakopoulos, Katerina Pramatari ⁎, Georgios Doukidis

ELTRUN, Department of Management Science and Technology, Athens University of Economics and Business, 47 Evelpidon & Lefkados Str., 113 62 Athens, Greece

## a r t i c l e i n f o

Article history: Received 3 October 2006 Received in revised form 21 October 2008 Accepted 2 November 2008 Available online 14 November 2008

Keywords: Out-of-stock Out-of-shelf Shelf availability Heuristic rules Classi<sup>fi</sup>cation problem Rule-based decision support system

## a b s t r a c t

The problem of products missing from the shelf is a major one in the grocery retail sector, as it leads to lost sales and decreased consumer loyalty. Yet, the possibilities for detecting and measuring an “out-of-shelf” situation are limited. In this paper we suggest the employment of machine-learning techniques in order to develop a rule-based Decision Support System for automatically detecting products that are not on the shelf based on sales and other data. Results up-to-now suggest that rules related with the detection of “out-ofshelf” products are characterized by acceptable levels of predictive accuracy and problem coverage.

© 2008 Published by Elsevier B.V.

## 1. Introduction

Consumer value and satisfaction are fundamental to building consumer loyalty (to the brand) and shopper loyalty (to the store) and to increasing sales and category pro<sup>fi</sup>tability [16]. A powerful way to create value and satisfaction is to keep shelves fully ranged [46], but “out-of-shelf” (OOS) is still a frequent phenomenon in the grocery retail sector. Out-of-shelf rates vary wildly among retailers and their outlets depending on a variety of factors, but the majority tends to fall in the range of 5–10%. In their analysis, which is a compilation of many global surveys on the extent, causes, and consumer responses to retail out-of-shelf situations in the grocery retail sector, Gruen et al. estimate an overall average OOS rate of 8.3% [26]. However, in most European countries levels between 10 and 15% are not unusual [47]. Emmelhainz et al.'s [21] research results further show that a shelf stock-out can make a manufacturer lose more than half of his buyers to competitors, whereas retailers face the loss of up to 14% of the buyers of the missing product. This revenue loss (approximately 1.5% of sales) stems not only from lost product sales during the OOS period, but can also extend to later periods or other product categories [9].

In this paper, we investigate the possibility of developing a system that detects the OOS products, utilizing machine-learning techniques. More speci<sup>fi</sup>cally, based on data available in the store information system, such as sales-data, ordering info, product assortment etc. we study the development of a rule-based decision support system that will automatically discover OOS situations on a daily basis for all the stores of a retail chain. In the following section the “out-of-shelf” problem, as well as the alternative approaches to measuring it, are discussed in more detail. Then the proposed rule-based Decision Support System is described in the next section, while Section four discusses the way the system has been developed and validated. Section <sup>fi</sup>ve presents the results from the use of the system followed by a critical discussion and some concluding remarks on future research.

## 2. The “out-of-shelf” problem

The term “out-of-shelf” (OOS) is used in grocery retailing to describe the situation where a consumer does not <sup>fi</sup>nd the product he/ she wishes to purchase on the shelf of a supermarket during a shopping trip. The term OOS covers the cases where the product exists in the store (so it is not out-of-stock), but it is not placed in the right position on the shelf where the consumer can <sup>fi</sup>nd it (it is, for example, in the store's back-room or delivery facilities). This term is broader than the term “stock-out” (or “out-of-stock”), which is usually met in the pertinent literature, as a stock-out certainty that implies an OOS situation, while the opposite is not always true.

An OOS occurs more frequently than a stock-out and it is rather dif<sup>fi</sup>cult to capture. The stock-out problem has been investigated in the area of Inventory Management for over 30 years and several models have been presented [29]. On the other hand, the OOS problem is mainly discussed in the marketing literature from the consumer reaction perspective [9,21]. The next table (Table 1) summarizes the variables affecting the product availability in the store, as discussed in the pertinent literature. The <sup>fi</sup>rst column is the name of the variable, which may be expressed in more than one way (e.g. sales velocity could be calculated as mean sales of a product for a period, but it can also be expressed in terms of how frequently a product is sold). The second column shows whether the variable is associated to the stockout or the OOS problem or both and the last column refers to pertinent work in the literature. Commenting on the <sup>fi</sup>rst row of the table, as an example, it can be said that faster moving items require either bigger shelf space or more frequent shelf replenishments in order to achieve the same levels of shelf availability as slower-moving items, implying a relation between this variable and the OOS problem. In addition, sales velocity is also associated to inventory levels and the stock-out problem.

Table 1  
Variables related to the problem

<table><tr><td>Variable</td><td>Problem addressed</td><td>Reference</td></tr><tr><td>Sales velocity</td><td>Stock-out/Out-of-shelf</td><td>[4]</td></tr><tr><td>Inventory level</td><td>Stock-out</td><td>[13,20]</td></tr><tr><td>Promotional product</td><td>Stock-out/Out-of-shelf</td><td>[26]</td></tr><tr><td>Shelf space</td><td>Out-of-shelf</td><td>[53,18,17]</td></tr><tr><td>Stock centralization</td><td>Stock-out</td><td>[12,42]</td></tr><tr><td>Market share</td><td>Stock-out/Out-of-shelf</td><td>[6]</td></tr><tr><td>Seasonality</td><td>Stock-out</td><td>[40]</td></tr><tr><td>Day</td><td>Out-of-shelf</td><td>[26]</td></tr><tr><td>Store size</td><td>Stock-out/Out-of-shelf</td><td>[26]</td></tr><tr><td>Employees</td><td>Out-of-shelf</td><td>[52]</td></tr><tr><td>Store managers decisions</td><td>Stock-out/Out-of-shelf</td><td>[10]</td></tr></table>

## 2.1. Measuring OOS

The recognition of OOS as a major problem in the retail sector has been based on the measurement of the phenomenon. All the available studies have been based on physical store audits, where a researcher visits the retail outlet and reports the status of the product or the status of the shelf. From the empirical point of view, availability (and consequently the OOS rate) might be determined in two different ways:

1. Measurement of product availability by determining whether a product is (or not) on the shelf.

2. Measurement of shelf availability through the identi<sup>fi</sup>cation of how many items are on the shelf divided by how many items could exist on the shelf when it is fully replenished.

The <sup>fi</sup>rst (and most popular) method examines if the product is on the shelf regardless of the number of available units. Thus, every product is characterized by a binary state (e.g. EXISTS or OOS). By summarizing the frequency of OOS observations, we get the OOS rate.

The shelf availability measurement method is slightly different since it assumes that a speci<sup>fi</sup>c shelf space is allocated to a single product and the idea is to estimate the load of this shelf space. Thus, the result of this measurement method is a continuous variable (shelf availability) ranging from full OOS (shelf availability = 0%) to a full shelf (shelf availability=100%).

Due to the nature of the retail store operations (e.g. the concurrent execution of shelf replenishment by the store personnel and the consumers' shopping) the product/shelf availability might change during the day. In order to overcome such an issue, it is possible to measure product/shelf availability more than once during the working hours of the store (e.g. measure product/shelf availability in the morning and again during the evening). Although repeated measurements could provide a more accurate insight of the product/shelf availability levels, the measurement frequency is subject to cost constraints.

In practice the measurement of OOS is initiated either by the supplier or the retailer. Due to resource and budget constraints, usually a sample list of products is composed, including representative products from various categories, and the measurements take place for a given time period (e.g. a week) and for prede<sup>fi</sup>ned outlets. Researchers visit the selected stores of the retail chain once a day (or seldom twice) and report which products are available (or not) at each store. This implies that most of the studies refer to product availability. However, in the following we use the term shelf availability study to refer to this process regardless of whether the measurements refer to shelf or product availability. These measurements are then used in order to estimate the OOS rate for the whole retail chain. Although this process might be valid from a statistical point of view, there are several factors undermining the validity of the measurement results, such as the following:

• Shelf-layout related factors: Consider that a product is on the shelf but is not visible to the consumer (e.g. at the top of the shelf) or the product is in the store but at a different position than what the consumer expected (e.g. at a promotional stand). This means that the consumer would assume that the product is not available. However, the researcher would strive to report correctly the status of the product on the shelf.

• Human related factors: This refers to the fact that the behavior of the store manager and the rest of the store personnel changes when conducting a shelf-availability study in the store, what is referred to as the Hawthorne effect [28]. Usually, the store manager interacts with the researcher and identi<sup>fi</sup>es the products marked as OOS in the store. As a response to this, the store manager takes care that the missing products are ordered and replenished as soon as possible. Moreover, the store personnel increase their commitment and replenish the shelf more frequently. In other words, when conducting store audits the reported results tend to present a more effective picture of shelf/product availability than on the normal days.

• Cost related factors: Due to budget constraints, most of the shelf availability studies monitor a sample product list for a limited number of stores in a speci<sup>fi</sup>c time window. Thus, the study does not address the dynamic changing states of the shelf for various product categories, but only provides a snapshot of what was the situation when the researcher visited the store.

The above factors give an indication of the various obstacles that exist in acquiring accurate and timely information regarding the extent of the OOS problem. Thus, it is a crucial requirement for the retail sector to have a single and uniform method that estimates product availability without having to conduct physical store audits, what we call automatic-detection approaches (or methods). The term “automatic” is used here not necessarily to imply high automation behind the method used, but mainly in order to emphasize the distinction between manual and systembased approaches.

A <sup>fi</sup>rst approach for the automatic detection of OOS is the use of store inventory data in order to calculate stock-outs as an approximation to OOS. However, this approach faces two serious problems. On one hand, it is unlikely to have perfect (accurate) inventory information, as also demonstrated by the study of Kang and Gershwin [32]. On the other hand, the cases where the product might be in the store (and is thus not a stock-out) but not on the shelf often exceed 30% of the reported OOS cases and can be as high as 60% or more [47]. That means that the automatic detection of OOS cannot rely on inventory data alone.

A second automatic-detection approach is the use of Radio-Frequency Identification (RFID) technology [43]. Using item-level RFID tags and several readers throughout the store it would be possible to track and locate every single item, thus determining product and shelf availability. However this enabling technology is not fully functional yet at this level and it is expected that it will take several more years before item-level tagging is widely adopted by the industry. Thus, this method will not be further examined in this paper.

A third approach has been proposed by ECR Europe, after a joint effort of retailers and suppliers in the European grocery retail sector, and is referred to as theOOS Index (or European OOS Index - EOI) [27]. Taking into account only fast moving items with low sales volatility, the OOS Index monitors the sales of the corresponding products on a daily basis; if for a given day a product sells zero items (or lower than a prede<sup>fi</sup>ned ceiling), then it is consider to be OOS. The problem that the OOS Index has is that it is relevant for only a very limited number of products, normally less than 5% of a typical product assortment found in grocery retail stores. The OOS Index will be used in this paper as a benchmark.

![](/api/attachments/5B2JPKD8/fulltext/images/67614d6db270909d1ec310e6ff9cd7c340c4b94f208081fd588f967909c056cd.jpg)  
Fig. 1. The Architecture of ISOS

A fourth approach, which is the proposition of this paper, suggests the automatic detection of OOS products based on a Rule-Based System. We propose that through the intervention of machine-learning methods it is possible to develop a Decision Support System for detecting the products that are not on the shelf, as described in the following section.

## 3. A DSS for the automatic detection of OOS

The DSS for the automatic detection of OOS proposed in this paper takes into account information that is currently available in any retail information system (e.g. sales data from the point-of-sales (POS data), orders, product assortment etc.) and according to some rules it detects products missing from the shelf in order to support respective decisions and corrective actions. The rules are drawn from previous known OOS examples, collected from physical store audits, and are extracted through several machine-learning algorithms. Similar approaches have been widely used in fraud-detection systems and anti-spamming software, but, to the best of our knowledge, this is the <sup>fi</sup>rst time this approach is used to address the OOS problem. The potential system users include: (a) the store managers, who wish to identify OOS situations and take corrective actions, (b) the sales manager(s) of the retail chain, who want to have a comparative view regarding the shelf availability performance of every store and make respective decisions and (c) the product suppliers, who, in this way, can monitor the status of their products in every store from a distance. We call this system ISOS and a general view of the system is depicted in Fig. 1.

The system consists of the following modules:

• Data Consistency Module: It is the module that communicates with existing information systems of the retailer and imports the required data every day. This module incorporates few heuristic methods to remove noise from the data.

• Attribute Measurement Module: This module implements all the required processes in order to calculate the measures and attributes for every product (e.g. average sales, days-to-sell etc.).

• Inference Module: This last module is aware of the rules of the system and applies them to all the products.

We assume that at the end of a working day all the required data are available in the existing information system of the retailer and are accessible by the proposed DSS. The <sup>fi</sup>rst step is to apply data cleaning procedures in order to minimize noise-in-the-data effects. Then the system calculates the prede<sup>fi</sup>ned attributes for every product and every store and <sup>fi</sup>nally applies the rules and creates the OOS list for every store. The OOS list may be sent to the respective users via e-mail or may be presented to the users over a web-interface, so that it is easily accessible to both the retail store managers and the product suppliers following the model of a web-based DSS [30].

Several design issues have been faced during the development of the DSS. One major issue has been the selection of the appropriate history of data to support the calculation of attributes. For instance, one product attribute used by the DSS is the average sales of a product. The selection of a long sales history (e.g. more than 12 months) might affect this attribute because of seasonal and advertisement effects, while the selection of a small period (e.g. less than 3 months) may not render adequate number of observations for all the products. Another consideration is the size of the data that can be handled ef<sup>fi</sup>ciently without affecting the response of the system. Thus, we selected a 6-month period as a convenient time-frame for the calculation of attributes based on historical data. The time frame is handled by the DSS as a sliding window, meaning that with the arrival of new data every day, the <sup>fi</sup>rst day of the time frame is removed and all the attributes are calculated based on the new set of data.

Other important design issues refer to selecting the data that should be used as well as the logic applied in deciding whether a product is OOS or not. In the next sections we provide some details regarding the data utilized by the DSS, the reasoning for selecting a heuristic approach versus an analytical one and <sup>fi</sup>nally the iterative steps used to build the system.

## 3.1. Available data

The data available for our research are falling into two broad categories. The <sup>fi</sup>rst category refers to data coming from the internal information system of a retailer, while the other includes data coming from physical audits (visits at the store to determine if a product is on the shelf or not).

Speci<sup>fi</sup>cally, the data coming from the retailer information system, which are typically maintained by the majority of retailers worldwide, include:

• Points-of-Sales (POS) Data: The sales data collected by the automatic scanning systems at the cashiers of the store. The POS data are recorded by the system on a daily base.

• Product Assortment: The set of products that a store is merchandizing at a given point in time. Obviously, only products belonging to the active assortment need be checked for OOS. The product assortment may be different from store-to-store, depending on the store size, and from dayto-day, due to product introductions or discontinuations.

Table 2 Sample of shelf availability list

<table><tr><td colspan="6">Date of visit: Store: AVAILABLE ON Time of visit: SHELF</td></tr><tr><td>SKU code</td><td>Category</td><td>Subcategory</td><td>Description</td><td>EXISTS</td><td>OOS</td></tr><tr><td>16462</td><td>ALCOHOL</td><td>GIN</td><td>GIN GORDONS 700 ML</td><td></td><td></td></tr><tr><td>402125</td><td>REFRESHER</td><td>COLA</td><td>COCA COLA BOTTLE 500 ML</td><td></td><td></td></tr><tr><td>803418</td><td>GENERAL DETERGENT</td><td>DAILY HOME USE</td><td>GLORY LIQUID 750 ML</td><td></td><td></td></tr><tr><td>899911</td><td>HAIR SHAMPOO</td><td>FOR WOMEN</td><td>ORGANICS NATURAL CREAM 250 ML</td><td></td><td></td></tr><tr><td>....</td><td>......</td><td>......</td><td>......</td><td></td><td></td></tr></table>

• Product Categories: A tree structure linking categories, subcategories and products and describing the (sub)category(ies) a product belongs to.

• Product Catalogue: A list of all the products that the retail chain merchandizes.

• Orders/Deliveries: A log of the products ordered by the store and the products delivered to the store.

While other pieces of information may be highly relevant to the OOS problem, such as the shelf position and space allocated to a product, these were not used in our study, as they were not available and are not usually maintained in retail information systems.

Based on these data, several attributes are calculated for each product on a daily basis. These attributes are a core element of the system, as they represent the independent variables of the problem. Attributes that were initially de<sup>fi</sup>ned include average sales and standard deviation for a sixmonth period, average sales and standard deviation for speci<sup>fi</sup>c days of the week, e.g. Saturday versus Monday average sales, average number of items sold per day, etc. After a closer inspection of the available data and based on recommendations from market experts, more attributes were de<sup>fi</sup>ned, especially in relation to the non-selling days of a product, as the large majority of products had less than one sale per day. Thus, further attributes were included in the study, such as the average number of days between two consecutive sales of a product and respective standard deviation and the average number of days since a product's last selling date.

The data coming from the store audits record product availability, i.e. describe whether a speci<sup>fi</sup>c product was found on shelf or not during a speci<sup>fi</sup>c visit, once per day. Table 2 presents a sample shelf availability list completed during a physical audit. Products were monitored at the stock-keeping-unit (SKU) level, i.e. there was no distinction between regular and promotional products of the same type.

## 3.2. Choosing the approach: analytical vs. heuristic

In order to de<sup>fi</sup>ne the logic that should be followed by the DSS in detecting OOS situations, we examined several analytical models and methods (e.g. inventory control models, demand forecasting etc.). However we found that the information records describing the holding inventory were highly inaccurate, which is in turn con<sup>fi</sup>rmed by the literature [32]. We further examined the possibility to analytically model the demand of a single product using well known theoretical statistical distributions (like normal, exponential and Poisson). In doing so, we examined a six-month-sales period for all the products merchandized by few stores, considering the demand time-series of each product including working days with zero demand, and we used the goodness-of-<sup>fi</sup>t statistical test. Taking into account a small number of degrees of freedom (dfb10) and for various levels of signi<sup>fi</sup>cance, we found that only about 3% of the products follow a statistical distribution with high level of signi<sup>fi</sup>cance (aN 0.8). Reasons of the low <sup>fi</sup>t are the <sup>fl</sup>uctuations of demand due to advertisement effects, the different sales volumes during and at the end of the week, possible seasonal patterns etc.

In general, we found that it is very dif<sup>fi</sup>cult to estimate the expected demand pattern for products at store level as a basis to identify OOS situations. This means that existing analytical models could not be utilized to support the logic of the DSS and we, thus, chose to follow a heuristic approach.

![](/api/attachments/5B2JPKD8/fulltext/images/9e0c9028dccf3b2084863d0716647a602923c35e405fe74cbbe271d1bf7d70f5.jpg)  
Fig. 2. The iterative process of developing the rules: a sequence of experiments

A sample learning set

<table><tr><td>SKU code</td><td>Store size</td><td>Last POS</td><td>Average sales</td><td>Stdev sales</td><td>...</td><td>Class</td></tr><tr><td>15362</td><td>Large</td><td>17</td><td>21.43</td><td>12.7</td><td>...</td><td>EXISTS</td></tr><tr><td>302123</td><td>Medium</td><td>0</td><td>0.326</td><td>2.382</td><td>...</td><td>EXISTS</td></tr><tr><td>713318</td><td>Medium</td><td>1</td><td>0.643</td><td>1.9373</td><td>...</td><td>EXISTS</td></tr><tr><td>990012</td><td>Small</td><td>0</td><td>0.0227</td><td>1.037</td><td>...</td><td>OOS</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>....</td><td>...</td><td>EXISTS</td></tr></table>

The baseline idea was to discriminate the products into two sets (EXISTS/OOS) corresponding to the availability on the shelf. In principle, this de<sup>fi</sup>nes a classi<sup>fi</sup>cation (or discrimination) problem as found in the areas of Statistics and Machine Learning. A series of algorithms (e.g. Naïve Bayes, Bayes Networks, C4.5, RIPPER etc.) have been developed to classify new and unknown examples based on the patterns that have been discovered from known cases. Important and rigorous literature has been proposed over the last decades ([44,2,51,22]), while several classi<sup>fi</sup>cation systems are also found in the area of Decision Making ([32–35,39,50]). In the following section we describe the iterative process we followed in order to develop and test speci<sup>fi</sup>c (heuristic) rules that have the ability to correctly detect OOS products following this approach.

## 3.3. Developing the rules

The development of the heuristic rules was based on an iterative process between collecting examples of product availability, applying classi<sup>fi</sup>cation algorithms to identify patterns of OOS behavior and then validating these patterns against actual observations. Speci<sup>fi</sup>cally, each phase in this iterative process was an experiment consisting of the following three steps:

1. Physical Audit: As already explained, this is currently the most widespread method used to detect OOS situations and measure the problem in retailing. Physical audits were used in order to collect actual examples of product availability.

2. Building Classifiers: A classi<sup>fi</sup>cation algorithm gets as input labeled examples (i.e. known examples classi<sup>fi</sup>ed as EXISTS or OOS) and makes a classi<sup>fi</sup>cation model, i.e. a set of rules classifying products as EXISTS of OOS based on their attribute values. This model is what the algorithm has learned from the known examples and, ideally, can be used in order to classify new and unlabeled examples. The prediction accuracy and the generalization ability of the model are the major concerns.

3. Validation: The last step addresses the issues of internal and external validity of the classi<sup>fi</sup>cation model. The internal validity deals with how accurate the classi<sup>fi</sup>cation model is for the available examples, while the external validity examines the effectiveness of the classi<sup>fi</sup>cation model in new and unclassi<sup>fi</sup>ed examples. Internal validity is examined by separating the whole learning set into a training and a test set and the latter is then used in order to examine the predictive accuracy of the system. The external validity requires a physical audit in order to examine if the classi<sup>fi</sup>cation model is applicable and can therefore be employed in practice.

Fig. 2 depicts this iterative process. The various experiments are not independent because the external validation of the previous experiment is conducted by a physical audit which is the baseline of the next experiment.

At the end of each experiment a set of rules has been de<sup>fi</sup>ned. This is the sum of the already known rules from previous experiments, augmented by the ones discovered during the current experiment, leaving out those that have underperformed during the validation step.

In the next section we describe three different experiments we have conducted in order to develop the required solution for the automatic discovery of OOS situations.

## 4. Experimental design of the system

For the purpose of the research we conducted three different experiments, following the three steps as described above. The <sup>fi</sup>rst experiment is called Initialization, the second Extension while the last one is called Refinement. For almost two years we focused on settingup the experiments, analyzing the data, building the system and coming-up at the end with a concrete solution. Each experiment is brie<sup>fl</sup>y discussed in the next paragraphs.

## 4.1. Initialization experiment

The <sup>fi</sup>rst experiment was initiated by a physical audit in order to collect examples of product availability. For a time period of one week, nine different retail stores were selected and 109 different SKU's were monitored regarding shelf availability. These SKU's were selected to form a representative set using strati<sup>fi</sup>ed sampling based on sales velocity and product category. At the end of the physical audit we had 5886 examples available (both EXISTS and OOS). In addition, we got all the required data from the retail information system (e.g. 6-month POS Data for the nine stores, orders and deliveries of all the SKU's etc.) and calculated the aforementioned attributes for every example case of the physical audit. This process rendered what we call a Learning Set, as shown in Table 3.

The rows in Table 3 correspond to speci<sup>fi</sup>c instances of a product at a certain store and date, while the columns correspond to the attributes calculated based on the available data discussed in section 3.1, i.e. the independent variables. The last column is the dependent variable derived from the physical audits. The learning set is the collection of the labeled examples and it may be handled from a classi<sup>fi</sup>cation algorithm in order to discover patterns (classi<sup>fi</sup>ers). However it is a common practice to divide randomly the learning set into two individual sets: (a) the training set and (b) the test set. The training set is provided to the classi<sup>fi</sup>cation algorithm in order to learn from examples and develop a classi<sup>fi</sup>cation model, while the test set is used to calculate the misclassi<sup>fi</sup>cation cost. This process is called Cross-Validation [49]. Eight different learning sets were de<sup>fi</sup>ned based on the example cases from the physical audit and using different calculated attributes. More speci<sup>fi</sup>cally, four of the learning sets were de<sup>fi</sup>ned in order to correct noise-in-the-data effects. For example the second learning set differed from the <sup>fi</sup>rst original one in that it did not contain those OOS cases that referred to products that had not been delivered to the store during the last 6 months and have, thus, been probably de-listed. The next four learning sets were based on these four ones but introduced different calculated attributes, such as a new attribute combining the sales average and standard deviation in one measure, which may work more ef<sup>fi</sup>ciently in case there is noise in the data. The reason we de<sup>fi</sup>ned eight different learning sets instead of just one was in order to control the effect of the learning set as well as of the calculated attributes on the development of the classi<sup>fi</sup>cation model.

Table 4 List of classi<sup>fi</sup>cation algorithms

<table><tr><td>Statistical</td><td>Machine Learning</td><td>Neural Networks</td></tr><tr><td>Bayes network [11]Naïve Bayes [45]Multinomial logisticClassification [3]Support vectors machine [7]</td><td>IBk [2]KStar [14]Alternating decision tree [23]C4.5 [44]Naïve Bayes tree [37]Logistic model tree [38]Random forest [8]Decision table [36]RIPPER [15]Ripple down rules [25]</td><td>MLP [48]Radial basis function [41]</td></tr></table>

Table 5  
Table 6  
The Confusion Matrix

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Classified as</td><td rowspan="2">Class</td></tr><tr><td>Negative</td><td>Positive</td></tr><tr><td rowspan="2">Observed</td><td>Negative</td><td>A</td><td>B</td><td>EXISTS</td></tr><tr><td>Positive</td><td>C</td><td>D</td><td>OOS</td></tr></table>

Another issue examined during the Initialization phase was the selection of the appropriate classi<sup>fi</sup>cation algorithms. For the purpose of our study, we grouped the classi<sup>fi</sup>cation algorithms into three categories (statistical, machine-learning and neural networks) based on the structure of the output classi<sup>fi</sup>ers. In principle, the classi<sup>fi</sup>ers of statistical algorithms are described through a set of probability functions, while the machine-learning algorithms develop rules (IF-THEN) and neural-networks provide a topology (network) with the appropriate weights. The algorithms examined during the Initialization phase are listed in Table 4.

Every algorithm addresses the same (classi<sup>fi</sup>cation) problem, but putting all the pieces together into a single decision support system might be a complex procedure, because of the nature of each classi<sup>fi</sup>er. Thus, we conducted ANOVA tests to compare the overall ef<sup>fi</sup>ciency of each category of algorithms and we found that the most appropriate algorithms for the OOS problem are those belonging to the machinelearning category.

The last steps of the Initialization phase were to create Training and Test Sets, feed each one to the classi<sup>fi</sup>cation algorithms belonging to the machine-learning category, collect the classi<sup>fi</sup>er models and <sup>fi</sup>nally select the most appropriate rules. Thus, the last step was to develop classi<sup>fi</sup>ers and utilize speci<sup>fi</sup>c techniques to examine the internal validity of every classi<sup>fi</sup>cation model and make comparisons in order to select the best classi<sup>fi</sup>cation model for every Learning Set.

In order to compare the classi<sup>fi</sup>cation models and evaluate the respective rules we used the Confusion Matrix (Table 5). A confusion matrix is an array showing relationships between true and predicted classes. Each row in the confusion matrix represents an observed class, each column represents a predicted class and each cell counts the number of examples in the intersection of these two classes. Obviously, the ideal model should have the quantities B and C equal to zero.

Based on the Confusion matrix, we identi<sup>fi</sup>ed two relative measures. The <sup>fi</sup>rst is the Support (or Coverage) which shows how many cases of OOS were correctly identi<sup>fi</sup>ed (quantity D) from the whole available examples of OOS (sum of C and D). The second measure is called Accuracy (or Confidence) and describes how many OOS cases were correctly identi<sup>fi</sup>ed divided by the total number of examples described as OOS from the classi<sup>fi</sup>cation model (sum of B and D). The analytical form of Support and Accuracy follows.

$$
\mathrm{Support} = \frac {D}{C + D}\tag{1}
$$

$$
\text { Accuracy } = \frac {D}{B + D}\tag{2}
$$

These two measures are competitive, as stated in the literature and observed in our experiments [1,22,44]. For example, a classi<sup>fi</sup>cation model with high Accuracy is likely to have low Support. In other words, a classi<sup>fi</sup>cation model with high predictive accuracy tends to identify correctly OOS cases that are easy to capture (e.g. a product that has not sold a unit for more than 40 days). However, in such a case the measure of Support would be very low, because several OOS examples would not be detected by the classi<sup>fi</sup>cation model (large value for the C quantity in the confusion matrix).

Performance of classi<sup>fi</sup>cation algorithms for different learning sets

<table><tr><td></td><td>Selected classification algorithm</td><td>Total performance</td><td>Number of candidate rules</td></tr><tr><td>Learning set 1</td><td>Random Forest</td><td>0.665±0.02</td><td>68</td></tr><tr><td>Learning set 2</td><td>NB Tree</td><td>0.511±0.07</td><td>59</td></tr><tr><td>Learning set 3</td><td>RIPPER</td><td>0.77±0.03</td><td>43</td></tr><tr><td>Learning set 4</td><td>C4.5</td><td>0.604±0.06</td><td>84</td></tr><tr><td rowspan="3">Learning set 5</td><td>RIPPER</td><td>0.642±0.03</td><td>28</td></tr><tr><td>C4.5</td><td>0.672±0.04</td><td>76</td></tr><tr><td>NBTree</td><td>0.664±0.03</td><td>38</td></tr><tr><td>Learning set 6</td><td>C4.5</td><td>0.514±0.06</td><td>64</td></tr><tr><td>Learning set 7</td><td>RIPPER</td><td>0.746±0.04</td><td>28</td></tr><tr><td rowspan="2">Learning set 8</td><td>NBTree</td><td>0.561±0.08</td><td>46</td></tr><tr><td>C4.5</td><td>0.61±0.05</td><td>55</td></tr></table>

In order to overcome this problem we employed a measure called Total Performance which is de<sup>fi</sup>ned as the harmonic mean of Support and Accuracy. This implies the search for a balanced classi<sup>fi</sup>cation scheme: we need to identify several OOS cases while keeping low error levels. The Total Performance is calculated as follows:

$$
\text { TotalPerformance } = \frac {2 ^ {*} \text { Support } ^ {*} \text { Accuracy }}{\text { Support } + \text { Accuracy }}\tag{3}
$$

The Total Performance measure has been empirically shown that is appropriate for comparing classi<sup>fi</sup>ers when the data are characterized by the class imbalance problem [31]. The measure of Total Performance was examined for all the algorithms belonging to the machinelearning category using 10×2 Cross Validation and t-test to identify statistical signi<sup>fi</sup>cant difference between the algorithms. The comparisons had been conducted with level of signi<sup>fi</sup>cance a=0.001. Table 6 presents the results from this comparison.

The last column of the table presents the number of rules created by the classi<sup>fi</sup>cation algorithm. In general from all the selected classi<sup>fi</sup>cation algorithms we identi<sup>fi</sup>ed almost 600 rules addressing the problem of OOS. However not all of them are appropriate to predict new OOS cases, thus the following selection criteria were applied:

• The con<sup>fi</sup>dence of the rule in the test set should be greater than 0.8. This means that it correctly classi<sup>fi</sup>es more than 80% from the external examples. We call them external examples since they did not contribute to the learning phase of the classi<sup>fi</sup>er.

• The length of the rule should not be long, because this is an indication that the rule suffers from over-<sup>fi</sup>tting.

The application of the selection criteria revealed 157 rules from all the classi<sup>fi</sup>cation schemes. Because the learning sets were not independent, we further identi<sup>fi</sup>ed 30 common rules, thus the <sup>fi</sup>nal rule set contained 127 rules, which were considered as the <sup>fi</sup>rst solution to the OOS problem. The next task was to embed these rules into the rule-based Decision Support System and study the detection effectiveness of each rule as well as of the whole system.

The next table (Table 7) presents some indicative rules, as have come out of this process. The variables used in the rules correspond to the product attributes calculated based on the available data, as

## Table 7

Performance of classi<sup>fi</sup>cation algorithms for different learning sets

IF (average\_total b0.05) and (lastzerosequence b97) and (stdv\_total b0.22) and (zeros\_avgb1.71) THEN OOS

IF (lastzeroseqN=21) and (average\_totalN=1.217742) THEN OOS

IF (store\_size=small) and (lastzeroseqN=107) THEN OOS

IF (lastzeroseq N= 18) and (average\_total b= 0.03) and (zeros\_std N= 25.5) and (average\_totalN=0.02) THEN OOS

IF (lastzeroseq N= 6) and (average\_total b= 0.04) and (zeros\_avg b= 21.83) and (lastzeroseqb=19) THEN OOS

The Con<sup>fi</sup>dence and Support measures for the overall system

<table><tr><td>Test set</td><td>Confidence level</td><td># of rules</td><td>Confidence/accuracy</td><td>Support/coverage</td></tr><tr><td rowspan="3">TeS1</td><td>=1</td><td>46</td><td>1</td><td>0.26813</td></tr><tr><td>[0.8, 1]</td><td>50</td><td>0.951261</td><td>0.270038</td></tr><tr><td>[0.5, 1]</td><td>56</td><td>0.768725</td><td>0.279103</td></tr><tr><td rowspan="3">TeS2</td><td>=1</td><td>35</td><td>1</td><td>0.297302</td></tr><tr><td>[0.8, 1]</td><td>43</td><td>0.910565</td><td>0.315612</td></tr><tr><td>[0.5, 1]</td><td>56</td><td>0.742647</td><td>0.340668</td></tr><tr><td rowspan="3">TeS3</td><td>=1</td><td>35</td><td>1</td><td>0.323016</td></tr><tr><td>[0.8, 1]</td><td>43</td><td>0.911591</td><td>0.343475</td></tr><tr><td>[0.5, 1]</td><td>54</td><td>0.754578</td><td>0.362098</td></tr><tr><td rowspan="3">TeS4</td><td>=1</td><td>19</td><td>1</td><td>0.031815</td></tr><tr><td>[0.8, 1]</td><td>28</td><td>0.923611</td><td>0.082969</td></tr><tr><td>[0.5, 1]</td><td>47</td><td>0.747126</td><td>0.162196</td></tr><tr><td rowspan="3">TeS5</td><td>=1</td><td>14</td><td>1</td><td>0.023235</td></tr><tr><td>[0.8, 1]</td><td>23</td><td>0.901155</td><td>0.155344</td></tr><tr><td>[0.5, 1]</td><td>42</td><td>0.754799</td><td>0.191414</td></tr><tr><td rowspan="3">TeS6</td><td>=1</td><td>6</td><td>1</td><td>0.014551</td></tr><tr><td>[0.8, 1]</td><td>22</td><td>0.883333</td><td>0.05282</td></tr><tr><td>[0.5, 1]</td><td>43</td><td>0.717458</td><td>0.186765</td></tr></table>

previously explained. For example, the variable average\_total and stdv\_total refer to a product's average sales and respective standard deviation during the whole period, while the variable lastzerosequence refers to the number of non-selling days since the last sale. The variables that were included in the selected 127 rules give an indication of the attributes that are more important in classifying the OOS cases, as not all of them were included in the <sup>fi</sup>nal set of selected rules. These include (in descending order of occurrence): number of days between two consecutive sales of a product, store size, average daily sales in a six-month period, product type, and day of the week.

## 4.2. Extension experiment

In order to examine the detection capabilities of the Decision Support System, a physical study was conducted for a second time. As an alternative approach, a different process was followed at this stage during the physical audits in 6 different retail outlets. The process was the following:

1. Visit the store once daily.

2. Use random walks in the store and discover OOS products.

3. Write the codes and inspect in detail the whole category where an OOS was found.

After 15 days we collected a list of OOS single cases (more than 3000 counts) and expanded the list with EXISTS cases as derived from the POS Data, forming a single test set (with 28,500 counts). Note that for every single OOS case we were adding 10–14 different EXISTS cases, in order to maintain the distribution close to 8% which is the world average OOS rate. Based on the assumption that “if a product had been found OOS for a certain day, then this product would have been OOS for all the previous days that it had not sold any item”, we expanded the OOS cases as well as the EXISTS cases in the way described above, deriving a larger test set (TeS2 - 56,000 counts). Finally, taking into account that “if the day of last sale for an OOS product was within the 15-day horizon of the physical audit, then this should be an OOS case for the respective days” and adding further EXISTS examples we created the <sup>fi</sup>nal and largest test set (TeS3 - 80,000 examples). Moreover, by examining the data we found that some OOS cases of the physical audit referred to products that had sold their last unit more than a month ago. Thus, we decided to remove these inaccurate OOS examples and take into account only the examples that had sold an item during the last 30 days. This process resulted in the creation of three more test sets (TeS4, TeS5 and TeS6). At the same time, the Decision Support System was producing OOS lists for each of the 15 days of the trial period.

The next table (Table 8) presents the evaluation results of the detection system for the various test sets. Note that the rules had been developed based on different training sets and were able to detect the OOS cases in a new and totally unknown test set, as has been our objective. For the <sup>fi</sup>rst three test sets, the results are satisfactory since with high Accuracy (N90%) the system could detect about 30% of the OOS cases of the test set (Support), through the utilization of 40–50 rules from the initial solution. This result is quite “suspicious”, considering the diversity of OOS cases and the complexity of the problem and this was the reason for developing the updated test sets (TeS4, TeS5 and TeS6).

As mentioned above, the TeS4, TeS5 and TeS6 test sets excluded OOS cases that were outdated (i.e. products that had not sold for more than 30 days). The results for Accuracy and Support are low for these training sets, revealing that the initial solution is biased towards detecting OOS products that have not been in the store for a long time (either stock-out or de-listed products), which are relatively easy to capture. We thus decided to concentrate our efforts on the last 30- day-time-frame and build classi<sup>fi</sup>ers only from the last three test sets.

The procedure followed in this experiment was simpler compared to the initialization experiment. We used only 8 different classi<sup>fi</sup>cation algorithms (Decision Trees and Rule based learners) and utilizing 10×2 Cross Validation t-paired test we found the best classi<sup>fi</sup>cation algorithm for each training set. We also extended the independent variables and added three new attributes. Finally, we used again a selection procedure to identify the appropriate rules from the set of candidate rules. At the end of the process, we added 116 new rules to the Decision Support System, keeping 38 rules from the initial solution.

## 4.3. Refinement experiment

The objective of the re<sup>fi</sup>nement experiment was the re-examination of the detection capabilities of the system based again on a physical audit. The three major issues examined were: (a) the overall Accuracy of the system, (b) the Support of the system and (c) how timely an OOS case is detected by the system, as an additional evaluation criterion.

The physical audit was based on the OOS lists produced by the system. That meant that we did not know how many were the total number of OOS cases occurring in the store during a day, which would be necessary to know in order to measure the Support of the system. In order to overcome this limitation, we estimated an average number of OOS cases for every store, based on the fact that around 5% of the products are not on the shelf. Although the worldwide average of OOS is calculated at the 8% as mentioned in the introductory section, we observed from physical audits (during the initialization and extension experiments) that the retail chain of our research had an average OOS rate of 5%.

![](/api/attachments/5B2JPKD8/fulltext/images/6623692d3dc7b5143e54a46cb2551c32e800208168c0c0badd14aa28bcd5e7cd.jpg)

![](/api/attachments/5B2JPKD8/fulltext/images/8d6c38a44b186f0dee9dbdca50e7e35afdb081c74a3654e8cf682617895356c5.jpg)  
Fig. 3. The cases of timely (a) and late (b) detection.

Table 9  
Different Versions of the ISOS system

<table><tr><td rowspan="2">System version</td><td colspan="2">Number of rules</td><td rowspan="2">Attributes supported</td><td rowspan="2">History of data used</td><td rowspan="2">Supported functionality</td></tr><tr><td>Before validation</td><td>After validation</td></tr><tr><td>ISOS ver. 1</td><td>127</td><td>35</td><td>19</td><td>6-month</td><td>· Use product assortment data to determine which products to monitor· Remove outliers from POS Data</td></tr><tr><td>ISOS ver. 2</td><td>154</td><td>58</td><td>22</td><td>6-month and 14-month</td><td>· Identify products that are in the store· Extra features to remove noise from the data· A product that has been mentioned as OOS would not be monitored the next day· Focus on early detection of an OOS case by adoption of special-purpose attributes</td></tr></table>

We visited six different stores for 2 weeks. Every day we were getting the OOS list by the system, which was produced based on the POS data of the previous day, and were checking whether the system predicted correctly an OOS case or not. During this validation phase we found that, with high Accuracy (N90%), the system could detect approximately 27% of the real OOS cases occurring in the store. In addition, after the physical audit was completed, we were able to calculate how timely the system had detected the OOS products.

As graphically depicted in Fig. 3, we de<sup>fi</sup>ned two different cases to describe the time-frame of the detection. A timely detection happens when the system detects the OOS before the expected next sale. The time of the expected next sale (μ⁎) is calculated as the mean number of days between two consecutive sales for a speci<sup>fi</sup>c product. If the system detects the OOS case later than the expected next sale, then we argue that the retailer suffered from lost sales. We found that the system could timely detect about 35% of the OOS cases, usually capturing slowmoving items. Moreover, we saw that the system could correctly detect these OOS cases no later than 3 days after the last sale.

Furthermore, during the re<sup>fi</sup>nement experiment we observed some qualitative <sup>fi</sup>ndings. Speci<sup>fi</sup>cally, during the <sup>fi</sup>rst week of the experiment, we realized that in some cases the system falsely identi<sup>fi</sup>ed products as OOS, but these products were not easy to locate on the shelf. We thus de<sup>fi</sup>ned three problematic situations: (1) the product was not visible on the shelf (e.g. was at a very top or bottom corner), (2) the product was in bad shape and (3) only one unit was on the shelf. The next week of the physical study we also examined these situations and found that, in about 35% of the cases that the system had falsely detected a product as OOS, this referred to a product falling into one or more of the aforementioned problematic situations. This means that although the rules had falsely classi<sup>fi</sup>ed a product as OOS, from a qualitative consumer perspective this might have been a “correct” detection, rendering the system more informative than just detecting OOS cases.

## 5. Using the system

Two different versions of the rule-based Decision Support System were built, each one encapsulating the lessons from the respective experiment: ISOS Ver.1 after the Initialization phase and ISOS Ver. 2 after the Extension phase. The next table (Table 9) summarizes the characteristics of these two different versions of ISOS.

The backbone of the ISOS system is the inference engine as composed by the rules. The ISOS Ver.1 initially had 127 different rules and after the validation procedure we kept only 35 in order to <sup>fi</sup>netune the detection effectiveness of the system. These 35 rules were embedded in the next version of ISOS together with the new rules identi<sup>fi</sup>ed during the Extension phase. The ISOS Ver. 2 was initially designed with 154 different rules and after the validation we have chosen 58 rules.

Each version was compared to the detection capabilities of the European OOS Index, based on the results of the physical store audits. The next <sup>fi</sup>gure presents the Accuracy and Support of ISOS Ver.1 versus the European OOS Index (Fig. 4).

It is easy to observe that the Accuracy of the OOS Index is much lower than that of ISOS Ver.1. We examined the accuracy for three different test data sets (small, medium and large size). In all the cases the accuracy of the OOS Index was below 50%, which meant that less than half of the products the European OOS Index detected (proposed) were real OOS cases. The ISOS Ver.1 system seemed to perform much better with more than 90% Accuracy, as calculated after the validation phase and based on the 35 effective rules.

As far as the Support measure is concerned, we observe that the European OOS Index has very limited scope. Speci<sup>fi</sup>cally, the test data sets contained between 1800 and 3000 different OOS examples and the OOS Index could detect less than 60 of them, referring to fast-moving products (i.e. products selling more than 10 items per day). However, our experimental data suggest that most of the OOS cases appear in the slower-moving segment. In addition, the fast moving items are highly visible in the store, as they usually hold big shelf space, so if this shelf space is empty then the store employees can easily notice it during a day. It is thus recommended that for an OOS detection system to be useful in the case of fastmoving products, this should work on an hourly rather than on a daily basis.

![](/api/attachments/5B2JPKD8/fulltext/images/2aa9d62194cdd606a123be30c30179acff0b034bbb2736d99c73b37a19da8fe5.jpg)

![](/api/attachments/5B2JPKD8/fulltext/images/22b05e9e9c98a665afd2d891ab451c64cf323b6f26b2ce09282ef54cd2383cdc.jpg)  
Fig. 4. Comparison of accuracy and support between European OOS Index and ISOS Ver. 1.

Table 10  
Overview of detection capabilities for the examined mechanisms

<table><tr><td>Detection mechanism</td><td>ISOS Ver.1</td><td>OOS Index</td><td>ISOS Ver.2 (6-month)</td><td>ISOS Ver.2 (14-month)</td></tr><tr><td>Accuracy</td><td>92%</td><td>36%</td><td>92%</td><td>94%</td></tr><tr><td>Support</td><td>13%</td><td>0.27%</td><td>27%</td><td>18%</td></tr></table>

The ISOS Ver. 1 system performed much better than the European OOS Index in terms of the Support measure, but we considered this performance low, as 85% of the OOS cases were still not captured. Our efforts to increase the Support of the solution have rendered ISOS Ver.2.

The improvements were sought towards the following directions:

• Development of new rules

• Design of new attributes and removal of redundant ones

• Better handling of information quality issues and noise-in-the-data effects

• Increase of history data from 6 months to 14 months

The increase of the history data time horizon was based on the expectation that the larger the set of data used, the better the measurement of the product attributes and, consequently, the more accurate the inference engine would be. This decision resulted in the development of two different instances of the same system: (a) ISOS Ver.2 (6-month) and (b) ISOS Ver.2 (14-month).

The next table (Table 10) summarizes Accuracy and Support for all four detection mechanisms examined.

ISOS as a detection approach seems to achieve high levels of Accuracy, which means that the system correctly predicts OOS products. However, none of the detection mechanisms could cover all the different OOS cases occurring in the store, resulting in rather low levels of Support. Judging from the increase in Support achieved between ISOS Ver. 1 and ISOS Ver. 2 (from 13% to 27%), we believe that the Support of ISOS could further be increased through more experimental iterations and larger scale trials.

## 6. Conclusions and future research

The research presented in this paper suggests that a rule-based Decision Support System, based on machine-learning techniques, can assist in the automatic detection of products missing from retail shelves. Such a system can help a retail chain increase its pro<sup>fi</sup>tability, by measuring and controlling the OOS situations, thus avoiding lost sales. The OOS problem is very dif<sup>fi</sup>cult to monitor through automated means, but the suggested heuristic approach provides satisfactory results. We have shown how to utilize existing data to support such an application and conduct continuous experiments in order to increase the solution's detection capabilities. The challenge is to reach a solution with an appropriate trade-off between Support and Accuracy. From our experiments we found that with Accuracy greater than 90% the system is able to detect about one third of the OOS cases occurring daily in the store.

Taking into account the cases of timely OOS detection, i.e. the cases where the OOS detection occurs before the expected next sale, we are able to calculate the economic impact of the system. Speci<sup>fi</sup>cally, taking into account the number of OOS cases detected on time and assuming that the consumer response to an OOS in about 9% of the cases is a lost sale [26] – which can be avoided by using the system – we estimate a 0.37% sales increase for the retail chain. For the product supplier the economic impact can be even higher, as the consumer response to an OOS is often the purchase of a substitute product, not taken into account in the previous calculation. This is a rather conservative estimate, as it does not consider the longer-term bene<sup>fi</sup>ts from increased consumer loyalty associated with lower OOS levels [46].

Using data from a different retail chain and following the same procedure for the development of rules, we ended up with different classi<sup>fi</sup>ers. This fact suggests that the rules deployed in the context of a retail chain might not be transferable in general to another retail chain. This can be attributed to the fact that there are differences in the processes and organizational aspects of a retail chain which are depicted in the retail chain's information model and data (e.g. ordering processes, product assortment, promotional events etc.). Thus, the proposed Decision Support System needs to be further validated and possibly incorporate a different set of rules before it is employed in the context of a different retail chain.

From the empirical work it has been made possible to investigate speci<sup>fi</sup>c theoretical questions as well. An interesting <sup>fi</sup>nding has been the inability to ef<sup>fi</sup>ciently model the demand of a single product selling at a retail store using a theoretical statistical distribution [29]. This constraint should be taken into account when developing models in the area of sales forecasting and inventory management where such a modeling approach is not rare. We argue that models assuming that the demand follows a certain statistical distribution are not expected to be validated in real life applications at the retail store for the majority of products. Another <sup>fi</sup>nding relates to the usage of different machine-learning algorithms. In our case, we found that the most appropriate algorithms are those coming from the area of Decision Trees. This has been rather expected as an outcome, since the structure of decision trees allows to discriminate the OOS examples in a more <sup>fl</sup>exible way compared to the Neural Networks and Statistical algorithms [5,8]. Neural Networks seem to suffer from the class imbalance problem, which is frequent in real life applications, while Statistical algorithms were confused by problems such as white noise and missing values in the data [19,24]. Last but not least, this work has helped de<sup>fi</sup>ne and validate the variables that can be calculated based on the available data and partly explain the OOS problem, taking into account the occurrence of these variables in the <sup>fi</sup>nal set of selected rules. However, further research is required in order to clearly identify the variables that play a more important role than others in classifying the OOS cases.

As a closing remark, we can refer to some aspects of the system that present opportunities for further research. More analysis may be conducted in order to better understand the OOS cases identi<sup>fi</sup>ed by the system and those that are not. For example, does the system perform better for faster than slower moving items or for certain product categories? Currently all the rules are equally important in deciding if a product is OOS or not. However, it is possible to associate a different weight to each rule, so that the OOS products are detected via a voting mechanism. Another aspect of the system worth further investigating is the system's adoption and acceptance by the users. The store managers may not feel comfortable with such a monitoring system, as, in addition to help address the OOS problem, it may be used to compare the stores' performance. In addition, new opportunities for research in the area of supply chain collaboration are presented, as the system can be used both by retailers and suppliers as a web-based DSS over an Internet platform.

## References

[1] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, ACM SIGMOD Record 22 (2) (1993).

[2] D. Aha, D. Kibler, M. Albert, Instance-based learning algorithms, Machine Learning 6 (1991).

[3] J. Anderson, Separate sample logistic discrimination, Biometrika 59 (1972).

[4] R. Anupindi, M. Dada, S. Gupta, Estimation of consumer demand with stock-out based substitution: an application to vending machine products, Marketing Science 17 (1998).

[5] R. Bayardo, R. Agrawal, Mining the most interesting rules, Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 1999, San Diego.

[6] D. Bell, G. Fitzsimons, An experimental and empirical analysis of consumer response to stockouts, Working Paper #00-001, Wharton Marketing Working Papers Series The Wharton School, University of Pennsylvania, Philadelphia, PA, 2000.

[7] B. Boser, I. Guyon, V. Vapnik, A training algorithm for optimal margin classi<sup>fi</sup>ers, Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory, 1992, Pittsburgh.

[8] L. Breiman, Random forest, Machine Learning 45 (1) (2001).

[9] K. Campo, E. Gijsbrechts, P. Nisol, Towards understanding consumer response to stock-outs, Journal of Retailing 76 (2) (2000)

[10] K. Campo, E. Gijbrechts, P. Nisol, Dynamics in consumer response to product unavailability: do stock-out reactions signal response to permanent assortment reductions? Journal of Business Research 57 (2004).

[11] E. Castillo, J. Gutiérrez, A. Hadi, Expert Systems and Probabilistic Network Models, Springer-Verlag, New York, 1997.

[12] S. Cetinkaya, C.Y. Lee, Stock replenishment and shipment scheduling for vendor managed inventory, Management Science 46 (2) (2000).

[13] T. Clark, H. Lee, Performance interdependence and coordination in business-tobusiness electronic commerce and supply chain management, Information Technology and Management 1 (1) (2000).

[14] J. Cleary, E. Trigg, K⁎: An instance-based learner using an entropic distance measure, Proceedings of the 12th International Machine Learning Conference, 1995.

[15] W. Cohen, Ef<sup>fi</sup>cient pruning methods for separate-and-conquer rule learning systems, Proceedings of the 13th International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI-93), France, Chambéry, 1993.

[16] F. Colacchio, O. Tikhonova, J. Kisis, Consumer response to out-of-stock: decisionmaking process and in<sup>fl</sup>uencing factors, ECR Europe Berlin Conference, 2003.

[17] D. Corsten, T.W. Gruen, Stock-outs cause walkouts, Harvard Business Review 82 (5) (2004).

[18] P. Desmet, V. Renaudin, Estimation of product category sales responsiveness to allocated shelf space, International Journal of Marketing Research 15 (1998).

[19] P. Domingos, Unifying instance-based and rule-based induction, Machine Learning 24 (2) (1996).

[20] B. Downs, R. Metters, J. Semple, Managing inventory with multiple products, lags in delivery, resource constraints, and lost Sales: a mathematical programming approach, Management Science 47 (3) (2001).

[21] M. Emmelhainz, L. Emmelhainz, J. Stock, Consumer responses to retail Stock-outs, Journal of Retailing 67 (2) (1991).

[22] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, 1996.

[23] Y. Freund, L. Mason, The alternating decision tree learning algorithm, Proceedings of 16th International Conference on Machine Learning, Morgan Kaufmann, 1999.

[24] N. Friedman, D. Geiger, M. jai Goldszmidt, Bayesian network classi<sup>fi</sup>ers, Machine Learning 29 (3) (1997).

[25] B. Gaines, P. Compton, Induction of ripple down rules, Proceedings of the 5th Australian Joint Conference on Arti<sup>fi</sup>cial Intelligence, World Scienti<sup>fi</sup>c, Hobart, Australia, 1992, Singapore.

[26] T. Gruen, D. Corsten, S. Bharadwaj, Retail out-of-stocks: a worldwide examination of extent causes and consumer responses, The Food Institute Forum, CIES, 2002, FMI, GMA.

[27] G. Hausruckinger, Approaches to Measuring On-Shelf Availability at the Point of Sale, ECR Europe, White Paper, , 2006.

[28] E. Heylighen, Web Dictionary of Cybernetics and Systems, , 2003 Available at: http://pespmc1.yub.ac.be/ASC/indexASC.html

[29] W. Hopp, M. Spearman. Factory Physics, International editionMcGraw Hill, 2000.

[30] D. Jichang, H.S. Du, W. Shouyang, K. Chen, X. Deng, A framework of web-based decision support systems for portfolio selection with OLAP and PVM. Decision Support Systems 37 (2004).

[31] M. Joshi, On evaluating performance of classi<sup>fi</sup>ers for rare classes, Proceedings of the 2002 IEEE International Conference on Data Mining (Icdm'02), ICDM, Japan, Dec 2002.

[32] Y. Kang, S. Gershwin, Information inaccuracy in inventory systems: stock loss and stockout, IIE Transactions 37 (9) (2005).

[33] M. Kiang, A comparative assessment of classi<sup>fi</sup>cation methods, Decision Support Systems 35 (4) (2003).

[34] S. Kim, Stochastic ordering and robustness in classi<sup>fi</sup>cation from a Bayesian network, Decision Support Systems 39 (3) (2005)

[35] E. Kim, W. Kim, Y. Lee, Combination of multiple classi<sup>fi</sup>ers for the customer's purchase behavior prediction, Decision Support Systems 34 (2) (2003).

[36] R. Kohavi, The power of decision tables, Proceeding of the European Conference on Machine Learning (ECML'95), 1995.

[37] R. Kohavi, Scaling up the accuracy of naive Bayes classi<sup>fi</sup>ers: a decision tree hybrid, Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, AAAI Press, 1996.

[38] Ν. Landwehr, Μ. Hall, E. Frank, Logistic model trees, Machine Learning 59 (2) (2005).

[39] Χ. Li, A scalable decision tree system and its application in pattern recognition and intrusion detection, Decision Support Systems 41 (1) (2005).

[40] R. Metters, Producing multiple products with stochastic seasonal demand and capacity limits, Journal of Operational Research Society 49 (3) (1998).

[41] J. Moody, C. Darken, Fast learning in networks of locally tuned processing units, Neural Computation 1 (1989)

[42] S. Nahmias, S. Smith, Optimizing inventory levels in a two-echelon retailer system with partial lost sales, Management Science 40 (1994).

[43] E.W.T. Ngai, T.C. Cheng, E. Au, S. Kee-Hung Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2005).

[44] J. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[45] I. Rish, An empirical study of the naive Bayes classi<sup>fi</sup>er, IJCAI 2001 Workshop on Empirical Methods in Arti<sup>fi</sup>cial Intelligence, 2001.

[46] Roland Berger, Full-shelf satisfaction, Reducing Out-Of-Stocks in the Grocery Channel, Grocery Manufacturers of America, 2002.

[47] Roland Berger, Optimal Shelf Availability – Increasing Shopper Satisfaction at the Moment of Truth, ECR Europe Publications, 2003.

[48] D. Rumelhart, G. Hinton, R. Williams, Learning internal representation by error propagation, in: D.E. Rumelhart, J.L. McClelland (Eds.), Parallel Distributed Processing: Exploration in the Microstructure of Cognition 1: Foundations, MIT Press, Cambridge, Mass, 1986.

[49] S. Salzberg, On comparing classi<sup>fi</sup>ers: pitfalls to avoid and a recommended approach, Data Mining and Knowledge Discovery 1 (3) (1997).

[50] S. Thomassey, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (1) (2006).

[51] V. Vapnik, The Nature of Statistical Learning Theory, Springer Verlag, New York, 1995.

[52] C. Vuyk, Out-of-Stocks: A Nightmare for Retailer and Supplier, Beverage World, , 2003.

[53] M. Yang, An ef<sup>fi</sup>cient algorithm to allocate shelf space, European Journal of Operational Research 131 (2001).

Dimitris Papakiriakopoulos holds a B.Sc. in Informatics and M.Sc. in Information Systems from AUEB, and a Ph.D. in Information Systems and Arti<sup>fi</sup>cial Intelligence also from AUEB He is a senior research officer at the FITRUN Research Center at AUEB and has extensive research experience, having been involved in various research projects for the last 9 years. His research focuses on utilization of machine learning methods, especially for the detection of out-of-shelf situations.

Katerina Pramatari is Assistant Professor at the Department of Management Science and Technology of the Athens University of Economics and Business (AUEB). She holds a B.Sc. in Informatics and M.Sc. in Information Systems from AUEB, and a Ph.D. in Information Systems and Supply Chain Management also from AUEB. She has won both business and academic distinctions and has been granted eight state and school scholarships. Her research and teaching areas are supply and demand chain collaboration, traceability and RFID, e-procurement, e-business integration and electronic services. She has published 18 papers in scienti<sup>fi</sup>c journals including the Information Systems Journal, Journal of Information Technology, The European Journal of O.R., Computers and O.R., Supply Chain Management: An International Journal, and International Journal of Information Management.

Professor Georgios Doukidis has a B.Sc. in Mathematics, University of Thessaloniki, an M.Sc. in Operational Research, London School of Economics, and a Ph.D. in Simulation/ Arti<sup>fi</sup>cial Intelligence, London School of Economics – LSE. He worked as Lecturer at LSE and Visiting Professor at Brunel University. Currently, he is Professor in the Department of Management Science and Technology at the Athens University of Economics and Business (AUEB) and Director of the ELTRUN E-Business Research Center. He has published more than 60 papers in scienti<sup>fi</sup>c journals and acted as guest editor in the Journal of the O.R. Society, European Journal of I.S., Journal of I.T., International Journal of E-Commerce, Supply Chain Management: An International Journal.
