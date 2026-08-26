---
otero_id: 11482
otero_key: "BTJ5J55G"
title: "From requirements to implementations: a model-driven approach for web development"
authors: "Susana Montero; Paloma Díaz; Ignacio Aedo"
year: "2007"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000689"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# From requirements to implementations: a model-driven approach for web development

Susana Montero, Paloma Dı´az and Ignacio Aedo

Laboratorio DEI., Dpto. de Informa´tica, Escuela Polite´cnica Superior, Universidad Carlos III de Madrid, Av. Universidad 30, Madrid, Spain

Correspondence: Susana Montero, DEI Laboratory, Computer Science Department, Escuela Polite´cnica Superior, Universidad Carlos III, Av. Universidad 30, Legane´s, Madrid 28911, Spain. Tel: þ 34 91 624 9499; E-mail: smontero@inf.uc3m.es

## Abstract

Model-Driven Development (MDD) is an appropriate paradigm for web development since interoperability and flexibility are required to cope with implementation technologies and functionalities that are in permanent evolution. In this paper, we describe and illustrate the MDD process of the ADM (Ariadne Development Method) hypermedia/web engineering method. The two cornerstones of the ADM are the Labyrinth þ þ meta-meta-model, which formalizes the core constructs used within all the design meta-models, and the meta-meta-model specification as an ontology that provides semantics and reasoning not only for model transformations but also for consistency checking and model validation. These features have been essential in the development of a CASE tool, called AriadneTool that supports the different abstract levels of modeling, model transformations as well as the generation of light prototypes in different web implementation technologies. European Journal of Information Systems (2007) ${ \bf 1 6 , }$ 407–419. doi:10.1057/palgrave.ejis.3000689

Keywords: web engineering; model-driven development; meta-models; model transformations; light prototypes

## The importance of an MDD approach in WIS engineering

Nowadays, Web Information Systems (WIS) are full-fledged, complex software systems whose characteristics and new usage scenarios lead to a myriad of problems. The core requirements for this kind of systems include large amounts of information organized in a web structure that can be freely browsed by users selecting links (Isakowitz et al., 1998).WIS usually integrate new or existing processes or systems within a single interactive interface and have a large number of heterogeneous end-users, holding different access rights and using different kinds of devices, that implies specific requirements on usability and security. As a consequence, WIS need a solid approach for the conceptual structuring of the information space and its access as well as for engineering and implementing the required access services.

Furthermore, the development of WIS is strongly influenced by several facts including (Kappel et al., 2006): web technologies are immature and inhomogeneous; there is a need for fast and effective developments due to the continuous change of requirements and the extremely competitive time-to-market pressure; and, finally, development teams are multidisciplinary since knowledge and expertise from different areas (software engineering, hypermedia engineering or usability engineering) are required. Therefore, aspects like interoperability, portability, integration, reuse and flexibility are crucial.

The Model-Driven Development (MDD) paradigm is becoming quite popular thanks to the efforts of the OMG group (OMG, 2003) and, particularly, to the MDA proposal (Model-Driven Architecture) for object-oriented development (ORMSC, 2001). This paradigm aims to move the development effort from implementation toward the creation of models based on a meta-model from which code can be generated automatically or semi-automatically. The basic goal is to provide more powerful tools to define abstract specifications in terms of components and services that belong to the domain of application. Moreover, since the meta-modeling level provides a formal specification of the system that is comprehensive, consistent, unambiguous, and platform-independent, different kinds of model transformations (Caplat & Sourrouille, 2003) can be applied not only to generate code but also to support portability and interoperability or the automatic validation and verification of requirements.

The MDD development paradigm turns out to be most appropriate in the case of WIS. Since web implementation technologies as well as the functionalities offered to the users are in permanent evolution, WIS interoperability and flexibility are inescapable requirements for which the MDD framework provides smart solutions that are not dramatically affected by changes in technology. Moreover, due to short development cycles and the complexity of WIS, it is recommended to use software tools that support not only the modeling itself but also automatic code generation and model consistency check.

In this paper, we describe the MDD process of the Ariadne Development Method (ADM). The ADM proposes a number of meta-models that are used to design, at different levels of abstraction, the structure, navigation capabilities, interactive behaviors, functional requirements, multimedia presentations, and access policies of WIS. The ADM was originally envisaged as an MDD approach, where design meta-models are based on a hypermedia/web meta-meta-model called Labyrinth þ þ . Moreover, the ontological representation of this metameta-model is used to validate a number of syntactical and semantical rules. A software tool called AriadneTool supports the automatic generation of light prototypes in different web implementation technologies, including HTML, SMIL, and RDF.

The remaining of this paper is organized as follows. First, we review the literature on MDD approaches for Web Engineering. The next section focuses on the MDD approach underlying the ADM. Then, there is an example that illustrates how protoypes are generated from requirements applying a number of transformations between meta-models expressed at different abstraction levels. The paper ends discussing the main contributions of our proposal and summarizing some conclusions and ongoing works.

## Review of literature

Several methodologies have been proposed in order to cope with the increasing number of requirements for WIS, not always taking the Web meta-models into account. Next we distinguish some web engineering methods that follow an MDD approach, using models to specify the different aspects involved in the WIS design, and software tools to support transformations between model abstraction levels and generation of code. In section ‘Discussion and lessons learnt’ we will provide a comparison with the ADM proposal.

\- OOHDM (Schwabe & Rossi, 1998) proposes five different steps: Requirements Gathering, Conceptual Design, Navigational Design, Abstract Interface Design, and Implementation. This method has evolved to SHDM that includes the specification of a metamodel together with formalisms and primitives introduced by the Semantic Web (Nunes & Schwabe, 2006).

\- UWE (Hennicker & Koch, 2000) comprises an UML Profile for modeling Web systems, a process and tool support. It follows the MDA principles and uses the OMG standards, in particular QVT for the specification of transformation rules between models. The transformation specification is supported by meta-models,Web Requirements Engineering meta-model (WebRE), the UWE meta-model, and the meta-model of the Web Software Architecture approach (WebSA) containing elements for modeling requirements, structure and behavior, and the architecture of Web systems, respectively (Koch, 2006).

\- OO-H (Go´mez et al., 2001) uses well-known UMLcompliant diagrams to represent the required conceptual information in four models: the Object Model, the Dynamic Model, the Functional Model, and the Navigational Model. It supports a transformationbased construction of a presentation model based on modeling elements of the navigation model and code generation based on the conceptual, navigation and presentation models. The VisualWADE tool offers support for all steps of the development process, including automatic generation of prototypes.

\- WebML (Ceri et al., 2003) is a visual language for specifying the content structure of Web applications and the organization and presentation of contents in one or more hypertexts. The modeling elements of WebML are mapped to architecture components of MVC2, which can be transformed into components for different platforms. The use of WebML is supported by a tool called WebRatio that assists the production of the conceptual models and automates code generation.

## A model-driven approach for web development

ADM is a web engineering method that proposes a systematic yet flexible process to design and evaluate hypermedia and web systems (Dı´az et al., 2005). From a modeling perspective, and compared to similar web engineering methods, its most relevant contributions are its support for the specification of complex multimedia pages, functional requirements, complex user structures and security policies. In fact, the method is particularly useful in large-scale web systems involving different kinds of users who hold different access permissions. From a software engineering perspective, there are four features of the ADM that stress its utility as a web development tool:

![](/api/attachments/BTJ5J55G/fulltext/images/e43e83c172c95f3a6aba188a4c42faf992ae24ffdf57a1fe369adfc3f91e7383.jpg)  
Figure 1 Meta-modeling architecture of the ADM web engineering approach.

\- It establishes a systematic process where all the phases are decomposed in activities that generate a number of mandatory or optional design artifacts, so that developers get disciplined and aware of the different tasks that have to be performed.

\- It relies on a flexible process that implements the star life cycle (Preece, 1994) and, therefore, the sequence among development phases is shaped according to the project needs and requirements.

\- It proposes an integrative or holistic process since there are design models that deal with the different design views of a WIS (including information structure, navigation capabilities, system function, interactive behaviors, presentation features and access control).

\- It is a platform-independent method since, as it will be described on this paper, it is based on an MDD approach and models are then defined in terms of elements of the domain of application instead of using web implementation units.

In this paper, we will focus on the MDD approach underlying the ADM method that makes possible to generate conceptual models from requirements; modify, create, and validate conceptual and detailed models; and transform detailed models into system prototypes in different web implementation technologies. More information and a thorough discussion on the ADM method and its application to real developments can be found in Montero et al. (2004a) and Dı´az et al. (2005).

The MDD approach of ADM is based on the use of models as the primary development tool. Such models can be managed in an efficient way by web engineers and even discussed with stakeholders since they express solutions in terms of the domain of the application instead of using implementation units. Figure 1 shows the modeling architecture of our proposal that is an instance for the web domain of the classical OMG four-layer architecture.

Next subsections go deeper into the meta-modeling layers of our proposal.

## The M3 meta-meta-modeling layer: Labyrinth þ þ

The ADM web engineering method was conceived as an MDD approach with the primary goal of achieving interoperability among different implementation platforms, a most relevant challenge in an environment like the web where technology is in permanent evolution. Indeed, the first step was the definition of a platformindependent reference meta-meta-model, called Labyrinth þ þ (Dı´az et al., 1997; Aedo et al., 2003), that offers constructs to specify all the components of any hypermedia/web system (such as nodes, contents, links, anchors, groups, users, attributes or events), the relationships among the different components (such as composition, access control, location or time- and space-based constraints) and the operations that can be performed on each component (such as create a new link, add a content to a node, or synchronize a number of multimedia items). The main contributions of Labyrinth þ þ can be summarized as follows (Dı´az et al., 1997, 2001): it supports complex composition mechanisms both for information entities and users; it offers constructs to specify dynamic multimedia presentations involving space- and timebased relationships; it makes possible the definition of different kinds of links, including n-ary or dynamic ones; and it includes constructs to specify access policies by means of a role-based access model (Aedo et al., 2003).

The Labyrinth þ þ meta-meta-model is formally defined as an ontology to provide formal support for models integration, validation, and transformation.

## The M2 meta-modeling layer: the ADM meta-models

A step further in the meta-modeling framework is represented by the different ADM design meta-models (see Table 1) that are abstractions of the Labyrinth þ þ components. Thus, while the M2 layer offers design meta-models that are closer to the web developers’ perspective, and in some cases to the stakeholders, the M3 layer guarantees a formal support for validation and other kinds of model transformation, like code generation.

Table 1 ADM design meta-models

<table><tr><td colspan="2">Conceptual design</td></tr><tr><td>Meta-models</td><td>Design concern</td></tr><tr><td>Structural Diagram</td><td>Information entities (composite and simple nodes) and its structure</td></tr><tr><td>Navigation Diagram</td><td>Navigation paths and tools</td></tr><tr><td>Functional Specifications</td><td>Additional services not necessarily related with navigation</td></tr><tr><td>Internal Diagrams</td><td>Nodes and contents&#x27; structure and appearance</td></tr><tr><td>Attributes Catalogue</td><td>Properties and metadata</td></tr><tr><td>Events Catalogue</td><td>Interactive behaviors</td></tr><tr><td>Users Diagram</td><td>Kinds of users (roles and teams)</td></tr><tr><td>Authorization Rules</td><td>Authorized functions for roles and teams</td></tr><tr><td>Categorization Catalogue</td><td>Kinds of objects</td></tr><tr><td colspan="2">Detailed design</td></tr><tr><td>Instances Diagram</td><td>Concrete nodes</td></tr><tr><td>Instanced Users Diagram</td><td>Concrete roles and teams</td></tr><tr><td>Specification of Access Structures</td><td>Detailed specification of dynamic/adaptive navigation paths and tools</td></tr><tr><td>Detailed Specification of Functions</td><td>Full specification of additional services</td></tr><tr><td>Detailed Internal Diagrams</td><td>Appearance and structure of concrete nodes and contents</td></tr><tr><td>Users Allocation</td><td>Assignment of specific users to specific roles</td></tr><tr><td>Access Table</td><td>Concrete access rights for each concrete node and content</td></tr><tr><td>Presentation Specifications</td><td>Presentation features of each concrete node and content</td></tr></table>

The ADM embraces six design perspectives (Structure, Navigation, Interaction, Processes, Presentation, and Access) from two abstraction levels: Conceptual Design and Detailed Design. Furthermore, it includes an Evaluation phase, outside of the scope of this paper, that relies upon the use of prototypes and design models to assess the system usability in terms of a set of well-defined evaluation criteria.

Apart from the meta-models summarized in Table 1, the method also includes a number of inter- and intravalidation rules to check the design completeness, consistency, and integrity. Intra-validation rules check conformance with respect to the ADM syntactical rules (e.g., in generalization or aggregation relationships, composite nodes should be the source of the relation). Inter-validation rules ensure that each entity is fully and correctly described by means of cross-references among related products (e.g., for each node in the Conceptual Design, there is a set of Presentation Specifications defined during the Detailed Design).

In order to help less-experienced or casual web developers to adopt right solutions considering all the different perspectives involved in WIS development, we have integrated existing design knowledge gathered in several collections of design patterns (van Duyne et al., 2002; Rossi et al., 2001; Ferna´ndez & Pan, 2001). The first step to be able to automatically produce conceptual models from design patterns was to count on a formal meta-model to express patterns in a unambiguous a machine-understandable way for which we adopted the three-layered ontology described in Montero et al. (2004b).

## The M1 modeling layer: WIS models and design patterns

At this level, developers create instances of the ADM meta-models that gather the features of their WIS, for which they can use AriadneTool (Montero et al., 2004a; Dı´az et al., 2005), a toolkit automating many of the web design tasks, such as creating design models, checking the correctness and integrity of the design, producing documentation about the project, and generating prototypes in HTML, XML, SMIL, and RDF. Figure 2 shows the toolkit architecture. Thanks to the ontological definition of Labyrinth þ þ , the toolkit includes a number of validation rules that check the completeness, consistency, and correctness of these models, so that design models comply with the semantics defined at each ADM meta-model.

Since patterns are presented like rules that guide the transformation between a given problem and a solution, a correspondence between conceptual problems and modeling solutions can be established. In our famework, designers can link their requirements with design patterns and automatically obtain a first version of conceptual models that reuses expert knowledge. Such design patterns are concrete instances of the designpattern meta-model of layer M2 and make up a pattern language with 34 patterns collected from the literature. Patterns are organized according to their design concern, which is the nature of the problem they solve. Design concerns include:

![](/api/attachments/BTJ5J55G/fulltext/images/4a443bf815d48306c680e88da7938cc8aaa3e7bd4fe0650897a81493c9773153.jpg)  
Figure 2 AriadneTool architecture.

\- structure (e.g. the Task-based Organization pattern (van Duyne et al., 2002)),

\- navigation (e.g. the Location Bread Crumbs pattern (van Duyne et al., 2002)),

\- presentation (e.g. the Navigation Bar pattern (van Duyne et al., 2002)),

\- interaction (e.g. the Action Buttons pattern (van Duyne et al., 2002)),

\- personalization (e.g. the Content Personalization pattern (Rossi et al., 2001)) and

\- security (e.g. the Authorization pattern (Ferna´ndez & Pan, 2001)).

In the next section, we will introduce the ARCE project to show how light prototypes are generated from requirements applying a number of transformations between the modeling layers explained in this section.

## The ARCE project: a running example

ARCE is a web-based system oriented toward enhancing the management of multinational disaster response within the scope of the Latin-American Association of

Governmental Organisms of Civil Defense and Protection. The system provides mechanisms to notify an emergency, to ask for resources, and to offer assistance in order to orchestrate an integrated and efficient response. In order to help to illustrate how AriadneTool allows designers to produce models of the application and generate code for a target platform by means of model transformations, we have selected some representative requirements of the ARCE project to act as a running example:

\- R1. In routine situation, countries can publish news and exchange Internet messages.

\- R2. In an emergency situation, the country or countries affected can make an initial report of the situation and ask for resources, whereas other members can offer and consult the requested resources.

\- R3. Both routine and emergence functionalities have to be easily accessible.

## A pattern-based approach for the transformation of requirements into models

The MDD approach of ADM starts creating platformindependent models. It is very hard to derive puporseful models from a set of requirements usually expressed in natural language. Moreover, during this transformation, designers have to take critical decisions which may be sometimes inadequate leading to a mismatch between requirements analysis and conceptual design. To overcome these issues, we propose to reuse knowledge; in particular, to use the proven experiences collected in hypermedia and web design patterns.

![](/api/attachments/BTJ5J55G/fulltext/images/4bea8a136e154e5def7a3ccaf4f0b3bf2aa22404dc29ba9d60aeea0edcda0846.jpg)  
Figure 3 The transformation from requirements to models.

AriadneTool includes a pattern wizard devoted to generating conceptual models from a set of requirements using design patterns. Patterns have been formalized using an ontological framework for domain-specific pattern representation (Montero et al., 2004b).

The wizard starts gathering requirements through the Volere Requirements Specification Template (Robertson & Robertson, 2006). In the requirement template, a new field has been added so that the designer can select the pattern that best fits the requirement from the pattern language that is available on a semantic web repository (Hypatterns, 2006) that containts the pattern descriptions. Let us take one of the ARCE’s functional requirements to illustrate this process: ‘R1. During a routine situation, countries can publish news and exchange messages’. At this first step, an inspection of the Taskbased Organization pattern (van Duyne et al., 2002), included in our repository, shows that it contributes to organize a set of related tasks in a quick and easy way. In this case, we need to capture the routine tasks in a model.

This pattern helps to accomplish this goal in a twofold way. First, the solution of the pattern shows how to describe the requirement as a set of design entities. Second, this pattern has been classified as a pattern that deals with structural design problems; therefore, the result of such transformation will be placed at a Structural Diagram. Figure 3 depicts the transformations made by the pattern wizard:

(1) The Task-based Organization pattern solution is described as a composite aggregation component that represents a set of the tasks. This code is part of the pattern language that has been defined using the OWL and RDF languages, both W3C recommendations (W3C, 2004a, b).

(2) From this template, the requirement has been represented as the task Routine, which is an aggregation of the task Publish\_news and the task Exchange\_ messages.

(3) Finally, all these elements have been represented as design entities in the Structural Diagram of ADM, which describes that the nodes Publish\_news and Exchange\_messages will be the web pages in charge of performing these tasks, and both tasks can be accessed through the composite node Routine. Later, during modeling refinement, this last node can be turned into a navigation tool in order to provide an easy and quick access to such tasks.

Navigation Diagram  
![](/api/attachments/BTJ5J55G/fulltext/images/fa71a94cfa1dee286a2c2c05aa06ba21e2f1d20b4999e8894f90fdab76540241.jpg)

![](/api/attachments/BTJ5J55G/fulltext/images/9a28b2a19cb505ecb7fa175a2d85ab1598f15ea383b865ca555f0d973e2494c5.jpg)  
Figure 4 Part of the Conceptual Design for the ARCE Project.

After applying this process over the ARCE’s functional requirements, AriadneTool generates a first approach of a number of ADM models included at the Conceptual Design level, but the designer is in charge of improving and refining them. Figure 4 shows some of the conceptual models for the three requirements defined at the beginning of this section. The Structural Diagram reflects the node Arce as homepage of the system, which is composed of a set of nodes that represent the information structure. The Navigation Diagram shows the links among nodes in which the node Arce has turned into a navigation tool to provide access to all nodes, as stated in the requirement R3. The Internal Diagram of Node Arce depicts its contents, that is a navigation bar and the space in which the nodes Publish\_news, Exchange\_messages, Initial\_Report, and Offer\_Resources will be displayed. The ARCE web system is much more complex as it can be seen in Dı´az et al. (2005).

## Refinement of the design level: from Conceptual Design to Detailed Design

At the design level, the modeling is accomplished from two complementary perspectives: Conceptual Design and Detailed Design.

![](/api/attachments/BTJ5J55G/fulltext/images/b7595bfaada116a3fdf9b017e2e67380d7c694e81d647a1f8a7643e4e2b8e6d5.jpg)

![](/api/attachments/BTJ5J55G/fulltext/images/e76ab4621f133535ea61cd611bd9cb5e0321dd09bf9ff121a669528e34dad6bd.jpg)

![](/api/attachments/BTJ5J55G/fulltext/images/6acf331da7d3f31eef4e9b0fb26dfc4b63844695b84d8bf49ec441027401bd64.jpg)  
Figure 5 The Functional Specifications of the ARCE Project.

In order to illustrate the differences between these two abstraction levels, let us consider the Functional Specifications of the ARCE project in a more detailed way. This model is devoted to specify all those services supported by the system that go beyond navigation, such as database access, information retrieval facilities, or communication mechanisms. Figure 5 includes the tasks gathered in requirements R1 and R2 as system functions. The functions have been described following a top-down approach, grouped by routine or emergency. Each of the previous groups is further divided into sub-functions, which in turn are broken down into descriptions of the step-by-step tasks in order to ensure that functions can be reused and are defined properly.

Table 2 The Labyrinth ++ as an ontology  
```txt
The Labyrinth++ as an OWL ontology
<owl:Class rdf:ID="Composite">
    <rdfs:subClassOf rdf:resource="#Node"/>
    <rdfs:subClassOf rdf:resource="#ContainerLaby"/>
</owl:Class>
<owl:Class rdf:ID="Simple">
    <rdfs:subClassOf>
    <owl:Class rdf:ID="Node"/>
</rdfs:subClassOf>
<owl:TransitiveProperty rdf:ID="hasNodeAggregation">
    <rdfs:range rdf:resource="#Node"/>
    <rdfs:domain rdf:resource="#Composite"/>
    <rdfs:subPropertyOf>
    <owl:TransitiveProperty rdf:about="#hasNode"/>
    </rdfs:subPropertyOf>
    <rdf:type
rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
</owl:TransitiveProperty>

Instance of Labyrinth++ in RDF
<Composite rdf:ID="Routine">
    <hasNodeAggregation
rdf:resource="#Publish_news"/>
    <hasNodeAggregation
rdf:resource="#Exchange_messages"/>
</Composite>
<Simple rdf:ID="Publish_news"/>
<Simple rdf:ID="Exchange_messages"/>

Wellformedness rules
"A Simple Node can't have a \"hasNode\" property",ERROR,"Structural"
while (iterator,hasNext()) {
    Individual simpleInstance = (Individual)iterator.next();
    Property property = model.getProperty(nameSpace+"hasNode");
    StmtIterator iterStatements = model.listStatements(simpleInstance,property,(RDFNode)#null);
    if (iterations.hasNext()) {
    String id = recoveryId(simpleInstance,model,nameSpace);
    if (id != null) {
    setComponent(id);
    sendError();
```

Then, during the ADM Detailed Design, the abstract entities and functions specified in the previous phase are instanced into concrete elements. In the Detailed Functional Specification, the previous functions are classified in two different types: Tasks that are functions which require the user intervention to be performed, basically through form-based interfaces; and Operations, that are functions only triggered by the user but are performed by the system executing a script, program, or invoking a web service. In this case, the function fpublish\_news is a task invoked by the user that provoke the execution of the following sequence of functions: fvalidate\_data (check all mandatory fields that are filled), fsubmit\_news (submit the information to the server), finsert\_news (create a new entry for the item of news), and fdysplay\_news (display the new item in the browser). Moreover, for each function a code file can be attached.

Next step is to associate each function with a specific object that is involved in it. With this purpose, the task fpublish\_news is associated with the node Publish\_news where the user starts to execute it; and all its operations are associated with the event OnClick of the content Add, which is the button used to trigger the function.

Moreover, during this stage, designers can check the consistency and completeness of the models with respect to their semantics. For that, AriadneTool translates all the models created during the Conceptual Design into instances of the Labyrinth þ þ ontology. Some representative concepts of the meta-meta-model definition as an ontology are shown in the first cell on the first row of Table 2.

This fragment contains part of the elements used to represent the concept Node that can be Simple or Composite, and the property hasNodeAggregation needed to describe the example of Structural Diagram has been previously presented. The instances of these elements defined during the ADM Conceptual Design in each model are shown in the second cell on the first row of Table 2. The meta-meta-model is complemented with well-formedness rules that are executed over the instance of the meta-model. One of these rules, which checks that a simple node cannot have a whole/part or specialization relationship with others nodes, is gathered on the second row of Table 2. Ontology provides the syntantic restrictions and semantic rules provide the semantic restrictions.

![](/api/attachments/BTJ5J55G/fulltext/images/fd0fa3f8c7b31b7f8c87ec8923fbc8c6e9c46c53df938b07f8ab21762bfd5a73.jpg)  
Figure 6 Diagram of the Builder pattern adapted to our prototype generator module.

This instance of the Labyrinth þ þ together with the information about resources gathered during the Detailed Design will be used to accomplish the final step.

## From models to prototypes based on web markup languages

Once the models for all design views in both abstraction levels have been specified, they can be transformed to light prototypes. AriadneTool supports this transformation into different implementation source codes based on web markup languages such as HTML, XML, SMIL, and RDF. The prototype wizard is in charge of gathering the required implementation details for mapping the models to a given target platform.

In order to perform this last transformation, this module has been implemented applying the builder pattern (Gamma et al., 1995). This pattern allows us to separate the construction of the prototype from its representation in different languages so that the same construction process can give place to prototypes. Figure 6 depicts the class diagram for the builder pattern applied to our context.

The process of transformation is launched and led by the class AriadneReader. Although during the design level the hypermedia modeling concerns (structure, navigation, presentation, behavior, processes, and access) have been dealt separately in different models, they are views of the same instance of the Labyrinth þ þ , which is the input artifact to generate the different source codes. Actually, the class AriadneReader contains general transformation rules that determine the order in which the elements of the meta-meta-model instance have to be translated. Since each target platform can have its own technological constraints with regard to the conceptual representation of the application (i.e., n-ary links are not supported by the web technology or synchronizations between multimedia contents are only supported by the SMIL language), the specific transformation rules are managed by the interface Converter. This abstract interface defines methods that turn Labyrinth þ þ elements into their target representation.

Currently, AriadneTool has specialized converters for SMIL, XML, and RDF. HTML code is obtained applying XSLT to the XML code. Following with our example, in order to translate the node Publish\_news to code, the class AriadneReader calls to the method ConvertNode. For the SMIL language, a file with a .smil extension is generated. Labels to determine the begining and the end of an SMIL node and each content of the node as a region are created. In the case of the semantic web prototype, an RDFS schema to provide the vocabulary of the application domain and RDF files for the data are generated.

![](/api/attachments/BTJ5J55G/fulltext/images/f99abfe4a93a1dd3a850e3b39c64c10538e3a6b99306269d2b6525f6c0c7b7e7.jpg)  
Figure 7 Snapshot of the node ARCE as page of the ARCE System.

Each node is turned into a class and its contents are its properties. For more details about transformation rules, see Montells et al. (2005). Finally, the XML code is obtained directly from the documents of a design project since they are stored as XML files.

In Figure 7, a snapshot of the node Arce is shown as result of the steps followed in this section. This node contains a navigation bar and displays the information of the system; in this case, the node Publish\_news that allows users publish new news, as it was designed during the Conceptual Design level (see Figure 4).

## Discussion and lessons learnt

In order to discuss the main contributions of our proposal, we will make use of the research framework described in Hevner et al. (2004), whose application to the work here presented is depicted in Figure 8.

As aforementioned, we propose a couple of design artifacts: a method called ADM and an automation tool called AriadneTool. The ADM method provides a number of meta-models that can be used by developers of a multidisciplinary team to specify the different characteristics of their systems, including the information structure, the navigation capabilities, the tasks supported, the interactive mechanism, the multimedia presentations, and the access rules. The automation tool, AriadneTool, makes possible to create such models and relies on a number of model transformation processes to support model validation as well as the automatic generation of conceptual models from requirements by means of design patterns. Both, the method and the tool, have been developed in an iterative way by testing its applicability and expressivity in real projects and design experiences where the ADM method has been shown most useful both for the expressivity of its meta-models as well as for the flexibility of the process.

The model-driven approach here described is based on knowledge from the web engineering arena (in terms of hypermedia/web reference models and methods) as well as from the model-driven development domain (in terms of meta-modeling and model transformation). In particular, we first established a modeling architecture that is an instance for the web domain of the classical OMG four-layer architecture (see Figure 1). Model definition and transformation is supported by the automation toolkit AriadneTool.

Moreover, the empirical evaluation of ADM in web design courses, where the method was used by novice developers, revealed that what is chiefly required is a mechanism to facilitate the explicit reuse of web design knowledge, in the form of design patterns, so that developers can approach the development process as a learning experience as suggested for the software development life cycle by Klein & Hirschheim (1991).

Though in the web engineering research field, various MDD approaches have been proposed in the past 10 years; in practice, most of them do not fully exploit the potential of the two MDD cornerstones, meta-modeling and model transformation, as it will be discussed in the next paragraphs.

![](/api/attachments/BTJ5J55G/fulltext/images/6cb164254fca5daf10765d04f618269d355bd1e7f34a0a4a764561b2476b805e.jpg)  
Figure 8 Application of the research framework to ADM and AriadneTool.

Firstly, most of these methods provide design models belonging to the M2 layer that deal with different perspectives of a hypermedia/web system but the other architectural layers, including M3, are not considered, except for UWE which includes a common meta-model for the representation of web requirements engineering (Escalona & Koch, 2006). Our approach was originally conceived as an MDD framework where the M3 layer, the Labyrinth þ þ meta-meta-model, has been instanced as a number of purposeful ADM design meta-models in the M2 layer. Developers make use of the AriadneTool to create specific instances of the ADM meta-models that represent specific solutions to their requirements. Finally, AriadneTool applies model transformation to create instances of such models corresponding to code for different operation environments.

Secondly, hypermedia/methods neglected meta-modeling at the beginning, but since meta-modeling is a prerequisite of the MDD approach authors are now providing a formal representation of their design artifacts according to MOF (Koch & Kraus, 2003; Schauerhuber et al., 2006). Opposed to this tendency, the design metamodels of ADM rely on a formal meta-meta-model Labyrinth þ þ that has been iteratively improved during its lifetime to cope with technology advances. In our case, we have surpassed the initial notation that used set theory (Dı´az et al., 1997) to adopt an ontological approach that provide us with a machine-understandable semantics as well as enabling consistency checking and model validation, two features that are not supported directly by MDA (W3C, 2006).

Thirdly, transformations from models to code are also supported in most methods, in either manual (Koch, 2006) or automated way (Go´mez et al., 2001; Ceri et al., 2003; Montero et al., 2004a; Nunes & Schwabe, 2006). However, the transformation from web requirements to models remains as an unsolved problem yet. Again, UWE has gone for the forthcoming QVT transformation language to address this transformation but it has to be done in a manual way (Koch et al., 2006) while our approach supports a semi-automatic ontology-based transformation from requirements to design models mediated by design patterns. This mechanism not only helps designers to take rationale design decisions based on expert knowledge but also introduces them to good design principles and practices embodied in design patterns, so that design patterns become both a development guide as well as a learning tool providing multidisciplinary design knowledge to web developers.

Finally, and from a practical point of view, when applied in real experiences, as the one reported in the previous section, our web MDD proposal has been shown most useful since:

(1) Designers can concentrate on developing models that solve their problems instead of getting bewildered by implementation and aesthetic issues. Indeed, as the ADM proposes design artifacts covering complex features of web systems (such as multimedia presentations, interaction, or access control), developers can realize they need to analyze problems they had initially underestimated or considered as implementation decisions. For example, security modeling is often postponed till the implementation phase on the assumption that this is a problem that only concerns the web server security mechanisms. However, security is a basic requirement from the application point of view that has to be integrated in the whole development cycle (Brose et al., 2001).

(2) Design models can also be used to perform analytical evaluations involving stakeholders since each of the ADM meta-models intentionally hide unnecessary information to focus on a specific kind of problem. For example, prototypes are not particularly useful for evaluating the information structure, since stakeholders have to abstract by themselves the structure underlying the system they are navigating through and decide whether this is the most appropriate structure or not. On the contrary, an easy to understand graphical representation of this structure, like the ADM Structural Diagram, can be discussed with stakeholders without being disturbed by other design issues like the aesthetics of the user interface.

(3) Design patterns help to reuse knowledge, not only what is particularly useful for novice designers but also just to reduce design efforts. Moreover, as web developers apply patterns in their design they also get knowledge on useful solutions, so that patterns also act as informal learning tools.

## Conclusions and further research

In this paper, we have described the model-driven process underlying the ADM hypermedia/web development method. In particular, we have focused on the

## About the authors

Ignacio Aedo has a degree and a doctorate both in Computer Science from the Polytechnic University of Madrid. Since 1992, he has been working in the Carlos III University where he is currently a full professor in the Computer Science Department. His research areas include access modeling, emergency management systems, human computer interaction, and e-learning. He is co-author of several articles and books concerning her research activities. Paloma Dı´az received a degree and a doctorate both in Computer Science from the Polytechnic University of Madrid. Since 1992, she has been working in the Carlos III University where she is currently a full professor in the Computer Science Department and is the Head of the DEI transformations between its different abstraction levels that range from transformations of web requirements to ADM models and from the latter to web code. These transformations are defined at the meta-meta-model level, M3 Layer in OMG terms, and are based on the ontological expression of Labyrinth þ þ . Moreover, the specification of this meta-meta-model as an ontology has provided the ADM with the semantics and the reasoning to automate the consistency checking and model validation as well as to generate applications for the Semantic Web (Montells et al., 2005). Both features, the meta-modeling and ontologies, resulted essential in order to achieve a satisfactory model-driven framework that has been empirically evaluated by applying it in a real project: ARCE. From this practical experience, we have detected some aspects that require further research.

Model validation, both syntactic and semantic, is useful but not enough since what developers demand are useful hints on how to amend their errors with a minimum effort. In this sense, we have started a complementary work based on the use of graph grammars as the meta-modeling formalism and an extension of the ATOM3 tool as the meta-modeling environment, to integrate redesign rules as well as design metrics that suggest or directly perform design improvements (Guerra et al., 2005).

We have also stated the role of design patterns as learning tools in the sense they show novice designers good solutions to their problems, but it would be convenient to analyze how developers can provide feedback based on their own experience to improve the patterns as well as their application to very specific domains. Furthermore, tools to make easier the access to patterns to a multidisciplinary audience are required, since catalogues organized whether as an alphabetical list or using other esoteric criteria that are not meaningful to most web developers (such as the design perspective) difficult the access to the right pattern for a specific problem.

research group. She has been mainly researching in hypermedia/web engineering, access control modeling, e-learning, and emergency information systems. She is co-author of several articles and books, member of ACM, and senior member of the IEEE.

Susana Montero received a degree and a doctorate both in Computer Science from the Carlos III University. Since 1999, she has been working in the same university where she is currently an assistant professor in the Department of Computer Science. Her research interests include hypermedia development methodologies, CASE, knowledge representation, and their applications to hypermedia development process.

## References

AEDO I, Dı´AZ P and MONTERO S (2003) A methodological approach for hypermedia security modeling. Information and Software Technology 45(5), 229–239.

BROSE G, KOCH M and Lo¨HR KP (2001) Integrating security policy design into the software development process. Technical Report B–01–06. Freie Universita¨t Berlin, 13 November.

CAPLAT G and SOURROUILLE JL (2003) Considerations about model mapping. In Proceedings of the Workshop in Software Model Engineering, San Francisco, USA, http://www.metamodel.com/wisme-2003.

CERI S, FRATERNALI P, BONGIO A, BRAMBILLA M, COMAI S and MATERA M (2003) Designing Data-Intensive Web Applications. Morgan-Kaufmann, San Francesco, CA, USA.

Dı´AZ P, AEDO I and PANETSOS F (1997) Labyrinth, an abstract model for hypermedia applications. Description of its static components. Information Systems 22(8), 447–464.

Dı´AZ P, AEDO I and PANETSOS F (2001) Modelling the dynamic behaviour of hypermedia applications. IEEE Transactions on Software Engineering 27(6), 550–572.

Dı´AZ P, MONTERO S and AEDO I (2005) Modelling hypermedia and web applications: the Ariadne development method. Information Systems 30(8), 649–673.

VAN DUYNE DK, LANDAY JA and HONG JI (2002) The Design of Sites: Patterns, Principles, and Processes for Crafting a Customer-Centered Web Experience. Addison-Wesley Longman Publishing Co., Inc., Boston, MA ,USA.

ESCALONA MJ and KOCH N (2006) Metamodeling the requirements of web systems. In Proceedings of the Second International Conference on Web Information Systems and Technologies: Internet Technology Web Interface and Applications pp 310–317, Setu´bal, Portugal.

FERNA<sup>´</sup>NDEZ EB and PAN R (2001) A pattern language for security models. In Proceedings of the 2001 Conference on Pattern Languages of Programming, Illinois, USA.

GAMMA E, HELM R, JOHNSON R and VLISSIDES J (1995) Design Patterns: Elements of Reusable Object-Oriented Software. Addison Wesley, Reading, MA.

Go´MEZ J, CACHERO C and PASTOR O (2001) Conceptual modeling of device independent web applications. IEEE MultiMedia 8(2), 26–39.

GUERRA E, Dı´AZ P and DE LARA J (2005) A formal approach to the generation of visual language environments supporting multiple views. In Proceedings of the 2005 IEEE International Symposium on Visual Languages and Human-Centric Computing (VL/HCC’2005), pp 284–286.

HENNICKER R and KOCH N (2000) A UML-based methodology for hypermedia design. In Proceedings of the International Conference UML’2000 – The Unified Modeling Language – Advancing the Standard, LNCS 1939, York, Springer.

HEVNER AR, MARCH ST, PARK J and RAM S (2004) Design science in information systems research. MIS Quarterly 28(1), 75–105.

HYPATTERNS (2006) A Semantic Web pattern repository. http://hypatterns. no-ip.info:8080/.

ISAKOWITZ T, BIEBER M and VITALI F (1998) Web information systems. Communications of the ACM 41, 78–80.

KAPPEL G, PRo¨LL B, REICH S and RETSCHITZEGGER W (2006) Web Engineering: The Discipline of Systematic Development of Web Applications. John Wiley & Sons, New Jersey, USA.

KLEIN HK and HIRSCHHEIM R (1991) Rationality concepts in information system development methodologies. Accounting, Management & Information Technology 1(2), 157–187.

KOCH N (2006) Transformation techniques in the model-driven development process of UWE, In Proceedings of the Workshops at International Conference on Web Engineering. (ICWE ’06), p 3, ACM Press, New York, NY.

KOCH N and KRAUS A (2003) Towards a common metamodel for the development of web applications. In Proceedings of the Third International Conference on Web Engineering (ICWE 2003), Oviedo, Spain.

KOCH N, ZHANG G and ESCALONA MJ (2006) Model transformations from requirements to web system design. In Proceedings of the Sixth International Conference on Web Engineering, pp 281–288, ACM Press, New York, NY.

MONTERO S, Dı´AZ P and AEDO I (2004a) AriadneTool: a design toolkit for hypermedia applications. Journal of Digital Information 5(2).

MONTERO S, Dı´AZ P and AEDO I (2004b) A semantic representation for domain-specific patterns. In Proceeding of Metainformatics, International Symposium MIS 2004, Salzburg, Austria.

MONTELLS L, MONTERO S, Dı´AZ P and AEDO I (2005) Model-driven approach for Semantic Web based-hypermedia applications. In Proceedings of the Workshop on Web-Oriented Software Technologies IWWOST05, Porto, Portugal.

NUNES DA and SCHWABE D (2006) Rapid prototyping of web applications using domain specific languages and model driven design. In Proceeding of International Conference on Web Engineering 2006, pp 153–160, ACM Press, New York.

OMG (2003) Ontology definition metamodel request for proposals, OMG Document: ad/2003-03-40.

ORMSC (2001) Model Driven Architecture, Document number ormsc/ 2001-07-01, Architecture Board ORMSC.

PREECE J (1994) Human-Computer Interaction. Addison-Wesley Publishing Company, New York, NY.

ROBERTSON S and ROBERTSON J (2006) Volere requirements specification template. http://systemsguild.com/GuildSite/Robs/Template.html.

ROSSI G, SCHWABE D, DANCULOVIC J and MIATON L (2001) Patterns for personalized web applications, In Proceedings of EuroPlop’01, pp 423–436, Irsee, Germany.

SCHAUERHUBER A, WIMMER M and KAPSAMMER E (2006) Bridging existing web modeling languages to model-driven engineering: a metamodel for WebML. In Workshop Proceedings of the Sixth international Conference on Web Engineering, p 5, ACM Press, New York, NY.

SCHWABE D and ROSSI G (1998) Developing hypermedia applications using OOHDM. In Proceedings of Workshop on Hypermedia Development Process, Methods and Models (Hypertext’98) Pittsburgh, PA, USA.

W3C (2004a) RDF/XML syntax specification. http://www.w3.org/TR/ rdf-syntax-grammar/.

W3C (2004b) OWL web ontology language reference. http://www. w3.org/TR/owl-ref/.

W3C (2006) Ontology driven architectures and potential uses of the Semantic Web in systems and software engineering. http://www. w3.org/2001/sw/BestPractices/SE/ODA/.
