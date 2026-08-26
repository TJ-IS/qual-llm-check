---
otero_id: 28
otero_key: "AW2JXPRG"
title: "ODDM: A framework for modelbases"
authors: "Thadthong Bhrammanee; Vilas Wuwongse"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.09.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# ODDM: A framework for modelbases

Thadthong Bhrammanee <sup>⁎</sup>, Vilas Wuwongse

Computer Science & Information Management Program, School of Engineering and Technology, Asian Institute of Technology, Thailand

Received 19 February 2006; received in revised form 29 August 2007; accepted 23 September 2007 Available online 4 October 2007

## Abstract

The Web extends today's modelbases—an important DSS component—by enabling their sharing and reusing over the information network. A modelbase with a formal, precise, and expressive framework will enhance the interoperation and benefit machine–human as well as machine–machine interactions. Therefore, this paper proposes a Web-based-compatible framework for modelbases, namely ODDM. “Model Ontology” and “Model Schema” are main components of the framework. Both components seamlessly interoperate by means of OWL Declarative Description (ODD). The classification of existing modelbase frameworks is presented. Requirements for the framework are identified and the proposed framework's conformance to the requirements is also discussed.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Modelbase; Model management; Web-based DSS; Data model; Ontology

## 1. Introduction

A Decision Support System (DSS) and its components have been impacted by Web technologies and new perspectives of DSS users. The Web has been a widely accepted information infrastructure and Web technologies have become gadgets for both server- and clientside computation, particularly the technologies that are based on eXtensible Markup Language (XML). A DSS has to inevitably exploit Web technologies to improve its accessibility and widespread employment [7,30,44]. Perspectives of DSS users have altered from decision models—quantitative models—as ad hoc program subroutines to decision models as services [8,9,50]. In short, users prefer to access a convenient decision support application and use a decision model over the information network instead of owning a copy of it. They realize that this will help overcome problems of hardware and software configuration while at the same time, eliminate the duplication of effort needed to develop similar decision models. Due to those key factors, the so-called Web-based DSS [8] has gained ground, and decision support applications and their components are being more widely shared and reused. Here, a Web-based DSS is seen as a computerized system that uses Web-based technologies and architectures as an infrastructure for decision-making. The information for decision-making can then be distributed with widespread access (either internally or externally) via Web-browsers.

Similar to an ordinary DSS, a Web-based DSS mainly comprises a database and a modelbase as its important substances [44]. The former performs data organization and retrieval using database queries; the latter stores a collection of decision models. This paper refers to the term “decision model” as a quantitative model used in Management Science and Operations Research (MS/OR) such as optimization and financial models. Like a database, a modelbase also needs a data model. The data model of a modelbase is a framework that the modelbase uses to represent and describe its decision models as well as their relationships and constraints.

Various frameworks for modelbases have been proposed by a number of authors. However, they have limitations in exploiting the opportunities the Internet provides and in offering an immediate adaptation to a Web-based environment. Notable limitations are those related to Web-deployable capability, advertisement and discovery, interoperability, expressiveness, model consolidation, and model execution.

Some existing frameworks do not provide adequate Web-deployable capability (e.g., [11,13,15,33]). Such frameworks not only complicate Web deployment but also are incompatible with Web-based technologies that grow rapidly, e.g., XML and Web Services. Model advertisement and model discovery on the Web may be discouraged by frameworks that allow announcing merely simple information and provide searching by simple keywords (e.g., [9,11,20,21]). Consequently, a suitable decision model will possibly not be elicited if its description is syntactically different from words or phrases in a search. Frameworks that lack interoperability demand Web-based DSS applications perform excessive interpretation and mapping effort when combining or exchanging different information defined by different enterprises. The expressiveness is limited in frameworks that are not sufficiently flexible to formally represent certain information such as integrity constraints, mathematical notations, and relationships among decision models. Performing model joining and integration—linking or combining multiple models when only one model cannot serve the need—is awkward if there is insufficient description of decision models or an inadequate conflict solution mechanism. Lastly, a decision model may not be executed on the Web to obtain a solution result (e.g., [13,36]), as some frameworks have no supportive computation mechanism.

This paper proposes a generic framework for modelbases called OWL Declarative Description for Modelbases (ODDM). The framework aims to flexibly represent various types of decision models. ODDM is suitable for assimilating into the Web-based infrastructure and is ready to be enhanced. It is based on OWL (Web Ontology Language) which is the ontology language recommended by W3C [5] and an important language for the Semantic Web [6]. The framework comprises two major components: Model Ontology and Model Schema. The former provides meanings of specific terminology agreed upon by concerned user communities and applications; the latter contains purely generic schematic descriptions of decision models. Note that here the terms “decision model” and “model” will be used interchangeably, depending on the context. A transportation problem will serve as an example throughout since it is a well-known example often used in modelbase literature.

An overview of the Semantic Web and OWL is introduced in Section 2. Requirements for a good framework for modelbases are identified in Section 3. Sections 4, 5, and 6 present the essence of the proposed framework, its detailed representation, and its operations, respectively. Section 7 explains a prototype implementation, Section 8 discusses the benefits of ODDM, and Section 9 reviews related works. Finally, Section 10 contains conclusions and suggestions for future work.

## 2. The Semantic Web

The Semantic Web [6] is a vision for the future of the Web on which information can be processed by machines. It extends current human-readable web contents by encoding their explicit meanings in a form that can be understood by computers. As a result, machines can perform operations on web resources in an intelligent manner. The Semantic Web relies on an important technology, i.e., ontology. Ontology—a formal, explicit, shared specification of a conceptualization—provides the Semantic Web with common definitions of terms and their relations used in web resources; and thus facilitates the understanding and processing of the web resources. In the context of the Semantic Web, ontology is a document or file that formally defines terms and their relations [6]. Like other documents, ontology requires a language for its description.

An ontology language is a formal language used to encode an ontology so that it can be shared and processed by machines. Web Ontology Language (OWL) [5], an ontology language recommended by W3C, is a formal markup language for describing ontological data and for sharing information on the Internet. At present, many communities have adopted the OWL standard and have disseminated their information using OWL or an OWL-compatible syntax for the sake of interoperability [16,46]. OWL is in fact a vocabulary extension of the Resource Description Framework (RDF) [31]; OWL provides more facilities to represent machine-interpretable meanings of Web contents such as additional vocabularies to describe classes and properties. Fundamentally, OWL employs RDF graphs [31] as its primitive basis, i.e., a statement representing a piece of information is modeled as a graph that comprises the subject (resource) node and the object (resource or literal) node of the statement as well as the property arc describing a relationship between the two nodes. The direction of an arc always points toward the object of a statement. An oval, an arrow, and a rectangle denote the resource, resource property, and literal object, respectively. For example, the statement “a transportation flow has a source location as its origin point” can be presented by having a transportation flow as a subject, a source location an object, and a has origin a property presenting a relation between those two nodes (Fig. 1). An RDF graph can be serialized in the XML-based syntax called RDF/XML, which is in turn an exchange syntax for OWL (known as OWL RDF/XML). An OWL RDF/XML document thus comprises a set of OWL elements denoting relations among certain resources.

## 3. Requirements for good data models

A good data model or framework for the modelbase of a Web-based DSS should have the following capabilities:

(1) Compatibility with Web technologies. A Webbased DSS is obligated to employ Web-applicable technologies in most, if not all, of its components. A framework for modelbases must be Webtechnology-compatible in order to yield modelbases deployable in the Web-based environment.

(2) Support of interoperability. In the Web environment, modelbases can be independently developed and maintained at different websites by heterogeneous groups of people. A framework should enable modelbases to be interoperable by providing a precise context description of information to allow sharing of a similar understanding when processing the same set of information.

(3) Support of advertisement and discovery of decision models. A framework is expected to facilitate finding and eliciting suitable decision models from a Web-space model repository by creating user awareness for an available decision model through advertisement of the model's public information. The next-generation Web, the Semantic Web, requires greater capability of a framework in terms of model discovery; the framework should allow intelligent agents to find decision models by their semantic contents rather than merely by keywords and their syntactic forms.

(4) High expressive power. In addition to the normal ability to describe decision models, the following four representation capabilities are desirable. Firstly, a good framework should support the representation of application-dependent integrity constraints (e.g., user-defined rules). Secondly, an expressive framework should be assimilable with Web technologies that enable expressing mathematical notations, including algebraic formulae and symbols, to satisfy users that prefer to inspect a decision model algebraically. Thirdly, an efficient framework should support indexing [23,41], i.e. accommodating the characterization of set elements and allowing basic operations on them. Indexing can be handled either in symbolic subscripts [19,29] or in a subscript-free [38] manner. Finally, the emerging practice of model sharing and model distribution may draw incomplete information due to improper coordination. Accordingly, a good framework should embed the ability to form and allow storing of a decision model even when some parts of the model are notyet-known. Though this point has not been adequately addressed in existing frameworks, it should be taken into account.

![](/api/attachments/AW2JXPRG/fulltext/images/02e0f99e140d37e815db9f747911cb5438a46f885132b88b3787ef408fb9eb2c.jpg)  
% The TransportationFlow ,SourceLocation, and DestinationLocation are owl:Class. The property hasOrigin defines a % relation between the TransporationFlow and the SourceLocation, and the hasDestination between the % TransporationFlow and the DestinationLocation  
Fig. 1. An RDF graph example.

(5) Support of model joining and integration. A good framework should provide an adequate level of abstraction of a model description in order to perform model joining and integration [34]. Model joining simply links models based on their input/output. A framework that provides an external view of model description would facilitate such operation. On the other hand, model integration requires users or applications to access an internal structure in order to modify decision models and perform complex model consolidation. This operation requires a framework to offer an internal view of model description. A framework should also support conflict resolutions which arise during model joining and integration. Common conflicts [34] include naming conflicts (use of the same name to refer to individuals), granularity conflicts (different granularity bases of models, e.g., compute annually or quarterly), and dimensional/unit of measurement conflicts. A framework that provides the means to handle these conflicts is desirable.

(6) Model executability. A framework should represent a decision model in a form that can be feasibly comprehended by Web applications inclusive of mathematical computation. The conceptual design of a framework that can be smoothly integrated with a mathematical execution engine to yield a solution result is one promising aspect of a good framework.

The next section presents a new data model that provides a convergence between model representation and Web technologies as well as takes into consideration the requirements for a good modelbase data model.

## 4. The proposed data model: conceptual framework

Generic decision problems normally contain terminologies and descriptions of the problem structure.

Consider, for example, a transportation problem, the objective of which is to minimize the total cost of transporting product requirements without exceeding supplier capacities. The problem contains terms such as transportation flow, source/destination location, and shipment quantity. The problem also has description of the problem's constructs, e.g., model inputs include transportation cost of transportation flows, supply quantities of source locations, and demand quantities of destination locations; and a supply constraint of the problem requires that the total product quantity shipped must be less than or equal to the supply quantity. An individual company may adopt an available generic problem description to solve its own similar problem.

This section presents the primary components of modelbases (Fig. 2): (1) the Model Ontology— references of common terms—and (2) the Model Schema—systematic descriptions of decision models. RDF graphs are employed to demonstrate examples of this conceptual framework.

## 4.1. Model ontologies

This paper proposes the “Model Ontology” as one of the major components of the framework. A Model Ontology provides an indispensable and consistent terminology, in accordance with known and accepted classifications, which can be used to describe different decision models and their components. The agreements of terminology as well as rules for extending terms and their relations are explicitly defined in a user and machine understandable fashion.

When a decision model is formulated from scratch (e.g., [12,19,29]), different users may generate different conceptualizations for the same problem. Improper documentation of the formulation process and terms can lead to difficulty in reusing the model or in its understanding in the future. When a model is generated from templates (e.g., [10,35]), existing templates may inadequately provide terms and insufficiently be declarative for extending template elements and terms. Lastly, when multiple models are consolidated in the Web space, terminology conflicts may arise. Without a consensus on meaning, the exchange of model information on the Web becomes complicated. All of these problems reflect a need for a formal specification of shared conceptualization for modelbase users and applications. The proposed “Model Ontology” aims to address these problems.

The Model Ontology consists of four main parts: problem taxonomy, mathematical model entities, world concepts, and arithmetic-related properties.

![](/api/attachments/AW2JXPRG/fulltext/images/d35a6312c73474c4ba9b3825f1628f339c80defe3f081500db04dae829510555.jpg)  
Fig. 2. ODDM components.

■ Problem taxonomy consists of terms and classifications of mathematical problems, e.g., optimization, simulation, and forecast, transportation, and assignment.

■ Mathematical model entities encompass indispensable elements of a quantitative model, e.g., Object and Relation [25].

■ World concepts bring together necessary views of the real world, which relate to concerned decision problems. They also correspond to “mathematical model entities” in some sense. Their broad conceptual elements may cover Resource, Activity, Time, Event, State, and Quantity.

Arithmetic-related properties include a Relation denoting comparability between model elements, e.g., Equal and Less Than, a Function Type indicating a predefined procedure, e.g., Sum and Mean, and an Operator signifying an operator symbol, e.g., Minus and Time.

The RDF graph of Fig. 3(a) illustrates a sample Model Ontology containing a small set of classes and relationships related to the logistics domain, which will also be used in the later transportation problem. The graph shows that a transportation flow has a source location and a destination location as its origin and destination, respectively. Each source and destination location has supply and demand capacities, respectively. From the viewpoint of the world concepts, the source location is considered to be a resource that supports activities, i.e., a transportation flow. On the other hand, from the angle of the mathematical model entities, the source location is considered to be a primitive index.

The elements and relations used in the example are accepted for temporary use since there is currently no default ontology in a modelbase domain and none of the existing related ones (e.g., [25,26,43,47,49,51]) has all the necessary terms and relations served as a shared conceptualization for decision models. For example, GAMS [26] and NEOS [43] look at the main concept of mathematical problems but disregard basic terms of the real world domain, such as “resource” and “activity”. While OZONE [49] presents an ontology for a scheduling and logistics domain, it does not explicitly offer a relation, function, or operator used in a quantitative model. The actual Model Ontology may incorporate other existing ontologies related to the MS/ OR domain.

## 4.2. Model schemas

The Web-processible schema, so-called “Model Schema”, is proposed as a counterpart of Model Ontology. A model schema presents a generic schema for describing a decision model such as a transportation problem or assignment problem. The terminology used in a model schema is drawn from the Model Ontology, thus eliminating vagueness for modelbase users and Web-based DSS applications. A model schema can be specialized into a model instance, for example, a transportation problem for company A is a model instance of a transportation model schema.

![](/api/attachments/AW2JXPRG/fulltext/images/e6128f44c7dc467564cb89d867836824e2edc3e13dded808210313a11abe6b26.jpg)  
Fig. 3. A sample topography of transportation problem and its references.

Modelbase users have realized the need to specialize a generic pattern of a certain decision model to solve similar business problems in order to reduce excessive effort and time in formulating a decision model from scratch [10,36]. For example, the description of a generic transportation problem should be instantiated by both companies A and B if they have similar logistics problems. In addition, a Web-based DSS application in the Semantic Web era requires human- and machineprocessible information; problem descriptions must be defined not only for syntactic form, but also for their semantic content. As a result, it is necessary to have a model schema that generically describes a decision model and facilitates both structure and semantic trading when exchanging information among applications. It is also essential that a data model can uniformly represent both model schemas and model ontologies in order to yield less translation effort between both components when they borrow terms and perform meaning interpretation. Lastly, a model schema should support the interest of different users that use its instance decision models, i.e., some users are interested in knowing decision model inputs/outputs while others the organization of internal structure of decision models.

The structure and semantics of a model schema are determined by the “Meta-Model Schema”. This schema of model schemas identifies an “external view” and an “internal view” of a decision model description; they are referred to as Model Profile and Model Configuration, respectively. Both views serve various desirable aspects in terms of information item inspection.

## 4.2.1. Model Profile

Model Schema is “presented” by Model Profile—a black box view. Its major parts are:

– One textDescription referring to a short abstraction of the decision model.

– One modelClassification referring to the problem in the taxonomy of problem types in Model Ontology.

– One hasModelConfiguration referring to the corresponding Model Configuration.

– One or more inputs pointing to an Input class. One dataValue and one measureUnit for each Input.

– One or more outputs pointing to an Output class. One dataValue and one measureUnit for each Output.

## 4.2.2. Model Configuration

Model Schema is “described” by Model Configuration—a glass box view, which comprises major elements of model constructs. The following are key parts:

– One or more modelConstructs pointing to a Construct class which serves as skeletons, major model constructs of a particular decision model (e.g., objective function, constraint, decision variable, and independent variable for an optimization model type).

– One (optional) math containing MathExpression correspond to MathML of the model construct.

The element Construct is extensible; it can contain properties and related elements that are appropriate for describing each Construct.

Fig. 3(b) shows Meta-Model Schema; Model Profile and Model Configuration are main elements. The Model Profile contains inputs/outputs information; the Model Configuration provides internal constructs of a decision problem. Based in this Meta-Model Schema, the Transportation model schema is depicted in Fig. 3(c). The example focuses on elements and detailed relationships of the TransportationConfiguration—a specialization of the Model Configuration. Major model constructs are the objective function, constraints, decision variables, and independent variables. The objective is to minimize total cost of shipment. There are demand and supply constraints. The shipment quantity of each transportation flow is considered a decision variable. Supply quantity of source locations, demand quantity of destination locations, and the transportation cost of each flow are considered independent variables. The transportation model schema selectively employs problem-relevant terminology from Model Ontology. Property characteristics such as owl: disjointwith can be used to enhance the semantics of items. For example, if a source location and a destination location are disjoint, one can infer that they have no member in common (If a location A is a destination location of the flow, it can only be a destination location. The location A can only accept goods but cannot supply goods.).

The semantics of terminology appearing in the transportation schema can be further inspected by examining Model Ontology. In the illustration, the bold ovals in Fig. 3(a) (Model Ontology) depict the genesis of the corresponding bold ovals in Fig. 3(c) (Transportation model schema). Thus, for example, users who see the source location and destination location elements in the transportation model schema can learn from the Model Ontology their meaning, i.e., those elements are primitive indexes and resources required by an activity.

Suppose the Havill Company needs to apply the Transportation model schema to its similar problem situation. The HavillTrans, an instance of the Transportation model schema, can be created as illustrated in Fig. 3(d). For example, Indianapolis, Chicago, and Hoover are source locations. New Orleans, Orlando, and Miami are destination locations. There are transportation flows from each source to destination locations and each flow has associated cost, e.g., Chicago–Orlando is a transportation flow; the transportation cost associated with this flow is 8 hundred dollars. There are supply and demand quantities of each location, e.g., Indianapolis has a supply quantity of 1 ton and New Orleans has a demand quantity of 4 tons. Due to the space limitation, Fig. 3(d) shows a partial illustration. The rest of the numerical data may be taken from the screenshot in Fig. 15 and instantiated in a similar manner as in this illustration; the data is borrowed from the classical transportation (Hitchcock) problem [42].

## 4.3. Model Ontology and Model Schema constraints

Restrictions can be put on Model Ontology and Model Schema in order to constrain the semantics. Restrictions on items in the Model Ontology, in the sense of common phenomena, are referred to as Model Ontology Constraints. For example:

– Location constraint. The origin and destination of transportation must be different locations.

– Shipment quantity constraint. If goods have no loss of generality (e.g., an evaporation of liquids), the quantity of goods shipped from one location must be identical when it reaches the next location. If loss of generality exists, net gain or loss in units must be taken into account.

– Comparability in sum constraint. All quantities to be summed must be comparable. Only quantities that have compatible units of measurement are comparable; their units of measurement must have the same dimensions.

On the other hand, restrictions on items in Model Schema elements are referred to as Model Schema Constraints. Note that they are different from ordinary constraint functions (such as an ordinary Linear Programming (LP) constraint) which serve as an ordinary part of a description of a decision model. Examples of Model Schema constraints are:

– Any decision variables that appear as part of a constraint must also appear as part of an objective function.

– For an LP duality problem, if a schema describes the primal form of a maximization problem, then a schema describing its dual form must be the schema for a minimization problem (and vice versa).

Constraints enhance the semantics of modelbase items. Though OWL can be employed to encode basic framework components (i.e., Model Ontology and Model Schema); OWL still has limited expressive power for describing complex constraints (restrictions) and rules. A representation language that can enhance the limited expressive power of OWL is desirable. The next section presents such a language and shows how to use it to represent model constraints.

## 5. The proposed data model: detailed framework

Due to its high expressive power, OWL Declarative Description (ODD) is employed as an underlying language to describe the framework components as well as constraints, in a formal and declarative manner.

## 5.1. Introduction to ODD

ODD is a language which combines OWL and RDF Declarative Description (RDD) [1], as well as providing a computational power by means of clauses (rules).

RDD is a modeling language that can directly represent all RDF-based languages. ODD extends RDD by 1) incorporating elements that contain an OWL namespace and 2) introducing ontological axioms for support of OWL semantics. ODD can directly represent OWL and extend ordinary well-formed OWL elements by the incorporation of variables for the enhancement of expressive power and representation of implicit information of a decision model into so-called OWL expressions. Every component of an OWL expression can contain variables, e.g., tag names or attribute names (N-variables), string or literal contents (Svariables), and expressions (E-variables) (Fig. 4). Every variable is prefixed by “\$T:” where T denotes its type; for example, \$S:ResourceX is an S-variable which can be specialized into a string. Ordinary OWL elements— ground OWL expressions—are OWL expressions without variables. OWL elements with variables are called nonground OWL expressions. As a concrete example, consider the OWL expression:

bowl:ObjectProperty rdf:ID=q\$S:SomeRelationshipqN brdfs:domain rdf:resource=q#TransportationFlowq/N brdfs:range rdf:resource=q#SourceLocationq/N b/owl:ObjectPropertyN

<table><tr><td>Variable Type</td><td>Prefix</td><td>Instantiation to</td></tr><tr><td>N-variables (Name variables)</td><td>$N:</td><td>Element types or attribute names</td></tr><tr><td>S-variables (String variables)</td><td>$S:</td><td>Strings</td></tr><tr><td>P-variables (Attribute-value-pair variables)</td><td>$P:</td><td>Sequences of zero or more attribute-value pairs</td></tr><tr><td>E-variables (OWL-expression-variable variables)</td><td>$E:</td><td>Sequences of zero or more OWL expression</td></tr><tr><td>I-variables (Intermediate-expression variables)</td><td>$I:</td><td>Parts of OWL expression</td></tr></table>

Fig. 4. Variable types.

This expression represents certain (possibly indirect) relationships between the resources TransportationFlow and SourceLocation. For instance, it can represent

bowl:ObjectProperty rdf:ID=qhasOriginqN brdfs:domain rdf:resource=q#TransportationFlowq/N brdfs:range rdf:resource=q#SourceLocationq/N b/owl:ObjectPropertyN

which specializes the S-variable \$:SomeRelationship into the hasOrigin property, indicating the relationship between the TransportationFlow and the SourceLocation.

More complex and implicit information can be modeled by an ODD description. An ODD description is a set of OWL clauses, each of which has the form:

$$
H \leftarrow B _ {1}, \dots , B _ {m}, \beta_ {1}, \dots , \beta_ {n}.
$$

where m, $n \geq 0 ,$ , H and $B _ { i }$ are OWL expressions, and each of the $\beta _ { i }$ is a predefined OWL constraint—useful for defining a restriction on OWL expressions. The OWL expression H is called the head, the set $\{ B _ { 1 } , . . . ,$ $B _ { m } , \beta _ { 1 } , . . . , \beta _ { n } \}$ the body of the clause. When the body is empty, such a clause is referred to as an OWL unit clause and the symbol $\bullet _ {  } ,$ will often be omitted; hence, an OWL element or document can be mapped directly onto a ground OWL unit clause. Given an

ODD description P, its meaning, denoted by M (P), is the set of all OWL elements that are directly described by and are derivable from the unit and the non-unit clauses in P, respectively. Paper [1] gives theoretical details.

ODD employed OWL clauses to support OWL ontological semantics. As an example, Fig. 5 contains OWL clause $A _ { \mathrm { i n v } }$ which models an ontological axiom of OWL, owl:inverseOf. This axiomatic rule states that if a property \$S:PropertyX is an inverse of a property \$S:PropertyY, then for a \$S:Resource1 that has the \$S: PropertyX pointing to a \$S:Resource2, one can infer that the \$S:Resource2 also has the property \$S:PropertyY pointing to the \$S:Resource1. Referring to the example in Fig. 1, if the property hasOrigin is an inverse property of the property sourceOf, one can infer that a SourceLocation in Fig. 1 is a “source $\mathrm { o f ^ { \circ } }$ a TransporationFlow. Note that the meaning of other OWL modeling constructions, such as owl:SymmetricProperty and owl:complementOf can also be defined in terms of OWL clauses in a similar manner.

In summary, a modelbase can be modeled as an OWL description consisting of unit clauses, representing OWL elements describing the modelbase items, and non-unit clauses, describing relationships, constraints, and other semantic information derived from the modelbase.

![](/api/attachments/AW2JXPRG/fulltext/images/85e9d9107d063c8ca64737929f30d95cf46f13e12e71bf5a1c07e438b35a0eea.jpg)  
Fig. 5. Axiomatic semantic of OWL modeling constructs.

![](/api/attachments/AW2JXPRG/fulltext/images/cd51aa624cf88f40762e2c62dca594ea052841eee1e65058460577629d806f40.jpg)  
% The clause CshipmentQuantity presents a standard nature of a shipment quantity of a product that has no loss of generality: The quantity of % products from a source location must not be lost or gained when it reaches the destination location  
Fig. 6. Model Ontology constraint example: a shipment quantity constraint

## 5.2. Representation of model constraints

Constraints on Model Ontology and Model Schema (aforementioned in Section 4.3) can be defined in terms of ODD clauses. The head specifies the resulting element; the body presents information to be selected as well as conditions. As an example, the clause C in Fig. 6 presents a simple Model Ontology constraint regarding the nature of a shipment quantity of products. It states “if a product is considered one with no loss of generality, the quantity of product shipped from a source location must not be lost or gained when the product reaches the destination location”. The head of clause C<sub>ShipmentQuantity</sub> describes the results, which indicates the value of product units when reaching the destination location, the body extracts the corresponding information regarding the transportation flow, which includes the source and destination locations, and product units at each location. The ODD Equal and Subtract functions in the body check to determine if the product is considered a no loss of generality one; then subtract zero from the unit amount at the source location will become the unit amount at the destination location, i.e., there must be no product lost or gained during the shipment.

When Model Schema borrows terms from Model Ontology, a model schema will also carry the semantics (defined by a Model Ontology constrains) of the borrowed terms. Such semantics is also passed on to model instances. Constraints are also useful for model management such that any change made to an information item in modelbases must abide by the rules.

## 5.3. Modelbase users

Among different types of modelbase users [39] (as identified in Fig. 2), a model builder maintains the ontology so that schemas for decision models can be properly created. The model builder is also responsible for maintaining changes in model schemas or model instances made or submitted by other user types. The model builder may cooperate with system technicians for any technical assistance. An analyst identifies an appropriate model and may manipulate the model to suit his problem situation, and, either passes the selected decision model to decision makers or assigns instance data (if known). A decision maker either creates an instance decision model by supplying the data obtained from the analyst or simply runs the model (if data are pre-assigned). A single person can play roles in more than one user type and multiple users can occupy a role.

## 6. Operations on decision models

ODD is used as a query language for the framework in addition to its use as a representation language. Therefore, not only modelbase components can be uniformly represented under the same language, operations on all components can be seamlessly performed using the same query language as well.

There exists a limited number of query languages for modelbases and existing ones inadequately address the retrieval of query results beyond a syntactic-level query [14,28]. This framework employs an OWL clause for a query formulation. The query is formalized as an OWL

![](/api/attachments/AW2JXPRG/fulltext/images/9015a173f341351d366b82b09e602754720cd5b50a6db81c94649ab2e909b6ee.jpg)  
% The clause CSchemaSearch1 represents % a rule which gives the name % of a model schema that aims to % optimize something and there is % no intermediate location in the % problem description(i.e., source % and destination locations are % disjoint).  
Fig. 7. Model Schema retrieval rule example (retrieval by an internal view).

non-unit clause, called a query clause of which there are three parts. First, the head serves as a constructor describing the structure of the result element. Second, the body acts as a pattern specifying the interested information to be selected. Last, the optional constraint proceeds as a filter denoting additional Boolean conditions. Given an ODD description P specifying information items along with rules, a query represented by a description Q is evaluated by transforming the description $( P \cup Q )$ until it becomes the description $( P \cup Q ^ { \prime } )$ , where $\mathcal { Q } ^ { \prime }$ consists of only ground unit clauses and the meaning M $( P \cup Q ) = M ( P \cup Q ^ { \prime } \ )$ .

This section presents the common operations: retrieval and composition. An arbitrary integrity constraint is also discussed.

![](/api/attachments/AW2JXPRG/fulltext/images/dc9a9580b4e1039156f56af447bc8713bf695e2682ea5c534301c40ceeb6e9ca.jpg)  
Fig. 8. Modeling of a flow characteristic.

## 6.1. Retrieval

A retrieval operation returns a required component from decision models satisfying given conditions. The ODD query permits selecting various aspects of decision models, i.e., external views, internal views, or a combination of both. The head specifies the resulting elements and the body identifies the matched pattern and constraints.

Following are examples of retrieving model schema and model instance using an internal view.

Example 1. (Retrieval by an internal view. Model schema retrieval). The clause $C _ { \mathrm { S c h e m a S e a r c h 1 } }$ in Fig. 7 demonstrates an example of a rule that gives the name of a model schema that aims at optimizing something and the problem description contains no intermediate location (i.e., source and destination locations are disjoint). The clause $C _ { \mathrm { { C h a r a c t e r i s t i c C h e c k } } }$ in Fig. 8 represents a rule that identifies the characteristic of a transportation flow: if the origin and destination locations of a transportation flow have no member in common (i.e., they are disjoint), the transportation flow has no intermediate location; note that this is one of the characteristics that distinguish the transportation problem from its relatives, such as the transshipment problem. The following query $Q _ { 1 }$ retrieves names of model schemas that aim at minimizing the total cost of shipment and the model should have no intermediate node:

Q : bModelSearch condition=“minimize TransportationCost\_NoIntermediateLocation”N bModelSchemaNameN\$S:ModelSchema

b/ModelSchemaNameN

bMinimizeNTotalCostOfShipmentb/MinimizeN b/ModelSearchN

Since the example Transportation model schema of Fig. 3(c) can match with the body of the rule

ElementLength (\$S:LocationList \$S:LocationCount  
![](/api/attachments/AW2JXPRG/fulltext/images/8dba2e88f406db5a3d5ce463dab51b17783dc0664f363c02fd3bca7f787c74e9.jpg)  
% The clause CSchemaSearch2 represents % a rule which gives the name of an % instance X of a transportation % schema along with a countof % number of its source locations, % and the specified source location % name must be a member ofthe % list Y of those source locations.  
% A list oflocation will be % constructed. The xet:SetOf % constructs the list oflocation % \$E:LocationList based from the % constructor specified with % xet:Constructor.  
IsMember (<SourceLocation><name>\$S:SourceLocationName/name><SourceLocation>. \$E:LocationList.

Fig. 9. Model instance retrieval.

given in Fig. 8 and also satisfies the rule's filtering conditions, a result described by the head of the rule is used by the rule of Fig. 7, which then yields another result shown in the $\varrho _ { \mathrm { a n s l } }$ . The element $\varrho _ { \mathrm { a n s l } }$ would be the answer to the given query, i.e., the TransportationModelSchema:

Q<sub>ans1</sub>:bModelSearch condition=“minimize

TransportationCost\_NoIntermediateLocation”N

bModelSchemaNameNTransportationModelSchemab/ModelSchemaNameN

bMinimizeNTotalCostOfShipmentb/MinimizeN b/ModelSearchN

Example 2 (Retrieval by an internal view. A model instance retrieval). The clause $C _ { \mathrm { S c h e m a S e a r c h 2 } }$ in Fig. 9 retrieves an instance of a Transportation model schema, i.e., a transportation problem of a specific company. The clause employs an ODD Set-of-reference, ElementLength, and IsMember functions to list all source locations, to retrieve a count of its source locations, and to impose a specific location as one of the source locations, respectively. The query Q<sub>2</sub> retrieves an instance of a transportation schema that has Chicago as one of its source locations.

Q :bModelSearch condition=“SpecificSource Location\_and\_LocationCount”N

bModelInstanceN\$S:SomeSchemaInstance b/ModelInstanceN

bNumberOfSourceLocationN

\$S:LocationCountb/NumberOfSourceLocationN

bRequiredSourceLocationNChicagobRequired SourceLocationN

b/ModelSearchN

Fig. 3(d) contains a transportation instance, Havill-Trans, which satisfies the query condition. As a result, the query returns counts of source locations appeared in the HavillTrans as in the clause $\mathcal { Q } _ { \mathrm { a n s } 2 }$

$\varrho _ { \mathrm { a n s } 2 } ^ { }$ :bModelSearch condition=“SpecificSource Location\_and\_LocationCount”N

bModelInstanceNHavillTransb/ModelInstanceN

bNumberOfSourceLocationN3

b/NumberOfSourceLocationN

bRequiredSourceLocationNChicagobRequiredSource-LocationN

b/ModelSearchN

## 6.2. Composition

A composition operation seeks to combine multiple models. This paper classifies this operation into one that simply joins the decision models based on inputs/ outputs, and the other that integrates multiple decision models by excessively modifying the internal structures. The head specifies the composition result and the body presents component decision models, composition rules and constraints.

![](/api/attachments/AW2JXPRG/fulltext/images/70f5e6a875fa8c9dece7344c70d61b102db54bb223483b1981df9682fbcd02d7.jpg)  
Fig. 10. Integrity constraint example (datatype validation).

![](/api/attachments/AW2JXPRG/fulltext/images/76a77f2c6c4c87cfbe61567c7f5686bd88e67978c87c561a6a881631e8146d49.jpg)  
Fig. 11. A prototype system overview.

## 6.3. Integrity constraint

An integrity constraint defines an arbitrary restriction or validation. The head specifies the warning message and the body indicates the detected patterns and constraints.

Example 3 (Validation of datatypes). The clause C in Fig. 10 seeks to validate and report a warning once there exists a wrong data type of Decision Variable for the basic transportation problem. The data type should allow for a non-negative value

![](/api/attachments/AW2JXPRG/fulltext/images/a0487cbbd05058494e8a9355cb8ad6b0a2d3fb34c5a25436329091a585f0ec5d.jpg)  
Fig. 12. A protégé user interface (showing Model Ontology).

![](/api/attachments/AW2JXPRG/fulltext/images/47f875ef597c24ece681e3e2d33d71ccc9e775ce4a58761e6139748f5fb33c7b.jpg)  
Fig. 13. A Web-form for model selection.

because one cannot ship things in negative units. The clause indicates that if the datatype of Decision Variable does not equal &dt;ShipmentQuantityValue, it violates the nature of the logistics (i.e., one cannot ship negative units). The clause $E _ { \mathrm { D a t a t y p e } }$ presents the user-defined datatype &dt;ShipmentQuantityValue which limits values to a numeric greater than or equal to 0, using minInclusive.

![](/api/attachments/AW2JXPRG/fulltext/images/f637b1393e3e87caed00385787565aa47387b0a3074ac9e7632ec41e66935aff.jpg)  
Fig. 14. Query output on Web browser.

## 7. A prototype system

## 7.1. System implementation

A prototype based on the proposed framework has been implemented (Fig. 11). It is available at http:// krwin.cs.ait.ac.th/mmsdss. Asp.net is employed to create Web forms and graphic user interfaces. Protégé [32] is used as an ontology editing tool to create and manage OWL elements representing Model Ontology and Model Schema. The system employs an XML rule language—XML Equivalent Transformation (XET) [2]— as the underlying language for computation, which allows direct, succinct, and efficient reasoning with both implicit and explicit OWL elements without the necessity of data conversion. Note that the implementation simply aims at showing the feasibility of the design framework when incorporated into a modern Web-based XML technology environment; some selected operations are materialized.

The prototype implementation employs Web Services Description Language (WSDL) for the encoding of messages and Simple Object Access Protocol (SOAP) for the transmission of requests to the modelbase server to execute operations. After SOAP transmits a WSDL message containing a request, the system will then subsequently compute the request using its XET engine and reply via a response message showing resulting outputs.

The model-solving is carried out by extracting and expressing instance data in the MathML format in order to be processed seamlessly by a modern mathematical solver that recognizes MathML. Intuitively, the transformation can be done by either using a well-known transformation language for XML, like XSLT, or by using an ODD clause, i.e., the head describes the resulting MathML elements, the body extracts the necessary model schema instance. This implementation employs XSLT. Maple [40], a mathematical application package, is used in this implementation as a mathematical solver.

## 7.2. System usage

The prototype provides basic model retrieval, shows model information, lets users enter numeric data via Web form interfaces, and finally sends model information to a mathematical solver to obtain a solution result. Currently, nine examples of model schemas are available in the model repository just for the purpose of test of concept.

Initially, a model builder creates model ontologies and model schemas by using Protégé (Fig. 12). Note that though RDF graphs are useful for visualization of modelbase items, they may not be suitable for more complex structure and for information maintenance. As a result, Model Ontology and Model Schema are stored in their text versions (i.e., as OWL documents).

![](/api/attachments/AW2JXPRG/fulltext/images/42a24f85301dc20183717da417e6395d013a962699c2c13166b2eec5dab8cc0e.jpg)  
Fig. 15. User interfaces for a model instance execution.

Advanced ontology creation tools like Protégé have advantages over plain editors. They provide more features that facilitate users, e.g., user interfaces for showing an ontology tree, consistency checking of names, conversion from OWL elements to RDF graphs, import of ontologies, and archiving the current version. Those features are also useful to manage changes in Model Ontology and Model Schema.

The system lets an analyst choose decision models via Web form interfaces by (1) selecting a decision objective among optimization, estimation, and computation [24], then (2) choosing a subject of that objective, e.g., total shipping cost or total assignment cost (Fig. 13). An actual modelbase system may provide more search conditions. The search process may be borrowed/ adapted from available research on model section such as [4,24]. Assume the usage scenario whereby a user looks for decision models to optimize total shipping cost (similar to Example 1 of Section 6), the system will process the user's query to retrieve model schemas by looking from the internal view (Model Configuration) and then lists available decision models in the system that meet the user's search condition. The user can then select a specific model schema name to inspect more of its information, i.e., internal and external information of the decision model schema. The screen in Fig. 14 shows the resulting page providing a summary of the Transportation model schema as well as a Scalable Vector Graphics (SVG) graph of the schema.

Next, a decision maker can create a decision model instance via Web forms. The screen in Fig. 15(a,b) provides forms for entering instances for the Transportation model schema; the test data are borrowed from the classical transportation (Hitchcock) problem [42] (original node names are replaced with new location names). The form fill-in sequence for this problem type includes (1) entering the numbers of sources and destinations, (2) entering identification and capacity of sources and destinations (Fig. 15(a)), and (3) entering transportation cost for all flows (Fig. 15(b)).

Finally, model instances will be transformed into MathML and passed to a mathematical solver for obtaining solutions. The screen in Fig. 15(c) provides a user-friendly presentation of solution results obtained from the solver.

## 8. Benefits of the proposed framework

ODDM can satisfy the requirements presented in Section 3 as follows:

(1) Compatibility with Web technologies-By employing ODD—a formal XML-based language deployable on the Web—as a basis, ODDM is compatible with various flavors of XML-based Web technologies such as OWL, RDF, XSLT, and Web services framework.

(2) Support of interoperability—Each component of the framework supports interoperability. First, Model Ontology enables a large degree of interoperability in terms of terminology sharing and reuse for many users and applications by means of reference to the same basic concepts. Second, having such an agreed Model Schema can promote the understanding of the description of a decision model. Different decision model descriptions sharing a common meta-schema can easily exchange or map model items. The meanings of terms used in different decision models are properly defined and easy to be comprehended because they all refer to the terms defined in Model Ontology. Last, model instances that are based on a common model schema can become interoperable even their specific problem contexts are vary because the common model schema guarantees the semantics of items in model instances. Moreover, sharing understanding of information items among the ontology, schema, and instance can be harmoniously performed because they are uniformly encoded under the same representation language.

In the case that different modelbases use OWL as a primitive ontology facility, they will be able to use mapping constructs of OWL to relate the corresponding terms in other modelbases in order to share and reuse information. For example, one modelbase may use the term “Transportation cost” while another “Freight Cost” in their model schemas, but those modelbases can share understanding on the equivalence of the terms by referring to the common Model Ontology. In this case, both terms are costs associated with “Transportation Flow”; thus, they are equivalent. In addition, the framework employs XML and its open-standard technologies. As a consequence, it is extensible to the integration with other information or specifications, especially those described in a specific application markup language family such as MathML and ontologies defined in OWL.

(3) Support of advertisement and discovery of decision models—The two framework components— Model Profile and Model Configuration—together with a formal declarative language lead to the support of announcing decision models. Model

Profile holds external information for a simple advertisement, whence Model Configuration supplies sufficient information for further invocation.

Present mechanisms for the advertisement and discovery of Web services, such as UDDI, which defines a framework for public service registries, and WSDL, which describes the functions of services, provide only the syntactic-level description of the functionality of services. Therefore, they are insufficient for automated machine interpretability of the meaning of semantic annotation statements. Consequently, the present proposed framework does not use a standard registry facility. In the future, as indicated by [3], existing service registries may be enhanced to enable them to handle OWL and ODD statements. With such enhancement, the future service registries will be able to process the semantic components of modelbases, e. g., OWL axioms and Model Ontology constraints. This would lead to semantic search and discovery of decision models and their intelligent execution.

(4) High expressive power—The expressiveness of ODD yields the following benefits. First, the concept of an OWL non-unit clause enables expressing application rules and integrity constraints, and introducing flexibility of system maintenance and query processing. Second, MathML content markup, a de-facto way of expressing standard mathematical notation on the Web, optionally stored in Model Schema, provides an alternative for the readability of mathematical equations by users and machines. Third, ODDM is considered a symbolic subscriptfree language [38]; hence, it provides ease of model formulation and ease of use for those who did not originally create a model to bridge their conceptualizations. Elements related to indexing are primitively defined in Model Ontology and can be later specialized for use in Model Schema. For example, when tracing the elements to the Model Ontology with reference to the use of indexing in the transportation model shown in Fig. 3(c), both SupplyQuantity and DemandQuantity are referred to as IndependentVariable, a kind of Variable. SourceLocation and DestinationLocation are referred to as PrimitiveIndex. TransporationFlow is referred to as CompoundIndex, etc. Last, ODDM is so flexible that a decision model with not-yet-known information can still be stored. Employing an OWL variable, a model builder may either supply such information once it is known or pre-assign sets of enumeration of the possible values to the final users.

(5) Support of model joining and integration— Decision models can be linked at various levels of abstraction. Model Profile pertains to linkage on input/output, when the output of one model becomes the input of another. On the other hand, Model Configuration concerns modifying the internal structure of the multiple models being integrated.

ODDM provides the means for conflict resolution that may occur during those operations. By means of explicit specification of terminology stored in the Model Ontology, naming conflicts can be solved. By means of integrity constraints together with the computation mechanism of ODD, granularity and dimensional/unit of measurement conflicts can be solved.

(6) Model executability—ODDM is equipped with an XET engine that facilitates not only the transformation of the models to suit a solver specific input format but also the extraction of MathML. The justified MathML can then be transparently used in conjunction with a MathMLrecognized solver, such as Maple [40], for obtaining a solution.

## 9. Related works

The representation of modelbases has long been studied and the proposed framework accommodates benefits of existing research. Existing frameworks can be distinguished along two criteria: (1) the focus of content and (2) the representation techniques of decision models. A framework normally employs a combination of an appropriate focus of content and a suitable corresponding representation.

The focus of content leads to five focusing approaches. First the data-centric approach treats information about decision models as data and represents it using a traditional database data model, e.g., the hierarchical [20], the entity-relationship [11], and the relational [37] models. Secondly, the structure-centric approach views a decision model as a definitional system so users can perceive it as the large picture [22,48]. This approach allows more details of problem contexts to be specified than the data-centric approach. Thirdly, the abstraction-centric approach reduces a model's complexity by hiding all but the relevant data. The approach is influenced by an object-oriented paradigm and also adopts object-oriented mechanisms such as an inheritance [35,36]. However, works of [35] and [36] do not focus on Web deployment. The proposed framework supports the positive features of the object-oriented paradigm such as inheritance (e.g. class inheritance and property inheritance) and general ization. Fourthly, the logic-centric approach employs logic-based theory to provide domain axioms and structure of decision models as well as allowing inferences about a model structure [27,33]. The ODD approach also supports this capability by means of ODD clauses. Finally, the computation-centric approach contains algebraic/algorithmic representations as well as emphasizing execution of decision models [12,19,22,29].

The representation techniques of frameworks can be divided into four forms. The graphic form represents, graphically, the relations among parts of a decision model. Diagrams and icons are popular tools for creating this visual perception [11,13,15,22,36]. The text form expresses a decision model in terms of text. A framework may employ a combination of plain text and programming language. The former uses readable plain text to help describe certain information of a decision model, e.g., Structured Modeling Language (SML) [22] contains a plain text description part. The latter either adopts existing programming language such as Prolog or issues a new arbitrary syntax to describe a decision model [12,19,22,29,33]. The algebraic form resembles traditional algebraic notation. It is commonly used as part of a text-based representation. Lastly, the schematic form restricts the structure and content of a decision model to a certain formal schema so that a machine can validate the document structure [18,30,39]. Many frameworks mainly restrict the representation techniques to one form and insufficiently address alternatives to represent decision models in other forms. ODDM provides means to represent modelbase components in various forms: the graphic form by the RDF graph, the text form by the OWL/XML syntax, the math notation form via the MathML, and the schematic form via the formal structure/schema of the description of each modelbase component.

The need for research on modelbases for Web-based DSS has been addressed in [45]. Most aforementioned existing frameworks are not readily adaptable to the current Web technology, partly because they were developed before the Web era. Yet, several frameworks have attempted recently to accommodate Web-related model representation [30,39]. Those attempts advocate the importance and necessity of XML-based technologies and the distributed environment of the Web. However, they utilize only primary merits of XMLbased languages.

Kim [30] aims to promote model sharing by using XML Document Type Definition (DTD) to describe elements of Structured Modeling (SM) [22] but XML DTD itself has limitations, as it is a language for describing XML document syntaxes; and hence is unable to express precise semantics. The framework also insufficiently provides the means for model operations.

Lyer et al. [39] use SM elements as a basis for spreadsheet models. Their work acknowledges the need to access decision models in a distributed environment. Web services architecture is employed to support such an environment. Layers of organization knowledge are classified but knowledge contents and descriptions of decision models are merely represented in a syntactic form. This prevents an opportunity to formally annotate semantic information for further machine processing.

In regard to XML-based modelbase representation, the proposed framework covers all the strengths of the existing approaches and offers some advantages over them. For example, it allows the expression of precise semantics, rules, and axioms. Moreover, it also provides query operations on decision models.

## 10. Conclusions and future works

The paper has presented a formal framework for modelbases, namely ODDM which captures key characteristics of a modern modelbase framework, facilitates the reuse and sharing of decision models, as well as handling both current and future impacts on modelbase representations. The framework yields a declarative specification delivering a user- and machinevocabulary with clear semantics by means of ontology. This XML-based framework also permits an extraction of implicit information embedded in primary information. The framework is elucidated with various exemplars presented in different forms (such as a graphical form), using the transportation problem as an example throughout.

ODD serves as a language that supports the basis of the framework as well as providing means to exploit operations on the framework. ODD facilitates the uniform representation of the two main framework components as well as the query language. The prototype has been implemented to demonstrate the feasibility of the conceptual design supported by widely accepted Web technologies.

Seen as a foundation, the proposed framework raises future works and suggests extensions including, but not limited to: (1) Extending the set of queries and raising an abstraction of query language for modelbases. (2) Expanding terminology in Model Ontology from its primitive seeds. (3) Developing independent user interfaces appropriated for other types of modelbase users. Currently available tools [17] can be integrated into the user interface for a model builder to edit and validate the ontology as well as schema. (4) Enhancing the interchangeability among the Model Schema and other off-the-shelf MathML computation tools once they are mature. (5) Providing a formal procedure to accommodate the mapping of elements in the framework and that of other major existing frameworks.

## References

[1] C. Anutariya, V. Wuwongse, K. Akama, E. Nantajeewarawat, RDF Declarative Description (RDD): a language for metadata, Journal of Digital Information 2 (2) (2001).

[2] C. Anutariya, V. Wuwongse, K. Akama, V. Wattanapailin, Semantic Web modeling and programming with XDD, Proceedings of 1st Semantic Web Working Symposium (SWWS’01), CA, 2001.

[3] D. Asuman, K. Yildiary, L. Gokce, Enhancing ebXML registries to Make them OWL Aware, Distributed and Parallel Databases 18 (2005).

[4] S. Banerjee, A. Basu, Model type selection in an integrated DSS environment, Decision Support Systems 9 (1993).

[5] S. Bechhofer, F. Harmelen, J. Hendler, I. Horrocks, D. McGuinness, P. Patel-Schneider, L. Stein, OWL Web Ontology Language reference, W3C Recommendation 10 February, 2004, http://www.w3.org/TR/owl-ref/.

[6] T. Berners-Less, J. Hendler, O. Lassila, The SemanticWeb, Scientific American 284 (5) (2001).

[7] H. Bhargava, R. Krishnan, The World Wide Web: Opportunities for Operations Research and Management Science, INFORMS Journal on Computing 10 (4) (1998).

[8] H. Bhargava, D. Power, Decision support systems and web technologies: a status report, Seventh Americas Conference on Information Systems, 2001.

[9] H. Bhargava, R. Krishnan, S. Roehrig, M. Casey, D. Kaplan, R. Müller, Model management in electronic markets for decision technologies: a software agent approach, Proceed ings of the 30th Hawaii International Conference on System Sciences, 1997.

[10] M. Binbasioglu, Process-based constructive approach to model building, Decision Support Systems 12 (1994).

[11] R. Blanning, An entity-relationship approach to model management, Decision Support Systems 2 (1986).

[12] A. Brooke, D. Kendrick, A. Meeraus, R. Raman, GAMS: A User's Guide (GAMS Development Corporation, 1998.

[13] J. Choobineh, A diagramming technique for representation of linear models, OMEGA International Journal of Management Science 19 (1) (1991).

[14] J. Choobineh, SQLMP: a data sublanguage for representation and formulation of linear mathematical models, ORSA Journal on Computing 3 (4) (1991).

[15] G. Collaud, J. Pasquier-Boltuck, gLPS: graphical tool for the definition and manipulation of linear problems, European Journal of Operational Research 72 (1994).

[16] DAML Ontology Library, http://www.daml.org/ontologies/.

[17] DAML Tools, http://www.daml.org/tools/.

[18] O. Ezechukwu, I. Maros, OOF: Open Optimization Framework, Departmental Technical Report 2003/7, Imperial College, London, 2003.

[19] R. Fourer, Database structure for mathematical programming models, Decision Support Systems 20 (1997).

[20] R. Fourer, D. Gay, B. Kernighan, AMPL: A Mathematical Programming Language, Management Science 36 (1990).

[21] GAMS model library, http://www.gams.com/modlib/modlib. htm.

[22] A. Geoffrion, An introduction to structured modeling, Management Science 33 (5) (1987).

[23] A. Geoffrion, Indexing in modeling language for mathematical programming, Management Science 38 (3) (1992).

[24] D. Ghosh, R. Agarwal, Model selection and sequencing in Decision Support Systems, Omega, International Journal of Management Science 19 (2/3) (1991).

[25] H. Greenberg, The role of software in optimization and operations research, Encyclopedia of Life Support Systems, Ch. 6.5, 2002, Eolss Publishers, Oxford, UK.

[26] Guide to Available Mathematical software (GAMS), NIST, http://gams.nist.gov.

[27] K. Hiraishi, A constraint logic programming language keyed CLP and its applications to decision making problem in OR/MS, Decision Support Systems 14 (1995).

[28] S. Huh, Q. Chung, A model management framework for heterogeneous algebraic models: object-oriented data base management systems approach, Omega, International Journal of Management Science 23 (3) (1995).

[29] T. Hurlimann, LPL: A Mathematical Modeling Language version 4.42, Working paper, Department of Informatics, University of Fribourg, 2001.

[30] H. Kim, An XML-based modeling language for the open interchange of decision models, Decision Support Systems 31 (2001).

[31] G. Klyne, J. Carroll, Resource Description Framework (RDF): Concepts and Abstract Syntax, W3C Recommendation 10 February, 2004, http://www.w3.org/TR/rdf-concepts/.

[32] H. Knublauch, R. Fergerson, N. Noy, M. Musen, The Protégé OWL Plugin: An open development environment for Semantic Web Applications, Third International Semantic Web Conference- ISWC, 2004.

[33] R. Krishnan, A logic modeling language for automated model construction, Decision Support Systems 6 (1990)

[34] K. Krishnan, K. Chari, Model management: survey, future research directions and a bibliography, Interactive Transactions of ORMS 3 (1) (2000).

[35] O. Kwon, S. Park, RMT: a modeling support system for model reuse, Decision Support Systems 16 (1996).

[36] R. Lazimy, Object-oriented modeling support system: model representation, and incremental modeling, Proceedings of the Twenty-Sixth Annual Hawaii International Conference on System Science, 1993.

[37] T. Liang, Integrating model management with data management in Decision Support Systems, Decision Support Systems 1 (1985).

[38] S. Lin, D. Schuff, R. Louis, Subscript-free languages: a tool for facilitating the formulation and use of models, European Journal of Operational Research 123 (3) (2000).

[39] B. Lyer, G. Shankarakarayanan, M. Lenard, Model management decision environment: a Web service prototype for spreadsheet models, Decision Support Systems 40 (2005).

[40] Maplesoft, http://www.maplesoft.com/.

[41] S. Maturana, Issues in the design of modeling languages for mathematical programming, European Journal of Operationa Research 72 (1994).

[42] NAG Fortran Library Routine Document H03ABF, http://www. nag.co.uk/numeric/fl/manual/pdf/H/h03abf.pdf.

[43] NEOS Guide Optimization Tree, http://www-fp.mcs.anl.gov/otc/ Guide/OptWeb.

[44] D. Power, S. Kaparthi, Building web-based Decision Support Systems, Studies in Informatics and Control 11 (4) (2002).

[45] D. Power, R. Sharda, Model-driven Decision Support Systems: Concepts and Research Directions, Decision Support Systems 43 (2007).

[46] Protégé OWL ontologies, http://protege.stanford.edu/plugins/ owl/owl-library/.

[47] C. Schrlenoff, M. Gruninger, F. Tissot, J. Valois, J. Lubell, J. Lee, The Process Specification Language (PSL) Overview and Version 1.0 Specification, NISTIR 6459, National Institute of Standards and Technology, Gaithersburg, MD, 2000.

[48] T. Sen, K. Chari, A graphical modeling system: application in organizational model management, International Journal of Management Science 25 (2) (1997).

[49] S. Smith, M. Becker, An ontology for constructing scheduling systems, working notes of 1997 AAAI Spring Symposium on Ontological Engineering, Stanford, AAAI Press, CA, 1997.

[50] S. Sridhar, Decision Support using the Intranet, Decision Support Systems 23 (1998).

[51] M. Uschold, M. King, S. Moralee, Y. Zorgios, The enterprise ontology, the knowledge engineering review 13, Special Issue on Putting Ontologies to Use, 1998.

![](/api/attachments/AW2JXPRG/fulltext/images/eedda1de305c03cff5a6fa379ebeac6fe9b09bd6aca2029cb9c3471b06526bc9.jpg)  
Thadthong Bhrammanee is a Doctoral degree candidate in the Computer Science & Information Management Program, School of Engineering and Technology, Asian Institute of Technology, Thailand. She received a B.A. degree in Business Administration from Mahidol University, Thailand, and an M.B. A in Information Systems from the University of Toledo, USA. Her current research interests are in the area of decision support systems, and data and knowledge management.

![](/api/attachments/AW2JXPRG/fulltext/images/fadaa617b9d02f3e400e5dbcfa1ad6fd55227c9f4cb2be69934ce6bf30861c25.jpg)

Vilas Wuwongse is a Professor in the Computer Science & Information Management Program, School of Engineering and Technology, Asian Institute of Technology, Thailand. He received his B. Eng and M. Eng from the Department of Control Engineering, and D. Eng from the Department of Systems Science, Tokyo Institute of Technology, Japan. His research and teaching interests are in the areas of information modeling and representation, and Semantic Web. He pub-

lished in several professional journals such as Journal of Intelligent Information Systems, IEEE Transactions on Knowledge and Data Engineering, and Computational Intelligence.
