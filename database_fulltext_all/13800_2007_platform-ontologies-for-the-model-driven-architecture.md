---
otero_id: 13800
otero_key: "MPPB9C2M"
title: "Platform ontologies for the model-driven architecture"
authors: "Dennis Wagelaar; Ragnhild Van Der Straeten"
year: "2007"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000686"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Platform ontologies for the model-driven architecture

Dennis Wagelaar<sup>1</sup> and Ragnhild Van Der Straeten<sup>1</sup>

<sup>1</sup>System and Software Engineering Lab, Vrije Universiteit Brussel, Brussels, Belgium

Correspondence: Dennis Wagelaar, System and Software Engineering Lab, Vrije Universiteit Brussel, Pleinlaan 2, Brussels 1050, Belgium.

Tel: þ 32 2 629 2974;

Fax: þ 32 2 629 2870;

E-mail: dennis.wagelaar@vub.ac.be

## Abstract

The model-driven architecture enables the deployment of software applications on different platforms. It is based on a pattern in which a platform-independent model is transformed into a platform-specific model, given a platform model (PM). Currently, the model transformations used for this task implicitly assume this PM, which makes it unclear whether a model transformation can be used for platforms other than the one assumed. In order to target very specific platforms and platform variants, model transformations must be reusable beyond their assumed platform. We propose an explicit PM that can be used to reason about platform dependencies of model transformations and their applicability to specific platforms. In addition, we show how PMs can be integrated in a model-driven configuration management framework. European Journal of Information Systems (2007) 16, 362–373.

doi:10.1057/palgrave.ejis.3000686

Keywords: model-driven architecture; ontologies; description logic; domain-specific modelling; configuration management

## Introduction

The model-driven architecture (MDA) allows for ‘separating the specification of the operation of a system from the details of the way that system uses the capabilities of its platform’ (Miller & Mukerji, 2003). This enables the deployment of software applications on a variety of different platforms. The MDA is based on a pattern that involves modelling the software in a platform-independent model (PIM). This PIM should then be transformed to a platform-specific model (PSM), given a platform model (PM). Currently, models are transformed directly from PIM to PSM, without using a PM. The model transformations implicitly assume a PM. This makes it much easier to write model transformations, as one only has to deal with the limited scope of targeting a single, assumed platform. It is unclear, however, whether a model transformation can be used for platforms other than the one for which it was written. The only safe assumption is that each targeted platform requires its own corresponding set of model transformations.

In practice, this means that only a relatively small number of general platforms can be targeted, for example, Java or C þ þ . Targeting very specific platforms, for example, Qtopia Palmtop Environment (http://www.trolltech.com/products/qtopia/) or J2ME personal profile (PP) 1.0 (http://java.sun.com/products/personalprofile/), is not feasible due to the maintenance overhead, even though such precise targeting can result in a better-optimised PSM in terms of memory footprint, available features, etc. Especially in a world where constrained computing devices become more commonplace every day (Ducatel et al., 2001), getting the most out of such a platform is very important.

On the other hand, most model transformations are reusable over multiple platforms and it is only how they are combined that makes them applicable to only one specific platform. For example, one model transformation could target all Java 2 platforms by transforming the types of UML properties (OMG, 2005) with a multiplicity greater than one to Java using the Java 2 Collections framework. The Java 2 Collections framework is included in several Java platforms, including J2ME PP and J2SE for the desktop computer (http://java.sun.com/j2se/). If this transformation is applied in combination with a transformation that targets the Java Swing graphical user interface framework, the target platform is already limited to J2SE. Owing to the fact that each configuration of model transformations is also maintained by hand, the problem of limited platform support remains.

We propose a separate PM, which can be used to automatically select and configure a number of reusable model transformations for a given platform. This PM is expressed in the web ontology language (OWL) (Smith et al., 2004), which is an extensible language for describing ontologies. We use the OWL–DL variant, which corresponds to description logic (Baader et al., 2003) and allows us to apply automatic reasoning. This PM forms a basis for describing platforms in general and can be extended to include the specific platform information that is relevant for a particular application domain. One or more platform constraints can be defined for each model transformation. This way, the model transformations are no longer limited to one platform, but can instead be used for a well-defined class of platforms. Concrete platforms are modelled separately and refer to the same basis PM. An automatic reasoner, such as Racer (Mo¨ller & Haarslev, 2003), can be used to verify whether a concrete platform satisfies the platform constraints of a model transformation. In addition, it can determine which platform constraint forms the closest match to a concrete platform, allowing for optimisation towards a concrete platform.

To bring the model transformations and PMs together, we propose to augment an existing technique for configuration management with PMs. Domain-specific modelling (DSM) (Ledeczi et al., 2001; Tolvanen & Rossi, 2003) is a technique that can be used to model software configurations (Wagelaar & Van Der Straeten, 2006). Software configurations are described in a DSM language – a configuration language in our case. The configuration rules are typically represented by the configuration language meta-model. DSM lies close to MDA in that it also uses model transformation to generate an implementation of a high-level model. In the case of a configuration model (CM) for model transformations, such a generated implementation can take the form of a build script that applies the configured model transformations.

As the configuration of an MDA-based build framework involves the choice of model transformations, these model transformations are represented in the configuration language meta-model as meta-classes. We annotate each of these meta-classes with one or more platform constraints. In this way, we can determine the platform constraints for each model transformation, but also for each configuration – or combination – of model transformations. This is done by reflection on the meta-classes that have been used to define a CM. An automatic reasoner can be used to determine which configuration of model transformations forms the closest match to a concrete platform. It can also verify whether a concrete platform satisfies a configuration of model transformations.

The rest of this paper is structured as follows: first, we explain in detail how platform ontologies can be modelled. Then, we introduce a case study of a software application that is targeted to multiple platforms. Next, we discuss how configuration management can be carried out using DSM techniques and how the platform ontologies can be used in conjunction with CMs. Tool support for the proposed approach is discussed in the following section. The next section discusses related work, and the conclusions and future work are discussed in the last section of this paper.

## Platform modelling

In order to reason about platforms and platform constraints, an ontology of platforms is used. Ontologies can serve as a common vocabulary for a domain (Gruber, 1993). The relationships between the ontology elements can be used to reason about elements based on that ontology, even if those elements are not related directly. A platform ontology allows one to base expressions about a platform on the vocabulary expressed by the ontology. By using a common model of platforms, we can reason about the relationship between a platform description and a platform constraint, even if the two do not have a direct relationship. An example platform constraint is that the Java 2 Collections framework needs to be present. An example of a platform description is a Sharp Zaurus hand-held computer. As both the platform constraint and the platform description refer to the platform ontology to explain what the Java 2 Collections framework and the Zaurus hand-held computer are, one can derive whether the Zaurus hand-held computer platform satisfies the Java 2 Collections framework constraint.

## A platform vocabulary

Before modelling any specific platform properties, a basic structure needs to be defined, into which platform extensions can be fitted. A predefined ontology is used for describing context (Preuveneers et al., 2004), which includes the platform. The platform is defined as the context in which the software must run, as opposed to the context of the user. Note that we use a more recent version of the context ontology in this paper. The part of the ontology that models platforms is shown in Figure 1. The full ontologies used in this paper can be found at http:// ssel.vub.ac.be/ssel/research:mdd:platformkit:ontologies.

OWL Ontologies basically provide concepts, properties and instances. A concept represents a set of instances, much like an object-oriented class. A property describes a relationship of a concept with another concept (or primitive type), similar to an object-oriented class attribute. Instances are like objects in that they are an instance of a concept and can be related to other instances according to the properties defined for its concept.

The ‘Platform’ concept in this ontology can provide ‘Features’, which can take the form of ‘Software’ or ‘Hardware’. This is denoted by the ‘providesFeature’ property. A ‘\*’ next to the property names denotes a one-to-many relationship. ‘Software’ and ‘Hardware’ are broken down into different sub-concepts as indicated by the special isa subsumption relationship. The set of operating systems, for example, subsumes the set of software in general. Features can require other features, for example, the need for a particular ‘VirtualMachine’ or a user interface ‘RenderingEngine’ that supports voice communication. This is denoted by the ‘requiresFeature’ property, which represents the transitive closure of required features.

The ontology can be extended for particular subdomains of platform, such as Java runtime environments (JREs). Figure 2 shows part of such an ontology. ‘JRE’ is a sub-concept of ‘Software’. ‘Software’ is prefixed by ‘platform:’ to indicate it refers to the ‘Software’ concept from the main platform ontology (see Figure 1): the ‘platform:’ prefix refers to the XML namespace ‘platform’, where the ‘:’ serves as a namespace delimiter. A ‘JRE’ consists of a virtual machine and a built-in class library, denoted by the ‘providesJavaVM’ and ‘providesBuiltinJavaLibrary’ properties. A ‘JavaVM’ can support one or more of the various existing bytecode formats (‘supportsBytecode Format’).

As the most important difference between the various JREs lies in the built-in class library from the point of view of a software engineer, we focus on the Java class library APIs. Each particular JRE complies with a particular Java specification, such as JDK 1.1, J2SE 1.5, J2ME PP 1.0, etc. Each of these specifications has their own class library API. The differences between these APIs are significant enough to justify a separate ontology for each

![](/api/attachments/MPPB9C2M/fulltext/images/2c56f1c285786aac573a8e7a973f9d9197f02b8ab7122e9a6e057438ad473d50.jpg)  
Figure 1 Partial view of the context ontology for describing platforms.

JRE specification. Figure 3 shows part of the ontology for the J2ME (PP) version 1.0 specification.

The J2ME PP 1.0 ontology provides specific JRE and class library concepts: ‘J2me-pp-1\_0JRE’ and ‘J2me-pp-1\_0ClassLibrary’. The ‘providesBuiltinJavaLibrary’ property from the Java ontology is restricted such that instances of ‘J2me-pp-1\_0JRE’ can only provide instances of ‘J2me-pp-1\_0ClassLibrary’ as a built-in class library. All Java packages that are part of the built-in class library are represented as separate concepts. The ‘JavaAwtLibrary’ concept, for example, represents the class of all Java libraries that implement the java.awt package of the J2ME PP 1.0 API. As ‘J2me-pp-1\_0ClassLibrary’ represents the set of all Java libraries that implement the full J2ME PP 1.0 API, it subsumes all package library concepts.

The reason why all API packages are represented as separate concepts is to be able to specify overlap in the APIs of different JRE specifications. A simplified version of the ‘JavaxMicroeditionIoLibrary’, for example, is also part of the J2ME mobile information device profile (MIDP) 1.0 API. The J2ME PP 1.0 version of ‘Javax MicroeditionIoLibrary’ is modelled as a sub-concept of ‘JavaxMicroeditionIoLibrary’ in the J2ME MIDP 1.0 ontology, which is prefixed by ‘midp:’. The same situation applies for ‘JavaUtilLibrary’.

![](/api/attachments/MPPB9C2M/fulltext/images/494a7d90ff1f51e31ad986bfc55ac4968cdf165525cc55104d4b3e9c4ef2c6e9.jpg)  
Figure 2 Partial view of an ontology for describing JREs.

![](/api/attachments/MPPB9C2M/fulltext/images/70b52fa889e8325504c1a3bd4fce30961b0930ebc95970c3fe0bbbbb5676d090.jpg)  
Figure 3 Partial view of an ontology for describing the J2ME PP 1.0 specification.

## Modelling concrete platforms

Given the base platform ontology and the extensions for the relevant domains, we can model concrete platforms as ontology instances. The Sharp Zaurus PDA, for example, has a J2ME PP 1.0 JRE. The ontology that describes this is shown in Figure 4.

The concepts ‘Platform’, ‘J2me-pp-1\_0JRE’ and ‘J2mepp-1\_0ClassLibrary’ are taken from the platform and J2ME PP 1.0 ontologies. The instances, ‘zaurusC860’, ‘zaurusJRE’ and ‘zaurusClassLibrary’, are depicted as rounded rectangles and are instances of the ‘Platform’, ‘J2me-pp-1\_0JRE’ and ‘J2me-pp-1\_0ClassLibrary’ concepts. This is depicted by the io (instance of) relationships. The ‘zaurusC860’ platform has a ‘providesFeature’ relationship with the ‘zaurusJRE’ JRE and the ‘zaurusClass Library’ Java class library. Finally, ‘zaurusJRE’ has a ‘providesBuiltinJavaLibrary’ relationship with ‘zaurus ClassLibrary’ to indicate that ‘zaurusClassLibrary’ is part of the ‘zaurusJRE’.

## Modelling platform dependencies

Platform dependencies can be modelled by defining new, completely specified concepts. Such concepts have necessary-and-sufficient constraints in addition to any necessary constraints. A necessary constraint is depicted by the isa relationship: whereas it is necessary that each ‘J2me-pp-1\_0JRE’ instance is also an instance of ‘JRE’, being a ‘JRE’ instance is not sufficient for also being a ‘J2me-pp-1\_0JRE’ instance (see Figure 3). We will use the notation for describing conditions as used in the Prote´ge´ ontology editor (http://protege.stanford.edu/), which is one of the most popular ontology editors. A constraint that requires a platform with a J2ME PP 1.0 ‘JavaAwtLibrary’ can be defined as a concept ‘JavaAwtPlatform’, which is a subconcept of ‘Platform’ (necessary) and provides a ‘JavaAwt Library’ as defined by the J2ME PP 1.0 ontology (necessary-and-sufficient):

$$
\begin{array}{r c l} \text {JavaAwtPlatform} & \sqsubseteq & \text {platform: Platform} \\ & \equiv & \text {platform: providesFeature} \\ & & \text {pp: JavaAwtLibrary} \end{array}
$$

Whenever a ‘Platform’ instance fulfils the condition of providing a ‘JavaAwtLibrary’, it can be classified as an instance of ‘JavaAwtPlatform’. This classification can be performed by automatic reasoners. This way, concrete platform instances can be matched against a completely defined constraint concept. If a platform description ontology instance classifies as an instance of the constraint concept, then the constraint holds for that instance. For example, the ‘zaurusC860’ platform from Figure 4 classifies as an instance of ‘JavaAwtPlatform’, as ‘zaurusClassLibrary’ is an instance of ‘J2me-pp-1\_0ClassLibrary’, which is a sub-concept of ‘JavaAwtLibrary’ (see Figure 3).

## Case study

An MDA case study has been developed to evaluate our platform modelling approach (see http://ssel.vub.ac. be/ssel/research:mdd:casestudies:im). This case study uses the example of an instant messaging client. The instant messaging client is modelled in UML as a PIM. In this case, platform-independent means that the PIM can still be refined towards any Java-based platform and is as such independent from any specific Java platform (e.g. J2SE 1.3 or J2ME MIDP 1.0). It has several optional features, which are modelled in separate, semi-platformspecific UML models. Several model transformations are used to translate high-level design elements into platform-specific elements, resulting in a PSM. Finally, code is generated from the PSM. All model transformation and code generation is carried out using the ATLAS transformation language (ATL) (Jouault & Kurtev, 2005).

![](/api/attachments/MPPB9C2M/fulltext/images/4e98806e2c8e93d2af0d4f47094b1378de068571236046bc8ecd32562b6a063f.jpg)  
Figure 4 Partial platform description for the Sharp Zaurus SL-C860 PDA.

![](/api/attachments/MPPB9C2M/fulltext/images/4b99ec07f20e7fb3d0f9f61b11b66264a4350e77c20345656c14c85a3f8256e6.jpg)  
Figure 5 Partial PIM class diagram for a simple instant messaging client.

Figure 5 shows the UML class diagram of part of the PIM. The instant messaging client is able to send and to receive messages over different kinds of networks (e.g. Jabber/Internet or SMS). It also keeps a list of contacts for each supported network and a list of active conversations. The design is split up into a model, edit, view and networking part, each in their own package. Concrete view and network types are considered optional features and are specified in separate models.

The PIM contains several elements that are not available in the Java programming language environment used for the target platform. These elements are the ‘Applet’, ‘Observer’, ‘Observable’, ‘subscribe’ and ‘Singleton’ stereotypes, the ‘String’, ‘Integer’, ‘Exception’ and ‘OclAny’ data types and public properties without accessor operations (‘getters’ and ‘setters’). Model transformations are used to translate each of these elements to one or more elements that are available in the target programming environment.

A simplified excerpt of the model transformation that introduces accessor operations for each public property is shown below:

```swift
rule PublicPropertyCollection {
    from s : UML2!Property (
    (s.visibility = #public) and s->isNavigable() and not s->isSingle() and not s.isOrdered)
    using {
```

```txt
baseNameS : String = s->accessorBaseNameS(); }
to t : UML2!Property mapsTo s (...),
    getOp : UML2!Operation (
    name <- 'get' + baseNameS,
    class <- s.class,
    visibility <- s.visibility,
    isStatic <- s.isStatic,
    ownedParameter <- Sequence{getPar}),
    getPar : UML2!Parameter (
    name <- 'return',
    lowerValue <- getParLow,
    upperValue <- getParUp,
    type <- s.type,
    effect <- #read,
    direction <- #return),
    getParLow : UML2!LiteralInteger (
    value <- s->lower(),
    getParUp : UML2!LiteralUnlimitedNatural (
    value <- s->upper(),
    getBehavior : UML2!OpaqueBehavior (
    specification <- getOp,
    name <- getOp.name + 'Behavior',
    language <- Sequence{thisModule.language},
    body <- Sequence{s->getter()}),
    ...
    )
}

helper context UML2!Property
def : getter() : String =
    if self->isSingle() then self.name->getterBody()
    else self.name->multiGetterBody() endif;
```

This transformation rule introduces a ‘getter’ operation for each public, multiple, non-ordered and navigable property. The ‘getter’ helper method is used to create the method body for this operation. This helper method calls the ‘multiGetterBody’ helper method that is contained in a separate platform-specific library:

```typescript
helper context String
def : multiGetterBody() : String = self->javaMultiGetterBody();

helper context String
def : javaMultiGetterBody() : String = 'return' + self + '.elements();';
```

The helpers shown above assume that the java.util.- Vector class is used to implement multiple properties in Java. This class has an elements( ) method that returns a java.util.Enumeration object. Another implementation of this platform-specific library uses the following helper code:

```txt
helper context String
def : javaMultiGetterBody() : String = 'return new IteratorEnumerationAdapter(' + self + '.iterator());';
```

This implementation of ‘javaMultiGetterBody’ assumes that the java.util.Collection interface is used to implement multiple properties in Java. As this class has no method that can return a java.util.Enumeration, an adapter class is used that wraps the native java.util.Iterator object inside a java.util.Enumeration object.

This example model transformation with its alternative library implementations shows how and where platform constraints are introduced into the model. While java.util.Vector is available in all Java platforms, java.util.Collection is only available in Java platforms that support the Java 2 Collections Framework. Whereas J2ME PP 1.0 does support this, J2ME MIDP 1.0 does not: hence, the solution that uses java.util.Collection requires at least the JavaUtilLibrary defined by J2ME PP 1.0 (see Figure 3)

## Configuration management

In order to manage which models, model transformations, etc. to use when building our software, we define a DSM language for expressing configurations. The structural definition (abstract syntax) of this language is given in a meta-model. For the instant messaging case study, this meta-model is split up in a part for configuring the model transformations and their libraries and a part for configuring the specific instant messaging features. In this paper, we will focus on the part of the meta-model that is concerned with the configuration of the model transformations.

Figure 6 shows the meta-model of the configuration options for the model transformations. Each configuration starts with an instance of the ‘Transformation-Config’ meta-class. Among the configuration options are alternative model transformations (e.g. ‘UML2Applet’ or ‘UML2MIDlet’) and programming language mapping libraries (e.g. ‘JavaMapping’, ‘Java1DataTypes’).

Note that the configuration meta-model (CMM) does not represent all available model transformations: only the model transformations that can vary over different configurations are part of the CMM, whereas the model transformations that are common for each configuration are left out of the CMM. The model transformation from the previous section that introduces accessor operations, for instance, is not represented in the CMM. This is because it is always included when building the instant messenger software. The developer does not need to model it as part of the configuration.

This kind of knowledge, which is common for each configuration, is contained inside a model transformation that maps CMs to an implementation. The implementation we used for our CMs is an Ant ‘build.xml’ script. Ant scripts are the Makefile equivalent for Java-based software development: they execute the different steps required for building and/or packaging the software.

Part of the ATL transformation that creates the ‘build.xml’ XML model from a CM is shown below:

```txt
rule ConfigRoot {
    from s : CMM!TransformationConfig
    -- <project name="s.buildPath">
    to root : XML!Root mapsTo s (
    name <- 'project',
    children <- s->contents(),
    name : XML!Attribute (
    parent <- root,
    name <- 'name',
    value <- s.buildPath)
}
```

```txt
Sequence{
    thisModule->UML2Profiles(self),
    thisModule->UML2Accessors(self),
    self.observer->observer(),
    thisModule->UML2AbstractFactory(self),
    thisModule->UML2Singleton(self),
    self.applet->applet(),
    thisModule->UML2AsyncMethods(self),
    thisModule->UML2DataTypes(self),
    thisModule->Generate(self),
    thisModule->Transform(self),
    thisModule->LoadBaseModels(self),
    thisModule->AllBase(self)
};
```

Note that the order of execution is part of the configuration knowledge that is contained in this model transformation. All build targets are added in order, with specially typed helper methods for the variable model transformations. Below is an example of the specially typed helper methods for the ‘UML2Observer’ and ‘UML2JavaObserver’ transformations:

![](/api/attachments/MPPB9C2M/fulltext/images/fc708a09b2462cad49f081279e91d842e5c3675235d06082872e96fed508c35f.jpg)  
Figure 6 Meta-model of the model transformation configuration language.

```txt
helper context CMM!UML2JavaObserver
def : observer() : XML!Node =
    thisModule->UML2JavaObserver(self.config);
helper context CMM!UML2Observer
def : observer() : XML!Node =
    thisModule->UML2Observer(self.config);
```

If the CM uses an instance of the ‘UML2JavaObserver’ meta-class, the first helper method is invoked. Otherwise, the second helper method is invoked. This example shows how the varying parts of the configuration are read from the CM and translated into the corresponding implementation. The result of this transformation is a ‘build.xml’ file that executes the applicable model transformations according to the common, fixed configuration knowledge and the varying configuration knowledge inside the CM.

## Platform-aware configuration

In order to leverage the PM in the configuration process, a link has to be made from the configuration language to the PM. When looking at the configuration language meta-model shown in Figure 6, it becomes apparent that each concrete meta-class can impose certain platform constraints. Whenever a particular feature is included at least once in a CM, the platform constraints of that type of feature – or meta-class – apply. Hence, a link to the PM is made for each meta-class. It then becomes possible to trace back the platform constraints for each CM through the meta-model of the configuration language.

In the Eclipse Modeling Framework (EMF) (Budinsky et al., 2003), it is possible to create annotations for each model element. Annotations are grouped by name and can contain multiple key-value pairs. In our CMMs, a ‘PlatformKit’ annotation has been added to each metaclass that introduces a ‘PlatformConstraint’ value. In addition, the meta-model itself contains a ‘PlatformKit’ annotation, which contains an ‘Ontology’ value that points to the platform ontology model. Table 1 shows the ‘PlatformConstraint’ annotation values for each meta-class that has a platform constraint. The values represent XML-style references to OWL concepts in the ontology that contains the platform constraints.

Table 1 Configuration language meta-model annotations

<table><tr><td>Meta-class</td><td>PlatformConstraint value</td></tr><tr><td>JavaMapping</td><td>#JavaMappingPlatform</td></tr><tr><td>Java1DataTypes</td><td>#Java1Platform</td></tr><tr><td>Java2DataTypes</td><td>#Java2Platform</td></tr><tr><td>UML2Observer</td><td>#Java1Platform</td></tr><tr><td>UML2JavaObserver</td><td>#JavaObserverPlatform</td></tr><tr><td>UML2Applet</td><td>#AppletPlatform</td></tr><tr><td>UML2MIDlet</td><td>#MIDletPlatform</td></tr></table>

## Classification of platform constraints

As platform constraints are represented as OWL concepts, they can be classified in a subsumption hierarchy. The OWL concepts at the root of the hierarchy are least specific and the concepts at the leaves are most specific. In the case of platform constraints, least specific and most specific refer to platform specificness.

The platform constraints themselves are defined independently of each other and typically use necessaryand-sufficient conditions. Consider the following platform constraints:

$$
\begin{array}{r c l} \text {UtilPm} & \sqsubseteq & \text {platform: Platform} \\ & \equiv & \exists \text {platform: providesFeature} \\ & & \text {midp: JavaUtilLibrary} \\ J 2 \text {UtilPm} & \sqsubseteq & \text {platform: Platform} \\ & \equiv & \exists \text {platform: providesFeature} \\ & & \text {pp: JavaUtilLibrary} \end{array}
$$

Even though these platform constraints are defined independently, they are strongly related. Both are sub-concepts of ‘Platform’ and ‘J2UtilPm’ requires ‘pp:JavaUtilLibrary’, which is a sub-concept of ‘midp:JavaUtil

Library’ (see Figure 3). Each instance of the ‘pp:Java UtilLibrary’ concept is also an instance of the ‘midp:JavaUtilLibrary’ concept; hence, each instance of the ‘J2UtilPm’ concept is also an instance of the ‘UtilPm’ concept. Therefore, ‘J2UtilPm’ can be classified as a subconcept of ‘UtilPm’. As ‘J2UtilPm’ is a sub-concept of ‘UtilPm’, it is more specific than ‘UtilPm’. All platform constraints at the leaves of the sub-concept/superconcept hierarchy are considered most specific, while all platform constraints at the root of this hierarchy are considered least specific.

An automatic reasoner for OWL–DL, such as Racer, can automatically infer these sub-concept relationships. As this can be an expensive computing task, the classification of platform constraints is carried out in advance and separate from constraint validation. The platform constraints only need to be re-classified when they change. The platform constraints change only when the models (PIMs) and/or model transformations to which they pertain have changed.

In a CM, several platform constraints apply. When comparing different CMs to find out which is most specific or least specific, groups of OWL concepts have to be compared, instead of single OWL concepts. This can be done by defining an intersection concept for each group of platform constraints. An intersection concept represents the intersection of the sets of instances defined by the platform constraints. Hence, an instance that classifies as an instance of each of the platform constraints in a group classifies as an instance of the intersection concept. The intersection concepts for each group can be classified in a hierarchy in the same way that platform constraints are classified. The most-specific and least-specific group of platform constraints can now be determined.

It is possible that no sub-concept relationship between platform constraints – or intersections of platform constraints – can be inferred. In that case, it cannot be determined which (group of) platform constraint is more or less specific. This situation is handled by providing the (group of) platform constraints as a manually sorted list, ordered by user preference. Using the strategy described above, the automatic reasoner can now sort the list mostspecific-first or least-specific-first and leaves the order unchanged where no sub-concept relationship can be inferred.

## Platform constraint satisfaction

As soon as a concrete platform description is available – usually at the time of deployment – the platform constraints can be checked against this concrete platform. Consider the concrete platform described in Figure 4. The ‘zaurusC860’ instance classifies as an instance of the ‘J2UtilPm’ platform constraint that is mentioned before: ‘zaurusC860’ is a ‘platform:Platform’ that provides the ‘zaurusClassLibrary’ feature, which is an instance of ‘j2me-pp-1\_0:J2me-pp-1\_0ClassLibrary’, a sub-concept of ‘j2me-pp-1\_0:JavaUtilLibrary’. If an instance of a platform constraint is found in the concrete platform description, that platform constraint is considered satisfied.

Classifying the instances for each OWL concept does not require a fully functional OWL–DL reasoner. Instead, a partial, instance-based reasoner such as the Jena OWLMicroReasoner (http://jena.sf.net) can be used. This reasoning task consists of comparing all instances against the fixed set of platform constraints and is hence a less expensive computing task.

In the previous subsection, we have used intersection concepts for the purpose of classifying a hierarchy of groups of platform constraints. Note that this intersection concept cannot be used for checking whether a group of platform constraints is satisfied. The platform constraints in a group may refer to different parts of the platform and can be disjoint as such. In that case, the intersection concept cannot have any instances, which means it cannot be satisfied. Therefore, a group of platform constraints is considered satisfied if and only if each platform constraint in that group is satisfied.

The procedure for checking platform constraint satisfaction uses the platform constraint hierarchy that results from the classification of platform constraints. Each unsatisfied platform constraint is pruned from that hierarchy, such that the resulting hierarchy contains only satisfied platform constraints. Using this pruned hierarchy, it is possible to determine the most-specific and least-specific (group of) platform constraints that are valid for the given concrete platform according to the method given in the previous subsection.

## Tool support

A proof-of-concept tool, PlatformKit http://ssel.vub.ac.be/ssel/research:mdd:platformkit), has been developed that implements platform constraint checking as well as platform-based optimisation. PlatformKit is implemented as an Eclipse plug-in. It uses EMF for all meta-modelling and Jena for OWL–DL manipulation. The tool uses a DL reasoner, such as Racer (Mo¨ller & Haarslev, 2003), for pre-calculation of the constraint taxonomy. Constraint validation itself is performed by the built-in OWLMicroReasoner of the Jena framework.

PlatformKit can be used to profile a configuration language meta-model to target a specific platform. Each meta-class that has a platform constraint is validated against a prototype concrete platform description. Only meta-classes with satisfied platform constraints may be used when modelling a configuration for the targeted prototype platform. This scenario is shown in Figure 7.

The different actions that PlatformKit performs are depicted as boxes, where nested boxes represent subactions. First, PlatformKit extracts the platform constraints from the configuration language meta-model and groups them per meta-class in a special constraint space model. A constraint space contains the groups of

![](/api/attachments/MPPB9C2M/fulltext/images/43e2a965bbb57ad95a21f6c60387cc23b4e3bc7dcc4cbc64cc7e53620726b457.jpg)  
Figure 7 Flowchart of the platform-profiling scenario.

platform constraints – or constraint sets – used for classification of the platform constraints. Together with the platform vocabulary ontologies and the platform constraint ontology, the constraint space model provides enough information for PlatformKit to classify the concept taxonomy. This action requires the intersection concepts for each constraint set to be generated before the concept hierarchy can be inferred. The resulting inferred ontology contains all relevant parts of the platform vocabulary ontologies as well as all platform constraints and constraint set intersection concepts. Together with the constraint space model and a platform instance ontology, the inferred platform ontology can be used to determine which constraint sets (correspond to meta-classes) are most specific and have all their constraints satisfied. This information is used by PlatformKit to dynamically adapt the EMF-based CM editor, such that only those elements of which its metaclass’ platform constraints are satisfied can be added to the model. The list of available model elements is also sorted most-specific-first and the ‘validate’ option of the editor includes a platform constraint satisfaction check.

In addition, PlatformKit can be used to reason about the CMs themselves. In this case, all platform constraints that apply for a CM are grouped together. The platform constraint groups for each CM can now be classified in a subsumption hierarchy, such that the most-specific and least-specific configuration can be determined. At deployment time, a concrete platform description is matched against each of the configurations, after which the most-specific or least-specific valid configuration can be deployed. This scenario is shown in Figure 8.

This scenario looks very similar to the previous one, which shows that most PlatformKit functionality can be reused for this scenario. Instead of extracting all platform constraints in the configuration language meta-model, PlatformKit retrieves the meta-classes used in each CM and extracts the platform constraints that apply to those meta-classes. The platform constraints are then grouped in the constraints space model as constraint sets per CM. Classification of the taxonomy works exactly the same way as in the previous scenario, except that constraint sets now correspond to CMs instead of configuration language meta-classes. PlatformKit can now again determine which constraint sets are most specific and have all their constraints satisfied. As constraint sets now correspond to CMs, the result can be used to deploy the best configuration for a given concrete platform.

![](/api/attachments/MPPB9C2M/fulltext/images/0f6dd8627638b59058b81517a384e3e5504697909b1e70b12ee61cde37075543.jpg)  
Figure 8 Flowchart of the deployment scenario.

A web interface (Java servlet) is provided to support platform-based deployment of the various configurations. The servlet receives a concrete platform specification from a client, against which the available configurations are validated. It can either return the most-specific (default) or least-specific option that is still valid, based on the client’s preferences. It then redirects the client to the URL that contains the corresponding configuration.

## Discussion and related work

Platforms are the primary differentiators in MDA-based software engineering approaches, as they determine the nature of PIMs, PSMs and the mappings between them. No explicit models of these platforms currently exist. We consider explicit models of these platforms to be necessary if we want to automate any decision-making process based on platforms. The lack of explicit PMs is also discussed in Almeida et al. (2004). They introduce abstract platforms, which describe a set of elements to model a PIM against. This set of elements includes design artefacts that are available in a target platform (classes, interfaces) and design constructs that can be mapped to that platform (stereotypes, profiles), for example, with model transformations. The goal of abstract platforms is to ease platform-independent modelling. Our PMs can be used to define explicit platform dependencies for each abstract platform. In Tekinerdog˘an et al. (2004), platform selection rules are discussed, which allow for pre-selecting a number of target platforms. In this way, less platforms need to be supported. In our case, platform selection rules can be used to narrow down the amount of platform domain concepts (e.g. Java virtual machines) that need to be modelled to support the pre-selected target platforms.

We chose to use DSM as our configuration management approach. In Czarnecki et al. (2005), it is demonstrated that feature models can also be used for configuration purposes. In this context, a configuration consists of the features that were selected according to the variability constraints defined by the feature model. The relationship between feature modelling and domainspecific languages is explored in Deursen & Klint (2002). An important conclusion is that feature models can be translated into a DSL grammar (or meta-model). This is illustrated by their feature description language (FDL), which follows the same structure as a BNF grammar. The meta-models we use for describing our features can hence be considered to be equivalent to feature models. The fact that both DSM and the MDA itself can share the same model-driven technology also greatly simplifies matters.

We use OWL ontologies to represent our PMs. In Meng et al. (2006), an ontology-based software comprehension framework is presented. Our platform ontologies can contribute to this framework and to the knowledge management of software development in general. Our use of ontologies to support the MDA is also in line with a trend where model-driven approaches increasingly converge with ontology-based approaches (Roser & Bauer, 2006; Kappel et al., 2006). In Be´zivin et al. (2005), an infrastructure for combining UML/MOF models and ontologies is introduced. Such an infrastructure can be useful for a better integration of platform constraints into configuration languages that are based on MOF. In OMG (2006), the OMG proposed a standardised meta-model for ontologies. We have in fact used an EMF-based version of this meta-model (http://www.alphaworks.ibm.com/tech/semanticstk) to transform UML models of the API of specific Java platforms, such as J2ME PP 1.0 and J2ME MIDP 1.0, to ontologies of these platforms using the ATL. The UML models of the API were in turn generated using the Jar2UML tool (http://ssel.vub.ac.be/ssel/research:mdd: jar2uml).

## Conclusions and future work

This paper has illustrated how platform ontologies can be used to explicitly define the platform dependencies of the models and model transformations involved in MDA-based software development. It has shown how platform dependencies are decoupled from concrete platforms, which aligns with the separate evolution of the software being developed and the targeted platforms.

Model-driven software configuration can be performed using DSM techniques. Configuration language metamodels can be annotated with platform constraints from a platform ontology. Several automatic reasoning tasks can be carried out on configuration models and metamodels, based on classification of platform constraints in a most-specific/least-specific hierarchy and validation of these platform constraints against concrete platform descriptions. The relatively expensive computing task of hierarchy classification can be performed in advance and its result is reused for validation, which is a less expensive computing task.

Tool support has been developed for supporting platform ontologies in the Eclipse platform. EMF configuration language meta-models and configuration models can use platform constraints for platform-based optimisation and validation. A web interface has been developed to support platform-based deployment.

Our approach already makes limited use of OMG’s ODM for the automatic generation of platform ontologies. The automatic generation of additional platform ontologies is ongoing work. An important part of this process is the reverse engineering of Java class libraries to UML models. Our own Jar2UML tool is used to perform this task. We are currently experimenting with reverse engineering all references made by the class library – including references made by bytecode instructions – in addition to the class library itself. This allows us to infer the required Java API for any given Java binary. This inferred API can be compared against the various Java API specifications using model transformation, so that we can determine the Java platforms on which the given Java binary runs.

Currently, each client of the web-based deployment service has to manually provide a platform description. In the future, the user agent identifier string of most mobile devices can be used to look up a static platform description in a database. In case the platform is more dynamic – the user installs most of the software on traditional computers, for instance – a special platform discovery agent can be used to create a platform description on the fly. Such an agent does not need to have intricate knowledge of each platform, as most platform knowledge is encoded in the base platform ontology and its extensions.

## Acknowledgements

The authors thank the anonymous reviewers for their constructive comments and suggestions, which allowed them to better position their work. Furthermore, the authors thank the CoDAMoS project members and user committee for discussing their ideas as well as the Institute for the Promotion of Innovation by Science and Technology in Flanders (IWT-Flanders) for their financial support.

## About the authors

Dennis Wagelaar is a research assistant at the System and Software Engineering Lab of the Vrije Universiteit Brussel in Belgium. He holds an M.Sc. degree in Computer Science (University of Twente, the Netherlands). His research interests are model-driven engineering and using knowledge-based techniques in the field of software engineering.

Ragnhild Van Der Straeten is a post-doctoral researcher at the System and Software Engineering Lab at the Vrije

## References

ALMEIDA JPA, DIJKMAN RM, VAN SINDEREN M and PIRES LF (2004) On the notion of abstract platform in mda development. In Proceedings of the Eighth International Enterprise Distributed Object Computing Conference (EDOC 2004), Monterey, CA, USA, pp 253–263, IEEE Computer Society.

BAADER F, CALVANESE D, MCGUINNESS D, NARDI D and PATEL-SCHNEIDER P (Eds) (2003) The Description Logic Handbook: Theory, Implementation and Applications. Cambridge University Press, Cambridge, UK.

BE´ZIVIN J, DEVEDZ<sup>ˇ</sup>IC<sup>´</sup> V, DJURIC<sup>´</sup> D, FAVREAU J, GAS<sup>ˇ</sup>EVIC<sup>´</sup> D and JOUAULT F (2005) An m3-neutral infrastructure for bridging model engineering and ontology engineering. In Proceedings of the First International Conference on Interoperability of Enterprise Software and Applications (INTEROP-ESA’05), Geneva, Switzerland Springer-Verlag.

BUDINSKY F, STEINBERG D, MERKS E, ELLERSICK R and GROSE TJ (2003) Eclipse Modeling Framework, The Eclipse Series, Addison Wesley Professional.

CZARNECKI K, HELSEN S and EISENECKER UW (2005) Staged configuration through specialization and multilevel configuration of feature models. Software Process: Improvement and Practice 10(2), 143–169. Special Issue on Software Product Lines.

DEURSEN AV and KLINT P (2002) Domain-specific language design requires feature descriptions. Journal of Computing and Information Technology 10(1), 1–17.

DUCATEL K, BOGDANOWICZ M, SCAPOLO F, LEIJTEN J and BURGELMAN JC (2001) Scenarios for ambient intelligence in 2010. Technical Report, IST Advisory Group (ISTAG) [Online] ftp://ftp.cordis.lu/pub/ist/docs/ istagscenarios2010.pdf.

GRUBER TR (1993) A translation approach to portable ontology specifications. Knowledge Acquisition 5(2), 199–220.

JOUAULT F and KURTEV I (2005) Transforming models with ATL. In Model Transformations in Practice Workshop at MoDELS 2005, Montego Bay, Jamaica.

KAPPEL G, KAPSAMMER E, KARGL H, KRAMLER G, REITER T, RETSCHITZEGGER W, SCHWINGER W and WIMMER M (2006) Lifting metamodels to ontologies: a step to the semantic integration of modeling languages. In Proceedings of the ACM/IEEE Ninth International Conference on Model Driven Engineering Languages and Systems (MoDELS 2006), Genova, Italy, Volume 4199 of Lecture Notes in Computer Science, pp 528–542, Springer-Verlag.

LEDECZI A, BAKAY A, MAROTI M, VOLGYESI P, NORDSTROM G, SPRINKLE J and KARSAI G (2001) Composing domain-specific design environments. IEEE Computer 34(11), 44–51.

MENG WJ, RILLING J, ZHANG Y, WITTE R and CHARLAND P (2006) An ontological software comprehension process model. In Proceedings of the Third International Workshop on Metamodels, Schemas, Grammars, and Ontologies for Reverse Engineering (ATEM 2006), Genoa, Italy.

Universiteit Brussel, Belgium. She holds M.Sc. degrees in Applied Mathematics (Universiteit Gent, Belgium) and in Applied Computer Science (Vrije Universiteit Brussel, Belgium). She received a Ph.D. in Science at the Vrije Universiteit Brussel. She has published many peer-reviewed international articles on the topic of inconsistency management in model-driven engineering.

MILLER J and MUKERJI J (2003) MDA Guide. Object Management Group, Inc. Version 1.0.1, omg/03-06-01, Needham, MA, USA.

Mo¨LLER R and HAARSLEV V (2003) Description logics for the semantic web: racer as a basis for building agent systems. Ku¨nstliche Intelligenz 17(3), 10–15.

OMG (2005) Unified Modeling Language: Superstructure. Object Management Group, Inc. Version 2.0, formal/05-07-04, Needham, MA, USA.

OMG (2006) Ontology Definition Metamodel. Object Management Group, Inc. Sixth revised submission to OMG/ RFP ad/2003-03-40, ad/2006-05-01, Needham, MA, USA.

PREUVENEERS D, VAN DEN BERGH J, WAGELAAR D, GEORGES A, RIGOLE P, CLERCKX T, BERBERS Y, CONINX K, JONCKERS V and DE BOSSCHERE K (2004) Towards an extensible context ontology for ambient intelligence. In Proceedings of the Second European Symposium on Ambient Intelligence (EUSAI 2004), Eindhoven, The Netherlands (MARKOPOULOS P, EGGEN B, AARTS EHL and CROWLEY JL, Eds), Volume 3295 of Lecture Notes in Computer Science, pp 148–159, Springer-Verlag.

ROSER S and BAUER B (2006) An approach to automatically generated model transformation using ontology engineering space. In Proceedings of the Second Workshop on Semantic Web Enabled Software Engineering, Athens, GA, USA.

SMITH MK, WELTY C and MCGUINNESS DL (2004) OWL Web Ontology Language Guide World Wide Web Consortium. W3C Recommendation 10 February 2004 [Online] http://www.w3.org/TR/owl- guide/.

TEKINERDOG<sup>˘</sup> AN B, BILIR S and ABATLEVI C (2004) Integrating platform selection rules in the model driven architecture approach. In Model Driven Architecture: European MDA Workshops: Foundations and Applications, MDAFA 2003 and MDAFA 2004, Enschede, The Netherlands, June 2003 and Linko¨ping, Sweden, June 2004. Revised Selected Papers (ASSMANN U, AKS¸IT M and RENSINK A, Eds), Volume 3599 of Lecture Notes in Computer Science, pp 159–173, Springer-Verlag.

TOLVANEN JP and ROSSI M (2003) Metaedit+: defining and using domainspecific modeling languages and code generators. In Companion of the 18th Annual ACM SIGPLAN Conference on Object-oriented programming, systems, languages, and applications (OOPSLA 2003), Anaheim, CA, USA, pp 92–93, ACM Press.

WAGELAAR D and VAN DER STRAETEN R (2006) A comparison of configuration techniques for model transformations. In Proceedings of the Second European Conference on Model Driven Architecture – Foundations and Applications (ECMDA-FA 2006), Bilbao, Spain (RENSINK A and WARMER J, Eds), Volume 4066 of Lecture Notes in Computer Science, pp 331–345, Springer-Verlag.
