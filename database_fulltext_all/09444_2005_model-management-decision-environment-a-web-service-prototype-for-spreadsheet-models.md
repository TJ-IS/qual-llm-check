---
otero_id: 9444
otero_key: "PD7ZUX3T"
title: "Model management decision environment: a Web service prototype for spreadsheet models"
authors: "Bala Iyer; G. Shankaranarayanan; Melanie L. Lenard"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.01.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model management decision environment: a Web service prototype for spreadsheet models

Bala Iyer<sup>a,</sup>\*, G. Shankaranarayanan<sup>a</sup>, Melanie L. Lenard<sup>b</sup>

<sup>a</sup> Information Systems Department, School of Management, Boston University, 595 Commonwealth Ave Boston, MA 02215, USA <sup>b</sup> Crystal Decision Systems, 1318 Beacon Street, Suite 2, Brookline, MA 02146, USA

Received 1 September 2002; accepted 1 January 2004 Available online 8 April 2004

## Abstract

In the modern day, digital enterprise data and models are widely distributed. Decision-making in such distributed environments needs secure and easy access to these resources, rapid integration of decision models, and the ability to deploy these in real time. This demands a different approach for model management—one that permits decision-makers to not only share/access but also evaluate/understand models, choose appropriate ones from a collection of models, and orchestrate the execution of the model(s) in real time. In this paper, we describe an architecture that defines a service-oriented, Web servicebased approach to model management. We first present a classification of stakeholders from the perspective of model management and identify the layers of modeling knowledge required for managing models. We then define a formal representation for organizing the content knowledge using a graph-based representation. We have used spreadsheet model(s) as a vehicle for explaining and demonstrating our concepts in this paper. Finally, we describe an environment (virtual business environment, VBE) that is based on a Web services architecture that would help store, retrieve, and distribute the layers of modeling knowledge to the various categories of users identified.

Keywords: Structured modeling; Model management; Spreadsheets; Knowledge layers; Web services

## 1. Introduction

Models<sup>1</sup>, like data, are important organizational resources. Ever since Sprague and Carlson’s [30] seminal work recognizing models, along with data and dialog (user interface), as a key component of

Decision Support Systems (DSS), research in model management has attempted to help decision-makers make better use of models [4,15,20,31]. A majority of the research deals with capturing just one type of knowledge (referred to as content knowledge in this paper) about models. Furthermore, models are assumed to be stored in one central location and few deal with models distributed across the organization. In the modern day, digital enterprise data and models are widely distributed and decision-making now demands secure and easy access to these resources, rapid integration of decision-models, and the ability to deploy these in real time. Mobile technologies further impact this by allowing decision-makers to be mobile while permitting access to model/data resources that span organizational boundaries [2]. These demand a different approach for model management—one that permits decision-makers to not only share/access but also evaluate/understand models, choose appropriate ones from a collection of models, and orchestrate the execution of the model(s) in real time.

Early decision support systems were based on a central computing model. Such systems placed the model manager, data manager, and interface manager accessing a single computer. With the advent of local area networks, data and models were often duplicated and changes made were not systematically controlled. This resulted in multiple versions and in- consistent results. Client/server architecture raised issues about partitioning the functionality between clients and servers. The Internet has promoted the rise of service-oriented architecture such as Web services that creates new opportunities and challenges for maintaining model integrity while permitting very widespread distribution and sharing of models and data.

A key question for DSS designers using the client/ server model is how to partition the functionality between the clients and servers. A simple approach is to store the model, data, and dialog managers in the client. The model base with the models and associated data is stored in the server. This approach would result in a tight coupling between the model base and the client applications—a change to the application logic implies that the model base must be modified to reflect the change.

Another approach—a three-tiered one—would make the client responsible only for presentation and user interface logic. This allows the server to specialize in maintaining the model base and the database. The middle tier stores the logic for constructing or revising models and the strategy for accessing the information that will facilitate this change. This loosely couples the client and the server, allowing many unrelated clients to use the same data/model server or make many servers accessible to the same client.

In this paper, we describe a variation of this threetiered architecture that adopts the service-oriented, Web service-based approach to model management. We also describe the implementation of this architecture in a decision support environment. We first present a classification of stakeholders from the perspective of model management and identify the layers of modeling knowledge required for managing models. We then define a formal representation for organizing the content knowledge using Structured Modeling (SM) [15]. For brevity, we have restricted our discussion in this paper to content knowledge. The architecture described incorporates the knowledge layers to support model management as a Web service. We finally describe the implementation of this architecture and show how it can support decision-making in distributed decision environments. Such a facility would not only promote sharing and reuse of models but also encourage collaborative work [15]. We have used spreadsheet models as a vehicle for explaining and eventually demonstrating our concepts as they are probably the most widely used (and abused!) modeling technique in organizations. There are an estimated 30 million users [28] of spreadsheets and 20 – 40% of the models contain errors [24].

Section 2 summarizes the relevant work on distributed model management and spreadsheet models to differentiate our contribution and to define the scope of this research paper. Section 3 presents the classification of stakeholders based on user requirements and the different types of knowledge required for managing models. Section 4 describes the organization of content knowledge (the focus here) and a brief description of the options for capturing other knowledge layers. The architecture and implementation details for model management as a Web service is proposed in Section 5. The conclusions and directions for further research are presented in Section 6.

## 2. Relevant literature

In their article on model management systems, Bharadwaj et al. [4] identify three approaches to model representation: database, graph-based, and knowledge-based. These approaches are differentiated based on the discipline from which the underlying concepts were borrowed. The database approach envisions models being organized using a data model [12], such as the entity – relationship (E – R) model [7] or the relational model [8]. The graph-based approach relies on concepts of graph theory and represents mathematical models as graphs, digraphs, or hypergraphs. The knowledge-based approach uses knowledge representation schemes, such as semantic networks, first-order predicate calculus, and production rules. Structured Modeling (SM), the framework adopted in this paper for organizing content knowledge, is a graph-based approach.

Bharghava et al. [5] describe DecisionNet, a system for sharing models and solution algorithms on the Internet. Two architectures are proposed for locating models, each built for one of two modeling languages: AMPL [14] and GAMS [6]. Both architectures rely on model suppliers to register their product with ‘‘yellow pages’’ that can be searched by potential model users (a.k.a. decision-makers). The architecture for AMPL relies on the user being knowledgeable about models, methodologies, and languages. In contrast, the architecture for GAMS expects very little modeling knowledge from the user. Instead, it requires model suppliers to provide detailed information about the products they register and relies more on the system (software agents) to help users identify and use models. The architecture proposed in this paper is more akin to the GAMS architecture in that model suppliers register their models along with detailed information about each with a Web service broker. Users request for models by specifying requirements and the broker assists in retrieving relevant models and sets up the model environment for execution at the user end. The model execution in DecisionNet occurs at the supplier end while it occurs at the user end in our system. Moreover, the users may customize existing models to better suit their needs as models are recreated at the users’ end.

Dolk [11] proposes an integrated modeling environment for distributed model management that permits customization. The decision metrics, structural definitions of the models, and the modules used for analyzing or interpreting results are each stored separately: the first two in data warehouses and the third as software components that can be plugged in, based on the user’s need. A conversion process reads the model information in the warehouse and represents models in Unified Modeling Language (UML) that in turn may be translated into executable code for model execution. The plug-ins attach to the executable code. It is not explicit whether the users can search for models, query model information, or evaluate models.

Furthermore, the use of a data warehouse to capture structural definitions limits the extent of ‘‘structural’’ customization possible. Both model providers and users must be knowledgeable about the models to register and deploy them.

Huh et al. [17] describe a collaborative model management environment for distributed model management in organizations. This work emphasizes the tracking and management of changes to models, derivation hierarchies, and the systematic propagation of model changes across the different departments within the organization. This research provides a mechanism for maintaining the consistency of the shared (organization-wide) model base. In our implementation, we have not addressed tracking and propagation of changes to models or derivation hierarchies in model management. Our focus here is on identifying the layers of knowledge for model management and describing an architecture that incorporates these layers to support model management as a Web service.

We illustrate our approach to model management using spreadsheet models. Ronen et al. [27] were among the first to suggest a structured approach to designing spreadsheet models. They propose the use of Spreadsheet Flow Diagrams (SFD) to encourage structured, top-down design of spreadsheets. Isakowitz et al. [18] propose separating the logical and physical aspects of spreadsheet models to support their sharing and reuse. They identify the primitives needed to represent spreadsheets that define algorithms to factor (or synthesize) spreadsheet models to decompose (or build) them using these primitives. Plane [25] uses ideas from influence diagrams for a graphical technique called influence ‘‘charts’’ to represent the logical structure of spreadsheet models. Two advantages of the graphical technique are highlighted: its usefulness in building complex models and its ability to improve communication within model building teams.

Apart from the concepts presented in literature, we believe that there are additional needs for managing spreadsheet models in a distributed environment. Firstly, given the disparate set of stakeholders and their unique requirements for model information (knowledge), there is a need to clearly understand and distinguish the different types of knowledge about models. To easily manage the knowledge, there is a need for a formal framework to organize knowledge contained in models (e.g., spreadsheet models). Finally, to implement a system for model management in a distributed environment, an architecture that ties together the different components and creates a seamless environment is needed.

## 3. Knowledge layers for model management

To identify the different types of knowledge associated with models, we first identify the different types of model users (stakeholders) and their disparate requirements for modeling knowledge. We adopt this approach to associate the knowledge layers with the stakeholders and thereby define the manner in which the knowledge in each layer is organized, managed, and delivered.

## 3.1. User roles

There are three roles played by users of model management systems (see Fig. 1), and this leads each to have a different view of model management. The first role is that of a model builder who is involved in building models by abstracting from some real life phenomenon. After understanding the domain, this person builds and maintains models using a model definition language.

The second role is that of an analyst. An analyst obtains results for decision-makers by applying models to data. To do this, the analyst has to identify appropriate models, manipulate them to suit the current problem, and run these models with data sets to produce results. If the analyst can’t find an appropriate model, he/she interacts with model developers to build one.

![](/api/attachments/PD7ZUX3T/fulltext/images/76a250d128b5f4351c157f87578e3e10855d5ab8736a63674f02da289210a58a.jpg)  
Fig. 1. Types of model users.

The last role is that of a decision-maker. The decision-maker is primarily interested in obtaining support for some decision-task. To accomplish this, the decision-maker may, using a suitably designed interface, access a model, provide requisite data, execute the model, and inspect the results. He/she may require support for interpreting the results. In other instances, the decision-maker may choose to delegate the task to analysts.

Typically, a single individual may play all three roles. Today, with widespread use and sharing of spreadsheet models within organizations, it is more likely that these roles will be distributed over several people. Each role has a different objective in interacting with the model and, therefore, its requirements for model information is different.

## 3.2. Types of model knowledge

Modeling knowledge may be classified into five different layers or types as shown in Fig. 2. These are workflow, evaluative, operational, content, and process knowledge layers.

The workflow knowledge layer captures information that will facilitate workflow management. Workflow is the coordination of the execution of a process that is designed as a sequence of tasks [21]. Workflow management systems aim to define, support, and monitor the coordination of tasks in a business process. Currently, there exist several formalisms for capturing workflow knowledge: action workflow diagrams [23], role interaction nets [29], and dynamic workflow management [21]. Workflow knowledge helps the system ‘‘push’’ relevant models to the users (decision-makers) when needed.

The evaluative knowledge layer contains information about the model’s overall value and any metrics associated with the model. It provides responses to questions posed by analysts and decision-makers on issues such as the reliability, robustness, and usefulness of the model in decision-tasks. Such knowledge may be obtained from model builders and from decision-makers who have previously used the model. In addition, discussion groups or newsgroups within the organization may capture this type of knowledge.

![](/api/attachments/PD7ZUX3T/fulltext/images/73135796fd5c4c6bcae8bd6b7424741e595d70533da03e3e5abb6ac5ebff1707.jpg)  
Fig. 2. Knowledge layers for model management.

The operational knowledge layer contains information about model pragmatics such as the parameters and data required to run the model, keystrokes needed to get results, and the model execution time. Besides, this layer also captures information about solution strategies such as goal seeking, optimization, and scenario analysis. Typically, such information is contained in reference/user manuals.

Content knowledge captures the logical workings of models including spreadsheet models. It is valuable when an analyst wants to make some minor changes to an existing spreadsheet model or when a model builder wants to reuse one or more existing models to build a new one. For example, while using a profit and loss model, an analyst may want to change the formula for, say, depreciation. This would be difficult if he or she did not understand the existing formulas. Isakowitz et al. [18] use the schema representation language (FRL) as an internal representation for spreadsheet schemas. In this paper, we use Structured Modeling to organize and represent content knowledge.

The process knowledge layer stores all the information related to the process of building spreadsheet models. This knowledge will facilitate the building of models and their maintenance under changing environmental conditions. Model builders are involved in cycles of information gathering and discussions with other participants. Very rarely do model builders get their models ‘‘right’’ the first time. They are constantly changing the structure and underlying assumptions of the models. When they make the changes to the model, they often struggle to determine the reasoning behind existing structures and assumptions. To facilitate the ability to modify models under such circumstances, it is necessary to have access to the formulation history in an organized manner [10]. Usually, model builders rely on memory or informal notes for this purpose, but for large problems in a more collaborative environment, the limitations are obvious. This type of knowledge will be valuable primarily to model builders and, to a lesser extent, to analysts and decision-makers.

To illustrate how the layers of modeling knowledge are used, consider the following example. Forecasting the earnings for the foreseeable future is a recurrent event in most organizations. In the case of Quantum Consulting, this forecast was presented during their quarterly consultant meetings. Jerry, the president of the company, would present the group with an overview and finish with a status report on performance and how it compared to the goals that were set. He relied on his office assistant, Kathy, to provide him with the revenue projections. Kathy usually called the managers for the various practices to get their revenue estimates. She would use these numbers and other assumptions to make the earnings projections.

Recently, Kathy left the company to pursue other interests. Because a quarterly meeting was fast approaching, Jerry quickly moved another employee, Julie, to her position. The first thing that Julie did was to arrange a half-day meeting with Jerry to get an understanding of the overall process. In our framework, this knowledge would reside in the workflow knowledge base. After she understood the process, Julie wanted to know if there were any standard forms or spreadsheet models available to help her in the process. Jerry told her that Kathy had developed a spreadsheet model for the forecasting. After talking to the network administrator, Julie located the spreadsheet easily. However, she had problems using the spreadsheet. She did not know where the assumptions were stored, what data she had to supply, or who could provide her with the information. In essence, she was looking for operational knowledge. To solve this problem, Jerry authorized the hiring of Kathy to come in on weekends to train Julie.

For the next quarterly meeting, one major change was causing problems for Julie. One of the company’s clients, Mtech, decided to infuse some capital into the company and a guaranteed set of projects in exchange for a 15% discount in the rates charged by Quantum.

This meant that the projected sales growth rate had to be changed to reflect the Mtech business. Because Julie did not have to make any such changes during the previous quarter forecast, she was now at a loss. If she had a knowledge base containing content knowledge, she would have realized that the projected growth rate was 10% for the next three quarters and 20% for the following two. Knowing this, she could confidently add the guaranteed revenues from Mtech to the model and get the new net earnings estimates.

Model knowledge plays an important role in effectively managing models. To be useful, the captured knowledge must be organized in a manner that facilitates convenient management and delivery of knowledge in widely distributed settings. In this paper, we restrict our discussion on organizing knowledge to the content knowledge layer. Options for organizing and managing other knowledge layers are briefly addressed for completeness.

## 4. Organizing content knowledge for model management

Structured Modeling is a framework for representing models based on a set of interrelated definitions of all the elements comprising a model [15]. In effect, this definitional system is a model of models or a metamodel. Structured Modeling identifies the basic components of models, the relationships among these components, and conditions under which a model may be termed ‘‘structured’’. All this is accomplished using three basic types of elements: entities, attributes, and functions. For details on using Structured Modeling, readers may refer to Ref. [22].

For a spreadsheet model to be reused, new users (model builders and possibly analysts) and model builders need to learn about its inner workings. New users need to understand the input requirements to use the model. Model builders need to understand underlying assumptions to modify it. This can be difficult because the very freedom allowed by spreadsheets (i.e., any given cell in the spreadsheet may contain either data or a formula or some text) often obscures the logical design of the model (i.e., the model schema).

Isakowitz et al. [18] propose a method for extracting the logical structure and data elements from a standard spreadsheet. The first step in their method asks that users outline their spreadsheet; then, a factoring algorithm extracts the model schema (along with the data, editorial, and binding properties) for the spreadsheet. They also explore how the model schema, once obtained, can serve as a template to synthesize physical spreadsheets.

Taking this idea one step further, we propose that model builders work with a model schema (in effect, an outline of the spreadsheet) throughout the modeling process. This model schema models a spreadsheet in much the same way as a data model schema models a database. The model schema captures the logical relationships in the model and serves as the basis for creating the code to define the physical spreadsheet.

## 4.1. Model schema

We propose representing the model schema graphically using a generic structure diagram. This generic structure diagram is based on the genus-level graph of SM and is similar to influence charts suggested by Plane [25]. The generic structure diagram would always be available as an alternate representation of the spreadsheet. (Having an alternate view of the spreadsheet is analogous to what is done in Microsoft Project k where project activities may be viewed as a PERT chart or a Gantt chart or as a spreadsheet containing activities, precedence, duration, start, and finish dates.).

As an illustration, consider a simple spreadsheet model (adopted from Ref. [18]) shown in Fig. 3. It is a projection of profit and loss over a period of 6 years. The generic structure diagram (model schema) for this spreadsheet is shown in Fig. 4. In Fig. 4, we have used rectangles to represent entities, triangles to represent attributes, and octagons to represent functions. Solid lines show functional dependence. For example, the calculation of COGS (Cost of Goods Sold) depends on Sales and COGS<sup>\_</sup>Rate. A dotted line is read as ‘‘is indexed by’’ or ‘‘is an attribute of’’. For example, Lease is indexed by Year, meaning that there is a value for the attribute Lease corresponding to each instance of the entity Year.

Every generic structure diagram corresponding to some model will have the special entity Scenario (shaded in Fig. 4 and duplicated for convenience only). This entity can capture attributes (and assumed values for each) that do not belong to any specific

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr><tr><td>1</td><td></td><td>growth</td><td>overhead</td><td>COGS</td><td>tax rate</td><td></td><td></td></tr><tr><td>2</td><td>assumptions</td><td>10%</td><td>2,500</td><td>60%</td><td>48%</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td colspan="4">P&amp;L Forecast (all figures in 000&#x27;s)</td><td></td><td></td></tr><tr><td>5</td><td></td><td colspan="4">-</td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td>1992</td><td>1993</td><td>1994</td><td>1995</td><td>1996</td><td>1997</td></tr><tr><td>8</td><td></td><td colspan="6">- = = = = - = = = = = - = = = = = - = = = = = - = = = = = - = = = = = - = = = = = -</td></tr><tr><td>9</td><td>sales</td><td>6,000</td><td>6,600</td><td>7,260</td><td>7,986</td><td>9,148</td><td>10,280</td></tr><tr><td>10</td><td>COGS</td><td>3,600</td><td>3,960</td><td>4,356</td><td>4,792</td><td>5,489</td><td>6,168</td></tr><tr><td>11</td><td>overhead</td><td>2,500</td><td>2,500</td><td>2,500</td><td>2,500</td><td>2,500</td><td>2,500</td></tr><tr><td>12</td><td>lease</td><td>100</td><td>100</td><td>500</td><td>500</td><td>500</td><td>500</td></tr><tr><td>13</td><td>gross</td><td>(200)</td><td>40</td><td>(96)</td><td>194</td><td>659</td><td>1,112</td></tr><tr><td>14</td><td>tax</td><td>0</td><td>19</td><td>0</td><td>93</td><td>316</td><td>534</td></tr><tr><td>15</td><td></td><td colspan="4">-</td><td></td><td></td></tr><tr><td>16</td><td>net income</td><td>(200)</td><td>21</td><td>(96)</td><td>101</td><td>343</td><td>578</td></tr><tr><td>17</td><td>Avg_Net_Inc</td><td>124</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 3. Sample spreadsheet model.

entity in the model but define the model environment in general (e.g., Growth<sup>\_</sup>Rate). This convention avoids the awkwardness of having attributes that do not belong to any entity. Furthermore, it corresponds neatly with the ‘‘Scenario Manager’’ feature of Microsoft EXCELk, a feature that makes it possible to generate multiple scenarios from the same spreadsheet model. The Scenario Manager allows the user to supply a name (e.g., Base Case) for the scenario, designate those cells whose values determine the scenario, and designate those cells containing the scenario result. In Fig. 4, we see that Growth<sup>\_</sup>Rate, Cur<sup>\_</sup>Sales, COGS<sup>\_</sup>Rate, Overhead, Tax<sup>\_</sup>Rate, and Lease are the values that determine the Scenario, and Avg<sup>\_</sup>Net<sup>\_</sup>Inc is the designated result. In addition, the generic structure diagram shows the cardinality of the various relationships. For spreadsheet models, cardinality information is essential to define the correct layout generating spreadsheets.

![](/api/attachments/PD7ZUX3T/fulltext/images/87174282e4af4c85224e4b4a69d475405b141c22ec6fb96d905f3216b404ba19.jpg)  
Fig. 4. Generic structure diagram (model schema) for the spreadsheet in Fig. 3.

In Fig. 4, the relationships for which no cardinality information is specified are assumed to be one-to-one; for example, there would be one value of the attribute Lease and one value of the function Sales for each Year entity, and one value of the function Gross for each value of Sales and each value of Lease. In Fig. 4, Scenario is in a one-to-many relationship with Growth<sup>\_</sup> Rate, that is, specifying one scenario includes providing many values for growth rate. As there is a one-toone relationship between Year and Growth<sup>\_</sup>Rate, there will be as many values for Growth<sup>\_</sup>Rate as there are Years. Furthermore, as there is a one-to-one relationship between Taxes and Year by way of Sales and Gross, there will be as many values of Taxes as there areYears. A different situation is the relationship between Tax<sup>\_</sup>Rate and Taxes. Each Scenario corresponds to one value of Tax<sup>\_</sup>Rate, but that same value is used to calculate the many values of the function called Taxes.

Another use of cardinality is shown by the function Avg<sup>\_</sup>Net<sup>\_</sup>Inc, which would calculate the average over all Years of the values of Net<sup>\_</sup>Inc. The cardinality of the relationship between Avg<sup>\_</sup>Net<sup>\_</sup>Inc and Net<sup>\_</sup>Inc would be one-to-many. This information makes it possible to anticipate that only one cell and one formula will be needed for Avg<sup>\_</sup>Net<sup>\_</sup>Inc, no matter how many cells and formulas are needed for Net<sup>\_</sup>Inc.

There are restrictions on what constitutes a valid diagram. For example, cycles are not permitted—that is, if Sales is dependent on Advertising, then Advertising cannot be (even indirectly) dependent on Sales. In other words, there must be some sequence for evaluating the spreadsheet. Furthermore, an attribute can be dependent only on an entity; a function can be dependent only on attributes and other functions. These and other rules can be enforced during the drawing process. Jones [19] has used graph grammars as the basis for a syntax-directed editor for graphical representations of structured models.

For each function shown on the diagram, the user is asked to specify a generic formula using the names of attributes or other functions. This formula might be hidden from view or shown on the diagram. For example, the user might define Gross as:

Gross ¼ Sales - COGS - Lease - Overhead

The graphical representation is intuitively appealing, and there is anecdotal evidence (see Plane [25]) that it is helpful to model builders. However, it may become unwieldy for larger, more complex models (refer Appendix C for the generic structure diagram of a slightly more complex model). Furthermore, the schema needs to be transferred over the network to the users when accessed and the graphical representation is not well suited for this. For these and other reasons, we need to have a text version of the model schema as well. Fig. 5 shows the text schema for the

Scenario /e/

Year /e/

Growth Rate /a/ {Year, Scenario}

Cur\_Sales /a/ {Scenario}

COGS\_Rate /a/{Scenario}

Overhead /a/ {Scenario}

Tax\_Rate /a/ {Scenario}

Lease /a/ {Year}

Sales (Growth\_Rate, Cur\_Sales) /f/ {Year}

COGS (Sales, (N:1)COGS\_Rate) /f/

Gross (Sales, COGS, Lease, (N:1)Overhead) /f

Taxes (Gross, (N:1)Tax Rate) /f/

Net\_Inc (Gross, Taxes) /f/

Avg\_Net\_Inc ((1:N)Net\_Inc) /f/

Fig. 5. Model schema in text form for the sample spreadsheet model.

spreadsheet model in Fig. 3. The syntax used in Fig. 5 for specifying the generic components of the model and their dependencies is loosely based on Geoffrion’s [15] original proposal. The name of each component is given first, followed by functional dependencies, if any, enclosed within parentheses. Each component is then identified as an entity (denoted as /e/), attribute (/a/), or function (/f/). This is followed by indexing dependencies enclosed within braces [2] for attributes and (optionally) for functions.

We extend the basic SM notation by adding a notation for indicating functional dependencies that are not one-to-one. For example, the many-to-one relationship between COGS and COGS<sup>\_</sup>Rate is shown by inserting (N:1) before COGS<sup>\_</sup>Rate like ‘‘COGS (Sales, (N:1)COGS<sup>\_</sup>Rate) /f/’’. This tells us that COGS is a function having a one-to-one (implicitly) dependence on Sales and a many-to-one dependence on COGS<sup>\_</sup>Rate.

To implement this in the model management environment, a (any) spreadsheet model must be translated into its equivalent model schema (factoring-like process) and a spreadsheet model must be created from its equivalent model schema (synthesizing process). These functionalities are implemented using software modules (or engines) in our implementation of the model management system and are described in Section 5. The following section provides an overview of how the content knowledge captured in the model schema and generic structure diagram (for a spreadsheet model) is reflected in the spreadsheet model that was synthesized using this content knowledge.

## 4.2. Working with the spreadsheet

The spreadsheet that was synthesized from the generic structure diagram (Fig. 4) and model schema (Fig. 5) is shown in Fig. 6. The generic formulas are repeated at the top of the spreadsheet for easy reference. The shaded areas of the spreadsheet are the cells where the user would enter data values or formulas. Firstly, the user would enter names or labels for the instances of the entities, such as ‘‘Year’’. (These could be the actual years (1992, 1993, etc.) or just an identifying number (1, 2, etc.). However, the data entered is restricted to text (not numeric) form so that it may be used to create names for cells. Once this was completed, areas of the spreadsheet would be allocated for all of the attributes and functions. Each such area is assigned a unique name for reference.

The user would then enter values for attributes. Because the attributes ‘‘Lease’’ and ‘‘Growth<sup>\_</sup>Rate’’ depend on ‘‘Year’’ (Fig. 4), the spreadsheet in Fig. 6 allows for entering a value for each of these attributes for each year specified. The entity Sales has a selfreferencing arrow in Fig. 4. This indicates that the formula for Sales in some year is dependent on Sales in other years. In such a case, the user would be asked to enter these formulas individually. An area in the spreadsheet is set aside for supplying this detail. For the model shown in Fig. 6, Sales in 1992 is set equal to the attribute Cur<sup>\_</sup>Sales. For the years 1993–1995, sales are forecasted to grow linearly. In subsequent years, the growth rate is applied to the average of the preceding 2 years. The generic structure graph does not capture these details. The auditing tool (Fig. 7) supplied with EXCEL can get a graphical representation of this relationship.

Finally, the generic formulas for the functions will be translated into array formulas in the spreadsheet. As an illustration, Fig. 7 shows the EXCEL window with the menu bar and the formula bar along with the spreadsheet. The cells for the function ‘‘Gross’’ are selected, causing the name of the highlighted area (‘‘Gross’’) and the array formula defining the value of ‘‘Gross’’ to appear on the formula bar.

The spreadsheet does not permit altering an individual cell in any area defined by an array formula. If a user wishes to enter elements of a function individually, he/she would be required to return to the generic structure diagram and add a self-referential arrow. Of course, the user can change the array formula shown at the top of the spreadsheet causing the corresponding formula in the diagram to be changed also.

The spreadsheet user is free to modify the physical appearance of the spreadsheet in any way that does not violate the relationships shown in the generic structure diagram. For example, the user might choose to move a section of the spreadsheet to a different place on the same sheet (or to a different sheet) or the user might choose to transpose the rows and columns of a given area (referred to as changes to binding properties in Ref. [18]). However, the user would be prevented from moving part of any area (e.g.,

<table><tr><td>Instructions</td><td colspan="7">Data and Formula Entry</td></tr><tr><td rowspan="6">Formulas for generic functions</td><td colspan="7"></td></tr><tr><td>COGS</td><td colspan="6">=Sales*COGS_Rate</td></tr><tr><td>Gross</td><td colspan="6">=Sales - COGS - Lease - Overhead</td></tr><tr><td>Taxes</td><td colspan="6">=IF ((Gross &gt;0), Tax_Rate*Gross,0)</td></tr><tr><td>Net_Inc</td><td colspan="6">=Gross - Taxes</td></tr><tr><td colspan="7"></td></tr><tr><td>Enter name for Scenario</td><td>SCENARIO</td><td colspan="6">Base Case</td></tr><tr><td rowspan="2">Enter values for each Scenario attribute</td><td>Cur_Sales</td><td colspan="2">Overhead</td><td colspan="2">COGS_Rate</td><td colspan="2">Tax_Rate</td></tr><tr><td>6000</td><td colspan="2">2,500</td><td colspan="2">60%</td><td colspan="2">48%</td></tr><tr><td>Enter labels (text only) for each entity.</td><td>YEAR</td><td>1992</td><td>1993</td><td>1994</td><td>1995</td><td>1996</td><td>1997</td></tr><tr><td rowspan="2">Enter values for Corresponding attributes</td><td>Growth_Rate</td><td>0%</td><td>10%</td><td>10%</td><td>10%</td><td>20%</td><td>20%</td></tr><tr><td>Lease</td><td>100</td><td>100</td><td>500</td><td>500</td><td>500</td><td>500</td></tr><tr><td>Enter formulas for individual functions</td><td>Sales</td><td>6,000</td><td>6,600</td><td>7,260</td><td>7,986</td><td>9,148</td><td>10,280</td></tr><tr><td rowspan="11"></td><td colspan="7">P &amp; L Forecast</td></tr><tr><td>YEAR</td><td>1992</td><td>1993</td><td>1994</td><td>1995</td><td>1996</td><td>1997</td></tr><tr><td>Sales</td><td>6,000</td><td>6,600</td><td>7,260</td><td>7,986</td><td>9,148</td><td>10,280</td></tr><tr><td>COGS</td><td>3,600</td><td>3,960</td><td>4,356</td><td>4,792</td><td>5,489</td><td>6,168</td></tr><tr><td>Lease</td><td>100</td><td>100</td><td>500</td><td>500</td><td>500</td><td>500</td></tr><tr><td>Overhead</td><td>2,500</td><td>2,500</td><td>2,500</td><td>2,500</td><td>2,500</td><td>2,500</td></tr><tr><td>Gross</td><td>(200)</td><td>40</td><td>(96)</td><td>194</td><td>659</td><td>1,112</td></tr><tr><td>Tax</td><td>0</td><td>19</td><td>0</td><td>93</td><td>316</td><td>534</td></tr><tr><td></td><td>----</td><td>----</td><td>----</td><td>----</td><td>----</td><td>----</td></tr><tr><td>Net_Inc</td><td>(200)</td><td>21</td><td>(96)</td><td>101</td><td>343</td><td>578</td></tr><tr><td>Avg_Net_inc</td><td>124</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 6. Spreadsheet generated using model schema.

Net<sup>\_</sup>Inc) defined by an array formula. Furthermore, the user could format entries or add labels, shading, lines, notes, etc. in the usual manner (referred to as changes to the editorial properties of the spreadsheet in Ref. [18]). To understand the usefulness of storing content knowledge using SM, let us go back to the example described at the end of Section 3. From that description, it is clear that Julie did not have a good understanding of the spreadsheet model that she discovered with the network administrator’s help. If the model schema were captured using a generic structure diagram, Julie can get some help when she tries to make changes to the spreadsheet model. For example, let us assume that when she learns about the infusion of capital from Mtech, she tries to change the sales estimates in the spreadsheet. Based on the generic structure diagram, we can generate an error message indicating that the sales estimates are dependent on sales in other years. Thus, the content knowledge can help her understand the spreadsheet model and reduce errors made in modifying it.

![](/api/attachments/PD7ZUX3T/fulltext/images/fb8415345d7e145072ea85370b0beccfda915edcd2cfa21a3337f1adc2b4bcae.jpg)  
Fig. 7. Modeling aids in EXCEL spreadsheets.

We have addressed content knowledge in detail here. The other four knowledge layers are important, and for completeness, we include a brief description of how these may be organized. As for the other layers of the knowledge base, we still have to provide support for the processes that create them and describe structures to store them. For example, to store workflow knowledge, techniques such as Role Interaction Nets [29], Action Workflow [23], and Dynamic Workflow modeling [21] can be used. The Dynamic Workflow technique is used in the implementation described here. Both evaluative knowledge and operational knowledge can be captured using commercially available discussion tools/products such as LotusNotes<sup>2</sup> and Blackboard<sup>3</sup>. In our implementation, both operational and evaluative knowledge are organized as ‘‘briefs’’ (brief-documents) that are managed using Blackboard and are searchable using keywords only. To capture process knowledge, systems that capture decision rationale, such as gIBIS [9] and CADS [13], are available. In our implementation, process knowledge is stored in the form of ‘‘assumptions’’. A section of the spreadsheet model (say, A74 –F80) is used to define the assumptions/business rules applicable to this model and this information is saved as text when a model spreadsheet is factored. Similarly, when a model is synthesized, the process knowledge is saved as metadata associated with the model.

## 5. Architecture of the virtual business environment

To support decision-making in dynamic environments, we propose a virtual business environment (VBE). A business environment is considered virtual when its instantiation at any point (spatial and temporal) is dependent on the physical surroundings and locations of the actors, decision contexts, capabilities of the devices being used, and the actors’ entitlements. An enterprise can have several such environments, and its boundaries may be established on an instance-by-instance basis. The business processes (or subprocesses) are defined in a virtual environment based on the needs of the decision-maker(s). The VBE would allow organizations to run different business processes concurrently and securely while sharing resources. For example, a VBE can support concurrent availability of different business views (e.g., one for senior executives and another for project managers, both sharing data, models, and business contexts).

Conceptually, the VBE (Fig. 8) consists of a domain resources subsystem, a subsystem of engines, and a dialog management subsystem. The domain resources subsystem manages structured and subtly structured (nontabular) data including expert knowledge, models, and data needed for decisionmaking in that domain. The dialog management subsystem is responsible for interacting with the user to query information, provide inputs, and interpret the responses from the engines to create ‘‘individualized’’ outputs for the user. The outputs can be rendered in different ways as determined by the metaphors (captured in the user profile). The process domain typically contains software components called Business Context Engines (or simply, an engine). An engine is defined as an analysis object that represents and implements a complex business capability requiring the integration of knowledge, decision-models, and data resources. Engines are shareable and reusable in disparate business contexts. The engines can be thought of as large blocks of reusable applications that instantiate complex business functions. To do so, the engine needs to integrate resources, synchronize models/data, normalize outputs, dynamically allocate resources, and enforce business rules. Engines may be added to or expunged from a VBE. An engine manager maintains the library of engines and identifies appropriate engines and the necessary resources to run them. Core engines required for implementing the VBE for model management are [32]: (1) knowledge management engine (for managing and providing access to the model knowledge); (2) personalization engine (to customize access and display of information for decision-makers); (3) resource maintenance engine (to capture and maintain model metadata and resources); (4) delivery engine (to target delivery points and coordinate delivery of information); (5) analysis engine (to interpret results and evaluate ‘‘what-if’’ scenarios); (6) factoring/synthesis engine (to extract the structured model components for spreadsheets and to construct executable spreadsheets on the fly [18]); and (7) a coordination engine (to coordinate the execution of multiple models and associated resources). Key design issues for the VBE, similar to research challenges tackled for distributed models [1], include: (1) locating engines, data, expertise, and other resources distributed across the environment; (2) establishing and maintaining interengine communications on the network; (3) coordinating the execution of distributed engines; (4) synchronizing replicated engines or data to maintain a consistent state; (5) detecting and recovering from failures in an orderly, predictable manner; and (6) securing resources by limiting remote access to authorized users.

![](/api/attachments/PD7ZUX3T/fulltext/images/3918ed2af35cfa1f838b1c5e328ff587dbce72d40a0aab975dda5ce12e47e422.jpg)  
Fig. 8. A conceptual view of a VBE (shown with decision-maker component).

This environment is also connected to a modelbase, database, schema, a document base, discussion archive, and a layered knowledge base as described in Section 3. Based on ideas about user views of model management presented in Section 3, we identify three types of client components to implement the functionality needed to support the three user roles. In addition, we list a fourth type, model administrator, to fulfill a few system-generated needs. This role of a model administrator is quite similar to the role played by a database administrator. In the next few paragraphs, we will describe the functionality of each client, along with the associated tasks that need to be performed.

## 5.1. Decision-maker

This client component helps the decision-maker search and select models from the model base. To facilitate the search, we couple it with the knowledge management engine that supports searching. Once the user selects a model from the model base, the client has to interpret the SM representation of the model and determine the data that the user has to provide. After getting data from the user, the client should facilitate model execution (this requires access to solvers) and allow the user to select the desired outputs from the model. Finally, this client should also help to integrate the results of running the model with the existing workflow of the user. This is done by analyzing the workflow, representing them using a workflow representation language, and storing them in the layered knowledge base.

## 5.2. Analyst

Using this component, the analyst can either select a model or try to comprehend the model that the decision-maker has chosen. This means that this client, just as in the case of the end-user client, should understand Structured Modeling descriptions of models and help the analyst select the required outputs and run the model. This client must also help the analyst move data and outputs generated by a model from one model to another. In addition, the analyst client should provide an interface that will help the analyst make changes to the models and to submit them as new models.

## 5.3. Model builder

This component helps model builders to create and submit new models, using the underlying model definition language, into the content layer of the knowledge base. In our work, we use Structured Modeling primitives to describe models. This means that the client interface could use a graphical or character-based front end to get the definitions from the model developer. After getting the definition from the model developer, the client should interface with a spreadsheet package and help the developer move from the definition to an instance of the spreadsheet model as shown in Fig. 6.

## 5.4. Model administrator

This component supports the needs of the model administrator. The model administrator can use this client to enter information into the layered knowledge base, especially into the workflow, operational, evaluative, and process layer. To provide this functionality, the client should choose a representation language for each layer in the knowledge base and provide a user-friendly interface to define each. Model administrators can use this client to define access rights to models, automate procedures for submitting and using models from the system, and implement usage policies.

## 5.4.1. Implementation

In its current form, the (interactive) decisionmaking component in the VBE (Fig. 8) is designed and implemented using applets, Dynamic HTML, or Java server pages. This client component is used to locally handle user navigation, manage layouts and displays, perform computations, and compose the user query. The engines (shown in Fig. 8 as a layer of engines topped by Business Context Engine) in the architecture diagram are the various engines that client components (decision-maker, administrator, etc.) can use to access the information contained in the repositories. In some situations, users have to make choices without sufficient information about the alternatives. We have incorporated this layer in the architecture to assist and augment the process that users rely on for finding the models of interest. This concept is quite similar to the notion of ‘‘recommender’’ systems described in Ref. [26]. Each engine has an XML wrapper that describes what services it provides. An engine can be created from scratch or it can encapsulate functionality in existing applications as a Web service. When an engine is ready to be published, its description can be documented using WSDL (see Appendix A for the WDSL description to register the engine for the spreadsheet model in Fig. 3) [16].

A model developer or analyst can call a model by using a URL tag and WSDL description of a particular service/model. This information can be queried from a UDDI registry. If and when a Web service needs to call another service, it sends a request as an XML document in a SOAP envelope. This protocol can work across a variety of transport mechanisms, either synchronously or asynchronously. Fig. 9 illustrates how these pieces fit together. Firstly, the user discovers all the possible models from the registry and how to use them, and then picks the one that is best suited for their need. The user has details on how to invoke the models and can do so directly. The other interesting benefit is that the user can select and group models into composite service that can be called and reused.

The virtual business environment contains a set of domain resources such as the database, the cache, the discussion archive, and the document base. The database contains the data sets that were used to run the models and copies of the outputs generated by running the models. The model base contains information about the model such as model name, default value file, content knowledge schema location, program/macro file, and data file. The database contains the data that is needed to run a model and the output that is generated from running the spreadsheet models. The schema contains the data-type definition information of the content knowledge. In the current implementation, we have to manually create a schema for every model. Future implementations will allow the modeler to describe the model using generic structure diagram using a GUI and the system will generate the corresponding XML schema. Furthermore, if the VBE is implemented for the Web service architecture, tools, such as Apache AXIS, can automatically convert the XML DTD to WSDL. The cache is the working database, that is, it contains all the information (content knowledge, data, and binding) necessary to instantiate and run the spreadsheet model. The discussion base contains the evaluative knowledge captured using discussion tools. Finally, the document base contains the operational knowledge and process rationale stored in the form of documents. This document base could be managed by a document management system. We show the layered knowledge base (in Fig. 8) as a separate entity because it contains the metadata about the various knowledge layers. The actual knowledge itself will be stored in the database, or in the discussion archive, or in the document base.

![](/api/attachments/PD7ZUX3T/fulltext/images/15f59342effc84d93df9bfdb5c59b41b39226a7929e05ca8f942fe51459ef31b.jpg)  
Fig. 9. Conceptual architecture for Web services

In some situations, a decision-maker/analyst needs to execute more than one model in some sequence where results from one serve as an input to another. In the current implementation, this execution of the models must be planned and orchestrated by the user/decision-maker. In the future, this coordination will be largely automated (controlled by the business context engine in the VBE) after obtaining the required specifications from the user.

Having described the static features of the system, we now describe its interaction with a user. The user—model administrator, model builder, analyst, or decision-maker—first logs on to the system. The nature of the interaction from then on varies depend ing on the type of user. For example, if the decisionmaker is trying to locate a model to help in making a decision, he/she could go about that in two ways. In the first case, the user can directly select a model from the model base using the drop down menu. Next, the user can explore the knowledge base of that model. In particular, the user may want to view the generic structure diagram to get a better understanding of the model and may do so by selecting the content option. Once the user is convinced that they have the right model, they can access it and run it using solvers, such as Microsoft EXCELk, to run the models. In the second case, decision-makers use the knowledge management engine to locate a model. This engine that is available in the VBE can help the user search through the knowledge layer and to eventually locate a model. In both cases, a particular model or information from the model base has to be retrieved. To get these models, the knowledge management engine sends a request to the resource maintenance engine that constructs the query and executes it against the knowledge base. Later, the model is imported into a solver to run it and to create reports. In other instances, users may send a request for information about a model. Again, a request is sent to the resource maintenance engine, which will convert these requests into queries against the layered knowledge base.

A model builder could describe a model in schema language that we have proposed or in the graphical form that we outlined in Section 4. This representation could then be converted to XML format that includes a data-type definition file and instances of them. In our implementation, we plan to convert these XML files to Java libraries that can be automatically translated to WSDL file shown in Appendix A (notice that the internal labels assigned by the user to various components within a spreadsheet such as LeaseFor92 are kept intact). This WSDL file can then be used within the Web service environment to provide an interface to the models (and even scope some methods to be public and others to be private!).

We have implemented the Web services environment using IBM’s Web services Toolkit version 3.1 (WSTK). The VBE is implemented on a PC environment running Apache Tomcat 4.0.4 as the Web server. The Web interface is created using Java Server Pages (JSP). The engines are implemented using Java Beans that can communicate with the backend. The domain resources for the VBE are stored in Microsoft SQL Server 2000. In the current implementation, we have five models in the model base. Each model is represented as a structured model and the schema is stored as an XML file in the schema database. Each model has a WSIL (a UDDI substitute) entry in the model base. The functions in the spreadsheet are stored as Java programs. When the synthesis engine incorporates these models into the spreadsheet, they are converted into spreadsheet macros. Only the content knowledge is stored in the model base. In the next release of the VBE, we will add the other layers of knowledge.

## 6. Conclusions and future work

In this paper, we have explored how a collection of models and associated information can be organized, stored, and used over an organizational Intranet using a VBE. We have identified several kinds of users and classified the modeling knowledge they need. We have proposed a method for organizing one layer of knowledge and also presented a preliminary architecture and implementation for a VBE that supports collaborative model management in a distributed model environment.

We have implemented a prototype for collaborative model management described in this paper and plan to test it in an organization where spreadsheet modeling is common. This will allow us to evaluate the framework and architecture and make the necessary changes to deliver the functionality. We would also like to explore how this system is being used to deliver the model management as a capability. A capability calls for more than an implementation [3] of a technology; it also requires organization structure changes and new management processes. For example, in the case of the collaborative modeling environment that we describe, organizations will need incentive systems to encourage decision-makers, model builders, and analysts to share their experiences and models. In addition, new processes have to be put in place to facilitate the use of the environment. These, together with a well-designed modeling environment, are necessary ingredients of an organizational capability for collaborative model-based work in support of decision-making.

We are also in the process of defining a formal framework to evaluate model quality. Given a Web service environment, the decision-maker will be faced with a variety of similar models, provided by a large set of model providers (suppliers), all of which may serve his/her purpose. In such situations, knowing metainformation about the model captured in the knowledge layers and using a set of metrics defined to evaluate model quality, the decision-maker can make an informed choice.

## Acknowledgements

This research has been sponsored by Boston University School of Management’s Institute for Leading in a Dynamic Economy (BUILDE). We thank Mark Chen and Rajesh Jha for help with the coding.

Appendix A. WSDL file for the spreadsheet model described in Section 4 was generated using Apache AXIS

```xml
<?xml version="1.0" encoding="UTF-8"?>
= <wsdl:definitions targetNamespace="http://168.122.30.172:8080/AXIS/Scenario.jws/AXIS/Scenario.jws"
    xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:apachesoap="http://xml.apache.org/xml-soap"
    xmlns:impl="http://168.122.30.172:8080/AXIS/Scenario.jws/AXIS/Scenario.jws-impl"
    xmlns:intf="http://168.122.30.172:8080/AXIS/Scenario.jws/AXIS/Scenario.jws"
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:message name="getAvgNetIncomeRequest" />
    = <wsdl:message name="getSpreadSheetResultsRequest">
    <wsdl:part name="GrowthRateFor92" type="xsd:double" />
    <wsdl:part name="LeaseFor92" type="xsd:double" />
    <wsdl:part name="SalesFor92" type="xsd:double" />
    <wsdl:part name="GrowthRateFor93" type="xsd:double" />
    <wsdl:part name="LeaseFor93" type="xsd:double" />
    <wsdl:part name="SalesFor93" type="xsd:double" />
    <wsdl:part name="GrowthRateFor94" type="xsd:double" />
    <wsdl:part name="LeaseFor94" type="xsd:double" />
    <wsdl:part name="SalesFor94" type="xsd:double" />
    <wsdl:part name="GrowthRateFor95" type="xsd:double" />
    <wsdl:part name="LeaseFor95" type="xsd:double" />
    <wsdl:part name="SalesFor95" type="xsd:double" />
    <wsdl:part name="GrowthRateFor96" type="xsd:double" />
    <wsdl:part name="LeaseFor96" type="xsd:double" />
    <wsdl:part name="SalesFor96" type="xsd:double" />
    <wsdl:part name="GrowthRateFor97" type="xsd:double" />
    <wsdl:part name="LeaseFor97" type="xsd:double" />
    <wsdl:part name="SalesFor97" type="xsd:double" />
    </wsdl:message>
    <wsdl:message name="getSpreadSheetResultsResponse" />
    = <wsdl:message name="getAvgNetIncomeResponse">
    <wsdl:part name="return" type="xsd:double" />
    </wsdl:message>
    = <wsdl:portType name="Scenario">
    = <wsdl:operation name="getAvgNetIncome">
    <wsdl:input message="intf:getAvgNetIncomeRequest" name="getAvgNetIncomeRequest" />
    <wsdl:output message="intf:getAvgNetIncomeResponse" name="getAvgNetIncomeResponse" />
    </wsdl:operation>
    = <wsdl:operation name="getSpreadSheetResultsParameterOrder="GrowthRateFor92 LeaseFor92 SalesFor92 GrowthRateFor93 LeaseFor93 SalesFor93 GrowthRateFor94 LeaseFor94 SalesFor94 GrowthRateFor95 LeaseFor95 SalesFor95 GrowthRateFor96 LeaseFor96 SalesFor96 GrowthRateFor97 LeaseFor97 SalesFor97">
    <wsdl:input message="intf:getSpreadSheetResultsRequest" name="getSpreadSheetResultsRequest" />
    <wsdl:output message="intf:getSpreadSheetResultsResponse" name="getSpreadSheetResultsResponse" />
    </wsdl:operation>
</wsdl:portType>
= <wsdl:binding name="ScenarioSoapBinding" type="intf:Scenario">
    <wsdl:soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http" />
    = <wsdl:operation name="getAvgNetIncome">
    <wsdl:soap:operation soapAction="" />
    = <wsdl:input name="getAvgNetIncomeRequest">
    <wsdl:soap:body encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    namespace="http://168.122.30.172:8080/AXIS/Scenario.jws/AXIS/Scenario.jws"
    use="encoded" />
```

## Appendix A (continued)

```xml
</wsdl:input>
= <wsdl:output name="getAvgNetIncomeResponse">
    <wsdlsoap:body encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    namespace="http://168.122.30.172:8080/AXIS/Scenario.jms/AXIS/Scenario.jms"
    use="encoded" />
</wsdl:output>
</wsdl:operation>
= <wsdl:operation name="getSpreadSheetResults">
    <wsdlsoap:operation soapAction="" />
= <wsdl:input name="getSpreadSheetResultsRequest">
    <wsdlsoap:body encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    namespace="http://168.122.30.172:8080/AXIS/Scenario.jms/AXIS/Scenario.jms"
    use="encoded" />
</wsdl:input>
= <wsdl:output name="getSpreadSheetResultsResponse">
    <wsdlsoap:body encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    namespace="http://168.122.30.172:8080/AXIS/Scenario.jms/AXIS/Scenario.jms"
    use="encoded" />
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
= <wsdl:service name="ScenarioService">
= <wsdl:port binding="intf:ScenarioSoapBinding" name="Scenario">
    <wsdlsoap:address location="http://168.122.30.172:8080/AXIS/Scenario.jms" />
</wsdl:port>
</wsdl:service>
</wsdl:definitions>
```

## Appendix B. Schema in text form for a revenue model

<table><tr><td>Scenario/e/ Month/e/</td></tr><tr><td>New_Clients/a/{Month} Catg1_Client_R/a/{Scenerio} Catg2_Client_R/a/{Scenerio} Catg3_Client_R/a{Scenerio} Catg1_Clients(New_Clients,(N:1)Catg1_Client_R)/f/{Month} Catg2_Clients(New_Clients,(N:1)Catg2_Client_R)/f/{Month} Catg3_Clients(New_Clients,(N:1)Catg3_Client_R)/f/{Month} Total_catg1_Client(Catg1_Clients)/f/{Month} Total_catg2_Client(Catg2_Clients)/f/{Month} Total_catg3_Client(Catg3_Clients)/f/{Month} Total_New_Clients(Total_catg1_Client,Total_catg2_Client,Total_catg3_Client)/f/{Month}</td></tr><tr><td>Old_Clients/a/{Scenerio}</td></tr><tr><td>BasicPrice_Catg1/a/{Scenerio} BasicPrice_Catg2/a/{Scenerio} BasicPrice_Catg3/a/{Scenerio} DownPayment_Pct/a/{Scenerio} ImplTime_Catg1/a/{Scenerio} ImplTime_Catg2/a/{Scenerio} ImplTime_Catg3/a/{Scenerio} Revenue_Basic((N:1)BasicPrice_Catg1,(N:1)BasicPrice_Cat2,(N:1)BasicPrice_Cat3, Catg1_Clients,Catg2_Clients,Catg3_Clients,(N:1)DownPayment_Pct,(N:1)ImplTime_Catg1,(N:1)ImplTime_Catg2,(N:1)ImplTime_Catg3)/f/{Month}</td></tr><tr><td>Maintfee_catg1/a/{Scenerio} Maintfee_catg2/a/{Scenerio} Maintfee_catg3/a/{Scenerio} Revenue_Maint_old((N:1)Mainfee_catg2,(N:1)Old_Clients)/f/ Revenue_Maintenance((N:1)Maintfee_Catg1,(N:1)Maintfee_Catg2,(N:1)Maintfee_Catg3, Total_Catg1_Client,Total_Catg2_Client,Total_Catg3_Client)/f/{Month} Total_Revenue_Maint(Revenue_Maint_old,Revenue_Maintenance)/f/{Month}</td></tr><tr><td>Adds_catg1/a/{Scenerio}Adds_catg2/a/{Scenerio}Adds_catg3/a/{Scenerio} Revenue_Adds((N:1)BasicPrice_Catg1,(N:1)BasicPrice_Catg2,(N:1)BasicPrice_Catg3,(N:1)ImplTime_Cat g1,(N:1)ImplTime_Catg2,(N:1)ImplTime_Catg3),(N:1)Adds_Catg1,(N:1)Adds_Catg2,(N:1)Adds_Catg3, Total_Catg1_Client,Total_Catg2_Client,Total_Catg3_Client)/f/{Month} Revenue_Adds_Old((N:1)BasicPrice_Catg2,(N:1)Old_Clients,(N:1)Adds_Catg2)/f/ Total_Revenue_Basic&amp;Adds(Revenue_Adds_Old,Revenue_Basic, Revenue_Adds)/f/{Month}</td></tr><tr><td>Total_Revenue(Total_Revenue_Maint,Total_Revenue_Basic&amp;Adds)/f/{Month}</td></tr></table>

Appendix C. Generic structure diagram for the revenue model

![](/api/attachments/PD7ZUX3T/fulltext/images/b4721c94f224b7fd79d23be761d457c0e749cb08b6b0c0604e6741c5c0a439c8.jpg)

## References

[1] R.M. Adler, Distributed coordination models for client/server computing, IEEE Computer 28 (1995) 14– 22.

[2] P. Balasubramanian, G. Shankaranarayanan, Architecting decision support for the digital enterprise—a Web services perspective, Presented at Eight Americas Conference on Information Systems, Dallas, Texas, 2002, pp. 163–169.

[3] P. Balasubramanian, N. Kulatilaka, J. Storck, Managing information technology investments using a real-options approach, Journal of Strategic Information Systems, 2000.

[4] A. Bharadwaj, J. Choobineh, A. Lo, B. Shetty, Model management systems: a survey, Annals of Operation Research 38 (1992) 17 – 67.

[5] H.K. Bhargava, R. Krishnan, S. Roehrig, M. Casey, D. Kaplan, R. Muller, Model management in electronic markets for decision technologies: a software agent approach, Presented at 30th Hawaii International Conference on System Sciences, Hawaii, 1997.

[6] J. Bischop, A. Meeraus, On the development of a general algebraic modeling system in strategic planning environment, Mathematical Programming Study 20 (1982) 1 – 29.

[7] P.P. Chen, The entity – relationship model: toward a unified view of data, ACM Transactions on Database Systems 1 (1976) 9 – 36.

[8] E.F. Codd, Extending the database relational model to capture more meaning, ACM Transactions on Database Systems 4 (1979) 377– 387.

[9] J. Conklin, M. Begeman, gIBIS: a hypertext tool for exploratory policy discussion, ACM Transactions on Office Information Systems 6 (1988) 303– 331.

[10] V. Dhar, M. Jarke, Conceptual modeling and change propagation, in: B. Konsynski (Ed.), Information Systems and Decision Process, IEEE Computer Society Press, Los Alamitos, CA, 1992, pp. 217– 230.

[11] D.R. Dolk, Integrated model management in data warehouse era, European Journal of Operational Research 122 (2000) 199– 218.

[12] R. Elmasri, S.B. Navathe, Fundamentals of Database Systems, Second ed., The Benjamin/Cummings Publishing, Redwood City, CA, 1994.

[13] J. Favela, Capture and dissemination of specialized knowledge in network organizations, Journal of Organizational Computing and Electronic Commerce 7 (1997) 201 – 226.

[14] R. Fourer, D. Gay, B.W. Kernighan, A mathematical programming language, Management Science 36 (1990) 519 – 554.

[15] A.M. Geoffrion, An introduction to structured modeling, Management Sciences 33 (1987) 547 – 588.

[16] S. Graham, S. Simeonov, T. Boubez, D. Davis, G. Daniels, Y. Nakamura, R. Neyama, Building Web Services with Java: Making Sense of XML, SOAP, WSDL and UDDI, Sams, Indianapolis, 2002.

[17] S.-Y. Huh, Q.B. Chung, H.-M. Kim, Collaborative model management in departmental computing, Informs 38 (2000) 373–389.

[18] T. Isakowitz, S. Shocken, H. Lucas, Toward a logical/physical theory of spreadsheet modeling, ACM Transactions on Office Information Systems 13 (1995) 1 – 37.

[19] C.V. Jones, Attributed graphs, graph grammars, and structured modeling, Annals of Operation Research 38 (1992) 281– 324.

[20] R. Krishnan, Model management: survey, future directions and a bibliography, ORSA CSTS Newsletter 14 (1993) 7– 16.

[21] M.M. Kwan, P.R. Balasubramanian, KnowledgeScope: managing knowledge in context, Decision Support Systems 35 (2002) 467 – 486.

[22] M.L. Lenard, Fundamentals of structured modeling, in: G. Mitra (Ed.), Mathematical Models for Decision Support, Springer Verlag, Berlin, 1988, pp. 695– 713.

[23] R. Medina-Mora, T. Winograd, R. Flores, F. Flores, The action workflow approach to workflow management technology, Presented at 4th Conference on CSCW, New York, 1992.

[24] R.R. Panko, J. Richard, P. Halverson, Spreadsheets on trial: a survey of research on spreadsheet risks, Presented at Hawaiian International Conference on System Sciences (HICSS-29), Hawaii, 1996.

[25] R. Plane, How to build spreadsheet models, OR/MS Today, (1997) 50 – 54.

[26] P. Resnick, H.R. Varian, Recommender systems, Communications of the ACM 40 (1997) 56 – 58.

[27] B. Ronen, M.A. Palley, H.C. Lucas, Spreadsheet analysis and design, Communications of the ACM 32 (1984) 84 – 93.

[28] S. Savage, Weighing the pros and cons of decision technology in spreadsheets, OR/MS Today, (1997) 42 – 45.

[29] B. Singh, G.L. Rein, Role Interaction Nets: a Process Description Formalism, MCC Tech, Austin, 1992. CT-083-92.

[30] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice – Hall, Englewood Cliffs, 1982.

[31] E.A. Stohr, B.R. Konsynski, Information Systems and Decision Processes, IEEE Computer Press, CA, 1992.

[32] G.P. Wright, A.R. Chaturvedi, R.V. Mookerjee, S. Garrod, Integrated modeling environment in organizations: an empirical study, Information Systems Research 9 (1997) 64 – 84.

Bala Iyer is an assistant professor of Management Information Systems in the Department of Information Systems, Boston University. Professor Iyer received his PhD from New York University with a minor in Computer Science. His research interests include designing knowledge management systems using concepts from system design, hypertext design, and workflow management, exploring the role of IT architectures in delivering business capabilities, querying complex dynamic systems, hypermedia design, and development, and model management systems. Recently, he has begun to analyze data on the software industry to understand the logic and patterns of emergence of software architecture from two complementary perspectives: (1) the emergent architecture as a network of connections among a set of components (modules) that interoperate across one or more platforms; (2) the emergent architecture is the result of moves and countermoves by different companies supplying these modules and platforms, and as such, the architecture is dynamic and evolving.. He has published papers in the Communications of the ACM, Communications of AIS, Decision Supports Systems, Annals of Operation Research, Journal of the Operational Research Society and in several proceedings of the Hawaii International Conference of Systems Sciences.

Ganesan Shankaranarayanan obtained his PhD in Management Information Systems from the University of Arizona in 1998. His current research areas include schema evolution in databases, heterogenous and distributed databases, data modeling requirements and methods, and structures for and the management of metadata. Specific topics of metadata include metadata implications for data warehouses, metadata management for knowledge manamement systems/architectures, metadata management for data quality, and metadata models for mobile data services. He is a member of the editorial review board for the Journal of Database Management.
