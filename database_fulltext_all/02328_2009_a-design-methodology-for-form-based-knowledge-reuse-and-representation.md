---
otero_id: 2328
otero_key: "CWFGKKRG"
title: "A design methodology for form-based knowledge reuse and representation"
authors: "Jen-Her Wu"
year: "2009"
journal: "Information & Management"
doi: "10.1016/j.im.2009.06.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A design methodology for form-based knowledge reuse and representation

Jen-Her Wu \*

Department of Information Management, National Sun Yat-Sen University, 70 Lien-Hai Road, Kaohsiung 80424, Taiwan

## A R T I C L E I N F O

Article history: Received 27 November 2007 Accepted 15 June 2009 Available online 17 July 2009

Keywords: Design science Knowledge management Form-based knowledge management systems Factoring and synthesis Cognitive fit theory

## A B S T R A C T

Paper forms are regularly used for collecting and disseminating knowledge in offices; they are a natura way of eliciting requirements of knowledge workers. Many organizations have implemented a groupware system to integrate the organizational knowledge and support knowledge creation. However, design methods for flexible form-based knowledge reuse and representation are limited. We developed a methodology based on the enhanced cognitive fit theory; it utilizes factoring and synthesis principles to manipulate form-based knowledge. The methodology was articulated using the design science research methodology. A prototype embedded methodology was built to support a knowledge worker in knowledge creation and reuse in a high tech firm. The resulting system allowed flexible formbased knowledge creation that was useful for problem solving and exploiting opportunities. Implications and conclusions are discussed.

\- 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizational knowledge is an organization’s most valuable strategic asset. In IS, most research on knowledge management assumes that knowledge has positive implications for organizations [13]. Leading management and organizational theorists believe that, to remain competitive, an organization must efficiently and effectively capture, create, locate, and share knowledge in order to apply it to solve problems and exploite opportunities [6].

A form as used in this article is a way of organizing and presenting knowledge. Most organizations use forms to present knowledge and communicate with their affiliates or other organizational entities (such as suppliers). Knowledge captured in forms is generally well structured and thus can easily be captured and formalized. Therefore, they are an important means of designing and developing form-based knowledge management systems (FBKMS). In the fast-changing and competitive environment, meeting the dynamic needs of knowledge workers requires the FBKMS to be flexible in storing, creating, and presenting knowledge; this must, of course, include flexibility in adding new knowledge, modifying it, and changing its layout in existing forms or creating an entirely new one. Traditionally, forms are constructed at the systems analysis and design stage when software is developed. Rewriting system code is necessary when a new form is needed or an old one must be constructed. This is inconvenient and expensive, and it significantly restricts the flexibility of the operation.

One way to overcome this problem is to develop systems that allow knowledge workers to create and modify their forms easily. In other words, knowledge workers should handle some of their own knowledge reporting needs through ad hoc form development without the intervention of computer professionals. This flexibility is particularly useful in developing FBKMS, when new and ad hoc knowledge creation and presentation is essential.

Although report generation is not new, most existing approaches require that the user has knowledge of the database. The role of the system is to organize the specified data into tables. For instance, Lotus Notes provides Framesets (to create a frame), Pages (to link to other web pages), Forms (to link to other forms), Views (to create a form), and other functions that allow the end users to create and manage their one- and two-dimensional forms. It also provides functions for key words and full-text search and is a more sophisticated tool for managing forms and documents. It also allows users to add onto the Crystal Report tool, which provides more sophisticated capabilities, such as allowing creation of sub-reports in a report and manipulation of more complex two-dimensional forms. However, when using more sophisticated functions (e.g., Design View and Crystal Report), end users must be able to define data sources and understand the database schema before they can integrate multiple tables or aggregate the data. This is difficult for users who may not have professional database knowledge. Smolnik and Nastansky [17] suggested a way of integrating topic maps with Lotus Notes for organizing and navigating organization knowledge. However, they did not provide a method.

A perennially interesting research topic in the IS field is how to develop new systems for semi-structured or compound knowledge representation. This requires a methodology for knowledge factoring and synthesis in order to build the relationships among the knowledge stores, retrieve the knowledge, and represent it based on predefined templates. This topic is interesting because as IT develops and technical knowledge grows, IT is applied to new areas that were not previously believed amenable to IT support [3,10]. We follow the design science research guidelines of Hevner et al. [7] and Peffers et al. [12] to develop a methodology for dealing with form-based knowledge storage and representation based on the principles of factoring and synthesis and cognitive fit theory. Our approach embeds more semantic knowledge in the factoring and generalization process to simplify the ad hoc reporting process. This allowed us to simplify knowledge form management.

Our prototype system, KnowledgeManager, used a form-based knowledge presentation capable of providing flexible form-based knowledge creation and presentations; it was implemented as a demonstration of the system’s feasibility and value. It was designed for the knowledge worker when designing a new product.

## 2. The need for form-based knowledge management

Knowledge is an abstract notion that has been the center of epistemological debate in western philosophy since the classical Greek era [2]. It is information that has value because it can be meaningfully organized and accumulated or manipulated through experience, communication, or inference. It has the highest value, the most human contribution, the greatest relevance in making decisions and actions, and the greatest dependence on a specific situation or context [4]. A hallmark of the new economy is the ability of organizations to realize economic value from their knowledge assets as well as their assets of information, production distribution and affiliation [5].

Knowledge can be viewed both as something to be stored and manipulated and as a driver in a process of simultaneously knowing and acting; i.e., applying expertise. As a practical matter, organizations need to manage knowledge both as an object and a process [8]. As an example, we examined the experience of a Chip Resistor and Capacitor manufacturer. This organization has knowledge workers (in particular, Resistor and Capacitor designers) who must consider many factors and alternatives during the design process. There are technical, marketing, and customer issues. Most of the knowledge involved is presented in the forms that they fill out.

To deal with today’s competitive and fast-changing environment, knowledge workers are continuously facing new situations and a need to record and discuss their set of experiences with colleagues throughout their career to make the organization continuously improve its competitive position over time. This means that they need a device to manage knowledge efficiently and effectively and naturally re-use and share parts of it (experience or ‘‘know-how’’) in challenging situations [1,15].

Re-using and sharing knowledge is the basic idea of knowledge management. The reuse of knowledge process involves the following stages: its capture and documentation, its packaging for reuse, its distributing or disseminating and its reuse [9]. This requires a structuring and storage of knowledge in such a way that other people can use it easily as well as reuse it. When investigating ‘‘structuring’’ in the knowledge management realm, knowledge must first be codified and prepared in such a way that it can be shared; i.e., it requires a suitable form of representation. Knowledge must be organized in such a way that it can be found when it is needed: i.e., there is a need for a structure or knowledge base (a knowledge repository) in which knowledge can be stored. The knowledge repositories typically contain a specific type of knowledge for a particular business function or process. Many kinds of repositories are involved in knowledge reuse. Perhaps the most basic distinction is that repositories may contain documents or data. In this paper, we concentrate on form-based knowledge and storing it in a system for knowledge sharing and reuse.

<table><tr><td colspan="8">Market ReportProduct Type: CapacitorDate: 10/15/2004Prepared by:XXXXX</td></tr><tr><td colspan="8">Market Analysis:1. Customer requirements analysis:(1). According to estimation of ASUS &amp; Compal NB requirements,....(2) Requirements of 3C component application....2. Competitive Product Analysis:The competitive products list as follows.</td></tr><tr><td colspan="8">Product Development Plan:Base on Market analysis, The next generation product development strategy of Capacitor will be:(1). The goal of product specification:....(2). The goal of quantity:....(3). The goal of product cost:....</td></tr><tr><td colspan="8">Customer RequirementProduct Type: Capacitor Date:10/01/2004 Prepared by:xxxxxxCustomer:ASUS....Customer Grade:A</td></tr><tr><td colspan="8">Product Required Plan</td></tr><tr><td>No</td><td>Specification</td><td>Unit</td><td colspan="2">Required QTY</td><td>Month</td><td colspan="2">Remark</td></tr><tr><td>1</td><td>0603X105_160</td><td>KPCS</td><td colspan="2">1200</td><td>2005.04</td><td colspan="2"></td></tr><tr><td>2</td><td>0603X105_160</td><td>KPCS</td><td colspan="2">1500</td><td>2005.05</td><td colspan="2"></td></tr><tr><td colspan="8">Conclusion:1. Develop product by advance material, process, technologies, and....2.......</td></tr><tr><td colspan="8">Competitive ProductProduct Type: Capacitor Date: 10/01/2004 Prepared by:xxxxxxVendor: Murata</td></tr><tr><td colspan="8">Product Specification</td></tr><tr><td>No.</td><td>Dielectric</td><td>Size</td><td>Voltage</td><td>Cap.</td><td>Tolerance</td><td>Thickness</td><td>Termination</td></tr><tr><td>1</td><td>X5R</td><td>0402</td><td>6.3V</td><td>105</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2</td><td>X5R</td><td>0402</td><td>10V</td><td>225</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3</td><td>X5R</td><td>0402</td><td>16V</td><td>104</td><td>-</td><td>-</td><td>-</td></tr></table>

Fig. 1. Example of capacitor market report.

A knowledge form can be analyzed by studying its objects and structure. The knowledge object is the basic element. It is an atomic packet of knowledge content that can be labeled, indexed, stored, retrieved, and manipulated. Each has a heading, attributes, and content. The heading is the index or classifier of the object; it will include attributes to describe its domain and values. The content is the body of knowledge of the object. Knowledge objects can also possess a relationship: the knowledge structure provides the relationship between the object and the context for interpreting content.

In Fig. 1, for instance, the capacitor and resistor manufacturer generates a capacitor market report for the ASUS Corporation. This market report is the heading; it has three attributes: product type, date, and prepared by; capacitor or resistor is the value of the product type attribute. The Capacitor Market Report might consist of two major knowledge objects: Capacitor Market Analysis and Capacitor Product Development Plan. Thus, the Capacitor Market Report has an aggregation relationship, as shown in Fig. 2. In addition, generating the Capacitor Market Analysis has a reference relationship with Customer Requirement and Competitive Product.

![](/api/attachments/CWFGKKRG/fulltext/images/014cc7ee279f981c7c21331900cd104f603623a3bb6bc47ccaf0ed6eaee8b179.jpg)  
Fig. 2. Example of knowledge objects and their relationship.

## 3. Theoretical foundation

## 3.1. Factoring and synthesis

To increase knowledge reuse flexibility, a knowledge form can be abstracted at one of three levels:

1. The Object/Instance Level: A knowledge object is an instance of a knowledge template, which is instantiated by adding its content. This is the most common knowledge element to be defined and seen.

2. The Template Level: A knowledge template is the skeleton of a knowledge object, in which content and attribute values has been removed and possibly changed to represent others. The example in Fig. 3 shows a relationship between a knowledge object and its template which may contain headings, fixed texts, operation expressions, graphics, and other attributes that are not stored in the database.

3. The Meta-template Level: This is a further abstraction of templates that provides a capability for generalizing the headings with their associated types. A knowledge metatemplate can therefore be instantiated into multiple knowledge templates that might be mutually joined through a relationship. A template can thus have multiple knowledge objects, as shown in Fig. 3 (adapted from Wu et al. [18]).

Based on different levels of abstraction, knowledge can be manipulated and managed through a factoring and synthesis processes, as shown in Fig. 4. Factoring is a process of aggregation and generalization. It builds knowledge templates and metatemplates from existing knowledge forms. Synthesis is a process of specialization and instantiation. It constructs knowledge instances from knowledge meta-templates or knowledge templates.

The first step in factoring is knowledge analysis, which extracts knowledge objects from knowledge forms and builds their relationships. A structure can be built from the object headings. Knowledge objects are stored and indexed by the heading structure in a database for efficient retrieval. Contents and values in knowledge objects are then removed to build templates (Factoring 1). For instance, in Fig. 4, five capacitor related knowledge objects can be identified: Market Report, Market Analysis, Product Development Plan, Customer Requirement, and Competitive Product. As shown in Fig. 2, the Capacitor Market Report has an aggregation relationship with Capacitor Market Analysis and Capacitor Product Development Plan. In addition, generating the Capacitor Market Analysis has a reference relationship with ASUS— Capacitor Customer Requirement and Compal—Capacitor Competitive Product.

The knowledge templates are next generalized into knowledge meta-templates (Factoring 2). Knowledge meta-template construction is based on the generalization of a set of templates in relationship or type similarities among headings. In Fig. 4, for instance, the knowledge objects can be generalized into five knowledge templates: Market Report, Market Analysis, Product Development Plan, Customer Requirement, and Competitive Product. These have the same relationship as they do at the object level. Furthermore, they and the relationships can be generalized into a meta-template called Market Information.

The synthesis process constructs knowledge objects from metatemplates and/or templates. When form-based knowledge is needed, the knowledge worker chooses the proper meta-template to build template(s) by defining the headings and their attributes. If more than one template is created, their relationships need to be

![](/api/attachments/CWFGKKRG/fulltext/images/adc8b46c7e5b665b7114f5ee39a89d70c22a341f5ba099b7f868ca583a70c97f.jpg)  
Fig. 3. Meta-template, template, object and their relationships.

Knowledge Instance  
![](/api/attachments/CWFGKKRG/fulltext/images/39c16279926e1397320b67dcaf9d1a7defc4b65c25f42d7690890662880c3382.jpg)  
Fig. 4. Factoring and synthesis of knowledge forms.

defined (Synthesis 1). Once the knowledge templates and relationships are built, the FBKMS retrieves knowledge objects from the knowledge base and maps objects into templates based on the template specification (e.g., heading and attributes). A knowledge instance is then constructed (Synthesis 2). The process of creating forms and knowledge artifacts can be performed in a bottom-up or a top-down fashion, i.e. either by building reusable forms from existing artifacts or by designing forms from the start and engineering the documents top-down.

Thus the synthesis process has two stages: knowledge template definition and knowledge object creation. In the knowledge template definition stage, the knowledge worker chooses a knowledge meta-template and then defines heading and attributes to build preliminary knowledge template(s) and their relationships, based on the requirements. The preliminary knowledge templates may need to be further edited to meet the exact knowledge presentation needs, as necessary. In the knowledge object creation stage, a knowledge worker can fill in the needed information based on previously created templates; the FBKMS can then retrieve the knowledge objects from the knowledge base and display the knowledge, as specified.

## 3.2. Cognitive fit theory

Cognitive fit theory considers a problem solution to be the consequence of the relationship between a problem representation and its problem-solving task. Problem solvers work on the information in the problem representation and the task to produce a mental representation (the internal representation of tasks in human working memory). The cognitive processes then manipulate this representation to solve the task. Human beings will select problem-solving processes that are compatible with their mental representations. Accordingly, mental representations and problem-solving processes interact with each other and then they are gradually formed to guide problem solvers to a problem solution.

![](/api/attachments/CWFGKKRG/fulltext/images/b3e64995bd4f9acf537d48a1651a8276a1554facac0cd4b9b0127475f894a0e0.jpg)  
Fig. 5. The Enhanced cognitive fit model.

Sinha and Vessey [16] enhanced the cognitive fit model by regarding the problem-solving tool as a predictor of the problemsolving performance, as shown in Fig. 5. They suggested that a match between the problem-solving task and tool is even more important than a match between a task and the problem representation. Thus, a match between a task and the information provided by problem-solving tool will result in improved problemsolving performance [11]. Shaft and Vessey [14] further found that higher levels of software mental representation and of the problem-solving task were positively associated with problemsolving performance when cognitive fit existed.

Knowledge creation is a human activity, often ill-structured and ad hoc and neglected by IS researchers. Because human beings are regarded as limited information processors, reducing manipulation complexity in the task environment will improve problem solving. The knowledge creation process is dynamic and complex and is best understood as a process of problem definition followed by development and application of knowledge to solve the problem. There has been very little systematic research focused on methodologies for developing and implementing the knowledge creation process in this way.

Because, most organizations use forms to present knowledge and to communicate with their affiliates, etc. in an office environment, based on cognitive fit theory, forms representation and FBKMS are an important way to support knowledge creation by knowledge workers. The perceptual inference pattern of knowledge creation with a knowledge management system (KMS) for knowledge workers is shown in Fig. 6, where the knowledge creation task (problem-solving task) and required relevant knowledge representation (problem representation) use a KMS (problem-solving tool) to determine the knowledge creation performance. Essentially, individuals engaged in knowledge creation are attempting to solve a problem so that a course of action can be recommended, resulting in increased knowledge creation efficiency and effectiveness.

While performing knowledge creation, a knowledge worker constructs a mental representation using an internal cognitive processes selected from a structurally similar problem. The worker then selects a problem-solving process that is compatible to their mental representation. The worker will then be guided through the problem-solving process. When the types of information required by the knowledge creation task and knowledge representation mismatch, workers will no longer be guided in their choice of problem-solving processes. This occurs because an additional data transformation step has become necessary for constructing the mental representation suitable for knowledge creation. In this situation, knowledge creation problem-solving performance deteriorates. When the types of information needed in the knowledge creation task and knowledge creation and required knowledge representation match, knowledge workers use problem-solving processes that also need the same type of information. Consequently, the knowledge creation task will be simpler. Hence, knowledge creation with cognitive fit leads to effective and efficient knowledge creation performance.

![](/api/attachments/CWFGKKRG/fulltext/images/4f177da64e5d5948b3a796b5bf862ca6d989c1d34a86e9c1a0a2effcfbf95510.jpg)  
Fig. 6. General model of knowledge creation with the support of a KMS.

## 4. Design methodology for form-based knowledge reuse and representation

Using cognitive fit theory with factoring and synthesis provides a method for form-based knowledge reuse and representation; it has three major stages: knowledge requirement modeling, knowledge structure modeling, and the application (see Fig. 7). The knowledge requirement modeling stage is the processes of knowledge acquisition and transformation. The knowledge structure modeling stage is the knowledge factoring process; it includes knowledge form analysis and knowledge structure design. Once these stages are completed, the accessible knowledge base and structure are constructed and the system can be applied to construct knowledge forms in the synthesis process.

## 4.1. Knowledge requirement modeling

The objective of this stage is to acquire and model the knowledge worker’s knowledge activities (i.e., the work flow) and its associated knowledge. An activity diagram that involves the use of Unified Modeling Language (UML) is often used in modeling work flow [19]; thus the activity sequence is presented in an activity diagram. The detailed specification and the knowledge needed for each activity must then be further described in the activity specification table, which includes the activity name, activity specification, the knowledge required for the activity and by which provider, plus the knowledge produced in that activity and by the producer. Samples of these are given in Fig. 8.

## 4.2. Knowledge structure modeling

## 4.2.1. Knowledge form analysis

Knowledge form analysis identifies the knowledge objects and their relationships for each activity, based on the knowledge (both required and produced).

![](/api/attachments/CWFGKKRG/fulltext/images/c71acdc5beb725b2474fee0a208607007cf3ef1dac2bc95eb5ddc9f325564e0f.jpg)  
Fig. 7. Design methodology for form-based knowledge reuse and representation.

![](/api/attachments/CWFGKKRG/fulltext/images/c18478c3676f3821deb050629580dc1cd189b6ce96fd637b110e5fdc85038b73.jpg)

<table><tr><td></td><td>1.1 Market Survey</td><td>1.2 New Technology Research</td><td>1.3 New Product Development Planning</td></tr><tr><td>Activity Specification</td><td>Product investigating to find out customer requirements and competitive product analysis in specific market for decision making of new product or technology development.</td><td>Fundamental technology research Planning for new technology development and validation.</td><td>To make Use of information about Market Report or Technical Research Plan to construct the target specification of new product or technology development.</td></tr><tr><td rowspan="2">Knowledge Required/ Provider</td><td>Customer Requirement/Sales Department.</td><td rowspan="2">Technical Research Report; Patent Information / R&amp;D Department.</td><td>Market Report / Marketing Dep.</td></tr><tr><td>Competitive Product Analysis / R&amp;D Department.</td><td>Technical Research Plan / R&amp;D Department.</td></tr><tr><td>Knowledge Produced / Producer</td><td>Market Report / Marketing Department.</td><td>Technical Research Plan / R&amp;D Department.</td><td>Product Development Plan / R&amp;D Department.</td></tr></table>

Fig. 8. Activity diagram and activity specification.

The process of knowledge form analysis is recursive:

## Begin

For each knowledge form

Do

Identify knowledge objects (Include heading, attributes, contents, etc.)

Analyze the relationships among the objects

Fill object glossary

Until all knowledge forms are examined

End of knowledge form analysis

To define the procedures, knowledge forms are first analyzed to identify knowledge obiects, attributes and relationships. We used the knowledge form in Fig. 1 as an example. It has five knowledge objects; each has a heading, attributes, and knowledge contents. Each heading has a name and a set of attributes. For instance, Capacitor Market Report has the attributes of product type, date, and producer.

The process of identifying knowledge objects is recursive. The knowledge objects describing the same concept should be aggregated into one group with aggregation (i.e., a whole-part relationship). For instance, the Capacitor Market Report consists of Capacitor Market Analysis and Capacitor Product Development Plan. Thus, this Report has an aggregation relationship. In addition, generating the Capacitor Market Analysis needs to refer to the knowledge of Capacitor Customer Requirement, and/or Capacitor Competitive Product. Thus, the Capacitor Market Analysis has a reference relationship with them. These relationships are shown in Fig. 9.

To describe the resulting information, an object glossary must be built. It includes object name, heading, attributes, relationship, and associated objects, as shown in Table 1. This information provides a clear understanding of the meaning and structure of each object in an application.

![](/api/attachments/CWFGKKRG/fulltext/images/afb9c0936e57cb260d29f7b9909951aef25f21889f1b7e1b06a6f1651f4e97ef.jpg)  
Fig. 9. Knowledge objects and relationship of Capacitor Market Report.

Table 1  
Object glossary of Fig. 1.

<table><tr><td>Object Name</td><td>Heading</td><td>Attributes</td><td>Relationship</td><td>Associated Objects</td></tr><tr><td>Capacitor Market Report</td><td>Market Report</td><td>Product Type, Date, Producer</td><td>Aggregation Aggregation</td><td>Capacitor Product Development Plan Capacitor Market Analysis</td></tr><tr><td>Capacitor Product Development Plan</td><td>Product Development Plan</td><td>Product Type, Date, Producer</td><td>Aggregation</td><td>Capacitor Market Report</td></tr><tr><td>Capacitor Market Analysis</td><td>Market Analysis</td><td>Product Type, Date, Producer</td><td>Aggregation Reference Reference</td><td>Capacitor Market Report Capacitor Customer Requirements Capacitor Competitive Product</td></tr><tr><td>Capacitor Customer Requirements</td><td>Customer Requirements</td><td>Product Type, Date, Producer, Customer Name, Customer Grade</td><td>Reference</td><td>Capacitor Market Analysis</td></tr><tr><td>Capacitor Competitive Product</td><td>Competitive Product</td><td>Product Type, Date, Producer, Vendor, Model, Price</td><td>Reference</td><td>Capacitor Market Analysis</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

## 4.2.2. Knowledge structure design

Normally, a system has more than one knowledge form. Therefore, object glossaries obtained from different knowledge forms must be integrated to derive a complete object glossary and build a relationship structure. During the integration process, restructuring may be needed; attention must also be paid to handling naming conflicts and redundancies in the knowledge objects and their attributes.

Once this is completed, the knowledge objects can be abstracted into a template and the set of templates might then be further generalized for a meta-template. The knowledge structure design procedure is therefore:

## Knowledge structure design

## Begin

Merge the object glossary and resolve conflicts

Generalize the object into template

Initialize a template group

For each template Do

If the template can be classified into one of the template groups

Then add it to the template group and construct the relationship among the templates

Else build a distinct template group

Until all templates are examined

Each template group can then be further generalized into a meta-template

## End of object structure design

![](/api/attachments/CWFGKKRG/fulltext/images/d883d065aad80db851089c5fe763e0601017b5c972791bbd71cf262609556b20.jpg)  
Fig. 10. Sample of the template and meta-template.

In constructing a knowledge structure, aggregation, generalization, and user defined relations are used to identify the object relationships within each template group. Aggregation allows several objects of a different nature to be combined into a higherlevel concept; a template or meta-template. A reference relationship is user defined; it shows that creating one object may use the knowledge from another. Fig. 9 has an example of aggregation and reference relationships.

Generalization allows several concepts of a similar nature to be merged into a higher-level concept; for instance, Capacitor Market Analysis, ASUS—Capacitor Customer Requirement, and Compal— Capacitor Competitive Product can be generalized into templates called Market Analysis, Customer Requirement, and Competitive Product, respectively (see Fig. 10). These can be further generalized into a higher-level concept: a meta-template called Market Information.

One way to maximize flexibility during form construction is to decompose and store the knowledge in a form at the elementary level. To accomplish this, knowledge objects can be indexed by the object structures, as shown in Fig. 11; e.g., in our prototype implementation, there are three meta-templates: Market information, Research information and Proposal information. Each meta level has a corresponding template level; e.g., the Market information consists of Market Report, Market Analysis, Product Development Plan, Customer Requirement, and Competitive Product. Similarly, each template level can have several objects or instances; e.g.,

Customer Requirement can have ASUS—Capacitor Customer Requirement and Compal—Capacitor Customer Requirement, etc.

## 4.3. Application

The major function of the application phase is to construct knowledge forms (objects or instances) from knowledge metatemplates and/or templates. To allow knowledge workers to create their own forms easily, it is necessary to automate the process. The automatic knowledge form construction is:

(1). Knowledge template construction

(1.1). Select a suitable knowledge meta-template to create templates

(1.2). Specify the headings, attributes and relationships

(2). Knowledge form display

Map the resulting objects into the template and perform necessary operations, as specified in the template

In our implementation, knowledge workers must determine what knowledge form or object they need in order to choose a suitable meta-template in the knowledge template construction phase and then specify the headings, attributes, and relationships. Once this phase is completed, the knowledge workers can request a knowledge form display, where the system automatically constructs the template, retrieves the knowledge objects, and maps the resulting knowledge objects to the knowledge template. The resulting knowledge form can then be either viewed on the screen or printed to support the knowledge management activity.

![](/api/attachments/CWFGKKRG/fulltext/images/4117262a7a493f3110463d61530d356decf54ba846759f22f656c6224f46d750.jpg)  
Fig. 11. Sample of meta-template, template, object and their relationships.

![](/api/attachments/CWFGKKRG/fulltext/images/0f29d689f2efe2f55e5881d87655d11075d54fb7820d329ddb3a32f11d1d7e85.jpg)  
Fig. 12. The scenario of Market Report creation.

## 5. A prototype and case study evaluation

To demonstrate the feasibility of the proposed methodology, a prototype system, called KnowledgeManager, was developed. We evaluated the prototype through observational methods to illustrate its utility and application. It was implemented using MatrixOne’s PDM, called eMatrix, and Oracle’s DBMS. To illustrate how the knowledge worker applies the system to support knowledge management activities (such as creating knowledge forms); an example using Capacitor market report was implemented. In our prototype implementation, there are three metatemplates: Market information, Research information, and Proposal information. Each meta level has its equivalent template level; e.g., the Market information is composed of Market Report, Market Analysis, Product Development Plan, Customer Requirement, and Competitive Product templates. Similarly, each template level can have several objects or instances; e.g., Customer Requirement can have ASUS—Capacitor Customer Requirement and Compal—Capacitor Customer Requirement instances, etc.

If the knowledge worker is about to develop a product design plan for Capacitor, the knowledge worker needs to reuse knowledge involving competitive products (from the R&D Department) and customer requirements (from the Marketing Department) to analyze the market situation and create a Capacitor Market Report (see Fig. 12).

![](/api/attachments/CWFGKKRG/fulltext/images/1edd2300f993ed82aadd26dab10ad9e7f4bcd8bee51ce4ce1048e2e39545c0e9.jpg)  
Fig. 13. Knowledge support the product feature specification.

Primary Customer (ASUS and Askey)

![](/api/attachments/CWFGKKRG/fulltext/images/cf92709b4e4a03aaeb7e0de27e25eef9f79eea8263a39663f2b6deb6ff281468.jpg)  
Fig. 14. Knowledge supports the product function specification.

To do this, the knowledge worker may choose the metatemplate, Market Information at the start. Once the meta-template has been chosen, the KnowledgeManager allows the knowledge worker to specify the needed attributes and work on the knowledge contents to create the Capacitor Market Report. During the design process, the knowledge worker can refer to the existing competitive product knowledge by selecting the Competitive Product template and filling in the needed attributes to retrieve knowledge about the primary competitor’s products, such as Murata and TDK. This provides a good basis for determining the best set of product features, such as the Capacitance and Voltage values, etc. Thus, the new product’s features should be better than those of the competitors’ product (see Fig. 13).

The knowledge worker can then retrieve the existing Capacitor Customer Requirement, such as those from ASUS or Compal, as a basis for determining the new product’s functions and production quantity (see Fig. 14). For instance, the new product’s functions (e.g., range of the required values) can be optimized to fit more customers. This design can increase the production quantity and reduce the production cost.

Once this process is completed, the new Capacitor Market Report is generated. The knowledge worker reuses the existing knowledge: Customer Requirement and Competitive Product to support the new product planning decision and consequently generate knowledge for new product design specifications. The knowledge worker can send the knowledge objects to the editing area for possible refinement, as necessary. As an example, the knowledge workers may polish the format of the preliminary templates or objects and save them in the KnowledgeManager for further knowledge sharing.

## 6. Conclusions

The analysis process and proposed artifact were evaluated with respect to the motivating problems discussed in the introduction.

Our results showed that the process and artifact allowed knowledge workers to analyze and design knowledge activities and their associated form-based knowledge. Once completed, the accessible knowledge base and structure can be constructed and the system can be applied to construct knowledge forms in the synthesis process to support knowledge creation.

We have presented a design methodology for form-based knowledge reuse and representation based on factoring and synthesis principles and cognitive fit theory. A prototype FBKMS based on the cognitive fit theory was built to support a knowledge worker’s knowledge creation for a high tech firm. It allowed us to simplify knowledge form management and facilitate knowledge creation. Our analysis and discussion showed us that the analysis process and proposed artifact have the potential to benefit organizations that have already adopted or are planning to adopt FBKMS. The contribution is three-fold:

\- First, the methodology can alleviate the difficulty in knowledge reuse and representation. It integrates several concepts and methods into the design process and artifact and provides better fit on mental representation that allows knowledge workers to create their own knowledge forms and facilitate the knowledge creation.

\- Second, the method allows a skeleton of the knowledge form and its associated knowledge objects to be managed separately. This provides flexibility for knowledge reuse and representation and helps the construction of form-based KMS to be effective in using existing knowledge. The knowledge worker may specify different templates and fill them with knowledge object in the knowledge base.

\- Finally, we developed a general model for knowledge creation and design methodology for form-based knowledge reuse and representation and a KMS prototype embedded in the methodology to support form-based knowledge generation. This makes it different from existing methods and it can improve the capabilities of ad hoc support in KMS.

## Acknowledgements

The author thanks Mr. Yingya Lu (Manager, ASE Group) for his effort in the early draft of this manuscript. The author also thanks to Mr. Mike Pan (Manager, ASE Group), Mr. Frank Chien and Mr. Steven Huang (Walsin Technology Corporation), Mr. Michael Chen (IBM, Certified Lotus Professional). Without their cooperation and full support, this investigation could not have been undertaken. This research was supported by the National Science Council of Taiwan under grant #NSC 96-2416-H-110-012-MY3 and was partially supported by Aim for the Top University Plan of National Sun Yat-Sen University and the Ministry of Education, Taiwan.

## References

[1] A.E. Akgu¨ n, J. Byrne, H. Keskin, G.S. Lynn, S.Z. Imamoglu, Knowledge networks in new product development projects: a transitive memory perspective, Information & Management 42 (8), 2005, pp. 1105–1120.

[2] M. Alavi, D.E. Leidner, Knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1), 2001, pp. 107–136.

[3] F. D’Aubeterre, R. Singh, L. Iyer, A semantic approach to secure collaborative interorganizational eBusiness processes (SSCIOBP), Journal of the Association for Information Systems 9 (3/4), 2008, pp. 231–266.

[4] M. Earl, Knowledge management strategies: toward a taxonomy, Journal of Management Information Systems 18 (1), 2001, pp. 215–232.

[5] A.H. Gold, A. Malhotra, A.H. Segars, Knowledge management: an organization capabilities perspective, Journal of Management Information Systems 18 (1), 2001, pp. 185–214.

[6] V. Grover, T.H. Davenport, General perspectives on knowledge management: fostering a research agenda, Journal of Management Information Systems 18 (1), 2001, pp. 5–22.

[7] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science research in information systems, MIS Quarterly 28 (1), 2004, pp. 75–105.

[8] C.W. Holsapple, K.D. Joshi, Knowledge manipulation activities: results of a Delphi study, Information & Management 39 (6), 2002, pp. 477–490

[9] M.L. Markus, Toward a theory of knowledge reuse: types of knowledge reuse situations and factors in reuse success, Journal of Management Information Systems 18 (1), 2001, pp. 57–94.

[10] M.L. Markus, A. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 26 (3), 2002, pp. 179–212.

[11] D. Nevo, Y.E. Chan, A Delphi study of knowledge management systems: scope and requirements, Information & Management 44 (6), 2007, pp. 583–597.

[12] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, Journal of Management Information Systems 24 (3), 2007, pp. 45–77.

[13] U. Schultze, D.E. Leidner, Studying knowledge management in information systems research: discourses and theoretical assumptions, MIS Quarterly 26 (3), 2002, pp. 213–242.

[14] T.M. Shaft, I. Vessey, The role of cognitive fit in the relationship between software comprehension and modification, MIS Quarterly 30 (1), 2006, pp. 29–55.

[15] K. Sherif, B. Xing, Adaptive processes for knowledge creation in complex systems: the case of a global it consulting firm, Information & Management 43 (4), 2006, pp 530–540.

[16] A.P. Sinha, I. Vessey, Cognitive fit: an empirical study of recursion and iteration IEEE Transactions on Software Engineering 18 (5), 1992, pp. 368–379.

[17] S. Smolnik, L. Nastansky, K-Discovery: using topic maps to identify distributed knowledge structures in groupware-based organizational memories, in: Proceedings of the 35th Hawaii International Conference on System Science, 2002.

[18] J.-H. Wu, H.-S. Doong, C.-C. Lee, T.-C. Hsia, T.-P. Liang, A methodology for designing form-based decision support systems, Decision Support Systems 36 (3), 2004, pp. 313–335.

[19] J.-H. Wu, S.-S. Shin, M.S.H. Heng, A methodology for ERP misfits analysis, Information & Management 44 (8), 2007, pp. 666–680.

![](/api/attachments/CWFGKKRG/fulltext/images/da557306d8cc051c482928a130d66a8d828a6d44ee50de1483628860b5e68210.jpg)

Jen-Her Wu is Professor of Information Management at National Sun Yat-Sen University. He has published three books (Information & Management, System Analysis and Design, Object-oriented Systems Analysi and Design) and over 60 papers in professional journals such as Information & Management, Decision Support Systems, Computers in Human Behavior, and others. His current research interests include infor mation systems development and management, human computer interaction, electronic commerce and innovation and knowledge management. He also serves as an associate editor of Computers in Human Behavior and on the editorial board of Information & Management.
