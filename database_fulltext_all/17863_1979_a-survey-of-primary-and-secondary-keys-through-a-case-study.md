---
otero_id: 17863
otero_key: "SY8ADMHZ"
title: "A survey of primary and secondary keys through a case study"
authors: "Jeffrey A. Hoffer"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90041-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Survey of Primary and Secondary Keys through a Case Study

Jeffrey A. Hoffer

Associate Professor of Management Information-Decision Systems, Department of Managerial Studies, Case Western Reserve University, Cleveland, Ohio 44106, USA

Two fundamental decisions face the designer of a database under an inverted file data base management system: (1) potential primary/secondary key definition and (2) selection among candidate keys for indexing. Functional dependencies and normalization have been defined as ways to construct potential primary keys. This tutorial paper suggests a set of both primary and secondary key types which has been helpful in developing potential keys. This set and the motivation for it are illustrated from an actual business database application. This application is further used to overview the benefits of a database design tool called ASSIST which evaluates alternative, potential keys.

Keywords: Data base design, inverted files, secondary indexes, key types, data base utilities.

![](/api/attachments/SY8ADMHZ/fulltext/images/d9aeb9ea628cab24927ee06ccec74b3d898a8009f746b37a66cdaf044debdf84.jpg)

Professor Hoffer received his B.A. in Mathematics from Miami University in 1969 and his Ph.D. in Operations Research and Computer Science from Cornell University in 1975 and has been on the faculty at Case Western Reserve University since 1973. He is currently an Associate Professor of Management Information-Decision Systems and Assistant Dean for M.B.A. Programs at CWRU. His research interests include the devel opment of decision making aids for the design of computing systems, especially for data base management. He is a past Chairman of the TIMS College on Information Systems and is also actively consulting for several major companies in various aspects of information systems development and management. He is a member of ACM, TIMS and ORSA.

## 1. Introduction

Business data processing applications are increasingly making use of inverted files and secondary indexes for access to databases. Some of the most popular Data Base Management Systems (DBMS) – ADABAS, System 2000, IMS and IDMS – support a multiple-index capability. Minicomputer vendors and software firms have developed similar database technologies for small business systems (e.g., IRIS [7] and DMS-II [3]). Relational DBMS ([5] and [6]) are often implemented using secondary indexes to support query processing (see, e.g., ZETA [9] and INGRES [18]).

The pros and cons of indexes for management of data have been outlined in detail by several authors (see [1] and [16]). Briefly, indexes:

(Pro 1) avoid costly data scanning and sorting;

(Pro 2) efficiently support queries involving multiple keys which are combined by Boolean expressions to define relevant records for processing;

(Pro 3) can reduce programming costs, since record access is via one common mechanism for a variety of record retrieval requirements and consequently programs are more understandable, as well as easier to test and maintain;

(Con 1) require storage overhead for the index entries and require nontrivial maintenance for many business applications involving large and constantly updated databases.

Deciding on what to index is difficult because of the complexities of the above tradeoffs, the potential choices are numerous, and index selection is just one aspect of the whole physical database design problem.

The decision is, however, crucial in many situations, such as in a mini-computer environment, where the power and capacity of the computer system does not permit the “safe” solution – index all fields or data types!

## 1.1. An Example

Cleveland Controls, Inc. (CCI) is a small manufacturing and engineering firm with approximately \$3M annual sales. It is one of the major suppliers of electronic controls and instruments for use in firing industrial boilers. These devices are sold separately and in complete systems. CCI also manufactures a line of diaphragm operated pressure sensing switches and is the leading supplier of these devices to the heating, ventilating, and air conditioning industry as well as the whole air handling industry.

![](/api/attachments/SY8ADMHZ/fulltext/images/5e3ca5996c498dc6e307bcbcdf684258b7df6a7802fd9dd955880caa9c938db9.jpg)  
Fig. 1. Order Tracking Logical Database Schematic.

In 1974 CCI installed a Date General NOVA-III minicomputer with a time-sharing operating and data management system IRIS [7,8]. The data management methods of IRIS include a multiple indexing capability with the only restriction that each key value for a given key must be unique. A key may be constructed under program control on any data or combination of data. Since 1974 CCI has computerized general ledger, some aspects of production scheduling, physical inventory counting and customer order tracking (among others). Figure 1 is a general schematic for the database to support customer order tracking. To track customer orders, eight different (logical) files are required. Selected contents (attributes) for these files are also depicted in Figure 1.

Customers, many of whom are manufacturing representatives or general engineering contractors, often have several ship-to-addresses: this has necessitated the creation of a separate logical ship-to-address file. Customer orders may have a variable number of "line items"; partial shipments and multiple line items may be shipped at the same time. Completely shipped (or "closed") orders are summarized in a separate file. As shown, Figure 1 implies that certain linkages between files will exist irrespective of the indexes chosen. For example, all the ship-to-addresses for a given customer can be found by following an access path beginning in the customer record and traversing through all associated address records.

There was rather quick agreement on Figure 1 and the contents of these files (the functional specifications were devised by a team of CCI personnel and external consultants). However, there was much less consensus on what should be used as primary and secondary keys. Consensus was difficult for two reasons:

(1) All persons on the project had their own notions on what types of keys could be constructed;

(2) It was not obvious, when discussing a proposed key, whether the storage and maintenance of the key would be more costly than the savings in retrieval.

The remainder of this paper will concentrate on a list of primary and secondary key types which was developed out of the discussions on the order tracking database. Section 3 will review some experience with an index evaluation utility (documented more full in [10–12]), which was also used for this application. The paper concludes with some general remarks on the design of databases.

## 2. Potential Key Types

This section discusses eleven different types of keys resulting from the customer order tracking system; we believe that these are useful in other data processing applications. It should be emphasized that this list of key types is not necessarily exhaustive; rather, it represents a wide range of key types synthesized from data processing applications at CCI and elsewhere.

(1) Single attribute identifier: This type of key corresponds to a single, primary key on the records in a file. The Customer account number in the Customer Master file and the Order number in the Customer Order Header file are examples of this type of key. Although it is the most common, there is no requirement (under IRIS) that it must be indexed. For example, if there is no program which requests ship-to-addresses based upon the entry of a particular (partial) address, there is no need to create an index on this single attribute identifier type key.

(2) Partial attribute: Many character strings are too long to use all characters for the key value. Customer name, Customer purchase order number and Catalog number are examples of such attributes. Although n selected characters of the attribute value may not guarantee a unique key value within an index, a set of n carefully chosen characters can be very discriminating. For example, the first 8 characters of the Customer name could be a useful partial attribute key for at least three reasons:

a) Beginning characters rather than middle or trailing characters of the name often are useful in resolving spelling errors upon entry (i.e., the first few characters often are more distinguishable and retained by human memory. The only potential problem is in abbreviations such as "A.B. Dick," which could also be "A B Dick" or "AB Dick").

b) Beginning characters can be used to find similar objects, such as customers, all of whom are subsidiaries of the same parent company since it is likely that the name of each subsidiary begins with the parent company's name.

c) This type of key in an index can approximate the ascending sorting order of the Customer name, which may be useful in certain reporting functions.

(3) Concatenated attributes: There are five different subtypes of concatenated attribute keys:

(3.1.) Unique value requirement: Several situations can arise where one is forced to combine two (or more) attribute values together to guarantee uniqueness. $^{1}$ One such situation was identified above, where more than one partial Customer name key might take on the same value. In this case, the first 8 characters of the Customer name must be suffixed with a character string to guarantee uniqueness. Two choices are readily available. One is the primary record key, Customer account number. Another is the physical record number. Each has its advantages. First, the lengths of the primary key and record number must be considered, since it is desirable to minimize the length of keys. Second, the primary key is itself useful information; if we want to know the Customer account number for a given customer identified by name, this query can sometimes be satisfied strictly by information within the index. Third, the physical record number as a suffix may be advantageous since keys with the same first 8 characters can be sorted in the index into ascending order by physical location; this can facilitate rapid data retrieval.

A second situation which forces this type of key is a logical secondary key such as the Promised delivery date in the Open Line Items file. Here there can be many ordered items which have been promised delivery on the same day, and a suffix may be necessary to guarantee key value uniqueness. Another example of this same situation can arise when implementing a one-to-many (1:M) relationship between two files. The relationship between a Customer Master record and its associated Customer Order Header records can be implemented using this type of key to create a Customer account number index on the Customer Order Header file.

(3.2) Multiple attribute identifier: Sometimes when one record (A) is dependent upon another (B), the unique identifier for record A is composed of the unique, primary key (or, more generally, some identifier) of record B plus some data from record A. Consider, for example, Open Line Item records. Here each record is distinguished by (at least $^{2}$ ) a joint or dual attribute key of Order number and Part number. The order in which these component keys are concatenated is immaterial in guaranteeing uniqueness, but the order does matter for efficient retrieval. For example, the sorting order of keys in the index, which is dictated by the order of concatenation, could imply that it is more efficient (or, in the extreme, feasible) to find all the parts (line items) for a given order, when the key is (Order number, Part number), or to find all the orders for the same part, when the key is (Part number, Order number). In fact, one may want to implement two indexes, one for each.

(3.3) Efficient retrieval: Inverted file structures are usually applied in situations where requests for data involve selecting records based upon Boolean expressions using some of the data. For example, one user of the database in Figure 1 could request to see all Open Line Item records with a given Part number AND with a specified Promised delivery data (possibly because of a discovered delay in the production of a given product). Although this request can be processed in several different ways, one way would be to use two indexes, one on Part number - possibly the (Part number, Order number) index mentioned previously - and another on the Promised delivery date. Two lists of record numbers would be constructed, one each for the records that satisfy the two data qualifications. Then the two lists would be intersected to identify which records satisfy both qualifications. This method, however, requires computer time to construct and match two lists. A possibly $^{3}$ more efficient scheme would be to have one index on the concatenated key Part number, Promised delivery date; this would eliminate the need for list intersection.

Another reason is to avoid access to records when the question involves only the existence of data. For example, the concatenated key of Part number, Promised delivery date can be used to answer the question "Is there an order for part 123 to be delivered anytime within the next week?"

(3.4) Intra-file relationships: Two cases arise in Figure 1 where a concatenated key index can be used to implement a relationship within the same file. The first case involves the use of the attribute Head office account number to relate subsidiaries of the same firm. Here a concatenated key of parent firm Customer account number, subsidiary firm Customer account number would support this relationship; a key using the parent firm Customer account number and some unique suffix would also work. The same relationship could also be implemented via pointers imbedded in the Customer Master records; these could chain subsidiaries via a ring structure.

The second case is an extension of the Item Master file to support bill-of-materials (B/M) and where-used (W/U) relationships among items (parts, components, and products). Here are index with keys composed of

(B, parent Part number, component Part number)

for the B/M and

## (W, component Part number, parent Part number)

for W/U can support product structure. Actually, either one or two indexes (one for the B/M relation and one for the W/U relation) are possible. Further, since the quantity of the component item is also usually of concern, such indexes might need is to be applied to an additional file of records which only contain quantities (i.e., the quantity record for a given key value indicates the number of units of the component needed to make the parent). The next type of key could be used to eliminate this additional file at the expense of extra storage space in the index.

(3.5) Information carrying: In IMS [14] record segments which are used to relate two record segments can have “intersection data” or data that pertains to the relationship but not to either record by itself. Quantity in the product structure illustration is intersection data. This data need not be located in a separate record but can be part of the concatenated key. For example, the keys outlined above can be appended with the quantity, thus eliminating the separate quantity record access. However, increased storage is required, since the quantity must now appear in each key whereas previously one quantity record could be shared by all keys for parent and components that have the same number of components per parent. Also, if there is more intersection data than quantity (e.g., some type of manufacturing instructions), the separate record may have to be accessed.

(4) Null value: Although it may seem that keys must have a non-trivial value, there are several cases where this is not true. One example is for missing data; it is possible that orders can be entered without specifying a Promised delivery date. An index can be used to point to those records with a null date. In this instance, the logical key is implicit, but the physical key in the index may be the physical record number or some program generated sequence number necessary to satisfy a key uniqueness requirement within an index.

In general, an index for this type of key is used to identify records which have a common characteristic; i.e., (implicit or explicit) values for one or more attributes. The characteristic may be a common (concatenated) value or a range of (concatenated) values. In the latter case, different values within the range need not be distinguished in the index. Figure 1 also shows orders with a Promised delivery date of 'RUSH' or records in the Customer Order Header file which represent the details of "closed" orders. Wong and Chaing [19] referred to such a set of records as an atom and suggested creating indexes for each atom.

(5) Records from several files: Since Figure 1 depicts the order tracking logical database, the Item Master file (because it contains part, subassembly and assembly items) might actually be implemented as three separate physical files. This might be advisable if the formats for these three record types are different; e.g., in record length. Even if three physical files are used, one common index is sufficient. In this case, the index entry, composed of the pair (key value, record address), must be able to indicate to which physical file the record address applies. Possibly part or item numbers are assigned so that parts, components, and final assemblies are distinguishable. Otherwise, some character must attached to either the key or record number to indicate the relevant file. Another example of the use of one index to access several files occurs when a given logical record is segmented (see [13]) into several physical subrecords. For example, an Item Master record might contain engineering, sales, accounting, and production data. Due to the nature of data processing, it may be more efficient to break the record into four parts, one for each of the four categories of data. Each file, however, can be designed so that physical subrecords of a given item are in the same relative position in each "subfile." In this case, one index (using relative record number pointers) can be used to access all four files.

(6) Audit or change: Monitoring changes to values in the database may be important. For example, the event of changing a Promised delivery date may trigger replanning of production. Besides any structures to support database recovery, the production scheduler may, therefore, want Order Line Item records "flagged" if the Promised delivery date is changed. This "flagging" can be accomplished in two ways. One is to create a separate null value index that simply catalogs changed records (i.e., record after images) or a concatenated key index could be constructed using the date of the change concatenated with a unique suffix. A second way, possible when only an indication of the change is required, uses an existing primary index. As an example of this approach, an (Order number, Part number) key for a changed record could be prefixed with a '1' and keys for records that have not changed (since the last review) with a '0'. This quickly identifies changed records using very little additional index space. Such a method does, however, force many programs to check for either a '0' or '1' prefix, which complicates programming. Also, when more than one change occurs between change reviews, all but the effects of the last change will be lost.

(7) Sorting: Keys may be created in permanent or temporary indexes simply to satisfy report sort order. For example, the Customer Master File might be indexed on a concatenated key using zip code to support the production of mailing labels to meet bulk mailing reduced rate restrictions. A temporary index might be used to key sort report line images for a report being spooled onto disk when the record input sequence (say physical sequential or via the primary key index) is different from the record reporting sequence. An example is a one-time or very infrequent open order status summary in ascending catalog number order when line items are permanently indexed only on Part number and not on Catalog number.

We have now reviewed a wide variety of types of potential keys. As indicated previously, after enumerating potential keys the database design team debated which of the potential keys were cost effective to implement. Although the decision was finally made using subjective analysis, an index selection system was developed to assist in future decisions.

## 3. Selection among potential keys

A key enumeration process based upon the taxonomy of potential key types leads to a long list of potential keys. It has been suggested by some practitioners and researchers that it is best to index all potential keys until actual database activity can be measured. Yet, that decision is not useful when one has found all potential keys since these keys will be redundant and indexing all will degrade database performance due to the excessive maintenance of indexes. Such redundancy exists because an index on one potential key can support the same activity of another potential key. A simple example is found in using the partial attribute key on Customer name in Figure 1. Two possible choices are the first 8 characters and the first 10 characters. Both are not needed!

In order to extend intuition and experience from guess-work to a systematic evaluation, an experimental inverted database modelling package has been developed. This package, called ASSIST (Automated System of Secondary Index Selection Techniques) specifically models indexes under IRIS. The reader should refer to references [10-12] for more details on ASSIST.

ASSIST is a set of twenty-three IRIS BASIC interactive programs. The first twenty-two of these are data entry and modification programs which maintain eleven different types of parameter files for defining an index selection problem. These parameters pertain to the definition of eight types of application programs which access a database, characteristics of the computer hardware and storage devices, statistics on operating system data access routines, constraints on response time and turnaround for the application programs and suggested indexing solutions.

The twenty third program in ASSIST evaluates the performance of a specified indexing solution. Using the parameter files as input, this program interactively reports (i.e., as the results are calculated) various performance measures:

(A) Time/cost for each application program (both predefined and ad hoc inquiry programs can be defined);

(B) Index storage space/cost;

(C) Time and space constraint values;

(D) A composite objective function, which is a specified sum of application program and space costs.

ASSIST has been used in graduate course in a School of Management to select indexes for the Customer order tracking database. Participants were a mix of full-time students and practicing data processing professionals. The project began with an information requirements study and a logical database design. Each student was then responsible for selecting their own keys and indexes and then were asked to repeat the design using ASSIST to evaluate alternatives.

Several observations can be made based upon this experience:

(1) All designers did not obtain the same solution. This was due to different assumptions of each designer leading to different parameter values and also due to the individual intuitive approaches. Often the differences resulted from different sets of potential keys, especially of the Partial attribute type; some designers ignored certain key types. This result reinforced the need for a key taxonomy (as developed in Section 2). Varying assumptions on application program design also led to different results.

(2) The users spent considerable time, by their own choice, on terminals (9–12 hours) entering parameters, executing and reexecuting alternative indexing solutions and at a desk (20–35 hours) analyzing results. The model itself executes in less than one minute of CPU time in interpretive IRIS BASIC.

(3) The users stated (after using ASSIST) that they had a much better appreciation for the influential factors in index definition and selection.

(4) The users each developed their own forms for recording parameter values and indicated that a vast majority of their time was spent in specifying values and in data entry. This suggests that additional tools, such as a Data Dictionary/Directory [2] or those described by Clark and Hoffer [4] for collection of database statistics, could feasibly permit the careful design of larger databases.

(5) Some users found that they could not conceive of any better indexing solution using ASSIST than they had constructed manually. Others showed as much as a 40% improvement.

## 4. Summary and Conclusions

This paper has reviewed, based upon an actual database application, the two major components of selecting keys for indexing in inverted file database management systems: potential key enumeration and evaluation of alternative keys. A list of eleven types of keys was introduced and it was suggested that this list can facilitate construction of potential keys. Finally, experience with an interactive inverted file design evaluation utility, ASSIST, was reviewed to indicate one systematic approach for evaluating alternative keys.

In conclusion it should be observed that index selection is only one aspect of a multi-decision, multi-criteria problem of database design. Few tools, like ASSIST, exist for the data resource decision maker. A few uncoordinated tools for database structure evaluation [15], record content specification [4,13], data inventory analysis [2]. and specific design aspects of particular commercially available DBMS [17] have been developed. However, these must be suitably expanded and integrated to provide the data resource manager with decision making tools similar to those which have been developed for production and investment management.

## References

[1] H.D. Anderson and P.B. Berra, Minimum Cost Selection of Secondary Indexes for Formatted Files, ACM-TODS, 2,1 (March, 1977), 68–90.

[2] British Computer Society, Data Dictionary Systems Working Party Report, Data Base, (Fall, 1977).

[3] Burroughs Corp., B-1700 Systems Data Management Systems II: Reference Manual, Mark V.5 Release, (January, 1976).

[4] J. Clark and J.A. Hoffer, A Procedure for the Determination of Attribute Access Probabilities, 1978 SIGMOD – Conference Proceedings (1978), 110–117.

[5] E.F. Codd, A Relational Model of Data for Large Shared Data Banks, CACM, 13, 6 (June, 1970), 377–387.

[6] C.J. Data, An Introduction to Database Systems, Second Edition, Addison-Wesley Publishing Co., (Reading, 1977), Chapters 4–11.

[7] Educational Data Systems, IRIS USER REFERENCE MANUAL (EDS 1017-4), (1974).

[8] Educational Data Systems, IRIS Business Basic Programming Manual, (EDS 1016), (1974).

[9] J.H. Farley and S.A. Schuster, Query Execution and Index Selection for Relational Data Bases, Proc. of the First International Conference on Very Large Data Bases (September, 1975), and Technical Report CSRG-53, Computer Systems Research Group, University of Toronto (March, 1975).

[10] J.A. Hoffer, Automated System of Secondary Index Selection Techniques: ASSIST, Users' Manual, Department of Managerial Studies, Case Western Reserve University, (1978).

[11] J.A. Hoffer, Selection of Secondary Indexes in a Mini-computer Environment, Department of Managerial Studies, Case Western Reserve University, (1978).

[12] J.A. Hoffer, Index Key Selection, (Q.E.D. Information Science, Inc., Wellesley, Mass, 1979).

[13] J.A. Hoffer, and D.G. Severance, The Use of Cluster Analysis in Physical Data Base Design, Proc. of the First International Conference on Very Large Data Bases (September, 1975), 69–86.

[14] IBM Corp. Information Management System/Virtual Storage System/Application Design Guide, IBM Form No. SH20-9025.

[15] S.T. March, Models of Storage Structures and the Design of Database Records Based Upon a User Characterization, Ph.D. Dissertation, Dept. of Operations Research, Cornell University, Ithaca, N.Y., (1978).

[16] J. Martin, Computer Data-Base Organization, Second Edition, Prentice-Hall, Englewood Cliffs, 1977).

[17] N. Raves and G.U. Hubbard, Automated Logical Data Base Design: Concepts and Applications, IBM Systems Journal, 16, 3 (1977), 287–312.

[18] M. Stonebraker, et al., The Design and Implementation of INGRES, ACM-TODS, 1,3 (September, 1976), 189–222.

[19] E. Wong and T.C. Chaing, Canonical Structures in Attribute Based File Organization, CACM, 14, 9 (September, 1971), 593–597.
