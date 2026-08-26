---
otero_id: 22571
otero_key: "RAYKYAGJ"
title: "A scenario-based object-oriented hypermedia design methodology"
authors: "Heeseok Lee; Choongseok Lee; Cheonsoo Yoo"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(99)00011-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A scenario-based object-oriented hypermedia design methodology

Heeseok Lee $^{*}$ , Choongseok Lee, Cheonsoo Yoo

Corporate Information System Laboratory, Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-43, Chongryangri-dong, Dongdaemun-ku, Seoul, South Korea, 130-012

Received 1 March 1998; accepted 16 January 1999

## Abstract

This paper defines an object-oriented methodology for developing hypermedia information systems. The methodology consists of six phases: domain analysis; object modeling; view design; navigation design; implementation design; and construction. Users' requirements are analyzed with a responsibility-driven technology using scenarios. Object-oriented views are generated as the result of object modeling, and then used for the subsequent navigation and implementation design. The implementation design phase deals with database schema, page structure and flow, and user interface. This methodology integrates enterprise databases with distributed hypermedia systems via Internet, Intranet, or Electronic Commerce. © 1999 Elsevier Science B.V. All rights reserved.

Keywords: Scenario; Object; Hypermedia; Intranet; Design methodology

## 1. Introduction

Hypermedia information systems allow users to share information through a variety of media such as text, video, image, and voice. Hypermedia systems can be widely used for world wide web (WWW) applications via Internet or Intranet $[1, 2, 5]$ . Furthermore, hypermedia services are already adding incremental value on the business-to-business arena for electronic commerce (EC).

Hypermedia extend the hypertext paradigm into multimedia. Hypertext is a nonsequential way of looking at text-based information. Even though manuals, books, reports, or some other documents may be stored within a computer system sequentially, hypertext provides an interface so that any number of nonsequential links may allow a user to access an item of interest elsewhere. Instead of navigation among text objects, hypermedia offer links among the whole spectrum of multimedia information [21].

Hypermedia development, especially on a commercial scale, often involves teams of developers who need to be managed and coordinated over an extended period of time. Formal systems development and project management techniques are needed to ensure that the hypermedia product meets its objectives, and is completed on time and within budget $[11]$ . Therefore, it is not surprising to note that the research for hypermedia development methodologies is active (e.g. HDM $[6, 7, 8]$ , EORM $[13, 14, 15]$ , RMM $[10, 11, 12]$ , and OOHDM $[18, 19, 20]$ ).

Hypermedia design method (HDM) provides a formal model for hypermedia applications. It is

based on an object-oriented technique that encourages the use of different perspectives in presenting the same conceptual entity. Enhanced object relationship model (EORM) is the first object-oriented hypermedia design methodology. EORM consists of three frameworks: class; composition; and graphical user interface (GUI) frameworks. Relationship management model (RMM) uses entity-relationship (E-R) abstractions; it enhances HDM by the use of additional access structures (conditional indexes and guided tours). RMM phases include E-R design, slice design, navigation design, conversion protocol design, user-interface design, runtime behavior design, and construction/testing. Object oriented hypermedia design model (OOHDM), another object-oriented methodology, adopts four design phases such as conceptual design, navigation design, abstract interface design, and implementation. A view based hypermedia design methodology (VHDM) has been proposed by Lee et al. [16]. Views are used to represent users' perception of hypermedia requirements. VHDM facilitates exploring the functionality of views in hypermedia applications.

![](/api/attachments/RAYKYAGJ/fulltext/images/b6525fe49843c238be8756f8b02688fccca23e92166964efdf802263782c936e.jpg)  
Fig. 1. SOHDM framework.

Table 1
Event list

Previous methods have several weaknesses. First, they employ relationships among data for determination of navigational paths. These data-oriented relationships in isolation may not reflect users' navigational requirements satisfactorily. Second, the integration of hypermedia with enterprise database is not sufficiently emphasized, in view of its importance for Intranet implementation. Third, research in the past adopts conceptual data models to capture users' requirements. Those models may not provide the flexibility that hypermedia systems require.

To solve such problems, this paper develops a scenario-based object-oriented hypermedia design methodology (SOHDM). The paradigm of object orientation should extend to the hypermedia development environment as a whole. SOHDM identifies requirements for hypermedia applications from the beginning of system development. Scenarios are used to enhance the expressive capability of modeling. In particular, object-oriented views are used as navigational units as well as logical user views.

## 2. A hypermedia design methodology

SOHDM consists of six phases: domain analysis; object modeling; view design; navigation design; implementation design; and construction. The framework of SOHDM is depicted in Fig. 1. For the purpose of clearer presentation, feedback among phases is not depicted. However, it is important for refining analysis or design outputs in each phase.

In the domain analysis phase, a context diagram is drawn to represent the system boundary. In addition, scenarios are employed to identify users' requirements. The scenarios result in an object model within the framework of class responsibilities collaboration (CRC). For better representation of relationships among object classes, a class structure diagram (CSD) is drawn. In the view design phase, object-oriented (OO) views are extracted from CRC cards. OO views are navigational units in the navigation design.

The navigation design phase defines access structure nodes (ASNs) and navigational links. ASN contains the access structure and path to OO views. For the sake of convenience, navigational links are presented in the form of a navigational link matrix.

Implementation design phase defines users' windows (e.g., a set of HTML pages) and navigational flows from one page to another page. In addition, detailed user interfaces (UIs) are designed. OO views may be transformed into relational database schema. Clearly, database independence is guaranteed. Finally, a hypermedia information system is built, which depicts the resulting physical database schema and UI specifications.

## 3. SOHDM: a case and details

## 3.1. Domain analysis

First, a system scope diagram is drawn to delimit the hypermedia system to be developed. A well-known data flow diagram (DFD) [22] is used. Typically, a context diagram (e.g., zero level DFD) is a good alternative. For the design of a bank accounting system, the system scope diagram is drawn as shown in Fig. 2. This system has three external entities: management; customer; and branch.

Events are identified for each external entity. An event is the trigger which starts the system. Five events are shown in Table 1.

SOHDM uses scenarios to identify hypermedia applications requirements from the earliest opportunity. Scenario activity charts (SACs) are developed to describe scenarios. SAC describes business processes according to actors. An actor is an operator of specific activities, i.e., a creator of events. Notation of SACs is given in Fig. 3. External entities are the primary candidates for actors in SACs. An event is a starting point, a trigger of a scenario. An activity is an operation by which an actor completes a scenario. An alternation is an activity which enables for an actor to choose the next activity. An activity flow is a sequence of activities. Termination is the end of a scenario.

<table><tr><td>Source entity</td><td>Event name</td></tr><tr><td>Branch</td><td>Request branch total informationRequest customer information</td></tr><tr><td>Customer</td><td>Check accountIdentify banking product type</td></tr><tr><td>Management</td><td>Request management total information</td></tr></table>

![](/api/attachments/RAYKYAGJ/fulltext/images/796e43d738d644bad34b194a0678c6b2ffcaf7d1c5732c520ffb14e5bccdde6a.jpg)  
Fig. 2. System scope diagram.

![](/api/attachments/RAYKYAGJ/fulltext/images/2871c5262fc2d48327be7334ef47dbda3a80af509c560e9f85286c3fca1bd632.jpg)  
Fig. 3. Notation of SAC.

Five SACs are generated from the five events. For the sake of simplicity, three scenarios are illustrated in Figs. 4–6.

## 3.2. Object modeling

Scenarios in SACs are used for object modeling. Scenarios are transformed into objects in the form of CRC cards. The CRC cards are adopted because they have attractive informal appeal that helps make complex modeling tractable.

![](/api/attachments/RAYKYAGJ/fulltext/images/f21baf511bec533ca478a55a46b96e1ea3d6f006a954b143c4309dff9473e493.jpg)  
Fig. 4. ‘Check account’ scenario.

![](/api/attachments/RAYKYAGJ/fulltext/images/ef1bcbdfa8555be513df11497d1e68256c5662083918cfd44bd49dc2c3a2a92a.jpg)  
Fig. 5. ‘Request customer information’ scenario.

Objects are generated from scenarios as follows:

1. Actors are primary candidates for objects; then activities are considered. Scenarios generate object candidates, such as current customer, prospective customer, account, branch, and transaction. In particular, another object, customer, a superset of current customer and prospective customer is defined.

2. Objects identified are documented in formatted index (CRC) cards. These include attribute lists and associators. In addition, cardinality of association is depicted (in a bracket). The cards may be specified repeatedly for refinement. Six object classes (Customer, Current\_Customer, Prospective\_Customer, Account, Branch, and Transaction) are modeled as shown in Fig. 7. For example, in the Current\_Customer CRC, the superclass is Customer. Current\_Customer class inherits the attributes and responsibilities from Customer class. It has Current\_Customer\_Initial\_Date as an attribute and Check\_Account\_Balance and Check\_Transaction as responsibilities.

Four types of relationships are depicted in CRCs (superclass/subclass, collaborators, components, and associators). To present these relationships more effectively, a CSD (Fig. 8) may be prepared.

![](/api/attachments/RAYKYAGJ/fulltext/images/b255425d0593318ccddb36d3806bab41ab39c2d25a196865639302c7c1b9dc4a.jpg)  
Fig. 6. ‘Request branch total information’ scenario.

<table><tr><td>Class : Customer</td><td>Superclass :</td><td>Class : Current_Customer</td><td>Superclass : Customer</td></tr><tr><td rowspan="3">Attributes:Cust_IdCust_SSNCust_NameCust_JobCust_RankCust_SdateCust_BdateCust_PhoneCust_ZipCust_AddrCust_CreditCust_Asset</td><td>Subclass:Current_CustomerProspective_Customer</td><td rowspan="3">Attributes:Cur_Cust_Initial_Date</td><td>Subclass :</td></tr><tr><td>Collaborators:</td><td>Collaborators:AccountTransaction</td></tr><tr><td rowspan="2">Components :</td><td>Components :</td></tr><tr><td rowspan="2">Responsibilities:Know_CreditKnow_Customer_Information</td><td rowspan="2">Responsibilities:Check_Account_BalanceCheck_Account_TransactionKnow_Current_Customer</td><td rowspan="2">Associators:Account (N)Branch (N)</td></tr><tr><td>Associators:</td></tr><tr><td>Class : Prospective_Customer</td><td>Superclass : Customer</td><td>Class : Branch</td><td>Superclass :</td></tr><tr><td rowspan="3">Attributes:Meeting_Memo</td><td>Subclass :</td><td rowspan="3">Attributes:Bran_CodeBran_NameBran_AddrBran_Phone</td><td>Subclass :</td></tr><tr><td>Collaborators:</td><td>Collaborators:AccountCurrent_CustomerProspective_Customer</td></tr><tr><td rowspan="2">Components :</td><td>Components :</td></tr><tr><td rowspan="2">Responsibilities:Know_Meeting_Memo</td><td rowspan="2">Responsibilities:Check_Account_Type_TotalCheck_Current_CustomerCheck_Prospective_CustomerKnow_Branch_Total</td><td rowspan="2">Associators:Account (N)Current_Customer (N)Prospective_Customer (N)Transaction (N)</td></tr><tr><td>Associators:Branch (1)</td></tr><tr><td>Class : Account</td><td>Superclass :</td><td>Class : Transaction</td><td>Superclass :</td></tr><tr><td rowspan="3">Attributes:Acct_NoAcct_BalanceAcct_Reg_DateAcct_Type</td><td>Subclass :</td><td rowspan="3">Attributes:Trans_CodeTrans_DateTrans_TypeTrans_Amount</td><td>Subclass :</td></tr><tr><td>Collaborators:Transaction</td><td>Collaborators:</td></tr><tr><td rowspan="2">Components :</td><td>Components :</td></tr><tr><td rowspan="2">Responsibilities:Check_TransactonKnow_Balance</td><td rowspan="2">Responsibilities:Know_Transaction</td><td rowspan="2">Associators:Account (1)Branch (1)</td></tr><tr><td>Associators:Branch (1)Current_Customer (1)Transaction (N)</td></tr></table>

Fig. 7. CRC cards.

![](/api/attachments/RAYKYAGJ/fulltext/images/2c325292d197cb5c329d21ae8e19e2d1b0382ddb2256a8e882031f92b4dd8764.jpg)  
Fig. 8. Class structure diagram.

## 3.3. View design

In the view design phase, objects are reorganized for navigational units. A navigational unit represents an OO view. The use of views in hypermedia application design has several advantages. First, views can support a number of users who have different requirements. Second, cognitive overhead can be effectively reduced, because heterogeneous attributes and responsibilities of objects are grouped into views. Third, hypermedia applications are easily extendable, since additional requirements of presentation or navigation can be accommodated.

We can extract OO views on the basis of responsibilities and attributes in CRC cards as well as their relationship in CSD. OO views are categorized into three types: base view; association view; and collaboration view. A base view is generated from a single object class. An association view is extracted from an association relationship. Similarly, a collaboration view is generated from a collaboration relationship.

![](/api/attachments/RAYKYAGJ/fulltext/images/d59ba461473280df5663cd7f9a6c2b8196d12e062699f1e066744f5440cebc4e.jpg)  
Fig. 9. Generating object oriented views.

In Fig. 9, the Current\_Customer\_View, a base view, is a subset of attributes and responsibilities in the Current\_Customer class. Branch\_Prospective\_Customer\_View, an association view, uses attributes and responsibilities in Branch class and Prospective\_Customer class. The origin of responsibilities for association views differs from that for collaboration views. In an association view, the responsibilities related with attributes are extracted. However, in case of a collaboration view, the responsibilities required for collaboration are of importance.

## 3.4. Navigation design

The navigation design phase deals with the manner in which users gather and use information on the basis of scenarios. In well-designed hypermedia applications, the way users explore the hypermedia is an important design issue, in order to avoid redundant information and prevent them from getting lost in the hyperspace. Past studies base the navigation design on data models in isolation. However, we suggest that the use of scenario as well as data model should improve the quality of the navigation design.

In navigation design, OO view and access structure node (ASN) are adopted for navigational units.

ASN is used to implement the grouping, which allows users to access other parts of hypermedia documents in RMM. ASN provides users the access structures which users can use to navigate to different or detailed part of hypermedia application.

The first step in the navigation design phase is to determine ASNs by using scenarios; flows that start from the system to the actor are the primary concern for determining ASN. An alternation or activity includes two types of activity flows, such as inflows and outflows. An activity inflow may become an ASN. An activity outflow may be the input fields of the ASN, and activity outflows from an alternation may be the menu of the ASN.

For example, in the ‘Request Customer Information’ scenario, the activity flow from ‘Categorize Request’ to ‘Request Customer Type’ may be an ASN entitled ‘Customer.’ The activity outflows from ‘Request Customer Type,’ such as ‘Current Customer’ and ‘Prospective Customer’ may be menus of the ASN. ‘Customer’ ASN has two menus, ‘Current Customer’ and ‘Prospective Customer.’

Next, navigational links are built. The ANS differs from OO view in that ASN contains only access paths to OO views, but OO view contains the actual information that users want to obtain. These OO views and ASNs correspond to nodes. HTML pages are implemented on the basis of these OO views and ASNs in the subsequent implementation design. A

![](/api/attachments/RAYKYAGJ/fulltext/images/121346bfac51d3b2617373384134b9379a7137b9d47b3200c52f8c5a2e0a7aaf.jpg)  
Fig. 10. Navigational link.

![](/api/attachments/RAYKYAGJ/fulltext/images/2b50cc0235353dd87c71766567de4775b4b2fa490e25de759a1180c0bf53f6e6.jpg)  
If the navigational unit in the first column is source, and the navigational unit in the first row is target.  
If the navigational unit in the first row is source, and the navigational unit in the first column is target.  
If the navigational unit in the first column and the navigational unit in the first row are bi-directional.

Fig. 11. Navigational link matrix.

link denotes the relationship between source and target node. This source and target node may be OO view or ASN.

ASNs are found from the scenarios and then navigational links are determined, as shown in Fig. 10, which shows that the navigational units are categorized into three separate groups, as indicated by dotted lines. Each group is separated from others because it has no related information, i.e., does not have any navigational link that leads to other groups. For the sake of convenience, links may be summarized in a form of a navigational link matrix. This matrix is shown in Fig. 11.

## 3.5. Implementation design

The next phase generates page structure, page flow, user interface, and logical database schema for construction in a particular development environment. Hypermedia application can be developed under a variety of system environments, including different DBMSs, and development tools such as CGI, HTML, Java [9], or Shockwaves. However, it is noted that our implementation design phase is independent of different environments.

First, the HTML page schema is designed by the organization of OO views, ASNs, and description details (text, image, sound, etc.). Fig. 12 shows an example of the page schema. For example, the page ‘Current\_Customer\_001’ entitled ‘Current\_Customer’ is based on two views, Current\_Customer\_View and Account\_Transaction\_View. It has two anchors that lead to ‘Main\_001’ and ‘Prospective\_Customer\_001’ pages.

Page schema in Fig. 12 is enhanced to user interface (UI) specifications by the use of UI components. Fig. 13 summarizes the notation for UI components. A caption is a text displayed in a component. An action is an interactive procedure. An action is executed when a component is clicked. Items are a set of data included in a component. The key-based transition refers to the current state of the components, while the simple transition does not.

<table><tr><td>PID :Main_001</td><td>Title : Main Menu</td></tr><tr><td colspan="2">•Views</td></tr><tr><td colspan="2">• DescriptionDescription of Main Menu</td></tr><tr><td colspan="2">•AnchorCurrent Customer / Current_Customer_001Prospective Customer / Prospective_Customer_001Management Information / MIS_001</td></tr><tr><td colspan="2">• Other ComponentLogo</td></tr><tr><td colspan="2"></td></tr><tr><td>PID : MIS_001</td><td>Title : Management Information</td></tr><tr><td colspan="2">•ViewsBranch_Account_View</td></tr><tr><td colspan="2">• DescriptionDescription of Management Information</td></tr><tr><td colspan="2">•AnchorMain Menu / Main_001</td></tr><tr><td colspan="2">• Other ComponentLogo</td></tr><tr><td colspan="2"></td></tr><tr><td>PID : Current_Customer_001</td><td>Title : Current Customer</td></tr><tr><td colspan="2">•ViewsCurrent_Customer_ViewAccount_Transaction_View</td></tr><tr><td colspan="2">• DescriptionDescription of Current Customer, and Help Message.</td></tr><tr><td colspan="2">• AnchorMain Menu / Main_001Prospective Customer / Prospective_Customer_001</td></tr><tr><td colspan="2">• Other ComponentLogo</td></tr><tr><td colspan="2"></td></tr><tr><td>PID : Prospective_Customer_001</td><td>Title : Prospective Customer</td></tr><tr><td colspan="2">•ViewsBranch_Prospective_Customer_View</td></tr><tr><td colspan="2">• DescriptionDescription of Prospective Customer, and Help Message.</td></tr><tr><td colspan="2">• AnchorMain Menu / Main_001Current Customer / Current_Customer_001</td></tr><tr><td colspan="2">• Other ComponentLogo</td></tr></table>

Fig. 12. Page schema.

ASNs determine the UI components. ASNs are transformed into HTML pages or anchors. Direct links correspond to buttons or images. Index, direct query, or indexed query is transformed into a choice or a list. Guided tour is transformed into a slide bar or buttons with 'Next' or 'Previous.' Fig. 14 shows the resulting UI specifications for the 'Current\_Customer\_001' page schema.

![](/api/attachments/RAYKYAGJ/fulltext/images/42a4735a59c5a88117524d96dafb5b2187c2b072f67d8564fce2c2c2a6e72460.jpg)  
Fig. 13. Notation of user interface component.

Next, object model is transformed to logical database schema. The transformation may not be necessary if OODBMS is used. In many real-life cases, however, relational DBMS are the most useful systems. Here, designers need rules that map object model into relational schema. The transformation rules can be found in Ref. [3] or [4]. We adapt Blaha's rule as follows:

First, each class is transformed into one table. Second, a generalization relationship is transformed into one superclass table and multiple subclass tables. Third, many-to-many relationships are transformed into distinct tables. Finally, one-to-one and one-to-many relationships are transformed into distinct tables or merged with a participating class. In addition to these rules, another transformation rule is considered for the collaboration relationships of our CRCs. Additional views or stored procedures may be required for these collaboration relationships. Transforming collaboration relationship into view is depicted in Fig. 15.

Transforming CRCs in Fig. 7 results in 10 tables, as shown in Table 2.

## 3.6. Construction

In the construction phase, developers implement a physically running hypermedia application system in target environments. All of the products during the implementation design phase should be mapped to physical elements, as shown in Fig. 16. A logical database schema generated in implementation design phase is transformed into physical database schema on target DBMS. User interfaces in running hypermedia are implemented by the use of user interface schema.

Branch\_Prospective\_Customer\_View (Bran\_Code, Bran\_Name, Cust\_Id, Meeting\_Memo)  
![](/api/attachments/RAYKYAGJ/fulltext/images/78895fc21aedee09bd7da2ea98033d3f854e87254c174e2da434cb12c4ceed3b.jpg)  
Fig. 14. User interface design specification.

![](/api/attachments/RAYKYAGJ/fulltext/images/edf6d8de3efcec2f1d60577f6afb60923c55b8dfc5637350b43bbdd174fbdbf3.jpg)  
Fig. 15. Collaboration relationship transformation.

Table 2  
Relational tables and views

<table><tr><td>Table name</td><td>Type</td><td>Attribute name</td></tr><tr><td>Customer</td><td>Table</td><td>Cust_Id, Cust_SSN, Cust_Name, Cust_Job, Cust_Rank, Cust_Sdate, Cust_Bdate, Cust_Phone, Cust_Zip, Cust_Addr, Cust_Credit, Cust_Asset</td></tr><tr><td>Current_Customer</td><td>Table</td><td>Cust_Id, Cur_Cust_Init_Date</td></tr><tr><td>Prospective_Customer</td><td>Table</td><td>Cust_Id, Meeting_Memo, Bran_Code</td></tr><tr><td>Branch</td><td>Table</td><td>Bran_Code, Bran_Name, Bran_Addr, Bran_Phone</td></tr><tr><td>Account</td><td>Table</td><td>Acct_No, Acct_Balance, Acct_Reg_Date, Acct_Type, Cust_Id, Bran_Code</td></tr><tr><td>Transaction</td><td>Table</td><td>Trans_Code, Trans_Date, Trans_Type, Trans_Amount, Acct_No, Bran_Code</td></tr><tr><td>Current_Customer_View</td><td>View</td><td>Cust_Id, Cust_Name, Cust_Job, Cust_Rank, Cust_Sdate, Cust_Bdate, Cust_Phone, Cust_Zip, Cust_Addr, Cust_Asset</td></tr><tr><td>Branch_Prospective_Customer_View</td><td>View</td><td>Bran_Name, Bran_Code, Cust_Id, Cust_SSN, Cust_Name, Meeting_Memo</td></tr><tr><td>Branch_Account_View</td><td>View</td><td>Bran_Name, Bran_Code, Acct_No, Acct_Type, Acct_Balance</td></tr><tr><td>Account_Transaction_View</td><td>View</td><td>Acct_No, Trans_Code, Trans_Date, Trans_Type, Trans_Amount</td></tr></table>

![](/api/attachments/RAYKYAGJ/fulltext/images/1abfb858d4bb3076831bd3c62c8b8ada18ce08dc2d0efc1441a2574ee5504be9.jpg)  
Fig. 16. Construction process of SOHDM.

## 4. An Intranet system

An Intranet system is built by the use of Oracle RDMBS [17], Java, and HTML for the Bank Accounting Applications. The system has a TCP/IP LAN based client/server configuration as shown in Fig. 17. Oracle call interface (OCI) is used as an interface gateway between Java and Oracle. The system is based on three-tier architecture, the first-tier for WWW clients, the second for the web server in Windows NT, and the third for Oracle database in UNIX.

![](/api/attachments/RAYKYAGJ/fulltext/images/25ded40b0e95cb08f1394d7b3806a16cf26d179561bac71ebd529e77565d1eac.jpg)  
Fig. 17. Target hypermedia system architecture.

![](/api/attachments/RAYKYAGJ/fulltext/images/e15f6cc3e6b7ed8184943bd8f113723ed2b9c8d507fb7b921a1f86a17a4cf0fd.jpg)

\- Operating well above its status as a regional bank, the Bank posted exceptional results in 1995. At year end, the Bank's total assets registered W8,140.2 billion (US\$10,507.6 million), and its stockholders' equity was W579.3 billion (US\$747.7 million). Translating this performance into measurable indicators, the Office of Bank Supervision of Korea in 1995 ranked the Bank first among its peer competitors in terms of both performance, and financial and management condition.

Document: Done

Fig. 18. Main menu screen.

Fig. 18 is the main menu screen. From the main menu icon (left side in Fig. 18), ‘Customer Information System,’ one can navigate among submenus like ‘Current Customer,’ ‘Prospective Customer’, ‘MIS’, and ‘Service and Products’. The main menu refers to the Main\_001 page schema.

Fig. 19 corresponds to an implementation for the ‘Current\_Customer\_001’ page schema. It has a scrolled text field which highlights the current page, as well as four buttons—‘Search with Id’, ‘Search with List’ ‘Special Customer’, and ‘Conditional Search’. The buttons act as anchors which lead users to embedded applications. If the ‘Search with Id’ button is clicked, then the ‘Customer Search with Id’ application is initiated. This application has an additional input field for search with customer Id. It has two buttons, ‘Transaction’, and ‘Credit’ for additional information on the related customers.

Fig. 20 shows results from retrieving prospective customer information. Prospective customers to be interviewed are listed for each branch. This page screen is implemented for ‘Prospective\_Customer\_001’ page schema. Clicking the ‘Branch’ button and then selecting the branch name provides a new window. Prospective customers in the branch selected are shown in this window.

Clicking the ‘MIS’ anchor in the left side of prospective customer page screen results in the ‘MIS’ page screen as shown in Fig. 21. This page is implemented for ‘MIS\_001’ schema. It shows the deposit amounts (today and yesterday) by headquarters, or branches.

![](/api/attachments/RAYKYAGJ/fulltext/images/cfad135d30620f12cd587718c35ff5b4a7e32c63029ebbe959017c1775facd7a.jpg)  
Fig. 19. Current customer page screen.

![](/api/attachments/RAYKYAGJ/fulltext/images/4a6baf99ecbf0c68c30fdb808b6fe5ba1530a6367d928075f32551f2f7e93003.jpg)  
Fig. 20. Prospective customer page screen.

![](/api/attachments/RAYKYAGJ/fulltext/images/a288cc19ad0da5e46e3e1864abc654de4ff3cad137d5e171c1c89c93dddb4efd.jpg)  
Fig. 21. Customer MIS page screen.

## 5. Methodology comparison

We compared features of SOHDM with those of four other major hypermedia design methodologies. This comparison is summarized in Table 3.

RMM and VHDM are based on E-R model and thus relatively simple to use. In contrast, SOHDM, as well as EORM and OOHDM adopt OO technologies to deal with rich semantics. Accommodating semantics may improve user satisfaction even with the price of analysis complexity.

In SOHDM, scenarios and CRCs are used for analyzing and modeling users' requirements. Specifying scenarios helps to capture ensure system flexibility from the earliest phase in the development process. In addition, the structure of CRC card promotes a behavioral approach to object modeling. The CRC card has an attractive informal appeal that helps make the emerging design tractable. SOHDM employs scenarios and OO views for finding navigational units. Concentrating on responsibility-driven scenarios and OO views is likely to capture navigational requirements better than static data entities.

## 6. Conclusions

This paper describes a scenario-based object-oriented methodology for developing hypermedia applications. We believe that our methodology is the first to use scenarios to capture hypermedia navigational requirements that are not shown in data relationship. The scenarios are then transformed into object-oriented views, which are used for designing hypermedia pages with navigational links. The use of scenarios is likely to improve the quality of hypermedia design to ensure flexibility from the earliest opportunity. The use of scenario as well as data model improves the quality of the navigation design.

Table 3
Comparison of hypermedia design methodologies

<table><tr><td>Criteria/methodology</td><td>RMM [10, 11, 12]</td><td>EORM [13, 14, 15]</td><td>OOHDM [18, 19, 20]</td><td>VHDM [16]</td><td>SOHDM</td></tr><tr><td>Authors and year</td><td>Isakowitz et al. (1995)</td><td>Lange (1993)</td><td>Schwabe et al. (1995)</td><td>Lee et al. (1998)</td><td>—</td></tr><tr><td>Key modeling technique</td><td>E-R</td><td>OO</td><td>OO</td><td>E-R</td><td>CRC cards &amp; scenarios</td></tr><tr><td>Phases</td><td>1. E-R design2. slice design3. navigational design4. conversion protocol design5. UI screen design6. run-time behavior design7. construction</td><td>1. class framework2. composition framework3. GUI framework</td><td>1. conceptual design2. navigational design3. abstract interface design4. implementation</td><td>1. requirement analysis2. E-R design3. view design4. navigational design5. mapping6. implementation</td><td>1. domain analysis2. OO modeling3. view design4. navigational design5. implementation design6. construction</td></tr><tr><td>Documentation</td><td>E-R diagramslice diagramRMDM diagram</td><td>class structureGUI design</td><td>OMT&#x27;s OO modelnavigational classabstract interfacedeesign model</td><td>E-R schemaview schemanavigationalschema</td><td>system scope diagramevent listscenario setsCRC cardclass structure diagramOO viewnavigation link schemapage schemaUI specification</td></tr><tr><td>Source of navigation</td><td>E-R relationship</td><td>OO relationship</td><td>OO relationship</td><td>E-R relationship</td><td>scenario and OO views</td></tr><tr><td>Approach to identifying users&#x27; views</td><td>none</td><td>none</td><td>view</td><td>view</td><td>scenario and OO views</td></tr><tr><td>Semantic richness</td><td>relatively poor</td><td>relatively rich</td><td>relatively rich</td><td>relatively poor</td><td>relatively rich</td></tr></table>

The methodology is effective for integrating WWW hypermedia system with enterprise databases. An Intranet system was built to demonstrate the usefulness of the methodology.

## References

[1] M. Bieber, C. Kacmar, Designing hypertext support for computational applications, Commun. ACM 38(8), 1995, pp. 99–107.

[2] M. Bieber, F. Vitali, Some Hypermedia Ideas for the WWW, Proceedings of 30th Hawaii International Conference on System Sciences, 1997, pp. 309–319.

[3] M.R. Blaha, W.J. Premerlani, J.E. Rumbaugh, Relational database design using an object-oriented methodology, Commun. ACM 31(4), 1988, pp. 414–427.

[4] J. Fong, Mapping extended entity relationship model to object modeling technique, SIGMOD Record 24(3), 1995, pp. 18–22.

[5] M. Frank, Shifting gears, Internet Systems 1, 1996, pp. 6–47.

[6] F. Garzotto, L. Mainetti, P. Paolini, Hypermedia design, analysis, and evaluation issues, Commun. ACM 38(8), 1995, pp. 74–86.

[7] F. Garzotto, P. Paolini, D. Schwabe, HDM: A model-based approach to hypertext application design, ACM Trans. Off. Info. Syst. 11(1), 1993, pp. 1–26.

[8] F. Garzotto, P. Paolini, L. Mainetti, Navigational patterns in hypermedia databases, Proceedings of the 26th Hawaii International Conference on System Sciences, 1993, pp. 370–379.

[9] J. Gosling, H. McGilton, The Java Language Environment, Sun Microsystems Computer Company, October 1995.

[10] T. Isakowitz, E.A. Stohr, P. Balasubramanian, Designing hypermedia applications, Proceedings of the 27th Hawaii International Conference on System Sciences, 1994, pp. 354–365.

[11] T. Isakowitz, E.A. Stohr, P. Balasubramanian, RMM: A methodology for structured hypermedia design, Commun. ACM 38(8), 1995, pp. 34–44.

[12] T. Isakowitz, A. Kamis, M. Koufaris, Extending the capabilities of RMM: Russian Dolls and Hypertext, Proceedings of 30th Hawaii International Conference on System Sciences, 1997, pp. 148–157.

[13] D.B. Lange, An object-oriented design method for hypermedia information systems, Proceedings of the 27th Hawaii International Conference on System Sciences, vol. 3, 1994, pp. 336–375.

[14] D.B. Lange, Enhanced relationships in object-oriented database modeling, Proceedings of Info. Science '93, 1993, pp. 296–304.

[15] D.B. Lange, Object-oriented hypermodeling of hypermedia supported information systems, Proceedings of the 26th Hawaii International Conference on System Sciences, 1993, pp. 380–389.

[16] H. Lee, J. Kim, Y.-G. Kim, S.H. Cho, A view-based hypermedia design methodology, Journal of Database Management 10 (2) (1999) pp. 3–13.

[17] ORACLE Co., Oracle 7 Server SQL Reference, Release 7.2, Oracle Corporation, April 1995.

[18] D. Schwabe, G. Rossi, Building hypermedia applications as navigational views of information models, Proceedings of the 28th Hawaii International Conference on System Sciences, 1995, pp. 231–240.

[19] D. Schwabe, G. Rossi, The object-oriented hypermedia design model, Commun. ACM 38(8), 1995, pp. 45–46.

[20] D. Schwabe, G. Rossi, S.D.J. Barbosa, Abstraction, composition, and layout definition mechanisms in OOHDM, Electronic Proceedings of the ACM Workshop on Effective Abstractions in Multimedia, Sanfrancisco, California, 1995.

[21] A. Simon, Strategic Database Technology, Morgan Kumfmann Publishers, Inc., 1995.

[22] E. Yourdon, Modern Structured Analysis, Prentice-Hall, 1989.
