---
otero_id: 21654
otero_key: "HJKVBFDW"
title: "Model and data integration and re-use in environmental decision support systems"
authors: "Andrea E. Rizzoli; J.Richard Davis; David J. Abel"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00068-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model and data integration and re-use in environmental decision support systems

Andrea E. Rizzoli <sup>a,)</sup>, J. Richard Davis <sup>b</sup>, David J. Abel <sup>c</sup>

a IDSIA— Istituto Dalle Molle di Studi sull’Intelligenza Artificiale, Lugano, CH-6900, Switzerland

<sup>b</sup> CSIRO Land and Water, Canberra, ACT 2600, Australia

<sup>c</sup> CSIRO Mathematical and Information Sciences, Canberra, ACT 2600, Australia

Accepted 19 October 1998

## Abstract

A software architecture for the management of environmental models is presented. The Systems Theory representation of models is embedded in an object-oriented approach that emphasises the separation of models from data, thereby promoting model and data integration and re-use. The concepts presented here correspond to the requirements of a Model Management System MMS . It is finally shown how a Decision Support System can use this approach to implement the MMS in order toŽ . facilitate problem definition via the domain base and problem solution via the model base .Ž . Ž . q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Model management; Model integration and re-use; Environmental decision support systems

## 1. Summary

A very large number of water-related models have been developed over the years, covering such topics as rainfall-runoff, in-stream water quality, flood prediction, ground-water accession, etc. There has been an increasing demand from managers for models that can handle more complex environmental problems. It is difficult to simply link the existing models together into integrated models for these problems because the models were never originally designed to standards that allowed such linking. Some difficulties are: intertwining of user interfaces with each of the models; lack of modular construction; differing computer languages; poor documentation of conceptual limitations and assumptions; and lack of standardization of input and output structures.

The advent of object-oriented approaches in computer science has made the systematic, modular development of new models more feasible and this technology is being increasingly adopted by modellers when writing new models. However, standards need to be set by the modelling community to ensure maximum re-usability of component models. The following sections provide a basis for an object-oriented approach using the concept of encapsulation of component models.

Existing models pose a further problem. There has been such an investment in these legacy models that it is impractical to discard them or rewrite in object-oriented form. There are various approaches to legacy models although none is as efficient as using properly designed object-oriented models 27 .<sup>w</sup> <sup>x</sup> The HYDRA project 11 and the TwoLe decision<sup>w</sup> <sup>x</sup> support system 26 are explorations into such an<sup>w</sup> <sup>x</sup> approach.

## 2. Introduction

Environmental problems lie at the cross-roads of multiple disciplines, and for this reason are often described by a set of interacting models. For instance, in a model of lake eutrophication, one model can describe the limnological processes and another one the ecological processes. The latter can also be decomposed into sub-models such as algal uptake of nutrients and food-web processes.

These integrated models need to be embedded in a Decision Support Systems DSS to help managersŽ . to assess environmental impacts of various policies and decisions. A standard DSS is composed of at least three modules: a data base management system Ž . Ž . DBMS , a model base management system MMS and a dialogue generation and management software Ž . DGMS 31 .<sup>w</sup> <sup>x</sup>

Among the necessary characteristics of the MMS module 24 are the following.<sup>w</sup> <sup>x</sup>

Ž . 1 The MMS should be able to create new models quickly and easily.

Ž . 2 The model building-blocks of the MMS should contain cognitively meaningful chunks of knowledge to the user.

Ž . 3 The MMS should be able to inter-relate models with appropriate linkages, thus providing the functions of model integration, model decomposition, sequential model processing, and concurrent model processing.

Ž . 4 The MMS should be able to manage the model base with functions analogous to data base management. The MMS should be able to decompose a query into a sequence of data retrievals and model invocations and retrievals.

Ž . 5 The MMS must have a meta-level encyclopedia, analogous to a DBMS’s data dictionary, which includes a repository of data, heuristics, tasks, models, users, and the relationships between them. The following characteristic can be added in order to include the legacy models now in widespread use.

Ž . 6 The MMS must be able to incorporate executable models written by other modellers and to connect them to other models in a seamless way.

Proposals to develop MMSs have arisen in Management Science and Operation Research 6,7,16, 24 , Artificial Intelligence 10 and System Theory<sup>x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 13,23,28,32,33 . Some authors in particular have dealt with issues that have some common ground with the ideas exposed in this work. For example, Bhargava and Kimbrough 3 discuss the embedded<sup>w</sup> <sup>x</sup> language technique. They remark that model languages, from natural language to mathematical formulae, are the common tools used by modellers to express their ideas, but they are not flexible enough to contain information about the modelling domain, such as information sources, logical and causal relationships among model entities, data descriptions, etc. They propose an embedding language that incorporates this extra information.

Hong et al. 16 pursue an approach based on<sup>w</sup> <sup>x</sup> measurement theory to represent the mapping from the domain world to the model base. The domain world is composed of an individual-level and of a class-level. The aim is to enhance model re-usability and integration via a general description of the model mechanism, independent of the specific application.

Another notable example of an approach to model management can be found in SYMMS, a model management system implemented on a UNIX workstation 20 . SYMMS uses a model description lan- <sup>w</sup> <sup>x</sup> guage that allows the user to define general-type modules and atomic-version modules, instances of the general-type ones.

The previously cited works and experience have originated mainly from the management sciences field, where the focus is on solving and integrating mathematical programming problems. Our work is aimed at presenting the architecture of a MMS well suited to solve spatial and temporal environmental problems.

All these authors agreed on the use of Object Technologies 15 to answer the above requirements. <sup>w</sup> <sup>x</sup> Object Technologies include object-oriented analysis, design, and programming paradigms as tools to develop software projects. Object-orientation is mainly based on three concepts: abstraction, encapsulation, and hierarchy. Paraphrasing Booch’s definitions 5 , abstraction has the purpose of denoting the<sup>w</sup> <sup>x</sup> essential characteristics of an object, providing crisply defined conceptual boundaries; encapsulation separates and puts in compartments the elements of an abstraction and separates the interface of an abstraction from its implementation; and finally hierarchy is a ranking or ordering of abstractions.

In the following, we explain how the model representation technique presented in this paper promotes model and data re-use with particular attention to environmental models.

## 3. A MMS for environmental models

The vast majority of models describing environmental systems and natural resources are dynamic models, since modellers are mostly interested in the change of systems over time in response to external actions. For instance, global warming models try to infer a relationship between the level of emissions and the change in temperature in different parts of the globe, over a period of several years.

Traditional modelling has often relied on the well assessed formalism proposed by Systems Theory where inputs, states, outputs, and parameters represent the data. The state transition function and the output transformation are the operations that can be performed on these data. Inputs and outputs can be connected to create the more complex models re quired in environmental modelling.

In this work, the design of a MSS based on Object Technology is proposed using the same mathematical formalism of Systems Theory; these two theoretical foundations are applied in order to enhance and facilitate some essential functions like model prototyping, data access, and model integration. The reason for such a MMS is due to the increasing complexity of environmental models, which are often made of several multi-disciplinary components, involving fields such as hydrology, ecology, control engineering, etc. The modeller is faced with the difficult task of integrating technologies, and to do this, has to integrate the sub-models which build the big picture. Moreover, the body of knowledge in the environmental sciences, and consequently the number of models, is constantly increasing. Model bases and model directories have been created to be able to tap into this knowledge, and software technologies are at work to make these resources available see, for instance, Refs. 14,17 .Ž <sup>w</sup> <sup>x</sup>.

Another issue in building DSS to support solutions of real-world problems is the time and cost to assemble the modelling systems and data resources and then to integrate these into information systems usable by planners or managers. Not unusually, this means that DSSs are completed only after the problem has effectively been solved by other means.

In the remainder of this paper, two main entities are introduced: the domain base and the model base. These entities are introduced in order to separate the description of the data items the domain from theŽ . description of how some of these data are combined to infer expected behaviours the models .Ž .

## 4. The domain base

The deductive modelling process typically stems from a deep study of the real world. This leads to the identification of some classes of basic entities to be included in the model. Then, the modeller starts to hypothesise about the kind of relations existing among these entities and then formalises the relationships, using mathematical tools. Often the modeller arrives at a satisfactory description of a phenomenon only after a lot of exploration with the structure of the model. A tool that would allow the user to substitute a model for another, to re-use a model and to easily manage data links would speed up this process 8 . <sup>w</sup> <sup>x</sup>

While most modelling software environments separate models from data, their focus is on models which can be fed with alternative data sets. Parameter calibration is the main problem. The approach of the MMS presented in this paper is reversed, data sets can be transformed via models which are applied to them. This approach allows the modeller not only to perform traditional parameter calibrations, but also examine alternative model structures, comparing how different models behave against the same data sets and evaluating the relative performance indicators. It is therefore required that models be written with respect to the available data in order to be able to substitute one model for another, automating data formatting and conversions and enforcing consistency of data usage in models. The implementation of these requirements leads to the possibility of effective re-use of models and data.

In practice if one wants to substitute one submodel for another in a complex inter-connected model, then it would be necessary to re-establish all the interface connections between the new sub-model and the surrounding ones and to redefine the data base access path for each parameter and input, state, and output variable. This approach is used in various MMS, both academic and commercial. However, re-usable models must define which kind of data they use and produce, and in which format, but not state the explicit data base access paths. A mechanism which implements this different approach is explained in the following sections, but first the concepts of domain classes, domain objects and models are introduced.

## 4.1. Domain classes and objects

Domain objects are instances of general structured data types Ž . domain classes . Domain classes are designed to achieve generality and re-usability: models are written mapping their data sets to the data attributes of domain classes. When a model is applied to an instance of a problem, it uses the domain class attribute names to access the corresponding attributes in the domain objects, which in turn point to data sources. Note that different models can refer to the same domain class. Thus, domain classes play the role of data types and therefore define generalisations of modelled objects that have some common features. Usually, a domain class provides a general description of an entity, e.g., the class of flat watersheds. A domain object is an instance, a particular case.

Domain classes are based on the concept of abstract data types and are inspired by a mix of the concept of object-oriented classes 5 , frames 19,30 ,<sup>w x</sup> <sup>w</sup> <sup>x</sup> database schemas 22 , and prototype systems 18 . <sup>w x</sup> <sup>w x</sup> The analogue with data types and therefore withŽ classes and database schemas provides generalisa- . tion, while similarities with prototype systems maintain the possibility of expanding the problem definition by incrementally modifying existing domain class definitions.

The union of all the domain classes defines the structure of the domain base. Domain classes can be decomposed into sub-classes. Sub-classes can be organised in a hierarchy, using classification and encapsulation principles.

The classification relationship, used to structure the domain base, is based on the concept of inheritance. Domain classes can be classified according to their nature Ž . is-a relationships . For instance, the class of steep watersheds and the class of flat watersheds derive their basic properties from a more general watershed class, but the flat watershed class also has some characteristic data attributes, such as the flood plain which is not an attribute of steep watersheds.

Encapsulation allows different description levels and provides the capability of describing big components as the sum of smaller ones Ž part-of relationships . For example, a watershed can be composed . of a number of sub-watersheds. This leads towards an object-oriented implementation of the data structures which is analogous to a non-normal form of a database table. Information is thus kept together in self-standing information pools.

The domain base structure depends on the particular solution strategy that the modeller has in mind. It is therefore a good practice to try to be as general as possible in designing the domain classes. It will be possible to specialise the descriptions later in the modelling process.

## 4.2. The structure of domain classes

A domain class is an abstract data type which is characterised by its set of data attributes. The data attributes of the domain class provide a description of the data and will be filled with actual data values when the instance of a domain object is created.

Data attributes are classified according to their role: input, output and local. Domain objects may communicate and exchange information. This flow of information will take place through the interface of the domain class defined by the input and output data attributes. The local data attributes are hidden to external domain classes. For example, a domain class which describes a watershed might have as input data attribute the rainfall in some gauging stations, as output attribute the measured watershed flow, and as local data the soil types over the watershed area.

For the purpose of classification and encapsulation, basic and compound domain classes can be defined. A compound domain class can have subparts, while a basic one is the elemental building block. A basic domain class BDClass can be then defined by the following data structure:

$$
B D C l a s s = \left\langle B D C l a s s _ {\mathrm{b}} ^ {(1)}, \dots , B D C l a s s _ {\mathrm{b}} ^ {(n)}, \boldsymbol {i} _ {\mathrm{b}}, \boldsymbol {l} _ {\mathrm{b}}, \boldsymbol {o} _ {\mathrm{b}} \right\rangle \tag {1}
$$

where $B D C l a s s _ { \mathrm { b } } ^ { ( i ) }$ is the superclass or a set of Ž superclasses of the basic class. BDClass and, if present, it must be another basic class. The basic class inherits the data attributes from the superclass. $i _ { \mathrm { b } } , \ l _ { \mathrm { b } } , \ o _ { \mathrm { b } }$ are the sets of input, local and output data attributes defined as:

$$
i _ {\mathrm{b}} = \left\langle \left(D B D a t a, i _ {1}\right), \dots , \left(D B D a t a, i _ {\mathrm{m}}\right) \right\rangle\tag{2}
$$

$$
l _ {\mathrm{b}} = \left\langle \left(D B D a t a, l _ {1}\right), \dots , \left(D B D a t a, l _ {\mathrm{p}}\right) \right\rangle\tag{3}
$$

$$
o _ {\mathrm{b}} = \left\langle \left(D B D a t a, o _ {1}\right), \dots , \left(D B D a t a, o _ {\mathrm{q}}\right) \right\rangle\tag{4}
$$

DBData Ž . Domain Base Data item is the abstract data type used to catalog and store data attributes. Among its fields we find:

\- name, a unique identifier for the data;

\- description, a general textual documentation of the meaning of the data item;

\- dimension, the physical units used to measure the data;

\- format, the data type e.g., Ž n by m matrix of reals, etc. ;.

\- value, a function returning the actual value of the data attribute or a reference to another data attribute in another domain object the usage of this Ž field as a reference is explained later when dealing with compound domain classes ..

Fig. 1 shows an example of a basic domain class representing a reservoir. The input data attribute set $i _ { \mathrm { b } }$ consists of only the inflow of water a tŽ .. The output set $o _ { \mathfrak { b } }$ by the reservoir water release $r ( t )$ . The local data attribute set $l _ { \mathrm { b } }$ includes the reservoir storage $s ( t )$ , the elevation function $h ( s ( t ) )$ which converts the volume of water to an elevation with respect to a reference value, and the minimum and maximum storage–discharge functions $( v ( a ( t ) , s ( t ) )$ , $V ( a ( t ) , s ( t ) ) )$ which define the shape of the reservoir discharge 21 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/HJKVBFDW/fulltext/images/2f49328d73af5366221d74add0bcbee61a3f149c77f94838e807422bd5c4578b.jpg)  
Fig. 1. A basic domain class. The reservoir domain class defines the data types used to describe a reservoir.

This example will be used throughout the paper, in order to show how this MMS can be applied to the case of the design of a DSS for water management, from data specification to the solution of the optimisation problem.

A compound domain class is defined by the tuple CDClass:

CDClass

$$
= \langle \text { superclasses }, \text { components }, i _ {\mathrm{c}}, l _ {\mathrm{c}}, o _ {\mathrm{c}}, \mathbb {M} \rangle\tag{5}
$$

where:

$$
\text { superclasses } = \left\langle D C l a s s _ {\mathrm{s}} ^ {1}, \dots , D C l a s s _ {\mathrm{s}} ^ {n} \right\rangle\tag{6}
$$

$$
\begin{array}{c} \text { components } = \langle (D C l a s s _ {\mathrm{c}} ^ {1}, c o m p o _ {1}), \dots , \\ (D C l a s s _ {\mathrm{c}} ^ {m}, c o m p o _ {m}) \rangle \end{array}\tag{7}
$$

The superclasses set is defined as the set of superclasses from which the current domain class inherits. It is composed of both basic and compound domain classes. While a basic domain class must inherit only from basic superclasses, a compound domain class can be derived from other compound domain classes.

A compound domain class is composed of a set of composing classes which are contained in the components set and represents the parts that make up the compound domain class. Again, these classes can be either basic or compound and therefore defined according to Eqs. 1 and 5 . Note that a name Ž . Ž . is assigned to identify each composing class $( c o m p o _ { 1 } , \ldots , c o m p o _ { n } )$ , in the same way that the data elements of a complex data type are named in a programming language e.g., type Ž complex is a record composed of a real part Re which is of type double and of an imaginary part Im of type ‘double’ ..

In a compound domain class the data attributes of the composing classes are hidden because they are nested encapsulated in these classes. The basicŽ . domain classes which make up the compound class are linked through the mapping defined by M which connects the inputs of the compound class to the inputs of the basic classes, the output of the basic classes to the outputs of the compound class and the outputs of the basic classes to inputs of the basic classes:

$$
\mathbb {M} = \left\{ \begin{array}{l} i _ {\mathrm{c}} \to i _ {b} \\ o _ {\mathrm{b}} \to i _ {\mathrm{b}} \\ o _ {\mathrm{b}} \to o _ {\mathrm{c}} \end{array} \right.\tag{8}
$$

Fig. 2 shows the layout of a compound domain class describing a very simple water system which includes a number of subclasses one catchment, oneŽ reservoir and one water consumer . The composing . classes are interconnected via a mapping: the reservoir receives the water inflow from the upstream catchment, and so on. This is all the information needed to build a compound domain class.

![](/api/attachments/HJKVBFDW/fulltext/images/beb053d4f69420a47e276adc36c3514883441a4e8f21b9a1a535cc8136b927fa.jpg)  
Fig. 2. A compound domain class. The spatial organisation of basic domain classes tries to model the spatial relationships observed in the real world data.

## 4.3. Basic and compound domain objects

A domain object is an instance of a basic domain class. The reservoir class seen in the previous example can be used to generate a reservoir domain object when the modeller defines the shapes of the storage–discharge functions and also specifies where to load and store the time series data associated with the water inflow, storage and release.

A basic domain object BDObj can be then defined by the structure:

$$
B D O b j = \left\langle B D C l a s s, D _ {\mathrm{b}} \right\rangle\tag{9}
$$

where BDClass is the originating basic domain class and $D _ { \mathfrak { b } }$ is the set of the values to be assigned to $i _ { \mathbf { b } } ^ { \prime } .$ $l _ { \mathbf { b } } .$ , and $o _ { \mathfrak { b } } ^ { \prime }$

Note that i and $o ^ { \prime }$ are subsets of, respectively, i and $^ { o , }$ since not all input and output variables are read or stored in the data base, but they can be linked to data attributes in other domain objects, as shown in Fig. 2.

In the same way, a compound domain object CDObj is defined by:

$$
C D O b j = \left\langle C D C l a s s, D _ {\mathrm{c}} \right\rangle\tag{10}
$$

where CDClass is the class used to generate the instance of a compound domain object and $D _ { \mathrm { c } }$ is all the data needed to create the sub-domain objects as defined in Eq. 5 and set the values of the dataŽ . attributes $i _ { \mathrm { c } } , \ l _ { \mathrm { c } }$ and $o _ { \mathrm { c } }$

Using the example compound domain class of Fig. 2, a water system domain object can be created by looking in the domain base for some basic domain objects to associate with the basic model classes. For instance, the Maggiore water system would assign the Ticino Catchment domain object to the theCatch catchment domain class, Lake Maggiore to theRes and, finally, Ticino River Agricultural Users to theUser.

4.4. Data mappings, aggregations and transformations

Choosing where to put data attributes, whether into a basic domain class at the bottom level of an encapsulation or in a compound one at the top, is based on data visibility. Sometimes a decision cannot be made, since the decision depends on the kind of model which will use the data attributes and different models may wish to use the same data set at different representation levels. For instance, the modeller could be interested in writing an aggregate model for a very large watershed which makes use of the ground-water permeability coefficients over the whole area which are stored in a matrix. In another model, the same data could be used related to a sub-area and a sub-matrix should be extracted to represent those properties. Data mappings are introduced to overcome this kind of problems.

Data mappings occur when data attributes in subdomain classes are mapped into data attributes in the compound domain class. This allows the modeller to operate on the whole set of data and not on single instances. Typical data ‘mappers’ are vectors, matrices, lists. A data mapping preserves the dimension of the data organising it in a structure which has a greater cardinality than the single elements. A data mapping M is represented by:

$$
\mathbb {M} \colon l _ {\mathrm{t}} \to L _ {\mathrm{T}}
$$

Where $\boldsymbol { l } _ { \mathrm { t } }$ is a vector of the sub-domain class data attributes and $\scriptstyle { L _ { \mathrm { T } } }$ is a vector in the local section of the super-domain class that has the same structure. For instance, in two domain classes Layer1 and Layer2 Žwhich represent two layers in a stratified lake there is a data attribute representing the nutri-. ent concentration $N ;$ in the domain class of type Lake it can be defined as a vector containing those two concentrations as elements:

$$
N _ {\mathrm{Lake}} = \binom{N _ {\mathrm{Layer1}}}{N _ {\mathrm{Layer2}}}
$$

Data aggregation is another operation which can be performed when some data attributes at the compound level are ‘intensive’ representations of the extensive data attributes contained in the sub-classes. For instance, the area of a catchment is the sum of the area of the sub-catchments; the temperature of a stratified lake can be considered equal to the weighted averages of the temperatures of the single layers into which it has been partitioned.

A data aggregation transforms a set of data of given cardinality into a representation with a lower cardinality often into a single data item . A dataŽ . aggregation is typically expressed by a function.

An example is given by:

$$
\boldsymbol {L} _ {\mathrm{T}} = f (\boldsymbol {l} _ {\mathrm{t}})
$$

where

$$
\boldsymbol {l} _ {\mathrm{t}} = \left( \begin{array}{c} l _ {\mathrm{st}, 1} \\ l _ {\mathrm{st}, 2} \\ \vdots \\ l _ {\mathrm{st}, n} \end{array} \right)
$$

$\scriptstyle { L _ { \mathrm { T } } }$ represents the local data attribute in the compound domain class and $\boldsymbol { l } _ { \mathrm { t } }$ a vector which contains the data attributes of the composing domain classes. The cardinality of $\scriptstyle { L _ { \mathrm { T } } }$ is equal to the cardinalities of the single elements $l _ { \mathrm { s t } , j } .$ For instance, suppose that two domain classes sc1 and sc2 of type subcatchment have the data attribute area. A data aggregation area can be defined as a local attribute of the compound domain class c of type catchment, which is composed of the two sub-catchments, and the aggregation function is defined as:

$$
A _ {\mathrm{c}} = a _ {\mathrm{sc1}} + a _ {\mathrm{sc2}}
$$

Finally, data transformations provide low-level data modifications among domain objects which potentially have communication problems. These problems may arise because data attributes may have different spatial or temporal scales, units of measurement, etc. A data transformation is usually a simple static function e.g., changing Celsius degrees toŽ Fahrenheit , but it can also be considered a model on. its own.

## 5. Models and the model base

The objectives of our MMS proposal are to make different models inter-operate seamlessly model in-Ž tegration and be able to test alternative models. against different working conditions model re-use . Ž .

When we started our work on model integration and reuse see Refs. 11,25 , techniques such as Ž <sup>w</sup> <sup>x</sup>. distributed computing on three-tiered architectures Ž . client–broker–server were being developed 1 .<sup>w</sup> <sup>x</sup> During the early application of our design to environmental problems the HLA High Level Architec- Ž ture approach of the DMSO 12 was described and, . <sup>w</sup> <sup>x</sup> recently, a special issue of the journal Decision Support Systems 4 has summarized a number of<sup>w</sup> <sup>x</sup> approaches.

All of the above mentioned works pointed out the need of model encapsulation in order to provide consistent interfaces to model functionalities. In this section, we describe our approach to encapsulation of environmental models.

A model class is an abstract data structure used to encapsulate the mathematical formulation of a given process to be modelled.

There are two kinds of model classes: basic and compound. A basic model class has a flat structure in the sense that is not composed of any other model; a compound model consists of other models. For instance, a reservoir can be considered a compound model when it is seen as an ecosystem composed of fish, zoo-plankton, and phytoplankton; conversely, when it is used to describe a simple storage of water in a water management system, the ecological components are neglected, it can be characterised as a basic model.

A key concept in our system is the generality of model formulations: in order to improve model reusability, model classes provide a way to write the model formulae in terms of data attributes of domain classes. Only when a model is assigned to an instance of a domain class a domain object is it Ž . linked to the data. Before that, it contains only the instructions on how to retrieve the data. This means that if n model classes can be associated with a given domain class, and if m instances of that domain class can be created that is,Ž m different domain objects , there will be a possible number of at. least m times n different model instances assuming Ž for simplicity that only one model instance per model class is generated ..

Potentially, many models can refer to a single domain class. Thus, a structure for retrieving and storing models, a model base, is needed. It has been shown by some authors 10,28 that the access operations to a model base must be analogous to the access operations allowed on a data base. In particular a model management system must allow the user to find a model corresponding to a given set of selection criteria, to modify a selected model and to compose a new model, possibly assembled from existing ones. It is not the aim of this work to discuss the issue of model selection see Falkenheimer andŽ Forbus 9 , but to describe how this approach can be<sup>w</sup> <sup>x</sup>. integrated in a model and solver selection tool for the solution of natural resources management problems.

Models must be re-usable with respect to domain classes. In a model, inputs, states, and outputs are variables, which can assume different values during a simulation run, while parameters are quantities that either are constant or have a limited range of variation. Inputs, states, outputs, and model parameters must find a correspondence in the data attributes of a domain class in the modelling domain. Thus, a model class is not a priori linked to a particular domain object but to a whole class of objects. If a new model class must use data attributes present in different domain classes, then a new domain class must be created, using the principles of aggregation or inheritance. Thus, input variables are mapped to input data, state variables and parameters to local data and output variables to export data in the domain class. Mapping a model variable to a domain class data attribute means to assign a context to that variable. Because, models can be expressed in very general terms, their formulations can be applied to different physical situations. Consider the simple example of the following model describing a decay phenomenon.

$$
\frac {\mathrm{d} y (t)}{\mathrm{d} t} = - C y (t)
$$

The independent variable t represents time; y can be the piezometric head in a reservoir or the voltage over a condenser: the meaning depends on the domain class to which the model is assigned, that is, to the context.

## 5.1. Basic models

A basic model class BMClass is defined by the following data structure:

$$
B M C l a s s = \left\langle D C l a s s, u _ {\mathrm{b}}, x _ {\mathrm{b}}, y _ {\mathrm{b}}, \Theta , \phi , \eta \right\rangle\tag{11}
$$

where DClass can be either a basic domain class or even a compound domain class, $u _ { \mathrm { b } }$ is the set of model inputs, $x _ { \mathrm { b } }$ the set of model states, $y _ { \mathrm { b } }$ the set of model outputs, is the set of model parameters. The state transition equation and the output transformation which describe the model in the Systems Theory approach are $\phi$ and , respectively.

The input, state, output and parameter sets are defined as:

$$
u _ {\mathrm{b}} = \left\langle \left(M D a t a, u _ {1}\right), \dots , \left(M D a t a, u _ {m}\right) \right\rangle\tag{12}
$$

$$
x _ {\mathrm{b}} = \left\langle \left(M D a t a, x _ {1}\right), \dots , \left(M D a t a, x _ {n}\right) \right\rangle\tag{13}
$$

$$
y _ {b} = \left\langle (M D a t a, y _ {1}), \dots , (M D a t a, y _ {p}) \right\rangle\tag{14}
$$

$$
\Theta = \left\langle \left(M D a t a, \theta_ {1}\right), \dots , \left(M D a t a, \theta_ {q}\right) \right\rangle\tag{15}
$$

These sets constitute the model interface.

Model variables and parameters are represented by the data type MData Ž . Model Data item with the following fields:

\- name, a unique identifier for the symbol;

\- description, a textual description of the meaning of the variable or parameter;

\- dimension, the unit of measure;

\- format, the data type, with its cardinality;

\- link, the reference to the data source. This field is detailed in the following paragraph.

The link field is of great importance, since it specifies where models get their inputs, states and parameters and where they put their outputs. It has been stated in Eq. 11 that model classes are associ-Ž . ated with domain classes in order to create model instances using the data stored in the related domain object. For example, an instance of a discretetime<sup>r</sup>discrete-space model of the reservoir is created by retrieving the continuous storage–discharge functions of its reservoir domain object and discretising them to create the release tables. These tables are a characteristic parameter of the reservoir model and, using the same set of storage–discharge functions, many alternative models can be generated, changing the discretisation of the inflow, storage and control inputs of the reservoir. In this case the link field must provide a reference to the data attribute of the domain class and a data transform function which is the function needed to convert the data from the format which is used in the domain class to the one used in the model class.

Another example may be provided by the inflow to the reservoir a tŽ .. One might be interested in simulating different models of the same reservoir against the same input data set. In this case the link field is used to reference the a tŽ . data attribute of the reservoir model class. The optional data transform function could convert the data sampling of the time series stored in the reservoir domain object to the sampling needed to run the model. While it is up to the user to define these links and to implement the data transform functions, these are one-off operations which are valid for all the model instances generated from the same model class.

Fig. 3 shows which model data attributes are linked to the ones of the domain class. The model input $a _ { t }$ is linked to the input data attribute $a ( t )$ of the reservoir domain class. The other model input $s _ { t }$ is the reservoir storage at time t as is therefore related to the local data attribute $s ( t )$ , as the model output $s _ { t + }$ that is the storage at time $t + 1$ . It is noteworthy that both a model input and an output refer to the same local data attribute, this is common when a discrete-time model is used to describe the behaviour of a continuous process, such as the water balance in a reservoir. Finally, $h _ { t } , \ r _ { t } ,$ and $R _ { t }$ are linked to the corresponding data attributes in the reservoir class. These links contain the data transform functions which map the continuous functions in the reservoir class to the discrete representation needed in the model.

![](/api/attachments/HJKVBFDW/fulltext/images/9b39cb8c852b227f8525defb1bc3ca4d0f7a53302fa1c950c37e8fd4b640725e.jpg)  
Fig. 3. A reservoir basic model class is linked to a reservoir class. Symbolic links are drawn to associate a data source with the model variables.

In Fig. 4, it is also shown how different model classes can refer to the same domain class. In this example, once the modeller has created an instance of the domain class, the Valtellina catchment, two model instances can then be derived which differ by the kind of model formulation which was employed Žthe ARX model, which takes into account exogenous inputs such as rainfall, and the ARMA model ..

In Figs. 3 and 4, some of the model inputs and outputs are ‘dangling’ such asŽ $u _ { t }$ . in Fig. 3 because the basic model is used as a component of a compound model. In this new situation the link field refers to one of the elements in the input, output, state and parameter sets of the compound model. An explanation of this usage is presented in Section 5.2 when describing the compound models.

A basic model can also be related to a compound domain class. In fact, the same domain object could be described by models at different scales of resolution. The modeller can organise the knowledge about the modelling domain in a structured way, where domain classes are made up of sub-domain classes and so on. The same modelling domain can be accessed by a model written by another modellerŽ . that has a more shallow view of the domain. Thus, it is sometimes convenient to have a basic model operate on a domain class which has a deep data structure that is composed of sub-classes . The basicŽ . model will be able to access these data through data aggregations and mappings. An example is reported in Fig. 5 where a black box ARX Model describes the compound domain object which represents the Tresa catchment. In the representation of the Tresa compound domain object there are four sub-catchments on which four different rainfall measurements

![](/api/attachments/HJKVBFDW/fulltext/images/2206aed337cf08359e8d503f0ce6557e8edbabe8ce951c3c3580e1f3a421f38d.jpg)  
Fig. 4. The same domain object can generate multiple model instances.

![](/api/attachments/HJKVBFDW/fulltext/images/8d15492d7b5f82b44619b07db21a3cdb47e94eb14e5b584047d4fca3c6b6dfe3.jpg)  
Fig. 5. A basic model can be associated with a compound domain object.

$( w _ { i } ( t )$ . for i:1 . . . 4 were gauged. These measurements are aggregated into their average w tŽ ..

This situation is common when the modeller wants to integrate a legacy model, written independently of the description of the domain base, in this framework.

## 5.2. Compound models

Like basic models, compound models are built on domain classes. Frequently it happens that there is one and only one set of domain objects, arranged according to a particular structure, that satisfies a particular compound model. An example is provided by the compound model of a watershed. When a real world watershed is modelled, its structure it is often so complex that there will be only one set of interconnected sub-watersheds that describes the structure of the compound watershed. On the other hand, a compound model for a stratified lake, composed of a set of basic models for each layer, can be applied to a wide variety of cases, not only to a particular lake.

A compound model is identified by:

\- a domain class with a non-empty set of sub- Ž parts ;.

\- a unique model identifier;

where the set of sub-parts of the domain class is put in relation to:

\- sub-domain class model unique identifier;

-influence links: ‘data from’ and ‘data to’ domain classes.

A compound model is therefore defined by:

CMClass<sup>s</sup> ² : DClass, components, u , l , y , L

Ž . 16

Where DClass is a domain class and components is the list of model classes which compose the compound model, defined as follows:

$$
\begin{array}{c} \text {components} = \langle (M C l a s s ^ {1}, m o d e l _ {1}), \ldots , \\ (M C l a s s ^ {m}, m o d e l _ {m}) \rangle \end{array}\tag{17}
$$

L is the mapping describing the linkages among the model classes which compose the compound model. This mapping is defined as:

$$
\mathbb {L} = \left\{\begin{array}{l}u _ {\mathrm{c}} \rightarrow u _ {\mathrm{b}}\\y _ {\mathrm{b}} \rightarrow l _ {\mathrm{c}}\\l _ {\mathrm{c}} \rightarrow u _ {\mathrm{b}}\\y _ {\mathrm{b}} \rightarrow y _ {\mathrm{c}}\end{array}\right.\tag{18}
$$

Note that the composing models are neÕer directly linked. The data exchange always happens through the special local data attributes $l _ { \mathrm { c } }$ . This is to ensure the re-usability of sub-models as it is explained in Section 5.3.

![](/api/attachments/HJKVBFDW/fulltext/images/122709183fdd8fc74521ccb1c0b27b2ad43e46a2691bcb7e5359876a7c6c55c1.jpg)  
Fig. 6. A compound model class for the Maggiore Water System.

The data attributes of a compound model are classified as input, local and output and are defined as:

$$
u _ {\mathrm{c}} = \left\langle \left(M D a t a, u _ {1}\right), \dots , \left(M D a t a, u _ {m}\right) \right\rangle
$$

$$
l _ {\mathrm{c}} = \left\langle \left(L D a t a, l _ {1}\right), \dots , \left(L D a t a, l _ {n}\right) \right\rangle\tag{19}
$$

$$
y _ {c} = \left\langle \left(M D a t a, y _ {1}\right), \dots , \left(M D a t a, y _ {p}\right) \right\rangle\tag{20}
$$

Ž . 21

The data type LData Ž . local data differs from the data type MData only because it lacks the link field, since the purpose of these data attributes is to provide an intermediate storage to connect the outputs to the inputs of the composing sub-models and not to access the data storages.

An example of a compound model class is reported in Fig. 6. The input data attributes $u _ { \textup { c } }$ are: the exogenous input $w _ { t + 1 } ;$ the input disturbance $e _ { t + 1 } ;$ the catchment state $c _ { t } ;$ the reservoir storage $s _ { t } ;$ and the water release decision $u _ { t }$ . These data attributes provide the input interface to the model, which will be useful when operating the compound model, as shown later in Section 6.

The local data attributes $l _ { \mathrm { c } }$ are the catchment runoff $a _ { t + 1 }$ which is then used as an input by the reservoir model, and the reservoir’s water release $r _ { t + 1 }$ which is fed into the water consumer theŽ HydroUser model ..

The output data attributes $y _ { \mathrm { c } }$ are the catchment and reservoir states at the next time step $( c _ { t + 1 } , s _ { t + 1 } )$ and the step cost $g _ { t + 1 }$ at time t <sup>q</sup> 1.

In Fig. 6, the arrows are directed from the sub models’ inputs to the compound model’s inputs to signify that data are retrieved from the compound model and fed into the sub models. On the other hand, the arrows are directed from the sub models outputs towards the compound model’s outputs. This means that the output values are stored in the outputs of the compound model and that the sub-models’ outputs refer to them.

## 5.3. Interchanging and connecting models

A focal point of the MMS architecture presented in this paper is model interchangeability. This means that the same model can be applied to various objects and that the same object can be modelled by different models in different simulation runs . WhenŽ . a new model is applied to an object, a new data set may be accessed. This is shown in the lattice of Fig. 7 where the generic domain class CatchDClass, which describes a catchment structure, can be used to create different catchment instances: using two alternative data sets to represent the same physical catchment ŽValtellinaCatch\_1 and ValtellinaCatch\_2. and another catchment: TresaCatchment. In this example, two alternative model classes ŽCatchMClass:ARX(m,q) and CatchMClass:ARMA(p,q). are associated with the generic domain class. This allows the modeller to produce a series of model instances, coupling the domain objects with the model classes. In this way, for instance, CatchModel\_A can be generated which is an instance of CatchMClass:ARX(m,q)

![](/api/attachments/HJKVBFDW/fulltext/images/8705002d6cd9ec4ffad9e1a2c816d12b68f3e79e9c3946c4065e852fd0fdb783.jpg)  
Fig. 7. The domain base and the model base can be combined to create new models.

and the CatchModel\_B, which is an instance of CatchMClass:ARMA(m,q), both applied to the case of the Tresa Catchment.

The advantage of this model and data organisation is more evident when assembling compound models. In Fig. 8, two compound models of the Lake Maggiore water system differ by the catchment model instances they use: the ARX or the ARMA models. In this case, model substitution is performed automatically by the MMS: the new model instance knows where to gather the input values and where to store its outputs, without any further user intervention, since all the required knowledge is embedded in the model class.

Model interchangeability is not always a straightforward process. Interchangeability is not independent of interconnection. A model can substitute for another only if both comply to the same interface requirements. For instance, model CatchModel\_A Ž . in Fig. 8 does not require a value for the rainfall $w _ { t + 1 }$ which is instead required in model Catch-Model\_B. While this case does not stop the compound model to work, since there is an ‘overabundance’ of model inputs, it could happen a situation where substituting a model with one endowed with a bigger input interface set can render the compound model unusable.

In such cases, model substitution cannot be delegated to the system and the user has to decide whether another model should be used or the domain and model classes need a re-design phase.

## 6. Putting the MMS to work

This section reports an example of how the proposed MMS framework is applied. One of the authors of this paper has been implementing a decision support system for the operations of multi-purpose reservoirs 26 . This system requires models for opti- <sup>w</sup> <sup>x</sup> misation—to generate a reservoir management policy and to suggest operation decisions—and simulation—to assess policy performance and its impact. For this reason, the models must be handled by ‘optimisation engines’ solvers and ‘simulation en- Ž . gines’ simulators . Ž .

The optimisation engine implements the Bellman dynamic programming algorithm 2 to find an opti- <sup>w</sup> <sup>x</sup> mal solution to the problem. The system analyst who wants to produce a policy can ‘plug-in’ one of the models which were devised for this purpose. The MMS provides the software architecture which makes the solver independent from the model formulation. Fig. 9 shows how the model of the Maggiore Water

![](/api/attachments/HJKVBFDW/fulltext/images/fa1a7f2e0912e8003eb14c4895acd8e87a7c4fb69304d99ded8b30dee5db37cc.jpg)  
Fig. 8. Model substitution for the Maggiore Water System.

![](/api/attachments/HJKVBFDW/fulltext/images/18c7b0bdbb645ecc6e7539e3afb4bf659462fcfa2a2fde41250e9d07ac899ce4.jpg)  
Fig. 9. A regulator for the Maggiore Water System is produced using a solver.

System is linked to the solver: the input interface of the compound model fetches its values from the solver, according to the dynamic programming search routine, all the values for the model inputs are tried and the cost $g _ { t + }$ and system state $x _ { t + 1 }$ Žthe couple $c _ { t + 2 }$ and $s _ { t + 1 } )$ are fed back into the solver. The solver also needs a decision model which defines the performance indicator J and the constraints.

The same solver can be used to solve another model, with a different input and output interface.

The solver, in fact, reads the characteristics of the model interface to generate the appropriate ‘stimuli during the optimisation algorithm. Typically, the solver reads the discretisation characteristics of the input variables to be able to appropriately span the ranges of the input variables with all the possible values in the discrete sets.

The result of the optimisation is a regulating policy which returns the amount of water to be released given the time and the state values. Since the catchment state is not observable, it must be reconstructed by a Kalman filter 2 . Therefore, the<sup>w</sup> <sup>x</sup> policy and the state re-constructor make up a regulator model which is used to produce the regulating decision. Fig. 10 shows how the regulator is used to produce daily decisions of water release. This time the solver is a simulator which feeds time series for rainfall Ž Ž .. w t and for observed catchment runoff Ž Ž ..a t . These measurements are used either to feed the simulated model and to reconstruct the non-observable part of the systems’ state.

![](/api/attachments/HJKVBFDW/fulltext/images/94e6517644240767d82fcf1f6e07d0bb3062a70a29ef29ac1f83262fe2f8723d.jpg)  
Fig. 10. Simulation of the Maggiore Water System.

The MMS we have presented here has been embedded in a DSS and used to explore the impact of alternative interventions on the management of Lake Maggiore, which is located at the border between Italy and Switzerland. The capability of testing different models against the same data sets was an asset in evaluating the management alternatives 29 . <sup>w</sup> <sup>x</sup>

## 7. Conclusions

The Model Management System presented in this paper shows how the modelling knowledge and the available data, represented in the domain base, can be organised in order to enhance model integration and re-use. Models are linked to domain classes of objects and they communicate through their interfaces. Models are therefore separated from a particular domain object, and can be re-used in problems that have a similar structure. The approach proposed here fulfills the requirements of an effective MMS Ž .Section 2 .

Ž . 1 The proposed architecture helps the modeller abstract the model from the data, thereby making it easier to re-use existing models and create new ones.

Ž . 2 Models are associated with domain classes which are real world entities or processes. Thus, models are related to representations of the modelling domain that have a meaning to the user.

Ž . 3 The MMS is deliberately designed to allow models to be linked together. Linkage is achieved via the model interfaces.

Ž . 4 The MMS has the same capabilities as a DBMS. Models can be stored, retrieved, deleted, and edited as if they were data items in a data base. Domain objects and models can be made persistent and therefore be treated as data items.

Ž . 5 Domain classes provide meta-level data descriptions used by models to access data types.

Ž . 6 The ability to associate a basic model with a compound domain class leads to a seamless integration of a ‘legacy’ model into the MMS.

In particular, it is relevant to notice the separation between the models and the data descriptions. The MMS approach presented in this paper gives data the same standing as models by the definition of domain classes. This design solution allows the re-use of data, not only of models, thus allowing the user to easily create modelling alternatives which can be applied to the same data sets.

The MMS design presented here is currently being implemented in the ‘Open Modelling’ software <sup>w x</sup> <sup>w x</sup> 25 , in the HYDRA project 11 and in a two-level Decision Support System for the operations of reservoir networks 26 . Although this design covers the<sup>w</sup> <sup>x</sup> requirements of a MMS, many practical details have to be settled during the implementation. Modelling using such software designs represent a major step towards more efficient modelling and, given the importance of predictive models to DSSs, more efficient DSS development.

## Acknowledgements

The authors gratefully acknowledge the anonymous referees for their constructive comments which helped to shape the paper in its final form. The first author wants to thank Professor Soncini-Sessa of Politecnico di Milano Italy for the many insightfulŽ . discussions on the subject of management and control of reservoir networks.

## References

<sup>w</sup> <sup>x</sup> 1 D. Abel, K. Taylor, D. Kuo, Integrating modelling systems for environmental management information systems, ACM-SIGMOD 26 1 1997 5–10.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 D.P. Bertsekas, Dynamic Programming and Optimal Control, Athena Scientific, MA, 1995.

<sup>w</sup> <sup>x</sup> 3 H.K. Bhargava, S.O. Kimbrough, Model management: an embedded languages approach, Decision Support Systems 10 Ž . 1993 .

<sup>w</sup> <sup>x</sup> 4 R.W. Blanning, R. Krishnan, R. Muller, Decision support on ¨ demand: emerging electronic markets for decision technologies, Decision Support Systems 19 3 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 G. Booch, Object-Oriented Analysis with Applications, 2nd edn., The Benjamin<sup>r</sup>Cummings Publishing, Redwood City, 1994.

<sup>w</sup> <sup>x</sup> 6 D.R. Dolk, J.E. Kottemann, Model integration and modeling languages: a process perspective, Information Systems Research 3 1 1992 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 D.R. Dolk, J.E. Kottemann, Model integration and a theory of models, Decision Support Systems 9 1993 .Ž .

<sup>w</sup> <sup>x</sup> 8 L. Del Furia, A. Rizzoli, An Integrated Modelling Environment for Object-Oriented Simulation of Ecological Models, Proceedings of the 26th SCS Annual Simulation Symposium, Washington, DC, March 29–April 1, 1993.

<sup>w</sup> <sup>x</sup> 9 B. Falkenheimer, K.D. Forbus, Compositional modelling: finding the right model for the job, Artificial Intelligence 51 Ž . 1991 95–143.

<sup>w</sup> <sup>x</sup> 10 P.A. Fishwick, Qualitative methodology in simulation model engineering, Simulation 52 3 1989 .Ž . Ž .

<sup>w</sup> <sup>x</sup>11 J.R. Davis, D.J. Abel, D. Zhou, A. Rizzoli, P. Kilby, HY-DRA: a Generic Design for Integrating Catchment Models, Presented at the American Society of Civil Engineers 21st Annual Conference on Water Resources Planning and Management Division, Denver, CO, 22–26 June 1994.

<sup>w</sup> <sup>x</sup> 12 DMSO, High Level Architecture http: Ž . <sup>rr</sup>hla.dmso.mil .

<sup>w</sup> <sup>x</sup> 13 G. Guariso, H. Werthner, Environmental Decision Support Systems, Ellis Horwood, Chichester, 1989.

<sup>w</sup> <sup>x</sup>14 G. Guariso, E. Tracanella, L. Piroddi, A.E. Rizzoli, A web accessible environmental model base: a tool for natural resources management, in: D. McDonald, M. McAleer, A. Jakeman Eds. , Proceedings of MODSIM 97, Hobart, Tas-Ž . mania, 8–11 December 1997 GAIA is available on-line atŽ http:<sup>rr</sup>www.ess.co.at<sup>r</sup>GAIA<sup>r</sup>..

<sup>w</sup> <sup>x</sup> 15 B. Henderson-Sellers, J.R. Davis, I.T. Webster, J.M. Edwards, Modern tools for environmental management: water quality, in: A.J. Jakeman, M.B. Beck, M.J. McAleer Eds. ,Ž . Modelling Change in Environmental Systems, Wiley, New York, 1993.

<sup>w</sup> <sup>x</sup> 16 S.N. Hong, M.V. Mannino, B. Greenberg, Measurement theoretic representation of large, diverse model bases: the unified modeling language LU, Decision Support Systems 10 Ž .1993 .

<sup>w</sup> <sup>x</sup> 17 M. Knorrenschild, R. Lenz, E. Foster, C. Herderich, UFIS: a database of ecological models, Ecological Modelling 86 2–3Ž . Ž . 1996 141–144, UFIS is available online at http:<sup>rr</sup> www.gsf.de<sup>r</sup>UFIS<sup>r</sup>ufis<sup>r</sup>ufis\_proj.html.

<sup>w</sup> <sup>x</sup> 18 H. Lieberman, Using prototypical objects to implement shared behavior in object-oriented systems, Proceedings of OOP-SLA-86, Portland, OR, 1986.

<sup>w</sup> <sup>x</sup> 19 M. Minsky, A framework for representing knowledge, in: P.H. Winston Ed. , The Psychology of Computer Vision, Ž . McGraw-Hill, New York, 1975.

<sup>w</sup> <sup>x</sup> 20 W.A. Muhanna, SYMMS: a model management system that supports model reuse, sharing, and integration, European Journal of Operational Research 72 1994 100.Ž .

<sup>w</sup> <sup>x</sup> 21 A. Nardini, C. Piccardi, R. Soncini-Sessa, On the integration

of risk aversion and average-performance optimization in reservoir control, Water Resour. Res. 28 2 1992 487–497.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 K. Parsaye, M. Chignell, S. Khoshafian, H. Wong, Intelligent Databases: Object-Oriented, Deductive, Hypermedia Technologies, Wiley, New York, 1989.

<sup>w</sup> <sup>x</sup> 23 F. Pichler, R. Moreno-Diaz Eds. , Computer Aided Systems Ž . Theory-EUROCAST ’89, Lecture Notes in Computer Science, Vol. 410, Springer-Verlag, Berlin, 1990.

<sup>w</sup> <sup>x</sup> 24 W.D. Potter, T.A. Byrd, J.A. Miller, K.J. Kochut, Extending decision support systems: the integration of data, knowledge, and model management, Annals of Operations Research 38 Ž . 1992 .

<sup>w</sup> <sup>x</sup> 25 A. Rizzoli, J.R. Davis, M. Reed, T. Farley, A DSS for catchment management, in: P. Zannetti Ed. , EnvironmentalŽ . Modelling, Vol. 3, Computer Methods and Software for Simulating Environmental Pollution and its Adverse Effects, Computational Mechanics Publications, Southampton, 1996.

<sup>w</sup> <sup>x</sup> 26 A. Rizzoli, R. Soncini-Sessa, Integrating and complementing human experience in water management with a two-level DSS, in: F. Burstein, H. Linger, H. Smith Eds. , Proceed-Ž . ings of the Workshop on Intelligent Decision Support, IDS ’96, Melbourne, 9 September 1996.

<sup>w</sup> <sup>x</sup> 27 P. Robertson, Integrating legacy systems with modern corporate applications, Communications of the ACM 40 5 1997Ž . Ž . 39–46.

<sup>w</sup> <sup>x</sup> 28 J.W. Rozenblit, P.L. Jankowski, An integrated framework for knowledge-based modeling and simulation of natural systems, Simulation 57 3 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 R. Soncini-Sessa, D. Canuti, A. Colorni, E. Laniado, F. B. Losa, A. Rizzoli, L. Villa, B. Vitali, Planning and management of a transnational water system, the case of Lake Maggiore, Italy–Switzerland, Presented at: International Workshop on barriers to Sustainable Management of Water Quantity and Quality, 12–15 May 1998, Wuhan, China.

<sup>w</sup> <sup>x</sup> 30 M. Stefik, D.G. Bobrow, Object-oriented programming: themes and variations, AI Magazine 6 4 1986 .Ž . Ž .

31 R.H. Sprague, Jr., E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

<sup>w</sup> <sup>x</sup> 32 B.P. Zeigler, G. Klir, M. Elzas, T.I. Oren, Methodology in Systems Modelling and Simulation, North-Holland, Amsterdam, 1979.

<sup>w</sup> <sup>x</sup> 33 B.P. Zeigler, Object-Oriented Simulation with Hierarchical, Modular Models: Intelligent Agents and Endomorphic Systems, Academic Press, New York, 1989.

![](/api/attachments/HJKVBFDW/fulltext/images/a6acd57d17966a89e221e6b3c6b1ce99a4fee9706f43dca626a628a16f4405d3.jpg)  
Andrea E. Rizzoli is a researcher with IDSIA in Lugano CH . He received aŽ . PhD from Politecnico di Milano in Control Engineering in 1991. His interests are in modelling and simulation of environmental and industrial processes.

![](/api/attachments/HJKVBFDW/fulltext/images/8ceb31dfef7f0013cb5b3bc290f9445ae45f2998c358369a0308379b14e76aa7.jpg)

J. Richard Davis has a PhD in physics. Over the last 10 years he has been developing decision support systems for a variety of environmental management problems. These include nutrient management in watersheds, effluent management from intensive rural industries and establishing flow requirements for aquatic biota. Some of these DSS are in use by management agencies around Australia. He is currently Leader of the CSIRO Urban and Rural Water Management program, and is based in Canberra.

![](/api/attachments/HJKVBFDW/fulltext/images/16434542eaf0337243c219da94457ed36c265e0eb3bd21188684d3205fadf01d.jpg)  
David J. Abel is a Science and Industry Manager and a Chief Research Scientist with CSIRO Mathematical Information Sciences. After a PhD James CookŽ University of North Queensland in Sys-. tems Engineering in 1978, he has specialised in Spatial Information Systems. Current interests are integrated systems, spatial database and information infrastructures.
