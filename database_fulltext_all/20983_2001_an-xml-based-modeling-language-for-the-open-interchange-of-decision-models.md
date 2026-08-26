---
otero_id: 20983
otero_key: "TQV6BYF4"
title: "An XML-based modeling language for the open interchange of decision models"
authors: "HyoungDo Kim"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00093-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An XML-based modeling language for the open interchange of decision models

HyoungDo Kim

Professional Graduate School of Information and Communication, Ajou UniÕersity, 526, 5Ga, NamDaeMoonRo, JoongGu, Seoul 100-095, South Korea

Accepted 6 January 2001

## Abstract

These days, a modeling tool or environment has to know about the others on the market and build bridges to them with which their customers insist on sharing models and data. When it is based on a closed architecture, a tangle of import<sup>r</sup>export point translators is required. Using an exchange standard, we can design an open architecture for the interchange of models and data. XML Extensible Markup Language provides a framework for describing the syntax forŽ . creating and exchanging data structures. The explosive growth of XML-based proposals and standards reflects the urgent requirements and its strength. This paper proposes an XML-based language for sharing models within the MSOR<sup>r</sup>DSS community. The language is able to allow applications and on-line analytic processing tools to models obtained from multiple sources without having to deal with individual differences between those sources. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Open interchange; Decision model; Modeling language; XML

## 1. Introduction

These days, a modeling tool or environment has to know about the others on the market and build bridges to them with which their customers insist on sharing models and data. When it is based on a closed architecture, a tangle of import<sup>r</sup>export point translators is required. Multiple versions of translators and proprietary formats aggravate managing them in a cost-effective manner. With an exchange standard, we can solve the problem by designing an open architecture for the interchange of models and data. XML Extensible Markup Language provides Ž .

a framework for describing the syntax for creating and exchanging data structures. The explosive growth of XML-based proposals and standards such as CML Ž . Chemical Markup Language 42 and MathML<sup>w</sup> <sup>x</sup> Ž . Mathematical Markup Language 24 reflects the <sup>w</sup> <sup>x</sup> urgent requirements and its strength.

This paper proposes a structured markup language, called OOSML Object-Oriented StructuredŽ Markup Language , for the representation and man- . agement of decision models within the MSOR<sup>r</sup>DSS community. The language is based on a conceptual modeling framework, Object-Oriented Structured Modeling OOSM 28 , which is an extension ofŽ . <sup>w</sup> <sup>x</sup> Structured Modeling SM 17 . In contrast to theŽ . <sup>w</sup> <sup>x</sup> previous object-oriented implementations of SM, it is an object-oriented extension to the SM framework itself, where object-oriented concepts and structuring principles such as object-oriented modular structures, models as entities and specialization are supported.

The fundamentals of OOSML are explained in this paper with a realistic and useful Ainitial valueB of what will emerge as a comprehensive and rich collection of modeling capabilities. We expect that the language will evolve very rapidly to become a robust foundation for sharing decision models within the MSOR<sup>r</sup>DSS community. Instead of existing modeling languages such as SML 19,20 , another<sup>w</sup> <sup>x</sup> language is required for the distinctive characteristics that XML can provide: simplicity, extensibility, interoperability and openness. These characteristics can satisfy some new requirements for modeling tools and technologies in the age of the Internet<sup>r</sup>Web. For instance, DecisionNet 3 is such a distributed, Web- <sup>w</sup> <sup>x</sup> based electronic market for decision technologies such as data, models, solvers and modeling environments. Problem-specific input and output data are exchanged via HTML forms, e-mail or the Internet’s file transfer protocols. However, consumers just view the results on the Web or get a results file through the Internet. Another example is DSS Web 40 for<sup>w</sup> <sup>x</sup> analyzing and visualizing data on the web. By employing XML, standard developers can easily cope with dynamic changes in the process of standardization. Developers for a modeling tool or environment can implement and manage a bridge, instead of a set of bridges, in a cost-effective manner with the help of ubiquitous parsers and supporting tools. Users can share their models with others on the Internet<sup>r</sup>Web by distributing them in a standard language.

The rest of the paper is organized as follows. Section 2 discusses the value of an open architecture for the interchange of decision models. Section 3 provides an overview of the OOSML. The potential of the language is discussed in the aspect of model sharing in Section 4. Finally, future research directions are summarized in Section 5.

## 2. Open interchange of decision models

In a closed architecture, a modeling tool or environment has to know about the others on the market and build bridges to them with which their customers insist on sharing models and data. This may produce a tangle of import<sup>r</sup>export point translators as Fig. 1 demonstrates. It is even worse when there are many versions having different release schedules and using proprietary formats. In many cases, a bridge might not exist at all. This leaves users stranded without a way to get their models working together. Furthermore, it does not scale well.

Using an exchange standard, we can design an open architecture for the interchange of models and data, which can improve the shortcomings of the closed architecture. To participate in this architecture, each vendor only needs to add support for the standard to leverage access to all the other tools as Fig. 2 depicts. Having a standard syntax for creating and exchanging data structures is obviously important for this type of integration. XML Extensible Ž Markup Language provides such a framework for . describing the syntax. Furthermore, everyone can participate immediately in a Web-enabled collaborative environment.

XML is a simplified subset of SGML 25 that<sup>w</sup> <sup>x</sup> maintains the SGML features of validation, structure and extensibility. Fig. 3 demonstrates the relationship. SGML allows documents to be self-describing, through the specification of tag sets and the structural relationships between the tags. This specification is referred to as the Document Type Definition Ž . DTD . HTML is a small hard-wired set of about 70 tags and 50 attributes, which allow HTML users to skip the self-describing aspect from a document. XML, on the other hand, retains the key SGML advantage of self-description through DTDs, while avoiding the complexity of full-blown SGML. XML is making rapid progress through standardization process. It has many benefits for folks who want to

![](/api/attachments/TQV6BYF4/fulltext/images/27fda0ac6bb1b93f261d49e654001e558c78b0eda5a6ba363791966042ecc5bc.jpg)  
Fig. 1. A web of point bridges.

![](/api/attachments/TQV6BYF4/fulltext/images/e37ae43016d381052666713a6c8231bb71dbeb69ddc180e437903233943007bc.jpg)  
Fig. 2. Open interchange.

improve structure, maintainability, searchability, presentation and other aspects of their document management. In addition to modifying the syntax and semantics of document tag annotations, XML also changes our linking model by allowing authors to specify different types of document relationships. Furthermore, there is a presentation specification language for XML documents that keep structuring and presentation information separate from actual data. The language XSL Extensible Style LanguageŽ . enables developers to format information more easily for Web viewing. Refer to Refs. 6,14,27,34,46,50<sup>w</sup> <sup>x</sup> for XML details.

Many communities have struggled to codify the tacit knowledge of their data using XML. The explosive growth of XML-based proposals and standards, inclusive of RDF Resource Description Format 33 ,Ž . <sup>w</sup> <sup>x</sup> SMIL Synchronized Multimedia Integration Lan-Ž guage 48 , CML Chemical Markup Language 42 ,. <sup>w</sup> <sup>x</sup> Ž . <sup>w</sup> <sup>x</sup> MathML Mathematical Markup Language 24 , Ž . <sup>w</sup> <sup>x</sup> OFX 9 , ebXML 12 , CDF 13 , OSD 22 , OBI<sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> 43 and OTP 44 , reflects the urgent requirements. The goal of this paper is also to propose such a language for sharing models within the MSOR<sup>r</sup>DSS community. The language is able to allow applications and on-line analytic processing tools to models obtained from multiple sources without having to deal with individual differences between those sources. In addition, it enables combined, collaborative use of a potentially very large number of individual models and proactive administration of collections of models based on business needs as well as mathematical principles. These capabilities are fundamental to effective deployment of decision models in commercial application domains. In the aspect of model sharing, the language is very similar to PMML Ž . Predictive Model Markup Language 10 . PMML<sup>w</sup> <sup>x</sup> provides a quick and easy way for companies to define predictive models and share models between compliant vendors’ applications. A PMML document provides a non-procedural definition of fully trained or parameterized analytic models with sufficient information for an application to deploy them. By parsing it with any standard XML parser, the application can determine the types of data input to and output from the models, the detailed forms of the models and how to interpret their results.

![](/api/attachments/TQV6BYF4/fulltext/images/25e0da2cb9adef5f559bf16bf794405dd6886b76fa612e72f7795f00b7e73054.jpg)  
Fig. 3. XML application process.

Someone may ask why we need another language instead of existing ones such as SML 20,21 , GAMS <sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 7 and AMPL 15 . It can be explained by the distinctive characteristics of XML: simplicity, extensibility, interoperability and openness. XML’s rigid set of rules helps make documents more readable to both humans and machines. XML documents are built upon a core set of basic nested structures. While the structures themselves can grow complex as layers of detail are added, the mechanisms underlying those structures require very little implementation effort. XML is extensible in two senses. First, it allows developers to create their own DTDs, effectively creating ‘extensible’ tag sets that can be used for multiple applications. Basically, XML is a metalanguage that can define a new tag-based language using XML DTD. XML-based standards and proposals are such things that are defined using XML DTDs. Second, XML itself is being extended with several additional standards that add styles, linking and referencing ability to the core XML set of capabilities. As a core standard, XML provides a solid foundation around which other standards may grow. Interoperability means that XML can be used on a wide variety of platforms and interpreted with a wide variety of tools. Because the document structures behave consistently, parsers that interpret them can be built at relatively low cost in any of a number of languages. XML supports a number of key standards for character encoding, allowing it to be used all over the world in a number of different computing environments. Openness means that the standard itself is completely open, freely available on the Web and that anyone can parse a well-formed XML document, and validate it if a DTD is provided.

## 3. OOSML: a structured markup language for sharing decision models

In the fields of MS<sup>r</sup>OR and Decision Support Systems DSS , modeling processes are knowledge- Ž . intensive and time-consuming. Researches on Modeling Environments ME 18,45 and ModelŽ . <sup>w</sup> <sup>x</sup> <sup>r</sup>Modelbase Management Systems MMS 2,5,23,26,Ž . <sup>w</sup> 32,41 are active in order to support the modeling <sup>x</sup> processes and related activities. To implement such an ME or MMS, a conceptual modeling framework is required for representing and managing decision models. Some distinctive frameworks for the purpose are as follows: Structured Modeling SM 17 , Ž . <sup>w</sup> <sup>x</sup> logic-based modeling 2,31 , graph grammar 26 , <sup>w</sup> <sup>x</sup> <sup>w x</sup> object-oriented modeling 23, 41 and frame-based <sup>w</sup> <sup>x</sup> modeling 4,35,36 . They raise modeling to a higher <sup>w</sup> <sup>x</sup> plane of abstraction and generality compared with traditional solvers.

OOSML is based on a conceptual modeling framework, Object-Oriented Structured Modeling Ž . OOSM , which is an extension of SM 17 . Most of<sup>w</sup> <sup>x</sup> object-oriented approaches to SM are in the level of implementation. For example, Lenard 38 uses the<sup>w</sup> <sup>x</sup> inheritance hierarchy of object-oriented programming paradigm to represent a structured model in terms of objects and classes. In implementing an SM language called BLOOMS, Gagliardi and Spera 16<sup>w</sup> <sup>x</sup> extended the definition of the 10th SM core concept Ž . generic structure in the framework of object orientation. Added definition is the following: Genera have their own functionality; Genera of the same type have the same operational behavior. A graphical approach taken by Chari and Sen 8 focus on a<sup>w</sup> <sup>x</sup> model graph for representing a model class. Note that model graphs can have module nodes that encapsulate a sub-graph containing a group of related nodes. Their implementation named GBMS<sup>r</sup>SM supports all the stages of the model development life cycle, which is implemented by an object-oriented language. Another graphical approach by Huh 23 <sup>w</sup> <sup>x</sup> adds some features from the entity-relationship model to the genus graph. In contrast to the previous object-oriented implementations of SM, OOSM is an object-oriented extension to the structured modeling framework itself, where object-oriented concepts are systematically supported by structuring principles such as object-oriented modular structures, models as entities and generalization<sup>r</sup>specialization. Please refer to Kim 28 for the details of OOSM.<sup>w</sup> <sup>x</sup>

Based on the framework, this paper proposes a structured markup language, OOSML. The language is formally defined by a simple XML DTD, which is specified in Fig. 4. An OOSML specification is composed of one model element and any number of instance elements. A ‘model’ element should be composed of one or more elements of ‘model’, ‘entity’, ‘aGenus’, ‘ vaGenus’, ‘fGenus’, or ‘tGenus’. Such a model element has an ‘id’ attribute for uniquely identifying itself in a document. An ‘entity’ element should contain either ‘peGenus’ or ‘ceGenus’. ‘aGenus’, ‘ vaGenus’, ‘fGenus’, or ‘tGenus’ elements can be added to such an entity. A ‘peGenus’ can be empty. That is, it can be used without an end tag, e.g.,<sup>-</sup> peGenus id <sup>s</sup> ’PLANT’<sup>r)</sup>. A ‘ceGenus’ element can contain ‘calls’ elements, whose ‘genus’ attribute identifies

<!ENTITY % nodeAttrs 'id ID #IMPLIED'> <!ENTITY % elementAttrs 'occurs (REQUIRED|OPTIONAL|ONEORMORE|ZEROORMORE) "REQUIRED"> <!ELEMENT oosml (model,instance\*)> <!ELEMENT model (model|entity|aGenus|vaGenus|fGenus|tGenus)+> <!ATTLIST model %nodeAttrs;> <!ELEMENT entity ((peGenus|ceGenus),(aGenus|vaGenus|fGenus|tGenus)\*)> <!ATTLIST entity %nodeAttrs; %elementAttrs;> <!ELEMENT peGenus EMPTY> <!ATTLIST peGenus %nodeAttrs;> <!ELEMENT ceGenus (calls)\*> <!ATTLIST ceGenus %nodeAttrs;> <!ELEMENT calls EMPTY> <!ATTLIST calls genus IDREF #REQUIRED %elementAttrs;> <!ELEMENT aGenus (datatype)> <!ATTLIST aGenus %nodeAttrs;> <!ELEMENT vaGenus (datatype)> <!ATTLIST vaGenus %nodeAttrs;> <!ELEMENT datatype EMPTY> <!ATTLIST datatype dt (R|RP|I|IP|STRING) "RP"> <!ELEMENT fGenus ((calls)+,frule)> <!ATTLIST fGenus %nodeÁttrs;> <!ELEMENT frule EMPTY> <!ATTLIST frule type (SCALE[SHIFT|POWER|MIN|MAX|LN|EXP|VSUM|VPROD|SUM|PROD|DOT) "SUM"> <!ELEMENT tGenus ((calls)+,trule)> <!ATTLIST tGenus %nodeAttrs;> <!ELEMENT trule EMPTY> <!ATTLIST trule type (LE|LT|EQ|GT|GE) "LE"> <!ELEMENT instance ANY> Fig. 4. XML DTD for OOSML.

called genera. ‘aGenus’ and ‘vaGenus’ elements should contain a ‘datatype’ element, of which ‘dt attribute identifies one of predefined data types. A ‘fGenus’ element should contain one or more ‘calls elements and a ‘frule’ element. The ‘type’ attribute of a ‘frule’ element identifies one of predefined functional rules. Similarly, a ‘tGenus’ element should contain a ‘trule’ element.

Let us take the Hitchcock–Koopmans transportation problem 11,17,38 as an illustrative example. <sup>w</sup> <sup>x</sup> The problem can be fully specified by OOSML as in Fig. 5. First of all, a model specification starts with a ‘model’ element, which is the target model to be described. For example, the transportation model is described by the following markup.

$$
\begin{array}{l} <   \text { model } \quad \text { id } = " M \_ T R A N S P O R T A T I O N" > \\ \dots \\ <   / \text { model } > \end{array}
$$

The ‘id’ attribute serves a dual role of identifying the definition, and also naming the specific model class.

A model is an aggregate of other models and entities. The model ‘M TRANSPORTATION’ is an<sub>–</sub> aggregate of ‘E PLANT’, ‘E CUSTOMER’ and<sub>– –</sub> ‘E LINK’. Furthermore, such a model can be de-<sub>–</sub> scribed by attribute genus aGenus , variable at-Ž . tribute genus vaGenus , function genus fGenusŽ . Ž . and test genus tGenus , like any entities. ‘MŽ . <sub>–</sub> TRANSPORTATION’ has ‘Name’ and ‘Creator’ attribute genera.

Entities group aGenus, vaGenus, fGenus and tGenus around peGenus or ceGenus, so they have to contain only one entity genus. The entity ‘E PLANT’ contains four genera, one of which is a peGenus ‘PLANT’. An entity may be required or optional for a model, and may occur multiple times, as indicated by its ‘occurs’ attribute having one of the four values ‘REQUIRED’, ‘OPTIONAL’, ‘ZEROORMORE’ or ‘ONEORMORE’. The default value is ‘REQUIRED’. One or more elements of the entity ‘E PLANT’ should occur in the instances of <sub>–</sub> the model ‘M TRANSPORTATION’. Attribute and<sub>–</sub> variable attribute genera must have a data type of ‘R’, ‘RP’, ‘I’ or ‘IP’, where ‘R’ stands for real values, ‘RP’ for positive real values, ‘I’ for integer values, and ‘IP’ for positive integer values. Attribute genus ‘SUPPLY’ must have a positive real value.

```xml
<?xml version="1.0"?>
<!DOCTYPE oosml SYSTEM "oosml.dtd">
<ooosml>
    <model id="M_TRANSPORTATION">
    <aGenus id="Name">
    <datatype dt="STRING" />
    </aGenus>
    <aGenus id="Creator">
    <datatype dt="STRING" />
    </aGenus>
    <entity id="E_PLANT" occurs="ONEORMORE">
    <peGenus id="PLANT" />
    <aGenus id="SUPPLY">
    <datatype dt="RP" />
    </aGenus>
    <fGenus id="OUTFLOW">
    <calls genus="FLOW" occurs="ONEORMORE" />
    <frule type="SUM" />
    </fGenus>
    <tGenus id="T_SUPPLY">
    <calls genus="OUTFLOW" occurs="REQUIRED" />
    <calls genus="SUPPLY" occurs="REQUIRED" />
    <trule type="LE" />
    </tGenus>
    </entity>
    <entity id="E_CUSTOMER" occurs="ONEORMORE">
    <peGenus id="CUSTOMER" />
    <aGenus id="DEMAND">
    <datatype dt="RP" />
    </aGenus>
    <fGenus id="INFLOW">
    <calls genus="FLOW" occurs="ONEORMORE" />
    <frule type="SUM" />
    </fGenus>
    <tGenus id="T_DEMAND">
    <calls genus="INFLOW" occurs="REQUIRED" />
    <calls genus="DEMAND" occurs="REQUIRED" />
    <trule type="EQ" />
    </tGenus>
    </entity>
    <entity id="T_LINK">
    <ceGenus id="LINK">
    <calls genus="PLANT" occurs="REQUIRED" />
    <calls genus="CUSTOMER" occurs="REQUIRED" />
    </ceGenus>
    <aGenus id="UNITCOST">
    <datatype dt="RP" />
    </aGenus>
    <vaGenus id="FLOW">
    <datatype dt="RP" />
    </vaGenus>
    </entity>
    <fGenus id="TOTALCOST">
    <calls genus="FLOW" occurs="ONEORMORE" />
    <calls genus="UNITCOST" occurs="ONEORMORE" />
    <frule type="DOT" />
    </fGenus>
    </model>
    <instance>...</instance>
</oosml>
Fig. 5. OOSML representation of the transportation problem.
```

Function and test genera can have ‘calls’ elements which explicitly define mathematical dependency on other genera. The ‘genus’ attribute of a ‘calls’ element identifies the genus called by the element. The ‘calls’ elements can also have an ‘occurs’ attribute. Related with the mathematical dependencies, ‘fGenus’ and ‘tGenus’ must have a rule for computation or comparison, respectively. The rule of a function genus has a ‘type’ attribute whose value is among ‘SCALE’, ‘SHIFT’, ‘POWER’, ‘MIN’, ‘MAX’, ‘LN’, ‘EXP’, ‘VSUM’, ‘VPROD’, ‘SUM’, ‘DOT’ or ‘PROD’. Its default value is ‘SUM’. The function genus ‘OUTFLOW’ has a rule type ‘SUM that means summation on the ‘FLOW’ genus. The rule of a test genus has a ‘type’ attribute whose value is among ‘LE’, ‘LT’, ‘GE’, ‘GT’ or ‘EQ’. Its default value is ‘LE’. The function genus ‘T<sub>–</sub>

SUPPLY’ has a rule type ‘LE’ that means ‘less than or equal to’. In most systems and environments based on SM, mathematical knowledge is only embedded in strings, and may be interpreted or compiled for function evaluation. The specification of function genera by factorable functions 37 is an<sup>w</sup> <sup>x</sup> early effort to conceptualize the generic rules in DSS area. Basic principle applied to the language design is to symbolically define the generic rules of function and test genera, and then to infer or constrain other facts based on the mathematical knowledge.

In an OOSML specification, a model instance is defined by an ‘instance’ element. The element can contain any other elements. However, they have to follow the schema defined in the ‘model’ element. For example, Fig. 6 shows the way to define instance elements. All the tag names come from the identifiers of their corresponding schema elements. Agents can validate OOSML model instances using its schema defined in an OOSML specification.

```xml
<instance>
    <Name>DistributionModel</Name>
    <Creator>H.D. Kim</Creator>
    <E_PLANT>
    <PLANT>DALLAS</PLANT>
    <SUPPLY>20,000</SUPPLY>
    </E_PLANT>
    <E_PLANT>
    <PLANT>CHICAGO</PLANT>
    <SUPPLY>42,000</SUPPLY>
    </E_PLANT>
    <E_CUSTOMER>
    <CUSTOMRER>NEWYORK</CUSTOMRER>
    <DEMAND>25,000</DEMAND>
    </E_CUSTOMER>
    <E_CUSTOMER>
    <CUSTOMRER>ATLANTA</CUSTOMRER>
    <DEMAND>15,000</DEMAND>
    </E_CUSTOMER>
    <E_CUSTOMER>
    <CUSTOMRER>LA</CUSTOMRER>
    <DEMAND>22,000</DEMAND>
    </E_CUSTOMER>
    <T_LINK>
    <LINK><PLANT>DALLAS</PLANT><CUSTOMER>NEWYORK</CUSTOMER></LINK>
    <UNITCOST>23</UNITCOST>
    </T_LINK>
    <T_LINK>
    <LINK><PLANT>DALLAS</PLANT><CUSTOMER>ATLANTA</CUSTOMER></LINK>
    <UNITCOST>17</UNITCOST>
    </T_LINK>
    <T_LINK>
    <LINK><PLANT>DALLAS</PLANT><CUSTOMER>LA</CUSTOMER></LINK>
    <UNITCOST>32</UNITCOST>
    </T_LINK>
    <T_LINK>
    <LINK><PLANT>CHICAGO</PLANT><CUSTOMER>NEWYORK</CUSTOMER></LINK>
    <UNITCOST>7</UNITCOST>
    </T_LINK>
    <T_LINK>
    <LINK><PLANT>CHICAGO</PLANT><CUSTOMER>ATLANTA</CUSTOMER></LINK>
    <UNITCOST>23</UNITCOST>
    </T_LINK>
    <T_LINK>
    <LINK><PLANT>CHICAGO</PLANT><CUSTOMER>LA</CUSTOMER></LINK>
    <UNITCOST>30</UNITCOST>
    </T_LINK>
</instance>
```  
Fig. 6. A model instance definition of the transportation problem.

In the past years, two kinds of modeling languages have been intensively studied by researchers: Ž . 1 algebraic languages such as AMPL 15 and <sup>w</sup> <sup>x</sup> GAMS 7 , and 2 SM languages. What makes the<sup>w</sup> <sup>x</sup> Ž . algebraic languages so popular in MS<sup>r</sup>OR community stems almost from the algebraic notation. Some comments and limitations on those languages can be found in Refs. 16, 39 . These motivated the study of<sup>w</sup> <sup>x</sup> the SM framework and variants of SM languages. OOSML can be viewed as a variant of SM, so it has the same benefits with SM languages. Those advantages include wide range of model representation and hierarchical structuring of models. In addition, OOSML adds object-oriented structuring principles into the SM framework. Those principles allow users to classify model components into entities and models that naturally match with users’ view. OOSML is fundamentally different from the other SM languages in that it is based on generalized markups. At least, OOSML inherits the advantages of XML inclusive of the following. 1 It is possible to view or processŽ . OOSML models on the Web. That is, we can transfer the semantics of models into the ubiquitous browsers of users. 2 We can share OOSML DTDŽ . and style sheets through global repositories as in the area of XML<sup>r</sup>EDI 51 . 3 There are many open<sup>w</sup> <sup>x</sup> Ž .

tools and standards such as parsers and DOM 47<sup>w</sup> <sup>x</sup> API for processing OOSML models. So, we can easily build a translator between heterogeneous models, e.g., between GAMS and OOSML models.

## 4. Model sharing

This paper has adopted XML as a meta-language for specifying OOSML, where its characteristics are described using elements and attributes. Although HTML provides a universal way to present information, it only addresses the presentation of data. XML takes this one step further by addressing the context, or meaning of the data. By defining the structure of decision models with XML tags, finding, manipulating, acting on and interacting with the models are much easier. When a user’s agent gets a model that conforms to the syntax and semantics of OOSML, it is able to analyze or manipulate the model easily and correctly. The highly structured delivery of data enables open interchange between servers and clients, and potentially between servers themselves.

In the aspect of model sharing, first of all, users can manipulate OOSML models, downloaded from a Web server, using a Web browser. They can analyze such a model by applying XSL style sheets to it. Fig. 7 demonstrates a simple architecture for sharing OOSML models between a modeling environment and other modeling tools<sup>r</sup>environments. The former is a Web-based integrated modeling environment Ž . WebIME 29 for sharing modeling knowledge on<sup>w</sup> <sup>x</sup> the Web. It is based on a multi-facetted modeling approach to mathematical model representation and management 30 . It includes various syntax-directed<sup>w</sup> <sup>x</sup> editors and graphical tools to support conceptual modeling, mathematical modeling, storage and retrieval, and solution. In the environment, we can generate OOSML models from its model base on the Web. Fig. 8 shows the model instance definition page, where OOSML models can be generated by clicking on the ‘Generate XML’ button. Fig. 9 demonstrates an applet viewer that uses a Java XML parser to display a generated XML document from the transportation model in a tree view.

![](/api/attachments/TQV6BYF4/fulltext/images/4b37f2c03ea921778f7a72d227b98bddaf3c2f83cd4fa9426db0f5cd93e2c56b.jpg)  
XML-Based Model Browsing  
Fig. 7. A simple architecture for OOSML-based model sharing.

In order to integrate modeling tools and environments using OOSML, we need to implement OOSML-aware agents. These agents are required to have four basic components: model access on the Internet<sup>r</sup>Web, OOSML model processing, interfacing with proprietary systems, and model translation. The second one is to manipulate OOSML models using XML technologies including XML, XSL and DOM. On the other hand, the third one is to deliver models to a specific modeling tool or environment. From parsed OOSML models, we can generate proprietary models through various ways using scripts

![](/api/attachments/TQV6BYF4/fulltext/images/1f9f59a863e1ee613c79a9d491b7d262ae8950352efb4d9f0588dd91f0bbddde.jpg)  
Fig. 8. OOSML model generation in WebIME.

```xml
<?xml version="1.0" ?>
<!DOCTYPE oosml (View Source for full doctype...)
- <oosml>
    <model id="M_TRANSPORTATION">
    - <aGenus id="Name">
    <datatype dt="STRING" />
    </aGenus>
    - <aGenus id="Creator">
    <datatype dt="STRING" />
    </aGenus>
    - <entity id="E_PLANT" occurs="ONEORMORE">
    <peGenus id="PLANT" />
    - <aGenus id="SUPPLY">
    <datatype dt="RP" />
    </aGenus>
    - <fGenus id="OUTFLOW">
    <calls genus="FLOW" occurs="ONEORMORE" />
    <frule type="SUM" />
    </fGenus>
    - <tGenus id="T_SUPPLY">
    <calls genus="OUTFLOW" occurs="REQUIRED" />
    <calls genus="SUPPLY" occurs="REQUIRED" />
    <trule type="LE" />
    </tGenus>
    </entity>
    - <entity id="E_CUSTOMER" occurs="ONEORMORE">
```  
Fig. 9. Transportation model in a tree view

and programs. Considering flexible management, XSL-based transformation is a good choice. Fig. 10 shows a part of XSL-based rules for transforming an OOSML model into a GAMS model. Although the sample rule looks very complex, it just identifies a peGenus contained in an entity and then finds all data related with the peGenus. Please refer to 49 for<sup>w</sup> <sup>x</sup> elemental details of XSL. Note that WebIME also implements an agent of the same kind to obtain OOSML models from other modeling tools and environments.

OOSML can be used for sharing decision models on the Internet among heterogeneous modeling tools and environments. Working with an open standardized interchange format makes it possible for modelers to use modeling tools appropriate for their objectives. Assuming that each tool supports an interchange format, we can trade decision models instead of exchanging proprietary models. OOSML is the first trial to propose an open and extensible model exchange format for modeling tools and environments.

In the DecisionNet, a software agent leads a user through a session in which s he supplies requested Ž . data through a series of HTML forms. All the model manipulation and output generation are performed on the server side. This approach limits the role of clients or other servers. One reason for the limitation is related with the automatic generation of model instances from corporate systems and databases. Because a user agent cannot interpret the meaning of the HTML forms, especially without model schema definition, the existing systems on the Web only support model-specific solutions or require that users should have high-level knowledge about modeling language specifics. In the DecisionNet, for example, users have to develop AMPL files. On the other hand, an XML application, WIDL Web InterfaceŽ Definition Language 1 , enables automation of all. <sup>w</sup> <sup>x</sup> interactions with HTML<sup>r</sup>XML documents and forms, providing a general method of representing request<sup>r</sup>response interactions over standard web protocols, and allowing the Web to be utilized as a universal integration platform. It enables interfaces to be described for web sites that are not controlled by calling programs. Instead of interface description, OOSML is used for specifying decision models, whose structure and semantics are contained in its DTD.

```xml
<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">
<xsl:template match="/"/>
<xsl:for-each select="/oosml/model/entity">
<xsl:if test="/peGenus">
SET <xsl:value-of select="@id"></xsl:value-of>
/xsl:for-each select="/oosml/instance/*[.!nodeName()=context(-1)/@id]">
<xsl:value-of selectFAST[.!nodeName()=context(-2)/peGenus/@id]">
</xsl:value-of>
</xsl:for-each>
/;
</xsl:if>
</xsl:for-each>
...
</xsl:template>
</xsl:stylesheet>
```  
Fig. 10. XSL-based transformation rule.

One of the desirable features of a new generation of modeling systems is the independence of model representation and model solution, with model interface standards to facilitate building a library of models and easily accessed solvers for retrieval, systems of simultaneous equations, optimization, and other important manipulations 17 . Logically, two servers <sup>w</sup> <sup>x</sup> for modeling and solving problems may be separate, but existing tools and environments are tightly coupled with specific solvers. OOSML can play the role of a standard language for promoting the open trading of models between servers.

## 5. Concluding remarks

This paper proposes a structured markup language for model representation and management on the Web as an XML application. The language is based on a conceptual modeling framework, OOSM, which is an object-oriented extension of SM. The language supports object-oriented concepts such as object-oriented modular structure, models as entities and specialization using structured markups. Such a language will be a catalyst in trading or integrating models or model-related activities on the Web and transform the Web from a global information space into a universal knowledge network. We demonstrate a simple architecture for OOSML-based model sharing with some implementation details between WebIME and other modeling tools<sup>r</sup>environments. Compared with making a non-XML standard such as SML, OOSML retains the distinctive characteristics that XML can provide: simplicity, extensibility, interoperability and openness. Compared with modeling tools<sup>r</sup>environments based on a closed architecture, ones based on OOSML only need to add support for the standard to leverage access to all the other tools.

Further research directions include the following.

Ž . 1 To standardize such a modeling language through practical reviews and modifications in the

MSOR<sup>r</sup>DSS community. Standardization can remove the need to invent another XML-based modeling language that will invoke excessive overhead for translation, learning, etc. OOSML should evolve into a standard language for decision model representation and management. The standard language will be a catalyst in trading or integrating models or modelrelated activities on the Internet<sup>r</sup>Web.

Ž . 2 To support XML-based modeling on the Web. XML technologies can be applied to modeling work itself to create an OOSML model schema and its instances. Using a model schema represented by the OOSML, for example, a user agent can perform diverse model management activities including form generation for modeling instances interactively on the Web. The highly structured delivery of data enables the agent to present different views of the same information in a cost-effective manner.

## References

<sup>w</sup> <sup>x</sup> 1 C. Allen, WIDL: Application Integration with WIDL, 1997. http:<sup>rr</sup>www.webmethods.com<sup>r</sup>technology<sup>r</sup>widl.html.

<sup>w</sup> <sup>x</sup> 2 H.K. Bhagava, S.O. Kimbrough, On embedded languages for model management, Decision Support Systems 10 3 1993Ž . Ž . 277–299.

<sup>w</sup> <sup>x</sup> 3 H.K. Bhargava, R. Krishnan, S. Roehrig, Model Management in Electronic Markets for Decision Technologies: A Software Agent Approach, Proceedings of HICSS–30, 1997.

<sup>w</sup> <sup>x</sup> 4 M. Binbasioglu, M. Jarke, Domain specific DSS tools for knowledge-based model building, Decision Support Systems 2 3 1986 213–223.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 R.W. Blanning, A relational framework for join implementation in model management systems, Decision Support Systems 1 1 1985 69–82.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 T. Bray, J. Paoli, C.M. Sperberg-McQueen, Extensible Markup Language XML 1.0, 1998. http: Ž . <sup>rr</sup>www.w3.org<sup>r</sup> TR<sup>r</sup>1998<sup>r</sup>REC-xml-19980210.

<sup>w</sup> <sup>x</sup> 7 A. Brooke, D. Kendrick, E. Meeraus, GAMS: A User’s Guide, The Scientific Press, Redwood City, CA, USA, 1988.

<sup>w</sup> <sup>x</sup> 8 K. Chari, T.K. Sen, An implementation of a graph-based modeling system for structured modeling GBMSŽ . <sup>r</sup>SM , Decision Support Systems 22 1998 103–120.Ž .

<sup>w</sup> <sup>x</sup> 9 CheckFree et al., Open Financial Exchange Specification 1.5, 1998. http:<sup>rr</sup>www.ofx.net<sup>r</sup>ofx<sup>r</sup>default.asp.

<sup>w</sup> <sup>x</sup> 10 Data Mining Group, PMML 1.1-Predictive Model Markup Language, 2000. http:<sup>rr</sup>www.dmg.org<sup>r</sup>html<sup>r</sup>pmml v1 .<sub>– –</sub> html.

<sup>w</sup> <sup>x</sup>11 D.R. Dolk, Model management and structured modeling: the role of an information resource dictionary system, Communications of the ACM 31 6 1988 704–718.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 ebXML, Creating a Single Global Electronic Market, 2000, May. http:<sup>rr</sup>www.ebxml.org<sup>r</sup>specindex.htm.

<sup>w</sup> <sup>x</sup> 13 C. Ellerman, Channel Definition Format CDF , 1997, March. Ž . http:<sup>rr</sup>www.w3.org<sup>r</sup>TR<sup>r</sup>NOTE-CDFsubmit.html.

<sup>w</sup> <sup>x</sup> 14 G. Flammia, XML and style sheets promise to make the web more accessible, IEEE Expert 1997 MayŽ . <sup>r</sup>June.

<sup>w</sup> <sup>x</sup> 15 R. Fourer, D.M. Gay, B.W. Kernighan, AMPL: A Modeling Language for Mathematical Programming, Student edn., The Scientific Press, Redwood City, CA, USA, 1993.

<sup>w</sup> <sup>x</sup> 16 M. Gagliardi, C. Spera, BLOOMS: a prototype modeling language with object-oriented features, Decision Support Systems 19 1997 1–21.Ž .

<sup>w</sup> <sup>x</sup> 17 A.M. Geoffrion, An introduction of structured modeling, Management Science 33 5 1987 547–588.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 A.M. Geoffrion, Computer-based modeling environments, European Journal of Operational Research 41 1989 33–43.Ž .

<sup>w</sup> <sup>x</sup> 19 A.M. Geoffrion, SML: a model definition language for structured modeling: Level 1 and 2, Operations Research 40 1Ž . Ž .1992 38–57.

<sup>w</sup> <sup>x</sup>20 A.M. Geoffrion, SML: a model definition language for structured modeling: Level 3 and 4, Operations Research 40 1Ž . Ž .1992 58–75.

<sup>w</sup> <sup>x</sup> 21 S. Hamacher, Modeling Systems for Operations Research Problems: Study and Applications, PhD Dissertation, Industrial Engineering, Ecole Paris Centrale, Paris, 1995.

<sup>w</sup> <sup>x</sup> 22 A. Hoff, H. Partovi, T. Thai, Open Software Description Format OSD , 1997, August. http: Ž . <sup>rr</sup>www.w3.org<sup>r</sup>TR<sup>r</sup> NOTE-OSD.

<sup>w</sup> <sup>x</sup> 23 S.Y. Huh, Modelbase construction with object-oriented constructs, Decision Sciences 24 2 1993 409–434.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 P. Ion, R. Miner, Mathematical Markup Language, 1998, January. http:<sup>rr</sup>www.w3.org<sup>r</sup>TR<sup>r</sup>WD-math.

<sup>w</sup> <sup>x</sup> 25 ISO, Information processing—text and office systems— standard generalized markup language SGML , Standard Ž . 8879 1986 .Ž .

<sup>w</sup> <sup>x</sup> 26 C.V. Jones, An introduction to graph-based modeling systems: Part I. Overview, ORSA Journal of Computing 2 2Ž . Ž . 1990 180–206.

27 R. Khare, A. Rifkin, XML: a door to automated web applications, IEEE Internet Computing 1997 July–August.Ž .

<sup>w</sup> <sup>x</sup> 28 H.D. Kim, Metaview Approach to the Development of DSS Modeling Environments, PhD Dissertation, KAIST, TaeJon, Republic of Korea, 1992.

<sup>w</sup> <sup>x</sup> 29 H.D. Kim, J.W. Kim, S.J. Park, WebIME: an web-based integrated modeling environment for multi-facetted model representation and management, International Journal of Management Science 1999 May.Ž .

<sup>w</sup> <sup>x</sup> 30 J.W. Kim, H.D. Kim, S.J. Park, Multi-facetted approach to mathematical model representation and management, Journal of the KORMS 23 2 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 R. Krishnan, PDM: a knowledge-based tool for model construction, Decision Support Systems 7 4 1991 301–314.Ž . Ž .

<sup>w</sup> <sup>x</sup> 32 O.B. Kwon, S.J. Park, RMT: a modeling support system for model reuse, Decision Support Systems 16 2 1996 131– Ž . Ž . 154.

<sup>w</sup> <sup>x</sup> 33 O. Lassila, Resource Description Framework RDF , 1998,Ž . February. http:<sup>rr</sup>www.w3.org<sup>r</sup>RDF.

34 A. Layman et al., XML-Data, 1998, January. http:<sup>rr</sup>www. w3.org<sup>r</sup>TR<sup>r</sup>1998<sup>r</sup>NOTE-XML-data.

<sup>w</sup> <sup>x</sup> 35 J.K. Lee, M.Y. Kim, Knowledge-assisted optimization model formulation: UNIK-OPT, Decision Support Systems 13 2Ž . Ž . 1995 111–132.

<sup>w</sup> <sup>x</sup> 36 J.S. Lee, Structure Frame Based Model Management System, Doctoral Dissertation, University of Pennsylvania, USA, 1989.

<sup>w</sup> <sup>x</sup> 37 M.L. Lenard, Representing models as data, Journal of Management Information Systems 2 4 1986 36–48.Ž . Ž .

<sup>w</sup> <sup>x</sup> 38 M.L. Lenard, An object-oriented approach to model management, Decision Support Systems 9 1993 67–73.Ž .

<sup>w</sup> <sup>x</sup> 39 S.V. Maturana, Issues in the design of modeling languages for mathematical programming, European Journal of Operational Research 72 2 1994 243–261.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 MicroStrategy, MicroStrategy: A Leading Worldwide Provider of Enterprise DSS Software, http:<sup>rr</sup>www.strategy.com Ž . 1998 .

<sup>w</sup> <sup>x</sup>41 W.A. Muhanna, An object-oriented framework for model management and DSS development, Decision Support Systems 9 1 1993 217–229.Ž . Ž .

<sup>w</sup> <sup>x</sup> 42 P. Murray-Rust, Chemical Markup Language CML 1.0, Ž . 1997, January. http:<sup>rr</sup>www.venus.co.uk<sup>r</sup>omf<sup>r</sup>cml<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 43 OBI Consortium, Open Buying on the Internet OBI Techni- Ž . cal Specifications Release V1.1, 1998. http:<sup>rr</sup>www. openbuy.org<sup>r</sup>obi<sup>r</sup>library<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 44 OTP Consortium, Open Trading Protocol, 1998. http:<sup>rr</sup> www.otp.org.

<sup>w</sup> <sup>x</sup> 45 S.J. Park, H.D. Kim, Constraint-based metaview approach for modeling environment generation, Decision Support Systems 9 4 1993 325–348.Ž . Ž .

<sup>w</sup> <sup>x</sup> 46 J. Tauber, XML after 1.0: you ain’t seen nothing yet, IEEE Internet Computing 1999 May–June. Ž .

<sup>w</sup> <sup>x</sup> 47 W3C, Document Object Model DOM Level 1 Specifica-Ž . tion, 1998, October. http:<sup>rr</sup>www.w3.org<sup>r</sup>TR<sup>r</sup>REC-DOM Level-1<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 48 W3C, Synchronized Multimedia Integration Language Ž . SMIL 1.0 Specification, 1998, June. http:<sup>rr</sup>www.w3.org<sup>r</sup> TR<sup>r</sup>REC-smil.

<sup>w</sup> <sup>x</sup> 49 W3C, XSL Transformations XSLT Version 1.0, 1999,Ž . November. http:<sup>rr</sup>www.w3.org<sup>r</sup>TR<sup>r</sup>xslt.

<sup>w</sup> <sup>x</sup> 50 W3C, XML Schema Part 0: Primer, 2000, April. http:<sup>rr</sup> www.w3.org<sup>r</sup>TR<sup>r</sup>xmlschema-0<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 51 XML<sup>r</sup>EDI Group, XML<sup>r</sup>EDI, 1998. http:<sup>rr</sup>www. xmledi.com.

![](/api/attachments/TQV6BYF4/fulltext/images/1ffdc742c1e753e870d7de50fd9c3a8e52092050d5b5b1d66e81366d601e483c.jpg)

HyoungDo Kim is an assistant professor of the Professional Graduate School of Information and Communication, Ajou University. He received his MS 1987Ž . and PhD 1992 degrees from the De-Ž . partment of Management Science, Korea Advanced Institute of Science and Technology KAIST . He received his Ž . BS degree from the Department of Industrial Engineering, Seoul Nationa University. From 1993 to 1999, he worked for a telecommunication com-

pany in the research of EC Electronic Commerce and InternetŽ . services. His current research interests include object-oriented modeling and simulation, workflow support, personalized multimedia services, data mining and XML-based B2B applications.
