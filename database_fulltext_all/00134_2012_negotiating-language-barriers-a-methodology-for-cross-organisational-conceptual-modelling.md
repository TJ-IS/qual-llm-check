---
otero_id: 134
otero_key: "GXG965FJ"
title: "Negotiating language barriers – a methodology for cross-organisational conceptual modelling"
authors: "Gunnar Dietz; Martin Juhrisch"
year: "2012"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2011.30"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ARTICLE

# Negotiating language barriers – a methodology for cross-organisational conceptual modelling<sub>w</sub>

Gunnar Dietz<sup>1</sup> and Martin Juhrisch<sup>1</sup>

<sup>1</sup>Department of Mechanical Engineering, Institute of Machine Tool and Control Engineering, Dresden University of Technology, Dresden, Germany

Correspondence: Gunnar Dietz, Department of Mechanical Engineering, Institute of Machine Tool and Control Engineering, Dresden University of Technology, Kutzbach-Building (R 205), D-01062 Dresden, Germany. Tel: þ 49 (351) 463-33615; Fax: þ 49 (351) 463-37073; E-mail: mail@gdietz.de

## Abstract

In common scenarios conceptual modelling is a methodology that – using semi-formal languages – has a high degree of freedom and is used to visualise certain aspects of a problem domain. However, especially in cross-organisational or international scenarios this freedom leads to many inconsistencies and conflicts. Therefore the restriction of the freedom of modelling is often discussed in the literature to counter the missing standardisation and to enhance the comparability of models. However, to be able to express certain concepts embedded within some distinguished environment (purpose, culture, infrastructure, language, terminology) models have to be domain-specific on the one hand, but comparable to models in other domains on the other hand. In this article a new approach is presented that offers a framework for restricted modelling without destroying the adaptability to certain different domains. The methodology includes an algorithm for comparing models in different domains and is therefore capable to not only dissolve certain standard comparability conflicts but also the domain conflict. European Journal of Information Systems (2012) 21, 229–254. doi:10.1057/ejis.2011.30; published online 20 September 2011

Keywords: conceptual modelling; description kits; restricted modelling; domain conflict; model transformation

## Introduction

Conceptual modelling offers a framework and methodology to describe several – usually IS-based – phenomena using semi-formal languages. In general, models are used to clearly exemplify certain ideas, concepts, requirements, conditions, implementations, etc. They share a broad freedom of expressing reality and may be used in several domains and cultural or organisational backgrounds.

Because of this broad freedom, model transformations are considered even in limited settings (e.g. a small company). At a very high level the information in analysis models can be used as a basis to create design models. In more specialised scenarios, models for the organisational structure or models of the IT infrastructure can be used to create a model of organisational roles as a basis for access management (see Dietz et al, 2009).

Another example is the comparison between processes based on their process models. A potential application would be the certification of companies according to the standards of ISO 9000–9004. A model-based certification of companies provides an automated verification of their process quality based on models from different organisational units or business divisions. A similar case is process benchmarking (see Horvath & Gleich, 1998, p. 326). A model-based identification and evaluation of performance gaps implies, in addition to the integration of distributed developed process models, the implementation of domainspecific ratios into the models, and, afterwards, their automated analysis.

To compare models or to transform models is a highly manual task including several stakeholders, especially domain experts. Comparison is even more difficult in a cross-organisational or international scenario because models are not only influenced by different language concepts, but also mirror cultural background and differing levels of technical development. One example is the change from procedural development via objectoriented development to service-oriented development paradigms. This example makes clear that comparability of certain ideas exemplified with different backgrounds is hard to establish, no matter how explicitly they were expressed in conceptual models.

To enhance the comparability of models and to resolve certain (language-based) conflicts, the restriction of freedom in conceptual modelling is especially discussed under the aspect of model integration in shared modelling projects (see Becker et al, 2006, p. 111). Within the scope of conceptual modelling, companies are systematically analysed and mentally reconstructed by means of semi-formal modelling languages (see Wand & Weber, 2002, p. 363; Khatri et al, 2006, p. 81; Soffer & Hadar, 2007, p. 599). The resulting models then are used in projects that reorganise or reconstruct certain aspects of the company (like information systems or business processes).

To summarise, we are faced with the problem of effective model comparison. The goal is to provide a basis for an automated analysis of models, where previously an extensive manual analysis was necessary. The aim of this article is to present a new modelling methodology consisting of a framework, called the Description Kit Approach (DKA), that improves usability for model comparisons. The main idea is the introduction of guidelines that allow the establishment of an adaptable consensus for restricted modelling by bridging the gap between language creation and language usage.

The article is structured as follows: After this introduction the research methodology that is used for developing the proposed framework is described. Then the modelling problem is defined and literature is reviewed with special attention to domain-specific modelling languages. The next section is the starting point for the development of the method and especially contains a requirements analysis. The main idea for solving the research problem is a set of guidelines. which are discussed in the next section. That section also contains a discussion on classic approaches, especially domainspecific languages. The idea of guidelines is then brought to life in the DKA, which serves as a demonstration of the research artefact. The approach is then evaluated in a detailed proof-of-concept before the article concludes with a discussion and ideas for further research.

## Research methodology

The authors use the paradigm of Design Science (see Peffers et al, 2008, p. 48). Scientific knowledge is gained by creating and evaluating artefacts in the form of languages, models, methods, or systems (see Walls et al, 1992, p. 41).

The design science approach was selected as the research methodology because it addresses important unsolved (practical) problems in a unique and innovative way or addresses some solved problems in a more effective way.

In contrast to other research, the aim of design science research is not necessarily to evaluate the validity of research results with respect to their truth, but to assess their usefulness to create artefacts as tools to solve certain problems (see March & Smith, 1995, p. 253; Hevner et al, 2004, p. 82).

The resolution of (practical) business problems is typically linked with a real world domain. Hence, research results are usually complex artefacts designed in an iterative, creative design research process (see Vaishnavi & Kuechler, 2004). Since this complexity makes it hard to determine the contribution of design research results to the IS knowledge base, Hevner et al proposed seven guidelines of design science. These guidelines arise from the need to document and trace the decision-making process and the underlying information like requirements, design proposals, and development records.

Design science can be done in a theory-based way or independent of any theory (see March & Smith, 1995, p. 254). If the research is theory-independent, the evaluation of the artefacts is of high relevance since the development of a theory, as a basis for the method design, is omitted. In that case, in contrast to the rigorous theory-based approach, the creation of the design in question does not necessarily need to be based on certain hypotheses.

In the present article we adopt a theory-based design because of its higher precision. Under a theory we understand a set of hypotheses in the shape of causeand-effect relationships (see Briggs, 2006, p. 573; Gregor, 2006, p. 611; Gehlert et al, 2009, p. 445). On the basis of existing theory fragments, hypotheses are implicitly explored and integrated. The necessary hypotheses for designing the method are deductively formulated. Following the research method presented in Peffers et al (2008, p. 48), the research process is structured as follows.

Identification of the problem. Outline the research entry point by defining the problem and showing its importance.

Definition of the research objective. The design process starts with the definition of the objectives for the method to present.

Building the requirements. The objective is further decomposed into requirements. This decomposition process serves two purposes: First, the design process can be traced more easily by specifying what constitutes this objective. Second, the decomposition of an objective into requirements allows for the evaluation of the IT artefact.

Demonstration of the artefact using design research. A prototype is developed and then tested.

Evaluation of the artefact. The method is exemplarily used in the form of a proof-of-concept (see van der Aalst & Kumar, 2003, p. 32).

In the context of the current research we can summarise this process as follows: A method is developed that allows automated utilization of semi-formal models. Hypotheses are derived from literature and mapped to requirements. The method is first designed, then implemented, and finally used in an example.

## Definition of the research objective

Information and knowledge has always played a fundamental role for solving problems. This includes for example decision making in business management or design decisions in software development projects – or even normal life. Nowadays the main problem is not anymore the availability of information, but instead the need to find, evaluate, combine, and utilise useful information that already exists.

Which role information exactly plays in a certain scenario depends highly on the domain where it is to be used. This may be a different domain from the domain where it comes from. As a consequence, information exists in uncountable forms. Information and knowledge has to be transferred and communicated from one domain to other domains. Languages take a central role in this process and form both a solution and a barrier for communication. The first step in utilising information is to understand it, which is only possible, when the information is put into the right form and communicated in the right language.

## Objectives for a model-driven solution

Information and knowledge have to be prepared, before they can be utilised. Informal and semi-formal models offer an abstract and informal way to represent information and knowledge. Graphical representations like entity-relationship diagrams, data-flow diagrams, statetransition diagrams, etc. are easy to understand both for the expert and the non-expert and therefore facilitate the communication between persons from different domains. Formal languages allow one to describe a certain phenomenon uniquely and precisely, but with a high level of abstraction of reality. They can be easily evaluated and verified or be used to automate certain tasks, but are limited in their flexibility to express realworld phenomena. Semi-formal languages offer a good compromise between the flexibility of natural language descriptions and formal descriptions.

Models offer several advantages. They allow a more efficient and more goal-oriented way to document and solve problems. They encapsulate complexity and visualise facts in a more standardised and more easy to understand way. Because of that, models can facilitate communication and can be used to automate certain tasks. The creation and use of models is supported by certain tools, which also allows the reusability of models for several use cases.

These advantages are the driver for addressing the main goal of this research – to offer a methodology to negotiate language barriers in cross-organisational scenarios – by a model-driven approach. They transfer into objectives for the presented methods. We will discuss in the following part that standard modelling methods still do not successfully solve the problem. Solving these issues not only helps in contexts, where modelling is already used, but may also open up the advantages of modelling for scenarios, where modelling is currently not used. After some discussion a requirements analysis is done to formulate more concrete objectives for the method.

## Definition of the modelling problem

Larkin and Simon discuss the aptitude of models to structure, describe, and analyse an unstructured problem (see Larkin & Simon, 1987, p. 65). Only after completing these three tasks is it possible to solve a problem within the modelling ‘reality’ and to transfer it back to the problem domain (see also Frank, 1999, p. 695).

A modelling method, however, only considers the creation of models. That means the methodology deals not with the model work itself, like to modify or transform a model or to compare models. Operations on the models that allow the solution of a problem within the modelling itself are not considered in most cases. If a method both addresses the creation of models and also the usage for solving problems, we refer to it as a model-based method.

The following scenario gives an example of when the potential for a model-based method will become clear: Consider a company that has business divisions in several countries. The development and launch of a new corporation-wide application system requires full transparency about the organisational structure and the process organisation for each division. The classic case for model-driven software development uses models within the analysis phase to illustrate the technical requirements for the application system (see for example Mellor & Shlaer. 1991: Pastor & Ramos

1995). Requirement models are the result of the analysis of the business requirements and use semi-formal descriptions in conceptual models. They are the basis for further development of design models or implementation models.

The starting point is the elicitation of the actual state in all relevant business domains or real world domains in the form of organisational analysis models. Then a comparison of models or parts of these models (we refer to ‘sub-models’) must be done to detect any overlapping areas of responsibility offering the same or similar services. This comparison is likely to result in the integration of all sub-models into a general model.

For the subsequent technical design, the general analysis model has to be transferred to an organisational target-state model (see Karow & Gehlert, 2006, p. 3913). This target-state model might focus on a service level enhancement by restructuring the organisational structure and process organisation. It can also include functional requirements for a new application system that should be developed (see Rosemann, 2007, p. 97). This description of a software solution from an exterior viewpoint corresponds to the natural ideas of domain experts about the application system (see Suhl & Blumstengel, 2002, p. 351). After the analysis phase, the software design can start. That involves a model-based description of the internal structure of the software system. This description contains software components and their relations (e.g. classes and functions) (see Bass et al, 2003, p. 10; Rosemann, 2007, p. 57).

In addition to model creation there is the problem of model integration. The organisational structure and process organisation can only become transparent by integrating all process and data models that were created independently. As a consequence, one has to deal with several models from differing projects, differing times of creation, and differing organisational divisions. These divisions may have their own differing methods for visualisation and levels of abstraction or even simply speak their own language. All these differences of course create a consistency problem that makes the integration of models very difficult.

The process of integrating semi-formal models is not trivial nor can it be done completely automatically. It is an iterative process mostly done by hand. The identification of equalities or similarities is far from easy and can only be done with the manual help of domain experts. Admittedly, there are already methods for the integration of semiformal models, but their application is limited when using them with highly interrelated models that come from different languages and cultures, as with international projects (see Bernstein et al, 2000, p. 55; Mikkonen & Pruuden, 2001, p. 52; Caruso & Umar, 2004, p. 9; Gehlert, 2007, p. 109). The integration becomes even more complicated by the desire to be able to react quickly to changing requirements, for example due to acquisition of new divisions, outsourcing, globalisation, new partnerships, or simply changing business processes.

An increase in the efficiency of requirements analysis could be achieved if the problem of the integration of distributed models could be done completely automatically (see Mellor & Balcer, 2002; Schmidt, 2006, p. 27). It means that algorithms, based on a set of rules, could perform the necessary model operations. Consequently, the necessary knowledge to perform the integration could be reduced, which in turn would reduce necessary time and expenses.

Independent from the presented scenario, this article also focusses on each kind of problem that arises from the need of creating models in different domains with a goal to integrate these models.

## Design and development

To design and develop the proposed approach, the research objectives are decomposed into requirements. This is done after the research problem and related state of the art is further discussed. A set of potential integration conflicts is identified and analysed to prepare for the requirements analysis. They are later used for demonstrating the functionality of the approach and its architecture. We use the use theory of semantics to provide a theoretical framework, in which the approach embeds, as well as the theory of domain-specific modelling and recent works on modelling conflicts as a theoretical basis for the method development.

## Theoretical background

This article emphasises conceptual process models (for example UML activity diagrams). Such models describe the behaviour of a system with the help of a sequence of states and transitions. In particular, business process models are always bound to some material domain. Their semi-formal degree of precision allows for the automatic performance of simple operations on them, such as consistency checks.

Process models are not typically designed by a single modeller or in a single modelling project. Empirical research shows that process models produced in a distributed modelling project vary in the vocabulary used, the level of abstraction, the level of detail, and the covered domain (see Hadar & Soffer, 2006, p. 568).

The high degree of freedom in conceptual modelling and the lack of standardisation of model elements in semi-formal modelling languages both lead to a series of conflicts when trying to integrate or merge conceptual models (see Pfeiffer & Gehlert, 2005, p. 109; Pfeiffer, 2007, p. 880; Rosemann, 2007, p. 41–78). For example, references across different models cannot be easily detected if these models use different systems of concepts; furthermore, it is hard to detect where two models overlap or describe the same phenomena if the level of abstraction varies between these models. The different types of integration conflicts are summarised in Table 1 and illustrated in an example in Figure 1.

Since the need for model comparisons calls for methods to reduce these barriers, Domain-specific Modelling Languages (DSML) have been recently established (see Kieburtz et al, 1996; Long et al, 1998; Sztipanovits et al, 1998; Kelly & Tolvanen, 2000; Becker et al, 2007a). To facilitate the construction of comparable models, domain-specific modelling approaches take corrective action within the process of model creation (see Becker et al, 2007a, p. 270). These approaches are based on the following hypothesis:

Fundamental Hypothesis. In order to obtain comparable results in a distributed modelling project, the degree of freedom of a modeller must be restricted (see Becker et al, 2007a). Limiting the degree of freedom in modelling increases the quality of the model in terms of model comparison (see Lindland et al, 1994, p. 42; Schu¨tte & Rotthowe, 1998, p. 240; Krogstie et al, 2006, p. 91).

Table 1 Integration conflicts in modelling (see also Figure 1)

<table><tr><td>Conflict</td><td>Definition</td></tr><tr><td>Language conflicts</td><td>Language conflicts affect the labels of model elements to compare. The avoidance or solution of homonyms and synonyms is the first prerequisite for model comparison.</td></tr><tr><td>Structure conflicts</td><td>Each modeller has the freedom to describe his domain at a specific level of abstraction and may choose a certain degree of detail. This leads to so-called structural conflicts.</td></tr><tr><td>Type conflicts</td><td>Type conflicts arise from the choice of varying choices of an appropriate grammatical concept for modelling.</td></tr></table>

The essence of the restriction of the freedom in modelling using DSMLs is the limitation of the language vocabulary to a number of domain-specific and semantically disjoint language constructs. PICTURE (Becker et al, 2007b), for example, presents a method that can be used for restricting the freedom in modelling to a certain set of domain-specific language constructs. PICTURE is a domain-specific modelling language that has been specifically developed for use in public administrations. Its modelling concepts represent information processing activities repetitively conducted in public administrations.

The basic hypothesis here is that the modellers are aware of the semantics of the domain-specific concepts and therefore do not choose inappropriate elements. With the elimination of type, synonym, homonym, and abstraction conflicts, the model comparison would be reduced to a syntax level. The restriction of the available terminology is flanked by a specific process modelling language with a simple syntax. Like every situation-specific modelling language, a DSML is created by a method developer as an artefact (see Harmsen et al, 1994, p. 218; Brinkkemper, 1996, p. 277). Meta-CASE tools support the creation of situation-specific modelling languages since they allow modelling in two phases (see Kelly et al, 2005). These two phases are the following:

Language creation. Language creation (or definition) means to define the syntax and the semantics of a (modelling) language using a meta-language in a metamodel. If the meta-language is in turn interpreted as a modelling language, we speak of a meta-modelling language.

![](/api/attachments/GXG965FJ/fulltext/images/4a19274b4ae886ab8ac0c131bd6edc33a93e67cd9e0ea7d22084d3cf94f51ba5.jpg)  
Figure 1 Integration conflicts (following Pfeiffer, 2007, p. 881) (‘bank’ on the left side is the term used in this organisation to refer to a bank (row) of seats).

Language usage. Language usage means the use of the modelling language to describe a certain issue.

Domain-specific language constructs and a simplified version of modelling will significantly facilitate the subsequent comparison of models. However, we will show that this is only possible at the expense of a decreased usability of these models in their domains. The restrictions are achieved by limiting the expressive power of the modelling language on the meta-model layer. The modeller is thus limited in the number of possible language constructs available to represent the intended meaning of the described facts. Conventions to restrict the modelling freedom may specify model elements, their attributes, and even their attribute values. Domain-specific constraints of the modelling language always have an impact on an appropriate process model of the modelling method. However, this applies in any case to all situation-specific developed modelling methods (see Harmsen et al, 1994, p. 218; Brinkkemper, 1996, p. 277).

The main assumption about domain-specific modelling is that the modelling grammar is designed to allow only exactly one linguistic construct for the modelling situation in question (see Pfeiffer, 2008, p. 120). The assumption can, however, only be valid for a (then) formal language. While the modelling grammar can be derived from the technical or business language, it is not possible to fully avoid inappropriate modelling constructs. There are two reasons:

\- Improper notion of semantics: Existing approaches about DSML are based on a relatively simple understanding of semantics (see below) to support the idea of creating a set of non-overlapping language concepts that can be fixed in a DSML.

\- Applicability to only one domain: The use of a DSML is limited to just one domain, namely the one the language was developed in. Thus, even if it may be possible to develop a set of non-overlapping language concepts, it would not help us in the multi-domain scenario that is discussed in our research.

Semantics studies the meaning of linguistic terms and tokens and is part of semiotics (which also includes syntactics and pragmatics). There are several different theories and even more opinions on the validity of these theories. Existing DSML approaches often use Idea Theory (see Locke, 1994, p. 59 and Lyons, 2000, p. 625). In this theory semantics is considered as the idea (the conception or the concept) that is associated with the linguistic expression. However, ideas cannot clearly be determined since they vary from person to person.

Another theory often used is Reference Theory (see Lyons, 1995, p. 78 and Deutsch, 2009, p. 446), which considers the semantic of a word even as a (direct or indirect) relationship of a token or term to the object or fact it refers to. However, one linguistic term can in fact refer to several objects or facts; vice-versa one object or fact can be represented by more than one term. A one-to-one relationship between terms and their meaning is therefore hard to achieve.

In this study we prefer a more recent position, the Use Theory, which goes back to Wittgenstein and has been extended with respect to constructivistic ideas by Lorenzen (see Lorenzen, 1973, p. 248; Wittgenstein, 2000, p. 77). This theory states that the meaning of a linguistic expression is defined by its use (see Lyons, 1995, p. 40 and Wittgenstein, 2000, p. 77). The meaning of a linguistic expression is the result of its perpetual concrete application in speech. The semantic follows from the context. In the process of using a word, its meaning gets continuously updated. To determine the meaning of a word, all rules for using certain linguistic terms must be adequately described. This is the case if all base words are introduced exemplarily and all other words are determined either by definition, subordination, contrariety, or continuity. Two linguistic terms therefore have the same meaning if and only if all rules for using them are equal (see Lorenzen, 1973, p. 248). This theory better reflects the nature of living and evolving languages and provides a good theoretical foundation for this research and its multi-domain scenario.

The use theory alone does not offer a solution for the above-mentioned problem of improper semantics for classic modelling approaches. In contrast, it creates the challenge of reshaping the modelling process to reflect this understanding of semantics. Only then can the use theory be applied in a useful way. This is the aim of the following discussion, which will lead to the requirements analysis and later on to the idea of guidelines in modelling and the creation of the DKA.

Domain-specific model elements nearly always include a semi-formal part (in the form of a free text). This can be summarised in the following assumption:

A1: The semantics of expressions in semi-formal modelling languages cannot be reduced to syntactic structures.

It may be said that domain-specific languages eliminate integration conflicts. However, the success is limited because the avoidance of these conflicts is secured by reducing the applicability of the models in their individual domains. Furthermore, since domain-specific ontologies are needed to create DSMLs, the limited availability of such ontologies is also a problem. In addition, a DSML ought to grow naturally, so that its vocabulary and grammar are not static. Consequently, recent DSMLs have in most cases too few language constructs to represent all the phenomena in their respective domain. The definition of domain-specific language constructs on the meta-model layer seems problematic in the context of this dynamic change (see Weller & Esswein, 2006, p. 132). Rarely does the literature on DSML discuss theoretical problems associated with meta-models that change over time. A generic approach is necessary to meet the dynamic nature of a domain language.

In addition, there are obstacles that always occur when a new modelling language is established in an organisation (see Pfeiffer, 2008, p. 124). Consider, for example, the case where an organisation-wide standard for the modelling of business processes was previously established that contradicts a transition to the new modelling language. A significant effort for the migration or the conversion of existing process models to the (new) domain-specific language is needed if the transition should be done nevertheless.

## The domain conflict

In the discussion about integration conflicts it is always assumed that the underlying domain that should be modelled does not change. Thus, in a comparison between two models it is assumed that both models describe the same domain. It therefore only makes sense to try to avoid integration conflicts if comparing two conceptual models describing the same real world phenomena. The comparison of conceptual models across companies or countries, however, poses another potential conflict that arises from the change of the domain. For this scenario we introduce the concept of a domain conflict.

A domain conflict results from the desire to compare models out of different domains. The term domain here means a certain viewpoint: A certain kind of representation or specific method to describe real world phenomena in an abstract way. The domain has an impact on, generally speaking, the behavioural pattern – and modelling is a behavioural pattern. Thus, a domain is defined as the interaction of the psychological imprinting and the impact of the environment. It therefore represents a group of persons belonging to this domain in the above sense. The term ‘group of persons’ is here used in an abstract way, independent of concrete persons. A domain often implies a common language (linguistic community), a common culture or country, a company or a department; or it may represent a group of persons with some notable behaviour (education, knowledge, experience, etc.). Hence, a domain represents a certain way to behave, to formulate, and to implement ideas.

The domain conflict is a consequence of a varying way of modelling in different domains or occurs because different kinds of artefacts are compared. It can be assumed that two different domains also have different approaches to describe artefacts. Consequently, model artefacts using various different diagrammatic representations are created or vary in their degree of precision. The main example comes from the problem of mapping enterprise models onto implementation models.

Figure 2 shows two alternative designs – explicated in UML notation – for a component to calculate the Laspeyres index. In the example we are confronted with the following problem: A service is required that calculates the inflation with respect to the country and a market basket of goods when given the base year. The first design was enriched with a material semantic by the developer using signifiers in natural language. The second one is completely designed using an abstract notation scheme. In addition, the country is encoded as an integer value. However, if we suppose that the problem solving algorithms are deployed appropriately, both alternatives are absolutely equivalent and similarly applicable. The material semantic inside the first alternative gets lost in the process of formalisation.

The question arises on how to deduce the meaning of the domain-specific model information in the second design and how to use this information to match this model with the model of the first design. Indeed, the qualification of the second design is not instantaneously deducible.

It is not enough to use a shared language to accomplish the model comparison. The modelling purpose at hand prevents the conceptual description within the model from being able to be done detached from the domain. In order to achieve the model comparison goal, we need a traceable connection between the conceptual description and the real world phenomena it describes with respect to the domain or implementation.

![](/api/attachments/GXG965FJ/fulltext/images/929b4857c72aaa308bc35f789c274628bfa6b721ea1f313800633251943c5d38.jpg)  
Figure 2 Domain conflict exemplified.

To summarise, based on the literature on conceptual modelling, especially domain-specific modelling, the suitability of semi-formal models as a potential input for an automated problem solving process was evaluated. This discussion was highly influenced by semantic theories, which also shed new light on the impact of DSMLs for solving integration conflicts and finally resulted in obtaining the concept of domain conflicts.

To be able to operationalise modelled information, language conflicts, structure conflicts, and type conflicts as domain conflicts have to be solved. Decisions and assessments on how to solve these conflicts must be made. This will be done in the following requirements analysis section, resulting in a requirements documentation that is later used for designing the model-based methodology.

## Requirements analysis

To solve the transformation problem a series of conflicts must be resolved. Some kinds of integration conflicts, such as homonym and synonym conflicts, can only be addressed by creating a consensus in the form of a linguistic community. Other conflicts are caused by different modelling scopes and levels of detail, or different usages of the modelling language. In addition to that, domain conflicts arise from the attempt to derive the formal nature of a model from its informal real-world domain. The different roles and the different subject areas involved in the modelling process lead to conflicts that are subsumed under the concept of domain conflict. Only by solving domain conflicts does one get two comparable models. The method has to facilitate the semantic comparison of conceptual models where the models are based on different domains. Quality requirements for models in both domains have to be kept. The requirements for the method have been consolidated below. These were argumentatively deductively deduced (see Wilde & Hess, 2007, p. 283). The foundations are a literature-based exploration of hypotheses as well as empirical findings (see Kra¨mer, 1988; Juhrisch & Esswein, 2007, p. 295; Juhrisch et al, 2008, p. 4; Juhrisch & Dietz, 2010a, p. 250).

## R1: Resolve language conflicts:

The method should resolve the semantic heterogeneity of specialised language constructs. Semantically disjoint and domain-specific language constructs should be placed at the modeller’s disposal. This idea was adopted from DSML since language conflicts are avoided. It is stressed that domain-specific concepts alone will not solve the modelling problem at hand.

## R2: Find a consensus:

To resolve language defects the method has to include the process of establishing a consensus for a terminology, which persons of different domains take an active part in.

## R3: Resolve structure and type conflicts:

To resolve structure and type conflicts the method must provide a way to organise domain-specific language constructs into a hierarchy.

## R4: Restrict conceptual modelling:

A congruent explication of real world phenomena can be obtained by a model creation process that uses conventions and guidelines. These conventions should enforce a consistent and standardised usage of the remaining freedom of the modelling language to improve the degree of automation (or to make it possible at all).

## R5: Problem-solving technique:

To resolve the domain conflict it must be possible to use artefacts from different domains commonly, or to compare these artefacts in at least a semi-automated fashion. Therefore, a procedure model or an algorithm should be available to compare certain object descriptions.

R6: User control for the model mapping:

The experts in both domains should have the possibility to have widespread control over the model mapping. Even if the method can resolve language conflicts, structure conflicts, and type conflicts, the domain conflict cannot be avoided completely. The reason for this is that the material semantic could not be completely deduced from its syntactic form. There are no conditions that allow mapping certain concepts in a unique way. Due to this fuzziness, the domain experts should be able to control the mapping results. This control includes tasks that could not be fully automated by the method, for example some parametrisation in the beginning or some decisions between alternatives during the mapping process.

## R7: Keep the domain-specific model purpose:

Restrictions to the ‘usual’ modelling process should be avoided. That means that a domain expert still should have freedom in describing reality from a business perspective, which implies that natural language constructs for this description should not be prohibited. The reason for this is that the modelling instruments really should contribute to an understanding of the models instead of hindering the modeller in expressing his/her ideas. The semantic gap between models out of different domains needs to be closed under these conditions. For this the method needs to be able to distinguish between model concepts for describing different domains.

Requirements for a method to create and then compare models have now been determined. In the following, assumptions are formulated about the environment in which the method is to be used. A successful utilisation of the method is based on these assumptions. These include A1 that was stated above.

A2: Within a linguistic community, the semantic of a language concept is invariant among its members.

A3: A modelling grammar already defines the categories of identifiable language expressions.

A4: The matching problem cannot be solved if not even one subset of common linguistic concepts is used in different domains.

A5: It is assumed that a consensus between members out of different domains can only be established for a small and limited set of linguistic concepts.

These assumptions are highly related to the discussion about semantic theories (see theoretical background), especially the use theory. Assumption A2 means the following: A ‘linguistic community’ refers to a group of persons with a common understanding of certain language concepts. Under the light of the above theories, that means that such a group uses these language concepts in the same way. This is, of course, hard to find in reality, which means that a successful application of the method depends on the ability to create such linguistic communities.

In the previous section it was shown that domainspecific modelling languages cannot fully satisfy the enunciated requirements. A common and uniform way of using the freedom of the modelling language should improve (or make possible at all) the automation of the model usage. To make this possible, it would be useful to have a way to ‘guide’ the modeller through the modelling process to impose restrictions without destroying the freedom of modelling. This thought will result in the concept of guidelines discussed below.

## Model-based methodology

A more structured way of modelling was found to be essential in order to resolve the – inevitable – domain conflict. The modelling necessitates the establishment of a traceable connection to the (real world) domain (see Assumptions A1, A2, A4). We discussed the use of domain-specific language constructs (see Requirements R1 and R3) and the restriction of the freedom of modelling – taking into account the domain-specific model purpose (see Requirements R2, R4, R5, and R7).

For two reasons these demands cannot be met using traditional modelling methods: First of all, a modelling method usually deals only with the creation of models and does not refer to the model utilisation with respect to a certain domain. Conceptual modelling languages in substance are domain-neutral. Second, a modelling method consists only of an integrated language and a process-based meta-model (see Brinkkemper, 1996, p. 278; Brinkkemper et al, 1998, p. 390; Tolvanen, 1998, p. 33). The problem-solving technique is not part of the method. If transformational work is already needed during the modelling process, another aspect has to be considered. Since modelling is always done within a certain domain it applies to, a certain usage of the model is always in mind. To make it possible to model based on a dedicated model usage, it seems to be a good idea to adopt some guidelines when creating the models.

Guidelines result in a restricted modelling and include the intentional aspect of the modelling process. The intentional aspect so far has implications on the development of the method, since it does not apply to traditional methods of meta-modelling, which means data and process modelling. In addition, guidelines have an effect on the language and procedure model of a modelling method even during the model usage phase.

Guidelines are the solution to the initial requirements, since they produce the following effects:

\- Restricted modelling: Guidelines enforce a certain use of the modelling language or restrict how to use a certain modelling method depending on the problem domain (see R4 and A3).

\- Reference to the problem domain: Guidelines are domain-specific and result in a domain-specific modelling (see R1, R3, and A1, A5).

\- Problem-solving technique: The guidelines are responsible for establishing a relationship between the (real world) object and the model element (R2, R7, and A4, A5) with the goal of solving the problem in question. As a new ‘ingredient’ to the modelling process they ensure an integration of the problemsolving technique into the modelling process (R5, R6).

To allow a problem-solving technique to be used automatically, a domain-invariant understanding of the modelled data is required. To achieve this common understanding the modelling process itself has to be altered. The use of guidelines helps manage the process of describing certain data in both domains. A common understanding is then enforced by following the guidelines during modelling. Models created under guidelines possess structured, formally analysable constructs instead of or in addition to semi-formal descriptions.

## Guidelines and classic language-based metaisation

When considering the relationship between model elements, the interpretation of these relationships depends on if they are considered within a single layer of the entire meta-model hierarchy or between two (or more) levels of that hierarchy. In the following section these differences are discussed and a new modelling layer is introduced.

## Classic language-based metaisation

The commonly used meta-concept defined by the Object Management Group (OMG) describes the relationship between a language – specified in a meta-model – and its explicated models as instantiation (see OMG, 2002). From a linguistic point of view, the modelling level M<sup>i</sup> provides a type system for the modelling level M<sup>i1</sup> (see Atkinson & Ku¨hne, 2000a, p. 2). The inter-level relationship is that an individual element on level M<sup>i1</sup> is meant as a realisation of an element of M<sup>i</sup>. By a repeated application of this kind of realisation one gets the meta-model hierarchy in Figure 3.

![](/api/attachments/GXG965FJ/fulltext/images/cd1ac88c1adb77bd70226264fde7e243549ce2f986a3debfcc56e81cd6d0304c.jpg)  
Figure 3 Classic language- and process-based metaisation.

A related interpretation of this inter-level relationship is based on object-orientation. The instantiation is interpreted as a concretisation of a class (see Atkinson & Ku¨hne, 2000b, p. 310; Atkinson & Ku¨hne, 2001, p. 20). Both the linguistic perspective as well as the objectoriented approach describe an inter-level relationship that is characterised as shallow instantiation (see Atkinson & Ku¨hne, 2001, p. 20). There is only one type of inter-level relationship, namely the relation between a type and its instance. This relationship always exists only between two adjacent meta-levels.

Each instance on $\dot { \mathbf { M } } ^ { 0 }$ must be assigned to exactly one type element at the meta-level ${ \bf { M } } ^ { 1 }$ and is interpreted as an expression of this type. In the understanding of a shallow instantiation, any influence of one type is restricted to its immediate instances (see Atkinson & Ku¨hne, 2001, p. 20). Thus, from the object-orientation viewpoint, after an instantiation of a class to an object, an attribute to an attribute value, and an association to an edge, no further instantiation is possible (see Atkinson & Ku¨hne, 2001, p. 20). Hence, a type has no effect on model elements that arise from further instantiation-steps (see Atkinson & Ku¨hne, 2001, p. 20).

## Guidelines and domain-specific languages

What characterises a classic DSML is the fixed inclusion of domain-specific statements into the meta-model layer ${ \bf { M } } ^ { 1 }$ . To specify the elements of a DSML typically a domain-ontology is used. Every element represents a set of elements within this ontology. It is assumed that the ontology guarantees that no element holds a semantic that is already covered by another element.

Changes of the DSML – needed to adapt the DSML to new situations like for example new regulations in the public sector domain – cause extensive effort to be implemented. The ontology as well as the meta-model have to be adapted and all created models have to be checked for inconsistency or loss of information. Strict DSMLs furthermore may not allow to assign statements in natural language to a modelling element, but instead force the modeller to choose from a given set of domainspecific statements. The only way to add further information is to add certain pre-defined attributes to a modelling element. As a compromise, often free text is allowed in certain parameters.

Different use cases therefore call for different domainspecific languages with a different capability of expression. This is especially true when these use cases are from different domains. In each use case the question has to be answered, which kind of information (and how much) should be fixed in the meta-model and which part should be left to the modeller to shape and formulate. This results in some kind of traffic between the meta-model layer ${ \bf { M } } ^ { 1 }$ and the model layer ${ \bf M } ^ { 0 }$ when moving between different use cases. However, due to the dynamic nature of language and language use this is even true within a fixed use case. Sometimes more restrictions are necessary to be able to operationalise the model data, which yields very strict DSMLs like PICTURE (see Becker et al, 2007b); sometimes more freedom is necessary to enhance the capability of expression. The latter can be observed even in nondomain-specific languages, like in UML extensions.

This traffic between the meta-model ${ \bf { M } } ^ { 1 }$ and the modelling layer r M ${ \bf M } ^ { 0 }$ can be a serious problem, since modifications of the meta-model may invalidate previously valid models (see Hovsepyan et $^ { a l , }$ 2009, p. 121;

Buckl et al, 2011, p. 285; Levendovszky et al, 2011, p. 259). This often results in quite rigid DSMLs and therefore a strong limitation to certain domains (see Pedro et $^ { a l , }$ 2009, p. 889; Mohagheghi & Haugen, 2010, p. 218; Levendovszky et al, 2011, p. 259). Guidelines avoid this problem by not restricting just the lexicon (the available vocabulary), but by restricting how the available terms should be used. This addresses especially relationships between different terms, parameters, and their values. This allows a greater freedom in the choice of language but instead restricts how the terms are used. It furthermore allows an easy adaptability of the concepts without altering the meta-model $\mathbf { \dot { M } } ^ { 1 }$ . Especially different specifications of guidelines in different domains are possible without losing track to the original concepts on the meta-model ${ \bf { M } } ^ { 1 }$

The next section will describe that this is achieved by introducing an intermediate modelling layer ${ { \bf { M } } ^ { 0 \star } }$ . This layer will allow the introduction of guidelines as mediators between language definition (on $\mathbf { M } ^ { 1 } )$ and language use (on $\mathbf { M } ^ { 0 } )$ . This especially allows different adaptations of the same concepts (on $\mathbf { M } ^ { 1 } )$ in different domains, and therefore different language use in different domains, without weakening a clear definition of concepts on the meta-model.

## Generic interpretation of the inter-level relationship

So $\operatorname { f a r } ,$ the discussion about inter-level relationship in a meta-model hierarchy is purely driven by the linguistic interpretation. In the linguistic interpretation a language-based meta-model is defined as a model of a language ${ \bf M } ^ { 1 } { \bf M } ,$ , which produces the model $\mathrm { { \bf M } } ^ { 0 } \mathrm { { \bf M } } .$ . As long as the studies remain on exactly two levels of modelling – language creation and language usage – this simple linguistic point of view offers a widely accepted understanding of the inter-level relationship. Driven by the idea of a restriction of the freedom of modelling, however, the boundaries between language creation and language usage must be further explained.

As mentioned, when considering different use cases, a smooth transition can be detected instead of a precise distinction between meta- and object-model. A strong separation between these layers is only possible when fixing a certain use case and disallowing adaption of the language used for this use case. The meta-model – in terms of the conceptual data model of the method – defines describable information. Passing from the metamodel to the object model, language-definition becomes less important and merges into language usage. A strict separation of language definition and usage is very hard in practice. This in fact weakens the border between the meta-model and the object-model.

Admittedly, the linguistic meta-model concept can be defined clearly if one uses completely domain-unspecific objects and relationships. But as soon as a certain domain is considered (or having a particular problem in mind to be solved model-based), this is no longer possible. For the requirement for a systematic introduction of guidelines, that fuzziness is a problem. In the following, therefore, a sharp demarcation of the layers is carried out by the introduction of an intermediate level. As explained in the previous section, guidelines are domain-specific.

In order to maintain a separation between the levels ${ \bf M } ^ { 0 }$ and $\mathbf { M } ^ { 1 } ,$ , it is necessary to introduce an intermediate level that forms the link between the domain-unspecific concepts at the level of ${ \bf { M } } ^ { 1 }$ and instances at ${ \bf \cal M } ^ { 0 ^ { \scriptstyle * } }$ level. Concepts are created at ${ \bf { M } } ^ { 1 }$ level that will be used for the modelling at level ${ \bf M } ^ { 0 } .$ . The way of using an ${ \bf { M } } ^ { 1 }$ level concept in a specific domain is specified by a set of guidelines. Their introduction into the meta-model hierarchy formally now implies the creation of a new middle layer. On this level it is specified how to model. There the guidelines have a systematic impact on the language usage.

The new modelling layer will be denoted by ${ { \bf { M } } ^ { 0 \star } }$ . The $\mathrm { { ^ { \prime } 0 \mathrm { { ^ { \prime } } } } }$ within this notation suggests that this layer is in some sense nearer to the ordinary modelling layer ${ \bf M } ^ { 0 } .$ . (In early formulations this layer was sometimes denoted by $\mathbf { M } ^ { 1 / 2 }$ or $\mathbf { M } ^ { 0 . 5 } .$ ) The new layer comes with new roles and responsibilities during the modelling process, and the ‘nearer’ here means that the guidelines on ${ { \bf { M } } ^ { 0 \star } }$ influence the procedure of modelling on $\mathbf { M } ^ { 0 } ,$ while the language creation on ${ \bf { M } } ^ { 1 }$ becomes independent. Adaptation processes that often were necessary on the language level are now pulled away from the language creation layer ${ \bf { M } } ^ { 1 }$ and pushed nearer to the ordinary modelling process on ${ \bf M } ^ { 0 } .$ The new layer ${ { \bf { M } } ^ { 0 \star } }$ therefore can be thought of as a mediator between different roles within the whole modelling procedure.

The main idea here is to weaken the strict separation of language creation and usage without destroying it. It is a pragmatic approach to create a bridge between these two responsibilities in a coordinated way. The intermediate layer carries most of the adaptation procedures and makes them visible to both sides as guidelines. The introduction of guidelines within the DKA therefore addresses the modelling procedure, not only the modelling result. The modelling result may even be quite similar compared to other modelling approaches; however, the modeller is guided through the modelling procedure, and common guidelines enhance the understandability of the modelling results.

Furthermore, these guidelines can be domain-specific and allow the use of a common language in a domainspecific way. Therefore the guidelines also serve as a bridge between different domains. A domain-unspecific concept at ${ \bf { M } } ^ { 1 }$ level can be used in different ways. The instances at the new middle layer represent these different ways. Modelling on ${ \bf M } ^ { 0 }$ is then done by complying to the specified options. By this a concept of constrained modelling is implemented.

Figure 4 illustrates the difference between the linguisticdriven understanding of the inter-level relationship and the more precise demarcation into three levels. For example, at ${ \bf { M } } ^ { 1 }$ level the concept of a bill of material (BOM) is introduced, while a certain BOM is modelled at level ${ \bf M } ^ { 0 } .$ . In between, a guideline determines the way to model a certain BOM – dependent on the domain and the model purpose. Similarly, the domain-unspecific ${ \bf { M } } ^ { 1 }$ level concept of a person can be introduced. A guideline then specifies, for example, how a person who is a student in a specific domain (e.g. a university) should (or must) be modelled. As a result, the domain-unspecific concept person is used differently at ${ \bf M } ^ { 0 }$ level if it is a student or, for example, an employee. Only these possibilities are offered for modelling. The result is a new approach to constrained modelling. Nevertheless, there are still interlevel relations, but now not only in a simple two-layered understanding, but also with the awareness that guidelines lie in-between. In that way the hard distinction between language creation and language usage is softened. We will explain in the next sections how this is done in detail.

![](/api/attachments/GXG965FJ/fulltext/images/fa9d71308e2a05df7200ddb8a3a478579c87947df402e3f8bf62a7670697f742.jpg)  
Figure 4 Distinction between classic and generic inter-level interpretation.

## Demonstration

This section demonstrates the artefact of this research, namely the DKA, by presenting implementation details. It will be discussed how guidelines are realised and how they bear fruit by using them in algorithms to solve the original research problem. This section also highlights the adaptability of the approach, and illustrates the algorithm for one use case, namely the configuration of service-oriented architectures.

## Implementation of guidelines

As mentioned above, the use of guidelines will allow the envisaged goal of comparing and mapping models in different domains. The DKA is a complete new approach that utilises the idea of modelling with guidelines by implementing the following hierarchy of concepts.

The DKA is the result of early ideas and research of the authors about model-based methods for configuring service-oriented architectures as well as identity management systems (see Juhrisch et al, 2007; Juhrisch & Weller, 2008; Dietz et $^ { a l , }$ 2009). With these two scenarios in mind, generalisations and commonalities were outlined, which led to the idea of focusing the research to developing an approach to implement guidelines as described in the earlier sections. In the following, the main ingredients of the DKA are described. Figure 13 shows an example of these concepts.

Description. This is a description of some facts within a framework of guidelines. A description may embed other descriptions.

A description is used by the modeller to express his ideas about some facts using a natural language within requirement or service models. The modelling using descriptions will lead to an increasingly precise expression of a description of real-world phenomena, objects, or object states and therefore can solve the domain conflict. The modeller still can express what he/she wants. However, he/she has to follow certain guidelines that will be enforced by the DKA. The result will be that the modeller is guided to model in the right way with respect to the goal of solving a given problem. See also Figure 11 for an example of the use of descriptions.

As described earlier, an ‘unguided’ use of language constructs leads to several problems. Guidelines therefore have to serve as a controlling instance between language usage and language creation. The creation of descriptions is an act of using language. Each language construct, therefore each description, will be of a certain type (see the definition of description kit types below). The creation of these types will be language creation. To implement the concept of guidelines, something between language usage and language creation is needed. The DKA implements the concept of a guideline by so-called description kits. Description kits supply some kind of framework to implement guidelines for the language usage in the sense of restricted modelling.

Description Kit. A description kit defines guidelines for the description of a concept. It is a set of properties, possible values, and constraints for a given concept ordered by some aspects. This order includes a hierarchy and allows the embedding of other description kits. This makes it possible to use other concepts for describing a given concept.

Therefore, description kits define the way certain descriptions have to be made (where ‘certain’ refers to all descriptions in the above sense that comply to the description kit in mind). This includes constraints for parameters and values, but – even more important – also the embedding structure. Descriptions have to follow the ‘rules’ imprinted by the description kit they belong to.

Guidelines in the sense of Figure 4 are thus represented by description kits and reflect a domain-specific understanding of a certain concept. A description kit for the concept Person on ${ \bf { M } } ^ { 1 }$ in that figure could, for example, be a kit ‘Student’ or a kit ‘Employee’ and would define guidelines on how to describe a person that in fact is a student or how to describe a person that in fact is an employee. This will be further explained in the following (see also Figure 13).

As stated, the main idea for introducing description kits (DescKits or DKs) is to provide a framework for the creation of descriptions (Descs or Ds) on the normal modelling layer (layer $\mathbf { M } ^ { 0 } )$ . Therefore, DescKits also represent partially natural language concepts – in the sense of domain-specific language constructs. The restriction to the concepts that are introduced on the layer of DescKits results in the partial solution of the mentioned language conflicts (see Dietz et al, 2009; Juhrisch & Dietz, 2010a). They document the consensus of the linguistic community with regard to the given vocabulary for the language analysis of relevant concepts and – even more important – how to use this vocabulary. This consensus has to be developed in consulting services (by method developers) together with the customer.

Description kits are created in a new layer ${ { \bf { M } } ^ { 0 \star } }$ that sits between the normal modelling layer (for language usage) ${ \bf { M } } ^ { 0 }$ and the meta-modelling layer ${ \bf { M } } ^ { 1 }$ for language creation. They serve as guidelines for the use of descriptions in the previously discussed sense. (Note that the description kits do not represent the language in an ordinary sense.)

Fundamental Hypothesis. The compliance with a given description kit will result in the correct procedure during the modelling with respect to the given problem (see Juhrisch & Weller, 2008, p. 1469).

Description Kit Type. A description kit type determines a concept that should undergo guidelines.

Normally description kit types (DescKitTypes or DKT) define obligated elements or actions within the modelling process. If the definition of these elements or actions is done with respect to the problem domain, description kits can be seen as a concretisation of the procedure model with respect to the given problem. The architecture of the DKA is generic. In the beginning of its development it was motivated by the goal of configuring service-oriented architectures; this seems to be a specific goal, but still service-oriented architectures can exist (or be planned) in very different domains. This motivated a generic approach that bore fruit later.

Taking these concepts of Descriptions, Description Kits, and Description Kit Types and filling these concepts with Parameters, Constraints, and Relations, one arrives at the data model shown in Figure 5. All these concepts are the fundament to build and use a Description Kit Language (DKL). Note that the data model shows relationships between the different concepts from a pure persistence viewpoint. The DKA comes along with several relationships that represent different kinds of instantiation. A concrete description kit for example is an instance of the concept ‘Description Kit’, but also some kind of instance of the description kit type it belongs to. This is shown in Figure 6. For a more detailed discussion about these different kinds of instantiation see Juhrisch (2010, pp. 142 and 150) and Juhrisch & Dietz (2010a, p. 256).

![](/api/attachments/GXG965FJ/fulltext/images/4cd0132df2bb413e9f23b94195577e3b9ed593f37a516706b720f179363bfa93.jpg)  
Figure 5 Data model of the Description Kit Language (context layer). Note that the different relations are purely understood as relations in a persistence model of the underlying modelling data and do not reflect all the instantiation relationships (see also the main text).

![](/api/attachments/GXG965FJ/fulltext/images/812dc1d033e7428d458d94b00be463313b2002a1e82797e61c12c5038ce7d634.jpg)  
Figure 6 The different instantiations within the DKA from different viewpoints. These instantiation layers form a three dimensional cube, which is shown from different viewpoints so that the different instantiation relationships are shown along the z-axis.

As described above, a guideline is represented by description kits. Here many parts of the DKA come together: The description kit type of the corresponding description kit, the embedding hierarchy, parameter types, value types, and constraints for those. On the description level the descriptions, their embedded descriptions, their parameters, values, and constraints have to follow the ‘rules’ given by the guidelines. This rule enforcement is not part of the data diagram. (On the instance level this could be visualised by commutative squares in the mathematical sense.)

One essential part of the guidelines are the constraints. Note that constraints also are used in descriptions to describe ‘possibilities’ like states of objects or conditions to other concepts. Again, the constraints of a description kit provide a framework for constraints at the description level. Both the structure of the DKA concepts DKT, DK, and D, including their embedding structure, and the constraints may enforce a restriction of language usage without destroying the freedom of the modeller. Free text parameters are still possible when it makes sense, while a fixed set of possible values may be given for other parameters. However, the full power of the DKA results from the embedding structure.

The creation of a DKL involves, as the first step, the creation of DescKitTypes with respect to the problem. These are then used to introduce DescKits that reflect the language consensus and represent the guidelines for the usage of descriptions. To realise this, a new model layer $\mathbf { \check { M } } ^ { 0 \star }$ is introduced that holds the DescKits and lies between the model layer M<sup>1</sup>, which holds the DescKitTypes that form the DKL, and the ordinary model layer $\mathbf { M } ^ { \tilde { 0 } } ,$ , which holds the descriptions – either in addition to another (ordinary) modelling language or in the form of an independent DKL usage.

![](/api/attachments/GXG965FJ/fulltext/images/2d165f8b51407834dd330d56b2f54229c475aefedfbefc70e1349d2abe8742d3.jpg)  
Figure 7 Guidelines in model-based methodology.

The framework for describing guidelines can be seen as a self-contained part within the model-driven method. It can be used in combination with other modelling methods or languages, or on its own. The goal, to solve a given problem, can in most cases be translated to a mapping problem or transformation problem of models in different domains. For these problems the DKA offers algorithms that can solve these problems or support a semi-automatic transformation. All these parts – a methodology for language creation, language usage, and algorithms for solving the given problems – are combined together to form the DKA.

Figure 7 summarises how this new aspect of guidelines is able to build a bridge between different domains by introducing structured and formal cores within the models that ensure the comparability of model entities. This creates the base for algorithms that are able to perform a comparison by mapping model entities in one domain to another domain. This will be described in the next section. This mapping moreover is then the basis for problem solving techniques that interpret the mapping result in a semi-automatic way to solve a certain problem in mind.

## The mapping algorithm

Using the DK approach, an algorithm should be introduced that is able to compare different models that use the same DKL (see Figure 7); for example, it could use a process model as a source model and a design model describing services as a target model. The original purpose of this algorithm was to find service candidates for process functions within a process model, but it is described completely generically so as to be useful also in other scenarios.

Because of the generic approach, the algorithm is controlled by certain characteristic numbers for each DKT. These characteristic numbers reflect the behaviour of descriptions of a certain description kit type within the model. They are exogenous, which means they have to be defined by the analyst during the definition of the DKL. How these numbers influence the algorithm will be described below.

The first step is to compare two single descriptions in two different models from different modelling domains. Note that a single description still may embed other descriptions, which means that this step already operates on sets of descriptions. However, relations play no role in this step. Since Ds (and DKs, DKTs) can be embedded into each other and every D (DK) can have parameters, values, and constraints, the structures to be compared are quite complex and the algorithm has to take into consideration the embedding location of each artefact to compare. To simplify the data model the algorithm operates on, we map all parameters and its values of Ds to so-called virtual Ds, which have the DKT ‘virt\_DescKit’ and are instances of DKs ‘virt\_Param’, ‘virt\_Value’, or ‘virt\_Constr’, respectively. This leads to a model transformation, which results in a model using only Ds (of certain DKs and DKTs) without parameters, values, or constraints.

After this model transformation the resulting data can be described as a tuple

$$
\mathcal {M} = \{\mathcal {M} _ {D}, \mathcal {M} _ {D K}, \mathcal {M} _ {D K T}, \kappa , \tau , \rho \},
$$

where

${ \mathcal { M } } _ { D }$ is the set of descriptions,

$\mathcal { M } _ { D K }$ is the set of description kits,

$\mathcal { M } _ { D K T }$ is the set of description kit types,

$\kappa : \mathcal { M } _ { D }  \mathcal { M } _ { D K }$ is the function that maps each description to the description kit it instantiates,

$\tau : \mathcal { M } _ { D K } \to \mathcal { M } _ { D K T }$ is the function that maps each description kit to the description kit type it belongs $^ { \mathrm { t o , } }$ and

$\rho : \mathcal { M } _ { D }  \mathcal { M } _ { D } \cup \{ \emptyset \}$ is the parent function: $\rho ( d )$ is the description that contains $d ,$ where $\rho ( d ) = \emptyset$ means that d has no parent.

The above data include both the source model and the destination model of the comparison. Therefore we have the set $\boldsymbol { \mathcal { S } } _ { D } \subset \mathcal { M } _ { D }$ of all descriptions of the source model and the set $\mathcal { D } _ { D } \subset \mathcal { M } _ { D }$ of all descriptions of the destination model. Note that the use of a common DKL means that we do not have to distinguish corresponding sets $\boldsymbol { S } _ { D K }$ and $\mathcal { D } _ { D K }$ or $\boldsymbol { S _ { D K T } }$ and $\mathcal { D } _ { D K T }$

In order to control the algorithm, characteristic numbers are introduced. That means that we have maps

$$
\lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {\ell}: \mathcal {M} _ {D K T} \to [ 0, 1 ] \subset \mathbb {R},
$$

so that for each DKT $t \in \mathcal { M } _ { D K T }$ we have $\ell$ numbers $\lambda _ { 1 } ( t ) .$ $\lambda _ { 2 } ( t ) , ~ . . . , ~ \lambda _ { \ell } ( t )$ . Some of these numbers are described below.

To shorten the notation, we often write

$\tau ( d )$ instead of $\tau ( \kappa ( d ) )$ for $d \in \mathcal { M } _ { D } ,$

$\lambda _ { j } ( k )$ instead of $\lambda _ { j } ( \tau ( k ) )$ for $k \in \mathcal { M } _ { D K } \ ( j = 1 , \ . . . , \ell ) ,$

$\lambda _ { j } ( d )$ instead of $\lambda _ { j } ( \tau ( \kappa ( d ) ) )$ for $\begin{array} { r } { \boldsymbol { { l } } \in \mathcal { M } _ { D } \ ( \boldsymbol { { j } } = 1 , \ \ldots , \ \ell ) . } \end{array}$

Now the preparations are done and the main part of the algorithm can begin.

In the next step we iterate through the sets of description kits step by step to compare them individually. This means we loop over all pairs $( d , d ^ { \prime } ) \in \mathcal { S } _ { D } { \times } \mathcal { D } _ { D }$ and determine how well d and $d ^ { \prime }$ correspond:

(i) Compare the DKTs: Check, if $\tau ( d ) = \tau ( d ^ { \prime } ) ;$

(ii) In case of a match in (i): Compare the DKs: Check, if $\kappa ( d ) = \kappa ( d ^ { \prime } )$ ;

(iii) In case of a match in (ii): Compare the Ds: Check, if $d = d ^ { \prime } ;$

(iv) Take the embedding position into consideration: Do the same checks $( \mathrm { i } ) { - } ( \mathrm { i } \mathbf { v } )$ for all parents, which means recursively compare d and $\rho ( d ^ { \prime } ) , \rho ( d )$ and $d ^ { \prime } ,$ as well as $\rho ( d )$ and $\rho ( d ^ { \prime } )$ (until they do not have a parent anymore).

The results of this check should be evaluated and weighted by the characteristic numbers for the DKL to get as a result a number $\sigma ( d , d ^ { \prime } ) \in [ 0 , 1 ]$ , which reflects how well the two descriptions correspond. This step is controlled by the characteristic numbers as follows.

With the notation

$$
\delta_ {x, y} = \left\{ \begin{array}{l l} 1 & \text { if } x = y \\ 0 & \text { if } x \neq y \end{array} \right.
$$

we can write

$$
\sigma^ {\mathrm{i} - \mathrm{iii}} (d, d ^ {\prime}) = \delta_ {\tau (d), \tau (d ^ {\prime})} \left(\lambda_ {1} (d) + \delta_ {\kappa (d), \kappa (d ^ {\prime})} \left(\lambda_ {2} (d) + \delta_ {d, d ^ {\prime}} \lambda_ {3} (d)\right)\right)
$$

for the intermediary result of steps (i)– (iii), and then

$$
\begin{array}{l}\sigma (d,d^{\prime}) = \frac{1}{\lambda_{1}(d) + \lambda_{2}(d) + \lambda_{3}(d)}\\ \times \max_{\substack{i\in \mathbb{N}_{\geq 0}\\ i^{\prime}\in \mathbb{N}_{>0}}}\left((\lambda_{4}(d))^{i + i^{\prime}}\sigma^{\mathrm{i - iii}}(\rho^{i}(d),\rho^{i^{\prime}}(d^{\prime}))\right) \end{array}
$$

with

$$
\rho^ {i} (d) = \underbrace {\rho (\rho (\ldots \rho)} _ {i \text { times }} (d) \ldots)) \quad \text { and } \quad \rho^ {0} (d) = d.
$$

The numbers $\lambda _ { 1 } , ~ \lambda _ { 2 } ,$ and $\lambda _ { 3 }$ here determine the ‘importance’ of a certain DKT, and also put weights to steps (i)–(iii) above. The numbers $\lambda _ { 4 }$ control to which amount a match is acknowledged that is not on the same level of the embedding hierarchy.

After calculating these numbers the results are to be consolidated to

$$
\bar {\sigma} ^ {\mathcal {S}} (d) \in [ 0, 1 ] \quad (\text { for   all } d \in \mathcal {S} _ {D})
$$

and

$$
\bar {\sigma} ^ {\mathcal {D}} (d ^ {\prime}) \in [ 0, 1 ] \quad (\text { for   all } d ^ {\prime} \in \mathcal {D} _ {D})
$$

which reflect how well a description d or d<sup>0</sup> is matched on the other side altogether. This step is also controlled by the characteristic numbers that control in which situations it is good or bad, for example, to have multiple matches (or no matches). That means for all $d \in S _ { D }$ a number $\bar { \sigma } ^ { S } ( d )$ is evaluated as a function of all $\sigma ( d , \ d ^ { \prime } )$ (where we iterate over all $d ^ { \prime } \in \mathcal { D } _ { D } \mathrm { ~ ) ~ }$ as follows:

(i) Count the number of all $d ^ { \prime } \in \mathcal { D } _ { D }$ with a large $\sigma ( d , d ^ { \prime } )$ (i.e. a matched pair).

(ii) Rate this (using the characteristic numbers) depending on only one match (good), more than one match (probably bad) or no match (very bad).

This evaluation makes use of a certain characteristic function (again controlled by some of the characteristic numbers), which reflects the ‘good’, ‘probably bad’ (which means the characteristic numbers control here if for a certain DKT it is acceptable or not acceptable to have multiple matches) and ‘very bad’ of step (ii). We refrain from going into detail here.

The numbers $\bar { \sigma } ^ { \mathcal { D } } ( d ^ { \prime } )$ are calculated analogously for each $d ^ { \prime } \in \mathcal { D } _ { D }$

In the last step these numbers will be consolidated again to get a number

$$
\sigma \in [ 0, 1 ]
$$

which describes the degree of how well the complete model data $\boldsymbol { S } _ { D }$ and $\mathcal { D } _ { D }$ correspond. This final result $\sigma \in [ 0 , 1 ]$ is calculated as a weighted mean of all $\bar { \sigma } ^ { S } ( d )$ and $\bar { \sigma } ^ { \mathcal { D } } ( d ^ { \prime } )$ (where the weights again are represented by characteristic numbers).

Since parameters, values, and constraints have been mapped to virtual descriptions (with their own characteristic numbers), they are of course part of all these calculations.

The second step involves the comparison of complete models or parts of complete models (‘sub-models’). While the first step did not take relations into account (because it is meant to compare single descriptions), the second step highly relies on relations. We assume here the case that a pure DKL is used for modelling, otherwise some more steps have to be taken into consideration.

Some preparations are needed for this step. Each RelationType represents a certain way for ‘information flow’ along a Relation of this type. The idea is to ‘fold’ the model along each relation, which means to replace the relation and the descriptions it connects by a new artificial description (similar to the virtual descriptions above) that still represents the essence of the information given by the whole sub-model. The result is a ‘convolution product’ of all involved descriptions, which is a new (more complex) description. In the mathematical sense that means to understand each Relation as a convolution operator, and the way it operates may depend on the RelationType.

The main example comes from the use case of configuring service-oriented architectures, where objects flow along service compositions. Descriptions are introduced for the interfaces of services. For the relation type that represents a service composition, the following convolution operation is introduced:

$$
\left(\left\{\text { Interface } \{\text { Input } \{\text { Object   } I _ {1} \} \} \{\text { Output } \{\text { Object   } O _ {1} \} \} \right\}\right)
$$

$$
\xrightarrow {\text { Flow }} \left\{\text { Interface } \{\text { Input } \{\text { Object   } I _ {2} \} \} \{\text { Output } \{\text { Object   } O _ {2} \} \} \right\}
$$

$$
\left\{\text { Interface } \{\text { Input } \{I _ {1} \cup (I _ {2} - O _ {1}) \} \} \{\text { Output } \{(O _ {1} - I _ {2}) \cup O _ {2} \} \} \right\}
$$

Here the curly brackets denote the embedding structure. The operations , and  are predefined operations that are based on the previous 1:1 mapping algorithm. In the case of X,Y the mapping algorithm is invoked for X and Y. If the algorithm results in a match, then X and Y are combined, which means all embedded descriptions, parameter, values, and constraints are put together. (This is done recursively, again using the ,-operator for the embedded parts.) In the case of  the opposite happens: Again the mapping algorithm is invoked; but in the case of a match the difference of X and Y is created: All completely matching parts of the descriptions are removed. For no match the result of XY is simply X.

It has to be noted that the 1:1 mapping algorithm in fact yields a number instead of simply a ‘yes’ (matching) or $' _ { \mathrm { n o ^ { \prime } } }$ (not matching). The current implementation therefore tests the mapping result against a threshold that can again be controlled by one of the ls. A future implementation may postpone this decision at this point and keep track of both possibilities (what happens if I say ‘yes’ here, what happens if I say ‘no’ here) until the final convolution result has to be determined.

As a simple example see Figure 8. This figure shows an example for both the ,-operator (call it ‘union’) and the -operator (call it ‘annihilation’): The left and the right side both represent in fact the same process of informing a person with help of a document, but modelled with different granularity. The left side explicitly describes the creation of the document and the sending of the document as two process steps. The document is the output of the first step and is used in the second step. The above folding operation recognises therefore this document as a temporary object and the annihilation operator ‘consumes’ the document, so that is is not contained in the convolution result. On the other hand, the union operation combines the two appearances of the person, so that the convolution result contains a person description with all necessary information for this task.

Another example for a convolution operation may be found in Dietz and Juhrisch (2010).

For each RelationType there may exist a whole set of convolution rules that have to be calculated when the folding algorithm is working. The algorithm then folds the whole model step-by-step (taking one relation after another) together to one single description. For these (now very big) descriptions the first original mapping algorithm then can be used, which results in a comparison of the complete models or sub-models in question.

However, this involves non-trivial graph-theoretical questions, which may be summarised as: In which order should the convolution be calculated, especially in the case of loops or branchings? The idea to answer this question is to consider all possible non-branched paths through a given graph, calculate the convolution as above, and then put all results together (using again the ,-operation).

![](/api/attachments/GXG965FJ/fulltext/images/48857525ffd727fe2f8b93a03d010726f3605213e621c1a72456b34a8d4404b5.jpg)  
Figure 9 Example for the convolution of (sub-)process chains using the DKA.

See Figure 9 for a more elaborated example of how this algorithm works.

In the case of using the DKA in combination with an ordinary modelling language, the relations given by the ordinary models have to be translated into Relations in the sense of the DKA. This involves a new difficulty, since also indirect relations have to be taken into consideration (since not all ordinary model elements may be annotated by descriptions – see Figure 10). To address this problem, empty (virtual) descriptions can be attached to intermediary model elements to bypass unannotated elements. The convolution operation would then fold a description into the next empty ‘bypass’-description. As a result, this description would move one step down and would be nearer to following model elements that may be annotated. This is repeated until it finally reaches an annotated description. In the next step the convolution would operate on these two, now neighbouring, descriptions. See Figure 10 for an illustration. This makes it possible to use the convolution (and therefore the whole mapping algorithm) also in this scenario.

![](/api/attachments/GXG965FJ/fulltext/images/b2ca0797a95d46774cbe73aceb54c3342c86009a1ebd0068a52c8fd755c4cee8.jpg)  
Figure 10 An example for indirect relationships and empty (virtual) descriptions – a simplified version of Figure 8 as an Event driven Process Chain (EPC).

To summarise, the complete mapping algorithm consists of two main parts: First the convolution and then the comparison of the convolution results. But since the convolution operation highly relies on the 1:1 mapping algorithm to calculate the union and annihilation operations, we have in fact the following sequence of events:

1. The 1:1 mapping algorithm compares all ‘atomic’ parts of the models in question.

2. The convolution is performed by using the previous comparison results.

3. The 1:1 mapping algorithm is invoked again for the convolution results.

The last step then yields a number between 0 and 1 as the degree of matching, which reflects all the intermediary results from the above steps in a weighted way. The algorithm is adaptable by controlling these weights with the help of exogenous variables.

## Evaluation

To check the basic applicability of the DKA, we tested the functionality of the algorithmic problem solution methods by an exemplary application (proof-of-concept). It is shown how the DKA is used in practice and how the initial requirements for the method are met (references to the requirements analysis are made in parentheses). The model-based methodology is used in an example of a university matriculation process done by a German university. The language chosen for creating the process model is UML 2.1.2, since it has found broad acceptance in practice (see OMG Object Management Group, 2007).

Prior to the creation of models, description kit types and description kits were created. Some of the description kits and their description kit type are shown in Figure 13. They reflect the consensus made in certain domains of the administration of the university, here especially the student registry office and human resources (R2).

Figure 11 shows a part of the registration process of a new student of mathematics. The student is registered for the course of study of mathematics and at the same time an account is created and assigned to the student. Figure 12 on the other hand shows a part of the process of employing a person. This process is modelled in a much coarser granularity and only consists of two steps: First employ the person, then grant that person access to resources.

Both (parts of) processes are ‘philosophically’ the same but look quite different. By looking purely at the UML diagrams, this similarity would be hard to notice. But all the activities in both figures are now annotated by descriptions. The form of these descriptions is given on the modelling layer M<sup>0</sup>\*, which means that the descriptions comply with their corresponding description kits.

The description kits now force the modeller to describe the activities in the UML diagrams by picking the most appropriate kits (R1, R4). This can be seen as ‘guiding’ the modeller to use the correct concept (reflected by the description kit type the description kit has) for describing the activities (R7). Because of the embedding structure, this selection of a concept also includes the choice of related concepts (represented by embedded description kits) (R3). Here for example the kit ‘Account’ is picked for the activity ‘granting access’. The modeller has to think about what he/she really wants to say. This includes thinking about what is really needed as information to perform the task. Constraints within the description kit can furthermore give more guidance for the modeller: A matriculation number for example belongs to a student, but not to an employee (R7). The new modelling layer ${ { \bf { M } } ^ { 0 \star } }$ is the perfect place to contain this information; otherwise this information would have to be put on M<sup>1</sup>, where it would only read ‘a person can have a matriculation number’. Other constraints may be the possible values for a status or a constraint that defines that only a matriculated student may have a matriculation number.

![](/api/attachments/GXG965FJ/fulltext/images/4ffddd45dec23c449f7a591fd70f867f9792970d62d6ac6656b9fd453d1006a2.jpg)  
Figure 11 UML activity diagram with descriptions. This diagram describes a simplified registration process for a student of mathematics.

![](/api/attachments/GXG965FJ/fulltext/images/3bd54b6c8fc6fb16cbac1653546bf640083ff0eaa12be4dc8b96b5e8978c6e39.jpg)  
Figure 12 Another UML activity diagram with descriptions. This diagram describes a similar process as the one in Figure 11: a (very) simplified employment process.

Since the meta-model of the DKL can be connected to the meta-model of another modelling language (like UML in the examples), constraints can also be made on how to annotate model-elements by descriptions (R7). It can be specified which modelling elements can or must be annotated, and the description kit type to make this annotation can be prescribed. This indirectly influences how a modeller is creating the original model, like for example the granularity. In the example of Figures 11 and 12 the constraint ‘each activity must be annotated by a description of type Service’ may have been used.

This shows how type conflicts and structure conflicts are addressed directly, since the constraints within the description kits guide the modeller towards using the right concepts for expressing his/her ideas; furthermore language conflicts are addressed by guiding the modeller to express his ideas in the right way (R1, R7). It has to be pointed out, however, that all these constraints should help the modeller to express their ideas in a useful way, not to restrict them in what he/she is able to express.

![](/api/attachments/GXG965FJ/fulltext/images/6d09e85951fe96a178c9899f43db1de85eddac24f17d2f46034b29e619d0e286.jpg)  
Figure 13 Example for a mapping between descriptions using the DKA.

The annotation by descriptions now yields a good comparability of both parts of processes (R5). First, both students and employees use the same description kit type ‘Person’. Second, both processes now use the description kit type ‘Account’ where the UML diagram was using the terms ‘account’ and ‘access’, respectively. The different granularity of both processes is now addressed by the convolution operation. Part of the result of the convolution operation (only the ‘Person’ part) can be seen in Figure 13. The convolution part of the algorithm therefore ensures the comparability of these two models with different detail level (R3). The mapping algorithm then can compare these two sub-processes step-by-step through all model-layers. This is shown again in Figure 13.

The algorithm starts with a comparison of the outer DKTs and finds a correspondence. However, the top-level analysis stops since MathStudent and ActiveEmployee are using different DKs. Subsequently the analysis takes a step forward into the inside of description MathStudent and ActiveEmployee. The algorithm compares the embedded DKTs. CourseInfo does not match, since the DKT Affiliation is not used in ActiveEmployee. In contrast, MatriculationStatus matches with ContractDetails on the DKT level (as both use the DKT Status). Now the DKs are compared, but do not match. The same holds for the comparison of the parameters of the outer DKT: there is no correspondence. After another inwards step, no more embedded DKTs can be found. Indeed, a correspondence appears when comparing the parameters of the embedded DKTs: the parameter Status matches, including its value. The results are weighted according to the DKTs and their embedding and are consolidated to an overall matching quality between 0 and 100%.

Of most importance is the match between the outer layers. Even though only the DKTs are matching on the outside, the inner structure, however, is also slightly match ing. Therefore the overall result is rated as fine to some extent. The gradual inward-looking algorithm into the content is the charm of the approach. This is what allows us to derive much more information than possible by standardising and comparing business objects using DSML.

As already discussed, every part of the algorithms is adaptable (R6). Depending on the context and the problem to solve it may be a good idea to match a students’ registration process with an employment process, or not. In concrete technical implementations of the mapping procedure (for example in CASE tools) the user should therefore be able to interact. The easiest way would be a list of possible matches sorted by the matching quality, so that the user can select the match that serves him best (R6).

In addition to the question of how guidelines apply in practical modelling projects, the question remains on how to create these guidelines (in the form of description kits), when this happens, and who is involved in this process (R2). A detailed discussion about the model of organisational roles of the DKA can be found in Juhrisch & Dietz (2010b). It is important to note, however, that one of the strengths of the DKA is the adaptability of guidelines after the modelling project has already started.

The adaptability of the DKL is in fact another advantage of the introduction of the new modelling layer M<sup>0</sup>\*. In ordinary meta-modelling approaches, modifications on the meta-modelling layer M<sup>1</sup> can destroy the validity of models on M<sup>0</sup> (see Saeki, 2006; Weller & Esswein, 2006). Using the DKA, the adaptation happens on M<sup>0</sup>\*, not on M<sup>1</sup>. A result may be that existing models do not follow the new guidelines anymore, but they are still valid models with respect to $\dot { \mathbf { M } } ^ { 1 }$ . This is another advantage when the DKA is compared to DSML.

## Discussion

Conflicts in modelling arise from using natural languages. The language always reflects some background (cultural, knowledge, expert domain, etc.) of the modeller. This results not only in language conflicts, but also in structure and type conflicts, which reflect different interpretations of how to model. Because most methodologies try to repair these conflicts when it is too late, models from a certain domain are only understood by the domain experts. The comparison of models now becomes very difficult. To solve this problem a new approach is presented that focuses on the whole modelling process and tries to attack the conflicts earlier by narrowing the gap between language creation and language usage.

A very early intervention in the modelling process allows the creation of methodologies for restricted modelling that, because of their adaptability during the modelling process, do not restrict the actual goal of modelling: To express the ideas of the modeller. To the contrary, the modeller now has some tools to express his/her ideas in a way that can be understood by others. Guidelines – as the main ingredient for procedure models – are designed by several hierarchies between different modelling layers. They can now be introduced into the modelling process in a formal way (by introducing a new modelling layer M<sup>0</sup>\*). This allows the solution of several conflicts, especially the domain conflict. The use of these models in a different domain than the domain in which they were created becomes possible. The presented approach utilises this by adding algorithms that facilitate model comparisons between different domains.

The DKA is generic – even if the development of the approach started with a very concrete goal in mind. The main fields of application for this approach were initially the configuration of service-oriented architectures (see Dietz et al, 2009, p. 5) and the configuration of identity management systems (see Juhrisch et al, 2007, p. 9; Juhrisch et al, 2009, p. 3). For both scenarios there are commonalities going much further than first expected. Therefore the usage of this approach in many fields of application is not only possible, but becomes a driving idea for the development of this approach. The DKA allows a simple adaptation of the semantic of its language tools to the changing requirements of a lively and developing domain. The DKL is not only adaptable at the beginning of a project, but also during the modelling process. Also the algorithms are adaptable to the domain and the original problem in question. The fields of application of the DKA are therefore manifold and offer a great potential for contribution to information science.

Most problems can be converted into a comparison problem. Information needs to be prepared and evaluated to be useful for solving a certain problem. This evaluation especially means to compare ‘what is’ (especially ‘what is known’) to ‘what should be’. As mentioned, the driving example for this was the goal of mapping requirements – formulated using natural languages – onto ‘reality’, or – more information science-specific – design models that describe service implementations. The description of requirements is semi-formal and involves, next to (formal) technical facts, natural languages to a large extent. This alone already creates a high dependency of problem solving approaches on knowledge, culture, organisational behaviour, and, last but not least, of course the language used for the description of the problem. This research attacks this problem by offering a model-driven approach for negotiating language barriers and therefore lowering this dependency in problem solving scenarios.

## Future research

Future research is needed in several areas. First, the success of the DKA is crucially dependent on the possibility to convince domain experts, software developers, and modellers to use the presented model-based method in the long run. In the previous section we demonstrated, by testing the developed algorithms, that a comparison and alignment of models in different domains is possible using the DKA. A full proof of the usefulness of the presented approach is still required by using it (as a prototype) in a detailed case study. That case study must show especially that the requirements mentioned in this article can be met better, faster, and/or more cost efficiently by the new method compared to ordinary methods. The possibility of combining the DKA with ordinary modelling methods for system analysis will help to secure a higher acceptance in daily use.

Another emphasis for future research is the technical development for the remaining parts of the prototype. The algorithms are already implemented within the modelling tool cubetto<sup>s</sup> toolset. There is a need for adding concrete support for the additional modelling layer M<sup>0</sup>\* – with respect both to the data model and the graphical user interface. In addition to that, further enhancements should be made to realise the identification of concrete objects (in contrast to only object descriptions that could be met by more than one object) to support automatic model transformation, for example to BPEL (Business Process Execution Language). This will allow for the identification of concrete object flows through different services in a service composition. Furthermore, the algorithms (especially the convolution parts) involve some graph-theoretical problems (that arise from comparing complete models or parts of them) that could be improved. Also the algorithms to compare the embedded structures of descriptions, DescKits and DescKitTypes, are interesting from a mathematical standpoint and are worth a further investigation for improvement.

As mentioned earlier, characteristic numbers control and adiust the algorithms and need to be defined (for each DKT) when creating a DKL. However, they behave similarly to adjusting screws for a machine and need to be readjusted when ‘the machine’ (the algorithm) is running. The use of neural networks to get a good set of characteristic numbers (which involves the training of the algorithms) is conceivable. Furthermore, it would be useful to include non-functional requirements into the algorithms in a more direct way (up to now they influence the algorithms indirectly when using descriptions to describe the non-functional requirements). Their influence on the mapping result needs to be more visible to the model expert. Last but not least there would be the interesting possibility of including ontologies in the mapping algorithms. While ontologies are not needed to achieve good results, they may help to improve the results. Also the support of generalisation and specialisation relations on M<sup>0</sup>\* and M<sup>0</sup> would help to develop constraints in a more detailed way, which again would improve the results of the algorithms.

## Conclusion

While there is a growing recognition that the adoption of models can enhance the success of Business Process Reengineering projects in general, and in the Information Systems development context in particular, there has been limited understanding of the specific needs of modelbased engineering. This research proposes a theoretical model – the DKA – not only based on new concepts, but also on a new idea of how the concepts work together toward a guideline-oriented modelling approach.

The idea of the introduction of guidelines is to be able to clearly fix linguistic concepts, but to still keep them adaptable. This means to distinguish between a definition of what has to be described (definition of the concept on the meta-model layer) and how to describe it (use of these concepts on the model layer). How to use a certain concept depends on the context. Depending on the context of the modeller (his domain) he/she will use certain concepts intuitively in a different way than another modeller from another context. To allow this, the guidelines, in contrast to DSMLs, do not force the modeller to use a concept exactly in the way it was defined on the meta-model layer. He still has the freedom to form a concept due to his ideas – however, not completely arbitrary, but within certain limits that are given by a consensus of a linguistic community (within his/her domain). These limits therefore reflect the understanding and conventions of the community and ensure that the models, created using these conventions, have a clear meaning within their domain. The principle of a living language (use theory) is thus incorporated into conceptual modelling.

In summary, after first describing the topic of this article, research questions were derived and the research methodology was outlined. The theoretical background for conceptual modelling was outlined to be able to generate a better understanding of the research problem. This included especially a discussion of several conflicts arising from using natural languages. From these problems a requirement analysis for a methodology to solve these conflicts has been derived. On the basis of these requirements, guidelines were introduced and discussed as a solution to the problem. This idea was then developed into the specification of the method, which focusses on the mapping between semi-formal models. The method was then assessed in a detailed proof-of-concept.

The mapping between semi-formal models from different domains is now resolvable semi-automatically by using the DKA. Given that most organisational decisionmaking (for example the adoption of a new Enterprise Resource Planning system) involves trade-offs between multiple factors, the use of this approach can create a useful assessment framework, and thereby guide decision-makers.

Kugeler portrays some problems in organisational and application development that offer potential application fields for the DKA (see Kugeler, 2000, p. 98, which again cites Darke & Shanks, 1996, p. 8; Rosemann, 1996, p. 219; Rosemann, 2000, p. 47). Here the DKA offers a methodical procedure, which today is not self-evident. One can foresee an increasing tendency to automate the development and configuration of application systems in the future. The presented approach lays a foundation for the concepts needed for this.

To conclude, incorporating models in IS development, engineering, or organisational management appears to be a growing trend within the research and practitioner communities. Our research initiates a first step towards the eventual development of ‘model-based methods theories’ that contribute to (IT) business alignment as mediators within and between business and engineering.

## Acknowledgements

The authors express their sincere gratitude to Prof. Dr. W. Esswein, Head of Chair for Information Systems, esp. Systems Engineering at the Dresden University of Technology, for his assistance in the preparation of the manuscript. Our thanks also go to the the Surrey International Institute and the Global Institute of Management and Economics of the Dongbei University of Finance and Economics, Dalian, for their support. We are also indebted to the anonymous reviewers and several colleagues for numerous invaluable comments.

## About the authors

Gunnar Dietz was Associate Professor and Director of MIS at the Global Institute of Management and Economics of the Dongbei University of Finance and Economics in China, before joining the ‘Tec-In’ research transfer project of the Dresden University of Technology in Germany. He received his diploma degree in Mathematics from the University of Hamburg, Germany, and his doctorate degree from the University of Mu¨nster, Germany. His research interests include IS development, business alignment, IT security, service-oriented architectures, software development, and mathematics.

Martin Juhrisch is currently Project Manager of the ‘Tec-In’ research transfer project of the Dresden

## References

VAN DER AALST WMP and KUMAR A (2003) Xml-based schema definition for support of interorganizational workflow. Information Systems Research 14(1), 23–46.

ATKINSON C and KU¨ HNE T (2000a) Meta-level independent modelling. In International Workshop on ‘Model Engineering’ (in conjunction with ECOOP’2000) (BE´ZIVIN J and ERNST J, Eds), Cannes, France, 13 June 2000, pp 1–4, Nice, Sophia Antipolis, France.

ATKINSON C and KU¨HNE T (2000b) Strict profiles: why and how. In Proceedings of the 3rd International Conference on the Unified Modeling Language – Advancing the Standard (UML 2000) (EVANS A, KENT S and S B, Eds), 2–6 October, York, UK, Lecture Notes in Computer Science 1939, pp 309–322, Springer-Verlag, Berlin, Heidelberg.

ATKINSON C and KU¨HNE T (2001) The essence of multilevel metamodeling. In Proceedings of the 4th International Conference on the Unified Modeling Language, Modeling Languages, Concepts, and Tools (UML 2001) (GOOS G, HARTMANIS J and VAN LEEUWEN J, Eds), 1–5 October, Toronto, Canada, Lecture Notes in Computer Science 2185, pp 19–33, Springer-Verlag, Berlin, Heidelberg.

BASS L, CLEMENTS P and KAZMAN R (2003) Software Architecture in Practice, 2nd edn. SEI series in software engineering, Addison-Wesley, Boston.

BECKER J, ALGERMISSEN L, FALK T and PFEIFFER D (2006) Reorganization potential in public administrations: identification and measurement with the PICTURE-approach. In Proceedinas of the 5th Internationg EGOV Conference (WIMMER M, SCHOLL HJ, GRO¨NLUND A<sup>˚</sup> and ANDERSEN KV, Eds), 4–8 September, pp 111–119, Krakow, Poland.

BECKER J, ALGERMISSEN L, PFEIFFER D and RA¨CKERS M (2007a) Building blockbased modeling of process landscapes with the PICTURE-approach. Wirtschaftsinformatik 49(4), 267–279.

BECKER J, PFEIFFER D and RA¨CKERS M (2007b) Domain specific process modelling in public administrations: the PICTURE-approach. In Electronic Government (WIMMER M, SCHOLL J and GRO¨ NLUND A<sup>˚</sup> , Eds), Lecture Notes in Computer Science 4656, pp 68–79, Springer-Verlag, Berlin, Heidelberg.

BERNSTEIN PA, HALEVY AY and POTTINGER RA (2000) A vision for management of complex models. SIGMOD Record (ACM Special Interest Group on Management of Data) 29(4), 55–63.

BRIGGS RO (2006) On theory-driven design and deployment of collaboration systems. International Journal of Human-Computer Studies 64, 573–582.

BRINKKEMPER S (1996) Method engineering: engineering of information systems development methods and tools. Information and Software Technology 38(4), 275–280.

BRINKKEMPER S, SAEKI M and HARMSEN F (1998) Assembly techniques for method engineering. In Proceedings of the 10th International Conference on Advanced Information Systems Engineering (CAiSE) (P B and T C, Eds), June, Lecture Notes in Computer Science 1413, pp 381–400, Springer-Verlag, Berlin, Heidelberg.

BUCKL C, KNOLL A, SCHIEFERDECKER I and ZANDER J (2011) Model-based analysis and development of dependable systems. In Model-based Engineering of Embedded Real-time Systems (GIESE H, KARSAI G, LEE E, RUMPE B and SCHA¨TZ B, Eds), Volume 6100 of Lecture Notes in Computer Science, pp 271–293, Springer, Berlin.

C F and U A (2004) Architectures to survive technological and business turbulences. Information Systems Frontiers 6(1), 9–21.

DARKE P and SHANKS GG (1996) Stakeholder viewpoints in requirements definition. Requirements Engineering 1(1), 88–105.

DEUTSCH M (2009) Experimental philosophy and the theory of reference. Mind and Language 24(4), 445–466.

DIETZ G and JUHRISCH M (2010) Model-based management – design and experimental evaluation. In Proceedings of the 14th Pacific Asia Conference on Information Systems, pp 452–462, Paper 44, Taipei,

University of Technology in Germany, where he also received his masters and doctorate degrees. His research interests include method engineering, modeldriven architectures, and service-oriented information systems.

Taiwan. Association for Information Systems, Acapulco, Mexiko. [WWW document] http://aisel.aisnet.org/pacis2010/44.

DIETZ G, JUHRISCH M and ESSWEIN W (2009) On the restriction of conceptual modeling – outlining an approach to enable business driven SOA. In Proceedings of the 15th Americas Conference on Information Systems (AMCIS), pp 1–14, Paper 580, San Francisco. [WWW document] http://aisel.aisnet.org/amcis2009/580.

FRANK U (1999) Conceptual modelling as the core of the information systems discipline – perspectives and epistemological challenges. In Proceedings of the Fifth America’s Conference on Information Systems (AMCIS 99) (HASEMAN D, NAZARETH S, and GOODHUE D, Eds), pp 695–697, Association for Information Systems, Milwaukee.

GEHLERT A (2007) Migration fachkonzeptueller Modelle. Logos Berlin, Berlin.

GEHLERT A, SCHERMANN M, POHL K and KRCMAR H (2009) Towards a research method for theory-driven design research. In Business Services: Konzepte, Technologien, Anwendungen, 9. Internationale-Tagung Wirtschaftsinformatik (HANSEN HR, KARAGIANNIS D and FILL H-G, Eds), Vol. 1, pp 441–450, O<sup>¨</sup> sterreichische Computer Gesellschaft, Wien.

GREGOR S (2006) The nature of theory in information systems. MIS Ouarterly 30. 611–642.

HADAR I and SOFFER P (2006) Variations in conceptual modeling: classification and ontological analysis. Journal of the Association for Information Systems 7(8). 568–592.

HARMSEN F, BRINKKEMPER S and OEI JLH (1994) Situational method engineering for information system project approaches. In Methods and associated tools for the information systems life cycle, Proceedings of the IFIP Working Conference (VERRIJN-STUART AA and OLLE TW, Eds), pp 169–194, IFIP, Elsevier Science BV, North-Holland.

HEVNER AR, MARCH ST, PARK J and RAM S (2004) Design science in information systems research. MIS Quarterly 28(1), 75–105.

HORVATH P and GLEICH R (1998) Prozeß-Benchmarking in der Maschinenbaubranche. Zeitschrift fu¨r wirtschaftlichen Fabrikbetrieb 93(7–8), 325-329.

HOVSEPYAN A, BAELEN S, BERBERS Y and JOOSEN W (2009) Specifying and composing concerns expressed in domain-specific modeling languages. In Objects, Components, Models and Patterns Volume 33 of Lecture Notes in Business Information Processing (AALST W, MYLOPOULOS J, SADEH NM, SHAW MJ, SZYPERSKI C, ORIOL M and MEYER B, Eds), pp 116–135, Springer, Berlin.

JUHRISCH M (2010) Richtlinien fu¨r die modellgetriebene Integration serviceorientierte Architekturen in Analysemodellen. PhD Thesis, Technische Universita¨t Dresden.

JUHRISCH M and DIETZ G (2010a) Constraints in conceptual modelling – outlining an approach to business driven web service composition. International Journal of Internet and Enterprise Management 6(3), 248–265.

J M and D G (2010b) Context-based modeling: introducing a novel modeling approach. In Modellierung betrieblicher Informationssysteme (MobIS 2010) (ESSWEIN W, TUROWSKI K and JUHRISCH M, Eds), Lecture Notes in Informatics (LNI), P-171, pp 111–130, Bonner Ko¨llen Verlag, Bonn.

JUHRISCH M, DIETZ G, WELLER J and ESSWEIN W (2009) Towards business driven web service authorization – project experiences in German university administrations. In Proceedings of the 15th Americas Conference on Information Systems (AMCIS 2009), pp 1–11, Paper 348, Association for Information Systems, Acapulco, Mexiko. [WWW document] http://aisel.aisnet.org/amcis2009/348.

JUHRISCH M and ESSWEIN W (2007) Closing the gap between enterprise models and service-oriented architectures. In /EEE Proceedinas of the 3rd

International Conference on Systems, Computing Science and Software Engineering (SCSS 2007) (SOBH T, Ed.), Springer, Bridgeport, USA.

JUHRISCH M and WELLER J (2008) Connecting business and IT: a model-driven webservice based approach. In Proceedings of the 12th Pacific Asia Conference on Information Systems (PACIS), pp 1469–1479, Paper 215, Suzhou, China. Association for Information Systems, Acapulco, Mexiko. [WWW document] http://aisel.aisnet.org/ pacis2008/215.

JUHRISCH M, WELLER J and DIETZ G (2007) Towards a model-driven approach to control identity management systems. In Proceedings of the 11th Pacific Asia Conference on Information Systems, pp 1–13, Paper 149, Auckland, New Zealand. Association for Information Systems, Acapulco, Mexiko. [WWW document] http://aisel.aisnet .org/pacis2007/149.

JUHRISCH M, WELLER J and DIETZ G (2008) Application access control using enterprise models. In Proceedings of the 12th Asia Conference on Information Systems (PACIS 2008) Suzhou, China. Association for Information Systems, Acapulco, Mexiko.

KAROW M, GEHLERT A, BECKER J and ESSWEIN W (2006) On the transition from computation independent to platform independent models. In AMCIS Conference Proceedings, Paper 469, pp 3913–3921, Association for Information Systems, Acapulco, Mexiko. [WWW document] http:// aisel.aisnet.org/amcis2006/469.

KELLY S, ROSSI M and TOLVANEN J-P (2005) What is needed in a metacase environment. Journal of Enterprise Modelling and Information Systems Architectures 1(1), 25–35.

KELLY S and TOLVANEN J-P (2000) Visual domain-specific modeling: benefits and experiences of using metacase tools. In Proceedings of International Workshop on Model Engineering (in conjunction with ECOOP’ 2000) (B J and E J, Eds), Cannes, France.

KHATRI V, VESSEY I, RAMESH V, CLAY P and PARK S-J (2006) Understanding conceptual schemas: exploring the role of application and its domain knowledge. Information Systems Research 17(1), 81–99.

KIEBURTZ R, MCKINNEY L, BELL JM, HOOK J, KOTOV A, LEWIS J, OLIVA DP, SHEARD T, SMITH I and WALTON L (1996) A software engineering experiment in software component generation. In Proceedings of 18th International Conference on Software Engineering 542–552, IEEE Computer Society Press, Berlin, Germany.

KRA¨MER S (1988) Symbolische Maschinen. Die Idee der Formalisierung im geschichtlichem Abriß. Wissenschaftliche Buchgesellschaft, Darmstadt.

KROGSTIE J, SINDRE G and JøRGENSEN H (2006) Process models representing knowledge for action: a revised quality framework. European Journal of Information Systems 15(1), 91–102.

KUGELER M (2000) Informationsmodellbasierte Organisationsgestaltung, Modellierungskonventionen und Referenzvorgehensmodell zur prozessorientierten Reorganisation. PhD Thesis, Westfa¨lische Wilhelms-Universität Münster. Münster

LARKIN JH and SIMON HA (1987) Why a diagram is (sometimes) worth ten thousand words. Cognitive Science 11, 65–99.

L T, R B, S ¨ B and S J (2011) Model evolution and management. In Model-based Engineering of Embedded Real-time Systems (GIESE H, KARSAI G, LEE E, RUMPE B and SCHTZ B, Eds), Volume 6100 of Lecture Notes in Computer Science, pp 241–270, Springer, Berlin.

LINDLAND OI, SINDRE G and SøLVBERG A (1994) Understanding quality in conceptual modeling. IEEE Software 11(2), 42–49.

LOCKE J (1994) An Essay Concerning Human Understanding, 24th edn. William Baynes and Son, Indianapolis, IN.

LONG E, MISRA A and SZTIPANOVITS J (1998) Increasing productivity at Saturn. IEEE Computer 35, 35–43.

LORENZEN P (1973) Semantisch normierte Orthosprache. In Zum normativen Fundament der Wissenschaft (KAMBARTEL F, Ed.), pp 231–249, Athena¨um-Verlag, Berlin.

LYONS J (1995) Linguistic Semantics: An Introduction. Cambridge University Press, Cambridge, New York.

LYONS J (2000) Bedeutungstheorien: Die Referenztheorie, die Ideationstheorie, Verhaltenstheorie der Bedeutung und behaviouristische Semantik, strukturelle Semantik, Bedeutung und Gebrauch, Wahrheitsbedingungen-Theorien der Bedeutung. In Sprachwissenschaft: Ein Reader (HOFFMANN L, Ed.), 2nd edn, pp 624–642, Walter de Gruyter Verlag, Berlin.

MARCH ST and SMITH GF (1995) Design and natural science research on information technology. Decision Support Systems 15(4). 251–266.

MELLOR S and BALCER M (2002) Executable UML: A Foundation for Modeldriven Architecture. Addision-Wesley, Munich.

MELLOR S and SHLAER S (1991) Object Life Cycles: Modeling the World in States. Computing Series, Yourdon Press, Englewood Cliffs, NJ.

MIKKONEN T and PRUUDEN P (2001) Flexibility as a design driver. IEEE Computer 34(11), 52–56.

MOHAGHEGHI P and HAUGEN Ø (2010) Evaluating domain-specific modelling solutions. In Advances in Conceptual Modeling – Applications and Challenges Volume 6413 of Lecture Notes in Computer Science (TRUJILLO J, DOBBIE G, KANGASSALO H, HARTMANN S, KIRCHBERG M, ROSSI M, REINHARTZ-BERGER I, ZIMNYI E, and FRASINCAR F, Eds), pp 212–221, Springer, Berlin.

OMG OBJECT MANAGEMENT GROUP (2002) Meta-object Facility (MOF) specification. Version 1.4. [WWW document] http://www.omg.org/mof/.

OMG OBJECT MANAGEMENT GROUP (2007) UML 2.1.2 superstructure specification. [WWW document] http://www.omg.org/spec/UML/ 2.1.2/Superstructure/PDF/.

P O and R I (1995) OASIS: a class-definition language to mode information systems using an object-oriented approach. In SP-UPV 95–788, UPV Publication Service, Valencia, Spain.

PEDRO L, RISOLDI M, BUCHS D, BARROCA B and AMARAL V (2009) Composing visual syntax for domain specific languages. In Human-Computer Interaction. Novel Interaction Methods and Techniques (JACKO J, Ed.), Volume 5611 of Lecture Notes in Computer Science, pp 889–898, Springer, Berlin.

PEFFERS K, TUUNANEN T, ROTHENBERGER MA and CHATTERJEE S (2008) A design science research methodology for information systems research. Journal of Management Information Systems 24(3), 45–77.

PFEIFFER D (2007) Constructing comparable conceptual models with domain specific languages. Proceedings of the 15th European Conference on Information Systems (ECIS2007), pp 876–888, University of St. Gallen, St. Gallen, Switzerland.

PFEIFFER D (2008) Semantic business process analysis – building blockbased construction of automatically analyzable business process models. PhD Thesis, Westfa¨lische Wilhelms-Universita¨t Mu¨nster.

PFEIFFER D and GEHLERT A (2005) A framework for comparing conceptual models. In Enterprise Modelling and Information Systems Architectures: Proceedings of the Workshop in Klagenfurt (DESEL J and FRANK U, Eds), Lecture Notes in Informatics P-75, pp 108–122, Ko¨llen Druck + Verlag GmbH, Bonn.

ROSEMANN M (1996) Multiperspektivische Informationsmodellierung auf der Basis der Grundsa¨tze ordnungsma¨ßiger Modellierung (in German, Multiperspective information modelling using the guidelines of modelling). Management & Computer 4(4), 219–226.

R M (2000) Vorbereitung der Prozessmodellierung. In Prozessmanagement. Ein Leitfaden zur prozessorientierten Organisationsgestaltung (BECKER J, KUGELER M, and ROSEMANN M, Eds), pp 45–90, Springer-Verlag, Berlin, Heidelberg (English translation: see R 2007).

ROSEMANN M (2007) Preparation of process modeling. In Process Management: A Guide for the Design of Business Processes (BECKER J, KUGELER M and ROSEMANN M, Eds), 2nd edn, pp 41–78, Springer-Verlag, Berlin, Heidelberg.

SAEKI M (2006) Configuration management in a method engineering context. In Advanced Information Systems Engineering, 18th International Conference, CAiSE 2006 (DUBOIS E and POHL K, Eds), June, Luxembourg, Lecture Notes in Computer Science 4001, pp 384–398 Springer-Verlag, Berlin, Heidelberg.

SCHMIDT DC (2006) Guest editor’s introduction: model-driven engineering. IEEE Computer 39(2), 25–31.

SCHU¨TTE R and ROTTHOWE T (1998) The guidelines of modeling: an approach to enhance the quality in information models. In Proceedings of the 17th International Conference on Conceptual Modeling (ER 1998) (LING TW, RAM S and LEE ML, Eds) Lecture Notes in Computer Science 1507, pp 240–254, Springer-Verlag, Berlin, Heidelberg.

SOFFER P and HADAR I (2007) Applying ontology-based rules to conceptual modeling: a reflection on modeling descision making. European Journal of Information Systems 16(5), 599–611.

SUHL L and BLUMSTENGEL A (2002) System engineering. In Essences of Business Informatics. Foundations, Applications, PC Praxis (FISCHER J, HEROLD W, DANGELMAIER W, NASTANSKY L and SUHL L, Eds), pp 323–404, Erich Schmidt Verlag. Berlin.

SZTIPANOVITS J, KARSAI G and BAPTY T (1998) Self-adaptive software for signal processing. Communications of the ACM 41(5). 66–73.

TOLVANEN J-P (1998) Incremental method engineering with modeling tools: theoretical principles and empirical evidence. PhD Thesis, University of Jyva¨skyla¨.

VAISHNAVI V and KuECHLER W (2004) Design research in information systems. [WWW document] http://desrist.org/design-research-ininformation-systems (accessed 16 August 2009).

WALLS JG, WIDMEYER GR and SAWY OAE (1992) Building an information system design theory for vigilantes. Information Systems Research 3(1), 36–59.

WAND Y and WEBER R (2002) Research commentary: information systems and conceptual modeling – a research agenda. Information Systems Research 13(4), 363–377.

WELLER J and ESSWEIN W (2006) Consequences of meta-model modifications within model configuration management. In Meta-Modelling and Ontologies, Proceedings of the 2nd Workshop on Meta-Modelling (WoMM) (BROCKMANS S, JUNG J and SURE Y, Eds), Lecture Notes in Informatics P-96, pp 125–139, Gesellschaft fu¨r Informatik, Ko¨llen Druck + Verlag GmbH, Bonn.

WILDE T and HESS T (2007) Forschungsmethoden der Wirtschaftsinformatik: Eine empirische Untersuchung. Wirtschaftsinformatik 49(4), 280–287.

WITTGENSTEIN L (2000) Philosophische Untersuchungen: Kap. 1, 2, 8–11, 17–18, 21, 23–25, 43, 65–67. In Sprachwissenschaft: Ein Reader (HOFFMANN L, Ed.), 2nd edn, pp 72–78, Walter de Gruyter Verlag, Berlin.
