---
otero_id: 17931
otero_key: "CN65DF62"
title: "From files to data base: A tutorial"
authors: "Václav Chvalovský"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90038-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# From Files to Data Base: A Tutorial

Václav Chvalovský

DP Centre of CKD PRAHA Co., Prague, Czechoslovakia

This paper aims at describing the transition procedure from conventional data files to a data base, beginning with data models of reality and ending with the data definition using the CODASYL DDL. The transition process is explained and a case study is also provided.

Keywords: Data bases, data models, entities, normalization of data, three normal forms of data, SET, DDL.

![](/api/attachments/CN65DF62/fulltext/images/b19df47a161a208ff5b1c00ef71c25f32057e10cd7733a022d429dce49dc7d7f.jpg)

Dr. Chvalovsky has been in EDP since 1965, most recently as the Programming Manager. He has worked on application projects and software systems, and has spent one year on assignments at ICL Ltd. in UK (decision tables software and COBOL compilers), and two years in Nairobi, Kenya as Lecturer; Director, Institute of Computer Science at the University of Nairobi. He is the author of more than 50 articles and like contri butions, and of books on Decision Tables (1974) and Data Bases (1976). He has also lectured on data processing courses and is, at present, a part-time lecturer on data processing and information systems at the Institute of Economics in Prague. He holds an ING degree from the Institute of Economics in Prague, and a PhD (CSc.) degree from the Czechoslovak Academy of Science.

## Introduction

Despite the proliferation of literature on data bases, the actual design of the data base is often poor and it becomes a serious source of embarrassment causing many errors in the implementation. While we have considerable understanding of logical and physical data structures, we still know little about their development.

Data base designers should know how to convert conventional data files into a proposed data base in such a way as to utilize all investment and experience built into the present files. Little is published that treats this subject in detail. Date [1] and Stewart [2] are examples of attempts to write a guide for potential data base designers.

This paper has been written for the data base professional; it outlines the conversion process from files to a data base. To do so, it deals with the following two main stages: (1) normalization of data, and (2) design of CODASYL SETS.

## 1. Conversion Process Outline

Since most of the terms and categories used in this text have already been defined and explained in literature on data bases (see ref. [1] or [3]), we can use them here to outline the principal stages of the conversion as shown in Fig. 1. The stages complete the transition from present data files to a data base.

I.1. Review of the Basic Terms: Reality, Entity, Attribute

We define reality as any conceivable non-empty set of objects which become subject to our observation or analysis. More specifically, inasmuch as we are dealing with automation, we always study reality from this point of view.

Reality is composed of a definite number of entities. Here we make a distinction between: entity type, and entity domain.

As to the type of entities we distinguish between real entities (people, machinery, stock items, buildings, accounts, etc.) and abstract entities, which map associations among the former. There are many entity domains: for example, the set of all employees may be specified as the set of Employee Entities, orders as the set of Order Entities, etc.

Properties shared by entities are called attributes (employee name, item number, product identification). Associations, i.e. abstract entities, can also possess properties.

## 1.2. Entities and Data Records (Files)

Conventional data files consist of various types of records. Every record is supposed to reflect the state

![](/api/attachments/CN65DF62/fulltext/images/480829477e83137aba11dcb8eecbe65e548e8c1bee7a2c1d8198ac532d9a92bb.jpg)  
Fig. 1a.

![](/api/attachments/CN65DF62/fulltext/images/3f6d26b2978e8433a97131fc46d7ca98773e11b2942f32f73ad8d852559b824f.jpg)  
Fig. 1b. Transition to a data base.

of its corresponding real entity at some discrete time period. Data items or fields stand for attributes.

It is important to remember that record types coming into the original data bases (the SET OF FILES in Fig. 1) map real entities only. We are, thus, used to working with a Personnel File, a Products File, a Goods File, etc. To keep up with the pace of automation, it became necessary to record certain associations as well, in addition to the state of real entities.

Lacking more suitable methods, we generally extended data records by adding new attributes. By combining attributes belonging to several real entities, we can now, to a certain degree, substitute associations for records and bind two or even more real entities via one record type.

## 1.3. Disadvantages of the Conventional Approach

Every DP professional has run into the problems connected with the present data files. A few of these are listed below. For further details, see ref. [3] or [5].

(1) It is extremely difficult to connect records of different types in the present files because of their great degree of independence.

(2) It is not easy to discover what particular real entities are mapped by present data records because of the long history of their continuous extension and amendment.

(3) Serious problems arise with the maintenance of integrity in present files. The need to update groups of attributes in several locations (data files or records) may cause problems.

(4) Finally, the size of data files can easily exceed reasonable limits.

Altogether, these disadvantages have made our sets of data files almost uncontrollable. This results in poor efficiency of data processing, which is dependent on the way data is structured and stored.

## 2. Normalization, Three Normal Forms of Data

Based on the above problems with the current files, it follows that the main idea behind data normalization is to attempt to move data closer to reality in the sense of improving the way that reality is being reflected in data. But practical requirements of navigation through records in the data base force us to deviate from this simple point of view.

## 2.1. Functional Dependence

Although it is possible to base our definition of functional dependence on basic concepts of the theory of sets (e.g., the way D. Tsichritzis and F. Lochovsky treat this subject in ref. [5]), we use instead the most popular definition offered by Martin in ref. [3]. With only minor revisions of the original, we can say that item B of a data record D is functionally dependent on item A of D if, at each instant of time, each value of A has no more than one value of B associated with it in data record D. In other words, item A is said to identify item B.

We make use of this concept when analyzing relations between record keys, i.e. key items (prime attributes) and nonkey items (nonprime attributes). Although we aim at producing data records with full functional dependence, we often have to split original records into more than one record to meet this goal.

This implies substitution of attribute relationship in original records by record associations.

Such associations have existed since we set up the first data file. However, because of the lack of more suitable methods of their implementation, we could not avoid combining attributes from more entities into one record. It is ironic that the identical method was followed when disks because readily available in the late sixties.

## 2.2. Three Normal Forms of Data

The normalization process attempts to produce records that will map their respective real entities as tightly as possible. To this end, three stages of the process are defined:

(1) conversion of unnormalized records to First Normal Form (1NF),

(2) conversion of records in 1NF to Second Normal Form (2NF),

(3) conversion of records in 2NF to Third Normal Form (3NF).

(1) A record is said to be unnormalized (NNF) if it contains one or more repeated groups on nonkey items.

Example: The following record contains details about programmers and the programs under development. It is in NNF:

PROJECTS (PERS-NUMBER (\*), PERS-NAME, GRADE, SALARY, PROGRAM-NAME, STARTING-DATE, TERM-DATE, SIZE, PROGR-LANG),

where PERS-NUMBER = record key, and the items commencing with

PROGRAM-NAME until PROGR-LANG (inclusive) can repeat (the number of programs) times.

(2) To convert records in NNF to INF we must separate repeated groups from the original records. However, this also means dividing the record from the Example into two new records. This step is shown in Fig. 2. Functional dependencies are shown using arrows oriented from keys to nonkey items to emphasize that an item "is being identified by . . ."

No matter how neatly the new records reflect their corresponding entities, something has been lost when the source record is broken into two parts. If the new records are left as they are, we have no means of finding out who is the author of which program; i.e. we have disrupted the original association between programs on one side and their originators on the other.

![](/api/attachments/CN65DF62/fulltext/images/7014718ee6195925861a3d4a055ec085bc6f781696004a52f02ce4a6d21a93e3.jpg)  
Fig. 2. Conversion to 1NF.

To remedy such a situation (i.e. not to lose the relationship between programs to programmers) we can retain the key of the former record, which becomes the key of the PROGRAMMERS record, and make it a part (a candidate key) of the key in the PROGRAMS record. By doing so, the latter record will contain the concatenated key. The expanded PROGRAMS record is shown in Fig. 3, though this may later cause some other problems.

(3) A record is in 1NF and also in 2NF is it has a concatenated key and if all nonprime items are fully functionally dependent on the entire concatenated key. That is, there can be no nonprime item such that it would depend on a candidate key only. It also follows from this definition that every record in 1NF not having a concatenated key is automatically in 2NF.

The record in Fig. 4 is in 1NF, but not in 2NF: only QTY-ORDERED is functionally dependent on the concatenated key as a whole, while other non-prime items depend on the candidate key PRODUCT-NO only via another candidate key, ORDER-NO. Once the original record is split (as shown in Fig. 5) that problem is solved.

![](/api/attachments/CN65DF62/fulltext/images/3cff995de2499c3df1d82ff2955dd772c7cf02f553bebf23b1310742d0beee4d.jpg)  
Fig. 3. Expanded record (concatenated key principle).

![](/api/attachments/CN65DF62/fulltext/images/c74741001dee0e0632bee6e62fc105714f3e5e0c316de45f471c3e85b1d7e26c.jpg)  
Fig. 4. Record in 1NF before further normalization.

![](/api/attachments/CN65DF62/fulltext/images/432f9ef7bbd7c4dbeba4b8fd05ed95e74a9135a9c452d66fa6b1671d1dc4ef6f.jpg)  
Fig. 5. Records in 1NF and 2NF.

![](/api/attachments/CN65DF62/fulltext/images/706cbd4060be0170b808a55fa66b1fd38aed2f33516907eea9dfce63a766b6e5.jpg)  
Fig. 6. Transitive dependence.

![](/api/attachments/CN65DF62/fulltext/images/a931a94a9ccf162c147f00e6e08d1e38531af1ac472a7a0d65203f4dbfec1e17.jpg)  
Fig. 7. Records in 3NF.

(4) The last normalization step, which aims at converting records already in 2NF to 3NF, should remove any transitive dependence. Transitive dependence is defined as the state when one or more nonprime items depend on the record key only via another nonprime item(s). This situation is best illustrated using the ORDER record as used in Fig. 5.

In Fig. 6, CUSTOMER-ADDRESS as well as CREDIT-RATING are transitively dependent on the key item (transitive dependence path is shown as circles). Conversion of this record to 3NF results in its splitting again into two records (Fig. 7).

Table 1.  
![](/api/attachments/CN65DF62/fulltext/images/10af996488ec8d9ad587fc10d5535cd452273920328cb43bbdf299476359ae19.jpg)

In most cases, data records in 3NF are ready to be stored in a data base. Although some authors describe a Fourth Normal Form (4NF) of data, it is of little practical value and seems to represent a rather exceptional and rare case. It is also sometimes called Boyce-Codd Normalized Form (BCNF). (see ref. [2] or [5])

Table 1 summarizes the rules of data normalization.

## 3. Definitions

## 3.1. Object and Control Relationship

The next step in transition to a data base is to define associations among records in 3NF and to set up a Global Data Model. The associations specified should reflect two kinds of actual relationships:

(1) the object relationship among real entities (e.g. certain products are manufactured from a definite set of material items, etc.),

(2) the control or arbitrary relationship among real entities to connect certain kinds of entities for control, often due to the management system.

It is mainly the latter sort of relationship which needs to be observed when designing navigation paths. Two things, in particular, are of great interest:

(1) the direction of an association between two or more records,

(2) the type of association: 1 to 1, 1 to M, or N to M. These can be drawn by means of directed arrows.

It is useful to adopt certain conventions at this point. Since we are also going to observe navigation requirements in SETS, we will use mostly bipolar arrows. Thus, the arrow will be on one side only if one way navigation (i.e. association) is assumed.

Table 2.

<table><tr><td>SET Name</td><td>OWNER Record</td><td>MEMBER Record</td><td>Associations</td></tr><tr><td>PRODUCTION</td><td>SUPPLIES</td><td>SUPPLIERPRODUCT</td><td>1 : 2M : 2</td></tr><tr><td>TRANSACTIONS</td><td>SALES</td><td>PRODUCTORDER</td><td>N : 1M : 1</td></tr><tr><td>DISPATCH</td><td>ORDERED-BY</td><td>ORDERCUSTOMER</td><td>N : 12 : 2</td></tr><tr><td>SUPPORT</td><td>TRANSL CRT</td><td>ORDERCUSTOMERCARRIER</td><td>1 : 1 : 1</td></tr></table>

## 3.2. SET Fundamentals

From now on, we will adopt the well-known and widely used principles of "CODASYL SETS." Since there is ample literature on this subject, we will review only the basics:

(1) A SET type consists of only one OWNER record type and one or more MEMBER record types.

(2) It is possible that any MEMBER record type in one SET type may also be OWNER type of yet another SET type.

(3) It is essential to distinguish between the SET type and its occurrences.

(4) The Singular SET is an exception to rule (1), as its only OWNER is SYSTEM, i.e. there are not actual OWNER data records in such SETS. We may consider this type of SET to be the same as a conventional data file.

(5) Fig. 8 introduces the basic graphical notation used here in the design of Global Data Model. This has been derived from Bachman's Diagrams.

## 3.3. SET Design Rules

To implement a SET, the following rules must be observed:

(1) Since association between A and B records is 1:M, and backward navigation is required, the process described below is adopted:

\- record B will carry a concatenated key (key A + key B);

\- a pointer will have to be stored in every record A pointing to the very first occurrence of record B belonging to the current SET occurrence (to maintain navigation from A to B);

\- to keep track of all occurrences of record B within a SET occurrence, it is necessary to make them into a chain by means of Forward/Backward Pointers, or else to use a pointer array attached to the OWNER record, possibly with single pointers back from the MEMBER record.

![](/api/attachments/CN65DF62/fulltext/images/182044f8afe037fe352a213e5b3b271ae117f34a07f3e44e6c445de1eccbea9e.jpg)  
Fig. 8. A CODASYL SET.

(2) Any navigation from record B to record C of the same SET, or vice versa can only be achieved via the OWNER record (record A).

(3) Since association between record A and record C is 1:1, it is enough to specify a concatenated key (A + C) in record C and to use a pointer from A to C, which is going to be stored in all occurrences of record A (There will be only one record A and record C in any one occurrence of the SET).

Rules (1) to (3) apply to the majority of SETs which are based on associations 1:1 or 1:M. Associations N:M cannot be implemented unless special care of the “N side” is taken in this association. In practice, we split any N:M association into two, (1 to N, and 1 to M and design two corresponding SETS.)

Consider now the earlier example of programmers and programs. It is probable that either of the following two conditions occur:

\- One programmer works on several programs at the same time $(1:M)$ ,

\- Several programmers work on the same program $(N:1)$ .

Under these circumstances, we must establish a special purpose association record and propose two SETs. This process, outlined in Fig. 9, is the only way to implement network-like data structures in accordance with the CODASYL SET principle. The association record PROG-PROG is a bridge between PROGRAMMERS and PROGRAMS. Association records in CODASYL SETS are often also used to carry items common to both partner records (the intersection data), thus saving space and speeding up enquiries. Record ORDERED (Fig. 5) is a typical example.

It must be said that the principle of association records is not new. There have been software systems making use of a similar principle since the mid sixties. An example is the ICL PLUTO System (for Production Control), whose data was broken logically into two parts: (1) Master File and (2) Structure File. Similar methods could be found in IBM's BOMP (Bill of Materials Processor).

![](/api/attachments/CN65DF62/fulltext/images/0dd2f04f863c778d2ac9b7841c7a684dfad45630094779c9db2d521487359302.jpg)  
Fig. 9. N : M association in SET.

## 4. A Case Study

Here we illustrate the complete transition process from files to a data base. The starting point is the conversion of data to 3NF, and the transition ends with specification and description of SETs in a Data Description Language (DDL).

## 4.1. Source (Original) Data Records

4.1.1. Orders (ORDER)

ORDER (ON (\*), DA, CN, CA, TC, TF, TR, PN, QU, UP)

ON = order number (record key)
DA = date of order
CN = customer number/name
CA = customer address
TC = transport company
TF = transport means
TR = transport rates
PN = product number/name
QO = quantity ordered by the customer
UP = unit price

4.1.2. Suppliers (SUPPLIER)
SUPPLIER (SN (\*), SA, QS, PN)
where
SN = supplier number/name (record key)

SA = supplier address
QS = quantity ordered from this supplier
    supplier
PN = product number/name

## 4.2. Record Occurrences (Sample)

## 4.2.1. Order

30851, 100580, UPINKASU, PRAHA1, CSAD, TRUCK, 15-15-09, 012, PILSNER, 1000, 4.00

30859, 150580, RADIOPALAC, PRAHA2, CSD, RAIL, 15-08, 012, PILSNER, 550, 4.00

30860, 150580, RADIOPALAC, PRAHA2, CSAD, TRUCK, 15-09, 112, GAMBRINUS, 400, 2.00 010, LAGER, 650, 1.90

30880, 170580, JEDNOTA-HOROVICKY, CSAD, TRUCK, 15-11, 012, PILSNER, 100, 4.00 510, LAGER, 250, 1.90

60039, 100480, MONIMPEX-BUDAPEST, CSD, RAIL, 19-00, 512, BAKALAR, 609, 3.90

## 4.2.2. Supplier

P-03, PRAZDROJ PLZEN, 1500, 012
P-04, GAMBRINUS PLZEN, 400, 112
S-01, V. POPOVICE BREWERY, 650, 010
S-03, RAKOVNIK BREWERY, 600, 512, 250, 510

## 4.3. Conversion to First Normal Form

Observing the rules of conversion, the first step results in records without repeating groups of items. Since we have to create at least one new record type, we must also decide on the key items of the new record(s).

There are two repeating groups in the example, one in the SUPPLIER records; the other in the ORDER records:

• PN, QO, UP (ORDER)

• QS,PN (SUPPLIER)

It is perfectly normal that a customer (a pub, bar or any similar establishment) places an order (e.g. to a wholesale dealer), requiring more than just one kind of beer. At the same time, we can place orders with the potential suppliers (vendors), who can supply more than one brand.

The following four records will be set up after the conversion to 1NF:

• ORDER (ON(\*), DA,CN,CA,TC,TF,TR)

• SALES (ON(\*), PN(\*), QO, UP)

• SUPPLIER (SN (\*), SA)

![](/api/attachments/CN65DF62/fulltext/images/1e76248c6b46999c7c79da5d47ed78bc994110e01851c5848529c3fe002887e9.jpg)  
Fig. 10. Conversion of example to 2NF.

• SUPPLIES (SN(\*), PN(\*), QS).

The actual occurrences of the new records can easily be derived.

## 4.4. Conversion to Second Normal Form

To convert the above four records to 2NF, we have to specify all functional dependencies among their items. These are depicted in Fig. 10. Since both the ORDER and SUPPLIER records have single keys, they are automatically in 2NF. The SUPPLIES record, although having a concatenated key, is also in 2NF because the quantity to be supplied depends on the entire key.

The situation in the SALES records is somewhat more complicated. Because we have a policy of having one price for one brand of beer, no matter to whom it is delivered, the unit price is dependent on the product number and not on the entire key. The only fully functionally dependent nonprime item in this record is QO.

To resolve this conflict, the SALES records are split into the following:

\- PRODUCT(PN(\*),UP)

• SALES(ON(\*),PN(\*),QO).

After this conversion we have five records in 2NF:

• ORDER(ON(\*),DA,CN,CA,TC,TF,TR)

\- PRODUCT(PN(\*),UP)

• SALES(ON(\*),PN(\*),QO)

• SUPPLIER(SN(\*),SA)

• SUPPLIES(SN(\*),PN(\*),QS)

## 4.5. Conversion to Third Normal Form

Let us first draw all functional dependencies in our five records in 2NF (Fig. 11). It is clear that the only record violating the definition of 3NF is ORDER. One customer may place several orders, so only DA and CN are fully functionally dependent on the prime attribute ON. At the same time, several transport companies may serve one customer, and more customers may use services of the same carrier. The relationship between CN and TC is N : M, and only TC is dependent on CN. Nonprime items CA, TC, TF, and TR are therefore only transitively dependent on the prime item ON (via CN or TC respectively).

![](/api/attachments/CN65DF62/fulltext/images/13ff16d1dc87bb9ebede476ee5b132474469023f8ac3ffd9a9f3391f359d96c7.jpg)  
Fig. 11. Functional Dependencies in 2NF.

Removing the transitive dependencies will result in the three records:

• ORDER(ON(\*),DA)

• ORDERED-BY(ON(\*),ON(\*),CA)

• CARRIER(ON(\*), ON(\*), TC(\*), TF, TR).

While there is no need to worry about the first of these records, the other two may cause some problems. Both of them are in 1NF only, as CA is dependent on CN only; similarly TF and TR are identified by TC. We leave this exercise to the reader and now show only the final four records after the conversion of ORDERED-BY and CARRIER records to 3NF.

• ORDERED-BY(ON(\*),CN(\*))

\- CUSTOMER(CN(\*),CA)

• TRANSPORT(ON(\*),CN(\*),TC(\*))

• CARRIER(TC(\*),TF,TR).

This last step brings us to the end of the entire conversion process. Our thorough data analysis has led to setting up nine records in place of the original two:

\- ORDER(ON(\*),DA)

• ORDERED-BY(ON(\*),CN(\*))

\- CUSTOMER(CN(\*),CA)

\- TRANSPORT(ON(\*),CN(\*),TC(\*))

• CARRIER(TC(\*),TF,TR)

\- PRODUCT(PN(\*),UP)

• SALES(ON(\*),PN(\*),QO)

• SUPPLIER(SN(\*),SA)

• SUPPLIES(SN(\*),PN(\*),QS).

The contents of the above records are divided into two main groups:

(1) Records: ORDER, CUSTOMER, CARRIER, PRODUCT and SUPPLIER describe real entities while (2) ORDERED-BY, TRANSPORT, SALES and SUPPLIES reflect abstract entities.

As long as we consider economic (business-like) reality to be the subject of our analysis, the latter category of records maps processes (transactions) initiated within the boundaries of the system. This is one of the most significant contributions of data base technology.

## 4.6. Set Design

## 4.6.1. Designing the Global Model of Data

The proposed data model depends, to a great extent, on the navigation requirements. The schema of Fig. 12 is therefore fairly subjective in nature and a confusion of interpretation could easily result. Five records, i.e. SUPPLIER, PRODUCT, ORDER, CUSTOMER, CARRIER, map real entities, and are the owners of the five SET types. MEMBER records are in the following SET types:

![](/api/attachments/CN65DF62/fulltext/images/17e2458334aac781b197e6b2956d194bc5d3e6ad99b093a037046d4e09b65b23.jpg)  
Fig. 12. A CODASYL Structure for an Example.

• PRODUCTION: SUPPLIES

• TRANSACTION: SUPPLIES

• BALANCE: SALES
ORDERED-BY
TRANSPORT

• DISPATCH: ORDERED-BY

• SHIPMENT: TRANSPORT

SUPPLIES, SALES, and ORDERED-BY records are MEMBER types in two SETs, while TRANSPORT participates in three SETs.

## 4.6.2. Impact of Navigation Requirements on the Model

Little of the literature on data bases goes further than this. (ref. [3], is an exception).

However, a closer look at the reality, as mapped by data records, reveals that real entities and data records mapping these entities, reflect only static features of the reality. On the other hand, abstract entities and their mapping in corresponding data records reflect dynamic features of the reality – or events.

There can be no doubt at this point which view is more important. Inasmuch as we all agree on the strategic aims – assisting and improving decision-making and management (control) of the reality – we should primarily focus interest on the dynamic features. This, however, implies certain modifications of our present view of the global data model introduced in Fig. 12.

The changes we have in mind have to do with navigation paths in the model. It is awkward to navigate the processes (abstract entities) towards their backing (real entities) unless the former become owners of sets. Such a change can drastically improve the overall efficiency of the whole system based on the new model, and can guarantee the much needed flexibility of data structures.

The proposed modification and the new model, are shown in Fig. 13. It is not difficult to explain the principles behind this schema.

Upon receipt of an order, a new ORDERED-BY record occurrence is created to connect the order with its customer. At the same time, another new record (SALES) is set up, binding the order and product, and indicating the quantity ordered on this particular concatenated key. The data base is searched to locate a potential supplier (using the product number and searching the PRODUCTION SET). A new SUPPLIES record is created, to bind the supplier with the product, and showing the quantity to be supplied by that respective supplier.

Also, a new record called SHIPMENT is established, connecting the order, customer, and carrier (who will deliver the goods).

The method outlined above has a definite advantage. The data records which map processes (events) are much more volatile and subject to frequent changes in comparison with their counterparts. It is more rational, then, to make these records OWNERS and create new occurrences of each SET any time a new event appears. One could even think of MEMBER records as playing the role of a “material backup” of the events.

The shift of emphasis towards events invokes antoher modification to our schema. There is no need, in the new model, to maintain pointers from MEMBERS to OWNERS. This is mainly due to the prevailing direction of navigation from OWNERS to MEMBERS. We can only work with MEMBER pointers from an OWNER record to its MEMBER record(s). This being the case, we would draw every OWNER: MEMBER association in the schema as: ← or ↔ respectively.

Absence of OWNER pointers may have significant impact on the physical data structures, i.e. the way data is going to be organized and stored in the data base. Considerable space on disks can be saved and the overall efficiency of the Data Base Management System (DBMS) can be improved as well.

The new model has much in common with relational data base models. The association records (OWNERS of the SETS) stand for relations defined above the sets of records mapping real entities. They can be used to connect or disconnect elements of the participating sets in a flexible manner and, thus, help in mapping system dynamics.

## 4.6.3. SET Specification in DDL

Having drawn our schema as the global data model, we should define it to be acceptable by the proposed DBMS. The CODASYL DDL for the SCHEMA is used here. Only the SET called TRANSACTION in Fig. 13 is specified. Only a skeleton of the RECORD and SET descriptions has been given.
RECORD DESCRIPTION.
RECORD NAME IS PRODUCT.
LOCATION MODE IS CALC USING PN,
DUPLICATES ARE NOT ALLOWED.
02 PN PIC 999.
02 UP PIC 99.99 COMPUTATIONAL.
RECORD NAME IS SUPPLIES.
LOCATION MODE IS CALC USING SN-PN,
DUPLICATES ARE NOT ALLOWED.
02 SN-PN.
03 SN PIC X(4).
03 PN PIC 999.
02 QS PIC 9(5) COMPUTATIONAL.
RECORD NAME IS SALES.
LOCATION MODE IS CALC USING ON-PN,
DUPLICATES ARE NOT ALLOWED.
02 ON-PN.
03 ON PIC 9(5).
03 PN PIC 999.
SET DESCRIPTION.
SET NAME IS TRANSACTIONS.
ORDER IS NEXT.
MODE IS CHAIN.
OWNER IS PRODUCT.
MEMBER IS SUPPLIES
MANDATORY AUTOMATIC.
MEMBER IS SALES
MANDATORY AUTOMATIC.

![](/api/attachments/CN65DF62/fulltext/images/fb993194237d7af084a37a93cc3caf920066620a93acd2961c7a5d6468d645b0.jpg)  
Fig. 13. A Different CODASYL Structure for Better Navigation.

For further details, the reader is referred to any CODASYL text. If the above SCHEMA were to be written for a particular DBMS, e.g. IDMS, we would have to supply more detailed specification, quoting the positions of record keys (pointers), etc.

## 5. Conclusion

The essential characteristic of the transition process from files to a data base is that it is a continuous process consisting of an indefinite number of iterations. We can never declare that the development of our data base has ended. The steps in this transition process can be summed up as:

(1) Thorough analysis of reality resulting in the survey of real and abstract entities mapped in corresponding data (records); the increasingly popular and much discussed infological theories are worth mentioning (see ref. [6]);

(2) Normalization of data making use of the analysis;

(3) SET design resulting in the definition of a Global Data Model based on data records in 3NF,

(4) Description of the Global Data Model by means of a DDL, i.e. setting up the SCHEMA;

(5) Description of partial views (maps of) SCHEMA, establishing individual SUB-SCHEMAS.

The Case Study shows the development process used to convert conventional data files to a data base. The process outlined here, however, may not be the only workable method of conversion, and is certainly far from a panacea. The actual conversion will always depend on the contents of the files involved, as well as on the proposed contents and structure of the data base.

Finally, it is important not to forget that data base design is a continuous development process, which is broken into many iterations aimed at improving the overall efficiency.

## References

[1] C.J. Date, An Introduction to Database Organization, (Addison-Wesley Publishing Co., Reading, 1976 (Vol. 1), 1977 (Vol. 2)).

[2] M. Stewart, "How Fourth Normal Form Files Can Be Constructed", Computer Weekly, 9–11–1978: 5–01–1979.

[3] J. Martin, Computer Data-Base Organization (2nd ed.), (Prentice-Hall, Englewood Cliffs, 1977).

[4] G.M. Nijssen (ed.), Modelling in Data Base Management Systems, (North-Holland, Amsterdam, 1976).

[5] F.H. Lochovsky, D.C. Tsichritzis, Data Base Management Systems, (Academic Press, New York, 1977).

[6] B. Langefors, B. Sundgren, Information Systems Architecture, (Petrocelli Books, New York, 1975).
