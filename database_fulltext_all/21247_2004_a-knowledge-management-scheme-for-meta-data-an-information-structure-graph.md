---
otero_id: 21247
otero_key: "A8CU6JDN"
title: "A knowledge management scheme for meta-data: an information structure graph"
authors: "Choon Yeul Lee"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00025-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A knowledge management scheme for meta-data: an information structure graph

Choon Yeul Lee

Graduate School of Business IT, Kookmin University, Chungnung-dong, Sungbuk-gu, Seoul 136-702, South Korea

## Abstract

For an effective management of data, we need various kinds of meta-data. This article proposes a scheme—an information structure graph (ISG)—to represent meta-data that are not managed as a database schema. An ISG is a directed graph, where nodes represent data objects. It is built on a database schema and extends it to include data creation structures. For each data object in a database schema, an ISG shows its input data objects and a data creation type. An ISG is an abstraction of a data creation structure and may be applied to enhance our understanding of data. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Data management; Meta-data; Data creation structure

## 1. Introduction

To provide relevant information about data is an indispensable task in data management. Information about data is stored as meta-data in a database system and helps users understand and use data correctly. However, database systems are incomplete in providing information about data, causing some serious misuse of data [2,7,8].

There are two types of meta-data that need to be represented in a database system. The first type is a meta-data about a database schema. It provides information about how to organize and store data such as: what a datum means; how the data are structured; and which value can be assigned to the data. The second type of meta-data is information about processes as applied to data such as: what activities and/or processes are performed to create data; and how data are to be calculated, derived and/or observed from other data items or a real world.

Most meta-data in current database systems are of the former type concerning a database schema. In the relational data model, for instance, meta-data are about tables, columns, indexes and integrity rules, which describe components of a database schema and their organization. Semantic data models, which have been proposed to complement the relational model with features like IS-A relationship, many-tomany relationship, etc., are geared toward a richer semantic description of a database schema [1,6,11,13].

Providing process meta-data, however, may significantly enhance users’ understanding and use of data. It allows users to grasp what the data really mean and how they can be used. Take quantity-on-hand as an example. If a quantity on hand is measured by an observation, it represents the quantity that is stored in a warehouse. If, on the other hand, it is calculated from the previous month’s quantity by deducting an outbound quantity and adding an inbound quantity, it represents the number that appears on an inventory book. If we can represent this process meta-data, it might improve our understanding of data. That is, we might detect that the two quantities on hands are not the same data items and thus they need to be managed independently.

To manage meta-data about processes, we need a representation scheme just like we have a database scheme to manage data. Data creation process comprises a critical aspect of process meta-data. This paper proposes a representation scheme for data creation process. In the next section, scopes of data creation structures are described. In Section 3, a scheme is proposed to formalize the data creation structure. It is formalized as a directed graph, which shall be called an information structure graph (ISG). In Section 4, ideas are proposed to apply an ISG to data management. They include controlling quality of data by searching a critical path in an ISG that shows highest error rates in intra- and inter-database operations; testing semantic homogeneity of data items by comparing their ISG to each other. Lastly, in Section 5, implications of the research are discussed.

## 2. A description of data creation structures

## 2.1. An abstraction of process meta-data

A process is a series of activities that are applied to data. It is the other side of data in information systems, which we need a full understanding of to manage data effectively. In the past, process meta-data have been described in the context of process specification. For example, structured analysis and design technique (SADT), data flow diagram (DFD) and Functional Models in UML (Unified Modeling Language) include them as a part of process specifications [4,5,10,16,17].

More recently there have been attempts to model process meta-data in a more data-like form. One is an information manufacturing system [14,15]. It decomposes information production into data units, vendors, data quality blocks, processing blocks and consumers. A data unit supplied by vendors passes through data quality blocks and processing blocks.

Then, it is delivered to consumers. Another one is an FIP model [9]. It models data processing as applying functions of information processing (FIP) to produce an output information product (OIP) from an input information product (IIP). For example, the following models a process of creating data<sup>\_</sup>set<sup>\_</sup>C by associating data<sup>\_</sup>set<sup>\_</sup>A and data<sup>\_</sup>set<sup>\_</sup>B:

$$
\text { Data\_set\_A } <   \text { associate } > \text { Data\_set\_B } = \text { Data\_set\_C }
$$

Here, data<sup>\_</sup>set<sup>\_</sup>A and data<sup>\_</sup>set<sup>\_</sup>B are IIPs, data<sup>\_</sup> set<sup>\_</sup>C is an OIP, and < associate> is an IFP. In an FIP model, information processes are modeled by six primitive functions—associate, filter, prompt, queue, regulate and transmit.

These process models abstract data processing from a perspective of data management. However, process models are defined independent of a database schema. Thus, they do not share a common presentation scheme with each other. For example, in a relational database system, a database schema is composed of columns and tables. These schema constructs do not match with process model constructs— such as data units in information manufacturing models and data sets in an FIP model. This kind of mismatch prohibits integrating a process meta-data with a database schema meta-data; for example, we may not trace processes that are applied to a schema construct and vice versa.

To manage meta-data effectively as a whole, we need a model that abstracts process meta-data and shares common representation scheme with a database schema. For this, we model process meta-data from the perspective of data creation by connecting an output data object with its input data objects and defining its creation type. These data objects are the ones that compose a database schema.

Data creation meta-data<sup>1</sup> answers the following questions:

What kinds of data items do we need to create a certain data item?

How data are calculated, derived and/or observed from other data items or real world?

Table 1  
Classification of data creation classes

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Values</td></tr><tr><td>Created</td><td>Not created</td></tr><tr><td rowspan="2">Data objects</td><td>created</td><td>object creation</td><td>object assembly</td></tr><tr><td>not created</td><td>value update</td><td>-</td></tr></table>

## 2.2. A classification of data creation structures

In general, data creation involves two actions. One is to create new data objects; the other is to create value for existent data objects. For example, we can create new customers by inserting customer records into a database. Or, we can create new addresses of current customers by updating their addresses. The former means that we create new data objects and assign new values to them. The latter means that we assign new values to the existent data objects.<sup>2</sup>

By combining these two perspectives of data objects and values, we categorize data creation into four classes as shown in Table 1.

(1) An object creation is to produce a new data object. A typical example might be to calculate a purchase order quantity based on a quantity on hand and a safety stock. However, some data objects such as customer order are captured without any reference to other data objects. They are called primitives or primitive data objects.

(2) A value update is to update a current value of a data object. A typical example is an update of a quantity on hand when goods are deposited or shipped.

(3) An object assembly is to produce a new data object without creating new data values. Typical examples are composing an inventory report from inventory items or generating a sales report from customer orders.

These classes are used to define data creation types in a formalization of data creation structures.

## 3. A formalization of data creation structures

To formalize data creation structures, we first conceptualize it as a graph, which shall be called an information structure graph (ISG). Then, we formalize an ISG.

## 3.1. A conceptualization of data creation meta-data

To conceptualize data creation meta-data, this research proposes to add data creation structures onto a database schema. We assume that a database schema is modeled based on the Entity-Relationship (ER) model<sup>3</sup> [3]. Fig. 1 depicts a typical ER diagram.<sup>4</sup> In the diagram, small circles at the end of lines denote many sides of the relationships.

Data creation meta-data are defined for each data object in an ER diagram. For example, let us assume that an inventory database is designed as shown in Fig. 1. Then, data creation meta-data are defined for each attribute like order<sup>\_</sup>no, qty, date and each entity like purchase<sup>\_</sup>order.

To define data creation meta-data, we propose an ISG, which is based on a conceptual graph. A conceptual graph has been applied to systems requirements formalization, especially for hardware systems [4,5] and semantics of natural language [12], etc.

An ISG is a directed graph that connects data objects. In an ISG, a parent node is an output data object and children nodes are input data objects. For example, let us assume that we update inventories by either an inbound delivery or an outbound delivery. Then it is conceptualized as shown in Fig. 2. In the figure, inbound<sup>\_</sup>delivery.quantity<sup>5</sup> and outbound<sup>\_</sup>delivery.quantity are input data objects. And, item.qoh is an output data object. A symbol assigned to item.qoh, , denotes that it is a value update.

![](/api/attachments/A8CU6JDN/fulltext/images/60f1381cd34683d08dfd951f3098e0fc9ecb71aba34f1c114d74416e44f0a870.jpg)  
Fig. 1. An inventory database schema.

As another example, let us assume that a purchase<sup>\_</sup>order is issued based on the following processes. Firstly, a customer order quantity is compared against a quantity on hand. Secondly, a new quantity on hand is calculated by subtracting a customer order quantity from the current one. Thirdly, if the calculated one is below a safety stock, a purchase order is issued. Then the process is conceptualized as shown in Fig. 3. It shows that purchase<sup>\_</sup>order.qty is produced from item.- qoh, customer<sup>\_</sup>order.qty and item.safety<sup>\_</sup>stock. A symbol assigned to order quantity, , denotes that it is an object creation.

![](/api/attachments/A8CU6JDN/fulltext/images/212686af8d8db7a7fd0ad793720c84be555462b9d279b0d873d983d1b165d130.jpg)  
Fig. 2. An information structure graph of a quantity on hand.

![](/api/attachments/A8CU6JDN/fulltext/images/0b480f13ef37fce2f440764c3276d4ead2bec6039f0515e762f75957629f232a.jpg)  
Fig. 3. An information structure graph for an order quantity.

In an ISG, an object assembly depicts a composition of data objects. Let us assume that an inventory summary report is generated from individual inventory items. Then, Fig. 4 shows that an inventory summary report is a composition of details of individual inventory items with the total value. The symbol, P, denotes that inventory<sup>\_</sup>summary<sup>\_</sup>report is an assembly of data objects. An object creation symbol () denotes that a total value is created from a quantity on hand and a price.

![](/api/attachments/A8CU6JDN/fulltext/images/6ef88e14e92ebf1553923fe348a192b66a567e0eecc916244c0375748769f12d.jpg)  
Fig. 4. An information structure graph for an inventory summary report.

In most cases of an object assembly, output data objects do not exist in a database schema. Thus, as shown in Fig. 4, they are included in the ISG in addition to database schema objects.

In sum, an ISG depicts input data objects, output data objects and data creation classes. Processes or functions are not described in detail. These ISGs depict process meta-data for each data objects in a database schema. Thus, we may get data semantics by observing and comparing their ISGs.

## 3.2. A formal description of information structure graph

An ISG is a directed graph composed of nodes and edges.

Definition 1. An information structure graph is a graph $G = \langle V , E , \mu \rangle$ such that,

(1) V is a set of nodes that represent data objects, and E is a set of edges that connect nodes. I.e., hV, Ei is a directed graph.

(2) l is a function from V to the set of data creation types { , , P, } that satisfy the following conditions:

(a) $\mu ( \nu ) { = } \odot$ if m is a leaf.

(b) $\operatorname { I f } \mu ( \nu ) = \otimes , \oplus , \odot ,$ , then there exist children and the children of m are distinct nodes.

Where, $\circledcirc , \ \otimes , \ \circledcirc , \ \oplus$ denote primitives, an object creation, a value update and an object assembly, respectively.

l(m) is called a data creation type of a data object m. For the sake of simplicity, we include input data objects into data creation types. Then, as shown in the following, l(m) denotes input data objects as well as a data creation type of m.

(1) $\mu ( \nu ) = \odot$ denotes that ‘‘m is a primitive data objects and there exists no input data object. I.e., there exists no edge with head $\nu . ^ { \prime \prime }$

(2) $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 1 } , \ldots , \nu _ { n } )$ denotes that ${ } ^ { * } \mu ( \nu ) = \otimes$ and m has n children $\nu _ { 1 } , . . . , . ,$ which are input data objects. And, there exist exactly n edges with head m and their tails are $\nu _ { 1 } , . . . . , \nu _ { n } .$ 99

(3) $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 1 } , \dots , \nu _ { n } )$ denotes that ${ } ^ { * } \boldsymbol { \mu } ( \boldsymbol { \nu } ) = \mathbb { O }$ and m has children $\nu _ { 1 } , . . . . , \nu _ { n } ,$ which are input data objects. And, there exist exactly n edges with head m and their tails are $\nu _ { 1 } , . . . . , \nu _ { n } .$ ,,

(4) $\scriptstyle \mu ( \nu ) = ( \oplus , \nu _ { 1 } , . . . , \nu _ { n } )$ denotes that ${ } ^ { * } \mu ( \nu ) = \oplus$ and m has n children $\nu _ { 1 } , . . . . , \nu _ { n } ,$ which are input data objects. And, there exist exactly n edges with head m and their tails are $\nu _ { 1 } , . . . . , { \nu _ { n } } .$

In short, l(m) denotes a single level ISG for a data object m (see Fig. 5).

Root( G) is the root of an information structure graph $G ;$ leaf( G) is a set of leaves of the graph G. Thus, the root of an information structure graph G(m) is the data object m. I.e., $\nu = \mathrm { r o o t } ( G ( \nu ) )$

In the definition of an ISG, we assumed that there exists only one data creation type for a data object. However, there may exist more than one data creation types for a data object. For example, a quantity on hand can be measured by counting the number of items in a warehouse. Or, it can be calculated by adding (subtracting) an inbound (outbound) delivery to the previous quantity on hand. In this case, either of the following can be true:

l(item.qoh) = , or l(item.qoh)=( , inbound<sup>\_</sup>delivery.quantity, outbound<sup>\_</sup>delivery.quantity)

This means that the data creation type is not a simple one but a composite one. Thus, we need to combine these simple data creation types to formulate a composite one. For this, we introduce artificial data objects of qoh<sup>\_</sup>measured and qoh<sup>\_</sup>calculated, which denote data creation types of qoh that is measured and qoh that is calculated, respectively.

l(item.qoh<sup>\_</sup>measured) = , l(item.qoh<sup>\_</sup>calculated)=( , inbound<sup>\_</sup>delivery. quantity, outbound<sup>\_</sup>delivery.quantity)

Then, l(item.qoh) is defined as follows, which shows that it can be either qoh<sup>\_</sup>measured or qoh<sup>\_</sup>calculated:

l(item.qoh)=(P, item.qoh<sup>\_</sup>measured, item.qoh<sup>\_</sup> calculated)

This example shows that, if a data creation type is a composite one, we need to introduce artificial data objects.

Artificial data objects are introduced for the sake of modeling. Thus, we may incorporate different numbers of artificial data objects even though we model

![](/api/attachments/A8CU6JDN/fulltext/images/204bfd3aa44124476dc260c864e34e46a31db25bec885bb715df121e6f7fc0f5.jpg)  
Fig. 5. Nodes in an information structure graph.

(Rule 1)

(Rule 2)

(Rule 3)

(Rule 4)

(Rule 5)

(Rule 6)

(Rule 7)

(Rule 8)  
(Rule 9)  
![](/api/attachments/A8CU6JDN/fulltext/images/9e63dacf1e1e6a933d4af67f284b5789a0f574769fc94817c6478e988886b0a3.jpg)  
Fig. 6. Information structure graph reduction rules.

the same data creation structure. For example, we may model the above data creation structure of qoh by introducing only one artificial data object, qoh<sup>\_</sup>measured, instead of two artificial data objects, qoh<sup>\_</sup>measured and qoh<sup>\_</sup>calculated.

$\scriptstyle \mu ( { \mathrm { i t e m . q o h } } ) = ( \mathbb { O } ,$ item.qoh<sup>\_</sup>measured, inbound<sup>\_</sup>delivery.quantity, outbound<sup>\_</sup>delivery.quantity)

This example shows that there exists more than one way to represent data creation structures. Here, we introduce rules to test the equivalences of ISGs.

ISG Reduction Rules. An information structure graph $G = \langle V , E , \mu \rangle$ is reducible with an order of ${ \mathfrak { O } } ,$ $\bigotimes \mathrm { > } \bigoplus$ . That is, the following rules are satisfied:

(1) If $\scriptstyle \mu ( \nu ) = ( \oplus , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu _ { 1 } ) = ( \oplus , \nu _ { 3 } , \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \oplus , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } )$

(2) If $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu _ { 1 } ) = ( \oplus , \nu _ { 3 } , \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } ) .$

(3) If $\scriptstyle \mu ( \nu ) = ( \oplus , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu _ { 1 } ) = ( \infty , \ \nu _ { 3 } , \ \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } )$

(4) If $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu _ { 1 } ) = ( \oplus , \nu _ { 3 } , \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } )$

(5) If $\scriptstyle \mu ( \nu ) = ( \oplus , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu _ { 1 } ) = ( \mathbb { O } , \ \nu _ { 3 } , \ \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } ) .$

(6) If $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 1 } , \nu _ { 2 } )$ and $\mu ( \nu _ { 1 } ) { = } ( \otimes , ~ \nu _ { 3 } , ~ \nu _ { 4 } ) ,$ , then $\scriptstyle \mu ( \nu ) = ( \infty , \ \nu _ { 3 } , \ \nu _ { 4 } , \ \nu _ { 2 } )$

(7) If $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu 1 ) = ( \mathbb { O } , \ \nu _ { 3 } , \ \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } )$

(8) If $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu 1 ) = ( \infty , \ \nu _ { 3 } , \ \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \mathbb { O } , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } ) .$

(9) If $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 1 } , \nu _ { 2 } )$ and $\scriptstyle \mu ( \nu 1 ) = ( \mathbb { O } , \ \nu _ { 3 } , \ \nu _ { 4 } )$ , then $\scriptstyle \mu ( \nu ) = ( \infty , \nu _ { 3 } , \nu _ { 4 } , \nu _ { 2 } )$

These rules are shown in Fig. 6. In the figure, the ISGs on the left-hand side are said to be reducible to the ones on the right-hand side.

Using the rules, we can test the equivalence of ISGs. For example, Fig. 7 is an ISG of item.qoh based on item.qoh<sup>\_</sup>measured and item.qoh<sup>\_</sup>calculated. And, Fig. 8 is an ISG of item.qoh based on item.qoh<sup>\_</sup>measured. Then, by applying Rule 5, it is shown that Fig. 7 is reduced to Fig. 8.

Information structure graphs grow as new nodes are added as input or output data objects. An ISG is said to be augmented if nodes and edges are added without altering its current structure.

Definition 2. An information structure graph $G ^ { \prime } = \langle V ,$ $E ^ { \prime } , \mu \rangle$ is an augmentation of a graph $G = \langle V , E , \mu \rangle$ if the following conditions are satisfied;

(1) $V \subseteq V ^ { \prime }$

(2) $E \subseteq E ^ { \prime }$

(3) If $( \nu _ { 1 } , \nu _ { 2 } ) { \in } E ^ { \prime } - E$ , then $\nu _ { 2 } \in V ^ { \prime } - V .$

![](/api/attachments/A8CU6JDN/fulltext/images/28e12bbaa525a1e63d5f5feb703c2cdc83801ee526f48c6ae85ffb8a9d063a7b.jpg)  
Fig. 7. An information structure graph for a quantity on hand with measurement.

![](/api/attachments/A8CU6JDN/fulltext/images/db9eb8f931118ab86af2b0cba7458875249fa32606a950c7003c76a0ce44fc7a.jpg)  
Fig. 8. An information structure graph for a quantity on hand with measurement reduced.

I.e., all new edges are between new nodes, or from nodes in V to a new node.

An augmentation adds new nodes to a graph without altering its structure. For example, in Fig. 9, graph<sub>2</sub> and graph<sub>3</sub> are augmentations of graph<sub>1</sub>. $\mathrm { G r a p h } _ { 2 }$ adds a root to graph . Graph adds a leaf as well as a root to graph<sub>1</sub>. However, graph<sub>4</sub> is not an augmentation of graph<sub>1</sub> because the structure of graph<sub>1</sub> has been changed in graph<sub>4</sub>.

Augmentations are transitive. I.e., if $G _ { 2 }$ is an augmentation of $G _ { 1 }$ and $G _ { 3 }$ is an augmentation of $G _ { 2 }$ , then $G _ { 3 }$ is an augmentation of $G _ { 1 }$ . Among augmented graphs, some have identical leaves. They are called homogeneously augmented graphs.

Definition 3 . Information structure graph $G _ { 1 }$ is called a homogeneous augmentation of $G _ { 2 }$ if $G _ { 1 }$ is an augmentation of $G _ { 2 }$ (or vice versa), and leaf( $G _ { 1 } ) =$ leaf( $G _ { 2 } )$ . A homogeneous augmentation set is a set of information structure graphs that are homogeneous to each other. $\mathrm { A }$ data object $\nu _ { 1 }$ is homogenous to a data object $\nu _ { 2 }$ if the information structure graphs of $\nu _ { 1 }$ and $\nu _ { 2 }$ are members of a homogeneous augmentation set.

Homogeneously augmented graphs share the same leaves. This means that data objects are created from the same primitive data objects. For example, in Fig.

9, graph<sub>2</sub> has the same primitive data objects, $\nu _ { 2 }$ and $\nu _ { 3 } ,$ as $\mathrm { \ g r a p h _ { 1 } ; }$ thus, $\mathrm { g r a p h } _ { 2 }$ is a homogeneous augmentation of graph<sub>1</sub>. However, graph<sub>3</sub> has an extra primitive data object, $\nu _ { 6 } ^ { \prime } ;$ thus, graph<sub>3</sub> is not a homogeneous augmentation of graph . From the fact that graph<sub>2</sub> and graph<sub>1</sub> are members of a homogenous augmentation set, we know that either data object $\nu _ { 4 } ^ { \prime }$ is derived from $\nu _ { 1 } ,$ or $\nu _ { 1 }$ is derived from $\nu _ { 4 } ^ { \prime }$ . However, $\nu _ { 5 } ^ { \prime }$ is not derived from $\nu _ { 1 }$ because graph<sub>3</sub> is not a homogeneous augmentation of graph<sub>1</sub>. As shown in this example, a homogenous augmentation set is an effective criterion to test the semantic relationships among data objects.

## 4. Applications of information structure graphs

An information structure graph is defined on a database schema and abstracts data creation structures succinctly. For each data object in a database schema, we can identify its creation structures. These data creation structures may be applied to data management and their quality control.

In enterprise data management, data are collected from multiple sources. In this case, it might be necessary to answer questions such as: what impacts do data have on other data objects? Which data are comparable to one another? These kinds of typical data management questions are easily answered by an ISG. For example, we might identify major sources of errors by traversing an ISG and searching a critical path that shows the highest error rates in an ISG. Further, we might test the semantic homogeneity of data objects by comparing their ISGs.

![](/api/attachments/A8CU6JDN/fulltext/images/5ace0ddb0960d6e46211cc1576e4b217dc67d0858b90d98514647a9ad9a1898b.jpg)  
Fig. 9. Augmentation of an information structure graph.

## 4.1. Quality control of database operations

An ISG shows data creation structures. Further, it is based on a database schema. Thus, it can be stored just like a database schema that is stored in a data dictionary. For example, in a relational database, ISGs can be described by the following tables, which denote nodes and edges of ISG, respectively.

ISG<sup>\_</sup>node (data<sup>\_</sup>object, data<sup>\_</sup>object<sup>\_</sup>type<sup>6</sup>, data<sup>\_</sup> creation<sup>\_</sup>type, etc.)

ISG<sup>\_</sup>edge (output<sup>\_</sup>data<sup>\_</sup>object, input<sup>\_</sup>data<sup>\_</sup>object, time<sup>\_</sup>lag, application<sup>\_</sup>name, etc.)

Using these tables, we can query for relevant information about data creation structures. For example, given a data item, we can retrieve all input data items that are used to create a quantity on hand:

<table><tr><td>SELECT</td><td>output_data_object, input_data_object</td></tr><tr><td>FROM</td><td>ISG_edge</td></tr><tr><td>CONNECT BY</td><td>PRIOR input_data_object = output_data_object</td></tr><tr><td>START WITH</td><td>input_data_object = ‘item.qoh’</td></tr></table>

The query retrieves all input data objects for item.- qoh. If an ISG for a quantity on hand is defined as shown in Fig. 7, the result is shown in Table 2.

From Table 2, primitive data objects of item.qoh are item.qoh\_measured, inbound\_delivery.qty and outbound\_delivery.qty. Thus, these data have to be correct for quantities on hand to be correct.

An ISG can also be used to identify data objects that are derived from a given data object. Let us assume that manual counting had been incorrect. Then, by querying output data objects that include qoh\_measured as an input data object, we can filter out data items that may have been infected by the poor manual counting.

Table 2

<table><tr><td colspan="3">A result of an ISG query</td></tr><tr><td>Output data object</td><td>Input data object</td><td>Input of input data object</td></tr><tr><td>item.qoh</td><td>item.qoh_measured</td><td></td></tr><tr><td>item.qoh</td><td>item.qoh_calculated</td><td>item.inbound_delivery.qty</td></tr><tr><td>item.qoh</td><td>item.qoh_calculated</td><td>item.outbound_delivery.qty</td></tr></table>

<table><tr><td>SELECT</td><td>input_data_object, output_data_object</td></tr><tr><td>FROM</td><td>ISG_node</td></tr><tr><td>CONNECT BY</td><td>PRIOR output_data_object = input_data_object</td></tr><tr><td>START WITH</td><td>output_data_object = ‘item.qoh_measured’</td></tr></table>

In most relational database systems, a database schema is stored in data dictionary tables as shown in the following:

TBL (table<sup>\_</sup>name, creator, table<sup>\_</sup>type, etc.) COL (table<sup>\_</sup>name, col<sup>\_</sup>no, col<sup>\_</sup>name, col<sup>\_</sup>type, width, nulls, etc.)

Then, we can join data creation meta-data tables with these data dictionary tables.

<table><tr><td>SELECT</td><td>ISG_node.output_data_object,ISG_node.data_creation_type,COL.table_name, COL.col_name,</td></tr><tr><td>FROM</td><td>ISG_node, COL</td></tr><tr><td>WHERE</td><td>ISG_node.data_object = COL.col_name</td></tr><tr><td>AND</td><td>ISG_node.data_object_type = ‘attribute’</td></tr></table>

As shown in the above, for each schema object in a data dictionary, we can easily look up its creation structures by joining data dictionary tables and ISG tables. These kinds of examples show that we can apply various kinds of analysis and management tools to ISGs to improve data management. In sum, an ISG provides a basic instrument to improve data management processes.

## 4.1.1. Quality control of intra-database operations

An ISG is a directed graph. Thus, we can convert an ISG to a distance network by assigning data management statistics such as error rates to its edges. Then, an ISG might be used to control database operations by searching a critical path that shows the highest error rates. For example, a company has noticed that it has issued lots of unnecessary purchase orders. To correct this problem, we may go through the ISG of a purchase order quantity, which is shown in Fig. 3. Let us assume that error rates<sup>7</sup> are collected for each primitive data objects and edges as shown in Fig. 10. Then, we can infer that incorrect manual counting has been the major source of unnecessary orders.

Further, if we can assign time lags to edges in an ISG, we can analyze accumulated time lags between real world events and database values. This kind of analysis on an ISG may be applied to schedule database back-ups and recoveries.

## 4.1.2. Quality control of inter-database operations

In enterprise data management, data are collected from multiple sources of operational databases and/or personal files. To load these data into a corporate database, they are to be compared to each other and transformed if necessary. An ISG can be applied to describe this kind of inter-database processes. For example, let us assume that a data warehouse is created from order data in an order database and customer data in a customer database. Then data creation structures are modeled as shown in Fig. 11.<sup>8</sup>

An ISG with multiple data sources depicts data extraction, transformation and cleansing processes. For example, an error rate of 0.01 is assigned to customer addresses in Fig. 11. It means that one customer out of 100 might have a wrong address. And a value of ‘  0.5’ assigned to a data creation type  means that 50% of the errors are corrected by data cleansing processes.

![](/api/attachments/A8CU6JDN/fulltext/images/3f914cc388f080ccabbe8617a6bfa6f1edbdcd0a2f94e95bddeabcc8d95b1e20.jpg)  
Fig. 10. An information structure graph with error rates

## 4.2. Testing semantic homogeneity of data objects

Information structure graphs conceptualize data creation structures. By utilizing this feature of information structure graphs, we can test such semantic relationships as homonyms. For example, a quantity on hand in Fig. 7 is not identical to that in Fig. 2. Thus, they are homonyms and have to be treated as distinct data items.

In addition to detecting homonyms, information structure graphs can also be used to test miscellaneous semantic relationships among data objects. If an information structure graph is an augmentation of another, then one is semantically built upon the other. If an augmentation is homogeneous (i.e., an augmentation does not include additional primitives), then one is derived from the other. If not, then one utilizes additional input data and thus is not derived from the other.

These kinds of semantic relationships can be applied to identify data objects that are comparable with each other. A data object is comparable with another if it is created from the same process as the other’s, which implies that its ISG is equivalent to the other’s. Thus, data objects are comparable with each other if their ISGs are equivalent to each other; they are not comparable with each other if their ISGs are not equivalent to each other. For example, the ISG of a quantity on hand in Fig. 7 cannot be reduced to that in Fig. 2. Thus, the quantity on hand in Fig. 7 is not comparable with the one in Fig. 2. On the other hand, the ISG in Fig. 7 is reduced to the ISG in Fig. 8; thus, the quantity on hand in Fig. 7 is comparable with the quantity on hand in Fig. 8 because their ISGs are equivalent to each other.

Semantic relationships among data are very helpful and may ease the processes of database aggregation. With the advent of data warehouses and business intelligence databases, data extractions and transformations have become major issues in data management. Without information structure graphs, we may have to go through all details of database schemas and application specifications to identify inter-related data objects; however, with information structure graphs, we can easily identify them by traversing the graphs. Further, we can group data objects that share common primitive data objects. These clusters of common primitive data objects help to work on relatively homogeneous data objects and ease data transformation tasks.

![](/api/attachments/A8CU6JDN/fulltext/images/38d1a60f6784e8dc15e1bf522ac94eb9ee1db0e5a1bf1ac442cd5f9e8f4614eb.jpg)  
Fig. 11. An information structure graph with error rates for inter-database operations.

## 5. Conclusions

The lack of a process meta-data that shares a common representation scheme with a database schema has been a motivation for this exploratory study. To integrate process meta-data with a database schema meta-data, an information structure graph (ISG) is proposed, which models process meta-data from the perspective of data creation.

Data creation process comprises a critical aspect of process meta-data and its abstraction enhances our understanding of data. Applications of an ISG might be retrieving all input data objects for a given data object; retrieving all output data objects derived from a certain data object; identifying a critical path to lower accumulated error rates; identifying interrelated data objects in terms of data creation; and, testing such semantic relationships as synonyms and homonyms.

This paper is an initial attempt to abstract data creation structures based on a database schema metadata. To better represent data creation processes, an ISG needs to be expanded to include additional data creation primitives such as ‘compare’, ‘correct’, etc. These primitives can be modeled as data creation types or distinct constructs from data creation types. In either case, their feasibility needs to verified.

## Acknowledgements

The author thanks Professor Sung-Hyun Juhn for insightful suggestion on the proof and presentation. Constructive criticism from anonymous reviewers greatly helped to improve the contents and composition of this paper.

## References

[1] S. Abiteboul, R. Hull, IFO: a formal semantic database model, ACM Transactions on Database Systems 12 (4) (1987, Dec.) 525 – 565.

[2] M.H. Brackett, The Data Warehouse Challenge: Taming Data Chaos, Wiley, New York, 1996.

[3] P. Chen, The entity relationship model—toward a unified view of data, ACM Transactions on Database Systems 1 (1) (1976, Mar.) 9 – 36.

[4] W.R. Cyre, Capture, integration, and analysis of digital system requirements with conceptual graphs, IEEE Transactions on Knowledge and Data Engineering 9 (1) (1997, Jan.) 8 – 23.

[5] C. Gane, T. Sarson, Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Englewood Cliffs, 1979.

[6] M. Hammer, D. McLeod, Database description with SDM: a semantic database model, ACM Transactions on Database Systems 6 (3) (1981, Sep.) 351 – 386.

[7] G.E. Liepens, V.R.R. Uppuluri, Data Quality Control: Theory and Pragmatics, Marcel Dekker, New York, 1990.

[8] T.C. Redman, Improve data quality for competitive advantage, Sloan Management Review (1995, Winter) 99 – 107.

[9] T.C. Redman, Data Quality for the Information Age, Artech House, Norwood, 1996.

[10] J. Rumbaugh, M. Blaha, W. Premerlani, F. Eddy, W. Lorensen, Object-oriented Modeling and Design, Prentice-Hall, Englewood Cliffs, 1991.

[11] D.W. Shipman, The functional data model and the data language: DAPLEX, ACM Transactions on Database Sys tems 6 (1) (1981, Mar.) 140 – 173.

[12] J.F. Sowa, Conceptual Structures: Information Processing in Mind and Machine, Addison-Wesley, Reading, 1984.

[13] T.J. Teory, D. Wang, J.P. Fry, A logical design methodology for relational databases using the augmented entity-relationship model, Computing Survey 18 (2) (1986, June) 197– 221.

[14] R.Y. Wang, A product perspective on total data quality management, Communications of ACM 41 (2) (1998, Feb.) 58 – 65.

[15] R.Y. Wang, V.C. Storey, C.P. Firth, A framework for analysis of data quality research, IEEE Transactions on Knowledge and Data Engineering 7 (4) (1995, July) 623– 639.

[16] J.D. Warnier, Logical Construction of Systems, Van Nostrand Reinhold, New York, 1981.

[17] E.N. Yourdon, Modern Structured Analysis, Prentice-Hall, Englewood Cliffs, 1990.

![](/api/attachments/A8CU6JDN/fulltext/images/57919b6c691a7afdc7573b83a3ad659faa0dedd8b083fe86311a604ac974131f.jpg)  
Choon Yeul Lee received the MBA degree in 1983 from the Seoul National University and the Ph.D. degree in 1990 from the University of Michigan. He is an associate professor of management information systems and acts as a Dean of the Graduate School of Business Information Technology at the Kookmin University. His research interests include database systems, meta-data management, and data quality management.
