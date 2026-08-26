---
otero_id: 6632
otero_key: "4X2BK5SS"
title: "Dimensional modeling: Identification, classification, and evaluation of patterns"
authors: "Mary Elizabeth “M.E.” Jones; Il-Yeol Song"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.12.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dimensional modeling: Identification, classification, and evaluation of patterns

Mary Elizabeth “M.E.” Jones <sup>a,⁎</sup>, Il-Yeol Song <sup>b</sup>

<sup>a</sup> Immaculata University Department of Mathematics–Computer Science–Physics Immaculata, PA 19345, United States <sup>b</sup> Drexel University College of Information Science and Technology Philadelphia, PA 19104, United States

Available online 10 January 2007

## Abstract

Software design is a complex activity. A successful designer requires knowledge and training in specific design techniques combined with practical experience. Designing a dimensional model embodies this challenge. This paper presents Dimensional Design Patterns (DDPs) and their application to the design of dimensional models. We describe a metamodel of the DDPs and show their integration into Kimball's dimensional modeling design process so they can be applied to design problems using a known practice. By providing a metamodel and a method for DDP use, we combine theory and a practical design technique with the goal of increasing the efficiency and effectiveness of the software designer. The experimental results show that the classroom use of DDPs increase the effectiveness by 25% and efficiency by 9% for students in designing dimensional models. This research shows that DDPs could be an effective tool not only for teaching a dimensional model in academia, but also for designing dimensional models in an industry setting. © 2006 Elsevier B.V. All rights reserved.

Keywords: Data warehouse; Dimensional modeling; Data models; Design; Patterns; Software engineering

## 1. Introduction

Research and experience suggest that software design is difficult and time consuming. Brooks discussed the difficulties involved in designing and implementing large systems when he stated: “plan to throw the first one away” [5]. The expertise for designing systems is acquired over a period of time by repeatedly performing design activities and refining the understanding of the system. Therefore, a first system can be considered a prototype that builds knowledge and experience. As a result, software engineers continually seek methods for improving the efficiency and effectiveness of the design process. Concentration on design techniques alone, however, has not guaranteed successful design solutions [5]. The challenge remains — how do software engineers obtain experience in order to create effective solutions?

A data warehouse is an integrated data repository specifically designed for performing analysis. The data for the data warehouse come from online transaction systems. That data is extracted, integrated, and stored in a dimensional model schema. Business analysts perform tasks such as trend, time series, market, and risk analysis while data mining algorithms are used to uncover unknown information.

Like other software design projects, data warehousing projects are complex, large, and difficult to design. Compounding the design difficulties is the lack of detailed guidance regarding dimensional modeling. Several books provide data warehousing design strategies by documenting the dimensional models that solve specific data warehousing problems [1,13,14,15,17]. Organized by subject area, the referenced books describe and exemplify specific dimensional modeling techniques in relation to specific business applications. These books are intended to assist data warehousing practitioners in understanding data warehouse design by studying and learning from the examples of those more experienced in data warehouse design and implementation. Because the examples represent approaches to specific situations they may not address a given practitioner's particular design problem, but they are nonetheless valuable.

Our research examines those dimensional models, identifies commonly occurring concepts and entities, and abstracts them into Dimensional Design Patterns (DDPs). In addition to the identification and classification of DDPs, their application toward creating new or evaluating existing dimensional models is equally important. When designing a dimensional model, designers consider the data that exists in on-line transaction systems, as well as the user requirements. The purpose of the DDPs is to triangulate the design process. In other words, a designer can use the DDPs in conjunction with the on-line transaction data and the user requirement to design or evaluate a dimensional model. Thus, this paper presents Dimensional Design Patterns (DDPs) and their applications to the design of dimensional models.

The idea to develop DDPs resulted from 1) observing a variety of books on patterns in other software areas, 2) knowing there was a lack of detailed guidance for designing dimensional models, 3) questioning whether patterns would be an appropriate mechanism for assisting data warehousing practitioners when creating dimensional models, and 4) wanting to create a structured method that is both useful and useable when thinking about, discussing, determining, and reviewing dimensional models.

The primary contributions of this paper are as follows. First, we present a taxonomy of patterns (DDPs) abstracted from over 50 case studies. The DDPs include three types: domain, fact and implementation DDPs. Second, through a DDP example, we illustrate the applicability of the Domain DDPs to an existing dimensional model. Third, our initial experiments show that the DDPs significantly increase the effectiveness of the design and reduce the time to design dimensional models.

Our research showed that the subjects using the DDPs were approximately 9% more efficient and approximately 25% more correct with their solutions than the subjects not using the DDPs. Our initial experimental results, however, reveal that more experimental data is required before drawing definitive conclusions regarding the effectiveness and efficiency of the DDPs.

The remainder of this paper is organized as follows: Section 2 provides background information regarding data warehousing, dimensional modeling, and software patterns. Section 3: (a) presents the driving concepts used to create the DDPs in order to increase DDP usefulness and usability, (b) details the three types of DDPs: domain, fact, and implementation, (c) illustrates the applicability of Domain DDPs to an existing dimensional model, and (d) describes how to apply the DDPs when designing a dimensional model. Section 4 describes the research study and also documents and discusses the initial results. Section 5 provides conclusions and future work.

## 2. Background

## 2.1. Data warehousing and the dimensional model

Data warehousing databases are usually conceptualized using a dimensional model and implemented using the star schema. A dimensional model is a “specific discipline for modeling data that is an alternative to entity relationship modeling” [14]. Like an entity relationship schema, a dimensional schema reflects a data structure. However, a dimensional schema is specifically designed to store data in a way that 1) emphasizes user understandability, 2) enhances query performance, and 3) accommodates change [8,14]. To achieve these design characteristics, a dimensional schema is typically denormalized.

A dimensional schema is composed of two types of tables: 1) a fact table and 2) a dimension table. The schema associated with a dimensional model is referred to as a star schema since pictorially its structure resembles a star. The fact table is centrally located with the dimension tables “radiating” outward from the fact table. Fact tables contain foreign keys and measurements. Dimension tables represent and capture business entities used for analyzing the measurements. Dimension tables contain primary keys which associate the dimension attributes to the fact table, and textual descriptions which describe the attributes or characteristics of the business entities.

## 2.2. What is a pattern?

The literature on patterns provides numerous definitions. As a result of studying those many definitions [2,3,4,6,7,9,10,11,12,16,18,20] it becomes clear that the following characteristics are evident in those definitions.

□ The problem that the pattern addresses is identified, recognized, and defined from real world situations.

□ A pattern provides an approach for formulating a solution to a real world problem.

□ The approach must be defined with respect to the real world context from which the problem emanates.

□ The approach is reusable because it has been successfully used to solve recurring real world problems.

□ A pattern endures over time.

In reviewing dimensional models, similarities in structure and content appear within, and in some cases, across subject areas. Since similarity is a prerequisite for pattern development it appears that pattern development for data warehousing applications is a promising research area.

## 3. Dimensional design patterns (DDPs)

The purpose of the DDPs is assisting data warehousing practitioners when designing dimensional models by providing an approach for identifying dimensions in a systematic and usable way. When studying existing dimension tables, one begins to observe categories of repeated requirements that manifest themselves across the design of many dimensional models. Kimball's examples [15]) and Adamson and Venerable's examples [1] were the basis for identifying the DDPs.

In order to create useful and usable DDPs the following criteria were adhered to:

□ DDPs are explained via a commonly known and recognized mental model with the intent of increasing the practitioner's ability to understand, remember, and apply the DDPs.

□ DDPs facilitate the identification of commonly used entities thereby providing a greater potential for improving design correctness with the initial model.

□ DDPs are common across many dimensional models, thus reusability is improved and design time may be decreased.

## 3.1. DDP mental model

Through research studies in human computer interaction designers recognize the importance of employing common mental models as design strategies for creating useful and usable interfaces. Software patterns can be difficult to learn, remember and apply. Therefore DDPs are explained via a commonly known and recognized mental model with the intent of increasing the practitioner's ability to understand, remember, and apply the DDPs. The mental model used for teaching students to write a story is the basis for Domain DDPs. The writer considers the “who, what, when, where, and why” components of the story. Each component integrates various aspects of the tale in a creative yet structured way.

The characters involved in the story are created and developed when considering the “who” component. Stories usually refer to important entities and the ideas for those entities are generated when considering the “what” component. Every story is set within a particular time frame and the “when” component aids the writer in identifying the time period. The story location is of particular importance and the “where” component aids the writer in determining the story's setting. The motivation or the reasons behind the story are determined by considering the “why” aspects of the story.

When studying existing dimensional models, it becomes apparent that each model reflects the past activities of a business. Historical data can be assembled and queried in a way that tells a variety of stories. In some cases, business analysts may know or suspect those stories or they may uncover stories that have surprise endings. Therefore the telling of a story is a reasonable mental model for identifying the potential dimensions for a dimensional model.

## 3.2. Domain DDPs

The Domain DDP Class Diagram (Fig. 1) presents core dimensions presented in a class diagram against which measurements (facts) are taken and questions are posed. The Domain DDPs are classified as the following types: temporal (when), location (where), stakeholder (who), action (what is done or accomplished), object (what), and qualifier (why).

When performing analyses, it is important to know when events occur. Facts are historical and those facts need to be placed in the context of a time period in order for the software engineer to perform meaningful analysis. As observed in the dimensional models studied, a time period is typically described in terms of the traditional calendar year, fiscal calendar, time, and/or a special period. Therefore, the temporal DDP is represented as an aggregate of the traditional calendar year, fiscal calendar, time, and special period classes (Fig. 2).

At times it is necessary to place facts in the context of where they occur. Therefore, the obvious use of the location class is capturing a specific locale (e.g., region, state, city, township, etc.) for a facility (e.g., store, warehouse, etc.). However it may also be helpful to gain knowledge regarding the operational attributes of a facility. The location DDP class relationships are represented as an aggregate relationship which captures the location and operational attributes of a facility (Fig. 3). More specifically, it captures the facility's purpose, individuals associated with managing the facility, locale, contact or communication data, and its physical (or configuration) characteristics.

![](/api/attachments/4X2BK5SS/fulltext/images/3e5119d9c3259764cde1fc64ff7324b3902a77069de28ab7c46dbc41de86b02f.jpg)  
Fig. 1. The Domain DDP Class Diagram.

A stakeholder can be associated with and described by an organization or a role. An organization is considered a group of people bound by common work, goals, or interests while a role describes a specific task and set of responsibilities. The stakeholder DDP describes individual stakeholders in terms of the organization to which they belong or their specific capacity or role they perform (Fig. 4). It may be used for measuring aspects of an organization or a specific role. The designer needs to decide whether it is necessary to evaluate the performance of the organization and/or the specific roles within the organization. The following are examples of organizations and roles: 1) a household would be considered an organization while the head of the household would be a role, 2) a financial company, such as a bank, would be considered an organization while an account owner would be considered a role, and 3) a service provider would be considered an organization while the service representative would be considered a role.

![](/api/attachments/4X2BK5SS/fulltext/images/31f94ebd4a3611036293cc53c859d51abdea08961190a98c61f3518cc673aba2.jpg)  
Fig. 2. The Temporal DDP.

![](/api/attachments/4X2BK5SS/fulltext/images/80a21e8523a4b87eacd099b11d689429ad078bcb7da5e80e9e619f5446be50c0.jpg)  
Fig. 3. The Location DDP.

An action is defined as accomplishing (or doing) something or exhibiting a behavior. For the action DDP there are two types of actions — work or behavior. Therefore the action DDP is modeled as a generalization–specialization (Fig. 5). It is typical to measure characteristics associated with the work of accomplishing a specific task. For example, in a manufacturing scenario the analyst may need to evaluate the efficiency of production runs, a retail store may want to assess the effectiveness of a promotion, or a credit company may want to measure the timeliness of credit payments. In many industries it is important to evaluate the behavior associated with an action. For example, an organization may want to determine customer satisfaction via the number and type of complaints received through the customer service group.

![](/api/attachments/4X2BK5SS/fulltext/images/117d39cda0d7f40c411370018b12e787781230f62a3b59f8a60f37522d0f878d.jpg)  
Fig. 4. The Stakeholder DDP.

The object DDP has two types of objects; conceptual and physical (Fig. 6). A conceptual object is defined as an abstract idea used within the domain; whereas a physical object is defined as a tangible entity that is used within the domain. Conceptual objects may be various types of accounts such as revenue accounts, general ledger accounts, savings accounts, checking accounts and expense accounts. Also in the insurance industry, a policy that documents the insurance coverage is an example of a conceptual object. In education, a course may be thought of as conceptual object. Examples of physical objects are products, items, components (used to assemble products), and ingredients.

![](/api/attachments/4X2BK5SS/fulltext/images/5b34cb864484833f72e6797f5baff913e3b81c7e11674cf5e0ecb26b4b98e7b3.jpg)  
Fig. 5. The action DDP.

![](/api/attachments/4X2BK5SS/fulltext/images/d189acbe96a588abbb25728438b6527174e3a4698757ce364c690fb7b0108d4e.jpg)  
Fig. 6. The object DDP.

There are cases when information is more meaningful if it can be classified by a readily identifiable grouping attribute. The qualifier DDP classifies data by profile, state, causal, or unit indicators (Fig. 7). The profile DDP is used to group facts based on an identifying characteristic associated with a particular group. For example, employee skill groups can profile employees by their expertise with specific skills. The state DDP describes the circumstances characterizing a particular condition at a point in time. Associating a customer's satisfaction with regard to a product or service characterizes the customers' level of happiness (or state) at a point in time. The cause DDP is used to ascertain a possible reason for the occurrence of an event. A retail store is likely to be interested in the effectiveness of an advertising campaign. Therefore it is important to link the specific advertisement to the customer's purchases. Gathering and analyzing this data over a period of time may indicate the advertisement's influence on the customer's buying behavior. The unit DDPs is used to define measurement data in its associated unit of measure.

When applying this model, the practitioner is not limited to using only a single class. A new dimension can be created by combining attributes from multiple classes to create a single combination dimension (Fig. 1).

## 3.3. Applicability of Domain DDPs to an existing model

This section illustrates the applicability of DDPs by mapping the Domain DDPs to an existing dimensional schema [1]. This model (Fig. 8) is composed of the sales fact table and the following dimension tables: time, dealers, customer demographics, products, and method of payment.

Applying the Domain DDP model to the Auto Make Sales example illustrates the use of Domain DDP classes in a single dimensional schema (Table 1). The column labeled represents the <sup>Dimension: DDP Mapping</sup>mapping of the dimension table to the DDP classes. The column labeled applies to <sup>Attribute: DDP Mapping</sup>the dimension table attributes and represents the mapping of dimension table attributes to the DDP classes.

The following explains the Auto Sales DDP Mapping:

□ The time dimension stores attributes that represent the traditional calendar structure.

□ The dealers dimension represents the organization who sells the automobiles. The organization is described in terms of its city and state. The dealers can be profiled by using the single brand flag which indicates which dealers sell a single brand of automobile. The date of first operation indicates when the dealer first opened for business.

□ All of the attributes in the customer demographics dimension provide the analyst with the ability to profile the dealers' customers.

□ The products dimension represents the automobile. Its attributes describe ways to classify (styling package, line, category, exterior color, interior color) each automobile. The model year and first model year represent the temporal dimension.

□ The method of payment dimension is the method in which the customer purchases the automobile. The term in months and rate attributes are profiling attributes while the finance lease agent is the individual who completed the lease.

## 3.4. Using the Domain DDPs

The process for using the DDPs to design a dimensional model was created with simplicity in mind. In general, if a concept is cumbersome, it is unlikely that software engineers will adopt it for use. This process provides the framework for thinking about and determining the dimensions and attributes without the burden of an overly complex process.

![](/api/attachments/4X2BK5SS/fulltext/images/88bf7a5dda775818f2d2925e44ebb65433de671bf6172b28334c944727e4a9a6.jpg)  
Fig. 7. The qualifier DDP.

![](/api/attachments/4X2BK5SS/fulltext/images/24d1929bf57103e04cc53ecada28af77b4a6bcff83ef42103a8b9ad7fa4b73ac.jpg)  
Fig. 8. An auto maker sales dimensional model [1].

When beginning a dimensional model, a business process must be selected and the grain of the data must also be determined. After those steps, the DDPs should be used to assist in determining the dimensions and attributes. The software engineer should be familiar with DDPs. A copy of the DDP class diagrams, their definitions and examples should be available for reference.

To begin determining the dimensions, the process requires systematically considering each Domain DDP individually in relation to the business process being modeled (Fig. 9). It is critical to ensure each Domain DDP is evaluated in terms of the business process. Most likely the software engineer or business analyst will need to iterate through the process several times. At the conclusion of considering each DDP individually, the dimensions and attributes should be re-evaluated for accuracy. This provides an additional iteration through the dimensions to add, edit or delete items from the dimensional model.

Tables 2 and 3 should be used in conjunction with the activity diagram (Fig. 9) to facilitate the identification of dimensions and attributes. It is the practitioner's method for applying the Domain DDP class diagram. For each Domain DDP, the associated set of questions leads the analysts to consider and determine the specific dimensions and attributes for their problem.

## 3.5. Fact DDPs

A fact provides a quantifiable measurement. Within a dimensional schema, the fact table stores measurements pertinent to the business process under analysis. When a software engineer is in the process of determining a dimensional model's facts, it is important to consider the grain of the fact table first. Since the grain of the fact table refers to the gradation of the data (or the level of detail) stored in the dimensional schema, the software engineer considers the measurements (or facts) pertinent to the type of analysis questions requiring answers.

Kimball [15] classifies fact tables in terms of their granularity. Grain is considered from the transaction, periodic snapshot, and accumulating snapshot levels.

Table 1  
The auto sales Domain DDP mapping

<table><tr><td>Auto maker sales dimensions</td><td>Dimension: DDP mapping</td><td>Attribute: DDP mapping</td></tr><tr><td>Time</td><td>Temporal</td><td>Temporal calendar</td></tr><tr><td>Dealers</td><td>Stakeholder</td><td>Stakeholder-organization location-locale qualifier-profile temporal calendar</td></tr><tr><td>Customer demographics</td><td>Qualifier</td><td>Qualifier-profile qualifies-status</td></tr><tr><td>Products</td><td>Object</td><td>Object-physical qualifier-profile temporal calendar</td></tr><tr><td>Method of payment</td><td>Action</td><td>Action-work qualifier-profile temporal calendar stakeholder-role</td></tr></table>

![](/api/attachments/4X2BK5SS/fulltext/images/bed9064264cef3f546cc63f7ca92883eb039778edd1a57faa7fedcde2f0afad6.jpg)  
Fig. 9. The Domain DDP activity diagram.

His classification addresses 1) the data's level of detail and 2) the operational aspects loading fact table data. However, a software engineer must also determine the specific facts required to fulfill the analysis requirements. Therefore, the Fact DDP is designed to extend Kimball's classification by modeling a third consideration that directs the software engineer to select the facts and classify them based on their additive property (additive, semi-additive, and non-additive concepts). Based on the type of facts in the fact table, the software engineer can then determine whether it is a transaction, periodic snapshot, or accumulating snapshot table.

When a software engineer is attempting to evaluate and analyze data, the measures must be applicable and convey meaningful information for the particular situation. In dimensional modeling it is important to understand the meaning and appropriateness of facts with respect to the description (dimension) data. Since facts are measurements it is reasonable to consider classifying measurements in a way that can help software engineers determine applicability of the facts with respect to the dimension data (Fig. 10).

The Fact DDPs are composed of measures and degenerate key(s). Typically measures are numeric but they can be textual. In dimensional modeling, numeric measures can represent two types of information: 1) activity measures and 2) intensity measures.

An activity measure is a specific numeric value that is meaningful for all the dimensions. It is usually calculated for a specific point in time. For example, the ‘quantity’ fact in the product sales fact table (Fig. 11) can be evaluated for the temporal (time by month) dimension, the object (product) dimension, and the location (geography) dimension. It can be used to describe and analyze product sales (quantity) in terms of a number of different scenarios:

□ sales for an object (product) classified by the object's (product's) category

□ quantity fact from the product sales fact table and the required dimension attributes from the product table

□ sales by time (temporal)

□ quantity fact from the product sales fact table, the required dimension attributes from the product table and the time by month table

□ sales by location

□ quantity fact from product sales fact table, the required dimension attributes from the product table and the location table

□ sales by time (temporal) and location

□ quantity fact from product sales fact table, the required dimension attributes from the product table, the time by month table, and the location table.

As demonstrated in the scenarios above, the quantity value is applicable regardless of whether all the dimensions or a subset of dimension are needed for the analysis scenario. Dimensional modeling practitioners use the term “additive” to describe activity measures.

An intensity measure is a specific numeric value that is appropriate for certain facts. Dimensional modeling practitioners use the term “semi-additive” to describe intensity measures. Like the activity measure, an intensity measure is usually calculated for a specific point in

Table 2  
Domain DDP dimension and attribute identification questions

<table><tr><td>Temporal — does the dimension need to:</td><td>Location — does the dimension need to:</td><td>Stakeholder — does the dimension need to:</td></tr><tr><td>Capture calendar periods?</td><td>Capture a specific locale (site)?</td><td>Describe the performance of an organization or a group?</td></tr><tr><td>Capture fiscal periods?</td><td>Describe the purpose or work accomplished at that locale?</td><td>Describe the performance of a specific individual or role of an individual?</td></tr><tr><td>Capture both calendar and fiscal periods?</td><td>Capture significant dates/times associated with the location?</td><td>Associate the stakeholder with a date and/or time?</td></tr><tr><td>Capture special periods such as academic semesters or holiday seasons, etc.?</td><td>Associate stakeholders with the locale?</td><td>Associate the stakeholder with a locale?</td></tr><tr><td rowspan="4">Capture time?</td><td>Describe the configuration of a locale?</td><td>Associate the stakeholder with an event or action?</td></tr><tr><td>Capture contact/communication information (e.g., phone, e-mail, etc.) for the locale?</td><td>Associate the stakeholder with an object?</td></tr><tr><td>Capture events or actions associated with the locale?</td><td>Describe the stakeholder with profile information?</td></tr><tr><td>Associate the location with an object?</td><td>Describe the stakeholder in terms of a state (e.g., single, married, etc.)?</td></tr></table>

time but the value represents a tendency or trend for the scenario. For example, the ‘inventory amount’ fact has been added to the previous product sales dimensional model (Fig. 12) to illustrate an intensity measure. The value of the inventory amount fact is additive for the object (product) dimension and the location (geography) dimension. In makes sense to determine the inventory amount of a particular product or to determine the inventory amount for a particular product at a specified location(s). However, a different evaluation approach is required when considering the temporal (time) dimension and this pattern is referred to as a temporally semiadditive measure [19]. The inventory amount, when considered over a time period, must represent an average amount. It is not reasonable to add the inventory amounts across time periods. For example, assume the inventory amount is 20 and 25 on day two. The inventory amount on the second day is 25 not 45; therefore the inventory amount is not additive for the temporal dimension. However it is reasonable to calculate the average inventory amount over a specified time period.

Another example where a designer must be cautious when applying additive measures is when a single dimension contains different types of information [19]. More specifically, when a dimension stores data for multiple products, the addition of the number of products will include all those unique products; therefore this measure may not be meaningful to the business analyst. This pattern is referred to as a categorically semi-additive measure [19].

A textual measure is a non-numeric value. However it can still provide valuable information. Consider a fact that stores the text values of “high”, “medium”, or “low” to classify customer purchase activity. In order to be meaningful to an analyst, those text values need to be pre-defined with regard to the boundary conditions that constitute each category. Consider an automobile insurance scenario with a ‘weather condition’ fact that stores a description of the weather conditions at the time of an automobile accident. Textual facts are non-additive.

Domain DDP dimension and attribute identification questions

<table><tr><td>Action — does the dimension need to:</td><td>Object (physical or conceptual) —does the dimension need to:</td><td>Qualifier (profile, state, causal, unit) —does the dimension need to:</td></tr><tr><td>Capture specific actions? What actions?Identify types of work (steps) associated with the action?Describe outcomes or results of work?Identify or describe behaviors?Associate a date/time with the actions?Associate the action with a location?Associate the action with stakeholders?Associate the action with an object(s)?Associate the action with profile information?Associate the action with status information?Associate the action with causal information?</td><td>Describe the classification of objects?Associate the object with a date/time?Describe the “life span” of the object?Identify ownership of objects?Associate the object with its location?Associate the object with an action(s)?Describe the configuration of the object?Associate the object with profile information?Associate the object with status information?Associate the object with causal information?</td><td>Provide profile information of a stakeholder, location, action, or object?Describe the status (or state) of a stakeholder, location, action, or object?Describe causal situations associated with a stakeholder, location, action, or object?Describe a measurement in terms of its unit of measure?</td></tr></table>

![](/api/attachments/4X2BK5SS/fulltext/images/02b848d438bc3fa7f267c611acdb3c588ebc1ed3d3fe342aecba26234064c16a.jpg)  
Fig. 10. The fact DDPs.

Kimball defines a degenerate key as a unique identifying attribute that is associated with the transaction system that originally generated the data [15]. It is not meaningful as a separate dimension, but it is useful when analyzing data associated with a specific transaction since it can be used as a grouping mechanism.

## 3.6. Using the fact DDPs

It is within the framework of this design process that the DDPs will be used to facilitate the creation of dimensional models. The activity diagram (Fig. 13) details the use of the DDPs within Kimball's framework [14,15].

The method for using the DDPs was designed with simplicity in mind. In general, if a methodology is cumbersome, it is unlikely that software engineers will adopt it for use. The methodology provides the framework for thinking about and determining the dimensions and facts without the burden of an overly complex process.

When beginning a dimensional model, a business process must be selected and the grain of the data must also be determined. After those steps, the DDPs should be used to assist in determining the dimensions and facts. The software engineer should be familiar with DDPs. A copy of the DDP class diagrams, their definitions and examples should be available for reference.

To begin determining the dimensions, the process requires systematically considering each Domain DDP individually in relation to the business process being modeled. However it is important to recognize that the development of a dimension is not a linear process. Because it is difficult to consider business processes in isolation, the software engineer will naturally consider the other Domain DDPs while working through each DDPs. The point is not a strict adherence to the proposed linear sequence. However, it is critical to ensure each Domain DDP is evaluated in terms of the business process. Most likely the software engineer or design team will need to iterate through the process several times. At the conclusion of considering each DDP individually, the dimensions should be re-evaluated in terms of the combined dimensions. This provides an additional iteration through the dimensions to add, edit or delete items from the dimensional model.

![](/api/attachments/4X2BK5SS/fulltext/images/2a4f67f77fd521bc90caac02d6c6f9035cd8ca28b61713561748c71b68a4a317.jpg)  
Fig. 11. The fact DDP — activity measure.

![](/api/attachments/4X2BK5SS/fulltext/images/6b8f0ab82b359a0ff6c29c9f1974ace4e306ab50a95a1862b148aeb2dbd9cdd6.jpg)  
Fig. 12. A sales dimensional model.

The next step is identifying the facts (or measures). Once a fact is determined it must be considered in conjunction with the existing dimensions. Recall that a fact has meaning when it is described by the dimensions. Without the appropriate descriptive data the fact is only a number without its context. If the appropriate descriptive data is not in the dimensional model, the software engineer needs to change the dimension tables appropriately. Next, it is necessary to identify whether the fact is an activity measure, an intensity measure, or textual. Also, its additivity property should be determined. It is helpful to group the facts by their additivity property for the purpose of placing like facts together in a single fact table.

Although the grain of the dimensional model was determined in step 2 of the process, it is important to confirm that each fact is in agreement with the selected grain. If the fact does not agree with the grain this may indicate that an additional fact table is necessary. Based on the list of facts, use Kimball's fact table classification characteristics can be used to determine the appropriate fact table(s) needed for the dimensional model [15]. Finally facts should be allocated to the specific fact table.

## 3.7. Implementation DDPs

The Implementation DDPs describes alternative physical design strategies for the standard dimensional model. Typically, the application of these strategies evolves with the use of the data warehouse.

Some of these strategies “break” the rules for creating dimensional models since they apply normalization rules. Normalization of dimensional models generally makes querying more difficult and usually slower. Therefore the general practice is to avoid its use. The other strategies are specific techniques that refine a dimensional model in order to facilitate the querying of data. The implementation dimension DDPs (Fig. 14) are aggregation, specialization, part assembly and type variation.

## 3.7.1. Aggregation

In general, software design is a series of decisions that require the trading off of one design option for another.

![](/api/attachments/4X2BK5SS/fulltext/images/0112ada7335b828293da2d5e16028c290b9aa6e62a1d0a85c2379bbbcb5c7e3b.jpg)  
Fig. 13. The DDP activity diagram.

The design of a dimensional model is no exception to the design trade off dilemma. For example, the general rule of thumb is to create a dimensional model containing data at the lowest level of detail. That strategy provides maximum querying flexibility since detailed data can be grouped together to provide summarized information. However, summarizing large volumes of data will likely slow query performance. In order to increase the speed of query performance, the software engineer can create an aggregate fact or an aggregate fact table [15].

An aggregation refers to the grouping of entities in order to facilitate the summarizing of data. An aggregate can be implemented as an individual fact. For example, an analyst may not want a numeric representation of a fact. It may be more helpful to group ranges of numeric data together by using a textual fact that describes a range of data values. A specific instance of this scenario is students' grade point averages. When determining academic honors, the grade point average is associated with a specific academic honor. By assigning the range of grade point averages to the associated academic honor all students within the appropriate grade point average can be analyzed together. Since this is simply a textual description of a numeric fact, this technique can be implemented using a textual fact that is defined in association with the student's grade point average.

![](/api/attachments/4X2BK5SS/fulltext/images/2a9a71a486720054fa7188b54b2676fb345b1fb5fbd02f865985e26146f1321a.jpg)  
Fig. 14. The implementation DDPs.

An aggregate can also be implemented as a fact table. The concept requires the combining of facts at the lowest level into facts that are summarized at a higher gradation. For example, if data is stored daily, it can then be summarized (or rolled up) to a weekly level. By creating separate fact tables with the data, presummarized query performance will improve.

## 3.7.2. Specialization

The generalization–specialization model represents a hierarchical relationship between dimensions (Fig. 15). The highest level represents the characteristics that are common to all modeled dimensions while the more specialized dimensions represent distinguishing characteristics between dimensions. This is likely to occur when a business has “heterogeneous products” [15] that are available to the same set of customers.

When this scenario arises Kimball recommends the use of an outrigger dimension. An outrigger dimension, also referred to as the snowflake design, is the normalization of dimension tables.

## 3.7.3. Type variation

The type variation DDP is similar to the specialization DDP in that it is also represented as a generalization–specialization model. The variation occurs within a single dimension table but is used multiple times within a fact table [15].

Kimball points to his order management example [15]. In this case, the date dimension is used to evaluate several facts. In other words, the date dimension plays different roles. For example, the date can represent the date the order was placed, the date the order was filled, the date the order was shipped or the date the order was received by the customer. It does not make sense to create a separate date dimension for every date fact that requires evaluation. Kimball recommends the creation of multiple views to solve this problem [15]. As a result, the net effect of multiple (virtual) tables with the creation of a single physical table.

## 3.7.4. Part assembly

At times it is important to assemble the components or parts of an organization or item. The assembly of the components leads to an understanding of the relationships between components.

A bridge dimension is used to capture and traverse the relationships between leaves (or nodes) in a hierarchical tree. The hierarchy relationship is implemented via a bridge table that defines the relationship of each node in the hierarchy to the other nodes in the hierarchy. Kimball recommends this approach to represent organizational hierarchies and manufacturing parts explosion hierarchies [15].

A bridge table is also used to solve the problem of multi-valued dimensions. For example, in the financial domain an account may be associated with two or more people thus requiring the linking of those people to a single account. Creating a bridge table between the account and customer dimension can mitigate the multivalued attribute.

![](/api/attachments/4X2BK5SS/fulltext/images/81139caa4bb9f8fe2886af88a7daa350a28adc814a5f288ce75b64c7029306b1.jpg)  
Fig. 15. The specialization DDP.

## 4. Research study and results

## 4.1. Research Study

A pre-test post-test experiment with an initial number of 41 undergraduate database students was conducted to determine the efficiency and effectiveness of the DDPs. Thirty two students completed the experiment since all students volunteered to participate in the research and could choose to withdraw at any time. The experiment measured the time and precision/correctness of design problems between the control group (no exposure to DDPs) and the experimental group (exposure to DDPs). The subjects had an understanding of database concepts and system analysis, but minimal experience with data warehousing concepts. The following null hypotheses were tested to evaluate whether exposure to the DDPs assisted undergraduate students in designing dimensional models.

□ $\operatorname { H } _ { 0 } { \mathrm { : } }$ Dimensional design patterns (DDPs) have no impact on the time to design a dimensional model.

□ $\operatorname { H } _ { 0 } { \mathrm { : } }$ Dimensional design patterns (DDPs) have no impact on the correctness of the dimensional model design.

The experiment was conducted in four steps (Fig. 16). The experiment began with a pre-study questionnaire for capturing demographic data. In step 2, basic dimensional modeling concepts were taught to all subjects. The teaching was followed by a dimensional modeling design problem to measure the subjects' initial understanding of those concepts. In step 3, the subjects were randomly assigned to either the control group (no exposure to DDPs) or the experimental group (exposure to DDPs). After teaching additional dimensional modeling and the DDP concepts, another design problem was administered to the subjects to evaluate the impact of the DDPs on the subjects' understanding of dimensional modeling. In the last step, subjects provided an assessment and comments regarding their experience with dimensional modeling examples and DDPs.

## 4.2. Research results

The demographic data describing the participating subjects captured in the pre-study questionnaire (Fig. 16 — step 1) can be summarized as follows: 93% were male, 93% were between the ages of 18 and 30, 95% were pursuing a bachelor of science degree in information systems or information science and systems, and 50% had work experience in their field of study.

The design problems were created to objectively evaluate the impact of the DDPs. The first design problem (Fig. 16 step 2) was used to ensure all subjects had a basic understanding of dimensional modeling prior to randomly assigning the subjects to either the control group or the experimental group. The first design problem provided a base line to ensure that all the subjects had a basic understanding of data warehousing and dimensional modeling prior to creating the experimental and control groups. At the conclusion of the first problem, the researcher was convinced that subjects understood the basics of dimensional modeling.

The second design problem was used to determine if exposure to the DDPs improved the effectiveness (correctness/precision) and the efficiency (time) of designing a dimensional model (Fig. 16 — step 3). Both groups were given the same design problem regardless of whether they were in the control group or the experimental group.

![](/api/attachments/4X2BK5SS/fulltext/images/82605777c18600b8f3fe52219f7e96362584f4e953f203c103b272ed156e32c3.jpg)  
Fig. 16. The experimental procedure.

Table 4  
Design problem #2 descriptive statistics — time

<table><tr><td>Time</td><td>N</td><td>Mean</td><td>Standard deviation</td><td>Standard error mean</td></tr><tr><td>Experimental group (DDPs)</td><td>18</td><td>11.5000</td><td>2.4071</td><td>0.5674</td></tr><tr><td>Control group (examples)</td><td>14</td><td>12.5714</td><td>4.1642</td><td>1.1129</td></tr></table>

For design problem #2, the time variable was compared between the experimental and control groups. The following is a comparison of the two groups using descriptive statistics. In addition a t-test was used to compare the performance of the control and experimental groups. Scores were calculated as a ratio of the number of points earned divided by the total possible points. The results of design problem #2 for time (Tables 4 and 5) and correctness/precision (Tables 6 and 7) are shown.

After the subjects completed the second design problem, each was given the post-study evaluation (Fig. 16 — step 4). The purpose of the post-study evaluation was to gain the subjects' perspective and opinions regarding their dimensional modeling experience with this study. The control group was not exposed to the DDPs so they were asked to evaluate their experience using Ralph Kimball's approach to dimensional modeling as well as the use of examples when designing dimensional models. The experimental group had exposure to Ralph Kimball's approach, examples, and the DDPs.

Although not as objective as the data resulting from the testing process, this information complements the design problem data by capturing the intangible aspects of this research.

When analyzing the data in common to both groups, the summarization comparing and contrasting the results is most helpful (Table 8). The experimental group rated dimensional modeling difficulty higher. Most likely this is due to recognizing underlying modeling complexities that are more recognizable in light of learning about the DDPs. They also rated the helpfulness of examples higher than the control group. This can be attributed to the fact that when the DDPs were taught, students recognized that the source of the DDPs was dimensional modeling examples. That is, the DDPs were discovered by studying many dimensional modeling examples. With regard to the subjects' impression of the impact of examples on the time it took to design a solution the experimental group thought the examples had less of an impact on their time than the control group. The experimental group also thought that the examples had less of an impact with regard to the correctness (or precision) of their solutions. The experimental group subjects' reliance on examples for future design problems was less than the control group reliance.

Table 6  
Design problem #2 — correctness

<table><tr><td>Correctness</td><td>N</td><td>Mean</td><td>Standard deviation</td><td>Standard error mean</td></tr><tr><td>Experimental group (DDPs)</td><td>18</td><td>32.8250</td><td>12.3107</td><td>2.9017</td></tr><tr><td>Control group (examples)</td><td>14</td><td>26.3100</td><td>13.5748</td><td>3.6280</td></tr></table>

Comparing and contrasting the experimental group's opinions of the examples versus their opinions of the DDPs (Table 9), the overall helpfulness of the DDPs and the examples were almost even; 84% to 83% respectively. They believed that the DDPs had more of an impact on reducing their time than the examples and they also stated that the DDPs had more of an impact on the correctness of their solutions. The experimental group would rely more on examples (89%) than the DDPs (78%); however that response makes sense in light of the result that two thirds of the experimental subjects would rely on a combination of examples and

Table 5  
Design problem #2 t-test — time

<table><tr><td rowspan="3"></td><td colspan="2">Levene&#x27;s test for equality of variances</td><td colspan="7">t-test for equality of means</td></tr><tr><td rowspan="2">F</td><td rowspan="2">Sig.</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Sig. (2-tailed)</td><td rowspan="2">Mean difference</td><td rowspan="2">Standard error difference</td><td colspan="2">90% confidence interval of the difference</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Time: equal variances assumed</td><td>2.694</td><td>.111</td><td>-.915</td><td>30</td><td>.367</td><td>-1.071</td><td>1.171</td><td>-3.058</td><td>.916</td></tr><tr><td>Time: equal variances not assumed</td><td></td><td></td><td>-.858</td><td>19.622</td><td>.401</td><td>-1.071</td><td>1.249</td><td>-3.228</td><td>1.085</td></tr></table>

Table 7  
Design problem #2 t-test — correctness

<table><tr><td rowspan="3"></td><td colspan="2">Levene&#x27;s test for equality of variances</td><td colspan="7">t-test for equality of means</td></tr><tr><td rowspan="2">F</td><td rowspan="2">Sig.</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Sig.(2-tailed)</td><td rowspan="2">Mean difference</td><td rowspan="2">Standard error difference</td><td colspan="2">90% confidence interval of the difference</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Correct: equal variances assumed</td><td>.166</td><td>.686</td><td>1.420</td><td>30</td><td>.166</td><td>6.515</td><td>4.5875</td><td>-1.271</td><td>14.301</td></tr><tr><td>Correct: equal variances not assumed</td><td></td><td></td><td>1.402</td><td>26.621</td><td>.172</td><td>6.515</td><td>4.6457</td><td>-1.402</td><td>14.432</td></tr></table>

DDPs or DDPs for future modeling problems. Only a third of the experimental subjects would rely solely on examples.

The experimental group was asked to answer 2 open ended questions: 1) identify the strengths of the DDPs in assisting you to design a dimensional model. Please explain the strengths and 2) identify areas where you believe the DDPs could be improved. Please explain your improvement.

The experimental group's responses to the open ended questions confirmed that this research met the initial goals. First and foremost, there was a desire to create patterns that were easy to understand and use. Second was to provide a structured framework to think about the design. The comments regarding the strengths of the DDPs affirmed the meeting of these goals.

With regard to the weaknesses, it was recognized that the initial DDP presentation was too theoretical. Therefore the second presentation was adjusted to clarify the use of the diagrams. Because the study was conducted in a very short span of time, the subjects did not have enough practice to identify potential difficulties.

The second design problem was a bit more difficult than the first problem. It was believed that with more education the problem needed to be a little more difficult in order to realistically test the impact of the DDPs. Although the t-test results for both the time and correctness variables are not significant, the results are still promising. The subjects using the DDPs were approximately 9% more efficient and approximately 25% more correct with their solutions than the subjects not using the DDPs.

The most significant weakness of this study was the short span of time that the subjects had to absorb this material. The research was conducted in three consecutive classes over a three-week period — one class a week. But due to the structure and content of the course it was not possible to increase the educational time. However because the positive overall results and the limitations associated with classroom research, the next phase of study needs to be in an industry setting.

## 4.3. Experimental results discussion

There are three areas of evaluation that could help continue the progress of this research. First, it would be interesting to present this approach to software professionals knowledgeable in the area of dimensional modeling and have them evaluate if this approach would have made their design process easier and more efficient. Second, it would be helpful to reverse engineer an existing industry dimensional model to determine the appropriateness of the DDPs with a more complex problem. Finally, it would be ideal to use the DDP process to create a dimensional model for industry implementation and use.

Table 8  
Post-study evaluation: comparing experimental group and control group responses for use of example

<table><tr><td>Question</td><td>Experimental-percentage</td><td>Control-percentage</td></tr><tr><td>Subjects considered the overall ease/difficulty of designing a dimensional model for this course as somewhat difficult or extremely difficult.</td><td>61%</td><td>47%</td></tr><tr><td>Subjects considered the overall helpfulness of dimensional modeling examples when designing a dimensional model for this course as very helpful or somewhat helpful.</td><td>83%</td><td>73%</td></tr><tr><td>Subjects thought that dimensional model examples either significantly or moderately reduced the time it took to design a solution.</td><td>60%</td><td>74%</td></tr><tr><td>Subjects thought that dimensional model examples were very helpful or somewhat helpful in assisting them in designing a correct solution.</td><td>61%</td><td>87%</td></tr><tr><td>Subjects would rely on dimensional model examples either exclusively or moderately.</td><td>89%</td><td>100%</td></tr></table>

Table 9  
Post-study evaluation: comparing use of example versus DDPs for experimental group

<table><tr><td>Example question</td><td>Experimental group % — use of examples</td><td>DDP question</td><td>Experimental group % — use of DDPs</td></tr><tr><td>Subjects considered the overall helpfulness of dimensional modeling examples when designing a dimensional model for this course as very helpful or somewhat helpful.</td><td>83%</td><td>Subjects thought the overall helpfulness of DDPs as compared to the examples were either very helpful or somewhat helpful.</td><td>84%</td></tr><tr><td>Subjects thought that dimensional model examples either significantly or moderately reduced the time it took to design a solution.</td><td>60%</td><td>Subjects thought that the DDPs either significantly or moderately reduced their time in designing a solution.</td><td>67%</td></tr><tr><td>Subjects thought that dimensional model examples were either very helpful or somewhat helpful in assisting them in designing a correct solution.</td><td>61%</td><td>Subjects thought the impact of DDPs as compared to the examples were either very helpful for somewhat helpful with regard to the correctness of the design solution</td><td>73%</td></tr><tr><td>Subjects would rely on dimensional model examples either exclusively or moderately.</td><td>89%</td><td>Subjects thought they would rely on DDPs (as compared to the examples) either exclusively or moderately.</td><td>78%</td></tr></table>

## 5. Conclusion and future work

In this paper, we have presented the DDPs abstracted from case studies and examples presented in the literature. The primary contributions of this paper are as follows. First, we have presented a taxonomy of dimensional design patterns (DDPs) abstracted from over 50 case studies. The DDPs include three types: domain, fact and implementation DDPs. Second, through a DDP example, we have illustrated the applicability of the Domain DDPs to an existing dimensional model. Third, our initial experiments show that the DDPs significantly increase the effectiveness of the design and reduce the time to design dimensional models. Our experimental results for the evaluation of the impact of DDPs on the time and correctness of the design process, although not statistically significant, showed a 25% improvement in correctness and a 9% improvement in time.

The opinion of the subjects, as reported in the questionnaires was encouraging. The DDPs: 1) helped the subjects in “thinking” about the design, 2) “acted as a guide”, 3) “helped simplify the design”, 4) “were more of a framework for design”, and 5) “helped me to think about the things that needed to be included in order to get the facts”.

The overall positive results combined with the limitations associated with classroom research means another type of study is required to better evaluate the impact of DDPs. There are three areas of evaluation that could help continue the progress of this research. First, it would be interesting to present this approach to software professionals (in an industry setting) knowledgeable in the area of dimensional modeling and have them evaluate if this approach would have made their design process easier and more efficient. Second, it would be helpful to reverse engineer an existing industry dimensional model to determine the appropriateness of the DDPs with a more complex problem. Finally, it would be ideal to use the DDP process to create a dimensional model for industry implementation and use.

## References

[1] Christopher Adamson, Michael Venerable, Data Warehouse Design Solutions, John Wiley and Sons, Inc, New York, 1998.

[2] Ellen Agerbo, Aino Cornils, “How to Preserve the Benefits of Design Patterns”, Proceedings of the Conference on Object-Oriented Programming, Systems, Languages, and Applications, Vancouver, Canada, October 18–22, 1998, pp. 134–143.

[3] Christopher Alexander, Sara Ishikawa, Murray Silverstein, Max Jacobson, Ingrid Kiksdahl-King, Shlomo Angel, A Pattern Language: Towns, Building, Construction, Oxford University Press, New York, 1977.

[4] Christopher Alexander, The Timeless Way of Building, Oxford University Press, New York, 1979.

[5] Frederick P. Brooks, The Mythical Man-Month. Reading: Addison Wesley Longman, Inc., 1995.

[6] Frank Buschmann, Regine Meunier, Hans Rohnert, Peter Sommerlad, Michael Stal, Pattern-Oriented Software Architecture: A System of Patterns, John Wiley and Sons, Chichester, 1996.

[7] Peter Coad, David North, Mark Mayfield, Object Models — Strategies, Patterns, and Applications, Yourdon Press, Englewood Cliffs, 1995.

[8] Michael J. Corey, Michael Abbey, Ian Abramson, Ben Taub, Oracle8 Data Warehousing — A Practical Guide to Successfu Data Warehouse Analysis, Build, and Roll-Out, Osborne McGraw-Hill, Berkeley, 1998.

[9] Paul Evitts, A UML Pattern Language, Indianapolis: Macmillan Technical Publishing, 2000.

[10] Martin Fowler, Analysis Patterns: Reusable Object Models, Addison-Wesley, Menlo Park, 1997.

[11] Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, Design Patterns: Elements of Reusable Object-Oriented Soft ware, Addison Wesley Longman Inc., Reading, 1995.

[12] David Hay, Data Model Patterns: Conventions of Thought, Dorset House Publishing, New York, 1996.

[13] John Horner, Il-Yeol Song, Peter Chen, Analysis of additivity in OLAP Systems, Proceedings of ACM DOLAP, 2004.

[14] Ralph Kimball, Richard Mertz, The Data Webhouse Lifecycle Toolkit, John Wiley and Sons Inc., New York, 2000.

[15] Ralph Kimball, Laura Reeves, Margy Ross, Warren Thornthwaite, The Data Warehouse Lifecycle Toolkit, John Wiley and Sons, Inc, New York, 1998.

[16] Ralph Kimball, Margy Ross, The Data Warehouse Toolkit, 2nd ed., John Wiley and Sons, Inc, New York, 2002.

[17] Robert Muller, Database Design for Smarties: Using UML for Data Modeling, Morgan Kaufmann Publishers Inc, San Francisco, 1999.

[18] Len Silverston, The Data Model Resource Book, vol. 1, revised ed, John Wiley and Sons, Inc, New York, 2001.

[19] Herbert A. Simon, The Sciences of the Artificial, 3rd ed, The MIT Press, Cambridge, 1996.

[20] John Vlissides, Pattern Hatching: Design Patterns Applied, Addison Wesley Longman Inc., Reading, 1998.

![](/api/attachments/4X2BK5SS/fulltext/images/f9c808cffa4648462ef0155c7c4e5fdc16083108a15f7177ed593ad2aaaceb6c.jpg)

Mary Elizabeth “M.E.” Jones is a full-time faculty member in the Department of Mathe matics–Computer Science–Physics at Immaculata University, Immaculata Pennsylvania. She received a BA from Immaculata University in Mathematics–Physics–Computer Science in 1982, an MA in Mathematics from Villanova University in 1984 and her Ph.D. from Drexel University's College of Information Science and Technology in 2006. Dr. Jones is respon

sible for teaching courses in mathematics as well as information technology and science. She has developed and re-designed several information technology courses and has also recently designed and implemented an undergraduate research program for the Department of Mathematics–Computer Science–Physics in order to introduce undergraduates to research and prepare them for graduate school. Her research is influenced by her industry experiences regarding designing and developing software applications in both government and commercial industries. Her doctoral dissertation: “Dimensional Modeling: Identifying Patterns, Classifying Patterns, and Evaluating Pattern Impact on the Design Process” has been the focus of her research. Its intent is to quantify a process for designing dimensional models through the use of patterns. She is a member of ACM and the IEEE Computer Society. Her e-mail is mjones@immaculata.edu.

![](/api/attachments/4X2BK5SS/fulltext/images/c4e3124089645050cf5ab6c2b206ce243286ac37a61978b208e741155b3b9c12.jpg)

Il-Yeol Song is a professor and the co-director of Data Mining and Bioinformatics Lab in the College of Information Science and Technology at Drexel University, Philadelphia, Pennsylvania. He received the MS and PhD degrees from the Department of Computer Science, Louisiana State University, in 1984 and 1988, respectively. His research focuses on practical application of modeling and design theory to real-world problems. His current research areas

include database modeling and design, design and performance optimization of data warehouses and OLAP, database systems for cyber forensics, data modeling and quality in bioinformatics, and objectoriented analysis and design with UML. Dr. Song has won three teaching awards from Drexel University: Exemplary Teaching Award in 1992, Teaching Excellence Award in 2000, and the Lindback Distinguished Teaching Award in 2001.Dr. Song has authored or co-authored more than 140 refereed technical articles in various journals, international conferences, and books. Dr. Song is a co-author of the ASIS Pratt\_Severn Excellence in Writing Award at National ASIS meeting (1997), the Best Paper Award in the 2004 IEEE Symposium on Computational Intelligence in Bioinformatics and Computational Biology (IEEE CIBCB 2004), and a Best Paper Nominated at the 2004 IEEE/ACM Web Intelligence Conference. He received a Research Scholar Award from Drexel University in 1992. He has also won thirteen research awards from the annual Drexel Sigma Xi Scientific Research Competitions or annual Drexel Research Days. He served or is serving as a program co-chair of DOLAP '98, CIKM '99, DOLAP '99, ER '03, DGOV '04, BP-UML '06, and DaWaK ‘07. Dr. Song is a steering committee member of CIKM, ER, and DOLAP conferences/workshops. He is a co-editor-in-chief of the Journal of System and Management Sciences. He is also an associate editor for the Journal of Database Management and International Journal of E-Business Research. In addition, he was a guest editor for Journal of Database Management, Data and Knowledge Engineering, and Decision Support Systems. He is a member of ACM, IEEE Computer Society, KSEA, and KOCSEA. His e-mail is song@drexel.edu.
