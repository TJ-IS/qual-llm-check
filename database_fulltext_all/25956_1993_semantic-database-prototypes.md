---
otero_id: 25956
otero_key: "545X8BCF"
title: "Semantic database prototypes"
authors: "R. Baskerville"
year: "1993"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1993.tb00119.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Semantic database prototypes

R. Baskerville

School of Management, State University of New York, Binghamton, New York, 13902-6000, USA

Abstract. This paper describes a technique for improving the semantic consensus of conceptual database designs. Semantic consensus is a condition where there is pragmatic agreement among database designers and all of the users about which aspect of reality is being represented by a particular database element, and how that representation is being coded. The technique, called semantic database prototyping (SDP), involves a prototype that has been designed and constructed purely as a consequence of the semantic data model. The purpose of the semantic database prototype is to promote direct user validation during the conceptual database design phase of information systems analysis and design. Its distinguishing characteristic is its capture of data element occurrences within the context of the database design. The research method was action research, and the project is also briefly described.

Keywords: action research, data base, data base design, information, information systems design, prototypes, prototyping, semantics, semantic data model, systems analysis.

## INTRODUCTION

The purpose of this paper is to describe a technique for the extension of prototyping into the task of database modelling. This semantic database prototype (SDP) technique is motivated by the need for concise communication between the user and the database designer. The approach is predicated on the notion that a prototype can serve as an abstraction level for conveying a data model. The scope of the paper includes the issue of semantics in database design, a description of the action research that led to the discovery of the technique, and a sufficiently detailed description of semantic database prototyping to permit the reader to apply the technique. Before concluding, the paper discusses some opportunities for future research in this area.

Database design is a critical step in information systems development. After implementation, a change in any fundamental attribute, relationship or constraint of an integrated database element may require modifications to every application that concerns that element. Such

## 120 R Baskerville

changes thus result in expensive application maintenance. Consequently, the Information Engineering (IE) literature emphasizes the importance of a careful, stable, data design relative to process design (Finkelstein, 1981; Martin & Finkelstein, 1981; Inmon, 1988; Martin 1990). It follows that mis-communication between database designer and user may be profoundly ruinous to the success of a new information system. A technique for improving the accuracy of this communication (such as the one described below) is of enormous importance for data-oriented system designs.

## SEMANTIC THEORY IN DATABASE MODELS

The two purposes of models, in general, are epistemological and logical. On the one hand, they help us to express our understanding; on the other, they help us to infer from the abstract that which is arcane in the reality (Harre, 1972). For these purposes, data models provide constructs by which we may abstract the inherent structure, operations, and constraints of data in reality (Tsichritzis & Lochovsky, 1982). Semantic theory is relevant because it regards the meaning in language, or the relationship between signs and objects in the world. These theoretical semantics of data models have historically provided a basis for discussions in this arena (Klein & Lyytinen, 1991).

## Metadata constructs versus capture

Research based on semantic theory has two directions. On the one hand, metadata construct research inevitably focuses on the proper inner workings of database management software: which possible data constructs are allowed, what mechanisms can be used for presenting data, etc. Manufacturers of database packages closely follow research into ideal metadata constructs. On the other hand, research into the process of capturing the metadata deals with approaches and methods for developing knowledge about an application domain and implementing a usable data model on whatever constructs are provided by the system. Analysts and designers of computer-based information systems closely follow research into ideal metadata capture techniques.

Semantic theory plays an important role in both of these research arenas, in much the same way as algorithm theory is important in both compiler and application program design. We provide a context for the work that follows with a brief review of each of these research streams.

## Semantic metadata construct theory

This work generally seeks an orthogonal taxonomy of the semantic requirements in data modelling, and originates in the concept of a semantic database model. Closely related to the relational data model, semantic models are distinguishable in that these ignore all implementation constraints. Chen's (1976) entity-relationship model is foremost among the semantic models. This research community has focused on the encoding of the universal semantic rules needed for metadata in the semantic database model. Such semantic database research seeks to minimize database design errors by offering constructs that permit an accurate, effective model. This model (i.e., the database) reflects the most essential real-world attributes, relationships and constraints relevant to the design domain.

'Such a semantic-based description and structuring formalism is intended to serve as a natural application modelling mechanism to capture and express the structure of the application environment in the structure of the database.' Hammer & McLeod (1981).

Earlier Hammer & McLeod (1976) focused on metadata constructs that facilitate semantic integrity. They delineated various levels of semantic integrity that database designers might achieve with semantic data models. Ronald Stamper's (1979) continuing work in LEGOL led to a definition of semantic normal form. This database design approach goes beyond the normalization of the unintended anomalies in operations on data, and seeks to reduce the unintended anomalies that accompany operations on the metadata. More recently, this project has led to the proposal for a 'normbase': constructs that can represent entire systems of social norms (Stamper et al., 1991). Ongoing experiments include the NORMA language, which represents the social knowledge of a group as a system of semantic and norm constructs.

## Semantic metadata capture theory

This body of research regards the cognitive, social and organizational processes by which designers learn, understand and capture the values of the metadata that is to be encoded by the constructs described earlier. One segment of this literature regards the conceptual difficulties of end-user database development. Jeffrey Hoffer (1982) pioneered the study of users and metadata capture from the perspective of information centre requirements. Throughout this stream of research, the semantic data models have consistently baffled and repelled end-users. Hoffer concluded that people tend to rely on data-process flow models when given a choice — it is the process that gives meaning to the data. Juhn & Naumann (1985) conducted an experimental comparison of the metadata validation task for end-users. These users were randomly assigned a validation task for a familiar database domain in the form of one of four models (two semantic models and two relational models). The results were mixed, and the semantic models imparted a better understanding of relationship and cardinality, but the relational models supported a better understanding of primary and foreign keys. Batra, Hoffer & Bostrom (1988) studied the impact of semantic data models on the end-user metadata capture process. Again, the results are mixed: the semantic data model and the relational model were each more confusing to end-users in specific circumstances. Importantly, the average total error rate by end-users with both relational and semantic data models hovered around 45%. Batra et al. (1988) suggest that the solution is to train and support users in the metadata discovery and validation tasks.

The LEGOL project represents a different segment of metadata capture research. Rather than train users in semantic data modelling, the LEGOL team developed MEASUR, a comprehensive set of tools for the analysis, design and construction of an information system based on social norms (Stamper, Althans & Backhouse, 1988). This work accepts that 'formal semantic theories fail to account for meanings that relate language to reality', and suggests that software engineering must find ways of overcoming the semantic misunderstandings created by designer-user differences in intentionality, culture, responsibility and commitment.

The work below is distinguished from the previous research by two characteristics. First, unlike the work in end-user database design, SDP permits end-user validation of a semantic data model by capitalizing on iterative learning, linguistic and semiotic semantics, and prototyping. Training users in semantic data modelling is not necessary. Secondly, unlike MEASUR, this technique is narrowly focused on the critical designer-user communication problem. Accordingly, SDP can be easily integrated into many existing systems development philosophies. Comprehensive business-oriented techniques such as MEASUR embrace a wide scope which requires that analysts and designers adopt 'a radically different philosophy' (Stamper, Althans & Backhouse, 1988) in the analysis approach.

## SEMANTIC CONSENSUS

Database designers seek to label everything in their design domain precisely. They may earnestly seek to understand and adapt existing labels, or to exercise institutional power and impose their own labels (cf. 'imposed consensus', Stamper, 1987). Semantic consensus is a condition where there is pragmatic agreement among database designers and all of the users, about which aspect of reality is being represented by a particular database element, and how that representation has been coded. At a very fundamental level, 'meanings depend upon consensus', (Stamper, 1987). Users and designers have difficulty understanding the meaning of database element names because they lack relevant shared experience. An 'interpersonality of language signs' is very difficult to achieve. Even so, '... where a common core of signification is obtained, the signs may have, to different individuals of the community, different additional significations' (Morris, 1946).

Theories of reference regard the naming of things or the meaning of terms. These theories evolve along two overlapping streams of thought: scientific (linguistics) and philosophical (semiotics). In the social sciences, the field of linguistics regards semantics as the study of the meaning in language. In philosophy, the field of semiotics regards semantics as a study of the logical relations between linguistic expressions and the objects in reality to which they refer (Postman & Weingartner, 1966).

Semantic theories of reference disagree whether such meaning is always some cluster of properties that we choose to associate with the name (Putnam, 1977), or whether certain 'natural kind terms' always refer to a real-world thing (Kripke, 1977). The practical difficulty for the database designer is that both views define semantic agreement as no more than a general consensus about 'enough' properties to capture the significance of the name. Disagreement will often be retained over some other properties associated with the name. This means that the designers and users may misunderstand the database model because they fail to communicate effectively the exact set of properties that each associates as the meaning of a database element name.

Semiotics focuses on the function of signs in describing objects in the world. Semiotic theory differentiates semantics (the relation between signs and reality) from syntactics (the relations among signs) and pragmatics (the relation between signs and behaviour). Pragmatic semiotics (cf. Stamper, 1973) and linguistic semantics (cf. Lech, 1974) are both concerned with behaviour as a way of understanding meaning in language.

This pragmatic aspect of semantics is highly related to the problem of semantic consensus. Semantics extends beyond words, regarding any object associated with a pattern of behaviour (or the pattern itself) as a sign that carries meaning. The process of attaching meaning to signs is itself a behavioural or social process (Stamper, 1973). We learn from this that database analysts must both discover and design these semantics. On the one hand, the analyst must find the pragmatic meaning of the terms and names of the user for things. On the other hand, the database analyst will often select or invent meaningful names for objects or behaviour patterns in the world of the user which are new or have never been delineated. These newly invented signs are incorporated in the abstract model of the analyst and consequently projected into the user's world.

Database designers have difficulty discovering the semantics of users because their conversations with users become defocused. User-designer communications naturally diverge in three ways:

## (1) Objective of their descriptions

The user must focus on processes that are applied to data. The primary role of the user is to process data; hence Hoffer (1982) noticed user penchants for 'process meaning' in data. In contrast, the database designer must focus on the relationships found among those data. Universal constraints occupy the concern of the designer.

## (2) Particularity of their knowledge

The user knows that the relevant set of data may be different for each specific processing act. That is, experience has inculcated the user about the data processing exceptions. Opposing this, the designer seeks to find the universals and wants to discover where these data are consistent; exceptions add brutal complexity. To the designer, it seems the user is mired in chaotic, uncontrolled complexity.

## (3) Degree of their abstractions

The user naturally focuses on specific instances of real-world things. The user is very familiar with the various objects or behaviours that are being represented by data. The designer's natural focus is directed to building generalized abstracts of these things: classes, relations and aggregations. To the user, it seems that the designer is constructing an imaginary world.

## 124 R Baskerville

## SEMANTIC DATABASE PROTOTYPING

Semantic database prototyping is a method for permitting end-user validation of a semantic data model. It presents data instances in the context of the data design, and thus permits the user to study the relationship between the abstract design and reality. Users and designers share an understanding by focusing on this prototype. In this social process, users and designers mutually must adjust their semantics, the rules of their language, their thinking, and ultimately their artifacts.

## Prototyping to increase semantic consensus

The details of an action research project are described in the appendix. This study concluded that a major factor contributing to the loss of semantic consensus is the lack of interactive user validation of database designs. As we have seen above, direct user reviews of conceptual database design models are problematic. As an alternative framework, prototypes are well-known mechanisms for improving user validation of systems designs (cf. Naumann & Jenkins, 1982; Boar, 1984; livari & Karjalainen, 1989). Prototypes surmount the esoteric nature of system design descriptions by presenting a working model of a specification.

Prototypes are known to improve user-designer communications (Mason & Carey, 1983). This is primarily because prototypes are more effective linguistic artifacts. Pelle Ehn (1989) recognizes that all systems descriptions are fundamentally linguistic artifacts. When seen from the viewpoint of Wittgensteinian language games, these design artifacts are examples and reminders with which designers and users may reflect upon some future computer system. Dahlbom & Janlert (1989) describe such artifacts as being shaped by our experiences; externalizations of thinking, which allow our ideas to be subjected to socially controlled systems of rules. By choosing to prototype, we choose an alternative linguistic artifact as the basis for user-designer understanding.

We will discuss the details of the technique below. The philosophy of the technique is rooted in its role as a shared artifact. On the one hand, the prototype represents the thinking of the database designer. It directly reflects the entity-relationship diagram. On the other hand, it presents the user with an artifact populated with sample data. The users may explore the design through the artificial processes implied by the semantic data model. Users may process the data by interactively transversing the entity-relationship diagram, exploring relations, taking note of the unaccounted exceptions, and studying attribute locations.

Application prototyping is much better known than database prototyping. Such application prototypes are designed and constructed mainly to demonstrate the specific procedural or processing requirements. Little thought has been given to the use of prototyping within the database design process. Shoval & Pliskin (1988) mention the database schema as one area of validation for experimental prototypes, and Loomis (1987) also alludes to database prototypes. But detailed descriptions of a specific prototyping tool for the purpose of user-driven conceptual database modelling does not exist, probably because the need for user-designer semantic consensus is poorly understood.

## Overview of the approach

The semantic database prototyping approach is an iterative, cyclical database analysis and design stage. It may be combined with various applications analysis and development methods as part of an overall information systems development methodology. From this perspective, it is a tool that would be suitable for the 'toolboxes' of structured systems analysis (DeMarco, 1979), object-oriented analysis (Coad & Yourdon, 1990), and information engineering (Martin, 1990). Its iterative, participative learning cycle from real world, to conceptual modelling, to real world artifact, makes the tools suitable for use in soft systems (Checkland, 1981) and socio-technical approaches (Mumford, 1983). The approach employs two interlocked design artifacts: a typical entity-relationship diagram, and a semantic database prototype (SDP). The interlocked nature of these two artifacts anchors the semantic data model to the evolving form of the prototype.

Initiation occurs when analysts first meet with the users and conduct a brief study of the problem domain. They produce an entity-relationship diagram. The programmers created the SDP by interpreting the diagram through five programming rules. The SDP is a particular kind of interactive, operational prototype. Hence, the diagram is chiefly used to illustrate the understanding shared between analysts and programmers.

Following this, users review and operate the prototype, selecting and entering a small quantity of sample data. The analysts and users meet before, during and after this operation. They chiefly discuss where the prototype places unsuitable constraints on the user's data capture and representation activities. In this way, the prototype is chiefly used to illustrate the understanding shared between the users and the analysts.

This process continues iteratively. The analysts modify the entity-relationship diagram and incorporate changes to alleviate the constraints. The programmers then correct the prototype for an additional round of user reviews. This cycle continues until the user suggestions cease, or diminish to a routine maintenance level. The following sections describe this approach in detail.

## Initiation

Semantic database prototyping commences with a very brief conceptual database design, rapidly prepared by an analyst from minimized user interviews. The resulting high error content of the inadequate design is accepted on the grounds that further extensive user participation in the design will bring these errors to analyst attention. The analyst, using normalization (Kent, 1983), dependency diagrams (Smith, 1985) or even intuition, constructs an entity-relationship diagram. Varied or enhanced versions of entity-relationship diagrams, such as information structure diagrams (Shlaer & Mellor, 1988), or the extended entity-relationship diagram (Elmasri, Hevner & Weeldreyer, 1985) will work as effectively as Chen's (1976) original technique.

Working directly from the conceptual design model, programmers build prototype data manipulation screens and simple printed report programs. This can be done rapidly by using the fourth generation tools available with most relational databases. Since the programmers work directly from the conceptual design model of the database, they require a set of rules that instruct them on how to map database constructs onto menu, screen and report formats.

## Programming rules

These rules provide programming instructions as to the translation of the conceptual data model directly into data entry/manipulation screen displays and printed reports. Four criteria circumscribe these rules and ensure that the prototype fulfils its roll as a linguistic artifact between users and designers.

First, the function prototype elements should consistently and explicitly conform to the entities and relationships in the data model. The objective is to create an artifact which reveals to the user the essential nature of the designer's thinking with regard to the data model.

Secondly, the rules should describe how the programmers may accomplish the entire construction of an SDP from the data model details. The need for any additional specifications from the analysts or designers would indicate problems. These problems could indicate an incomplete set of rules, or an attempt to introduce application-oriented processes into the prototype. Application-oriented processes, by compiling or summarizing data, may mislead the user about the design of the database.

Thirdly, the designer's names for various database entities, attributes, relationships, categories, etc., should be displayed along with instances of the data. That is, screens and reports should adhere to the data model naming scheme. This permits the user to discover conflicts between designer and user meanings for names. That is, semantic disagreements are made apparent.

Finally, the rules should take advantage of the available technology. Fourth generation tools accompany virtually all major relational databases, even the microcomputer-based packages. With these fourth generation tools, standard or 'default' screens, panels, and report listings are created directly from the internal metadata. This will minimize the programming task. In these cases, the rules should also require that programmers code data model names directly into the metadata. This further enforces the third criterion above, generating field labels, screen boilerplate and report headings directly from the designer's specifications.

The following paragraphs describe the five rules that evolved from the original work in the action research study team. These rules have been defined over the course of a number of subsequent data modelling projects.

## Rule 1: Entity screens.

All entity classes (tables) must be represented directly in a data entry/manipulation screen. This means that there should be a single screen for each box in the entity-relationship diagram. The screen should also permit multiple functions, e.g., row or record insertion, row query, row update (replace) following query, and row delete following query. All attributes are represented in the screen. However, where a large volume of attributes makes the screen too 'busy', the screen may be broken into two or more 'pages'.

## Rule 2: To-one screens

Any one-to-one or many-to-one relationship is conveyed by 'pop-up' windows in entity screens. That is, if we create an entity screen, and any entity instance displayed on that screen will be related to a single occurrence of another entity class, then it should be possible to call that related entity instance onto the display with a single keystroke or mouse click. An entity screen should display an indicator of an available pop-up screen when such to-one relationships exist. This might be by means of a graphic button or by highlighting an attribute which represents the foreign key to the related entity instance.

For example, consider the case where many students are related to one advisor. It should be possible to display a single student's data on a STUDENT entity screen. From this screen, at a single key-press, the ADVISOR screen, displaying the related advisor's data, should appear.

The exact implementation of this rule will depend on the features available in the programming environment. Most relational environments provide a mechanism by which two screens may be linked using designated attributes (foreign keys). Where windowing is unavailable, 'pop-over' windows can be used. Pop-over windows are little more than direct switches between two entity screens. Such pop-over windows can be programmed easily in most environments. In most cases, the pop-up screen can be a simple subroutine-like call to the related standard entity screen of the entity. This reduces the programming task considerably.

## Rule 3: One-to-many screens

One-to-many relationships must be illustrated with compound screens. That is, the 'one' entity class appears in the top portion of the screen, with repeating rows of the 'many' entity class appearing in the bottom portion. Most relational environments permit display screens to be divided into blocks or regions. The data displayed in these blocks can be linked by relating attributes from the underlying tables or entity classes. These blocks may display a single row or multiple rows. Using this feature, the screen is divided into an upper and lower region. Because of the size, both regions will be limited in the number of attributes that may be included in the display. The upper region displays a single instance of the 'one' entity class. The lower region displays multiple instances of the 'many' entity class. In case there are not enough tiers or rows to hold all of the 'many' entity instances, this lower region should be scrollable. While not absolutely necessary, this scroll feature is usually an automatic aspect of the screen generators.

For example, consider again the one-to-many relationship between students and advisor. This rule requires that a screen be created that displays a few important attributes of an ADVISOR instance in the upper half of the screen, and a list of related STUDENT instances in the lower half. Querying an advisor into this screen will automatically list all of the 'advisees'.

Pop-up screens should be available to the necessary entity screens. That is, a button should be available next to each entity instance (upper and lower portions) that permits access to the undisplayed attributes of the entity instances shown in one-to-many screens. For example, one could enable the ADVISOR button and receive the relevant full ADVISOR entity screen. Likewise, one could enable the button next to each STUDENT instance and pop-up the relevant full STUDENT entity screen.

## Rule 4: Many-to-many screens

Many-to-many relationships must be implemented in relational models by a correlation table. Consequently, many-to-many screens are generated as a multi-row screen derived from this correlation table. Such screens are very easily created by most relational database screen generation programs. The screen appears as columns of attributes, with attribute names appearing at the screen top. Each row on the screen represents an instance from the table, and a single instance of a relationship between two entity classes. Each row will usually equate with a row in the correlation table. Correlation tables will include at least two foreign keys, one from each of the entity classes in the relationship. Like to-one screens, buttons are associated with each foreign key. These can be used to summon the attributes of an entity instance involved in the relationship. Pop-up screen windows provide these attribute values. Ternary relationships may also be implemented with correlation tables and many-to-many screens.

Returning to our student's example, consider a case where one student is related to many courses, and one course is related to many students, a classic many-to-many example. Also suppose that the STUDENT table has a primary key attribute STUDENT\_NUMBER, and that the COURSE table has a primary key attribute of COURSE\_NUMBER. A many-to-many screen would consist of two columns, headed STUDENT\_NUMBER and COURSE\_NUMBER. Each row on the screen would represent the enrolment of a student, identified by an instance of STUDENT\_NUMBER, in a course, identified by an instance of COURSE\_NUMBER.

## Rule 5: Operational menus

A menu program must be constructed that allows users to navigate the screens and printed listing programs. While it may be necessary to adjust the menu design for the convenience of the user, it is initially designed as follows:

(1) A main menu permits selection of a screens menu and a printed listings menu.

(2) All entity screens, one-to-many screens, and many-to-many screens are available from the screens menu.

(3) The printed listings menu offers the user simple report generator programs. These provide listings of the instances of each database entity class and each correlation table. Most database and fourth generation language environments offer simple menu application generation capabilities. Often these may be a specialized form of screen in the screen generator.

## User review

The initial user review will involve a short explanation of the purpose of the prototype. Importantly, the users must understand that they are validating the structure of the data stores. Otherwise, their comments will address myriad procedural aspects that are not reflected by the semantic data model. The users' task is to select and enter a small quantity of sample data. They must select average and exceptional examples of data. During this process they should be mindful of particular instances of data that would not fit in the data entry forms which are offered.

The formats of reports and data manipulation screens are derived from the database design. As users exercise these prototype reports and screens, they will inevitably discover any semantic conflicts in the conceptual database design. In addition, the users should consider questions that must be answered from the database. They should be able to answer any question using the database, with the aid of paper, a pencil and a calculator.

After the user experiments with the prototype, the semantic exchanges between the design team and their 'world' are highly enriched in two primary ways.

(1) User attention focuses on both where and how the occurrences of data elements appear in the prototype. Example: a user may note that a data element is on the wrong screen, meaning that an attribute has been attached to the wrong object.

(2) Users will suggest corrections that reveal mistakes on the part of designers. Example: a user may be unable to enter a data code item into a field, meaning that an attribute has the incorrect data type.

## Iteration

Following a period of user review and experimentation, the analysts will likely make corrections to the entity-relationship diagram. Relationships may change cardinality, and attributes may migrate. Attributes will often move from the 'one' side of a relationship to the 'many' side of a relationship as users discover that more 'places' are needed on the screen for these data.

Subsequently, the prototype may be reprogrammed, and the user review process repeated. As the cycles repeat, the number of changes will diminish. The cycles will shorten as the group closes on consensus. Eventually the number of changes becomes a steady train of minor corrections. These clearly become typical maintenance problems. At this point, the semantic data model is complete, and this database design phase concludes.

The prototype will likely be discarded entirely. However, in some cases, the reports, entity screens and one-to-many screens can be useful foundations for elements of some applications.

There are two linguistic artifacts, the entity-relationship diagram and the SDP. Notably, these are the focus of two aspects of the organizational text which the design project studies. First is the user-analyst interaction, an interpretation of the organizational text and expressed in an entity-relationship diagram. Secondly, the analysts-programmer interaction, an interpretation of the organizational text and expressed in an SDP. Many errors and problems with the semantic data model are discovered by the programmers and analysts before the user review. That is,

## 130 R Baskerville

elements of the entity-relationship model will defy translation by the programming rules. As a result, the analysts and programmers work with one artifact to discover technical misunderstandings expressed in the other artifact.

## PROTOTYPE EXAMPLE: NAVAL DATABASE

In this section, we will illustrate a comprehensive example of an SDP. Figure 1 represents a simplified, but representational fragment of an entity relationship diagram (Chen, 1976). Each box in Figure 1 represents an entity class (and consequently a relational database table). The diamonds represent relationship classes connecting the entity classes. Cardinality is indicated by crow's feet on the lines connecting entities. The crow's feet represent a 'many' relationship, single line connections represent a 'one' relationship. There are no optional relationships shown. Four entity classes are represented, SHIP, EQUIPMENT, CAPTAIN, and HOME\_PORT. Three relationships are found: one-to-many between HOME\_PORT and SHIP, one-to-one between SHIP and CAPTAIN, and many-to-many between EQUIPMENT and SHIP. In relational database implementations of this model, a fourth table, SHIP\_EQUIP, is a correlative table implementing the many-to-many relationship. Attributes of each table are illustrated, and primary key (identifier) attributes for each class are denoted by an underscore.

![](/api/attachments/545X8BCF/fulltext/images/5ee20440bf0c36ec0b96507febe93389ff4509af2684cd684de0004c20c4d614.jpg)  
Figure 1. Entity-relationship diagram.

Data modelling rules precisely define the locations of foreign keys and correlation tables. Note, for example, that the one-to-many relationship must be implemented by the presence of the key from the 'one' table (HOME\_PORT.hpname) as a foreign key in the 'many' table (SHIP.hpname). Similarly, the cptname is found in the SHIP table as implementation of the one-to-one relation.

An SDP for an integrated database is a large undertaking. A database with 30 entities can be expected to generate 50 or more screens and about 25 simple printed listing programs. The technique overcomes this large workload by the use of fourth generation programming tools, and by declaring rules with which programmers may translate conceptual models (e.g., entity-relationship diagrams) directly into program code. The approach eliminates detailed program specifications.

## Implementing the programming rules

The example must illustrate how a data model can be expressed in a prototype. In order to see how user data can be viewed through this data model, we add flesh to the entity-relationship diagram above by populating the tables with a few simple instances. Figure 2 describes a few sample rows for each of the entities and relationships in the data model of Fig. 1.

## Rule 1: Entity screens

Entity screens were required for each of the four entities in the entity-relationship diagram. These include EQUIPMENT, SHIP, HOME\_PORT and CAPTAIN. As an example, Figure 3 illustrates the simple entity screen for the SHIP entity class. The other three screens were similar. Boxes in these screens represent data fields.

<table><tr><td colspan="5">SHIP</td><td colspan="3">CAPTAIN</td></tr><tr><td>SHNUMBER</td><td>SHNAME</td><td>SHTYPE</td><td>HPNAME</td><td>CPTNAME</td><td>CPTNAME</td><td>RANK</td><td>ADDRESS</td></tr><tr><td>14</td><td>Wales</td><td>Destr</td><td>Norflk</td><td>Jones</td><td>Bligh</td><td>Cdr</td><td>Palm St.</td></tr><tr><td>22</td><td>Essex</td><td>Carri</td><td>Norflk</td><td>Smith</td><td>Gray</td><td>Lt</td><td>Daisy Rd.</td></tr><tr><td>27</td><td>Kent</td><td>Destr</td><td>Portsm</td><td>Gray</td><td>Jones</td><td>Lt</td><td>Rose Dr.</td></tr><tr><td>35</td><td>York</td><td>Battl</td><td>Portsm</td><td>Bligh</td><td>Smith</td><td>Capt</td><td>Oak St.</td></tr><tr><td colspan="5">HOME_PORT</td><td colspan="3">SHIP_EQUIP</td></tr><tr><td>HPNAME</td><td colspan="2">ADDRESS</td><td colspan="2">PHONE</td><td>SHNUMBER</td><td>EQNUMBER</td><td>QTY</td></tr><tr><td>Norflk</td><td colspan="2">High Street</td><td colspan="2">1234</td><td>14</td><td>16</td><td>1</td></tr><tr><td>Portsm</td><td colspan="2">Central Ave</td><td colspan="2">5678</td><td>14</td><td>43</td><td>1</td></tr><tr><td></td><td colspan="2"></td><td colspan="2"></td><td>14</td><td>82</td><td>2</td></tr><tr><td colspan="5">EQUIPMENT</td><td>22</td><td>16</td><td>2</td></tr><tr><td>EQNUMBER</td><td colspan="2">NOMEN</td><td colspan="2">WEIGHT</td><td>22</td><td>43</td><td>3</td></tr><tr><td>16</td><td colspan="2">Anchor</td><td colspan="2">50</td><td>27</td><td>16</td><td>1</td></tr><tr><td>41</td><td colspan="2">Sail</td><td colspan="2">5</td><td>27</td><td>43</td><td>1</td></tr><tr><td>43</td><td colspan="2">Radar</td><td colspan="2">12</td><td>27</td><td>82</td><td>2</td></tr><tr><td>82</td><td colspan="2">Cannon</td><td colspan="2">40</td><td>35</td><td>16</td><td>2</td></tr><tr><td></td><td colspan="2"></td><td colspan="2"></td><td>35</td><td>41</td><td>1</td></tr><tr><td></td><td colspan="2"></td><td colspan="2"></td><td>35</td><td>43</td><td>1</td></tr><tr><td></td><td colspan="2"></td><td colspan="2"></td><td>35</td><td>82</td><td>10</td></tr></table>

Figure 2. Sample tables.

![](/api/attachments/545X8BCF/fulltext/images/8bb0cf0ef3f75ca5ecd18ead2b36b71d84f34fb29996486f802ec2e26a790959.jpg)  
Figure 3. Derived entity screens.

## Rule 2: To-one screens

There is a single many-to-one relationship in our example: SHIP-to-HOME\_PORT. In addition there is a one-to-one relationship, SHIP-to-CAPTAIN. The availability of these pop-up entities is indicated by small buttons next to CPTNAME and HPNAME in the SHIP screen shown in Figure 3. CPTNAME and HPNAME are foreign keys. In order to activate these screens, the user would point-and-click (or motor the cursor onto the button and press ENTER). Figure 4 illustrates a pop-up CAPTAIN entity screen in the SHIP entity screen. Home port data could be similarly accessed.

## Rule 3: One-to-many screens

There is a single one-to-many relationship in our example: HOME\_PORT-to-SHIP. Figure 5 illustrates the appearance of the HOME\_PORT to SHIP screen. The entity instances permitted into the two parts of the display are 'locked' together by a programmed restriction matching the relevant foreign key in the lower screen (SHNUMBER) to the primary key in the upper screen (HPNAME). This is, the program only permits ship entity instances to be displayed which possess a value of SHIP.hpname (foreign key) that equals the value of HOME\_PORT.hpname (primary key). In both cases illustrated in Figure 5 this value is 'Portsm'. It is unnecessary to display the home port name values of the ships in the lower screen since the lock-together logic defines this to be the same as that shown under the display of the home port at the top of the screen. The small boxes are buttons for pop-up entity screens. These appear next to the primary key attributes, and permit access to the undisplayed attributes of HOME\_PORT and SHIP instances.

![](/api/attachments/545X8BCF/fulltext/images/8d57852382f1b307ec2fa68b87a5cf2f3fa1eb4f6713d9fc9d6fd61e7e52c4a1.jpg)  
Figure 4. To-one pop-up window.

## Rule 4: Many-to-many screens.

The example contains a single many-to-many relationship between SHIP and EQUIPMENT. A ship may carry many types of equipment, and a type of equipment may be found on many ships. In the entity-relationship diagram, this relationship has a single attribute of its own (QUANTITY). Thus, the correlation table (SHIP\_EQUIP) has three attributes: the foreign key to SHIP (SHNUMBER), the foreign key to EQUIPMENT (EQNUMBER) and QUANTITY. The primary key in this table is a compound key, composed of SHNUMBER and EQNUMBER. Figure 6 illustrates a screen based on the SHIP\_EQUIP table which implements the relationship between SHIP and EQUIPMENT entities. This screen may be used for inserting or querying data (the query may be for update or delete) with less programming than the one-to-many screen described above, since a single physical table underlies its logic. Notice the buttons next to each SHNUMBER and EQNUMBER instance. These will pop-up entity screens for related SHIP and EQUIPMENT instances.

![](/api/attachments/545X8BCF/fulltext/images/9679148b625f9b71a40f6a82dc2587594bb6f69182c664f46e21c48a7b8c8a70.jpg)  
Figure 5. One-to-many screen.

## Rule 5: Operational menus

The naval database prototype starts with a main menu offering two selections: (1) Data Entry and Edit, and (2) Printed Reports. Both selections call sub-menus. The Data Entry and Edit Menu offers six selections: (1) Ship Entry and Edit, and (2) Ship's Equipment Entry and Edit, (3) Home Port Entry and Edit, (4) Home Ported Ships Entry and Edit, (5) Captain Entry and Edit, and (6) Equipment Entry and Edit. The Ship Entry and Edit options (1) calls the SHIP entity screen. Similarly Captain, Home Port and Equipment options (3, 5 and 6) call their respective entity screens. The Home Ported Ships option (4) calls the one-to-many screen. The Ship's Equipment option (2) calls the many-to-many screen. From the Printed Report Menu, there are options for five simple reports: (1) Ship Report, (2) Captain Report, (3) Home Port Report, (4) Equipment Report, and (5) Ship's Equipment Report. Each option requires a simple column-wise listing program to print a list of the contents of the respective tables.

## SEMANTIC DATABASE PROTOTYPE CHARACTERISTICS

The important physical characteristic of an SDP is that it has been designed and constructed purely as a consequence of the conceptual database model. The construction of SDPs is based solely on the entity-relationship diagrams. SDPs are clearly distinguished from application prototypes, even when the latter are database-oriented. These two types of prototypes have different purposes, and different sets of constraints. For example, application prototypes, even though database-oriented, are purposeful reflections of the procedures required by the organization and freely employ summaries and 'views' that project artificial data constructs. These constructs are derived from the simpler and more fundamental database elements and intentionally disguise the actual database design.

![](/api/attachments/545X8BCF/fulltext/images/429b78219a2ba243c469c3e79b671ebd7b87f43ae2d76153df39aee1968f1ebc.jpg)  
Figure 6. Many-to-many screen.

In addition to these singular physical attributes, SDPs are distinguished by particular objectives, functions, and theoretical characteristics. The objective of these prototypes is to facilitate a shared understanding between designers and users during the conceptual database design process. The various screens and reports will not be likely to be useful as components of any future computer-based system.

The function of SDPs is to provide a concrete computer-based projection of the conceptual database structure. The projection frames sample data within the structure of the conceptual database design.

The important theoretical characteristic of the approach is that the SDP is a functional linguistic artifact which directly reflects the abstract conceptual database design. The programmers build this artifact from the analysts' abstraction. The users interact with the design by attempting to manipulate their sample data within this artifact. The designers work with abstractions: names and characteristics of entities, relations and attributes. Users work with sample data, the reflected occurrences of the important things in their universe. Both groups exchange understanding via the artifact. The users see the database design as a window into their world.

Finally, SDPs are characterized by their strong theoretical balance with the semantic data model. The semantic data model enables semantic databases by providing the necessary constructs to express accurately a meaningful data abstract. SDPs provide a means to capture accurately this meaningful data abstract.

## FUTURE RESEARCH

The primary need for future research arises from the research method used in this study. The only epistemologically sound technique that can be used for immediately relevant study of new methods is action research. It is difficult to generalize the results of action research without considerable further study. Action research knowledge is necessarily idiographic. That is, some undiscovered qualities of the particular environment of this particular study may have led to the success of the technique, and it may prove unsuccessful in the majority of other organizations.

The technique has been used in a number of designs since this project, and the initial indications are that the technique is generalizable to small and medium data models. It remains to be seen if this approach is appropriate for large-scale systems. This seems a promising prospect for two reasons. First, the rule-based nature of the programming minimizes the labour required to generate large prototypes. Secondly, the technical foundation lies in centralized or distributed relational database application generators. Large groups of networked users can experiment with the SDP before the organization commits irrevocably to the model.

Several side effects of this technique are notable. There is an opportunity for further research into these effects. These include the interaction between analyst and programmer, inherent denormalization, and large system prototyping. The following paragraphs address each of these.

The analysts noted that many technical errors in their conceptual design surfaced during prototype construction. For example, the programmers would not be able to implement a one-to-many screen because a foreign key was missing from the 'many-side' table. Since the programmers were constructing screens directly from the conceptual database design, such errors had to be corrected before the users ever saw the functional version. Interested researchers could examine these technical improvements to database conceptual designs that result from semantic database prototyping.

Database practitioners point out that normalization beyond third normal form may be impractical (McFadden & Hoffer, 1991). The term 'denormalization' refers to the intentional sacrifice of possible database anomalies in favour of less complex designs that are simpler to implement. To a certain degree, denormalization was inherent in the semantic database design process, since programmers had to build prototypes using whichever technology had been specified by the design team for the final database. Two factors imposed practical limits on database complexity (and therefore the feasibility of normalization beyond third normal form). First, the deadline effect of scheduled prototype reviews forced programmers to pressure analysts for simplification wherever possible. Secondly, users would complain when the prototype became too difficult to operate because of large numbers of interrelated screens. This denormalizing effect of a direct physical implementation of a conceptual database design would make further interesting research.

Another interesting area to study would be the impact of SDPs on the validity of the venerable entity-relationship model (Chen, 1976). This model is presently a powerful canon in only half of the information systems development paradigms. Hirschheim & Klein (1989) identify these information systems development paradigms as: (1) Functionalism, (2) Social Relativism, (3) Radical Structuralism, and (4) Neohumanism. $^{1}$ The entity-relationship model plays a strong role in both the Functionalist and Radical Structuralist paradigms. Indeed the entity-relationship concept is a fundamental underpinning of almost all of the major developments most recently advanced by the Functionalists. It is a core element of both the Coad-Yourdon (1990) and Shlaer-Mellor (1988) strains of object-oriented systems analysis. It is fundamental to Martin's (1990), Finkelstein's (1989) and Inmon's (1988) strains of information engineering. Virtually every major CASE software package, such as ORACLE®CASE (Barker, 1990) and Software-Through-Pictures, employs this model as the primary graphical vehicle for the database design. Semantic database prototyping suggests an approach to developing the entity-relationship constructs in a manner that recognizes the subjectivity of meanings and necessity for shared understanding. This introduces notions from the Social Relativist and Neohumanist paradigms and suggests a future hermeneutic role of an emergent entity-relationship model as part of the organizational texts relevant to ethnographic and post-modern approaches.

Certain prototyping productivity problems are resolved by the methodology. Large-scale prototype projects were previously thought unfeasible because of the difficulty of management and control (Alavi, 1984). The combination of programming productivity tools and declarative program specifications (rules defining physical implementation of conceptual models) relieved these difficulties to some extent. Additional research is needed that studies the feasibility of using programming rules (declarative program specifications) for directly coding both database and application prototypes from both logical data models and logical process models.

Finally, the rule-based nature of SDP makes this technique an easy candidate for automation. Reasonably simple extensions to most CASE technology would permit the automatic generation of a complete SDP from the entity-relationship diagram and data dictionary portions of the repository. This is perhaps of more practical interest than scientific research, but is clearly open for further study.

## CONCLUSIONS

This paper has reported the discovery of a technique for improving the semantic consensus of difficult conceptual database designs. This technique, being a new method, was necessarily found in an action research project. The action research was successful: the three aims of action research address the immediate problem situation, development of self-help competency in the research subjects, and the goals of social science. The immediate problem was resolved with the acceptance of the database design, and its consequent stability over the two subsequent years of applications development. The competencies of the respective actors resulted as the systems knowledge of the analysts broadened to include data design principles, and as the user community developed a deeper understanding of their own data. The social science of information systems gained a new technique for achieving semantic consensus in data base design.

Semantic consensus is an important quality of a successful database design project. When there is pragmatic agreement among database designers and all of the users about which aspect of reality is being represented by a particular database element, the designers apprehend a stable, semantic data model. The semantic database prototyping technique arose from an action research project, and has been employed in small- and medium-sized data modelling projects. This indicates that some generalization is possible. However, future research must assert the generalizability of the approach to large-scale systems.

## APPENDIX — RESEARCH DESCRIPTION

The theoretical and practical importance of semantic consensus was discovered during an action research project. As is the nature of such projects, both theoretical and practical benefits surfaced. This appendix describes the circumstances of the research project, and how the method (semantic database prototyping) issued from the research.

## Research method

Action research has been used in the social sciences for decades, and is not unknown in sociotechnical research (Susman, 1983) or in information systems research (Wood-Harper, 1985). The approach is sometimes called action science (Argyris, Putnam & Smith, 1985). This approach projects the behaviour of researchers into their empirical domain of observation. A carefully developed, concise definition of action research is:

'Action research simultaneously assists in practical problem-solving and expands scientific knowledge, as well as enhances the competencies of the respective actors, being performed collaboratively in an immediate situation using data feedback in a cyclical process aiming at an increased understanding of a given social situation, primarily applicable for the understanding of change processes in social systems and undertaken within a mutually acceptable ethical framework'. (Hult & Lennung, 1980).

Action research involves intervention. Researchers both observe and participate in the phenomena under study (Rapoport, 1970). The approach recognizes the difficulty researchers must face in rejecting their own predilections, and is firmly rooted in an interpretivist philosophical paradigm. Susman & Evered (1978) ground action research on phenomenology, existentialism and hermeneutics.

Certain misconceptions are common about action research. Action research has been miscast as active case research, consulting or even as an unstructured, non-rigorous method. However, action research differs from case-oriented research methods in that case research does not allow intervention by the researcher into the research. Also, action research is not merely commercial consulting. Consultants are expected to supply reliable, proven approaches. Unlike consulting, action research aims for the development of new knowledge. This aim requires the host or client organization to commit their willing acceptance of experimental approaches. Finally, action research is not unstructured, and is rigorous when properly conducted. It first requires the establishment of a client-system infrastructure or research environment. Following this, there are five identifiable, iterative phases: (1) diagnosing, (2) action planning, (3) action taking, (4) evaluating, and (5) specifying learning. The five phases can be iterative (Susman & Evered, 1978; Susman, 1983).

## Client-system infrastructure

This research was conducted through a consortium of several American universities that numbered among its objectives the co-ordination of action research into experimental systems development techniques. The client-system infrastructure was established with an agreement to undertake continuance of a government information systems development project that had failed.

The study entailed the development of a procurement budgeting system for a government agency. The existing systems were mostly manual, supported by a few microcomputer spreadsheets, and had access to a peripheral mainframe database facility which contained data relating to one budget area. The study team was invited after two previous analysis and design efforts had failed. A previous relational database-oriented analysis and design project failed when the designers attempted a strict canonical design based on the current paper forms and records. The resulting specification was massive, and the estimates for implementing the system ranged above three calendar years. The client rejected the specification for a number of reasons, including: (1) the specification was already becoming obsolete when it was submitted, indicating the final system would be too outdated; and (2) no one in the organization who understood the applications could understand the specification. The users were suspicious of the complex specification, and the project failed.

A second analysis team applied a variant of the Business Systems Planning (IBM, 1984) approach. After several difficult months, it became clear that the analysts could neither comprehend nor document the flexibility in the existing system. A contributing factor was the user alienation that developed from a second team of questioning analysts.

As our study commenced, the team was composed of an experienced team leader with a strong practical background in logistics and information systems, an analyst with a strong background in the procurement system, and a scientist commissioned as an action researcher. Later, the team was expanded to include a programmer and a second analyst.

## 140 R Baskerville

## Intervention diagnosis

The team initially examined the previous failures. They found that these two early projects were defeated by the large set of data classes, the large volume of data, and the high degree of volatility in the organizational environment. Based on these findings, the team recognized the ultimate need for highly flexible applications. Following Information Engineering theory described earlier, they prescribed the greatest possible stability in the data model. However, a proper design project for a large-scale highly normalized database would require trained, experienced database designers and a substantial commitment by management. The esoteric nature of database design demanded the specialists, and the large interval of initial database analysis effort demanded indulgence from management.

From the outset, it became clear that neither specialists nor indulgence would be forthcoming for the team. Having been twice disappointed, management was not about to consider long periods of invisible analysis. Management wanted quick, measurable, and highly visible results. There also was clear justification for proscribing any database design specialists. The inability of previous database specialists to communicate with the users led to user alienation. Because of this, two members of the study team were selected because of their familiarity with the application areas. Even if database design specialists with strong experience in procurement systems could be located, the economics and temporary nature of the project would likely prevent their assimilation into the team.

Given these findings, the team focused its diagnosis on the lack of interactive user validation of database designs. The creation of such a process would serve to gratify management's need for prompt, visible results while alleviating the study team's deficiency in database design experience. In the first case, the frequent user consultation and verification of designs would assuage management. In the second case, the analysts would have to correct constantly and interatively their invalid specifications under the acute realities of user reviews.

## Action planning

Typically, conceptual database design employs techniques and documents such as normalization, entity-relationship diagrams, data structure diagrams, data dictionaries, etc. These meticulously aid in the elimination of design errors that interfere with database stability or promote undesirable anomalies during processing. In order to operationalize this solution, the team would need to surmount the esoteric nature of such database design descriptions because users could not be expected to understand these without considerable training and explanations. This simply would not be possible with the alienated group of users that confronted the team. The team sought a design description that maximized a shared understanding between the analysts and the users.

The team considered a prototyping approach since these improve user-designer communications (Mason & Carey, 1983), and satisfy the iterative nature of the proposal. Regular user reviews not only would improve shared understanding, but increase user participation in the design process. This alone would heighten the initial acceptance and effectiveness of a new system (cf., Lucas, 1976; Land, 1982; Mumford, 1983; Hirschheim, 1985). Also, if the design artifact was an operational prototype, analyst database experience would improve gradually as the project progressed. Further, an operational prototype would demonstrate rapid and visible results to management.

Notice that at this stage of the research, the important semantic motive for SDPs was not recognized. The goal was socio-technical participation. The use of prototypes for application development in this role had been widely endorsed. Agresti (1986) recognized application prototyping as one of several important new paradigms for software development, mainly because it is a framework that extends user participation beyond the abstract detachment of interviews. However, such application prototypes are designed and constructed mainly to demonstrate the specific procedural or processing requirements, and the mechanics and role of SDPs was unclear in the literature.

The team planned a new design tool in which prototyping (normally a vehicle for application development) was solely applied for database design. The approach thus planned to resolve the major conflicts presented to the study team: (1) The meaningfulness of analysts' dialogue with both users and programmers would be highly enriched by the existence of a mutually understandable design prototype. In this way the solution addressed both the issues of analyst experience and user alienation. (2) The visible results would clarify for both users and management the meaningful progress of the project.

## Action taking

The team conducted an initial rapid database prototyping of the database design. This original approach incorporated many of the essential ideals described in the foregoing paper, but was considerably more complicated. It included several major elements that were removed or reconsidered in subsequent learning cycles. The most important of these difficult elements were: a formal interview process, pre-specification standards for prototype components (instead of rules), printed report prototypes, and a parallel application prototyping cycle. The sections below discuss what was learned and how this led to discarding or modifying these elements.

## Evaluating

Herculean design and programming efforts characterized the first attempt in SDP construction. Clearly, it would be impossible for the team to repeatedly mount such a large project. An evaluation revealed, however, that process-oriented features were being drawn into the SDP specification. Also analysts and users had difficulties in isolating data relationships from the confounding process algorithms while specifying prototype screen panels and report listings.

## Specifying learning

On the first cycle, the team concluded that the SDPs could be successful in capturing semantic and technical errors in this client's database design: (1) The prototype revealed the design feasibility; (2) Users were enthusiastic in their control over system design elements; (3) The apparent rapid progress pleased management. However, the team learned several lessons about their approach: (4) The deadline effect hurt badly — the team needed an alternative to the large specification; (5) Generally the users ignored the report programs in favour of the interactive screens — it was clearly the process of entering real data into the prototype database that was most significant. Through the process of entering data, the users unveiled their semantic disagreements with the designers; (6) The parallel application prototype added complexity and created more confusion among users than clarification about prototype purposes. The following section will discuss how further iterations of the action research cycle dealt with problems (4) to (6).

## Further iterations

Five further iterations of the action research cycle led to a number of changes in the technique. Functional specifications were eliminated in favour of programming rules. These rules defined how the relationships and constraints illustrated in a data model should appear in data manipulation screens or printed reports. This left only the entity-relationship diagram as the prototype specification and medium of analyst-programmer communication. Such a simplified specification fundamentally eliminated algorithms $^{2}$ and helped to relive the deadline effect.

The users' semantic focus on the interactive screens led the team to drop the complicated report programs in favour of a few simple listings. This reduced the prototype complexity and helped the deadline effect. The team also modified its formal interview process (originally a sequence of group and individual interviews) after the second cycle — the users eliminated the need for group sessions by informally discussing the prototypes amongst themselves between cycles and deliveries.

The original technique included a single application prototype as a parallel development with the SDP. The original role of this functional application was to help users understand the difference between an application and an SDP. The team meant this specimen of an application prototype to serve as an aid in deflecting user desires to impose processing algorithms in the SDP. Ultimately, the team learned that this was unnecessary as system users could understand data design metaphors such as file folders and card stacks. The application prototype was unnecessary (even counter-productive) complexity.

Theoretical content tends to emerge from action research. This project is no exception. The initial theoretical focus was on socio-technical participation. The research activities balanced between software engineering and user participation. The important impact on user-designer semantics, and the underlying theory began to crystallize very late in the project. This theoretical foundation is described in the foregoing paper.

The basic technology used in the original action research project was ORACLE for MS-DOS (development) and VM/IS ORACLE (production). (Later projects also developed SDPs in R:Base.) Any relational database systems with a competitive set of fourth generation tools should be adequate for supporting the technique.

## REFERENCES

Agresti, W. (1986) What are the new paradigms? In: New Paradigms For Software Development, Agresti, W. (ed.), IEEE Press, Washington, DC.

Alavi, M. (1984) An assessment of the prototyping approach in information systems development. Communications of The ACM, 27, 556–563.

Argyris, C., Putnam, R. & Smith, D. (1985) Action Science. Jossey-Bass, San Francisco, CA.

Barker, R. (1990) Case\*Method: Tasks and Deliverables. Addison-Wesley, Wokingham.

Batra, D., Hoffer, J. & Bostrom, R. (1988) Comparison of user performance between the relational and the extended entity relationship models in the discovery phase of database design. Proceedings of the Ninth International Conference on Information Systems, DeGross, J. & Olson, M. (eds.), pp. 295–308. Minneapolis, MN.

Boar, B. (1984) Application Prototyping: A Requirements Definition Strategy for the 80's. J. Wiley, New York.

Burrell, G. & Morgan G. (1979) Sociological Paradigms and Organizational Analysis. Heinemann, Portsmouth, NH.

Checkland, P. (1981) Systems Theory, Systems Practice.
J. Wiley, Chichester.

Chen, P. (1976) The entity-relationship model: toward a unified view of data. ACM Transactions on Database Systems, 1, 9–36.

Coad, P. & Yourdon, E. (1990) Object-Oriented Analysis. Prentice-Hall, Englewood Cliffs.

Dahlbom, B. & Janlert, L.-E. (1989) An artificial world: an invitation to creative conversations on future use of computer technology. In: Proceedings of the 12th IRIS: Information Systems Research Seminar In Scandinavia, (Part I), Bodker, S. (ed.), pp. 111–127. Computer Science Department, Aarhus University, Aarhus.

DeMarco, T. (1979) Structured Analysis and System Specification. Yourdon, New York, NY.

Ehn, P. (1989) Playing in reality. In: Proceedings of the 12th IRIS: Information Systems Research Seminar In Scandinavia, (Part I), Bodker, S. (ed.), Computer Science Department, Aarhus University, Aarhus.

Elmasri, R., Hevner, A. & Weeldreyer, J. (1985) The category concept: an extension to the entity-relationship model. Data Knowledge Engineering, 1, 75–116.

Finkelstein, C. (1981) Information Engineering (five part in-depth series). Computerworld, 15.

Finkelsfein, C. (1989) An Introduction to Information Engineering: From Strategic Planning to Information Systems. Addison-Wesley, Sydney.

Hammer, M. & McLeod, D. (1976) A framework for database semantic integrity. Proceedings of the 2nd International Conference on Software Engineering. pp. 498–504. IEEE Computer Society, Long Beach, CA.

Hammer, M. & McLeod, D. (1981) Database description with SDM: a semantic database model. ACM Transactions on Database Systems, 6, 351–386.

Harre, R. (1972) The Philosophies of Science: An Introductory Survey. Oxford University Press, Oxford.

Hirschheim, R. (1985) Office Automation: A Social and Organizational Perspective. J. Wiley, Chichester.

Hirschheim, R. & Klein, H. (1989) Four paradigms of information systems development. Communications of the ACM, 32, 1199–1216.

Hoffer, J. (1982) An empirical investigation into individual differences in database models. Proceedings of the Third International Conference on Information Systems, Ginsberg, M. & Ross, C. (eds), pp. 153–167. Ann Arbor, MI.

Hult, M. & Lennung, S.-Å. (1980) Towards a definition of action research: a note and bibliography. Journal of Management Studies, 17, 241–250.

IBM (1984) Business Systems Planning: Information Systems Planning Guide, 4th edn. IBM Department 796, Atlanta, GA.

livari, J. & Karjalainen, M. (1989) Impact of prototyping on user information satisfaction during the IS specifi-cation phase. Information & Management, 17, 31–45.

Immon, W. (1988) Information Engineering for the Practitioner: Putting Theory into Practice. Yourdon, Englewood Cliffs, NJ.

Juhn, S. & Naumann, J. (1985) The effectiveness of data representation characteristics on user validation. Pro-

ceedings of the Sixth International Conference on Information Systems, Gallegas, L., Welke, R. & Wetherbe, J. (eds), pp. 212–226. Indianapolis, IN.

Kent, W. (1983) A simple guide in five normal forms in relational database theory. Communications of the ACM, 26, 120–124.

Klein, H. & Lyytinen, K. (1991) Towards a new understanding of a data modelling. In: Software Development and Reality Construction, Floyd, C., Züllighoven, H., Budde, R. and Keil-Slawik, R. (eds), pp. 203–219. Springer-Verlag, Berlin.

Kripke, S. (1977) Identity and necessity. In: Naming, necessity and natural kinds, Schwartz, S. (ed.), pp. 66–101. Cornell University Press, Ithaca, NY.

Land, F. (1982) Notes on participation. The Computer Journal, 25, 283–285.

Leech, G. (1974) Semantics. Penguin, Harmondsworth.

Loomis, M. (1987) The Database Book. Macmillan, New York.

Lucas, H. (1976) The Analysis, Design and Implementation of Information Systems. McGraw-Hill, New York.

Martin, J. & Finkelstein, C. (1981) Information Engineering. Savant Institute Report Vols I & II.

Martin, J. (1990) Information Engineering Book II: Planning and Analysis. Prentice-Hall, Englewood Cliffs, NJ.

Mason, R. & Carey, T. (1983) Prototyping interactive information systems. Communications of the ACM, 26, 347–354.

McFadden, F. & Hoffer, J. (1991) Data Base Management, 3rd edn. Benjamin-Cummings, Menlo Park, CA.

Morris, C. (1946) Signs, language and behavior. Prentice-Hall, New York.

Mumford, E. (1983) Designing Human Systems for New Technology: The ETHICS Method. Manchester Business School, Manchester.

Mumford, E. (1983) Designing Human Systems, Manchester Business School, Manchester.

Naumann, J. & Jenkins, A. (1982) Prototyping: the new paradigm for systems development. MIS Quarterly, 6, 29–44.

Postman, N. & Weingartner, C. (1966) Linguistics: a revolution in teaching. Dell, New York, NY.

Putnam, H. (1977) Is semiotics possible? In: Naming, necessity and natural kinds, Schwartz, S. (ed.), pp. 102–118. Cornell University Press, Ithaca, NY.

Rapoport, R. (1970) Three dilemmas of action research. Human Relations, 23, 499–513.

Schlaer, S. & Mellor, S. (1988) Object-oriented Systems Analysis: Modeling the World in Data. Yourdon, Englewood Cliffs.

Shoval, P. & Pliskin, N. (1988) Structured prototyping: integrating prototyping into structured system development. Information & Management, 14, 19–30.

Smith, H. (1985) Database design: composing fully normalized tables from a rigorous dependency diagram. Communications of the ACM, 28, 826–838.

Stamper, R. (1973) Information in business and administrative systems. Batsford, London.

Stamper, R. (1979) Towards a semantic normal form. In: Data Base Architecture, Bracchi, G. and Nijssen, G. (eds), pp. 337–339. North-Holland, Amsterdam.

Stamper, R. (1987) Semantics. In: Critical Issues in Information Systems Research, Boland, R. and Hirschheim, R. (eds), pp. 43–78. J. Wiley, Chichester.

Stamper, R., Althans, K. & Backhouse, J. (1988) MEASUR: Method for eliciting, analysing and specifying user requirements. In: Computerized Assistance During the Information Systems Life Cycle, Olle, T., Verrijn-Stuart, A. and Bhabuta, L. (eds), pp. 67–115. North-Holland, Amsterdam.

Stamper, R., Liu, K., Kolkman, M., Klarenberg, P., Van Slooten, F., Ades, Y. & Van Slooten, C. (1991) From database to nombase. International Journal of Information Management, 11, 67–84.

Susman, G. (1983) Action research: a sociotechnical systems perspective. In: Beyond Method: Strategies for Social Research, Morgan, G. (ed.), pp. 95–113. Sage, Beverly Hills, CA.

Susman, G. & Evered, R. (1978) An assessment of the scientific merits of action research. Administrative Science Quarterly, 23, 582–603.

Tsichritzis, D. & Lochovsky, F. (1982) Data Models. Prentice Hall, Englewood Cliffs, NJ.

Wood-Harper, T. (1985) Research methods in information systems: using action research. In: Research Methods in Information Systems, Mumford, E., Hirschheim, R., Fitzgerald, G. and Wood-Harper, T. (eds), pp. 169–191. North-Holland, Amsterdam.

## Biography

Richard Baskerville is an Assistant Professor of Information Systems in the School of Management at the State University of New York at Binghamton. He completed his MSc and PhD in Information Systems at the London School of Economics. His major research areas include information systems research and design methods. His work places particular emphasis on security and integrity design methods, as described in his book, Designing Information Systems Security.
