---
otero_id: 11238
otero_key: "C8ZQYGJY"
title: "Designing a cross-language comparison-shopping agent"
authors: "Shiu-Li Huang; Yu-Hsiang Tsai"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.10.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing a cross-language comparison-shopping agent

Shiu-Li Huang ⁎, Yu-Hsiang Tsai

Department of Information Management, Ming Chuan University, No. 5, De Ming Rd., Gueishan Township, Taoyuan County 333, Taiwan, ROC

a r t i c l e i n f o

Article history: Received 3 August 2009 Received in revised form 29 August 2010 Accepted 24 October 2010 Available online 3 November 2010

Keywords: Shopbot Comparison-shopping Ontology Semantic similarity Formal concept analysis

## a b s t r a c t

This research pertains to the design and development of a shopbot called WebShopper+. This shopbot is intended to help customers <sup>fi</sup>nd and compare e-tailers that market their wares using different languages. WebShopper+ is built with a multilingual ontology to overcome the language barriers that arise with global e-commerce. This research proposes a semi-automatic method of constructing a multilingual ontology by using the formal concept analysis and association analysis. It also proposes an automatic method for the categorization of product data into prede<sup>fi</sup>ned classes, with the aim of alleviating administrators' task load. Additionally, a semantic search mechanism based on concept similarity is designed to assist customers in <sup>fi</sup>nding more desirable products. The experimental results show that these methods perform well and the shopbot can help customers <sup>fi</sup>nd real bargains on the Web and to <sup>fi</sup>nd products that cannot be bought locally. © 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Online purchase-decision aids are becoming more and more important as the number of e-tailers is increasing. Consumers may purchase products through shopbots that can collect useful information from numerous e-tailers and present the data in a meaningful way, providing customers with purchase-decision aids. Shopbots identify candidate vendors according to user-de<sup>fi</sup>ned criteria and subsequently help customers to compare these vendors. Thus, consumers can make better purchase-decisions and subsequently purchase from or place a bid with suitable vendors. Shopbots assist customers by allowing them to easily <sup>fi</sup>nd desirable bargains. In addition, they enable vendors to monitor their competition and to reach a larger customer base [8,17]. Beyond these fundamental services, some researchers have attempted to expand the service horizon of shopbots by focusing on the utility of consumer purchasing behavior [24], identi<sup>fi</sup>cation of the best price for a bundle of items [11], and integration of sales promotion information into search results [12]. Because most electronic purchases are still not automated, customers often expend excessive amounts of time in the buying process, which includes collection and interpretation of information on many vendors and products, making purchase decisions, and subsequently entering purchase and payment information. Software agent technologies such as a shopbot provide a basis to solve these issues as they automate the most time-consuming activities of the purchasing process [22].

However, existing shopbots are only designed to collect information from e-tailers that use common language, or e-tailers that reside in a single nation. As a result, many customers are unable to locate real bargains on the Web and many e-tailers are constrained from reaching much of their potential market [17]. Global reach is a major advantage of e-commerce, but language barriers diminish this advantage. Previous researches have revealed that the trade between countries that share a common language is three times greater than trade between countries without a common language [13]. In addition, Internet users tend to surf websites presented in their native language [14,20]. To solve this problem, Huang and Tsai developed a shopbot with a multilingual ontology that would allow customers use their native language in searching for online product catalogs that were presented in different languages. Their experimental result showed that customers are able to locate more products and <sup>fi</sup>nd a greater number of bargains over the Web, using their shopbot [17]. A multilingual ontology is the taxonomy (i.e., a hierarchical structure of classi<sup>fi</sup>cations for a given set of objects) of products, in which categorizations can be expressed in different languages and their subsumption and equivalence relationships can be de<sup>fi</sup>ned. However, system administrators have to build this ontology manually and de<sup>fi</sup>ne product-classi<sup>fi</sup>cation rules before the shopbot can collect product data from venders' websites. Since product information provided by vendors is massive and changes frequently and de<sup>fi</sup>ning relationships among thousands of classes in different languages would be very time-consuming, more automatic approaches are required for building ontology and classifying product data ef<sup>fi</sup>ciently. Moreover, Huang and Tsai have developed a semantic searching mechanism that can interpret equivalence and subsumption relationships between concepts described in different languages [17]. For instance, the concept of “information management” has the same meaning as “資訊管理” in Chinese. The concept of “electronic commerce” (EC) is a sub-concept of information management. However, this searching mechanism only considers equivalence and subsumption; it does not consider concept similarity. For instance, the concepts of “intelligent agent” and “electronic commerce” most de<sup>fi</sup>nitely have some relationship between them, but they are not equal, nor do they subsume each other.

This research aims to design and develop a shopbot that can help customers to compare products located in e-stores, using different languages. To overcome the shortcomings of existing shopbots, this research (1) proposes a semi-automatic method of constructing a multilingual ontology; (2) designs an automatic method of classifying product data into said ontology; and (3) proposes a semantic searching mechanism based on concept similarity. The designed shopbot is expected to aid customers in <sup>fi</sup>nding desirable bargains on the Web without language barriers. In addition, it is expected to reduce system administrators' task loads by automating the processes of ontology construction and data classi<sup>fi</sup>cation.

## 2. Related work

This section introduces the existing conceptualization of shopbots and comparison-shopping sites. Additionally, the technical foundations adopted to develop our shopbot are discussed.

## 2.1. Shopbots and comparison-shopping sites

Shopbots, also known as comparison-shopping agents, are automated tools that query e-commerce sites, such as online shops, to retrieve product information. They then parse the received information to extract useful product and vendor information, which can be used to aid customers in making purchase decisions. These agents employ an automatic process to build wrappers (software programs used to extract structured data from Web pages) and they utilize a number of rules to parse semi-structured Web pages [6]. Shopbots are one type of specialized agents that are designed to help users <sup>fi</sup>lter and process information, by retrieving product details and comments, comparing products, vendors, and services based on user-de<sup>fi</sup>ned criteria, searching for products or services of the best-value, monitoring product availability or special offers and discounts from online shops, recommending services and products, and identifying new products of potential interest [8].

BargainFinder was the <sup>fi</sup>rst shopbot developed by Andersen Consulting; this shopbot was used for online price comparisons of music CDs [22]. BargainFinder was subsequently blocked by music retailer sites and ceased operating because it only compared prices, ignoring all other product attributes. Jango avoided this issue by sending requests via a user's browser, rather than sending requests directly from the agent. Excite acquired Jango in 1997 and incorporated it into their search technology, effectively creating a vendor-biased comparison site. Some shopbots are able to learn users preferences and provide customized services. IntelliShopper observes users' shopping behavior and customizes the information it presents while protecting user privacy [23]. Oh!Hot provides intelligent assistance according to users' behaviors and recommends information on merchandise to those users most likely to <sup>fi</sup>nd them interesting or attractive [29]. Although existing shopbots cannot understand the retrieved information and cannot discover new vendors dynamically, these shortcomings can be resolved using concepts of the Semantic Web and Web services [8].

In contrast to shopbots, comparison-shopping sites do not rely on agent-based technology. These sites depend on vendors to provide a required set of information, or they operate as meta-search engines of vendor sites [8]. BizRate (www.bizrate.com), Shopzilla (www.shoppzilla. com), DealTime (www.dealtime.com), ShopLocal (www.shoplocal.com), and PriceGrabber (www.pricegrabber.com) are typical examples of comparison-shopping sites that receive product information from hundreds of online shops. Customers can obtain a search result in the form of a list of items, with prices from different shops, and they can then identify the shop that offers the best price. The customers can then click the link they choose, in order to purchase from the associated shop.

Reviewing the most popular comparison-shopping sites [7], it is readily apparent that existing sites only support keyword search and do not support semantic search. A keyword search is unable to process relationships between keywords and therefore cannot support searches in multiple languages, even if the keywords have the same meaning in different languages. Moreover, existing shopbots and comparison-shopping sites only collect information from e-retailers that use a common language, or that reside in the same nation, thus customers are often not able to locate many of the bargains that exist on the Web and e-retailers are incapable of reaching much of their potential customer base around the world.

Huang and Tsai began efforts to address the aforementioned shortcomings, designing a shopbot referred to as WebShopper. This shopbot can be used to perform online price comparisons of computer books [17]. WebShopper possesses a multilingual ontology that describes concepts in both Chinese and English, and provides a semantic searching mechanism that overcomes the language barrier. WebShopper can understand the concepts underlying words entered by users. For example, when a user enters the concept of “personal computer” as a search term, the searching mechanism will look for books pertaining to desktops, laptops, and handhelds, because the shopbot understands that desktops, laptops, and handhelds are a form of personal computer. Users can search for books by entering conceptual words in their native languages, even if foreign retailers are providing the books. The shopbot collects a wide array of product data from e-stores that are located in different countries and using different languages, and classi<sup>fi</sup>es this data using prede<sup>fi</sup>ned classi-<sup>fi</sup>cation rules.

As progressive as it is, the multilingual ontology of WebShopper must be constructed and maintained manually. As such, the ontology construction process is very time-consuming when the classi<sup>fi</sup>cation hierarchy is large and complex. Prede<sup>fi</sup>ning rules for the classi<sup>fi</sup>cation of product data is also troublesome, as an administrator must observe source websites and <sup>fi</sup>nd patterns in the product titles and categories. In addition, the semantic searching mechanism would only search for products based on the subsumption and equivalence relationships of the conceptual terms entered by the user. WebShopper does not consider other, similar concepts that might satisfy the user's criteria. To address the aforementioned issues, this research designs and develops an improved shopbot. As well as, it provides a method of semi-automatic ontology construction, an automatic product data classi<sup>fi</sup>cation approach and a semantic searching mechanism that also considers conceptual similarities.

## 2.2. Formal concept analysis

This study presents the design of a method for semi-automatic ontology construction and a corresponding approach to automatic data classi<sup>fi</sup>cation, based on the formal concept analysis (FCA). The methodology of the FCA was <sup>fi</sup>rst proposed by Rudolf Wille [32]. It can be used for the purposes of data analysis, information retrieval, knowledge representation, and other, similar <sup>fi</sup>elds. FCA provides a framework with which to structure concepts, and to analyze and visualize data. It is often applied to the construction of ontologies that are based on large data sets. FCA usually relies on concept lattices to construct domain ontologies [9,16,27,28]. Ontology, in the philosophical view, refers to a discipline that deals with the nature and the organization of being. In this sense, we can refer to an ontology as a particular system of categorizations that re<sup>fl</sup>ects a given perspective of the world. In computer science, an ontology refers to an

Table 1

engineering artifact consisting of (1) a speci<sup>fi</sup>c vocabulary, which appears as concepts and relations that are used to describe a certain reality and (2) a set of explicit assumptions regarding the intended meaning of the vocabulary [21].

FCA entails de<sup>fi</sup>ning a concept within a formal context, C, that is de<sup>fi</sup>ned as a triple $C = ( O , A , R )$ . A formal context consists of two sets, O and A, and their binary relation, R. Within the context, the set of O is referred to as Objects, while the set of A is referred to as Attributes (i.e., o∈O and $a \in A$ refer to a particular object and attribute in the relation R). The relation can be denoted by $( o , \ a ) \in R$ or oRa. Using such expressions, we can state that “object o has attribute a,” or “attribute a applies to object $\smash { 0 . \stackrel { \because } { } }$

Further, FCA is based on a formal understanding of concepts, which are units of thought that consist of two parts: extension and intension. Given a formal concept represented by the pair (E, I), where $E \subseteq O$ and is referred to as the Extent, and $I \subseteq A$ and is referred to as the Intent. Consider E′, the set of attributes that apply to all objects belonging to E, and I′, the set of objects having all attributes belonging to I. The duality relationship is then formalized by

$$
E ^ {\prime} = \{a \in A | o R a \forall o \in E \},\tag{1}
$$

which is the set of all attributes common to the objects in E, and

$$
I ^ {\prime} = \{o \in O | o R a \forall a \in I \},\tag{2}
$$

which is the set of all objects that have all attributes in I.

A concept lattice is composed of several formal concepts, each of which has its own extent and intent. Concept lattices are useful in formulating a conceptual structure that can be used to identify patterns and regularities in a given volume of visible and accessible data [10]. For this reason, concept lattices provide a means of displaying the implicit relationships between data entities. As well, they are also capable of ordering concepts from most general to most speci<sup>fi</sup>c [18].

In order to form a concept lattice, it is <sup>fi</sup>rst necessary to identify the hierarchical sub-super-concept relations between all formal concepts. Given two formal concepts, $\left( E _ { 1 } , \ I _ { 1 } \right)$ and $\left( E _ { 2 } , \ I _ { 2 } \right)$ , where $E _ { 1 } \subseteq E _ { 2 }$ and $I _ { 2 } \subseteq I _ { 1 }$ , the sub-super-concept relation can be expressed as $( E _ { 1 } , I _ { 1 } ) \subseteq$ $\left( E _ { 2 } , I _ { 2 } \right)$ . Thus we can state that $\left( E _ { 1 } , I _ { 1 } \right)$ is a sub-concept of, or subsumed by $\left( E _ { 2 } , I _ { 2 } \right)$ , and $\left( E _ { 2 } , I _ { 2 } \right)$ is a super-concept of, or subsumes $\left( E _ { 1 } , I _ { 1 } \right)$ . The inheritance relation ⊑ constitutes a hierarchical ordering of concepts [18]. The broadest concepts will be at the top of hierarchy within the lattice, referred to as the supermum, while the narrowest will be at the bottom of hierarchy, referred to as the infimum.

In general, the process of FCA-based ontology construction entails extracting keywords from data sources, constructing a formal context, and constructing concept lattices [2,31]. First, during the keyword extraction phase, a number of keywords are extracted from documents. Second, during the formal context construction phase, the relationships between keywords and documents are established using a table. Table 1 provides an example of a formal context, in which $\ " { } \mathbf { X } ^ { \prime }$ denotes that the keyword occurs in the corresponding document. Finally, in the concept lattice building phase, the formal context is transformed into a concept hierarchy based on two relationships: inheritance and intersection. These relationships are de<sup>fi</sup>ned as follows.

1. Inheritance: when all documents that contain keyword A also contain keyword B, but not all documents that contain keyword B necessarily contain keyword A, concept A is said to be a subconcept of B, expressed as $A \subseteq B .$

2. Intersection: when some documents that contain keyword A also contain keyword B, and vice versa, the concepts A and B are said to have an intersection relationship.

Example of formal context.

<table><tr><td></td><td>E-Commerce</td><td>B2B</td><td>B2C</td><td>C2C</td><td>SCM</td><td>CRM</td></tr><tr><td>Document 1</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Document 2</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr><tr><td>Document 3</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>Document 4</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Document 5</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>Document 6</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Document 7</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td></tr></table>

Thus, we can transform the formal context expressed in Table 1 into a visualized relationship diagram, referred to as a concept lattice, as in Fig. 1. In this <sup>fi</sup>gure, arrows denote an inheritance relationship and dashed lines represent an intersection relationship. This concept lattice represents an example of an ontology.

## 2.3. Semantic similarity

In order to design a semantic searching mechanism that takes concept similarity into consideration, we survey the existing methods of determining semantic similarity. Lin de<sup>fi</sup>nes a number of intuitive concepts pertaining to similarity, described as follows [19]:

1. Intuition 1: the commonality between concepts A and B determines their similarity. The greater the commonality they share, the more similar they are.

2. Intuition 2: the differences between A and B determine their similarity. That is, the lesser the differences between them, the more similar they are.

3. Intuition 3: When both A and B are identical, the maximum degree of similarity between A and B is reached, regardless of the commonality they share.

Semantic similarity also refers to similarity between two concepts in an $" _ { 1 S - Q " }$ taxonomy, such as WordNet, and re<sup>fl</sup>ects the extent to which they share information in common [26]. For instance, the concept of a “personal computer,” in English, and the concept of $\cdot \cdot \{ \boxed { E } \lambda \sqrt { \frac { 2 } { E } } , \lambda \} ,$ in Chinese, have the same meaning, but they are depicted using different syntax. Furthermore, we can say that “pizza” and “food” are more closely related than “pizza” and “drink” because the former are more similar in meanings than the latter.

The ontology-distance and information-theoretic approaches are the main methods of calculating semantic similarity. The ontologydistance approach, <sup>fi</sup>rst proposed by Wu and Palmer [33], considers the “is-a” link distance between two concepts in an ontology, that is,

$$
\operatorname{sim} \left(C _ {1}, C _ {2}\right) = \frac {2 \times N _ {3}}{N _ {1} + N _ {2} + 2 \times N _ {3}},\tag{3}
$$

![](/api/attachments/C8ZQYGJY/fulltext/images/a1b54522fe75a4190294bae46e16ddefe54b22b538c550fa8b4e24f2ee5dcc38.jpg)  
Fig. 1. Example of concept lattice.

where $N _ { 1 }$ and N<sub>2</sub> represent the number of “is- $- \vec { \mathbf { d } } ^ { \ " }$ links from $C _ { 1 }$ and $C _ { 2 }$ to their most speci<sup>fi</sup>c (lowest) common super-class $C _ { 0 }$ in the ontology. N represents the number o $\mathrm { \ s u } _ { \mathrm { i } S - \mathrm { q } } \mathrm { \ s u }$ links from $C _ { 0 }$ to the root of the ontology (the class at the top of the ontology). For instance, in Fig. 2, the most speci<sup>fi</sup>c common super-class of health food and fresh food is solid food. Therefore, $N _ { 1 } = 1 , N _ { 2 } = 1 , N _ { 3 } = 2$ , and sim HealthFood; FreshFood = ${ \frac { 2 \times 2 } { 1 + 1 + 2 \times 2 } } = 0 . 6 6 7 .$

Resnik [26] proposes an approach to measuring semantic similarity based on information theory [4]. In Resnik's approach, the more information two concepts share in common, the more similar they are considered to be. The information shared by two concepts in common, denoted by I(common $\left( C _ { 1 } , C _ { 2 } \right) )$ , also re<sup>fl</sup>ects the information content of those concepts that subsume them in the taxonomy, that is,

$$
\operatorname{sim} _ {\text { Resnik }} \left(C _ {1}, C _ {2}\right) = \max I \left(\operatorname{common} \left(C _ {1}, C _ {2}\right)\right) = - \log P \left(C _ {0}\right),\tag{4}
$$

where $C _ { o }$ is the most speci<sup>fi</sup>c common super-class between $C _ { 1 }$ and $C _ { 2 } ,$ and $P ( C _ { o } )$ is the probability that a randomly selected object belongs to $C _ { o } .$ For example, each node in Fig. 2 represents a concept, C, with a probability $P ( C )$ , the most speci<sup>fi</sup>c common super-class of health food and fresh food is solid food. Therefore, the semantic similarity based on the Resnik's approach is sim $_ \mathrm { R e s n i k } ($ (Health Food, Fresh Food)=−log P(Solid Food)=−log (0.0363)=1.44.

Lin similarly proposed a method that presents an informationtheoretic de<sup>fi</sup>nition of similarity that can be used in every domain with a probabilistic model [19]. This method is suitable for measurement of the semantic similarity between two concepts in an $\because \mathrm { i } s \mathrm { - } \mathsf { a } ^ { \flat }$ taxonomy. Lin used the notation sim $\left( C _ { 1 } , C _ { 2 } \right)$ to denote the similarity between x and $x _ { 2 } ,$ , where $x _ { 1 } \in C _ { 1 } , x _ { 2 } \in C _ { 2 }$ , and the selection of a generic $C _ { 1 }$ is not related to the selection of a generic $C _ { 2 } .$ The amount of information included in ${ } ^ { \mathfrak { u } } { x } _ { 1 } \in C _ { 1 }$ and $x _ { 2 } \in { \cal C } _ { 2 } "$ is

$$
- \log P (C _ {1}) - \log P (C _ {2}),\tag{5}
$$

where $P ( C _ { 1 } )$ and $P ( C _ { 2 } )$ are probabilities that a randomly selected instance belongs to the concepts $C _ { 1 }$ and $C _ { 2 } ,$ respectively. Supposing the taxonomy is a tree-like hierarchy, and $C _ { 0 }$ is the most speci<sup>fi</sup>c super-concept of $C _ { 1 }$ and $C _ { 2 } ,$ the commonality between $x _ { 1 }$ and $x _ { 2 }$ is $x _ { 1 } \in C _ { 0 }$ and $x _ { 2 } \in C _ { 0 } .$ As such, the similarity is expressed by

$$
\operatorname{sim} \left(x _ {1}, x _ {2}\right) = 2 \times \frac {\log P \left(C _ {0}\right)}{\log P \left(C _ {1}\right) + \log P \left(C _ {2}\right)}.\tag{6}
$$

For example, using Eq. (6), we can determine that the semantic similarity between health food and fresh food is $\begin{array} { r } { 2 \times \frac { l o g ( 0 . 0 3 6 3 ) } { l o g ( 0 . 0 1 1 3 ) \ + \ l o g ( 0 . 0 1 0 6 ) } = } \end{array}$ 0:734.

The ontology-distance approach may cause problems, however, if there are two concepts having a great distance between them due to the ontology hierarchy. When using the distance approach, such concepts may be determined to be less similar than is actually the case. The ontology-distance approach tends to produce a similarity calculation that is biased downward. The results of an experimental evaluation have shown that Lin's method produces output that is closer to true human judgments than does Rensik's method or the ontology-distance approach [19]. As such, this research adopts Lin's method to calculate semantic similarity and applies it to the design of a semantic searching mechanism.

![](/api/attachments/C8ZQYGJY/fulltext/images/9f6bd3eb35b29823da792a5ad55023801958b9d4a37db13b1e75cc561717b93d.jpg)  
Fig. 2. Example of concept hierarchy.

## 3. System architecture

Fig. 3 illustrates the system architecture of a cross-language shopbot. A prototype system, termed WebShopper+, was developed based on this architecture. WebShopper+ helps customers to compare vendors and purchase costs of computer and business books.

The data collection agent collects product data from two types of Web documents: XML and HTML documents. XML documents are acquired from e-stores that offer Web services, while HTML documents are acquired from e-stores that do not offer Web services. After the data collection agent has collected and parsed all of the useful product data, it then classi<sup>fi</sup>es the data according to a prede<sup>fi</sup>ned product ontology, calculates purchase costs according to list prices, delivery fees, and exchange rates, and then saves product related data into the product database. The purchase cost is calculated in a speci<sup>fi</sup>c currency by the following equation:

$$
\text { Purchase   cost } = (\text { list   price } + \text { delivery   fee }) \times \text { exchange   rate }.\tag{7}
$$

The exchange rate agent updates exchange rates daily. Calculating purchase cost in a speci<sup>fi</sup>c currency makes it easy for users to determine the prices they must pay to purchase products from different vendors and to <sup>fi</sup>nd the most economical distributor.

Customers can employ the semantic searching mechanism to search for products in different languages. This prototype supports Chinese, English, and Japanese. The minimum similarity threshold can be set by the user to <sup>fi</sup>lter out those concepts that are less likely to be of interest. After searching, the mechanism will list and sort similar concepts by descending similarity. Users can then click one of the listed concepts to view the products associated with it. They can then compare the items further, in term of purchase cost, to <sup>fi</sup>nd the best vendor.

System administrators use three different editors to maintain the product ontology, delivery fees, and exchange rates. Additionally, an ontology construction toolkit provides some tools to help administrators build the ontology in a semi-automatic manner.

## 4. Ontology construction method

This research proposes a novel approach to constructing a multilingual ontology and develops an ontology construction toolkit that includes a keyword extracting tool, FCA tool, and conceptmapping tool, to help administrators build their product ontology in a semi-automatic manner. The following subsections will introduce the procedure and set of tools.

## 4.1. Ontology construction procedure

To ef<sup>fi</sup>ciently construct a multilingual ontology that is capable of supporting product data classi<sup>fi</sup>cation and semantic search, a semiautomatic ontology construction procedure is proposed. The following steps detail this procedure:

1. Construct a classi<sup>fi</sup>cation tree for each vendor according to the taxonomy used by said vendor (e.g., the category hierarchy of computer and business books used by Amazon). This step assists administrators in building initial classi<sup>fi</sup>cation trees quickly.

![](/api/attachments/C8ZQYGJY/fulltext/images/2d8376aa650aa38b765da283c86fb78537636a04f842a9238b7187e4b5f2d11f.jpg)  
Fig. 3. System architecture of WebShopper+.

2. Use the keyword extraction tools to obtain keywords from book titles, then remove meaningless or infrequent words to form the keyword set.

請輸入書籍類別名稱：3D程式設計

語意關聯程度：大於0.7

搜尋清除

|3D 程式設計(1)

應用程式(0.91)

繪圖與多媒體(0.847)

Adobe (0.828)

簡報(0.791)

|3D(0.781)

Adobe Acrobat (0.772)

數位摄影(0.74)

圖像處理&創作(0.728)

3D繪圖(0.725)

|3D Studio Max (0.711)

|Mac (0.71)

動畫與多媒體(0.709)

Web繪圖(0.708)

電腦輔助設計(0.702)

Fig. 4. System interface.

3. Use the FCA tool to analyze the context of the book titles and keywords generated in Step 2, and further extend the classi<sup>fi</sup>cation trees produced in Step 1. For example, suppose there is a conceptual term, “Java,” in an original classi<sup>fi</sup>cation tree and that the FCA tool has found that an inheritance relationship exists between this concept and “JavaServer Pages.” If this inheritance relationship is not revealed in the original classi<sup>fi</sup>cation tree, the administrator is advised to extend the classi<sup>fi</sup>cation tree by adding the concept “JavaServer Pages” as a sub-concept of “Java.”

4. Combine all extended classi<sup>fi</sup>cation trees that use common languages into a single integrated one; this step generates a classi<sup>fi</sup>cation tree for each language.

5. Combine the trees, in different languages, into the <sup>fi</sup>nal ontology. First, the concept-mapping tool is used to translate non-English concepts into English. Second, compare these translated concepts with the concepts in the English tree. If there are two concepts in different trees that are equivalent, these two concepts, in their original languages, are de<sup>fi</sup>ned to have an equivalence relationship. If no equivalence relationship is de<sup>fi</sup>ned, their sub-concept words are then compared. If the majority of sub-concepts in the different trees are equivalent, these two concepts may have an equivalence relationship, thus they require manual review by the administrator. These trees, in different languages, are ultimately combined into an ontology according to the equivalence relationships between their concepts.

By following the above steps, a multilingual ontology can be generated to assist the shopbot in (1) classifying book data from bookstores that use different languages and (2) providing a crosslanguage semantic searching mechanism. In this ontology, only inheritance and equivalence relationships are assessed between concepts; interception relationships are not considered because this ontology is constructed to represent a classi<sup>fi</sup>cation hierarchy. Product data comprise instances of these concepts. In order to improve the performance of semantic search, these instances are stored in the

## 書籍查詢結果:3D程式設計

<table><tr><td>圖示</td><td>書名</td><td>作者</td><td>ISBN13</td><td>ISBN10</td><td>比價</td></tr><tr><td></td><td>3D Game Engine Design: A Practical Approach to Real-Time Computer Graphics (The Morgan Kaufmann Series in Interactive 3D Technology)</td><td>David H. Eberly</td><td>9781558605930</td><td>1558605932</td><td>比價</td></tr><tr><td></td><td>3D Game Engine Design: A Practical Approach to Real-Time Computer Graphics (The Morgan Kaufmann Series in Interactive 3D Technology)</td><td>David H. Eberly</td><td>9780122290633</td><td>0122290631</td><td>比價</td></tr><tr><td></td><td>3D Game Engine Programming (Game Development Series)</td><td>Oliver Duvel</td><td>9781592003518</td><td>1592003516</td><td>比價</td></tr><tr><td></td><td>3D Game Environments: Create Professional 3D Game Worlds</td><td>Luke Ahearn</td><td>9780240808956</td><td>0240808959</td><td>比價</td></tr><tr><td></td><td>3D Game Programming All in One (Course Technology PTR Game Development Series)</td><td>Kenneth Finney</td><td>9781592001361</td><td>159200136X</td><td>比價</td></tr></table>

Fig. 5. Books belonging to speci<sup>fi</sup>ed concept.

## 此書籍有下列賣家：

<table><tr><td>圖示</td><td>書名</td><td>作者</td><td>原有價格</td><td>換算後價格(原價+運費)*匯率</td><td>賣家</td></tr><tr><td></td><td>3D Game Environments: Create Professional 3D Game Worlds</td><td>Luke Ahearn</td><td>GBP27.54</td><td>NTD1171.272</td><td>Amazon (UK)</td></tr><tr><td></td><td>3D Game Environments: Create Professional 3D Game Worlds</td><td>Luke Ahearn</td><td>GBP27.54</td><td>NTD1237.2219</td><td>Amazon (US)</td></tr><tr><td></td><td>3D Game Environments: Create Professional 3D Game Worlds</td><td>Luke Ahearn</td><td>USD37.96</td><td>NTD1580.8214</td><td>Amazon (US)</td></tr><tr><td></td><td>3D Game Environments: Create Professional 3D Game Worlds</td><td>Luke Ahearn</td><td>NT1748.0</td><td>NTD1813.0</td><td>Books (TW)</td></tr></table>

Fig. 6. Comparison of vendors of similar products.

product database along with the concept labels they are associated with. Administrators, with the assistance of the ontology construction process and toolkit, are able to construct a product ontology with a greater degree of accuracy and ef<sup>fi</sup>ciency. In addition, they do not need to manually formulate the classi<sup>fi</sup>cation rules for product data. The tools designed to support the ontology construction are described in detail in the following subsections.

## 4.2. Keyword extraction tool

The keyword extraction tool uses an n-gram method as well as part-of-speech taggers to extract keywords from product titles. An ngram is a sub-sequence of n items taken from a larger sequence [3]. It is typically used in various <sup>fi</sup>elds of statistical natural language processing. The items can be letters or words. Using letter-level 4- grams, for example, the phrase “easy\_or\_hard” can be split into 4- character substrings, such as “easy,” “asy\_,” “sy\_o,” to “\_har,” and “hard.” The keyword extraction tool uses the word-level n-gram method to extract keywords from product titles. For example, the book title “Learning Java programming language” can be divided into the keywords “Java” and “language” using a 1-gram method, “programming language” using a 2-gram method, and “Java programming language” using a 3-gram method.

The tool uses the CKIP part-of-speech tagger to tag the part-ofspeech for words in Chinese book titles. In addition, it uses Mecab, which is a part-of-speech and morphological analyzer to deal with Japanese book titles, and it uses OpenNLP to tag the part-of-speech for words in English book titles. After tagging, the tool extracts nouns, using 1, 2 or 3-grams to generate the candidate conceptual words that will be used in the subsequent FCA.

## 4.3. Formal concept analysis tool

To perform FCA, the FCA tool generates the formal context representing the relationship between product titles (objects) and their keywords (attributes). It then applies association analysis to determine the inheritance relationships between concepts. Association analysis is a technique developed in the <sup>fi</sup>eld of data mining; it can <sup>fi</sup>nd co-occurrence patterns from a large data source. In identifying association rules, association analysis depends on the measures of support and confidence. The FCA tool employs association analysis to <sup>fi</sup>nd inheritance relationships between concepts. First, the association analysis generates a frequent 2-item set that re<sup>fl</sup>ects keyword pairs that frequently co-occur in product titles. For example, if the keyword “programming language” usually appears with the keyword “Java” we can likely conclude that the concepts “programming language” and “Java” have an intersection or inheritance relationship. Second, the con<sup>fi</sup>dence of the association rules “Java→programming language” and “programming language→Java” are calculated. If a con<sup>fi</sup>dence of an association rule, such as “Java→programming language”, is equal to or slightly less than 1 we can likely conclude that programming language is a super-concept of Java, according to the theory of FCA. RapidMiner is used to perform the association analysis in the FCA process. We de<sup>fi</sup>ne the minimum con<sup>fi</sup>dence to be 0.9 and the minimum support to be 0.6 in generating the association rules. Classi<sup>fi</sup>cation trees are extended according to these rules.

## 4.4. Concept-mapping tool

To combine classi<sup>fi</sup>cation trees from different languages into a single ontology, we use English as the pivot language for translations between different languages. The concept-mapping tool uses the Google Dictionary API and the Wikipedia API to perform the automatic translation. First, the tool uses the Google Dictionary API to access the Japanese–English and Chinese–English dictionaries, to automatically translate concepts presented in Japanese or Chinese into English. However, using bilingual dictionaries does not allow us to address some words, such as proper nouns and abbreviations. To tackle this problem, the tool also accesses the Wikipedia API to deal with conceptual words that cannot be translated into English simply by looking to a bilingual dictionary. Those words that cannot be automatically translated using the Google Dictionary or Wikipedia APIs are then manually removed, revised or translated by an administrator. This is done, for example, by using Yahoo! Kimo Dictionary, Sanseido Web Dictionary or Yahoo! Japan Dictionary. After completion of the above steps, the tool detects which concepts are equivalent between different languages and helps the administrator to combine the classi<sup>fi</sup>cation trees from each language into the <sup>fi</sup>nal ontology.

## 5. Data collection agent and data classi<sup>fi</sup>cation method

The data collection agent retrieves product data from e-stores. Some e-stores provide Web services that allow other applications to access their product data. A Web service is a software system designed to support interoperable machine-to-machine interaction over a network [15]. Web services provide a standard protocol for the exchange of data between machines, using XML format. The data collection agent uses a Web service request to query the Web services provided by e-stores. First, the agent requests product data via a REST (Representation State Transfer) style Web service. Then, the agent receives a number of XML documents in reply, which include the product data, and subsequently parses them to extract useful information.

However, there are still many e-stores that do not provide these Web services. The data collection agent uses a tool referred to as a “Web spider” to retrieve Web pages in HTML format. A Web spider, also known as Web crawler or Web robot, is a software program used to browse websites automatically. It is usually used to generate a copy of all the visited pages so that a search engine can build indexes. The freeware tool HTTrack is an example of a typical Web spider. It crawls across Web pages based on some initial seeding data (starting pages), and retrieves the associated pages that match some prede<sup>fi</sup>ned conditions.

After product pages are collected, the data collection agent parses these pages and extracts useful product information. The agent automatically classi<sup>fi</sup>es this product data as per the prede<sup>fi</sup>ned categorizations in the product ontology. The classi<sup>fi</sup>cation procedure is described as follows:

1. The agent collects product data from online bookstores and identi<sup>fi</sup>es book titles, as well as the books' original categories, as de<sup>fi</sup>ned by the bookstores.

2. The agent then searches within the ontology for the concepts that match with the original category of the product. Because the concepts in the product ontology are sourced from keywords in book titles and the original book categorizations, all book data can be mapped to a corresponding concept.

3. Finally, the agent checks if there are sub-concepts that are subsumed by the corresponding concept in the ontology. It then <sup>fi</sup>nds the most speci<sup>fi</sup>c concept that is contained in the book title and uses this to determine the classi<sup>fi</sup>cation of the book data.

When the agent collects product data, it also needs to update the existing data in its product database. The agent compares the collected data against the database, according to the book's ISBN. If no change is necessary, the agent is <sup>fi</sup>nished. The agent records the most recent time of access to a given set of product details. If a product has not been accessed for a lengthy period of time, the agent concludes that this product has been removed by the vendor and deletes it from the database accordingly.

## 6. Semantic search

Semantic search is designed to help customers <sup>fi</sup>nd products that have a high semantic similarity with some speci<sup>fi</sup>ed concept. For example, the concept of “conveyance” could also refer to “transportation,” or “vehicle,” and may include the sub-concept of “train.” If we type “conveyance” into a keyword search, we will only retrieve those items that include the keyword “conveyance” in their title. A keyword search mechanism cannot identify related results like “transportation,” “vehicle,” or “train,” even though they share similar meaning. Further, we are unable to obtain any results pertaining to the concept of “conveyance” by typing the keyword “交通工具,” in Chinese, even though the meaning is identical. To address these gaps, this system provides a semantic search engine that will assist users in <sup>fi</sup>nding products based on the semantic meaning of speci<sup>fi</sup>ed concepts.

To enable the shopbot to understand conceptual meaning, an ontology is expressed in OWL to describe concepts and conceptual relationships. In the domain of the Semantic Web, an ontology is a document or a <sup>fi</sup>le that describes taxonomy and a set of inference rules that de<sup>fi</sup>ne the relationships between terms [1]. OWL is a language advocated by the W3C to represent ontologies that are intended for processing by software applications. For example, if we would like to express the two concepts of electronic commerce and EC as being equivalent, we can use the following OWL tags to do so.

bowl:Class rdf:ID="Electronic\_Commerce"/N

bowl:Class rdf:ID="EC"N

$$
\begin{array}{l} \text { <  owl:equivalentClass rdf:resource = "#Electronic_Commerce" / > } \\ \text { < / owl:Class>} \end{array}
$$

We also can indicate that the concept of “Electronic Commerce” is equivalent to the concept of “電子商務,” in Chinese, or “Eコマース,” in Japanese, in a similar manner. To express an “is-a” relationship between concepts, such as “B2B is a form of electronic commerce,” we can use the following OWL tags to do so.

bowl:Class rdf:ID="B2B"N

$$
\begin{array}{l} \text { <  rdfs:subClassOf   rdf:resource = "#Electronic_Commerce" / > } \\ \text { < /owl:Class>} \end{array}
$$

According to the above statements, an OWL reasoner can infer the implicit relationships (e.g., that “B2B” is a type of “電子商務” and a type of “Eコマース”). The multilingual ontology can support users input of conceptual words in their native language, searching for product titles described in English, Chinese, or Japanese.

When a customer inputs a conceptual word and speci<sup>fi</sup>es the minimum semantic similarity to consider, the data is transmitted to the searching mechanism, which is developed using the Jena API. The mechanism will reason, based on the ontology, and attempt to determine if there is a consistent concept amongst the search terms. The system will then begin to calculate the semantic similarities between the speci<sup>fi</sup>ed concepts and other concepts in the ontology, using Lin's method [19]. Finally, the concepts that have a similarity greater than the user-de<sup>fi</sup>ned parameter are returned. This semantic searching mechanism differs from the mechanism proposed by previous research [17]. Previous work has only considered subconcepts of a queried concept. But in this research, the semantic searching mechanism considers all concepts having high similarity with the queried concept. In other words, the search range can be viewed as a circle, where the center of a circle is the queried concept and the radius is determined by the user-de<sup>fi</sup>ned minimum semantic similarity.

## 7. System evaluation

This research proposes a prototype system, referred to as WebShopper+, which is developed based on the proposed architecture. WebShopper+ is intended to help customers search for computer books and business books, and to aid the comparison of their purchase costs and their respective vendors. WebShopper+ collects book data from the most popular online book-sellers, including Amazon (America, England, and Japan), Yahoo Shopping (Japan), Books (Taiwan), and Eslite (Taiwan) (note that Books and Eslite do not provide Web services). This shopbot deals with new books only and excludes used books. The bot is implemented using the Java programming language, with the Jena API.

Users are able to use their native languages to search for books. For example, a Taiwanese customer can enter the conceptual word “3D 程式 設計,” which means 3D programming, and can choose 0.7 as the minimum semantic similarity for the search results. Fig. 4 depicts the search results for this query, where the listed concepts are similar to “3D 程式設計,” with the similarity score provided (in parentheses). The top 10 concepts returned are 3D 程式設計 (3D programming), 應用程式 (applications), 繪圖與多媒體 (graphics and multimedia), Adobe, 簡報 (presentation), 3D, Adobe Acrobat, 數位攝影 (digital photography), 圖像 處理 & 創作 (image manipulation & creation), and 3D 繪圖 (3D graphics).

The customer clicks the concept they <sup>fi</sup>nd most interesting and all books belonging to this category are returned (see Fig. 5). As the user locates the book that he needs, he can press the button “比價” (compare prices) to check which vendors sell this product and at what prices, in order to <sup>fi</sup>nd the best vendor. Fig. 6 shows, in this case, that the <sup>fi</sup>rst item sold by Amazon in the United Kingdom is the cheapest book (NTD 1171) and the last item sold by Books in Taiwan is the most expensive one (NTD 1813). In this case, WebShopper+ enables the customer to use Chinese to search for English books and to reach foreign vendors. Thus, the customer saves NTD 642 if he purchases the book from Amazon in the UK, compared to Books, which is located in Taiwan. The customer can visit the vendor's page by clicking the book title and can then purchase the book.

## 7.1. Evaluation of the ontology construction and data classification methods

We now present a performance evaluation of the ontology construction method, measuring its precision and coverage. The system collected book data from e-tailers prior to April 1, 2009. In total, 1,213,628 pieces of data pertaining to 495,787 distinct books was collected. The ontology (accessible at http://sites.google.com site/shiulihuang/<sup>fi</sup>les/WebshopperPlus.rar) was constructed based on this data set, using the proposed ontology construction method and tools.

Four domain experts were invited to participate in the evaluation. The ontology was divided into two sections: computer books and business books. Two of the experts had pursued graduate studies in Information Management and Computer Science, respectively, and were therefore tasked with evaluating the ontology of computer books. The other two experts had pursued graduate studies in Information Management and Marketing Management, respectively, thus they were responsible for evaluating the ontology of business books.

After the domain experts had determined the number of misplaced and misnamed concepts, the precision of the ontology construction method was calculated by the following equation:

$$
\text { Precision   of   ontology   construction } = \frac {\text { The   number   of   accurate   concepts }}{\text { The   number   of   concepts   in   ontology }}.\tag{8}
$$

The experts also determined the coverage of the semi-automatic ontology construction method. The coverage represents the completeness of the ontology and can be calculated by the following equation:

$$
\text { Coverage   of   ontology   construction } = \frac {\text { The   number   of   concepts   in   ontology }}{\text { The   number   of   concepts   that   should   be   included   in   ontology }}.\tag{9}
$$

Thus, we can evaluate whether the ontology, built using our semiautomatic ontology construction method, is comparable to the ontology that was manually constructed by experts.

The ontology pertaining to computer books contained 1792 concepts. The degrees of precision of the ontology, as reported by the two relevant domain experts, were 99.944% and 95.647%, with an average of 97.796%. The coverage values reported were 99.666% and 99.335%, with an average of 99.501%. The ontology pertaining to business books contained 859 concepts. The precision values reported by the two relevant experts were 98.254% and 97.090%, with an average of 97.672%. The coverage values reported were 100% and 99.768%, with an average of 99.884%. These results suggest that the proposed ontology construction method is capable of achieving a degree of precision and coverage. Our semi-automatic method performs very well (comparable to experts in the <sup>fi</sup>eld) at a very low cost. In addition, our method requires less time and a lower human task load than the manual construction of the ontology.

In order to assess the performance of the automatic classi<sup>fi</sup>cation method, we measure the precision of the classi<sup>fi</sup>cation method. The system re-collected book data from the same online book stores during the period from April 1 to May 15, 2009. In addition to the original book data collected prior to April 1, 3102 new pieces of data were collected on 723 distinct books. We randomly selected 100 books from the product database, and invited a domain expert (i.e., a graduate student that had majored in Information Management) to determine whether this new data was classi<sup>fi</sup>ed into appropriate classes. The precision of the data classi<sup>fi</sup>cation method is calculated as follows:

$$
\text { Precision   of   classification   method } = \frac {\text { The   number   of   books   that   are   classified   accurately }}{\text { The   number   of   randomly   selected   books }}.\tag{10}
$$

The precision of the classi<sup>fi</sup>cation method was determined to be 100%. This result indicates that this method is capable of automatically, and correctly, classifying book data into the concepts prede<sup>fi</sup>ned in the ontology.

## 7.2. Evaluation of shopbot usefulness

In order to show that the shopbot is useful (i.e., that it truly aids customers in their search for real bargains on the Web), we assessed a random sample of 100 books to determine whether the majority of products tended to be distributed by e-stores sharing a common language, as well as whether differences in purchase costs existed among e-stores.

Table 2 shows the exchange rates and shipping fees used in this evaluation. The results show that two or more vendors sell the 56 books. The maximum difference in purchase cost was NTD 2750.495 (the book Advances in Knowledge Discovery and Data Mining: 12th Pacific-Asia Conference, the most expensive offer, was sold for NTD 7220 by Books in Taiwan, while the cheapest offer was NTD 4469.505, by Amazon in the United Kingdom) and the average difference between the highest and lowest purchase cost was NTD 399.806. This means that customers can save costs by using the shopbot. There are 29 books sold in two or more nations. Further, we found that 8 books were only sold in Taiwanese e-stores, 28 books were only sold in

Table 2  
Exchange rates and shipping fees used in evaluation.

<table><tr><td>Exchange rate</td><td>Shipping fee</td></tr><tr><td>USD 1 = NTD 32.975</td><td>Amazon US: USD 9.98</td></tr><tr><td>GBP 1 = NTD 53.83</td><td>Amazon UK: GBP 7.98</td></tr><tr><td>JPY 1 = NTD 0.3443</td><td>Amazon JP: JPY 2100Yahoo! Japan Shopping: JPY 1700Eslite: NTD 50Books: NTD 65</td></tr></table>

NTD: New Taiwan dollar; USD: United States dollar; GBP: Pound sterling; JPY: Japanese yen.

English e-stores, and 54 books were only sold in Japanese e-stores. These results reveal that cost variances do exist on the Web and that some products only exist in e-stores employing a certain language. The shopbot is able to help customers search for real bargains on the Web and to buy products that cannot be bought in their local countries.

## 7.3. Evaluation of user satisfaction

In order to prove that the shopbot is able to satisfy users' demands, we conducted an Internet experiment. We invited Internet users to use a prototype of the proposed system, which incorporated two semantic searching mechanisms: searching for similar concepts and searching for sub-concepts. We asked users to search for any computer or business books, using each of the two mechanisms, and employing Chinese, Japanese, or English words as search terms. The subjects were then asked to <sup>fi</sup>ll out a questionnaire to measure their information and system satisfaction. We used metrics of information quality and system quality de<sup>fi</sup>ned by DeLone and McLean's Information Systems Success Model [5]. The subjects' experiences with online shopping and background data were also collected as part of the questionnaire.

The invitation message was posted on the e-shopping and book forums of a bulletin board system (BBS) entitled PTT (ptt.cc), from June 30 to July 4, 2009. PTT is the largest BBS in Taiwan. There were 32 Internet users that participated in the experiment during this period. Table 3 summarizes the respondents' pro<sup>fi</sup>les. 37.5% of the respondents had experience purchasing items from foreign e-stores. The reasons for these purchases were that the products could only be bought from those other countries or that the products sold by foreign e-stores were cheaper. 50% of the subjects felt that the biggest dif<sup>fi</sup>culty in shopping at foreign e-stores was that they could not search for products using their native language. 46.9% of subjects indicated that their biggest dif<sup>fi</sup>culty in shopping at foreign sites was that they could not understand the foreign languages used. Therefore, language issues remain the biggest barriers to transacting at foreign estores.

Demographic data of respondents.

<table><tr><td>Measure</td><td>Items</td><td>Frequency</td><td>Percent</td></tr><tr><td rowspan="2">Gender</td><td>Male</td><td>19</td><td>59.4</td></tr><tr><td>Female</td><td>13</td><td>49.6</td></tr><tr><td rowspan="2">Age</td><td>25~29</td><td>21</td><td>65.6</td></tr><tr><td>20~24</td><td>11</td><td>34.4</td></tr><tr><td rowspan="3">Education</td><td>Master&#x27;s degree</td><td>4</td><td>12.5</td></tr><tr><td>Bachelor&#x27;s degree</td><td>25</td><td>78.1</td></tr><tr><td>Senior high school</td><td>3</td><td>9.4</td></tr><tr><td rowspan="10">Occupation</td><td>Service</td><td>2</td><td>6.3</td></tr><tr><td>Education/Research</td><td>1</td><td>3.1</td></tr><tr><td>Communication/Public relations/Advertising/Marketing</td><td>1</td><td>3.1</td></tr><tr><td>Information Technology</td><td>6</td><td>18.8</td></tr><tr><td>Manufacturing</td><td>1</td><td>3.1</td></tr><tr><td>Student</td><td>11</td><td>34.4</td></tr><tr><td>Medical</td><td>1</td><td>3.1</td></tr><tr><td>Arts</td><td>1</td><td>3.1</td></tr><tr><td>Others</td><td>2</td><td>6.3</td></tr><tr><td>Unemployed</td><td>6</td><td>18.8</td></tr><tr><td rowspan="2">Experience in using a shopping comparison website</td><td>Yes</td><td>12</td><td>37.5</td></tr><tr><td>No</td><td>20</td><td>62.5</td></tr><tr><td rowspan="2">Experience in purchasing from a foreign e-store</td><td>Yes</td><td>12</td><td>37.5</td></tr><tr><td>No</td><td>20</td><td>62.5</td></tr></table>

Questions 1, 2, and 3 of the questionnaire were used to measure the information quality with respect to accuracy, completeness, and relevance. Questions 4, 5, and 6 were used to measure the system quality, in terms of functionality and importance. For questions 1 through 6, we used a 7-point Likert scale to measure the respondent's degree of agreement, where 1 represented extreme disagreement and 7 represented extreme agreement. We used a paired sample t-test to examine the difference in quality between the two systems, the results of which are shown in Table 4.

These results indicate that System 2, which incorporates the semantic searching mechanism addressing concept similarity, has better information quality in terms of accuracy, completeness, and relevance, versus System 1, which has a semantic searching mechanism that takes sub-concepts into consideration. With regard to system quality, the subjects indicated that System 2 was more useful for international comparison-shopping than System 1. However, the functionality of the two systems was not signi<sup>fi</sup>cantly different. The reason for this similarity may be that these systems used the same data sources, ontology, and user interface.

Overall, these evaluations have validated the effectiveness of WebShopper+. The shopbot is able to correctly build a multilingual ontology, to collect product data from e-stores that are located in different countries and using different languages, to precisely classify product data into the categories prede<sup>fi</sup>ned in the ontology, to help customers search for real bargains on the Web using their native languages and buy products that cannot be bought in their local countries, and to improve user satisfaction.

## 8. Conclusion

Existing shopbots and comparison-shopping sites only collect information from e-retailers that use a given language or exist within the same nation due to which customers are unable to <sup>fi</sup>nd real bargains on the Web, and e-tailers are incapable of reaching the entirety of their potential global customer base. A multilingual

## Table 4

Paired-samples t-test of systems with different searching mechanisms.

<table><tr><td>Options</td><td>System 1 [mean (SD)]</td><td>System 2 [mean (SD)]</td><td>t-value (p-value)</td></tr><tr><td>1. Results of this searching mechanism are accurate</td><td>4.50(1.295)</td><td>5.34(1.285)</td><td>4.834***(0.000)</td></tr><tr><td>2. Results of this searching mechanism are complete</td><td>4.66(1.359)</td><td>5.09(1.228)</td><td>2.239*(0.032)</td></tr><tr><td>3. Results of this searching mechanism are relevant</td><td>4.50(1.459)</td><td>6.13(0.609)</td><td>8.143***(0.000)</td></tr><tr><td>4. This searching mechanism can assist me in finding the best offer</td><td>4.88(1.008)</td><td>5.03(1.062)</td><td>1.153(0.258)</td></tr><tr><td>5. This searching mechanism can assist me in finding foreign sources of products</td><td>4.97(1.177)</td><td>5.19(0.931)</td><td>1.422(0.165)</td></tr><tr><td>6. This searching mechanism is important for international comparison-shopping</td><td>5.00(1.136)</td><td>5.66(0.937)</td><td>4.715***(0.000)</td></tr></table>

System 1: System considering sub-concepts, System 2: System considering similar concepts.

ontology is required to enable a shopbot to understand various concepts in different languages. As product information that is provided by vendor sites is frequently changed, more automatic approaches are needed in building ontologies and in classifying product data ef<sup>fi</sup>ciently. This research has proposed a design for a shopbot, termed WebShopper+, to address these problems, proposing a semi-automatic ontology construction method, an automatic data classi<sup>fi</sup>cation method, and a semantic searching mechanism for inclusion. This shopbot possesses a multilingual ontology, which can assist users in searching for products using their native languages. The shopbot is able to help customers overcome language barriers that currently exist in most online shopping contexts, and to assist customers in <sup>fi</sup>nding desirable bargains more easily. In addition, the proposed design also enables vendors to monitor their competitors and to reach more customers globally. The evaluation results suggest that the proposed ontology construction method is able to achieve high precision and coverage. The classi<sup>fi</sup>cation method can automatically classify product data correctly. Moreover, the shopbot is able to bene<sup>fi</sup>t customers by comparing purchase costs and product vendors that are located across different e-stores and that are using different languages. Using the shopbot, customers can locate real bargains on the Web and potentially purchase products that are not available in their own countries.

Since the language barrier, which poses an impediment to global e-commerce, still exists, the requirement for a cross-language comparison-shopping agent is becoming more apparent. A multilingual ontology will enable a shopbot to understand concepts in different languages, which not only addresses the language issue but also enables searching mechanisms in <sup>fi</sup>nding more suitable, relevant products. Although this prototype only addresses books and only supports Chinese, English, and Japanese languages, the system architecture can easily be expanded to support all human languages and all types of products. Moreover, the proposed ontology construction and classi<sup>fi</sup>cation methods save signi<sup>fi</sup>cant amount of time and resources while maintaining high accuracy. These methods can be employed in any context that entails ontology construction and data classi<sup>fi</sup>cation, such as document management systems and search engines.

The purchase decision-making process includes the following steps: need identi<sup>fi</sup>cation, information search, negotiation, purchase and delivery, and after-purchase service and evaluation [25,30]. WebShopper+ supports the information search phase by answering the questions “what to buy?” and “from whom?” irrespective of the location of vendors or their languages. However, in order to overcome the language barrier, the other phases must also be supported. In the need identi<sup>fi</sup>cation phase, a recommender agent is required to proactively provide product information to customers on the basis of their pro<sup>fi</sup>les, preferences, and contexts. In the last three phases, related intelligent agents and intermediaries that can act as a proxy on the customer's behalf to communicate with foreign vendors, to deal with international payments, deliveries, duties, and laws are also required. Thus, research that attempts to determine the best approach to the design of the agents and business models for these intermediaries is likely to prove fruitful.

## References

[1] T. Berners-Lee, J.A. Hendler, O. Lassila, The semantic web, Scienti<sup>fi</sup>c American 284 (5) (2001) 34–43.

[2] ChenD.-N. , WuC.-H. , An ontology-based document recommendation system: design, implementation, and evaluation, Proceedings of the Paci<sup>fi</sup>c Asia Conference on Information Systems, Suzhou, China, 2008, pp. 469–480.

[3] D.J. Cohen, Recursive hashing functions for N-grams, ACM Transactions on Information Systems 15 (3) (1997) 291–320.

[4] T.M. Cover, J.A. Thomas, Elements of Information Theory, Wiley, New York, 1991.

[5] W.H. DeLone E.R. McLean The DeLone and McLean Model of Information Systems Success: A 10-year update, Journal of Management Information Systems 19 (4) (2003) 9-30

[6] DoorenbosR.B. , EtzioniO. , WeldD.S. , A scalable comparison-shopping agent for the World Wide Web, Proceedings of the 1st International Conference on Autonomous Agents, Marina del Rey, California, United States, 1997, pp. 39–48.

[7] eBizMBA, Top 20 Comparison Shopping Websites, Retrieved August 1, 2009, from http://www.ebizmba.com/articles/shopping

[8] M. Fasli, Shopbots: a syntactic present, a semantic future, IEEE Internet Computing 10 (6) (2006) 69–75.

[9] A. Formica, Ontology-based concept similarity in formal concept analysis, Information Sciences 176 (18) (2006) 2624–2641.

[10] B. Ganter, R. Wille, Formal Concept Analysis: Mathematical Foundations, Springer, New York, 1999.

[11] R. Gar<sup>fi</sup>nkel, R. Gopal, A. Tripathi, F. Yin, Design of a bundle shopbot, Decision Support Systems 42 (3) (2006) 1974–1986.

[12] Gar<sup>fi</sup>nkelR. , GopalR. , PathakB. , YinF. , Shopbot 2.0: integrating recommendations and promotions with comparison shopping, Decision Support Systems 46 (1) (2008) 61–69.

[13] GhemawatP. , Distance still matters: the hard reality of global expansion, Harvard Business Review (September, 2001) 137–147.

[14] P. Grace-Farfaglia, A. Dekkers, B. Sundararajan, L. Peters, S.-H. Park, Multinational web uses and grati<sup>fi</sup>cations: measuring the social impact of online community participation across national boundaries, Electronic Commerce Research 6 (1) (2006) 75–101.

[15] H. Haas and A. Brown, Web Services Glossary, Retrieved August 1, 2009, from W3C: http://www.w3.org/TR/ws-gloss

[16] HaavM.H. , A semi-automatic method to ontology design by using FCA, Proceedings of 2nd Concept Lattices and their Applications, Ostrava, Czech Republic, 2004, pp. 13–24.

[17] S.-L. Huang, Y.-H. Tsai, Developing a shopbot with multilingual ontology for global e-commerce, Journal of Internet Technology 10 (2) (2009) 111–118.

[18] M. Kim, Document Management and Retrieval for Specialised Domains: An Evolutionary User-based Approach, University of New South Wales, New South Wales, Australia, 2003.

[19] LinD. , An information-theoretic de<sup>fi</sup>nition of similarity, Proceedings of the 15th International Conference on Machine Learning, Madison, Wisconsin, USA, 1998, pp. 296–304.

[20] P.D. Lynch, J.C. Beck, Pro<sup>fi</sup>les of internet buyers in 20 countries: evidence for region-speci<sup>fi</sup>c strategies, Journal of International Business Studies 32 (4) (2001) 725–748.

[22] P. Maes, R.H. Guttman, A.G. Moukas, Agents that buy and sell, Communications of the ACM 42 (3) (1999) 81–91.

[21] A. Maedche, Ontology Learning for the Semantic Web, Kluwer Academic,Boston, 2002.

[23] F. Menczer, W.N. Street, A.E. Monge, Adaptive assistants for customized eshopping, IEEE Intelligent Systems 17 (6) (2002) 12–19

[24] A.L. Montgomery, K. Hosanagar, R. Krishnan, K.B. Clay, Designing a better shopbot, Management Science 50 (2) (2004) 189–206.

[25] R.M. O'Keefe, T. McEachern, Web-based customer decision support system, Communications of ACM 41 (3) (1998) 71–78.

[26] ResnikP. , Using Information content to evaluate semantic similarity in a taxonomy, Proceedings of the 14th International Joint Conference of Arti<sup>fi</sup>cial Intelligence, Montreal, Canada, 1995, pp. 448–453.

[27] StummeG. , MaedcheA. , FCA-MERGE: bottom-up merging of ontologies, Proceedings of the 17th International Conference on Arti<sup>fi</sup>cial Intelligence, Seattle, USA, 2001, pp. 225–230.

[28] Q.-T. Tho, S.-C. Hu, A. Fong, T.-H. Cao, Automatic fuzzy ontology generation for semantic web, IEEE Computer Society 18 (6) (2006) 842–856.

[29] J.C.R. Tseng, G.-J. Hwang, Development of an intelligent internet shopping agent based on a novel personalization approach, Journal of Internet Technology 6 (4) (2005) 477–485.

[30] TurbanE. , KingD. , McKayJ. , MarshallP. , LeeJ. , ViehlandD. , Electronic Commerce: A Managerial Perspective, 5 ed., Prentice Hall, New Jersey, 2008.

[31] S.-S. Weng, H.-J. Tsai, S.-C. Liu, C.-H. Hsu, Ontology construction for information classi<sup>fi</sup>cation, Expert Systems with Application 31 (1) (2006) 1–12.

[32] WilleR. , Restructuring lattice theory: an approach based on hierarchies of concepts, in: RivalI. (Ed.), Ordered Sets, Reidel, Dordrecht-Boston, 1982, pp. 455–470.

[33] WuZ. , PalmerM. , Verb semantics and lexical selection, Proceedings of the 32nd Annual Meeting of the Association for Computational Linguistics, Las Cruces, New Mexico, 1994, pp. 133–138.

Shiu-Li Huang received his Ph.D. degree in the Department of Management Information System from National Sun Yat-Sen University in 2005. He is an assistant professor at the Department of Information Management of Ming Chuan University, Taiwan. His papers have appeared in International Journal of Electronic Commerce, Electronic Commerce Research and Applications, Computers & Education, and several other journals. His research interests are intelligent agent, recommender systems, ecommerce, knowledge management, and e-learning.

Yu-Hsiang Tsai received his master's degree in the Department of Information Management from Ming Chuan University in 2009. His research has been published in Journal of Internet Technology. His research interests are intelligent agent, Web technology, and e-commerce.
