---
otero_id: 9032
otero_key: "8G45PETW"
title: "Spatially enabled customer segmentation using a data classification method with uncertain predicates"
authors: "Bo Fan; Pengzhu Zhang"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.03.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spatially enabled customer segmentation using a data classi<sup>fi</sup>cation method with uncertain predicates

Bo Fan <sup>a,</sup>⁎, Pengzhu Zhang

<sup>a</sup> School of International and Public Affairs, Shanghai Jiaotong University, Shanghai 200030, China

<sup>b</sup> Antai Management School, Shanghai Jiaotong University, Shanghai 200052, China

## a r t i c l e i n f o

Article history: Received 15 October 2007 Received in revised form 11 February 2009 Accepted 4 March 2009 Available online 16 March 2009

Keywords: Spatial data classi<sup>fi</sup>cation Customer segmentation Uncertain predicates

## a b s t r a c t

Spatial attributes are important factors for predicting customer behavior. However, thorough studies on this subject have never been carried out. This paper presents a new idea that incorporates spatial predicates describing the spatial relationships between customer locations and surrounding objects into customer attributes. More speci<sup>fi</sup>cally, we developed two algorithms in order to achieve spatially enabled customer segmentation. First, a novel <sup>fi</sup>ltration algorithm is proposed that can select more relevant predicates from the huge amounts of spatial predicates than existing <sup>fi</sup>ltration algorithms. Second, since spatial predicates fundamentally involve some uncertainties, a rough set-based spatial data classi<sup>fi</sup>cation algorithm is developed to handle the uncertainties and therefore provide effective spatial data classi<sup>fi</sup>cation. A series of experiments were conducted and the results indicate that our proposed methods are superior to existing methods for data classification

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Customer segmentation is used in analyzing and identifying groups of customers with similar characteristics by recognizing their most important factors [20]. This method is especially useful for companies that conduct special sales promotions and target services to different customers [1]. Data classi<sup>fi</sup>cation is a data mining technique that meets the needs for customer segmentation. Customer information stored in a database is analyzed in order to identify rules that partition the database into a given set of classes [2]. It is assumed that each item in the database belongs to a prede<sup>fi</sup>ned class, determined by an attribute called a decisional attribute. For customer segmentation, a customer's “profit” attribute, as calculated by the company, is often assumed as the decisional attribute, while the other customer attributes are regarded as conditional attributes. Therefore, the task of data classi<sup>fi</sup>cation is to reduce the large number of conditional attributes based on the value of the decisional attribute, as well as to extract the key characteristics of certain groups from a wide spectrum of customer attributes.

Current data classi<sup>fi</sup>cation techniques for customer segmentation include mathematical optimization methods [8,9], arti<sup>fi</sup>cial neural networks [11], and clustering methods [6,16]. All of these methods consider only relational data and exclude spatially-related data. According to some recent marketing science research, customers consumption behavior is determined not only by their personal attributes and sales information, but also by the surrounding objects and demographic information of the related address [12,13,20]. For example, the traf<sup>fi</sup>c conditions in the vicinity of a customer could in<sup>fl</sup>uence which store he would be inclined to visit. Similarly, the demographic description of a customer's residential or working area is useful information for an enterprise trying to understand the market segment that they serve. Nonetheless, the correlation between spatial information and customer behavior has not been effectively and actively studied. In this paper, we propose a spatial data classi<sup>fi</sup>cation method that <sup>fi</sup>nds interesting customer behavior patterns by incorporating spatially related attributes into sales information. For example, it uses spatial data classi<sup>fi</sup>cation rules similar to the following:

$$
\text { Close - to } (x, \text { park }) \land \text { Sex } (x, \text { male }) \land \text { Income } (x, \text { high })
$$

$$
\wedge \text { service - level } (x, h i g h) \Rightarrow \text { profit } (x, h i g h)\tag{1}
$$

$$
\text { Close - to } (x, \text { park }) \land \text { Sex } (x, \text { male }) \land \text { Income } (x, \text { high })
$$

$$
\wedge \text { service - level } (x, l o w) \Rightarrow \text { profit } (x, l o w)\tag{2}
$$

Rule (1): if a customer who lives close to “a park” is a “male” of “high income” and the “service level” of the enterprise for him is “high,” then he belongs to the “high profit” group of the enterprise. Rule (2): if a customer who lives close to “a park” is a “male” with “high income,” but the “service level” of the enterprise for him is “low,” then he belongs to the “low profit” group of the enterprise. In such a pair of spatial classi<sup>fi</sup>cation rules, there is a close-to (x, park) function that describes the spatial relationship between the customer's location and a surrounding object. This function provides a signi<sup>fi</sup>cant spatial clue for effective Customer Relationship Management (CRM), through which the enterprise could determine its customer service levels based on the geographical characteristics mentioned in the pair of rules.

Other than enhancing the service level for members of the customer group involved in Rule (2), the enterprise could also mark areas close to a park as important selling areas in a Geographical Information System (GIS) urban map. From this example, it is easy to see that the analytical function of spatially enabled customer segmentation is more powerful than that of traditional customer segmentation.

In this paper, spatial predicates are incorporated into the CRM analysis, and a spatial data classi<sup>fi</sup>cation method is proposed for customer segmentation. To conduct spatial data classi<sup>fi</sup>cation, however, two challenging problems must be solved. The <sup>fi</sup>rst problem stems from the large amount of spatial information available in a city. Only a small portion of spatial information affects customer behaviors and is relevant to the segmentation tasks. As such, an effective <sup>fi</sup>ltration method is required to identify the meaningful predicates (Section 3). The second problem is related to the dif<sup>fi</sup>culty of obtaining accurate predicates. Uncertainties exist in spatial information, yet customer spatial predicates should be able to accurately describe objects surrounding a customer's address that might affect his behavior. Current spatial data classi<sup>fi</sup>cation methods (e.g., spatial ID3) cannot suf<sup>fi</sup>ciently accomplish the segmentation task if it is riddled with uncertain predicates. Section 4 develops a rough set-based classi<sup>fi</sup>cation algorithm to handle uncertainties. Section 5 discusses a series of experiments that were conducted to prove the ef<sup>fi</sup>ciency of the proposed algorithms. Finally, the study is summarized in Section 6.

## 2. Research background

## 2.1. Relevant work

It is generally agreed that about 80% of currently used data contains some spatial elements or dimensions. This is typically true in all <sup>fi</sup>elds of human endeavor. Traditional information systems for decision support, commonly referred to as management information systems (MIS), were exclusively designed to handle non-spatial data, like sales information [5]. Meanwhile, the CRM systems have been improved by incorporating the analytical and visualization capabilities of GIS, because spatially related information can be stored in a spatial database and analyzed by GIS functions. All the current studies on GIS applications for effective CRM focus on using the original GIS functions that include querying, buffering, overlapping, as well as establishing suitable models in the GIS model-base to realize logistical planning for improved customer service [7]. For this objective, an enterprise can design market plans based on the visual distribution of customers on a digital map. Because they are limited to the original GIS functions, current studies are incapable of thoroughly analyzing the association between consumption behavior and the customers' spatial factors. Moreover, a suitable analytical function beyond GIS, called spatial data mining, has not yet been actively developed.

Spatial data mining is a sub<sup>fi</sup>eld of data mining that deals with the extraction of implicit knowledge, spatial relationships, or other interesting patterns that are not explicitly stored in spatial databases [5]. In the past, algorithms for spatial associations [4], clustering, generalized spatial description [7], and other functions have been analyzed. Spatial data classi<sup>fi</sup>cation is an area that has not attracted much attention, having only been applied to a few special <sup>fi</sup>elds, such as image classi<sup>fi</sup>cation for distinguishing different galaxies[5], or the entity classi<sup>fi</sup>cation of cities and stores [10]. This method is composed of four key steps. In Step 1, all task-relevant objects are collected and stored in a spatial database, containing the spatial and non-spatial attributes of the objects. In Step 2, the spatial predicates (spatial relationships for each pair of objects) within a speci<sup>fi</sup>c distance threshold are computed. At the same time, we need to compute a g-close-to() predicate to describe the coarse relationship of the two spatial objects [4,7]. The typical computation is done based on the Minimal Boundary rectangle (MBR) method, which offers indexes to simulate the objects approximately and judge the relationship between two spatial objects [6,10]. For Step 3, irrelevant spatial predicates are eliminated based on statistical methods. There are a large number of spatial predicates in the GIS, but only some of them are meaningful for the mining task. The current literature contains a method to compute the frequency of the spatial predicates and eliminate irrelevant ones by using a pre-de<sup>fi</sup>ned threshold [19]. This <sup>fi</sup>ltration step is indispensable, because it can reduce computational costs and enhance the quality of the data classi<sup>fi</sup>cation method [10]. Step 4 generates a binary decision tree using a spatial ID3 algorithm, which is a representative spatial data classi<sup>fi</sup>cation method in current research [5,10]. In general, Steps 1 to 3 build and re<sup>fi</sup>ne a task-related spatial dataset, and Step 4 partitions the dataset into a given set of classes.

## 2.2. Limitations of previous techniques

Existing spatial data classi<sup>fi</sup>cation methods, tailored for geographical or astronomical applications, are not suitable for customer segmentation. First, Step 1 must include sales information, besides the spatial database. Second, the information contained in the g-close-to() predicate in Step 2 is insuf<sup>fi</sup>cient for explaining customer behavior. For instance, close-to 10 m (x, store-1) and close-to 50m (x, store-2) are two spatial predicates of a customer x, denoting that the distance from the customer's location to store-1 is 10 m and the distance to store-2 is 50 m, respectively. Supposing that the commodity categories, the prices, and the services of store-1 and store-2 are the same, then the slight difference in distance indicated in the two predicates could almost decide that x would be more likely to visit store-1. Both predicates can be induced to a higher concept level and a more general g-close-to (x, store) predicate, and may thus no longer be distinguishable from each other. Therefore, aside from g-close-to(), more detailed and precise predicates are required to analyze customer segmentation. Such detailed predicates should be organized and mapped to a series of concept hierarchy trees. Third, the method of using the predicate frequency discussed in Step 3 is not suitable for eliminating the irrelevant predicates of customer addresses. For example, there may be a total of 100 sampled customer addresses in the database of a given store. All of the customers are close to a tree, thereby demonstrating that close-to (x, tree) is the most frequent predicate for all of the sampled customers. If 50 of the customers belong to the high-pro<sup>fi</sup>t class, and the remaining 50 customers belong to the low-pro<sup>fi</sup>t class, then the close-to (x, tree) predicate is meaningless in distinguishing different pro<sup>fi</sup>t classes of customers and should therefore be <sup>fi</sup>ltered out. In this paper, we will use the frequency (ratio) difference of a predicate in two classes, instead of the frequency of the predicate, as heuristic information. Then a new <sup>fi</sup>ltration method is proposed to meet the needs of customer segmentation. Finally, only predicates with a frequency difference larger than a prede<sup>fi</sup>ned threshold are used for further data classi<sup>fi</sup>cation. Our own approach to handle customer attributes will be illustrated in Section 3.

Additionally, the existing spatial classi<sup>fi</sup>cation methods in Step 4, which construct a decision tree to generate rules, work well only for a complete dataset without uncertainties. Instead of g-close-to(), more detailed spatial predicates are needed for CRM applications. In other words, g-close-to() should be divided into more speci<sup>fi</sup>c predicates that are often organized as concept trees. The computation of such speci<sup>fi</sup>c predicates requires that the boundaries of spatial objects be exactly determined in the GIS. However, the boundaries of spatial objects can only be known with <sup>fi</sup>nite accuracy. It is well known in the <sup>fi</sup>eld of geographical sciences that this is not always the case, because geographical objects naturally manifest incompleteness, inconsistency, vagueness, imprecision, and error in the real world [4]. Consequently, not every spatial predicate in the detailed levels of the concept tree can be clearly identi<sup>fi</sup>ed, even if the customers clearly provide their detailed addresses to the enterprise. Therefore, the MBR index cannot well simulate an uncertain object. For instance, the MBR method may inform the analysts that, “it is not certain, but it is possible that A is adjacent to B.” In order to realize spatially enabled customer segmentation, an ef<sup>fi</sup>cient classi<sup>fi</sup>cation algorithm capable of handling uncertainties should be developed as an alternative to the current spatial ID3 algorithms. Previous studies have proven that Rough Set (RS) theory is an ef<sup>fi</sup>cient tool to discover classi<sup>fi</sup>cation rules through a process of knowledge induction [14,15,17]. The classical rough set theory developed by Pawlak [14] is based on complete information systems. It classi<sup>fi</sup>es objects using upper-approximations and lower-approximations de<sup>fi</sup>ned on an indiscernibility relationship, which is a kind of equivalent relationship. Yet, only the properties of the relational data are analyzed. In the RS theory, in order to process an information system with uncertainties, the classical rough set theory needs to be extended to some inequivalent relationship. In this paper, two RS-based mechanisms are employed in order to present an inequivalent relationship, handle uncertain predicates, and reduce customer attributes. By incorporating such mechanisms, our proposed method for spatial data classi<sup>fi</sup>cation should produce more quali<sup>fi</sup>ed results than that of spatial ID3, which will be described in Section 4.

## 3. Handling customer attributes

Our own approach to handling customer attributes also includes three steps. Step 1 declares the information categories of customer attributes for our spatially enabled segmentation task. The contents of each category are illustrated in detail in Section 3.1. Step 2 uses the MBR method to compute spatial predicates and step 3 then <sup>fi</sup>lters out the meaningful ones from the large number of spatial predicates.

## 3.1. Categories of customer attributes

The goal of the spatially enabled customer segmentation process is to identify rules that divide the set of classi<sup>fi</sup>ed objects (customers) into a number of groups. All of the objects in a speci<sup>fi</sup>c group typically belong to a certain class. Besides sales information, spatial information is also included in the scope of our analysis. To realize the function of spatially enabled customer segmentation, the customer address is regarded as a spatial object. We therefore propose the novel idea of taking spatial predicates as part of the information categories. The Data Set (DS) for our task consists of three information categories: (1) sales information; (2) non-spatial attributes; and (3) spatial predicates.

## 3.1.1. Sales information

The sales information of the enterprise is also composed of two parts [1,9]. The <sup>fi</sup>rst part records customer information from the multiple channels of customer contacts. This includes address, age, income, sex, and level of education, among others. The second part is detailed information on the sales transactions, such as what the customer bought, when the transaction took place, the price of the item, and so on.

## 3.1.2. Non-spatial attributes

Non-spatial attributes describe the surrounding information of a geographical object and are customarily stored in the relation database of an urban GIS [13]. The non-spatial attributes are mainly composed of four types. The <sup>fi</sup>rst type consists of demographic information about a customer's workplace area, such as population, household, average income, and so on. The second type comprises demographic information about a customer's residential area. The third type consists of data on the non-spatial description of the store, such as the number of salespersons, the commodities categories in the store, the scale of the store, and so on. The fourth type consists of demographic data regarding the store area.

An effective data mining method requires a preparatory stage, which transforms the detailed data into a series of concepts. The concepts and concept hierarchies are often organized into a tree structure to denote the general knowledge of some detailed values regarding sales information and non-spatial attributes. For example, the details about an expenditure in the sales information can be generalized into a series of concepts, such as “low,” “medium,” and “high.” At the same time, the non-spatial attributes, such as “average income” or “area population” can also be represented by similar concepts. The representative method of building a concept tree is called Attribute Oriented Induction (AOI) [7].

## 3.1.3. Spatial predicates

A spatial predicate refers to a description of a spatial relationship between two geographical objects. The general expression of spatial relations can be transformed into facts classi<sup>fi</sup>ed as bSpatialrelationN (Refobj, Taskrelevantobj) [19]. The g-close-to() predicate is used to coarsely describe topological relationships between spatial objects (e.g., close-to (x, park) means that spatial object “x” lies close to spatial object “park”). As customer segmentation demands more informative spatial predicates than other application <sup>fi</sup>elds [5,10], we propose that g-close-to() should be extended to more detailed spatial relationships, represented as concept trees.

3.1.3.1. The concept tree for spatial relations. Various spatial predicates can be involved in spatial data mining. The spatial relation g-close-to is divided into more detailed ones, such as adjacent-to, intersect, close-to, driven-distance, and so on [4], all of which are shown in the concept tree of Fig. 1. Each predicate is organized into a concept hierarchy from general to detailed (e.g., the spatial predicate “intersect” is encoded as (1,1,1,2), which means this predicate is the second tree-branch at level 4). The concept tree can map spatial relations into concepts in order to realize the analysis of spatial predicates with multiple levels.

![](/api/attachments/8G45PETW/fulltext/images/9e8d048b0fe54638ce163966b502b2f1436c4fb10e45f08d678e538ab4619443.jpg)  
Fig. 1. The g-close-to spatial relation concept tree.

![](/api/attachments/8G45PETW/fulltext/images/c37ca1374802422e0cb817319353ba691b425bd98dc2f089e84f2bfc6f1e47fd.jpg)  
Fig. 2. The RefObj (Residential area) concept tree.

3.1.3.2. The concept tree for reference objects. A reference object is the main subject of the description for the spatial reference object (RefObj). It is the customer's location that affects the consumption behavior. The RefObj mainly concerns two locations: the residential area and the customer's workplace address. From these, we can extract spatial predicates with other task-related objects (TaskRelevantObj) stored in different themes of the GIS map, which include park, road, water, business, bus station, and so on. The RefObj concept tree is encoded in way that is similar to that for spatial relation. The customer's area of residence is presented as an example in Fig. 2.

3.1.3.3. The concept tree for task-relevant objects. A task-relevant object is a spatial object that is both relevant to the tlask at hand and spatially related to the reference object. Examples of concept hierarchy trees for task-relevant objects, such as business locations and traf<sup>fi</sup>c facilities, are presented in Figs. 3 and 4. Besides business locations and traf<sup>fi</sup>c facilities, multiple themes for spatial objects, including a hill, school, park, water, and road, among others, are all stored in the GIS as useful information for customer analysis. The Taskrelevantobj concept tree is encoded similarly to those for spatial relation and RefObj.

## 3.2. The filtration process for spatial predicates

In step 2, we can initially identify spatial predicates with multiple levels through the MBR method for a sample of objects (customers). But only a small part of the predicates can be considered useful for the classi<sup>fi</sup>cation task [5].

Afterward, a <sup>fi</sup>ltration method, as step 3, may be used to extract the relevant predicates, and is illustrated as follows. We <sup>fi</sup>rst present a relation table for expressing the spatial predicates and the class label of a customer. Then Algorithm 1 is proposed for selecting the meaningful predicates in such a relation table. Algorithm 1 is based on a newly proposed theory called revised set partition. In our case, only the relevant predicates are computed in detail for all of the classi<sup>fi</sup>ed customers.

![](/api/attachments/8G45PETW/fulltext/images/6e7e52f4e3fa5d642ce34a8770cfa4da962aa8ce8041ea65cf601a812bff29e7.jpg)  
Fig. 3. The Taskrelevantobj (Business location) concept tree.

![](/api/attachments/8G45PETW/fulltext/images/65dad0cc9e1f1ee4ef09de067fc6daec4d012426deb2be5b017d209956d5dc4a.jpg)  
Fig. 4. The Taskrelevantobj (Traf<sup>fi</sup>c facilities) concept tree

## 3.2.1. The relation table R for spatial predicates

The spatial relationships between reference objects and taskrelevant objects are extracted through spatial computation, according to Figs.1–4, as exempli<sup>fi</sup>ed by the predicates described in Table 1. Table 1 can be transformed into a relation table (Table 2). We can adopt such a relation table R (Row-Id, Spatialrelation, Refobj, Taskrelevantobj, d) to store the spatial predicates that express spatial relations between the reference objects and task-relevant objects, where d represents the decisional attribute of the Row-Id (i.e., Customer ID). Afterward, the spatial predicate <sup>fi</sup>ltration method can be used on such a relation table.

## 3.2.2. Computation of meaningful predicates

The set partition method proposed by Wang [19] computes frequency predicates as meaningful ones for generating spatial data mining rules. As illustrated in Section 2.2, frequency predicates may result in poor quality classi<sup>fi</sup>cation. We revise the set partition theory by taking the decisional label d into consideration, and then propose a new heuristic called ratio difference for computing the frequency difference of a predicate belonging to each class label. If the ratio difference of a predicate is larger than a given threshold, called the support threshold, then the predicate is regarded as meaningful for the segmentation task.

## De<sup>fi</sup>nition 1. Revised set partition.

U is a relation in the relation pattern $R , t , q \in U , X \subseteq R .$ The two rows of t and q are equivalent with respect to a given set of attributes X, if they satisfy (1) $t [ A | l ] = q [ A | l ]$ for all A in X (where ‘|l’ represents the concept level l for attribute A), or (2) t[d]=q[d]for d in X (where ‘d’ represents the decisional attribute). Any attribute set X partitions the rows of relations into equivalence classes [19]. We denote the equivalence class of a row t∈U with respect to a given set $X \subseteq R$ at level l by [t] or decisional attribute d by $[ t ] _ { d } , \mathrm { i . e . } [ t ] _ { X | l } = \left\{ q \in U | t [ A | l ] = q [ A | l ] \right\} \mathrm { o r } \left[ t \right] _ { D | d } = q \in U | t [ d ] = q$ [d]}. The set $U / \{ X | l \ \& \ d \} = \{ [ t ] _ { X | l \ \& \ d } , \ t { \in } U \}$ of the equivalence classes is a partition under X at concept level l or decisional attribute d, that is, U / {X|l & d} is a collection of disjoint sets (equivalence classes) of rows, with each set having a unique value for the attribute set X at concept level l or decisional attribute d; the union of the sets is equal to the relation U. Moreover, the rank |U/ {X|l & d}| of a partition U /{X| l & d} is the number of equivalence classes in U/ {X|l & d}.

Ten examples of spatial predicates with decisional attributes.

<table><tr><td>1. Contains (block1, E1), l</td><td>2. Intersect (block 2, No.4), h</td></tr><tr><td>3. Close-to 100 (block 3, bus 3), h</td><td>4. Close-to 200 (block2, bus2), m</td></tr><tr><td>5. Intersect (block 3, No.2), m</td><td>6. Close-to 100 (block1, bus 3), h</td></tr><tr><td>7. Close-to 200 (block1, E1), l</td><td>8. Intersect (block2, No.4), l</td></tr><tr><td>9. Close-to 200 (block 4,bus 2), m</td><td>10. Intersect (block 1, No.2), m</td></tr></table>

Example. Consider the relation in Table 2. Attribute Taskrelevantobj has value (1,2) from level 1 to level 2 on rows 1 and 7. As such they form an equivalence class as follows: Row-Id[1] = Row- $. \mathrm { I d } [ 7 ] _ { T a s k r e l e v a n t o b j | 2 } = \{ 1 , 7 \} .$ The entire partition at concept level 2 with respect to Taskrelevantobj is U / {Taskrelevantobj|2} = {{1,7}, {3,4,6,8,9},{2,5,10}}, the partition of U / {Spatialrelation|3} = {{1}, {2,5,8,10},{3,6},{4,7,9}}, and the partition of $U / \{ d \} = \{ \{ 1 , 7 , 8 \} , \{ 2 , 3 , 6 \}$ {4,5,9,10}}. If d is given the value “h” then U/ {d|h}={2,3,6}. Thus, the partition with respect to Spatialrelation at level 3, Taskrelevantobj at level 2, and d with value “h” is U / {Spatialrelation|3, Taskrelevantobj|2, $d | h \} = \{ \{ 3 , 6 \} , \{ 2 \} \}$ }. The elements {3,6} and {2} represent two spatial predicates as the two subsets of this partition. We will discuss the computation of the ratio for the spatial predicates in a later section.

Meanwhile, the count for a spatial predicate must be calculated <sup>fi</sup>rst. It is the number of different values for the attributes of Refobj, when the respective values of the attributes Spatialrelation and Taskrelevantobj agree. For example, supposing the concept level is 4 and the decisional label is “h”, we extract the partition with respect to attribute Refobj as follows: $U / \{ R e f o b j | 4 \} = \{ \{ 1 , 6 , 7 , 1 0 \} , \{ 2 , 4 , 8 \} , \{ 3 , 5 \} , \{ 9 \} \}$ , furthermore, U / {Refobj|4, d|h} = {{2},{3},{6}}. then, |U / {Refobj|4, d|h}| denotes the number of different reference objects whose decisional class labels are “h”, that is 3; if the <sup>fi</sup>rst element of U/{Spatialrelation|3,Taskrelevantobj|2, d|h} representing the spatial predicate S(h) is {3,6}, intersecting the set S (h) with the set U /{Refobj|4, d|h} results in{{3},{6}}. This means that the reference objects in row 3 and row 6 are different, that is, two different customers. Therefore, the count of S(h) is 2 or |S(h)|=2.

Table 2 Relation table of Table 1.

<table><tr><td>Row-ID</td><td>Spatial relation</td><td>Refobj</td><td>TaskRelevantObj</td><td>d</td></tr><tr><td>1</td><td>(1,1,3)</td><td>(1,1,1,1)</td><td>(1,2,1,1)</td><td>l</td></tr><tr><td>2</td><td>(1,1,1,2)</td><td>(1,1,1,2)</td><td>(2,2,2,2)</td><td>h</td></tr><tr><td>3</td><td>(1,2,1)</td><td>(1,1,1,3)</td><td>(2,1,1,3)</td><td>h</td></tr><tr><td>4</td><td>(1,2,2)</td><td>(1,1,1,2)</td><td>(2,1,1,2)</td><td>m</td></tr><tr><td>5</td><td>(1,1,1,2)</td><td>(1,1,1,3)</td><td>(2,2,1,2)</td><td>m</td></tr><tr><td>6</td><td>(1,2,1)</td><td>(1,1,1,1)</td><td>(2,1,1,3)</td><td>h</td></tr><tr><td>7</td><td>(1,2,2)</td><td>(1,1,1,1)</td><td>(1,2,1,1)</td><td>l</td></tr><tr><td>8</td><td>(1,1,1,2)</td><td>(1,1,1,2)</td><td>(2,1,1,2)</td><td>l</td></tr><tr><td>9</td><td>(1,2,2)</td><td>(1,1,1,4)</td><td>(2,1,1,2)</td><td>m</td></tr><tr><td>10</td><td>(1,1,1,2)</td><td>(1,1,1,1)</td><td>(2,2,1,2)</td><td>m</td></tr></table>

Afterward, the ratio of this predicate with the “h” class label can be calculated next. It is 2/3≈66.67% and is denoted by Ratio{S(h)}. Following the same process, the Ratio{S(m)} and the Ratio{S(l)} of this predicate are calculated as 1/3≈33.33% and 0/3=0%, respectively.

Based on the ratio calculation, the ratio difference of the spatial predicates is then analyzed. As far as the task of data classi<sup>fi</sup>cation is concerned, the meaningful predicates are those distinguished characters obviously belonging to a given class label instead of the others. In other words, if a predicate of the spatial objects with the class label “h” appears more frequently than that of objects with the class label “l” or “m”, then it is

## Algorithm 1

Input:

regarded as a meaningful predicate for the class label “h”. As a result, a support threshold must be used to measure the ratio difference after the calculation of the ratio for spatial predicates. For example, the spatial predicate refers to the value combination of Spatialrelation at concept level 3, Taskrelevantobj at concept level 2, Refobj at concept level 4, and d with value “h”. As discussed above, Ratio{S(h)}−Ratio{S(m)}=2/3−1/3≈ 33.33%, and Ratio{S(h)}−Ratio{S(l)}=2/3−0≈66.67%. If the support threshold (the value of which can be set based on statistical theory [10]) is given as 30%, and the ratio differences have passed the threshold, it iscloseto 100m (x, bus station), which would be considered the meaningful predicate for the spatial objects with the decisional class label “h”. This agrees well with the descriptions presented in Table 2 and Figs. 1–4.

(1) Relation table R= {U,X};

We proposed this <sup>fi</sup>ltration method to select the meaningful predicates from a large number of customer spatial predicates, in which only the relevant predicates were used for the subsequent classi<sup>fi</sup>cation task. This proposed method will reduce the computational time and simultaneously enhance the quality of the data classi<sup>fi</sup>cation. The algorithm is presented as follows:

(2) l1, l2, $l _ { 3 } ,$ Support threshold(t);

Output:

{Meaningful predicates};

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Method:
1.Begin
2. For each element $d_k$ in $d$ do; /*$d_k$ is a class label of the decisional attribute set $d$ in $R^*$
3.    For $i=1$ to $n$ do; /*$n$ is the row number in $R^*$
4.    For $j = i + 1$ to $n$ do;
5.    Compute $Q_1(d_k) = U/\{Spatial\text{relation} \mid l_1, Task\text{relevantobj} \mid l_2, d \mid d_k\}$; /*a partition set $Q_1(d_k)$ with respect to the value combination of $Spatial\text{relation}$ at concept level $l_1, Task\text{relevantobj}$ at concept level $l_2$, and $d$ with value “$d_k$”. */
6.    Compute $Q_2(d_k) = U/\{Re fobj \mid l_3, d \mid d_k\}$; /*a partition set $Q_2(d_k)$ with respect to Refobj at concept level $l_3$, and $d$ with value “$d_k$”. */
7.    Endfor;
8.    Endfor;
9.    For each element $S(d_k) \in Q_1(d_k)$ do; /*$S$ is an element in $Q_1(d_k)$, which represents a spatial predicate*/
10.    Compute $M(d_k) = S(d_k) \cap Q_2(d_k)$; /*take every element in $S(d_k)$ and intersect it with every element in $Q_2(d_k)$. This is an effective way to calculate the count of $M(d_k)^*$
11.    Compute Ratio$\{S(d_k)\} = \frac{|M(d_k)|}{|Q_2(d_k)|}$; /* compute the ratio of $S(d_k)$ by using the count of $M(d_k)$, which is divided by the count of $Q_2(d_k)^*$
12.    Endfor;
13.    Endfor;
14.    For each $d_p \in d - d_k$ do; /* take every class label that is different from $d_k$ in $d^*$
15.    Count $S(d_k): = 0$;
16.    If Ratio$\{S(d_k)\} - Ratio\{S(d_p)\} \geq t$ then /* the ratio difference satisfies the support threshold(t), which means the predicate S belonging to the class label $d_k$ occurs more frequently than that belonging to other class labels*/
17.    Count $S(d_k)++$ /*if the ratio difference satisfies the given threshold illustrated in line 15, then 1 will be added to the count of predicate S belonging to the class label $d_k^*$
18.    Endif;
19.    Endfor;
20.    If Count $S(d_k) = |d|-1$ then /*if predicate S belonging to the class label $d_k$ is occurs more frequently than that belonging to all of the other class labels*/
21.    Output $\{S(d_k)\}$; /* then S is the meaningful predicate of $d_k^*$
22.    Endif;
23. End ;
</div>

An incomplete information system.  
Table 5

<table><tr><td>O/AT</td><td>Close_to (x, water)</td><td>Close_to (x, park)</td><td>In (x, busi_center)</td><td>Avg_income</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>High</td></tr><tr><td>2</td><td>0</td><td>δ</td><td>0</td><td>High</td></tr><tr><td>3</td><td>δ</td><td>δ</td><td>1</td><td>Low</td></tr><tr><td>4</td><td>1</td><td>δ</td><td>1</td><td>High</td></tr><tr><td>5</td><td>δ</td><td>δ</td><td>1</td><td>High</td></tr><tr><td>6</td><td>0</td><td>1</td><td>δ</td><td>High</td></tr></table>

In Algorithm 1, lines 2 to 11 compute the ratio of each predicate based on our revised set partition method. Then, we incorporated a new optimization technique between lines 14 and 22 to compute the ratio difference of a predicate belonging to each decisional attribute (class label). The ratio difference between the two class labels of the same predicate is a heuristic to identify which one could be considered meaningful in predicting customer behaviors.

## 4. Rough set method for customer segmentation

After we handle the customer attributes, an effective algorithm should be designed to carry out the partition of such an attribute set. As described in Section 2.2, when we process an information system with uncertainties, the classical rough set theory needs to be extended to some inequivalent relations. Several uncertainty handling techniques suggested by RS theory have been discussed, scattered through different research studies [3,14,15,18]. Such techniques have never been used for either handling uncertain predicates or developing a spatial data classi<sup>fi</sup>cation method. For step 4, all of the uncertain predicates in the customer attribute set are denoted by δ. Such a set is believed to be an incomplete information system. We use two RS based-mechanisms to handle spatial uncertainties: similarity relation [14,15] and generalized decision [18]. When we judge the relationship between object x and object y on an attribute set A involving the uncertain value $\delta ,$ the similarity relation mechanism can let δ take all possible values of 0 or 1. Here x and y are assumed to be the similarity relation on attribute set A, which is denoted by $S _ { A } ( x ) = \{ x , y \} . \ S _ { A } ( x )$ is an inequivalent relation instead of an equivalent relation. So this mechanism can well tolerate the uncertain predicates. After a class label (decisional attribute) is chosen to transform the incomplete information system into a decision table (DT), the second mechanism, called generalized decision, is then used. Along with the application of the <sup>fi</sup>rst mechanism, the generalized decision of an object x on attribute set A, denoted by $\partial _ { A } x ,$ lists all of the values of a decisional attribute for each object in $S _ { A } ( x )$ . Based on the two uncertainty handling mechanisms, a discernibility function, which does its work by judging $S _ { A } ( x )$ and $\partial _ { A }  { \boldsymbol { x } }$ for each pair of objects, is proposed as Algorithm 2 to compute the relative reducts on DT for generating spatial data classi<sup>fi</sup>cation rules. In addition, by employing Algorithm 2, there may exist some rules with two decisional values, such as the rule Avg\_Income(x, high)⇒profit (x, high)∨profit (x, extreme-high). This is because the uncertainty handling mechanisms react on the data classi<sup>fi</sup>cation method, which can greatly enhance the classi<sup>fi</sup>cation quality. In contrast, without the mechanisms for handling uncertain predicates, building decision trees using the current spatial classi<sup>fi</sup>cation research studies fails to compute the information gains of uncertain predicates. Spatial ID3 only reduces the conditional attributes and forcibly maps them into a single decisional value. This will result in many poor classi<sup>fi</sup>cations.

A decision table.

<table><tr><td>O/AT</td><td>Close_to (x, water)</td><td>Close_to (x, park)</td><td>In (x, busi_center)</td><td>Avg_income</td><td>Profit</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>High</td><td>High</td></tr><tr><td>2</td><td>0</td><td>δ</td><td>0</td><td>High</td><td>High</td></tr><tr><td>3</td><td>δ</td><td>δ</td><td>1</td><td>Low</td><td>Low</td></tr><tr><td>4</td><td>1</td><td>δ</td><td>1</td><td>High</td><td>High</td></tr><tr><td>5</td><td>δ</td><td>δ</td><td>1</td><td>High</td><td>Extreme-high</td></tr><tr><td>6</td><td>0</td><td>1</td><td>δ</td><td>High</td><td>High</td></tr></table>

$S _ { A T } ( x )$ and $\partial _ { A T } ( x )$ of an incomplete decision table.

<table><tr><td>O/AT</td><td> $S_{AT}(x)$ </td><td> $\partial_{AT} x$ </td><td>Profit(d)</td></tr><tr><td>1</td><td>{1 2}</td><td>{high}</td><td>High</td></tr><tr><td>2</td><td>{2 6}</td><td>{high}</td><td>High</td></tr><tr><td>3</td><td>{3}</td><td>{low}</td><td>Low</td></tr><tr><td>4</td><td>{4 5}</td><td>{high, extreme-high}</td><td>High</td></tr><tr><td>5</td><td>{4 5 6}</td><td>{high, extreme-high}</td><td>Extreme-high</td></tr><tr><td>6</td><td>{2 5 6}</td><td>{high, extreme-high}</td><td>High</td></tr></table>

4.1. Using the rough set theory for spatial data classification with uncertain predicates

## De<sup>fi</sup>nition 2. Incomplete information system.

An information system is a pair ${ \cal S } = ( 0 { , } A T )$ , where O is a nonempty <sup>fi</sup>nite set of objects and AT is a non-empty <sup>fi</sup>nite set of attributes for any $a \in A T ,$ such that a $O \to V _ { a } ,$ where $V _ { a }$ is called the value set of a. Each subset of attributes $A \subseteq A T$ determines a binary indiscernibility relation ind(A) as follows: $i n d ( A ) = \{ ( x , y ) \in O \times O , \forall$ a∈ $\dot { \bar { \boldsymbol { x } } } \boldsymbol { A } , \boldsymbol { a } ( \boldsymbol { x } ) = \boldsymbol { a } ( \boldsymbol { y } ) \}$ [14]. If a system contains an uncertain value in $V _ { a } ,$ e.g. $\boldsymbol { a } ( \boldsymbol { x } ) = \boldsymbol { \delta } ,$ where δ denotes an uncertain value, it is called an incomplete information system. Table 3 presents an example of an incomplete information system.

## De<sup>fi</sup>nition 3. Similarity relation.

A similarity relation of the attribute set $A \subseteq A T ,$ denoted by SIM(A), is defined as $S I M ( A ) = \{ ( x , y ) \in O \times O | \forall a \in A , a ( x ) = a ( y ) { \mathrm { ~ o r ~ } } a ( x ) = \delta$ or $a ( y ) = \delta \} = \cap . S I M ( \{ a \} ) \ [ 1 5 ]$ . Here, δ represents all of the possible <sup>\aaA ð Þf g</sup>values of an uncertain attribute. A similarity relation is an inequivalent relation. For example, if the spatial predicate close-to (x, water) has an uncertain value in Table 3, δ can denote all of the possible values of 0 or 1. $S _ { A } ( x )$ denotes the set of objects that are not equal to but are similar to x: $S _ { A } ( x ) = \{ y \in O | ( x , y ) \in S I M ( A ) \}$ }. Objects are similar if they are unlikely to be discernible. Let $O / S I M ( A ) = \{ S _ { A } ( x ) | x \in O \}$ , where O/ SIM(A) is the coverage of O in the incomplete information system and is different from the partition of O/ind(A) in the complete information system. An example is shown as follows:

Example. By calculating the data shown in Table 3, we conclude that O={1,2,3,4,5,6}, AT={W,P,B,I}. We then adopt W, P, B, and I to represent close-to(x, Water), close-to(x, Park), in(x, Busi-center), and Avg\_Income, respectively. For the total attributes set $A T , O / S I M A T { = }$ $\{ S _ { A T } ( 1 ) = \{ 1 \} , S _ { A T } ( 2 ) = \{ 2 , 6 \} , S _ { A T } ( 3 ) = \{ 3 \} , S _ { A T } ( 4 ) = \{ 4 , 5 \} , S _ { A T } ( 5 ) = \{ 3 \} , S _ { A T } ( 6 ) = \{ 4 , 5 \} , \nonumber$ {4,5,6}, and $S _ { A T } ( 6 ) = \{ 2 , 5 , 6 \} \}$ }. For example, suppose that $x = 5 ,$ , all of the attribute values in AT of y=4 or 6 are similar for $x = 5 , s 0 S _ { A T } ( 5 ) =$ $\{ 4 , 5 , 6 \} ;$ suppose that $x = 6 ,$ all the attribute values in AT of $\mathrm { y } = 2$ or 5 are similar for $x = 6 , s o S _ { A T } ( 6 ) = \{ 2 , 5 , 6 \}$ . The results of $S _ { A T } ( 5 )$ and $S _ { A T } ( 6 )$ are not symmetric. As such, $O / S I M ( A T )$ is the coverage of O where uncertain values exist, while $O / i n d ( A T )$ can give a clear partition of O only within the complete information system.

The discernibility matrix of Table 4.

<table><tr><td>x/y</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td></td><td></td><td>I, B</td><td></td><td>B</td><td></td></tr><tr><td>2</td><td></td><td></td><td>I, B</td><td></td><td>B</td><td></td></tr><tr><td>3</td><td>I, B</td><td>I, B</td><td></td><td>I</td><td>I</td><td>I</td></tr><tr><td>4</td><td></td><td></td><td>I</td><td></td><td></td><td></td></tr><tr><td>5</td><td>B</td><td>B</td><td>I</td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td>I</td><td></td><td></td><td></td></tr></table>

Table 7  
Classi<sup>fi</sup>cation quality experiments of the combination of Algorithms 1 and 2.

<table><tr><td rowspan="2">Experiment no.</td><td colspan="2">Parameters</td><td colspan="3">RS algorithm</td></tr><tr><td>Support threshold</td><td>Predicate number</td><td>Rn</td><td>Tn</td><td>q (%)</td></tr><tr><td>1</td><td>0</td><td>532</td><td>245</td><td>352</td><td>69.6</td></tr><tr><td>2</td><td>0.1</td><td>211</td><td>253</td><td>322</td><td>78.6</td></tr><tr><td>3</td><td>0.2</td><td>92</td><td>267</td><td>301</td><td>88.7</td></tr><tr><td>4</td><td>0.3</td><td>86</td><td>264</td><td>278</td><td>94.9</td></tr><tr><td>5</td><td>0.4</td><td>73</td><td>179</td><td>189</td><td>94.7</td></tr></table>

De<sup>fi</sup>nition 4. Decision table (DT).

A decision table is an information system $D T = ( O , A T \cup \{ d \} )$ , such that $d \notin A T$ and δ $V _ { d } ,$ where d is a distinguished attribute called decision (decisional attribute) and $V _ { d }$ is called the value set of d. The elements of AT are called conditions (conditional attributes). Table 4 gives an example of a decision table that adds up a decisional attribute named $\ " { d } = p r o f i t "$ on the basis of Table 3. Meanwhile, AT is composed of other attributes except d.

## De<sup>fi</sup>nition 5. Generalized decision in DT.

Let us de<sup>fi</sup>ne a function $\partial _ { A } , A \subseteq A T ,$ as follows: $\partial _ { A } x = \{ i | i = d ( y )$ $y \in S _ { A } ( x ) \} [ 1 8 ]$ . Here, $\partial _ { A }$ will be called the generalized decision in DT.

Example. For the decisional attribute d in Table 4, we can calculate $S _ { A T } ( 4 ) = \{ 4 , 5 \}$ , then $\partial _ { A T } ( 4 ) = \{ d ( 4 ) , d ( 5 ) \} = \{ \mathrm { h i g h }$ , extreme-high}. The attribute values of a similar set $S _ { A T } ( x )$ and general decision function ∂ x for Table 4 are computed in Table 5.

De<sup>fi</sup>nition 6. Discernibility function for an incomplete decision table.

We propose to use the discernibility matrix to create a discernibility function for the reduction of customer information. The discernibility matrix has the advantage of extracting rules and can be reduced easily from the decision table. Let an incomplete decision table be ${ D T } = ( 0 ,$ $A T \cup \{ d \} )$ , the discernibility matrix of DT is a symmetric $0 \times 0$ matrix with entries $f ( x , y )$ consisting of sets of attributes that are discernable from each other. f(x,y) is de<sup>fi</sup>ned as:

$$
f (x, y) = \left\{ \begin{array}{l} \big \{a \in A T: a (x) \neq a (y) \text {   and   } d (y) \not \in \partial_ {A T} (x) \big \} \\ \big \{\phi d (y) \in \partial_ {A T} (x) \text {   or   } (x, y) \in S I M (A T) \big \} \end{array} \right.
$$

Furthermore, the discernibility function can be de<sup>fi</sup>ned as $\varDelta =$ $\underset { U \times U } { \wedge } \bigvee _ { a \in A T } f ( x , y ) ,$ , where $\underset { a \in A T } { \vee } f ( x , y )$ refers to all of the corresponding values obtained by $f ( x , y ) ,$ , and 1 refers to the conjunctions of $\underset { U \times \underline { { U } } } { \wedge }$ $\bigvee _ { a \mathop { \left( a \right) } } f ( x , y ) \left[ 3 , 1 7 \right] .$ Here, $\Delta = \underset { U \times U _ { a \in A T } } { \wedge } f ( x , y )$ is called the relative reducts for DT, and $\Delta ( i ) = \underset { i = x , y \in U a \in A T } { \bigcup } f ( i , y )$ is called the relative reducts for $x = i .$

Comparison of frequency-based algorithm and Algorithm 1.

<table><tr><td rowspan="2">Experiment no.</td><td colspan="2">Parameters</td><td colspan="3">RS algorithm</td></tr><tr><td>Frequency threshold</td><td>Predicate number</td><td>Rn</td><td>Tn</td><td>q (%)</td></tr><tr><td>6</td><td>0.4</td><td>624</td><td>268</td><td>390</td><td>68.7</td></tr><tr><td>7</td><td>0.5</td><td>358</td><td>289</td><td>364</td><td>79.4</td></tr><tr><td>8</td><td>0.6</td><td>193</td><td>301</td><td>346</td><td>87.0</td></tr><tr><td>9</td><td>0.7</td><td>75</td><td>212</td><td>291</td><td>72.9</td></tr><tr><td>10</td><td>0.8</td><td>11</td><td>170</td><td>256</td><td>66.4</td></tr></table>

Table 9  
Experiments on data classi<sup>fi</sup>cation quality with multiple-level predicates.

<table><tr><td rowspan="2">Experiment no.</td><td colspan="3">Parameters</td><td colspan="3">RS algorithm</td></tr><tr><td>n</td><td>t</td><td> $(l_1, l_2, l_3)$ </td><td>Rn</td><td>Tn</td><td>q (%)</td></tr><tr><td>11</td><td>10,000</td><td>0.3</td><td>(1,1,1)</td><td>140</td><td>145</td><td>96.6</td></tr><tr><td>12</td><td>10,000</td><td>0.3</td><td>(2,1,1)</td><td>264</td><td>278</td><td>94.9</td></tr><tr><td>13</td><td>10,000</td><td>0.3</td><td>(2,2,1)</td><td>298</td><td>382</td><td>78.0</td></tr><tr><td>14</td><td>10,000</td><td>0.3</td><td>(2,3,1)</td><td>316</td><td>477</td><td>66.2</td></tr><tr><td>15</td><td>10,000</td><td>0.3</td><td>(3,3,1)</td><td>418</td><td>692</td><td>60.4</td></tr></table>

Example. We use Table 4 to illustrate the knowledge reduction method with the discernibility matrix. Taking the computation of f (1,2) as an example, we can <sup>fi</sup>nd $\alpha ( 1 ) \neq \alpha ( 2 )$ on the attribute W according to the $f ( x , y )$ de<sup>fi</sup>nition; but $d ( 2 ) \in \partial _ { A T } ( 1 )$ means that the decisional attribute values of d in the <sup>fi</sup>rst record (object 1) are the same as those in the second record (object 2) of Table 5, thereby making $f ( 1 , 2 ) = \phi .$ Taking the computation of $f ( 1 , 3 )$ as another example, we can <sup>fi</sup>nd $\alpha ( 1 ) \neq \alpha ( 3 )$ and $d ( 3 ) \not \in \partial _ { A T } ( 1 )$ , so $f \ ( 1 , 3 ) = \{ I , B \}$ . The discernibility matrix of Table 4 is presented in Table 6 below.

By using the discernibility function of $\Delta = \underset { U \times U } { \wedge } \bigvee _ { a \in A T } f ( x , y )$ to compute the relative reduct for Table 6 and the discernibility function of $\Delta ( i ) = \underset { i = x . v \in U a \in A T } { \setminus } f ( i , y )$ to compute the relative reduct for x =i, we can then obtain the knowledge reduction rules presented as follows:

$$
\begin{array}{l} \Delta = (I \lor B) \wedge B \wedge I = I \wedge B; \quad \Delta (1) = (I \lor B) \wedge B = B; \\ \Delta (2) = (I \lor B) \wedge B = B; \quad \Delta (3) = (I \lor B) \wedge I = I; \quad \Delta (4) = I; \\ \Delta (5) = B \wedge B \wedge I = B \wedge I; \quad \Delta (6) = I; \end{array}
$$

The above rules mean that Avg\_Income and $I n ( x ,$ Busi-center) are the relative reducts for Table 4; while In(x, Busi-center) is the relative reduct for x =1 and x =2; Avg\_Income is the relative reduct for $x = 3 , 4 , 6 ;$ and Avg\_Income and In(x, Busi-center) are the relative reducts for x =5. Therefore, the spatial data classi<sup>fi</sup>cation rules for customer segmentation can be extracted from the results of the above reducts and shown as follows:

In(x, Busi-center)⇒profit(x, high); Avg\_Income $( x , l o w ) \Rightarrow p r o f i t ( x , l o w ) .$ Avg\_Income (x, high)⇒profit (x, high)∨profit (x, extreme-high); Avg\_Income (x, high)∧In(x, Busi-center)⇒profit (x, extreme-high)

## 4.2. The rough set-based spatial data classification method

On the basis of the rough set theory de<sup>fi</sup>nition described in a previous section, we designed a rough set-oriented data

Quality of the two algorithms without uncertain predicates.

<table><tr><td rowspan="2">Experiment no.</td><td colspan="3">Parameters</td><td colspan="3">ID3 algorithm</td><td colspan="3">RS algorithm</td><td>Difference</td></tr><tr><td>n</td><td>t</td><td> $(l_1, l_2, l_3)$ </td><td>Rn</td><td>Tn</td><td>q (%)</td><td>Rn</td><td>Tn</td><td>q (%)</td><td>% Gap</td></tr><tr><td>16</td><td>10,000</td><td>0.3</td><td>(1,1,1)</td><td>138</td><td>145</td><td>95.2</td><td>140</td><td>145</td><td>96.6</td><td>1.4</td></tr><tr><td>17</td><td>13,000</td><td>0.3</td><td>(1,1,1)</td><td>167</td><td>179</td><td>93.3</td><td>173</td><td>181</td><td>95.6</td><td>2.3</td></tr><tr><td>18</td><td>15,000</td><td>0.3</td><td>(1,1,1)</td><td>176</td><td>187</td><td>93.1</td><td>168</td><td>188</td><td>95.5</td><td>2.2</td></tr><tr><td>19</td><td>17,000</td><td>0.3</td><td>(1,1,1)</td><td>188</td><td>202</td><td>93.1</td><td>195</td><td>205</td><td>95.1</td><td>2.0</td></tr><tr><td>20</td><td>18,000</td><td>0.3</td><td>(1,1,1)</td><td>192</td><td>207</td><td>92.7</td><td>198</td><td>209</td><td>94.6</td><td>1.9</td></tr><tr><td>21</td><td>19,000</td><td>0.3</td><td>(1,1,1)</td><td>195</td><td>211</td><td>92.4</td><td>201</td><td>212</td><td>94.4</td><td>2.0</td></tr><tr><td>22</td><td>20,000</td><td>0.3</td><td>(1,1,1)</td><td>196</td><td>214</td><td>91.6</td><td>200</td><td>214</td><td>93.5</td><td>1.9</td></tr></table>

classi<sup>fi</sup>cation method for customer segmentation. Our approach can not only identify key factors that affect customer behavior, but also help enterprises construct more scienti<sup>fi</sup>c CRM strategies through spatially analytical functions. Algorithm 2 details the attribute-reduction method that is able to deal with uncertain predicates.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2
Input:
Data set (DS);
Output:
{Classification Rules};
Method:
1.Begin
2.    DT←DS;/* regard the Data Set(DS) in Section 3 as the decision table(DT)*/
3.    DT=(O,AT ∪ {d});/* choose the decisional attributed, and gather the other attributes as conditional attributes in DT. O refers to the set of spatial objects that represents customers' locations*/
4.    x,y ∈ O ;/*where x and y are the elements of set O*/
5.    For each x do;
6.    For each y do;
7.    Compute S$_{AT}$(x);/*compute the similarity relation in DT as described in definition 3*/
8.    Compute ∂$_{AT}$(x);/*compute the generalized decision in DT as described in definition 5*/
9.    Compute f(x,y) ;/* to build the discernibility matrix for the reduction of customer information as described in definition 6*/
10.    Endfor;
11. Endfor;
12. For i=1 to |O| do;
13.    For each y do;
14.    Compute Δ;/*compute the relative reduct of DT as described in definition 6*/
15.    Compute Δ(i);/*compute the relative reduct of the items for item i as described in definition 6*/
16.    Endfor;
17. Endfor;
18. Output {Classification Rules};
19.End;
</div>

## 5. Computational experiments

## 5.1. Experimental data and software

The experimental data used for testing our proposed method contained 20,000 items of customer records from a large chain supermarket in Beijing, China. These records were stored in a SQL server 2000 used as the data warehouse. Subsequently, we used the digital map of Beijing stored in supermap3.0 (GIS software) and adopted 1532 buildings (Reference objects at level 1) as customer locations, based on the addresses of the customers. There were 400 themes of digital maps containing over 64,000 polygons, lines, and points present in parks, roads, shops, and other objects. ArcSDE [7] was used as the matching tool, which ful<sup>fi</sup>lled the function of spatial data engineering by integrating the spatial and non-spatial data of the customers. Visual Basic 6.0 was used as the platform.

We used 80% of the customers as the training set and the remaining 20% as the testing set in all of the experiments. By running the RS-based algorithm and the spatial ID3 algorithm [10] separately, we evaluated the performances of the algorithms, the results are presented in Tables 7–10 and Fig. 5, where n refers to the number of customers; t and $\left( l _ { 1 } , l _ { 2 } , l _ { 3 } \right)$ represent the support threshold and concept hierarchies of the spatial predicates in Algorithm 1, respectively; q(%) is the fraction of the number of correct classi<sup>fi</sup>cation rules (Rn) in the number of total classi<sup>fi</sup>cation rules (Tn), representing the accuracy/quality of the data classi<sup>fi</sup>cation method; Gap is the difference in the q(%) between the RSbased algorithm and spatial ID3 algorithm; and d is the number of decisional labels, which was assumed to be four in the following experiments.

## 5.2. Combined performance of our filtration algorithm and RS algorithm

We tested the time cost and classi<sup>fi</sup>cation quality of Algorithm 2 following Algorithm 1. The set of concept levels of the spatial predicate used for the correlation analysis was (2,1,1), and n was assumed to be 10,000 in the following experiments. As described in Fig. 5, the time cost of Algorithm 2 apparently decreases depending on the value of the support threshold used in Algorithm 1. As shown in Table 7, the classi<sup>fi</sup>cation quality q increases drastically when the <sup>fi</sup>ltration method is used. We can also see that the classi<sup>fi</sup>cation quality of Algorithm 2 is greatly enhanced when the support threshold (t) of Algorithm 1 increases. The best result is 94.9% for a support threshold value around 0.3. Combined with Algorithm 2, we found that Algorithm 1 not only cut down the computational costs because of the many redundant predicates <sup>fi</sup>ltered out, but also improved the accuracy of the classi<sup>fi</sup>cation because it eliminated classi<sup>fi</sup>cation rules containing irrelevant predicates.

![](/api/attachments/8G45PETW/fulltext/images/01e252b334d7ea33ba6759985eea71c4c08b5ed0a833a592cba893ada0677397.jpg)  
Fig. 5. Execution time of the combination of Algorithms 1 and 2.

In order to test the quality of Algorithm 2 enhanced with the application of Algorithm 1, a frequency-based <sup>fi</sup>ltration method [19] was used on the same customer dataset for a comparison. As shown in Table 8, when the support threshold is around 0.6, the best quality of the RS method is only about 87%, substantially less than 94.9%. As such, we can draw the conclusion that our proposed Algorithm 1 preserved more meaningful predicates than the frequency-based method, which eventually resulted in improving the data classi<sup>fi</sup>cation quality of Algorithm 2.

5.3. Performance of the classification quality with multiple-level predicates

We also performed a number of experiments where the spatial predicates had multiple concept levels. The lower the concept level was, the more dif<sup>fi</sup>cult it was to obtain precise predicates. In other words, the proportion of uncertain predicates gradually increased when the concept level decreased.

As can be seen in Table 9, the data classi<sup>fi</sup>cation quality of the RSbased algorithm gradually decreases as the concept level goes down. This means that having more uncertain predicates will reduce accuracy of Algorithm 2.

5.4. Quality comparison of spatial ID3 classification method and spatial RS classification method

We <sup>fi</sup>rst compared the quality of our Algorithm 2 (RS-based algorithm) with that of the spatial ID3 algorithm in a case where a clear predicate was used. The concept levels (1,1,1), coarsely representing the predicate g-close-to (x, y), described the relationship between two objects without any uncertain information. As described in Table 10, the quality of the two algorithms decreases when the number of samples ranges from 10,000 to 20,000. Moreover, we can see that the Gap in quality of the two algorithms becomes stable at approximately 2%. This shows that the data classi<sup>fi</sup>cation quality of Algorithm 2 is just slightly better than that of the ID3 algorithm.

We then performed a number of experiments to test the quality of the two algorithms in a case where spatial predicates had multiple concept levels. As described in Table 11, the quality Gap of the two algorithms becomes larger when the concept levels gradually decrease. This demonstrates that the data classi<sup>fi</sup>cation quality of our RS-based method is better than that of the ID3 algorithm, especially when more uncertain predicates are involved.

Our RS-based algorithm has a mechanism to accept and tolerate uncertain predicates (De<sup>fi</sup>nition 3 to 6). By applying Algorithm 2 to an incomplete information table, it is possible to obtain rules like:

(1) Avg\_Income (x, low) Close-to (x, high-bridge) ⇒ Profit (x, medium) ∨ Profit (x, low). Close-to-100m(residential-area, direct-bus)

(2) ∧ Close-to-200m(work-area, location-of-small-competitor) ∧ Avg-income(residential-area, medium) ⇒Pr ofit (x, high) ∨Pr ofit (x, extreme-high)

Relation of parameter $( l _ { 1 } , l _ { 2 } , l _ { 3 } )$ to the quality of the two algorithms.

<table><tr><td rowspan="2">Experiment no.</td><td colspan="3">Parameters</td><td colspan="3">ID3 algorithm</td><td colspan="3">RS algorithm</td><td>Difference</td></tr><tr><td>n</td><td>t</td><td> $(l_1, l_2, l_3)$ </td><td>Rn</td><td>Tn</td><td>q (%)</td><td>Rn</td><td>Tn</td><td>q (%)</td><td>% Gap</td></tr><tr><td>23</td><td>20,000</td><td>0.3</td><td>(1,1,1)</td><td>207</td><td>213</td><td>97.2</td><td>209</td><td>214</td><td>97.7</td><td>0.5</td></tr><tr><td>24</td><td>20,000</td><td>0.3</td><td>(2,1,1)</td><td>223</td><td>308</td><td>72.4</td><td>267</td><td>315</td><td>84.8</td><td>12.4</td></tr><tr><td>25</td><td>20,000</td><td>0.3</td><td>(2,2,1)</td><td>312</td><td>502</td><td>62.2</td><td>435</td><td>537</td><td>81.0</td><td>17.8</td></tr><tr><td>26</td><td>20,000</td><td>0.3</td><td>(2,3,1)</td><td>368</td><td>735</td><td>50.1</td><td>567</td><td>765</td><td>74.1</td><td>24.0</td></tr><tr><td>27</td><td>20,000</td><td>0.3</td><td>(3,3,1)</td><td>379</td><td>994</td><td>38.1</td><td>612</td><td>877</td><td>70.3</td><td>32.2</td></tr></table>

Uncertain values exist in the spatial predicates that render the above rules with two decisional values. Without a mechanism for handling uncertain predicates, the spatial ID3 algorithm could reduce the conditional attributes of a customer and forcibly map the customer into a single decisional value. This phenomenon results in many incorrect classi<sup>fi</sup>cations.

In summary, the combination of our two algorithms is superior to the traditional spatial data classi<sup>fi</sup>cation technologies [5,10,12,13] with respect to the following three aspects: (1) the ability to handle uncertain predicates, (2) the ability to identify more relevant predicates, and (3) the ability to obtain more quali<sup>fi</sup>ed classi<sup>fi</sup>cations.

## 6. Conclusion

This paper incorporated a spatial data classi<sup>fi</sup>cation function into the analytical CRM. Spatial predicates between a customer's location and the surrounding objects were integrated into customer attributes. A <sup>fi</sup>ltration algorithm for spatial predicates was then proposed by applying the MBR method to compute spatial predicates. It aims to identify the meaningful spatial factors that could affect customer behavior. A spatial data classi<sup>fi</sup>cation based on rough set theory is proposed to explicitly consider uncertain spatial predicate values and to ef<sup>fi</sup>ciently solve the problems related to such uncertainties and realize spatially enabled segmentation. Our method can identify different customer groups based on the spatial clues implied in the spatial classi<sup>fi</sup>cation rules. This research can help enterprises to ef<sup>fi</sup>ciently realize the objectives of customer acquisition, maintenance, improvement, and selection. Moreover, it can be applied to enhance government services, as all citizens and enterprises can be regarded as spatial objects.

A series of experiments emphasized the importance of the <sup>fi</sup>ltration method, which can help obtain better quality and reduces the time consumed. Furthermore, Algorithm 1 resulted in more quali<sup>fi</sup>ed classi<sup>fi</sup>cations compared with frequency-based algorithms. Our RS-based classi<sup>fi</sup>cation method, which incorporates a mechanism for handling uncertain predicates, could perform more accurate classi<sup>fi</sup>cations than the spatial ID3 algorithm.

Nevertheless, although we have achieved promising results, our research on spatially-enabled customer analysis could be further extended. We plan to propose a spatial data clustering method for selecting the sites for customer service centers, as well as a spatial trend detection method for identifying customer diversions, among others.

## Acknowledgement

This research was supported by the National Social Science Foundation of China under Grant 07CTQ009 and the National Natural Science Foundation of China under Grant 70533030.

## References

[1] M. Achita, G. Mark, S. Nattawat, Segmenting online customers to manage business resources: a study of the impacts of sales channel strategies on consumer preferences, Information & Management 43 (2006) 678–695.

[2] A. Amiri, Customer-oriented catalog segmentation: effective solution approaches, Decision Support Systems 42 (3) (2006) 1860–1871.

[3] T. Beaubouef, F. Petry, Information-theoretic measures of uncertainty for rough sets and rough relational databases Information Science 109 (14) (1998) 185–195

[4] E. Clementini, P. Di Felice, K. Koperski, Mining multiple-level spatial association rules for objects with a broad boundary, Data & Knowledge Engineering 34 (2000) 251–270.

[5] M. Ester, H.P. Kriegel, Knowledge discovery in spatial databases: focusing techniques for ef<sup>fi</sup>cient class identi<sup>fi</sup>cation, [R] Proceedings of 4th International Symposia on Large Spatial Databases, Maine, 1995, pp. 67–82.

[6] B. Fan, A hybrid spatial data clustering method for site selection: the data driven method of GIS mining, Expert Systems with Applications 36 (3) (2009) 3923–3926

[7] J. Han, M. Kamber, Data Mining: Concepts and Technique, Morgan Kaufmann, 2000, pp. 122–135.

[8] J.J. Jonker, N. Piersma, D. Van den Poel, Joint optimization of customer segmentation and marketing policy to maximize long-term pro<sup>fi</sup>tability, Expert Systems with Applications 27 (2) (2004) 159–168.

[9] S.Y. Kim, T.S. Jung, Customer segmentation and strategy development based on customer lifetime value: a case study, Expert Systems with Applications 31 (2006) 101–107.

[10] K. Koperski, J. Han, N. Stefanovic, An ef<sup>fi</sup>cient two-step method for classi<sup>fi</sup>cation of spatial data, In Proceeding of 8th Symposium on Spatial Data Handling SDH'98, Vancouver, 1998, pp. 44–54.

[11] J.H. Lee, S.C. Park, Intelligent pro<sup>fi</sup>table customers segmentation system based on business intelligence tools, Expert Systems with Applications 29 (1) (2005) 145–152.

[12] J.A. Mazanec, Simultaneous positioning and segmentation analysis with topologically ordered feature maps: a tour operator example, Journal of Retailing and Consumer Services 6 (4) (1999) 219–235.

[13] S.M. Musyoka, S.M. Mutyauvyu, J.B.K. Kiema, F.N. Karanja, D.N. Siriba, Market segmentation using geographic information systems (GIS): a case study of the soft drink industry in Kenya, Marketing Intelligence & Planning 25 (6) (2007) 632–642.

[14] Z. Pawlak, Rough set approach to knowledge-based decision support, European journal of Operational Research 29 (3) (1997) 1–10.

[15] L. Polkowski, S. Tsumoto, T.Y. Lin, Rough Set Methods and Applications, Springer-Verlag, Germany, 2000, pp. 567–571.

[16] B. Saglam, F.S. Salman, A mixed-integer programming approach to the clustering problem with an application in customer segmentation, European Journal of Operational Research 173 (2006) 866–879.

[17] A. Skowron, Extracting laws from decision tables: a rough set approach, Computational Intelligence 11 (3) (1995) 371–388.

[18] R. Slowinski, J. Stefanowski, Rough classi<sup>fi</sup>cation in incomplete information systems, Mathematical and Computer Modelling 12 (1989) 1347–1357.

[19] L. Wang, K. Xie, Ef<sup>fi</sup>cient discovery of multilevel spatial association rules using partitions, Information and Software Technology 47 (11) (2005) 829–840.

[20] M. Wedel, W.A. Kamakura, Market Segmentation: Conceptual and Methodologica Foundations, Kluwer Academic Publishers, 1998, pp. 126–227.

![](/api/attachments/8G45PETW/fulltext/images/194ab2e6380a982b17bee93a9aa778cab9e0e684b7967be6f20691eedbc154c2.jpg)

Bo Fan is associate professor at school of international and public affairs, Shanghai Jiaotong University. He has received PhD degree from Harbin Institute of Technology, and his major is management information system. His research interests include CRM, Decision support system, E-government and GIS. He has published more than 30 papers and 4 books in these areas.

![](/api/attachments/8G45PETW/fulltext/images/d30fe47ffc827cb1c512e2a824b6f3b48a4163395be4043f4f53f3e3b2a6669f.jpg)

Pengzhu Zhang is Chair Professor in MIS & E-Commerce, Director of Center for Management Information Systems, Antai School of Management, Shanghai Jiaotong University. His articles have appeared in Decision Support Systems, Information Systems Engineering and many journals in Chinese. His research interests include group decision / team support systems, <sup>fi</sup>nancial management information systems, E-government & E-commerce.
