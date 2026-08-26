---
otero_id: 27014
otero_key: "5NFN5EUB"
title: "An Asset-Based Systems Development Approach to Software Reusability"
authors: "Jahangir Karimi"
year: "1990"
journal: "MIS Quarterly"
doi: "10.2307/248776"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
An Asset-Based Systems Development Approach to Software Reusability
Author(s): Jahangir Karimi
Source: MIS Quarterly, Vol. 14, No. 2 (Jun., 1990), pp. 179-198
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248776
Accessed: 23-10-2015 20:38 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

An Asset-Based Systems Development Approach to Software Reusability

By: Jahangir Karimi
College of Business and Administration
University of Colorado at Denver
1200 Larimer Street (Box 165)
Denver, Colorado 80204

## Abstract

Software reusability has been viewed as one of the major opportunity areas for improving software productivity. An overview of software reusability research suggests that the traditional approach to software development is inappropriate for the development of reusable software parts. An organizational strategy for making software reusability practical is needed. An asset-based systems development method, based on this strategy, focuses on the development of information assets designed to be reused. It also facilitates identifying, representing, and classifying information assets.

Keywords: software reusability, software productivity, information systems architecture, information asset, semantic modeling, abstraction, object-oriented systems development

ACM categories: D.2, D.2.9, D.2.m, D.3.3

## Introduction

Software reusability is viewed widely as a major opportunity for improving software productivity (Biggerstaff and Richer, 1987; Boehm, 1987a; Horowitz and Munson, 1984; Standish, 1984). Improving software productivity is critical because of the magnitude of software costs. These were estimated at roughly \$70 billion in 1985, and at over \$125 billion by 1990 for the U.S. alone (Boehm, 1988). Although in principal software reusability is a straightforward concept, there has not been significant progress in making it practical.

Studies of software reuse are contradictory but agree that, on average, one-half of all code from one application is reusable in another (Biggerstaff and Perlis, 1984; Lanergan and Grasso, 1984), and as much as 85 percent of code is reusable for some applications (Jones, 1984). In addition, it is believed that software reusability plays a central role in software productivity, maintainability, quality, portability, and standards (Bassett, 1987; Wong, 1986). Many organizations view software reusability as a technology that must be developed to ensure future competitiveness (Joyce, 1988; Prieto-Diaz and Jones, 1987; Swanson and Curry, 1989).

Lack of a clear reuse strategy has been identified as one of the major factors inhibiting widespread software reusability (Biggerstaff and Richer, 1987). The absence of an appropriate top-management reuse strategy results in project managers and programmers being unmotivated to reuse software, as well as management resistance toward allocating the up-front costs required to put software reuse into practice (Tracz, 1987a; 1987b).

Project managers and software developers often lack confidence in reusable software parts, and they frequently have little incentive to mandate software reusability. Many feel threatened that software reuse will lead to potential cuts in their own budgets and resources (Wong, 1986). As noted by Wong, “in terms of software contractors, the reuse of software may be in conflict with profit for developing, implementing, and maintaining a custom-built software application . . . there is often resistance to change and Not-Invented-Here syndrome” (p. 7).

Project managers' emphasis has focused on delivered lines of source code rather than on improving productivity of the software development process. This is in part due to the fact that demand for new software is increasing faster than our ability to develop it (Boehm and Papaccio, 1988). Boehm and Papaccio report that “the U.S. Air Force Data Systems Design Office has identified a four-year backlog of important business data processing software functions which cannot be implemented because of limited supply of personnel and training...the software backlog creates a situation which yields a great deal of bad software” (p. 1462). Both the project managers’ short-sighted view and the software backlog have resulted in a lack of commitment to development of the tools and training method needed to make software reuse practical. Two factors are likely to motivate top management to mandate software reusability. The first is from within the organization, where key decision makers may advocate an optimum reuse strategy. The second is from without, where competitors’ increased application of reuse may force the issue.

Programmers are also reluctant to reuse software for a number of reasons. It is more difficult to locate, understand, and modify existing software parts than to create new ones, especially if the original implementation lacks quality or is not designed for reuse. There is a lack of emphasis on software reuse by management/analysts, academic training courses, and traditional systems development life cycle processes and tools. Woodfield, et al. (1987) report that programmers untrained in reuse have difficulty evaluating reusability of a candidate software part.

A number of U.S. companies are reaping significant productivity increases due to cost savings associated with software reuse (Joyce, 1988; Prieto-Diaz and Jones, 1987; Swanson and Curry, 1989). These gains have been accomplished by specific actions from upper management: (1) identifying reusability as a corporate objective for the technical staff; (2) instituting company-wide, organized efforts to plan for reuse; and (3) establishing programmers' incentives for each software part accepted for a reuse library.

Matsubara, et al. (1981) describe a Japanese software factory that has made an organized effort toward software reusability. By making a decision to commit to standards and to recognize software reuse leverage, the factory has justified the cost of developing a critical mass of reusable software parts (Matsubara, et al., 1981).

Although reusability can be gained at different stages of the software development process, gaining it at the code level has long been an ultimate objective (McIlroy, 1969). However, efforts to achieve this have not been entirely successful. One of the major problems concerns understanding whether the available code needs to be modified. This is especially important when a user needs to extend the functionality of a module to be reused. Biggerstaff (1989) notes that a great deal of time is spent trying to reconstruct the software's design from the source code mainly because “the source code does not contain much of the original design information . . . such information has existed only in the minds of expert software engineers or application domain specialists” (p. 39). Tracz (1988) and Wong (1986) also suggest that ad hoc reuse is more difficult than preplanned reuse. In fact, ad hoc reuse attempts often fail.

Subroutine libraries and numerical computation routines are relatively successful cases of code reuse. According to Horowitz and Munson (1984), there are specific reasons for the success of the approach: (1) the limited and identifiable routine functionality offered by a few parameters that affect routine operation in a well-defined manner; (2) the utility of the routines in a new application regardless of the language used; and (3) the well-understood routine domains that allow the identification of standard functions and/or data types that are reusable in related applications.

There are limited payoffs associated with reusing code, especially undocumented or unstructured code, relative to the cost of the resources required to adapt the code to a new implementation and to new application requirements. This limit is also defined by the functionality or performance considerations of a new application. Considering that only about 15 percent of software development effort is devoted to coding in best project practices (Boehm, 1987b), the code reusability payoffs quickly reach a maximum due to the limited efforts usually spent on coding and the amount of code that can be reused.

Reusability at the design stage emphasizes reuse at the time of analysis and design, not after the implementation has been completed. A number of studies suggest that design for reusability is the only way software designers can approach an order-of-magnitude increase in productivity or quality (Biggerstaff and Richer, 1987). Lanergan and Grasso (1984) report that by standardizing and reusing design information and logic structures, a 50 percent gain in productivity is achieved in the development environment. Reuse potential is enhanced at the design level because implementation decisions reduce generality of the design information. Modules become less reusable the more specific they become because it is difficult to match detailed specifics. The success of the Japanese software factory, which also advocates the formalization of the software development process and products, is also attributed to design-level reusability (Matsubara, et al., 1981). The software parts are designed at the outset with reuse in mind.

Reusability at the design level is viewed as more important than reusability at the code level because (1) design activities introduce 50 percent to 60 percent of all defects during the development phase (Pressman, 1987), and (2) the cost of fixing or reworking software in the earlier phases of software life cycle is much smaller (by factors of 50 to 200) than in later phases (Boehm, 1988). Because at the design level there are more defects introduced and less costs associated with removing those defects than at the code level, a huge productivity gain is achievable by development of high-quality reusable design parts.

Technical problems associated with reusability at either design and/or code levels are due to a lack of methodologies and tools for: (1) identifying reusable software parts; (2) representing design information successfully; (3) classifying parts and implementation of an easily accessible, interactive parts catalogue; (4) translating and/or re-customizing of parts into an implementation language, and (5) composing parts into a final system.

This article proposes a strategy for improving software reusability within an organization. The strategy is for long-term organizational strategic advantage rather than short-term systems development objectives. Also proposed is a method to reduce the scope of technical problems. The following overview of software reusability research highlights how the proposed method extends and supports previous software reusability research and how it differs from the previous approaches. The proposed method and comparative review should be of special interest to practitioners and researchers.

## Overview of Software Reusability Research

Previous research has shown that the adaptability or reuse potential of a software part depends largely on the degree to which the domain analysis is performed to understand application domains and gather reusable analysis and design information (Biggerstaff and Richer, 1987; Prieto-Diaz, 1987; Tracz, 1987b). The domain analysis is necessary to identify common concepts, e.g., objects, operations and the relationships, that will form the basis for creating reusable software parts. Exploiting such a knowledge of a particular application domain has also been associated with software productivity improvements (Boehm, 1987).

An approach by Neighbors (1984) advocates using domain analysis to identify sets of common concepts in a particular application domain; in this approach, common concepts are recorded using a domain-specific language. Neighbors suggests that each domain yields a different domain representation language. The common concepts are given to a domain designer who specifies implementation for these concepts in terms of other concepts already identified in that domain. System requirements for a new application are considered in light of concepts already identified. By developing several systems for the same domain, a reuse of the domain analysis is achieved. However, as detailed by Horowitz and Munson (1984), this approach is inherently limited by a potential growth in domain languages, each of which must be mastered simultaneously.

Fischer (1987) also emphasizes the importance of domain analysis and domain-related abstractions in making reuse and redesign possible. He suggests the need for an intelligent design environment that keeps track of the levels of abstractions in a software design process. The levels of abstractions are generated throughout the entire process, from determination of system level requirements until implementation at the language level. Such an intelligent system facilitates reuse and redesign by allowing the user to change intermediate abstractions to form a slightly different system. But to do this the design of the intermediate abstraction levels must be an integral part of the software design process.

Studies have shown that the reuse potential of a software part depends largely on the degree to which the identified part, called a building block, is parameterized to facilitate the customizing process (Kaiser and Garian, 1987; Lenz, et al., 1987). A semantic representation system allowing the representation of reusable design information in factored form has been recommended (Biggerstaff and Richer, 1987; Prieto-Diaz and Freeman, 1987). Two recent developments allowing for representation of software parts in parameterized and factored forms are the Ada programming language and object-oriented approaches.

Ada is a programming language designed to facilitate reusability. Ada reusability guidelines are structured to include design for reuse, parameterization, and domain analysis. There have been extensive efforts by industry groups and research consortiums to realize software reuse with Ada (Tracz, 1987c). However, as suggested by Tracz (1987c), proposing a method for developing software based on reusable parts is language-independent; this is still an open area for research.

Object-oriented approaches seem to be the most promising methods for generating reusable software parts and composing systems (Meyer, 1987; Tracz 1987a; 1987b). Instead of building software modules by focusing on functions or detailed processing steps and sending data types between the resulting modules, these approaches use data types as the base for modularization and defining objects. In an object-oriented approach, the data types and their operations are grouped together as objects (types). Functions are performed by sending messages to the objects.

Inheritance is a key feature in an object-oriented approach toward reusability (Meyer, 1987; 1988; Stroustrup, 1988). With inheritance, new types (object-classes) may be defined by extension, specialization, and combination of previously defined types. The commonality between types is made explicit and is exploited by using the inheritance mechanism. Class (type) inheritance promotes code and design reuse because the code shared by several classes can be placed in its common superclass, and new classes can start with the code available in the superclass. The management of the composition of data types is achieved through object classes and class inheritance mechanisms.

Data types and typing, i.e., identifying new types in relation to already defined types, are the major organizing principles in object-oriented systems development. The user decides which data types are needed and provides a full set of operations for each needed type. A difficult decision in systems development using either Ada or object-oriented languages is determining which data type is needed. Making the decision correctly is very important; it affects the reusability, maintainability, and extensibility of the parts (systems) that are developed using this approach (Halbert and O'Brien, 1987).

In the next section, an asset-based system development strategy for identifying reusable design information is described. Differences between this strategy and the traditional application development are highlighted. This is followed by a description of a method for identifying information assets based on this strategy. Domain analysis and domain-related abstractions are the key features used to identify reusable design information. The method identifies the commonality among processes and data types and identifies appropriate types. These are the keys for developing reusable software parts using either functional or object-oriented approaches.

## An Asset-Based Systems Development Strategy

The asset-based systems development strategy proposed in this article emphasizes reusability at the design level rather than at the code level. It plans for software reuse at the organizational level through an integrated approach to systems development.

Figure 1 represents an asset-based systems development strategy. This strategy takes into account how the organizational strategic plan must derive the information systems strategic plan which, in turn, determines the information systems architecture (ISA) components. In this article, these components are called information systems assets. The ISA planning, modeling, and design activities are viewed as a means for proactive planning for the assimilation of technology in the organization (Devlin and Murphy, 1988; Karimi, 1988; Wardle, 1984; Zachman, 1987). This results in improved efficiency and effectiveness of the information systems resources.

The strategy shown in Figure 1 is different from traditional application-based systems development strategies (see Guimaraes, 1985) in many

![](/api/attachments/5NFN5EUB/fulltext/images/80232872eaffbbc25133fdf36980162a86845314f461203695154c3324cf0103.jpg)  
Figure 1. Asset-Based Systems Development Strategy

ways; there are differences in planning, organization, administration, and control of information resources. Such a strategy is needed because the traditional, application-oriented approach to system development is inappropriate for developing reusable software parts. The traditional approach fails to focus on: (1) planned reuse; (2) system development from an integrated perspective; and (3) long-term organizational strategic advantage. The strategy in Figure 1 requires moving away from traditional, stand-alone applications development toward an integrated approach that views systems development from an organizational perspective. It makes long-term commitments to organizational needs and translates long-term goals to short-term systems development objectives.

The proposed strategy is an extension of the concept of information assets taken from the data-driven or data-oriented concepts proposed by the National Bureau of Standards Fifth Database Workshop, as reported in Appleton (1986a). The NBS proposed five data assets: acquisition, storage, manipulation, retrieval, and distribution. Based on this strategy two distinct types of information assets are identified that are useful for improving application software reusability. These are application assets and data assets.

Application assets refer to design components/abstractions, e.g., logic structures, repeated many times across applications. By identifying and standardizing these abstractions and defining them logically in a single place, the potential for redundancy at both design and code levels is addressed prior to implementation. When the design information is not identified and defined logically across applications in an integrated manner, it cannot be constructed and maintained in a single place; it cannot be reused.

Data assets are associated with application assets. They capture objects, classes of objects, operations, and relationships in application assets as semantic data models. This knowledge captures the meaning of the application assets and encompasses the implicit and explicit restrictions placed upon objects, operations, and relationships associated with the application assets. Capturing semantic knowledge associated with the application assets makes it possible to implement, reuse, and maintain application software easily by using vocabularies that relate directly to the meaning of the applications.

Although the concepts of asset and asset development are not new (Appleton, 1986b), proposing a method for identifying design abstractions to create information assets has not been addressed before. As Appleton (1986a) notes, the traditional approach to software development not only ignores information assets and assets development but also does not take into account the possibility of reusing assets. Appleton states further that the development of data assets is still “black magic” in most projects. He advocates that a project team define assets during planning and that new system requirements be defined in terms of existing assets.

## A Method for Identifying Information Assets

The method proposed allows identification of the commonality among data and process types, the bases for identifying information assets. By identifying commonality at the organizational level, multiple development and maintenance efforts are avoided. At the applications design level redundancies are consolidated and information assets are constructed and maintained once, even though they may exist physically in multiple applications at the implementation level.

To identify information assets, the data and processes making up the ISA need to be integrated at an organizational level. Inmon (1984; 1986) suggests an approach for such an integration process. Extending on Inmon's approach, the following method can be used for identifying information assets: (1) identify the scope of integration; (2) build a semantic model of the scope; (3) identify application and task categories; and (4) identify application and data assets. These steps are detailed below in an example adopted from Inmon (1986).

## Identifying the scope of integration

The scope of integration is defined as a statement of which data and processes requirements are to be included in the integration process and which are to be excluded. Determining the “right scope” is a strategic decision. It consists of balancing the long-range and short-term goals of the organization and distinguishing what can be done from what would be nice to do.

Integration can be done at several levels: subsystem (module); functional (application); and operational mode (decision support, administrative, operational). Each scope of integration should contain only one operational mode, but scope of integration may cover broad functional lines. For example, operational systems are usually separate from administrative systems.

## Building a semantic model of the scope

Both a top-down and bottom-up analysis should be used in any integrated modeling process. A bottom-up analysis assures that all details are accounted for; but alone it cannot guarantee identification of major components and the inherent structure of the system. In contrast, a top-down analysis alone cannot guarantee that all details of processes and data are represented.

Semantic modeling techniques are viewed as ways of integrating and formalizing information systems requirements (Hull and King, 1987; Potter and Trueblood, 1988). The important result of semantic model research is the development of mechanisms for representing the structural aspects of business data using objects, attributes, type constructors for building complex types, and IS-A relationships (e.g., IS-A type-of, IS-PART-OF, IS-INSTANCE-OF).

In semantic modeling any concept or thing is first identified as an object; the objects are then organized into object-types or classes. Relationships between objects are viewed using different abstraction mechanisms; generalization, aggregation, or classification (Smith and Smith, 1977).

In generalization, similar objects are abstracted into higher-level object-types via the IS-A/SUBSET-OF relationship. This allows a designer to view similar objects relative to a more generic object. In aggregation, an object is related to its sub-components via IS-PART-OF relationship. This allows a designer to model an abstract object based on the properties or attributes of the object. Aggregation, therefore, involves specifying the structural components of an object. In classification, specific instances of object-type are related to a higher-level object-type via the IS-INSTANCE-OF relationship.

In semantic modeling of the scope of integration, the goal is to ensure that all major objects are represented and appropriately related to each other. Semantic modeling with a top-down analysis is similar to a decomposition process in which the base object types are defined first and the subtypes are defined from these in a top-down fashion.

As an example, assume the financial system of a bank is chosen as the scope of integration to be decomposed according to lines of internal organization of the bank as shown in Figure 2. The semantic modeling of this scope, however, emphasizes the business of the corporation rather than the organizational structure of the corporation; the mechanism used to relate the object types concerns function of the types. In Figure 2 the IS-A relationships are undirected and, like knowledge representation in artificial intelligence, when using semantic networks each object is represented by a node.

In decomposition the intent is to select common processes at each level of decomposition by generalization abstractions. However, as shown in Figure 2, at each level of decomposition (e.g., commercial, retail) each activity has functions unique to itself. For this reason, retail banking is subdivided further. The decomposition stops at the point of lowest functional distinction; that is, at the point at which the functional activities cannot be subdivided into a lower set of distinctive functions. Decomposition stops at the car loans and the signature loans because the subactivities of these activities, e.g., interest loan calculations, are not useful to distinguish between a car loan and a signature loan.

![](/api/attachments/5NFN5EUB/fulltext/images/23695bf499df2d03c306200b85c38053cb0bd22bc665b1058800f2f6f42eb27b.jpg)  
Figure 2. Generalization Abstractions of the Financial Systems of a Bank

Semantic modeling is done at the data level. On the data view side, entity-relationship diagrams (ERDs) are derived for the scope of integration (Chen, 1976). The most fundamental difference between an ER model representation and the representation above is the absence of the IS-A relationship in the ER representation. Also, in the ER model the use of attributes and relationships is restricted; attributes may be defined on both object-types and relationships; relationships are given a name and are viewed as entities themselves. Relationships in an ER model can be viewed as aggregation abstractions.

In building the global ERD, as with the generalization hierarchy in Figure 2, emphasis is on selecting common entities. In Figure 2, operational systems could be divided into two separate ERDs: a commercial ERD and a retail ERD. However, because of the commonality of entities and processes in the two modes of operation, one ERD is constructed that reflects both the commercial and the retail business of the bank. The entities and relationships within the scope of integration are consolidated using generalization/aggregation abstractions to construct the global ERD represented in Figure 3.

Figure 3 illustrates a global ERD representing the financial activities that occur inside the bank. Management of an account is the highest level of abstraction within the scope of integration. In this context, “account” can be either an extension of the bank’s money or resources to an individual or enterprise with the expectation of repayment, i.e., a loan, or it can be the acceptance of money by the bank for steward-ship, e.g., a savings deposit. The global ERD is useful to identify (1) relevant data inside the scope of the integration; (2) the primary business of the corporation at the highest level of abstraction; and (3) application and task categories.

## Identifying application and task categories

Primary business processes are identified at the same level of abstraction as the global ERD model shown in Figure 3. The focus is on identifying all processes that are fundamentally different; once the primary processes are identified they are defined and the processing cycle is identified.

![](/api/attachments/5NFN5EUB/fulltext/images/697b587883a87a2ecb63c88a3d6550e830ce44d0cc31c4c438d9193850a0d8af.jpg)  
Figure 3. Global ERD for a Retail Business of a Bank

As shown in Figure 4, the primary business processes common to the global ERD are acceptance of account, establishment of terms of account between bank and the customer, transaction against account (e.g., payment, credit), and account-related calculations. Using aggregation abstractions for each of the primary business processes, the functional activities (application categories) of the bank are identified. Four application categories representing the bank's four major accounts are: loan, demand-deposit, time-deposit, and credit card.

Both loan and time-deposit accounts are forms of “managing accounts.” While the bank may manage other types of accounts (e.g., trust accounts), the major bank accounts are included in the application categories. Also, more specific banking services, such as interest payment, interest collection, and activity charges can be classified as a subset of the four basic accounts identified.

Using aggregation abstractions, the application categories are expanded to subactivities. Figure 5 shows the subactivities of each application category.

For each application category (e.g., loan), unique subactivities (e.g., get credit check), and common subactivities across application categories (e.g., accept payment), are identified. Unique subactivities account for minor differences between the application categories that are most often related to errors and exceptions that are a part of the processing cycle. They are not considered to be part of the primary business of the corporation and are ignored during identification of application and task categories.

Common subactivities are repeated in many application categories. These subactivities are consolidated across application categories by generalization abstractions in order to form the two generic task categories shown in Figure 6: credit and payment. Using classification abstractions, generic task categories are related to application categories, as shown in Figure 7.

Using aggregation abstractions, task categories are decomposed to detail subtask level in order to identify the common processes of each task category. The relationships of each application category to the task categories and to the common processes at a lower level of abstraction are shown in Figure 8.

## Identifying application assets

The common processes for each task category are the basis for reusable design information. Table 1 relates the application categories to the credit task category and the common processes. As shown in Table 1, the common processes serve the same concepts across application categories; their detailed processing steps, however, are slightly different at the implementation level.

The standardized forms of the design information are the information assets that can be reused

![](/api/attachments/5NFN5EUB/fulltext/images/d789fe8381dead0b6589ca7d483623f9179c45f77cfb65c7181e12542f81b2df.jpg)  
Figure 4. Primary Business Processes and Application Categories

![](/api/attachments/5NFN5EUB/fulltext/images/a6d490ae954734f8dfb94301668ecc7e3699b6e5ff53debf21108533df7cc45e.jpg)  
Figure 5a. Sub-Activities of Each Application Category

across applications. By standardizing the definition of this design information, multiple implementation and maintenance efforts are avoided across applications. Standardization of the design information for the purposes of application assets representation and classification can be done using either functional or object-oriented approaches. The selection of a particular approach is influenced highly by the representation and implementation languages already used in the organization and the organization's plans for future use of those languages.

## Functional Approach

The functional approach to standardizing common processes can be achieved by specifying input, output, and detail-processing steps. The generalized application assets (common processes) comprise the code skeleton common to

![](/api/attachments/5NFN5EUB/fulltext/images/92e1cef10d11153546667223aa25d6dfa77b73a3ec112f2c59538ae66784b0ef.jpg)  
Figure 5b. Sub-Activities of Each Application Category

all specific applications. The related application program can be constructed by specifying those parts that have been left open in the generic application asset. In Figure 9, the representations of “verify date” and “amount of payment” are given in a pseudocode style using the functional approach. From this representation it is easy to see how pseudocode specification can be translated into a programming language.

For classification purposes, generalization/specialization rules can be specified for each task category. These specialization rules can consist of rules for constants, procedures, and interfaces, but each task category requires specification of different properties by a specialization rule. Mittermeir and Oppitz (1987) demonstrate the feasibility of building a software base management system that contains design information for task or application categories. This information is reused by completing it with different specialization rules for each task or application instance.

![](/api/attachments/5NFN5EUB/fulltext/images/8e65ef1b5aa9c8112a4bb8408811a8c1c6cb73479d806953bb80e26be2aee166.jpg)  
Figure 6. Generic Task Category Derived Using Generalization Abstractions

![](/api/attachments/5NFN5EUB/fulltext/images/697f758b61bd8b1ad40f1b38940641f802e5fac679dd9a2a2c479f90896cc4ce.jpg)  
Figure 8. Relationships Among Application Categories, Task Categories, and Common Processes

Table 1. Design Information for the Task Category Credit

<table><tr><td rowspan="2">Application Categories</td><td colspan="4">Task Category (Credit)</td></tr><tr><td>Verify Date, Amount of Credit</td><td>Verify Form of Credit</td><td>Calculate Interest, Charges</td><td>Record Payment</td></tr><tr><td>Loan Account</td><td>Verify Date, Amount of Credit on Loan</td><td>Verify Form of Credit on Loan</td><td>Calculate Interest, Charges on Loan</td><td>Record Payment on Loan</td></tr><tr><td>Demand-Deposit Account</td><td>Verify Date, Amount of Credit on Demand-Deposit</td><td>Verify Form of Credit on Demand-Deposit</td><td>Calculate Interest, Charges on Demand-Deposit Account</td><td>○</td></tr><tr><td>Time-Deposit Account</td><td>Verify Date, Amount of Credit on Time-Deposit</td><td>Verify Form of Credit on Time-Deposit</td><td>○</td><td>○</td></tr><tr><td>Credit Card Account</td><td>Verify Date, Amount of Credit on Credit Card</td><td>○</td><td>○</td><td>○</td></tr></table>

## Object-Oriented Approach

The inheritance mechanism represents what is called an IS-A relation in the semantic modeling technique. However, by inheriting methods (i.e., operations among types rather than attributes), focus is on capturing behavioral rather than structural aspects of application domains.

The proposed method identifies abstract data types useful for implementation in the objectoriented paradigm. As mentioned earlier, identification of appropriate data types is considered to be a major problem for object-oriented development. In the example, credit is a data type. Credit IS-INSTANCE-OF the four application categories; they are the supertypes for the Credit task category. Figure 10 is a graphical representation of the object-oriented development for the Credit task category.

Each type (e.g., credit loan) has a supertype (i.e., Credit) from which it inherits operations (methods) (e.g., verify amount and payment) and internal structure (i.e., storage representation for instance variables such as payment-amount). A type (class) can add to operations it inherits or it can redefine inherited operations. However, a type cannot delete the inherited operations. But different object-oriented languages allow varying degrees of control over what can be inherited and what can be overridden.

```txt
INPUT:
Account
Amount
Date
Ttype—transaction type—
(loan, time-deposit, demand-deposit, credit card)
Transfer to (*)
Special handling authorization

OUTPUT:
Valid account (y/n)
Valid amount (y/n)
Valid date (y/n)
Valid transfer (y/n)*
Valid transaction (y/n)

*optional, depending on activity

PROCESSING:
SET Valid account, Valid amount, Vaild date, Valid transfer,
Valid transaction to n
READ Account
IF Account valid and existing
Valid account=y
IF Date vaild—83<=yr<=88; 1<=mo<=12; 1<=day<=31
Valid date=y
IF Amount valid—0<=Amount <=10,000
& Special handling # 'bb'
Valid amount=y
IF Transfer to # 'bb'
RETRIEVE Transfer to Account
IF Transfer to Account Valid and Existing
Valid transfer=y
IF Valid account=y
IF Valid amount=y
IF Vaild date=y
Valid transaction=y
IF Transfer to # 'bb'
IF Valid Transfer=y
Valid transaction=y
```  
Figure 9. A Functional View for the Verify Date and Amount of Payment Application Asset

Operations have two subparts: interface and implementation. The interface defines the external characteristics of operations (i.e., name, type of arguments operations takes, messages to which an object can respond), and the implementation of the operation (i.e., actual code). Often a super-type describes the interface to the operations of the type but it omits some or all of the implementations of those operations. Supertypes, therefore, characterize the functionality that is common to all of their subtypes.

Among the difficult technical problems associated with designing reusable module structures is the need to take into account the commonalties existing between groups of related data and process types. The proposed method accounts for identification of these commonalties. By defining common processes as far up in the IS-A hierarchy as possible, definitions can be shared, without redefinition, by the greatest number of descendant classes (subtypes). In short, definitions can be reused.

By subtyping, commonality between types is accounted for in supertypes. Also, subtypes that recognize details and differences between types are created. A subtype is, therefore, a specialization of the supertype; conversely a supertype is a generalization of its subtypes. A mistake common among novice object-oriented programmers is avoided: typing is not used to represent aggregation abstractions (Halbert and O'Brien, 1987).

Object-oriented languages, by providing facilities to redefine the operations within a type and by supporting dynamic binding, facilitate reusability and flexibility in software development. Dynamic binding allows the user to request an operation with more than one data type without having to specify which type should be applied. These key features allow a design to be parameterized, represented, and developed in factored form.

## Identifying data assets

Data assets are defined as semantic knowledge associated with application and task categories. They are the implicit and explicit restrictions placed on objects, operations, and relationships within the application domain. By extracting this knowledge and defining it using semantic modeling techniques and tools (Borgida, 1985; Hull and King, 1987; Potter and Trueblood, 1988), the knowledge is standardized. It becomes reusable among several applications. As a result, the meanings of application assets are captured in the form of data assets rather than being embedded in the constraints and procedures involved in disparate applications.

![](/api/attachments/5NFN5EUB/fulltext/images/b009bdd82e6daed0ab275c7bdf53f7fc825bef8da429951b517f66fe3d3e1cf0.jpg)  
Figure 10. A Graphical Representation of an Object Oriented Development for the Credit Task Category

Figure 11 shows a partial credit data asset specification in a generic form that illustrates the data asset concept. It should be noted, however, that a number of semantic models are incorporated into programming languages; some of these languages allow direct translation of a semantic model from graphical form to language syntax. Although the syntax varies widely among these languages, they all support various forms of abstractions. In fact, extensive support for data abstractions is a key distinction between these languages and data dictionary directory systems. Also, these languages are not intended to be a DBMS; they are designed to support programming languages that encompass data management facilities based on semantic models.

OBJECT-TYPE: Loan
HAS-ATTRIBUTES:
Acct-number: INTEGERS;
Acct-balance: REAL;
Interest-rate: REAL;
Date: INTEGERS;
Payment-amount: REAL;
Credit-amount: REAL;

IS-A Credit;
IS-A Payment;
END-OBJECT-TYPE

OBJECT-TYPE: Credit
HAS-ATTRIBUTES:
Transaction-type: STRING;
Form-of-payment: STRING;
Interest-charges
DERIVATION: CALCULATION()
Acct-balance \*Interest-rate
Principal-payment
DERIVATION: CALCULATION ()
Payment—Interest-charges
Acct-balance
DERIVATION: CALCULATION ()
Acct-balance—Principal-payment

IS-A Credit—Loan;
IS-A Credit—Demand-Deposit
IS-A Credit—Time-Deposit
IS-A Credit—Credit card;
IS-INSTANCE-OF Loan;
IS-INSTANCE-OF Demand-Deposit;
IS-INSTANCE-OF Time-Deposit;
IS-INSTANCE-OF Credit card;

END-OBJECT-TYPE

Figure 11. A Partial Specification for the Credit Data Asset

Capturing structural aspects of application assets in the form of data assets makes this knowledge accessible and reusable in similar but different software development efforts. This results ultimately in eliminating some of the cost and rework currently experienced in software development projects.

## Management, Economic, and Integration Issues

The asset-based systems development strategy and the proposed method require a corporate infrastructure that encourages and rewards software reuse. It requires that top management understands the critical role of software reuse; it requires participation of project management and software experts in strategic information systems planning. These are essential requirements if top management is to address non-technical issues (e.g., legal and proprietary rights, compensation for the developers of reusable parts, internal cost apportionment methods for purchasing reusable parts, etc.) associated with software reuse. These are equally as important as the technical issues.

The economics of software reuse vary significantly with the problem domain and the development technology employed within an organization (Barnes, et al., 1987). Before software reuse starts to pay off, it requires an up-front investment in establishing and maintaining a library of reusable parts. The cost of establishing such a library varies depending on the library size and the tools used to populate, organize, access, and maintain the library. Widespread software reuse also requires experience in budgeting, scheduling, and managing a software development library.

The proposed method is based on data and process modeling, which allows easy integration of this method with the structured analysis and data modeling techniques. Furthermore, the CASE (computer aided software engineering) development environments support both data and process modeling tools (Chikofsky, 1988). These development environments allow for management of the integration of data and process models that use a central data dictionary. Through common notation that promotes standardization of documentation and development techniques, reuse of existing subsystems is supported. Currently, CASE development environments do not support code reusability or the use of expert systems technology to generate applications from rule-based specifications; CASE development environments also need to develop support tools for object-oriented software development.

## Summary and Conclusions

This article has reviewed and extended recent research on software reusability. It promotes the view that the traditional approach to software development lacks focus on (1) planned reuse; (2) system development from an integrated perspective; and (3) long-term organizational strategic advantages. Yet these are critical to making software reusability practical.

This article emphasizes an organizational strategy for software reusability. An asset-based systems development method based on this strategy is also presented. The proposed method requires the integration of data and process modeling through the use of semantic modeling techniques and tools. Such an integration eliminates redundancy in data and process definition within the scope of integration. Removing such redundancies results in elimination of multiple development and maintenance efforts. It also permits commonalties among data and processes, which are the bases for software reusability, and the identification and development of application assets and data assets. The method emphasizes reusability at the design rather than at the code level; it supports both functional and object-oriented systems development approaches.

As reusability technology matures, organizations will be pressured to adopt the new technology. Inability to respond to this challenge in a timely manner could preclude future competitiveness of many organizations.

## References

Appleton, D.S. “Information Asset Management,” Datamation, February 1, 1986a, pp. 71–76.

Appleton, D.S. “Very Large Projects,” Datamation, January 15, 1986b, pp. 63–69.

Barnes, B., Durek, T., Gaffney, J. and Pyster, A. "A Framework and Economic Foundation for Software Reuse," Software Productivity Consortium, Reston, VA, June 1987, pp. 1–12.

Basset, P.G. “Frame-Based Software Engineering,” IEEE Software (4:4), July 1987, pp. 9–15.

Biggerstaff, T. “Design Recovery for Maintenance and Reuse,” IEEE Computer (22:6), July 1989, pp. 36–48.

Biggerstaff, T. and Perlis, A. “Forward: Special Issue on Software Reusability,” IEEE Transactions on Software Engineering (10:5), September 1984, pp. 474–476.

Biggerstaff, T. and Richer, C. “Reusability Framework, Assessment, and Directions,” IEEE Software (4:2), March 1987, pp. 41–48.

Boehm, B.W. “Improving Software Productivity,” IEEE Computer (20:9), September 1987a, pp. 43–57.

Boehm, B.W. “Industrial Software Metrics Top 10 List,” IEEE Software (4:5), September 1987b, pp. 84–85.

Boehm, B.W. and Papaccio, P.N. “Understanding and Controlling Software Costs,” IEEE Transactions on Software Engineering (14:10), October 1988, pp. 1462–1477.

Borgida, A. “Features of Languages for the Development of Information Systems at the Conceptual Level,” IEEE Software (2:1), January 1985, pp. 63–72.

Chen, P.P. “The Entity-Relationship Model: Toward a Unified View of Data,” ACM Transactions on Database Systems (1:1), March 1976, pp. 9–36.

Chikofsky, E.J. “Software Technology People Can Really Use,” IEEE Software (5:2), March 1988, pp. 8–10.

Devlin, B.A. and Murphy, P.T. "An Architecture for a Business and Information System," IBM Systems Journal (27:1), 1988, pp. 60–80.

Fischer, G. “Cognitive View of Reuse and Redesign,” IEEE Software (4:4), July 1987, pp. 60–72.

Guimaraes, T. “A Study of Application Program Development Techniques,” Communications of the ACM (28:5), May 1985, pp. 494–499.

Halbert, D.G. and O'Brien, P.D. "Using Types and Inheritance in Object-Oriented Programming," IEEE Software (4:5), September 1987, pp. 71–79.

Horowitz, E. and Munson, J.B. "An Expensive View of Reusable Software," IEEE Transactions on Software Engineering (10:3), September 1984, pp. 477–487.

Hull, R. and King, R. “Semantic Data Base Modeling: Surveys, Applications, and Research Issues,” ACM Computing Surveys (19:3), September 1987, pp. 201–260.

Inmon, W.H. Integrating Data Processing Systems, In Theory and in Practice, Prentice-Hall, Englewood Cliffs, NJ, 1984.

Inmon, W.H. Information Systems Architecture: A System Developer's Primer, Prentice-Hall, Englewood, Cliffs, NJ, 1986.

Jones, T.C. “Reusability in Programming: A Survey of the State of the Art,” IEEE Transactions on Software Engineering (10:5), September 1984, pp. 488–493.

Joyce, E.J. "Reusable Software: Passage to Productivity?" Datamation, September 15, 1988, pp. 97–102.

Kaiswer, G.E. and Garian, D. "Melding Software Systems from Reusable Building Blocks," IEEE Software (4:4), July 1987, pp. 17–24.

Karimi, J. “Strategic Planning for Information Systems: Requirements and Information Engineering Methods,” Journal of Management Information Systems (4:4), Spring 1988, pp. 5–24.

Lanergan, R.G. and Grasso, C.A. “Software Engineering with Reusable Designs and Code,” IEEE Transactions on Software Engineering (10:5), September 1984, pp. 498–501.

Lenz, M., Schmid, H.A. and Wolf, P.F. "Software Reuse Through Building Blocks," IEEE Software (4:4), July 1987, pp. 34–42.

Matsubara, T., Sasaki, O., Nakajim, K., Takezawa, K., Yamamoto, S. and Tanaka, T. "SWB System: A Software Factory," in Software Engineering Environments, H. Hunke (ed.), North-Holland Publishing Company, Amsterdam, 1981, pp. 305–318.

McIlroy, M.D. "Mass Produced Software Components," Proceedings of 1969 NATO Conference on Software Engineering, Garmitch, Germany, 1969, pp. 89–98.

Meyer, B. “Reusability: The Case for Object-Oriented Design,” IEEE Software (4:2), March 1987, pp. 50–64.

Meyer, B. Object-Oriented Software Construction, Prentice-Hall, Englewood Cliffs, NJ, 1988.

Mittermeir, R.T. and Oppitz, M. “Software Bases for the Flexible Composition of Application Systems,” IEEE Transactions on Software Engineering (13:4), April 1987, pp. 440–460.

Neighbors, J.M. “The DRACO Approach to Constructing Software From Reusable Components,” IEEE Transactions on Software Engineering (10:5), September 1984, pp. 564–574.

Potter, W.D. and Trueblood, R.P. “Traditional, Semantic, and Hyper-Semantic Approaches to Data Modeling,” IEEE Computer (21:6), June 1988, pp. 53–63.

Pressman, R.S. Software Engineering: A Practitioner's Approach, Second Edition, McGraw-Hill, New York, NY, 1987.

Prieto-Diaz, R. “Domain Analysis for Reusability,” Proceedings of COMPSAC 87, Tokyo, Japan, October 1987.

Prieto-Diaz, R. and Freeman, P. “Classifying Software for Reusability,” IEEE Software (4:1), January 1987, pp. 6–16.

Prieto-Diaz, R. and Jones, G. “Breathing New Life into Old Software,” GTE Journal of Science and Technology (1:1), Spring 1987, pp. 23–31.

Smith, J.M. and Smith, D.C. "Data Base Abstractions: Aggregation and Generalization," ACM Transactions on Data Base Systems, June 1977, pp. 105–133.

Standish, T.A. “An Essay on Software Reuse,” IEEE Transactions on Software Engineering (10:5), September 1984, pp. 494–497.

Stroustrup, B. "What is Object-Oriented Programming?" IEEE Software (5:3), May 1988, pp. 10–20.

Swanson, M.E. and Curry, S.K. "Results of an Asset Engineering Program," Information and Management (16:4), 1989, pp. 207–216.

Tracz, W. “Software Reuse: Motivation and Inhibitors,” Proceedings of COMPCON 87, San Francisco, CA, February 1987a, pp. 358–363.

Tracz. W. "RMISE Workshop on Software Reuse Meeting Summary," Proceedings of the Rocky Mountain Institute for Software Engineering, Boulder, CO, October 14–16, 1987b, pp. 1–12.

Tracz, W. “Ada Reusability Efforts—A Survey of the State of the Practice,” Proceedings of the Fifth National Conference on Ada Technology and Fourth Washington ADA Symposium, Washington, D.C., March 1987c, pp. 35–44.

Tracz, W. “Software Reuse Myths,” ACM SIGSOFT (13:1), January 1988, pp. 17–21.

Wardle, C. “The Evolution of Information Systems Architecture,” Proceedings of the Fifth International Conference on Information

Systems, Tucson, AZ, November 1984, pp. 205–217.

Wong, W. “Management Overview of Software Reuse,” Technical Report PB87-109856/XAB, National Bureau of Standards, Gaithersburg, MD, 1986.

Woodfield, S.N., Embley, D.W. and Scott, D.T. "Can Programmers Reuse Software," IEEE Software (4:4), July 1987, pp. 52–59.

Zachman, J.A. "A Framework for Information Systems Architecture," IBM Systems Journal (26:3), 1987, pp. 276–292.

## About the Author

Jahangir Karimi is assistant professor of management information systems at the University of Colorado at Denver. He received his M.S.

and Ph.D. degrees from the University of Arizona, Tucson. His research interests include information systems management, strategic planning for information systems, information systems modeling, analysis and design, and software engineering. Recently he was invited by the National Academy of Science and the Chinese Review Commission of the Chinese University Development Project to teach a class in systems analysis and design to a group of Chinese faculty members at Fudan University in Shanghai, People's Republic of China. He has published in IEEE Transactions of Software Engineering, Communications of the ACM, MIS Quarterly, Journal of Management Information Systems, and a number of conference proceedings. Dr. Karimi is a member of the Association for Computing Machinery, the Computing Society, and the Society for Information Management.
