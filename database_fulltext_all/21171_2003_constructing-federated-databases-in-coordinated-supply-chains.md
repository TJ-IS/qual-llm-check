---
otero_id: 21171
otero_key: "2TYNT7T4"
title: "Constructing federated databases in coordinated supply chains"
authors: "Timon Chih-Ting Du; Hsun-Ming Lee; Ane Chen"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00131-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Constructing federated databases in coordinated supply chains

Timon Chih-Ting Du <sup>a,</sup>\*, Hsun-Ming Lee <sup>b</sup>, Ane Chen <sup>c</sup>

<sup>a</sup>Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Shatin, Hong Kong, China <sup>b</sup>Integrated Information System Corporation, USA

<sup>c</sup>Department of Industrial Engineering, Chung Yuan Christian University, Taiwan

Accepted 13 May 2002

## Abstract

Supply chain partnering is one approach in decreasing the risk of maintaining high inventories and improving due date requirements. Whether or not such partnerships run smoothly depends on the sharing of information, and successful information sharing is determined by the manner in which previously independent databases are coordinated. This study proposes the construction of attribute correspondence matrices (ACMs) for databases by extending the conventional schema coordination from peer-to-peer relationships into vertical relationships, i.e. supply chain relationships. Using ACMs, companies in the supply chain can share data with both upstream and downstream partners without leaking information to competitors. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Supply chain management; Federated databases; Attribute correspondence matrices

## 1. Introduction

In the past, enterprises were competitive when they provided the right quality of services or products to their customers on time. Business decisions, such as whether to buy parts or sell products, were based on push-type manufacturing rather than on customer-driven pull-type considerations. However, such companies can no longer be guaranteed of survival in dynamic environments in which end users are involved in the customization of products and functions. According to Shtub [14], in the future, dynamism in markets will lead to the increased development of decentralized, flexible structures that operate independently and with an awareness of decision-making and responsibility issues. Since becoming aware of such issues, enterprises have been moving towards the interorganizational coordination of their data and operations to shorten adaptation periods.

Companies have long studied coordinated supply chain relationships with the aim of providing products and services to end users at a low cost, and with high levels of service. The supply chain includes three major stages: procurement, production and distribution. To form a supply chain, a group of companies organize themselves into a chain of partners, and then work closely with one another as a virtual corporation. This is a temporary relationship that can involve independent companies, vendors and customers who want to work on projects together. Several database integration approaches have been proposed for multiorganizational environments. However, the integration of databases in coordinated supply chains faces several problems. The very act of integration is a tremendous task [13], and it takes a long time to translate numerous local schemas into a global conceptual schema [11]. Moreover, it is difficult to find a common intermediation with which to integrate heterogeneous databases [10]. The objective of this paper is to outline an innovative approach to the integration of databases in coordinated supply chains that allows each organization or company to effectively manage and share its own database.

Conventional coordinated supply chain research has focused on the development of analytic models for operational planning and strategic decision-making. Thomas defines three categories of operational coordination: buyer–vendor coordination, production – distribution coordination and inventory – distribution coordination [15]. Studies of buyer –vendor coordination have developed models that relate to the purchase of raw materials or parts from a single supplier [9] or many suppliers [1]. In contrast, production – distribution coordination emphasizes the integration of product manufacturing and distribution [7], whilst inventory – distribution coordination focuses on the efficiency of inventory levels to improve supply chain relationships [2,3]. Many operational models have been developed to address such crucial issues as the selection of batch sizes, the choice of transportation modes and the choice of production quantities. Strategic planning research considers plant or distribution center openings and closings, the allocation of equipment to manufacturing facilities, and the evaluation of changes in the flow of a particular product through the supply chain.

Some research projects have targeted information issues in supply chain environments. Fawcett [4] indicated that companies can produce additional services by obtaining information that is released into the supply chain. However, the supply chain generates a bullwhip effect, which causes a huge increase in inventory costs [5,16]. This effect is generated by: (1) demand forecasts updating in multiple levels; (2) forecasts of shortages in products; (3) order batching for economic reasons; and (4) price fluctuations [8]. Some studies have suggested the use of information technology, such as electronic data interchange systems or point of sale systems, to reduce this effect [6].

The use of information technology in coordinated supply chain networks creates intriguing research opportunities [12]. The integration of enterprises and their channels in electronic commerce raises questions, such as how to best organize data for efficient searching, how to develop efficient and effective tools for data mining and how to use the results of data mining in the manufacturing of products and the making of decisions.

Database integration is a crucial form of information technology for information searching and mining data in distributed environments. In particular, federated database management systems (FDMS) play significant roles in those companies that place selected business data in computer networks. Schema integration is a well-known approach to processing cooperative FDMS queries. However, it is difficult to maintain, and lacks flexibility and scalability [18]. Zhao et al. [17,19] has proposed an alternative, labeled schema coordination, for FDMS queries in multiorganizational environments.

Designing federated database management systems is similar to designing distributed databases. A distributed database has the advantages of local autonomy, improved performance, increased liability, better expansibility and information sharing. When designing a distributed database, either a top-down or a bottom-up approach can be used. As companies have their own databases before entering into the relationship, the bottom-up design of the distributed database is a better approach for integrating databases among companies. Moreover, in this approach the schema coordination strategy is better than the schema integration strategy for supply chain partners due to logical data independence and extensibility [11].

In schema coordination, each component database shares its logical data structure through export schemas (which will be discussed later). In addition, federated metadata is built on an attribute correspondence matrix (ACM), which is a flat table containing federated attributes and their mappings to all component attributes. When constructing ACM tables in coordinated supply chain networks, it might not be practical to establish a federated attribute agreement among members of a layered supply chain federation. Moreover, it might not be appropriate for each participant to access all component attributes, as suppliers of the same product can be competitors and should not expose their schema attributes to one another.

The schema coordination approach, which we propose as a way of constructing federated databases, provides the advantages of maintenance, flexibility, and the scalability of data. Coordinated supply chains represent complex relationships in which the establishment of a universal table con taining all federated attributes is difficult. Therefore, we propose a mechanism developed for the ACM from its lower-level nodes (buyers). We develop an algorithm, labeled ACM\_Partial, to design an ACM table for each company. In addition, an accessory attribute list prevents the data from being revealed to competitors through upper-level companies. Local queries are then transformed to search the information in the networks. Finally, we demonstrate the scalability of the approach insofar as adding a new node or removing an existing node from the supply chain does not significantly change the ACMs. Two types of queries are used for demonstration purposes.

## 2. Implementing a federated database in a supply chain

The federated database is developed by multiple layered schema coordination in a bottom-up design according to five steps: (1) the collection and transformation of export schemas; (2) the determination of federated attributes; (3) the construction of ACMs; (4) query transformation; and (5) the addition and removal of nodes. To illustrate this process, the definitions of the notations used in node $L _ { i j } ,$ which is a company in the supply chain partnership, are:

$F _ { i j } \mathrm { : }$ the ACM table for the jth node in level i; $A _ { i j } \mathrm { : }$ the accessory attribute list of the jth node in level i;

$C _ { i j } \mathrm { : }$ the set of nodes connected to $L _ { i j }$ in level $i - 1 ;$ $d _ { i j } .$ the set of local database attributes in the export schema; and

$f _ { i j } { \mathrm { : } }$ the set of federated attributes in ACM table $F _ { i j } .$

## 2.1. Collection and transformation of the export schema

In a coordinated supply chain network with m levels numbered from 1 to m (Fig. 1), level 1 is defined as the bottom level, e.g. the product retailer level. Each level consists of nodes that represent similar supply chain companies with local databases. An edge that connects the nodes at two levels indicates a vendor–buyer relationship that requires database integration. The nodes in level i are numbered from 1 to $m ( i ) ;$ and $L _ { i j }$ denotes the jth company in level i. Each export schema is in a table format with three columns that contain: (1) attribute names as they appear in the local database; (2) attribute types, such as key, nonkey and foreign key; and (3) attribute pointers that represent the logical database structure. A nonkey attribute must point to its key attribute, and a key attribute must point to its foreign keys, assuming that it has any.

A case study, as shown in Table 1, illustrates export schemas with two retailers (R1 and R2), two warehouses (W1 and W2) and two manufacturers (M1 and M2).

## 2.2. Determining federated attributes

To construct the supply chain FDMS using the schema coordination approach, the export schemas of the local databases are placed in their corresponding nodes (companies). The federated attributes $f _ { i j }$ are the union of local export schemas that will be used to form an ACM, and they provide a list of attributes for access by supply chain nodes. As this is a bottom-up design, it

![](/api/attachments/2TYNT7T4/fulltext/images/52370c1ba79aaaf49ae29b03b6a299d3cd189bb6c99e019f51a026c0f6693a7c.jpg)  
Fig. 1. Supply chain network with m levels.

Table 1  
Export schemas of Fig. 3

<table><tr><td colspan="3">(a) Retailer R1 export schema</td></tr><tr><td>R1.attribute</td><td>R1.type</td><td>R1.pointer</td></tr><tr><td>Sale.SaleNo</td><td>Key</td><td>Sale.Storage</td></tr><tr><td>Sale.SaleDate</td><td>Nonkey</td><td>Sale.SaleNo</td></tr><tr><td>Sale.Amount</td><td>Nonkey</td><td>Sale.SaleNo</td></tr><tr><td>Sale.Storage</td><td>Foreign key</td><td>Storage.ProductNum</td></tr><tr><td>Storage.ProductNum</td><td>Key</td><td></td></tr><tr><td>Storage.Name</td><td>Nonkey</td><td>Storage.ProductNum</td></tr><tr><td>Storage.Location</td><td>Nonkey</td><td>Storage.ProductNum</td></tr><tr><td>Storage.Amount</td><td>Nonkey</td><td>Storage.ProductNum</td></tr><tr><td>Storage.Price</td><td>Nonkey</td><td>Storage.ProductNum</td></tr></table>

(b) Retailer R2 export schema

<table><tr><td>R2.attribute</td><td>R2.type</td><td>R2.pointer</td></tr><tr><td>Sale.RecordNo</td><td>Key</td><td>Sale.Goods</td></tr><tr><td>Sale.Amount</td><td>Nonkey</td><td>Sale.RecordNo</td></tr><tr><td>Sale.Goods</td><td>Foreign key</td><td>Goods.Gno</td></tr><tr><td>Goods.Gno</td><td>Key</td><td>Goods.Gno</td></tr><tr><td>Goods.Name</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Goods.Type</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Goods.Price</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Stock.Sno</td><td>Key</td><td>Stock.Goods</td></tr><tr><td>Stock.Sdate</td><td>Nonkey</td><td>Stock.Sno</td></tr><tr><td>Stock.Loc</td><td>Nonkey</td><td>Stock.Sno</td></tr><tr><td>Stock.Quantity</td><td>Nonkey</td><td>Stock.Sno</td></tr><tr><td>Stock.Goods</td><td>Foreign key</td><td>Goods.Gno</td></tr></table>

(c) Warehouse W1 export schema

<table><tr><td>W1.attribute</td><td>W1.type</td><td>W1.pointer</td></tr><tr><td>Parts.PartNo</td><td>Key</td><td></td></tr><tr><td>Parts.Name</td><td>Nonkey</td><td>Parts.PartNo</td></tr><tr><td>Parts.Category</td><td>Nonkey</td><td>Parts.PartNo</td></tr><tr><td>Parts.Price</td><td>Nonkey</td><td>Parts.PartNo</td></tr><tr><td>Order.OrderNo</td><td>Key</td><td>Order.PartNo</td></tr><tr><td>Order.OrderDate</td><td>Nonkey</td><td>Order.OrderNo</td></tr><tr><td>Order.Quantity</td><td>Nonkey</td><td>Order.OrderNo</td></tr><tr><td>Order.PartNo</td><td>Foreign key</td><td>Parts.PartNo</td></tr></table>

(d) Warehouse W2 export schema

<table><tr><td>W2.attribute</td><td>W2.type</td><td>W2.pointer</td></tr><tr><td>Manufacturer.ManuNo</td><td>Key</td><td></td></tr><tr><td>Manufacturer.Name</td><td>Nonkey</td><td>Manufacturer.ManuNo</td></tr><tr><td>Manufacturer.Phone</td><td>Nonkey</td><td>Manufacturer.ManuNo</td></tr><tr><td>Manufacturer.Address</td><td>Nonkey</td><td>Manufacturer.ManuNo</td></tr><tr><td>Product.ItemNo</td><td>Key</td><td></td></tr><tr><td>Product.Description</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Product.Price</td><td>Nonkey</td><td>Stock.Goods</td></tr><tr><td>Stock.Num</td><td>Key</td><td>Stock.Product</td></tr><tr><td></td><td></td><td>Stock.Manufacturer</td></tr><tr><td>Stock.Amount</td><td>Nonkey</td><td>Stock.Num</td></tr></table>

Table 1 (continued )

<table><tr><td colspan="3">(d) Warehouse W2 export schema</td></tr><tr><td>W2.attribute</td><td>W2.type</td><td>W2.pointer</td></tr><tr><td>Stock.Product</td><td>Foreign key</td><td>Product.ItemNo</td></tr><tr><td>Stock.Manufacturer</td><td>Foreign key</td><td>Manufacturer.ManuNo</td></tr></table>

(e) Manufacturer M1 export schema

<table><tr><td>M1.attribute</td><td>M1.type</td><td>M1.pointer</td></tr><tr><td>Warehouse.Wnum</td><td>Key</td><td></td></tr><tr><td>Warehouse.Address</td><td>Nonkey</td><td>Warehouse.Wnum</td></tr><tr><td>Warehouse.Manager</td><td>Nonkey</td><td>Warehouse.Wnum</td></tr><tr><td>Product.Pnum</td><td>Key</td><td></td></tr><tr><td>Product.Type</td><td>Nonkey</td><td>Product.Pnum</td></tr><tr><td>Product.Pnum</td><td>Nonkey</td><td>Product.Pnum</td></tr><tr><td>Product.Info</td><td>Nonkey</td><td>Product.Pnum</td></tr><tr><td>Material.Mno</td><td>Key</td><td></td></tr><tr><td>Material.Mname</td><td>Nonkey</td><td>Material.Mno</td></tr><tr><td>Material.County</td><td>Nonkey</td><td>Material.Mno</td></tr><tr><td>Work.WorkNo</td><td>Key</td><td>Work.ProductWork.MaterialWork.Warehouse</td></tr><tr><td>Work.Quantity</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Work.Product</td><td>Foreign key</td><td>Product.Pnum</td></tr><tr><td>Work.Material</td><td>Foreign key</td><td>Material.Mno</td></tr><tr><td>Work.Warehouse</td><td>Foreign key</td><td>Warehouse.Wnum</td></tr></table>

(f) Manufacturer M2 export schema

<table><tr><td>M2.attribute</td><td>M2.type</td><td>M2.pointer</td></tr><tr><td>Raw.Rnum</td><td>Key</td><td></td></tr><tr><td>Raw.Cost</td><td>Nonkey</td><td>Raw.Rnum</td></tr><tr><td>Raw.Name</td><td>Nonkey</td><td>Raw.Rnum</td></tr><tr><td>Raw.Place</td><td>Nonkey</td><td>Raw.Rnum</td></tr><tr><td>Process.Pno</td><td>Key</td><td>Process.RawProcess.Goods</td></tr><tr><td>Process.Raw</td><td>Foreign key</td><td>Raw.Rnum</td></tr><tr><td>Process.Goods</td><td>Foreign key</td><td>Goods.Gno</td></tr><tr><td>Goods.Gno</td><td>Key</td><td></td></tr><tr><td>Goods.Name</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Goods.Price</td><td>Nonkey</td><td>Goods.Gno</td></tr><tr><td>Wholesaler.Wno</td><td>Key</td><td></td></tr><tr><td>Wholesaler.Name</td><td>Nonkey</td><td>Wholesaler.Wno</td></tr><tr><td>Wholesaler.City</td><td>Nonkey</td><td>Wholesaler.Wno</td></tr><tr><td>Wholesaler.Tel</td><td>Nonkey</td><td>Wholesaler.Wno</td></tr><tr><td>Shipment.Sno+</td><td>Key</td><td>Shipment.GoodsShipment.Wholesaler</td></tr><tr><td>Shipment.Sdate</td><td>Nonkey</td><td>Shipment.Sno</td></tr><tr><td>Shipment.Goods</td><td>Foreign key</td><td>Goods.Gno</td></tr><tr><td>Shipment.Wholesaler</td><td>Foreign key</td><td>Wholesaler.Wno</td></tr></table>

draws together the local export schemas and the lower level export schemas. That is, each company in the supply chain has a local database and an ACM. The first column of each ACM contains the federated attributes, the second column contains the local export schema and the third and later columns are the export schemas of lower-level nodes. Note that the same attributes of different local databases (which may have different attribute names) are placed in the same row, and federated attribute names are assigned to represent them.

## 2.3. Constructing ACMs

Assuming that all of the export schemas of the local databases are available, ACMs can be constructed accordingly. It should be noted that all of the attributes of these local databases might not be acquired at the time of constructing the ACMs. Therefore, the ACM design must maintain certain degree of flexibility for future expansion or shrinkage. Moreover, in the supply chain environment the design of an ACM must ensure that no company can access the databases of its competitors (i.e. the nodes in the same level). We, thus, propose an algorithm for the construction of ACMs based on partial network information. Similarly, we develop a query transformation procedure to query ACMs in the partial networks. In the algorithm, the ACM not only has federated attributes, but also includes a list of accessory attributes to prevent data being accessed by competitors.

Corresponding to Fig. 1, the algorithm ACM<sup>\_</sup> PARTIAL (see Fig. 2) creates both the ACM and the accessory attribute list for each node in the coordinated supply chain network. The algorithm allows node $L _ { i j }$ to have: (a) an ACM table with attributes in levels lower than i; and (b) an accessory attribute list. As the ACM includes the information (federated attributes) of the lower-level nodes (databases), the federated query can be decomposed and sent those nodes to retrieve the requested information.

Each node generates an ACM table with the following characteristics.

(1) Federated attributes in the first column, which represent the attributes with a common semantic in different databases.

(2) Local attributes in the second column, which are the database attributes exported by the node itself.

(3) Connected attributes, starting from the third column, which come from the connected nodes in the lower levels. Each column represents a connected node and the federated attributes of that node’s ACM table. As there are no federated attributes and ACM tables in the first level nodes (the lowest level), the construction of the ACM starts from the second level.

(4) Access path attributes, which are designed to direct information searches from one database to another. A federated attribute can be assigned as an access path attribute if its local attribute and connected attributes are either (a) keys of the export schemas, or (b) access path attributes of the connected ACM. For example, in the ACM table of warehouse W1 (see Table 2), a federated attribute Part Number is chosen as the access path attribute because the local attribute Part.PartNo is the key attribute of W1, and the connected attributes Storage.ProductNum and Goods.Gno are the key values of connected export schemas R1 and R2, respectively.

(5) Accessory attributes, which are created by the second part of the ACM\_PARTIAL algorithm, and are used to limit the query scope when a query is passed from the lower level. For example, the accessory attributes of manufacturer M1 are Sale Product Number, Sale Product Name, Sale Product category, Warehouse Order Number and so on. A query can only access these attributes when it is issued from the lower-level nodes, i.e. W1 and W2.

The computing time for the ACM\_PARTIAL algorithm is ${ \mathrm { O } } ( n ^ { 2 } m )$ , where n is the number of companies in a level, and m is the number of levels of a supply chain partnership. The ACM table of nodes is created according to the proposed algorithm. After generating the ACM table in a node, the federated attributes are passed from the lower-level node to higher-level connected nodes. In each node, the ACM is the only extra table needed for the sharing of data among partners. After designing the ACM, the query can be executed. According to Ozsu and Valduriez [11], the communication cost is a dominant factor compared with the CPU instructions and disk I/O time taken to execute queries on the Internet. The communication time (CT) of transferring k bytes of queries in the supply chain is $C T _ { i } { ^ { * } } _ { m } ( k ) { = } i { ^ { * } m } { ^ { * } } C T ( k )$ , where i is the number of nodes connected to the queried node and m is the number of levels in the supply chain. The proposed framework is significantly different to the design of a distributed database. In a distributed database, fragments (portions of tables) can be duplicated in related nodes. If the fragments are not duplicated, then the discretionary access control is complex, and the communication cost is high. However, if the fragments are duplicated, then the costs of data space and maintenance for the duplicated copies are tremendous, although the search cost might be low. In such a case, the security mechanism regarding data replication is an important issue.

## 2.4. Query transformation

In the supply chain, each company maintains both a local database and an ACM. Zhao’s [18] algorithm can be adapted to implement an iterative query transformation algorithm in coordinated supply chains. The algorithm uses four steps to decompose a federated query into subqueries, and sends them to component databases for processing (which will be discussed later). Note that the query direction relates to the ACM construction direction. For example, if the ACMs are constructed from lower-level nodes to upper-level nodes, then the query will be passed upward when the specified attributes cannot be found in a node. Similarly, if the ACMs are constructed from upper-level nodes to lower-level nodes, then the query can be passed downward when the specified

```txt
Algorithm ACM_Partial
Input: A coordinated supply chain network with m levels.
Output: the ACMs for the network nodes.
BEGIN
//PART I: constructing ACM
    Fij and Cij are empty; //Initialization
    Set f1j = d1j for j = 1 to n(1); //bottom-up approach; start from the lowest level 1
    For each level i = 2 to m in the network
    For each node Lij, j = 1 to n(i), in the level i
    For each node Li-1, k, k = 1 to n(i-1) in the level i-1
    Find Cij, the set of nodes connecting to Lij in the level i-1;
    Endfor
    Create Fij from dij and all fi-1, k's in Cij;
    Endfor
Endfor
//PART II: determine access path attributes of Fij;
    Aij and Cij are empty; //Initialization
    Set Amj = fmj for j = 1 to n(m); //start from the highest level m
    For each level i = m to 2 in the network
    For each node Lij, j = 1 to n(i), in the level i
    Aij = the intersection of dij and fij;
    Endfor
Endfor
END
```  
Fig. 2. Algorithm to create the ACMs in the supply chain.

![](/api/attachments/2TYNT7T4/fulltext/images/f27134fdd028b8e07858ff3d7afc8765e43ac7d204df912c25c17755d11ec414.jpg)  
Fig. 2 (continued ).

attributes cannot be found in the queried node. That is, if the query attributes cannot be found in the query node $L _ { i j } ,$ then the query is passed to upper-level nodes, say $L _ { i + 1 , j } ,$ if node $L _ { i + 1 , j }$ is connected to $L _ { i j } .$ This is because node $L _ { i j }$ has attributes in the federated attributes of its ACM. However, the upper-level nodes may contain the information of a competitor node, which is located in the same level as $L _ { i j } ,$ say $L _ { i , j + 1 }$ . If we allow the query being executed to pass through upper-level nodes toward the lower-level nodes, then $L _ { i j }$ can query the data of $L _ { i , j + 1 }$ through

$L _ { i + 1 , j } ,$ and the data security of $L _ { i + 1 , j }$ cannot be maintained. This is why an accessory attribute list is provided. The accessory attribute list is obtained by intersecting federated attributes and local export schemas (for example, the attribute Part Number of warehouse W in Table 2 is an accessory attribute, which is obtained by intersecting the federated attributes of W1 and its export schema, as shown in Table 1.) When a query is passed upwards, the query can only be mapped into the accessory attributes of upper-level nodes rather than complete federated attributes. For example, in Fig. 1, if a query cannot find an attribute from the federated attributes in $F _ { i j } ,$ then it is passed upwards to $L _ { i + 1 , 1 } , L _ { i + 1 , 2 }$ , and other connected nodes. If the query attribute still cannot be found at this level, then the query is passed to an even higher level, say $L _ { i + 2 , j } .$ . Note that when a query is passed from the lower-level node $L _ { i , j }$ to upper-level nodes, it can only access the accessory attribute list of their ACMs. This design prohibits the query of $L _ { i , j }$ from accessing $L _ { i , j + 1 }$ through to $L _ { i + 1 , j } ,$ and accessing $L _ { i + 1 , j + 1 }$ from $L _ { i + 2 , j } ,$ even though they are connected.

Table 2  
ACM table of the example in Fig. 3

<table><tr><td>Fed attribute</td><td>W1</td><td>R1</td><td>R2</td></tr><tr><td>Sale Number</td><td></td><td>Sale.SaleNo</td><td>Sale.RecordNo</td></tr><tr><td>Sale Date</td><td></td><td>Sale.SaleDate</td><td></td></tr><tr><td>Sale Amount</td><td></td><td>Sale.Amount</td><td>Sale.Amount</td></tr><tr><td>Sale Part</td><td></td><td>Sale.Storage</td><td>Sale.Goods</td></tr><tr><td>Part Numbera,b</td><td>Part.PartNo</td><td>Storage.ProductNum</td><td>Goods.Gno</td></tr><tr><td>Part Nameb</td><td>Part.Name</td><td>Storage.Name</td><td>Goods.Name</td></tr><tr><td>Part Categoryb</td><td>Part.Category</td><td></td><td>Goods.Type</td></tr><tr><td>Part Stock Location</td><td></td><td>Storage.Location</td><td>Stock.Location</td></tr><tr><td>Part Stock Quantity</td><td></td><td>Storage.Amount</td><td>Stock.Quantity</td></tr><tr><td>Part Sale Price</td><td></td><td>Storage.Price</td><td>Goods.Price</td></tr><tr><td>Part Stock Priceb</td><td>Part.Price</td><td></td><td></td></tr><tr><td>Part Stock Date</td><td></td><td></td><td>Stock.Sdate</td></tr><tr><td>Part Stock Number</td><td></td><td></td><td>Stock.Sno</td></tr><tr><td>Part Stock</td><td></td><td></td><td>Stock.Goods</td></tr><tr><td>Order Numberb</td><td>Order.OrderNo</td><td></td><td></td></tr><tr><td>Order Dateb</td><td>Order.OrderDate</td><td></td><td></td></tr><tr><td>Order Quantityb</td><td>Order.Quantity</td><td></td><td></td></tr><tr><td>Order Partb</td><td>Order.PartNo</td><td></td><td></td></tr></table>

(b) ACM table of warehouse W2

<table><tr><td>Fed attribute</td><td>W2</td><td>R1</td><td>R2</td></tr><tr><td>Sale Number</td><td></td><td>Sale.SaleNo</td><td>Sale.RecordNo</td></tr><tr><td>Sale Date</td><td></td><td>Sale.SaleDate</td><td></td></tr><tr><td>Sale Amount</td><td></td><td>Sale.Amount</td><td>Sale.Amount</td></tr><tr><td>Sale Product</td><td></td><td>Sale.Storage</td><td>Sale.Goods</td></tr><tr><td>Sale Product  $Number^{a,b}$ </td><td>Product.ItemNo</td><td>Storage.ProductNum</td><td>Goods.Gno</td></tr><tr><td>Sale Product  $Name^b$ </td><td>Product.Description</td><td>Storage.Name</td><td>Goods.Name</td></tr><tr><td>Sale Product Category</td><td></td><td></td><td>Goods.Type</td></tr><tr><td>Product Stock Location</td><td></td><td>Storage.Location</td><td>Stock.Location</td></tr><tr><td>Product Stock Quantity</td><td></td><td>Storage.Amount</td><td>Stock.Quantity</td></tr><tr><td>Product Sale Price</td><td></td><td>Storage.Price</td><td>Goods.Price</td></tr><tr><td>Product Stock Date</td><td></td><td></td><td>Stock.Sdate</td></tr><tr><td>Product Stock Number</td><td></td><td></td><td>Stock.Sno</td></tr><tr><td>Product Stock</td><td></td><td></td><td>Stock.Goods</td></tr><tr><td> $Product\ Stock\ Price^b$ </td><td>Product.Price</td><td></td><td></td></tr><tr><td> $Warehouse\ Stock\ Number^b$ </td><td>StockNum</td><td></td><td></td></tr><tr><td> $Warehouse\ Stock\ Product^b$ </td><td>Stock.Product</td><td></td><td></td></tr><tr><td> $Warehouse\ Stock\ Manufacturer^b$ </td><td>Stock.Manufacturer</td><td></td><td></td></tr><tr><td> $Manufacturer\ Number^b$ </td><td>Manufacturer.ManuNo</td><td></td><td></td></tr><tr><td> $Manufacturer\ Name^b$ </td><td>Manufacturer.Name</td><td></td><td></td></tr><tr><td> $Manufacturer\ Phone^b$ </td><td>Manufacturer.Phone</td><td></td><td></td></tr><tr><td> $Manufacturer\ Address^b$ </td><td>Manufacturer.Address</td><td></td><td></td></tr></table>

(c) ACM table of manufacturer Ml

<table><tr><td>Fed attribute</td><td>M1</td><td>ACM of W1</td><td>ACM of W2</td></tr><tr><td>Sale Number</td><td></td><td>Sale Number</td><td>Sale Number</td></tr><tr><td>Sale Date</td><td></td><td>Sale Date</td><td>Sale Date</td></tr><tr><td>Sale Amount</td><td></td><td>Sale Amount</td><td>Sale Amount</td></tr><tr><td>Sale Product</td><td></td><td>Sale Part</td><td>Sale Product</td></tr><tr><td>Sale Product Numbera,b</td><td>Product.Pnum</td><td>Part Number</td><td>Sale Product Number</td></tr></table>

Table 2 (continued )

<table><tr><td colspan="4">(c) ACM table of manufacturer M1</td></tr><tr><td>Fed attribute</td><td>M1</td><td>ACM of W1</td><td>ACM of W2</td></tr><tr><td>Sale Product Name $^{b}$ </td><td>Product.Info</td><td>Part Name</td><td>Sale Product Name</td></tr><tr><td>Sale Product Category $^{b}$ </td><td>Product.type</td><td>Part Category</td><td>Sale Product Category</td></tr><tr><td>Product Stock Location</td><td></td><td>Part Stock Location</td><td>Product Stock Location</td></tr><tr><td>Product Stock Quantity</td><td></td><td>Part Stock Quantity</td><td>Product Stock Quantity</td></tr><tr><td>Product Sale Price</td><td></td><td>Part Sale Price</td><td>Product Sale Price</td></tr><tr><td>Product Stock Date</td><td></td><td>Part Stock Date</td><td>Product Stock Date</td></tr><tr><td>Product Stock Number</td><td></td><td>Part Stock Number</td><td>Product Stock Number</td></tr><tr><td>Product Stock $^{b}$ </td><td></td><td>Part Stock</td><td>Product Stock</td></tr><tr><td>Product Stock Price</td><td></td><td>Part Stock Price</td><td>Product Stock Price</td></tr><tr><td>Warehouse Order Number $^{a,b}$ </td><td>Work.WorkNo</td><td>Order Number</td><td>Warehouse Stock Number</td></tr><tr><td>Warehouse Order Amount $^{b}$ </td><td>Work.Quantity</td><td>Order Quantity</td><td>Warehouse Stock Amount</td></tr><tr><td>Warehouse Order Product $^{b}$ </td><td>Work.Product</td><td>Order Part</td><td>Warehouse Stock Product</td></tr><tr><td>Warehouse Order Date</td><td></td><td>Order Date</td><td></td></tr><tr><td>Warehouse Order Manufacturer</td><td></td><td></td><td>Warehouse Stock Manufacturer</td></tr><tr><td>Order Production Material $^{b}$ </td><td>Work.Material</td><td></td><td></td></tr><tr><td>Order Warehouse $^{b}$ </td><td>Work.Warehouse</td><td></td><td></td></tr><tr><td>Product Order Price $^{b}$ </td><td>Product.Price</td><td></td><td></td></tr><tr><td>Manufacturer Number</td><td></td><td></td><td>Manufacturer.ManuNo</td></tr><tr><td>Manufacturer Name</td><td></td><td></td><td>Manufacturer.Name</td></tr><tr><td>Manufacturer Phone</td><td></td><td></td><td>Manufacturer.Phone</td></tr><tr><td>Manufacturer Address</td><td></td><td></td><td>Manufacturer.Address</td></tr><tr><td>Material Number $^{b}$ </td><td>Material.Mno</td><td></td><td></td></tr><tr><td>Material Name $^{b}$ </td><td>Material.Name</td><td></td><td></td></tr><tr><td>Material Country $^{b}$ </td><td>Material.Country</td><td></td><td></td></tr><tr><td>Warehouse Number $^{b}$ </td><td>Warehouse.Wnum</td><td></td><td></td></tr><tr><td>Warehouse Address $^{b}$ </td><td>Warehouse.Address</td><td></td><td></td></tr><tr><td>Warehouse Manager $^{b}$ </td><td>Warehouse.Manager</td><td></td><td></td></tr></table>

(d) ACM table of manufacturer M2

<table><tr><td>Fed attribute</td><td>M2</td><td>ACM of W1</td><td>ACM of W2</td></tr><tr><td>Sale Number</td><td></td><td>Sale Number</td><td>Sale Number</td></tr><tr><td>Sale Date</td><td></td><td>Sale Date</td><td>Sale Date</td></tr><tr><td>Sale Amount</td><td></td><td>Sale Amount</td><td>Sale Amount</td></tr><tr><td>Sale Product</td><td></td><td>Sale Part</td><td>Sale Product</td></tr><tr><td>Sale Product  $Number^{a,b}$ </td><td>Goods.Gno</td><td>Part Number</td><td>Sale Product Number</td></tr><tr><td>Sale Product  $Name^b$ </td><td>Goods.Name</td><td>Part Name</td><td>Sale Product Name</td></tr><tr><td>Sale Product Category</td><td></td><td>Part Category</td><td>Sale Product Category</td></tr><tr><td>Product Stock Location</td><td></td><td>Part Stock Location</td><td>Product Stock Location</td></tr><tr><td>Product Stock Quantity</td><td></td><td>Part Stock Quantity</td><td>Product Stock Quantity</td></tr><tr><td>Product Sale Price</td><td></td><td>Part Sale Price</td><td>Product Sale Price</td></tr><tr><td>Product Stock Date</td><td></td><td>Part Stock Date</td><td>Product Stock Date</td></tr><tr><td>Product Stock Number</td><td></td><td>Part Stock Number</td><td>Product Stock Number</td></tr><tr><td>Product Stock</td><td></td><td>Part Stock</td><td>Product Stock</td></tr><tr><td>Product Stock Price</td><td></td><td>Part Stock Price</td><td>Product Stock Price</td></tr><tr><td>Wholesaler Order  $Number^{a,b}$ </td><td>Shipment.Sno</td><td>Order Number</td><td>Warehouse Stock Number</td></tr><tr><td>Wholesaler Order Amount</td><td></td><td>Order Quantity</td><td>Warehouse Stock Amount</td></tr><tr><td>Wholesaler Order  $Product^b$ </td><td>Shipment.Goods</td><td>Order Part</td><td>Warehouse Stock Product</td></tr><tr><td>Wholesaler Order  $Date^b$ </td><td>Shipment.Sdate</td><td>Order Date</td><td></td></tr><tr><td>Wholesaler Order Manufacturer</td><td></td><td></td><td>Warehouse Stock Manufacturer</td></tr><tr><td>Order  $wholesaler^b$ </td><td>Shipment.Wholesaler</td><td></td><td></td></tr><tr><td>Product Manufacturing  $Price^b$ </td><td>Goods.Price</td><td></td><td></td></tr></table>

Table 2 (continued )

<table><tr><td colspan="4">(d) ACM table of manufacturer M2</td></tr><tr><td>Fed attribute</td><td>M2</td><td>ACM of W1</td><td>ACM of W2</td></tr><tr><td>Process Number $^b$ </td><td>Process.Pno</td><td></td><td></td></tr><tr><td>Process Raw Material $^b$ </td><td>Process.Raw</td><td></td><td></td></tr><tr><td>Process Product $^b$ </td><td>Process.Goods</td><td></td><td></td></tr><tr><td>Raw Material Number $^b$ </td><td>Raw.Rnum</td><td></td><td></td></tr><tr><td>Raw Material Name $^b$ </td><td>Raw.Name</td><td></td><td></td></tr><tr><td>Raw Material Place $^b$ </td><td>Raw.Place</td><td></td><td></td></tr><tr><td>Raw Material Cost $^b$ </td><td>Raw.Cost</td><td></td><td></td></tr><tr><td>Wholesaler Number $^b$ </td><td>Wholesaler.Who</td><td></td><td></td></tr><tr><td>Wholesaler Name $^b$ </td><td>Wholesaler.Name</td><td></td><td></td></tr><tr><td>Wholesaler City $^b$ </td><td>Wholesaler.City</td><td></td><td></td></tr><tr><td>Wholesaler Telephone $^b$ </td><td>Wholesaler.Tel</td><td></td><td></td></tr><tr><td>Manufacturer Number</td><td></td><td></td><td>Manufacturer.ManuNo</td></tr><tr><td>Manufacturer Name</td><td></td><td></td><td>Manufacture.Name</td></tr><tr><td>Manufacturer Phone</td><td></td><td></td><td>Manufacturer.Phone</td></tr></table>

<sup>a</sup> Access path attribute.  
<sup>b</sup> Accessory attribute.

## 2.5. Adding or removing nodes

A coordinated supply chain relationship should allow a dynamic partnership, in which a partner can join or leave the supply chain when needed. Therefore, the database design must be expandable. In a supply chain network, a node can be added to the top level, the bottom level, or middle level. However, the addition of a node will only affect those nodes that are located at upper levels, as the design is from the bottom level to the top level. For example, if node $L _ { 1 , j + 1 }$ is added to the bottom level, then the export schema will be passed to the nodes at $L _ { 2 , }$ to form the federated attributes and ACMs. The federated attributes will be further propagated to higher-level nodes to restructure the ACMS. However, if a node is added to the middle level, then the connected lower-level nodes must pass their federated attributes to it, and the federated attributes in the ACM of the newly added node will be passed to the higherlevel nodes. If a node is added to the top level, then only the connected lower-level nodes need to surrender their federated attributes, and an ACM is formed accordingly. The procedure for removing a node is similar to the procedure for adding a node.

## 3. Case study

Fig. 3 shows the database schemas of the local databases in a three-level supply chain network that is composed of two manufacturers (M1 and M2), two wholesalers (W1 and W2), and two retailers (R1 and R2). The manufacturers are connected to the wholesalers, and the wholesalers are connected to the retailers, but there is no direct link between the manufacturers and the retailers. Moreover, companies of the same level are assumed to be competitors and cannot mutually access data, e.g. retailer R1 cannot access the database of retailer R2. The export schemas are shown in Table 1, and their corresponding ACMs are shown in Table 2. It should be noted that based on the ACM<sup>\_</sup> PARTIAL algorithm, retailers R1 and R2 do not maintain ACMs, as they are the nodes at the lowest level.

Companies in the coordinated supply chain network can issue federated queries based on their own ACMs. The federated query is an extended SQL that allows the specification of target databases in the FROM clause:

![](/api/attachments/2TYNT7T4/fulltext/images/17107b9a33c1dd788904d20ea523fe037c848d6a1be202d5fc1ad2936ba2ed95.jpg)  
Fig. 3. Example of a supply chain network.

SELECT federated attributes

FROM databases

WHERE selection and interdatabase join conditions

The federated query is then transformed into subqueries of local databases by a query transformation procedure (which is discussed below).

As the ACMs are constructed directionally from the lowest level to the highest level, the federated queries that are issued to a node can be passed to either lowerlevel nodes or both lower-and upper-level nodes. Two query examples will be used to illustrate the operation: Query A queries the lower-level nodes and Query B queries both the higher-and lower-level nodes.

Query A: manufacturer M1 wants to ascertain which products are ordered by its warehouses and sold by the retailers at prices of more than US\$100, and this query can be written, with the federated attributes in square brackets, as:

SELECT [Sale Product Number], [Sale Product Name], [Product Sale Price], [Warehouse Number] FROM M1, W1, W2 WHERE M1.[Warehouse Order Number]=(W1, W2).[Warehouse Order Number] AND (W1, W2).[Product Sale Price]>100

Four steps are used to transform the federated query into subqueries that will be sent to connected databases, namely: query split, attribute conversion, join specification, and source object identification.

(1) Query split. Divide the federated query into subqueries that will be sent to local databases. For example, the query sent to node M1 can be divided into the query sent to (M1, W1) and the query sent to (M1, W2). The subquery involving M1 and W1 is:

DATABASE M1, W1 SELECT [Sale Product Number], [Sale Product Name], [Product Sale Price], [Warehouse Number] FROM WHERE M1.[Warehouse Order Number]=W1. [Warehouse Order Number] AND W1.[Product Sale Price]>100

(2) Attribute conversion. Convert the federated attributes into local attributes according to the ACM.

DATABASE M1, W1 SELECT M1.Product.Pnum, M1.Product.Info, W1.[Part Sale Price], M1.Warehouse.Wnum FROM WHERE M1.Work.WorkNo=W1.[Order Number] AND W1.[Part Sale Price]>100

(3) Join specification. Determine the reference integrity constraints between the foreign key and the primary key that are needed to access the attributes in the SELECT clause. The join conditions are identified as follows:

DATABASE M1, W1

SELECT M1.Product.Pnum, M1.Product.Info, W1.[Part Sale Price], M1.Warehouse.Wnum FROM

WHERE M1.Work.WorkNo=W1.[Order Number] AND M1.Work.Product =M1.Product.Pnum AND M1.Work.Warehouse =M1.Warehouse.Wnum AND W1.[Part Sale Price]>100

(4) Source object identification. Extract the relation names from the local attributes that are found in the SELECT and WHERE clauses, and place them in the FROM clauses.

DATABASE M1, W1

SELECT M1.Product.Pnum, M1.Product.Info, W1.[Part Sale Price], M1.Warehouse.Wnum FROM M1.Product, M1.Warehouse, M1.Work WHERE M1.Work.WorkNo=W1.[Order Number] AND M1.Work.Product =M1.Product.Pnum AND M1.Work.Warehouse =M1.Warehouse.Wnum AND W1.[Part Sale Price]>100

This query transformation must check whether or not all attributes have been converted into local attributes. If the final subquery that is derived from the fourth step includes federated attributes, then the next iteration is triggered, i.e. the query is passed to further lower-level nodes. In contrast, the transformation process is terminated when no federated attributes are involved in the subqueries. The subquery sent to node W1 [Part Number] includes the attribute of the access path between W1 and R1. Again, the algorithm checks whether or not the transformation is finished, and stops when level 1 is visited or all of the attributes are converted. Zhao [18] has discussed a similar procedure. The second iteration of this example is as follows.

(1) Query Split.

DATABASE M1, W1, R1 SELECT M1.Product.Pnum, M1.Product.Info, W1.[Part Sale Price], M1.Warehouse.Wnum FROM M1.Product, M1.Warehouse, M1.Work WHERE M1.Work.WorkNo=W1.[Order Number]

AND M1.Work.Product =M1.Product.Pnum AND M1.Work.Warehouse=M1.Warehouse. Wnum AND W1.[Part Sale Price]>100 AND W1.[Part Number]=R1.[Part Number]

(2) Attribute conversion.

DATABASE M1, W1, R1 SELECT M1.Product.Pnum, M1.Product.Info, R1.Storage.Price, M1.Warehouse.Wnum FROM M1.Product, M1.Warehouse, M1.Work WHERE M1.Work.WorkNo=Order.OrderNo AND M1.Work.Product =M1.Product.Pnum AND M1.Work.Warehouse =M1.Warehouse.Wnum AND R1.Storage.Price>100 AND W1.Part.PartNo =R1.Storage.ProductNum

(3) Join specification. There is no need for join specification in this example.

(4) Source object identification.

DATABASE M1, W1, R1 SELECT M1.Product.Pnum, M1.Product.Info, R1.Storage.Price, M1.Warehouse.Wnum FROM M1.Product, M1.Warehouse, M1.Work, W1.Order, W1.Part, R1.Storage WHERE M1.Work.WorkNo=W1.Order.OrderNo AND M1.Work.Product =M1.Product.Pnum AND M1.Work.Warehouse =M1.Warehouse.Wnum AND R1.Storage.Price>100 AND W1.Part.PartNo=R1.Storage.ProductNum

The second type of the federated query involves both lower-and upper-level nodes.

Query B: suppose that a manufacturer wants to ascertain both the sale and the manufacturing price of products that are sold at prices higher than US\$100. The following query is sent to warehouse W2.

SELECT [Sale Product Number], [Sale Product Name], [Product Sale Price], [Product Manufacturing Price] FROM W2, R1, R2, ALL WHERE W2.[Sale Product Number]=(R1, R2).[Sale Product Number] AND (R1, R2).[Product Sale Price]>100

The symbol ALL in the FROM clause represents a request to all of the databases that are higher than W2. Again, the query transformation algorithm is executed iteratively. However, the procedure is more complicated and includes two phases.

The query is sent to the lower-level local database. The procedure is exactly the same as in query A.

(1) Query split.

SELECT [Sale Product Number], [Sale Product Name], [Product Sale Price], [Product Manufacturing Price]

FROM W2, R1, R2, ALL

WHERE W2.[Sale Product Number]=R1.[Sale Product Number] AND R1.[Product Sale Price]>100

(2) Attribute conversion.

DATABASE W2, R1, R2, ALL SELECT W2.Product.ItemNo, W2.Product.Description, R1.Storage.Price, [Product Manufacturing Price]

WHERE W2.Product.ItemNo=R1.Storage.Pro-ductNumAND R1.Storage.Price>100

(3) Join specification. There is no need for join specification in this example.

(4) Source object identification.

DATABASE W2, R1, R2, ALL

SELECT W2.Product.ItemNo, W2.Product.Description, R1.Storage.Price, [Product Manufacturing Price]

FROM W2.Product, R1.Storage

WHERE W2.Product.ItemNo=R1.Storage.Pro-ductNum

AND R1.Storage.Price>100

As the query includes the key word ALL and requests the federated attribute [Product Manufacturing Price] belonging to the upper-level node, it must be passed to the upper levels (in fact, the W2 node is unsure of which other nodes have the [Product Manufacturing Price] attribute. The strategy is to pass the query to connected upper-level nodes whenever unknown attributes appear). The second stage deals with federated attributes in the upper levels. Another fourstep algorithm is adopted, but this time the passing direction is upwards. To translate the attributes properly, the execution requires the following modification.

(1) Query split. The query-split step takes place after the subquery in the first stage is sent back to warehouse W2 and federated attributes remain. Each manufacturer that is linked to W2 now generates a subquery by including a join condition in the WHERE clause. The access paths between two databases determine the join condition. In the example of query M2, the federated attribute [Sale Product Number] is the access path attribute in its ACM. The attribute is translated back to the local database as the Product.ItemNo and the Goods.Gno of nodes W2 and M2, respectively.

DATABASE W2, R1, R2, M2, ALL

SELECT W2.Product.ItemNo, W2.Product.Description, R1.Storage.Price, [Product Manufacturing Price]

FROM W2.Product, R1.Storage

WHERE W2.Product.ItemNo=R1.Storage.Pro-ductNum

AND R1.Storage.Price>100 AND W2.Product.ItemNo=M2.Goods.Gno

(2) Attribute conversion. The attribute-conversion step is critical in the upward query. As discussed above, companies at the same level of the coordinated supply chain can be competitors, as they run similar businesses. This means that it is very important not to reveal information to competitors. In this example, the query is passed from W2 to M1 and M2. It is a reasonable assumption that the upper-level nodes (M1 and M2) have information about both the lowerlevel nodes that are competitors (W1 and W2). The FDMS should not allow any nodes to retrieve data from other nodes at the same level. This is why an accessory attribute list is needed. That is, an upwardpassed query can only apply to the accessory attribute list in the higher-level nodes, instead of the complete ACM. This mechanism prevents the possibility of a node investigating its competitors by sending queries to upper-level nodes. As the design of the ACM has taken this situation into account, the constraint is easily applied in this step. In the example, [Product Manufacturing Price] is translated into Goods.Gno, which is located in the M2 database.

DATABASE W2, R1, R2, M2, ALL SELECT W2.Product.ItemNo, W2.Product.Description, R1.Storage.Price, M2.Goods.Price FROM W2.Product, R1.Storage WHERE W2.Product.ItemNo=R1.Storage.ProductNum AND R1.Storage.Price>100 AND W2.Product.ItemNo=M2.Goods.Gno

The second type of query is valid when the query transformation algorithm can convert all of the federated attributes. In contrast, the query is invalid when attribute conversion cannot be obtained after the highest level is reached.

(3) Join specification. There is no need for join specification in this example.

(4) Source object specification.

DATABASE W2, R1, R2, M2, ALL

SELECT W2.Product.ItemNo, W2.Product.De-

scription, R1.Storage.Price, M2.Goods.Price

FROM W2.Product, R1.Storage, M2.Goods

WHERE W2.Product.ItemNo=R1.Storage.Pro-ductNum

AND R1.Storage.Price>100

AND W2.Product.ItemNo=M2.Goods.Gno

As mentioned earlier, partnerships can change in a supply chain relationship. For example, a company might enter into a new relationship or terminate an existing relationship. Hence, the algorithm for constructing federated databases should have a mechanism to add a new node or to drop an old node without significantly affecting the existing structure. The proposed approach only expects a node to maintain ACMs and accessory attributes that have information about lower-level nodes (or upper level nodes when the design begins with the top level nodes). If a node is removed from the supply chain, then only the connected upper-level nodes change their ACMs. In fact, the higher upper-level nodes can remain the same unless: (1) all of the connected nodes at the same level as the removed node are deleted, or (2) the removed node has certain attributes that other nodes at the same level do not have (i.e. certain federated attributes are added because of the removed node). Similarly, if a new node is added to the supply chain, only the connected upper-level nodes have to change their ACMs. The upper-level nodes change their ACMs only when the newly added node has export attributes that other nodes at the same level do not have.

For example, if a new node, W3, is added to the supply chain network in our example, then the ACMs $F _ { i j }$ for the corresponding nodes $L _ { i j }$ are changed to:

<table><tr><td>nodeij</td><td>Corresponding ACM</td></tr><tr><td>node11(R1)</td><td> $L_{R1}$ : ACM [ $f_{R1}$ ]</td></tr><tr><td>node12(R2)</td><td> $L_{R2}$ : ACM [ $f_{R2}$ ]</td></tr><tr><td>node21(W1)</td><td> $L_{W1}$ : ACM [ $f_{W1}$ ]</td></tr><tr><td>node22(W2)</td><td> $L_{W2}$ : ACM [ $f_{W2}$ ]</td></tr><tr><td>node23(W3)</td><td> $L_{W3}$ : ACM [ $f_{W3}$ ]1,2</td></tr><tr><td>node31(M1)</td><td> $L_{M1}$ : ACM [ $f_{M1}, f_{W3}$ ]1,2</td></tr><tr><td>node32(M2)</td><td> $L_{M2}$ : ACM [ $f_{M2}, f_{W3}$ ]1,2</td></tr></table>

<sup>1</sup> Indicates that the node is directly affected by the removal of $W _ { 3 } .$  
<sup>2</sup> Indicates that the node is directly affected by the addition of $W _ { 3 } .$

## 4. Conclusion and discussion

The schema coordination approach to constructing federated databases provides the advantages of maintenance, flexibility, and scalability. We have argued that coordinated supply chains represent complex systems in which the establishment of a universal table that contains all federated attributes is difficult. Therefore, we have proposed an algorithm for developing ACMs according to a bottom-up design strategy. Using this algorithm, each company in the supply chain cooperates with its buyers (which are lower-level nodes from our perspective) to build an ACM of federated attributes to share data with partners, and accessory attributes to prevent the data from being accessed by competitors through upperlevel nodes.

The proposed algorithm provides a possibility for companies to form a coordinated supply chain partnership with

(1) Fewer efforts on sharing information and integrating databases.

(2) Fewer efforts on translating numerous local schemas into a global conceptual schema.

(3) Allowing heterogeneous databases to form a common intermediation.

(4) Sharing data among supply chain partners and preventing data from being accessed by competitors.

As we have focused on building federated databases in a supply chain network with ACMs and accessory attributes, only the vertical relationships of companies have been taken into consideration. It could be argued that horizontal relationships are established when new partnerships are formed. If this is the case, then either the approach taken by Zhao [18] or Ozsu and Valduriez’s [11] conventional distributed database design can be adopted. By integrating our approach and the peer-to-peer relationship approaches used in both studies, the performance for the complex relationships in supply chains can be further improved.

## Acknowledgements

The authors thank the reviewers for their valuable comments. Part of the work described in this paper was supported by the National Science Council of Taiwan (NSC-89-2213-E-033-013).

## References

[1] R. Anupindi, R. Akella, Diversification under supply uncertainty, Management Science 39 (8) (1993) 944– 963.

[2] A.J. Clark, H. Scarf, Optimal policies for a multi-echelon inventory problem, Management Science 6 (1960) 475 – 490.

[3] R. Ernst, D.F. Pyke, Optimal base stock policies and truck capacity in a two-echelon system, Naval Research Logistics 40 (1993) 879 – 903.

[4] S.E. Fawcett, Using strategic assessment to increase the valueadded capabilities of manufacturing and logistics, Production and Inventory Management Journal 2 (1995) 33 – 37.

[5] A.N. Haq, P. Vrat, A. Kanda, An integrated production – inventory – distribution model for manufacture of urea: a case, International Journal of Production Economics 39 (1991) 39 – 49.

[6] L.L. Hau, V. Padmanabhan, S. Whang, Information distortion in a supply chain: the bullwhip effect, Management Science 43 (4) (1997) 546– 558.

[7] L.L. Hau, V. Padmanabhan, S. Whang, The bullwhip effect in supply chains, Sloan Management Review (Spring, 1997) 93– 102.

[8] J.B. Houlihan, International supply chain management, International Journal of Physical Distribution and Materials Management 17 (2) (1987) 51 – 66.

[9] R.C. Kohli, Coordinating buyer – seller transactions across multiple products, Management Science 40 (9) (1994) 45– 50.

[10] M. Madhavaram, D.L. Ali, M. Zhou, Integrating heterogeneous distributed database systems, Computers and Industrial Engineering 31 (1/2) (1996) 315–318.

[11] M.T. Ozsu, P. Valduriez, Principles of Distributed Database Systems, 2nd ed., Prentice-Hall, New Jersey, 1999.

[12] M.J. Shaw, D.M. Gardner, H. Thomas, Research opportunities in electronic commerce, Decision Support Systems 2 (1997) 149– 156.

[13] A.P. Sheth, J.A. Larson, Federated database systems for managing distributed, heterogeneous, and autonomous databases, ACM Computing Surveys 22 (1990) 136– 183.

[14] A. Shtub, Enterprise Resource Planning (ERP), Kluwer Academic Publishers, Boston, 1999.

[15] D.J. Thomas, P.M. Griffin, Coordinated supply chain management, European Journal of Operational Research 94 (1996) 1– 15.

[16] D.R. Towill, Industrial dynamics modeling of supply chains, Logistics Information Management 9 (4) (1996) 43 – 56.

[17] J.L. Zhao, Schema coordination in federated database systems, Proceedings of the 4th Annual Workshop on Information Technologies and Systems (WITS’94), Vancouver, December (1994).

[18] J.L. Zhao, Schema coordination in federated database management: A comparison with schema integration, Decision Support Systems 20 (3) (1997) 243 – 257.

[19] J.L. Zhao, A. Segev, A. Chatterjee, A universal relation approach to federated database management. Proceedings of the 11th International Conference on Data Engineering, Taipei, Taiwan, March (1995).

![](/api/attachments/2TYNT7T4/fulltext/images/670a6a9017a9b0904864b6db854b40833c83f82cb24dfe30c0dcfcff8214fae8.jpg)  
Timon C. Du received his BS degree in Mechanical Engineering from the National Chung-Hsing University, Taiwan, in 1989. He obtained his Master’s and PhD degrees in Industrial Engineering from the Arizona State University. Currently, Dr. Du is an Associate Professor at The Chinese University of Hong Kong, Hong Kong, and Chun Yuan Christian University, Taiwan. His research interests are database management system, intelligent business and electronic business.

![](/api/attachments/2TYNT7T4/fulltext/images/af55f9641ff9746b8743c9f777a53408db57855e77f0f12a12f7f0b2e4a667c1.jpg)  
Hsun-Ming Lee received his BS degree in Applied Mathematics from Tatung University, Taiwan, in 1988. He obtained his Master’s and PhD degrees in Industrial Engineering from the Arizona State University. Currently, Dr. Lee is an engineer at ForeverLiving.com L.L.C.

![](/api/attachments/2TYNT7T4/fulltext/images/3a70c42c1cade1925f740df65da5b6cafdcd1c6098728b3363ea4fc012a7b002.jpg)  
Ane Chen received both his BS and MS degrees in Industrial Engineering from Chung Yuan Christian University in 1997 and 1999, respectively. Mr. Chen is cur rently working in industry. His research interests include information technology, database management and electronic commerce.
