---
otero_id: 6040
otero_key: "VX3F44DV"
title: "Conceptualizing Systems for Understanding: An Empirical Test of Decomposition Principles in Object-Oriented Analysis"
authors: "Andrew Burton-Jones; Peter N. Meso"
year: "2006"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0079"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/VX3F44DV/fulltext/images/c258ddc76e0d717065b165b6140bf9d8fb30973720484a0fbbf2beadf44b4dac.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Conceptualizing Systems for Understanding: An Empirical Test of Decomposition Principles in Object-Oriented Analysis

Andrew Burton-Jones, Peter N. Meso,

To cite this article:

Andrew Burton-Jones, Peter N. Meso, (2006) Conceptualizing Systems for Understanding: An Empirical Test of Decomposition Principles in Object-Oriented Analysis. Information Systems Research 17(1):38-60. http://dx.doi.org/10.1287/isre.1050.0079

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2006, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/VX3F44DV/fulltext/images/1b5e74253a882d4b611de4d73a86de37c9494fc802abf752110e66984b7cf802.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Conceptualizing Systems for Understanding: An Empirical Test of Decomposition Principles in Object-Oriented Analysis

Andrew Burton-Jones

Management Information Systems Division, Sauder School of Business, University of British Columbia, 2053 Main Mall, Vancouver, British Columbia, Canada V6T 1Z2, andrew.burton-jones@sauder.ubc.ca

Peter N. Meso

Computer Information Systems Department, J. Mack Robinson College of Business, Georgia State University, 35 Broad Street, Atlanta, Georgia 30302, pmeso@cis.gsu.edu

uring the early phase of systems development, systems analysts often conceptualize the domain under study and represent it in one or more conceptual models. One of the most important, yet elusive roles of conceptual models is to increase analysts’ understanding of a domain. In this paper, we evaluate the ability of the good decomposition model (GDM) (Wand and Weber 1990) to explain the degree to which conceptual models communicate meaning about a domain to analysts. We address the question, “Do unified modeling language (UML) analysis diagrams that manifest better decompositions increase analysts’ understanding of a domain?” GDM defines five conditions (minimality, determinism, losslessness, weak coupling, and strong cohe sion) deemed necessary to decompose a domain in such a way that the resulting model communicates meaning about the domain effectively. In our evaluation, we operationalized each of these conditions in a set of UML diagrams and tested participants’ understanding of those diagrams. Our results lend support to GDM across measures of actual understanding. However, the impact on participants’ perceptions of their understanding was equivocal.

Key words: systems analysis; conceptualization; conceptual model; decomposition; object oriented; unified modeling language; ontology; systems principles

History: Salvatore March, Senior Editor; George Marakas, Associate Editor. This paper was received on February 6, 2004, and was with the authors 13 <sup>3</sup> 4 months for 3 revisions.

## 1. General Research Problem

A key activity in systems analysis is to conceptualize the domain under study and represent it in one or more conceptual models. Conceptual models serve as representations of users’ perceptions of the static and dynamic phenomena in a domain and are usually graphical in nature (Davis 1992) (Figure 1a). Conceptual models have at least four purposes: (1) to increase analysts’ understanding of a domain, (2) to help developers and users to communicate, (3) to serve as a basis for design, and (4) to serve as documentation of the original requirements of the system (Kung and Solvberg 1986). We investigate the first of these purposes. We aim to identify principles that can explain the extent to which conceptual models communicate meaning about a domain to analysts.

The ability of conceptual models to increase analysts’ understanding of a domain has long been noted (Chen 1976), but initial research on this topic suffered from a lack of theory (Davis 1992). Without theory, researchers initially created conceptual modeling techniques based on personal experience or exploratory case studies (Olle et al. 1988). This led to a proliferation of techniques, denoted the “yet another modeling approach” (YAMA) syndrome (Wand and Weber 2002). In the last decade, theorydriven research has emerged to evaluate the extent to which conceptual models communicate meaning. Two research streams emerged: (1) intergrammar evaluations, which investigate whether different grammars communicate meaning more effectively in different tasks (Vessey and Conger 1994, Kim and

March 1995, Agarwal et al. 1996, Kim et al. 2000); and (2) intragrammar evaluations, which investigate principles for improving the use of one grammar when used on its own (Bodart et al. 2001, Gemino 2004, Shanks et al. 2004).

In this paper, we aim to contribute an improved understanding of principles that influence the extent to which conceptual models created via one grammar communicate meaning to analysts. We contribute to intragrammar rather than intergrammar evaluations for two reasons. First, even though a variety of conceptual modeling grammars are used in practice, many researchers and practitioners suggest that object-oriented (OO) systems analysis with the unified modeling language (UML) may be emerging as a de factor standard (Kobryn 1999, Purao and Vaishnavi 2003). Thus, by focusing our efforts on the UML grammar, we can focus on an important grammar in practice (Dobing and Parsons 2005). Second, notwithstanding its rapid emergence, many researchers note that OO analysis with UML is still not yet as well understood or as popular in practice as other approaches, and they have called for stronger theoretical guidance for constructing good OO conceptual models with UML (Vessey and Conger 1994, Wieringa 1998, Sircar et al. 2001, Johnson 2002, Davies et al. 2006). Thus, our general research question is What theoretical principles can explain the extent to which different conceptual models of a domain that are created via the same conceptual modeling grammar, e.g., UMLconvey meaning about the domain to analysts?

## 2. Specific Research Problem

According to Wand and Weber (2002, p. 368), “creating a faithful representation with a grammar entails two activities: identifying the phenomena to be modeled and mapping the phenomena into the grammar’s constructs” (see Figure 1b). To date, researchers who conduct intragrammar evaluations of conceptual modeling have focused on the second of these activities, i.e., mapping. For example, Bodart et al. (2001) and Shanks et al. (2004) note that some conceptual modeling grammars offer different grammatical constructs to ostensibly model the same phenomena (e.g., modeling an optional property via a class with an optional attribute or via a subclass with a mandatory attribute). Relying on a theory known as the

Figure 1 (a) Conceptual Models as Representations (Adapted from Davis 1992); (b) Conceptual Modeling as Identification and Mapping of Phenomena

![](/api/attachments/VX3F44DV/fulltext/images/6b829d10590bdac9d75a97bbbdef06502a9bef944f2a30f75d810b0aee32ef86.jpg)

“representation model” (Wand and Weber 1990), these studies found support for their predictions about the degree to which some grammatical constructs provide a clearer mapping of certain real-world phenomena than others.

In this paper, we complement this line of research by investigating principles for the first activity in Figure 1b: identifying the phenomena to model. In this respect, it is critical to stress that when undertaking the “identification” activity, analysts can “see” the world in different ways. Phenomena are not “out there” for analysts to identify. Rather, analysts have to use explicit and/or implicit principles to perceive and conceive real-world phenomena in useful, accurate ways before they map their conception into conceptual modeling constructs. As Goguen and Varela (1979) emphasize: “The world does not present itself to us neatly divided into systems, subsystems, environments     These are divisions which we make ourselves.”

What principles can be used in the identification phase of conceptual modeling to perceive and conceive real-world phenomena in useful, accurate ways? This is very much an open research question. Even so, some researchers and practitioners suggest that two cognitive principles are fundamental (Coad and Yourdon 1991, Paulson and Wand 1992, Parsons 1996):

• Decomposition: a top-down process by which individuals “breakdown    a complex system into smaller, relatively independent units” (Paulson and Wand 1992, p. 174), and

• Classification: a bottom-up process by which individuals “group individual things into categories based on similarity” (Parsons 2002, p. 159).

Decomposition and classification are fundamental processes that people use when comprehending phenomena (Lackoff 1987, Simon 1996) and systems analysts have long known of their importance (Lieberman 2003). For example, Larman (2001, p. 128) suggests that the “quintessential object-oriented step in analysis    is the decomposition of a domain of interest into individual conceptual classes.” It is surprising, therefore, that there are no generally accepted theories of decomposition and classification to support the identification phase of conceptual modeling. This aspect of conceptual modeling remains much more of an art than a science (Weber 1997, Lieberman 2003).

Although there is a great need for research on decomposition and classification, we focus on decomposition alone. We do so because while some studies have examined the potential for theories of classification to inform OO systems analysis (Parsons and Wand 1997), there has been no such research on decomposition. To investigate the potential for theories of decomposition to inform OO conceptual modeling in UML, we set out to identify a theory of decomposition that could explain the degree to which OO analysis models in UML convey meaning to analysts. Various principles and techniques exist to help practitioners achieve good decompositions. Perhaps the most well known are those of “functional” decomposition (Yourdon 1989). Despite the existence of such principles, only one general theory of decomposition has been proposed in information systems (IS) to our knowledge: the good decomposition model (GDM) (Wand and Weber 1990).

GDM derives from a theory of ontology (Bunge 1977, 1979) and memory (Collins and Quillan 1969) and specifies five criteria for defining a good decomposition. The relevance of GDM for OO analysis has not been studied to date, but its relevance for OO design is established. Specifically, GDM formed the basis of Chidamber and Kemerer’s (1994) OO design metrics suite, which is the most popular OO design metrics suite in practice (El-Emam 2002). However, Chidamber and Kemerer only operationalized two of GDM’s five criteria. GDM itself has never been subject to a full empirical test, nor has it ever been applied to systems analysis. If GDM is valid, OO analysis models in UML that comply with its criteria should communicate more meaning (i.e., facilitate more understanding) than models that do not (Simon 1996). Thus, we refine our general question into the specific research question studied in this paper: Do UML analysis diagrams that manifest better decompositions according to the good decomposition model- increase analysts’ understanding of a domain?

Two criticisms might be made in relation to this question. First, one might argue that the answer is obvious because the benefit of good decompositions may appear to be self-evident. While we acknowledge this criticism, our view is that there is little empirical evidence to show whether (and if so, how) the expected benefits of good decompositions are realized (Weber 1997, Bandi et al. 2003). Moreover, even if the benefits of good decompositions are selfevident, the relevant criteria for evaluating decomposition quality have never been clear (Parnas 1972, Briand et al. 1999). GDM offers several criteria, but these criteria have never been fully operationalized and tested. Thus, we do not believe that GDM’s value is self-evident.

Second, one might question our assumptions. We argue that decomposition occurs in the identification phase of conceptual modeling, but we test its effects by examining analysts’ understanding of a conceptual model (a UML diagram). As a result, our study assumes that decomposition problems that occur in the identification phase flow through to the conceptual model, i.e., they are not overcome in the mapping phase (see Figure 1b). One might argue that our research question might be irrelevant if such problems could be completely overcome in the mapping phase. While we acknowledge this criticism, we believe that the research question would still be important even in the unlikely situation that all decomposition problems could be overcome in the mapping phase. This is because the results of testing it can serve to highlight which issues should be attended to in the mapping phase (e.g., all GDM criteria or merely a subset of them) and the importance of doing so (e.g., the relative improvement in understanding that will result from addressing the criteria). We return to this issue in the discussion section (§7).

## 3. Good Decomposition Model (GDM)

The decomposition process involves perceiving a “messy” real-world domain (or users’ perception of that domain) and breaking it down to identify its structure and behavior. Following Figure 1b, once an analyst has identified the domain’s structure and behavior, s/he can engage in the mapping process to articulate her/his conception using the constructs of a modeling grammar (e.g., UML). In UML, the final conceptualization is typically specified across several interrelated diagrams, such as a class diagram, use case, and state chart (Rumbaugh et al. 1999).

Figure 2 Alternative Decompositions from the Real World to a Conceptual Model  
![](/api/attachments/VX3F44DV/fulltext/images/90ebb09d81e407c968f2651e85164cb3263534d088c3d4e63d1cfabaf15a5507.jpg)

As Figure 2 shows, an analyst could propose several decompositions to represent their conception of a domain. The aim of GDM is to propose a necessary set of criteria for determining the relative quality of alternative decompositions (Wand and Weber 1990).

## 3.1. GDM Criteria: Background

Like most theories, GDM draws heavily on prior work. Figure 3 illustrates the key strands of influence on GDM.

The first strand of influence on GDM is ontology (Bunge 1977, 1979). Ontology is a philosophical field that studies the structure and behavior of the world. GDM relies on ontology in two ways. First, ontology provides precise definitions for important concepts that humans use to decompose systems (e.g., class, attribute, event, law, etc.). These concepts have specific meanings in GDM that are distinct from but can be mapped to constructs in grammars such as UML.

Second, it allows GDM to make assumptions about the nature of systems and decompositions. In relation to the nature of systems, GDM draws on Bunge’s ontology to assume that systems comprise static phenomena (e.g., things, properties, laws, and subsystems), dynamic phenomena (e.g., events and state variables), and their interactions. In relation to the nature of decompositions, GDM draws on Bunge’s ontology to propose that the quality of a decomposition can be assessed by examining the characteristics of the system in response to dynamics (Paulson and Wand 1992). That is, rather than evaluate decomposition quality according to how well it serves a particular function (as in “functional decomposition”), GDM evaluates decomposition quality according to five criteria that characterize the coherence and efficiency with which a system responds to dynamics: minimality, determinism, losslessness, weak coupling, and strong cohesion (see Table 1).

Figure 3 Influences on GDM  
![](/api/attachments/VX3F44DV/fulltext/images/c701274c4b48c8a6ef9d77fb893fa812307a9f8677396e1c16a22b9e795a2410.jpg)

As Figure 3 shows, the second strand of influence on GDM is existing principles in other fields. Three fields are very influential: automata theory (for minimality and determinism), database (for losslessness), and programming (for coupling and cohesion) (Table 2). GDM does not define its criteria in exactly the same way used in these fields. Rather, it defines all of its criteria using a consistent language based on ontology. For example, the definitions of minimality and losslessness in GDM are related to, but are more general than, the definitions of minimality and losslessness in automata theory and database theory. The GDM definitions are no more (or less) “correct” than the definitions in these other fields; they are simply more general.

Table 1 Definitions of GDM Criteria (Adapted from Weber 1997)

<table><tr><td>Criterion</td><td>A conceptualization manifests a good decomposition only if</td></tr><tr><td>Minimality</td><td>...for every subsystem at every level in the level structure of the system there are no redundant state variables.</td></tr><tr><td>Determinism</td><td>...every event at every level in the level structure of the system is either an external event or a well-defined internal event.</td></tr><tr><td>Losslessness</td><td>...every hereditary state variable and every emergent state variable in a system is preserved in the decomposition.</td></tr><tr><td>Weak coupling</td><td>...the cardinality of the totality of input for each subsystem of the decomposition is less than or equal to the cardinality of the totality of input for each equivalent subsystem in the equivalent decomposition.</td></tr><tr><td>Strong cohesion</td><td>...for every set of outputs, all output variables affected by input variables are contained in the same set, and the addition of any other output to the set does not extend the set of inputs on which the existing outputs depend.</td></tr></table>

Table 2 GDM Criteria and Existing Decomposition Principles

<table><tr><td rowspan="2">Criterion</td><td colspan="4">Example of a related criterion in an existing field</td><td rowspan="2">Other fields that use a similar criterion</td></tr><tr><td>Criterion</td><td>Field</td><td>Description</td><td>Relevant reference</td></tr><tr><td>Minimality</td><td>Reachability</td><td>Petri-nets</td><td>All states must be reachable (must not be redundant)</td><td>Murata (1989)</td><td>Automata theory, Database theory</td></tr><tr><td>Determinism</td><td>Guard condition</td><td>Statecharts</td><td>States that lead to two or more poststates should have guard conditions to specify the appropriate path</td><td>Harel (1987)</td><td>Automata theory</td></tr><tr><td>Losslessness</td><td>Losslessness</td><td>Database</td><td>Inferences must not be lost when breaking a table into joined tables</td><td>Aho et al. (1979)</td><td>File/data compression</td></tr><tr><td>Weak coupling Strong cohesion</td><td>Coupling Cohesion</td><td>Programming</td><td>Modules should have minimal external interactions and high internal integration</td><td>Yourdon and Constantine (1979)</td><td>Industrial and managerial design</td></tr></table>

## 3.2. Applying GDM Criteria to

## OO Analysis in UML

UML offers many diagrams to support OO analysis, e.g., class diagrams, use case diagrams, sequence diagrams, and statecharts (Dobing and Parsons 2005). Violations of GDM criteria can occur in all of these diagrams, but some criteria pertain more to some diagrams than others. In the sections below, we explain each criterion, discuss the UML diagrams that each criterion pertains to, and provide an example violation of each one. Two issues should be noted in relation to these examples. First, the examples present simple, direct violations. More complex or subtle violations could certainly occur on the same or different diagrams. Second, violations of GDM criteria will rarely be explicit. Rather, violations will generally be implicit in the diagram’s semantics. Thus, while the violations shown in the examples below are fairly clear, it may not always be easy in practice to determine whether a violation actually exists.

To satisfy minimality, a system cannot contain redundant state variables, i.e., variables that do not change state or are not used during a system’s life. In UML, attributes represent state variables (Rumbaugh et al. 1999). Thus, violations of minimality are evident in a class diagram when an attribute is shown that no method in the system uses and that the system does not need. Figure 4 provides an example in the context of a contracting firm. The “applicant” classes show various attributes and methods. The violation of minimality contains two additional attributes (ethnic origin and eye color). Note that one must have an understanding of the domain modeled in the diagram to infer that these two attributes are redundant. For example, it is hard to think of a situation where “eye color” will be a relevant attribute to consider during a firm’s hiring process, but some government regulations may require businesses to consider “ethnic origin” during hiring.

Determinism relates to a system’s predictability in response to events. In UML, events are shown explicitly in statecharts and implicitly in activity and class diagrams. Bunge’s (1977) ontology distinguishes between external and internal events. External events are changes of state in a system caused by a change of state in another system or subsystem. Such events are inherently unpredictable. For example, a class cannot know when another class will send it a message.

Figure 4 Minimality—A Violation Occurs when a Class Contains Redundant State Variables

<table><tr><td>Violation</td><td>No violation</td></tr><tr><td>Applicant</td><td>Applicant</td></tr><tr><td>-Name-Application date-Resume date-Certification level-Ethnic origin-Eye color+Rejection letter()+Acceptance letter()</td><td>-Name-Application date-Resume date-Certification level+Rejection letter()+Acceptance letter()</td></tr></table>

Figure 5 Determinism—A Violation Occurs when an External Event Is Not Named or when an Internal Event Leads to More Than One Postevent State  
![](/api/attachments/VX3F44DV/fulltext/images/912883e9eb0f31db22c1318ae140b448890f6d29b366e72281327350a2e1da0b.jpg)  
<sup>.\_\_\_</sup> Internal event: Details the operation the class performs to change its state.  
<sup>\_\_\_\_.\_\_\_</sup> External event: Details the name of the external class and its state variable that triggers the change of state shown.

Although external events are unpredictable, the determinism condition requires that they be named so that the system knows their existence (Weber 1997). For example, in Figure 5, the diagram with no violation shows that applicants move from “on call” back to “in demand” when jobs are cancelled. The diagram with the violation shows that the move to “on call” depends on something related to the “job” class, but it does not name the external event. Thus, an analyst reading this diagram would need to review other diagrams of the domain and rely on his/her existing knowledge of the domain to determine what jobrelated event might explain the move to “on call.”

Internal events are internal state changes that a system controls, such as methods operating on attributes in their class. Determinism requires that internal events be named and well defined. A well-defined event means that given a specific pre-event state, an internal event leads to one and only one postevent state. Violations of this condition typically occur when an external event is overlooked (Weber 1997). Figure 5 gives an example. The diagram with the violation shows that applicants move from “in demand” to “on call” as a result of an internal event (“status update”) but that two further internal events (“retire” and “status update”) occur that lead to different states. The problem is that it is not clear why one of these internal events would occur rather than the other one. The diagram with no violation shows that a relevant external event had been overlooked: applicants move from “on call” to “requested” if the client interview is a success. Once again, if an analyst had to understand the diagram with the violation, s/he would have to review other diagrams of the domain and consider his/her existing knowledge of the domain to determine what factor(s) might cause the applicant to move to one or other postevent state.

Losslessness requires that emergent properties (i.e., properties emerging from subsystems interacting) are not lost during decomposition. In UML, properties are shown as attributes in class diagrams. Figure 6 gives an example. The diagram with a violation shows that applicants can have many contracts and receive a performance rating on each one. The diagram with no violation shows that applicants also have an emergent property—an overall performance rating—that derives from, but is not reducible to, the history of performance ratings on individual contracts. As a result, analysts who receive the diagram with the violation may not be aware of the presence of or implications of the emergent property in the business domain being modeled.<sup>1</sup>

Coupling refers to interactions among subsystems (Weber 1997). In OO design, Chidamber and Kemerer (1994) operationalized GDM’s definition of coupling as methods in one object uses methods or instance variables in another object. We apply the same operationalization to OO analysis and measure coupling as the number of other classes to which an object is coupled, including the number of ways that each object is coupled to any other object. In UML, interactions are represented explicitly on sequence diagrams and implicitly (via methods and associations) on class diagrams. Figure 7 gives an example. In the diagram with the violation, the interview class interacts with the applicant and client classes to record interview quality and interview results. In the diagram with no violation, interaction is reduced by locating the methods in the interview class.

Violation  
Figure 6 Losslessness—A Violation Occurs when a Class Loses an Emergent Property  
No violation

<table><tr><td>Applicant</td><td rowspan="2" colspan="2">Party to</td><td>Employee contract</td><td rowspan="4">Applicant</td><td rowspan="4" colspan="2">Party to</td><td>Employee contract</td></tr><tr><td>-Name</td><td>-Terms</td><td>-Terms</td></tr><tr><td>-Certification level</td><td>1</td><td>0..n</td><td>-Performance rating</td><td>-Performance rating</td></tr><tr><td>+Update certification()</td><td></td><td></td><td>+Update performance rating()</td><td>+Update performance rating()</td></tr></table>

In GDM, strong cohesion refers to the relationship between input sets and output sets in a transformation (Dromney 1996). In OO design, Chidamber and Kemerer (1994) operationalized GDM’s definition of cohesion as the similarity of methods in a class; the larger the number of similar methods, the more cohesive the class. We apply the same definition to OO analysis. In UML, similarity of methods can be shown in class diagrams and, at a higher level, in use case diagrams. Figure 8 provides an example. The “interview” class with the violation contains attributes and methods that can logically be separated into two sets (i.e., it has disjoint outputs). Strong cohesion is restored by splitting the classes into two more cohesive classes.

In summary, GDM details five criteria deemed necessary for a decomposition to be considered good. As noted above, Figures 4–8 illustrate simple ways of violating each condition; more complex or subtle violations could occur on the same and/or on different diagrams, e.g.:

• Minimality will be violated in class diagrams if an analyst includes attributes in a parent class that do not apply to all of the child classes.

• Determinism will be violated in activity diagrams if an analyst does not specify the condition causing a split in an activity.

• Losslessness will be violated in class diagrams if an analyst decomposes classes in such a way that (a) important associations among classes are lost, or (b) part-whole relationships are not correctly specified and the attributes or class names of the wholes or parts are lost.

• Weak coupling will be violated in sequence diagrams if an analyst includes unnecessary interaction among objects.

• Strong cohesion will be violated in use case diagrams if an analyst includes too much logic in each use case.

We next outline the process by which violations of GDM criteria affect analyst understanding.

## 4. Relating Decomposition to Understanding

GDM proposes that individuals will be more able to understand systems that comply with its criteria. To explain why its conditions affect analyst understanding, we must support its criteria with theories of cognition. Two bodies of theory help to explain this link.

First, we draw upon semantic network theory to propose that GDM violations lead analysts to construct inefficient mental representations of a domain (see Table 3) (Collins and Quillan 1969). Semantic network theory states that individuals store concepts in memory as nodes connected by paths (Ashcraft 2002). To perform cognitive tasks, individuals must recall concepts from memory. Recall follows a process of spreading activation: a node is primed in memory, which leads to paths connecting to it being activated (Ashcraft 2002). Activation has to be strong enough for a search to reach a connected node. Empirical tests show that greater activation strength enables faster and more accurate recall (Ashcraft 2002). As Table 3 shows, this suggests that GDM violations lead to inefficient mental representations by reducing activation strength and excluding relevant nodes.

Figure 7 Weak Coupling—A Violation Occurs when an Object Uses Methods or Instance Variables in Other Objects

<table><tr><td colspan="101">Violation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td colspan="4">Interview</td><td rowspan="2">Attends</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attends</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attends</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attends</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attends</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attends</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attenses</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attenses</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attenses</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attenses</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attenses</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2">Attenses</td><td rowspan="2">Client</td><td rowspan="2">Applicant</td><td rowspan="2">Booked on</td><td rowspan="2" colspan="4">Interview</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">- Name</td><td>+ Acceptance letter()</td><td>1</td><td>0..n</td><td>+ Record sample interview quality()</td><td>1</td><td>0..n</td><td>+ Schedule()</td><td>1</td><td>0..n</td><td>+ Rejection letter()</td><td>1</td><td>0..n</td><td>+ Create()</td><td>1</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record sample interview quality()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Schedule()</td><td>1</td><td>0..n</td><td>+ Record sample interview quality()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Schedule()</td><td>1</td><td>0..n</td><td>+ Record sample interview quality()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Schedule()</td><td>1</td><td>0..n</td><td>+ Record sample interview quality()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>0..n</td><td>1</td><td>0..n</td><td>+ Create()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>+ Record client interview result()</td><td>1</td><td>0..n</td><td>&lt;</td></tr></table>

Figure 8 Strong Cohesion—A Violation Occurs when a Class Contains Attributes and Methods that Can Logically Be Separated into Disjoint Sets  
![](/api/attachments/VX3F44DV/fulltext/images/c8ac20ffaa8557dbfe870da5bdd79f81a9a85eaac6579804851fe50973767f8f.jpg)

Second, problem-solving theories suggest that the quality of a person’s mental representation of a domain is a key driver of his/her ability to reason about the domain (Newell and Simon 1972). Specifically, problem-solving theories suggest that a person reasons about a domain by drawing on his/her mental representation of the domain together with his/her mental representation of the problem s/he faces about the domain to construct a “problem space” in memory (Newell and Simon 1972). Tests show that problemsolving performance is driven by a person’s ability to search his/her problem space (Newell and Simon 1972, Pretz et al. 2003). Because semantic network theory suggests that GDM violations lead to inefficient mental representations, we can therefore tie GDM violations to understanding by proposing that GDM violations reduce analysts’ ability to construct efficient problem spaces in memory and thereby reduce analysts’ ability to search their problem space when reasoning about the domain.

An assumption of the preceding arguments is that individuals encode elements (or chunks) of a conceptual model into memory in a more or less one-to-one mapping so that violations in the model will be manifest in an individuals’ mental representation of the model. This assumption might not hold in two situations. The first is when individuals have plenty of time to analyze a model. In this case, individuals are likely to engage in elaboration processes to restructure their semantic network. Such elaboration not only alters the mental representation of the model, but can improve an individual’s memory by increasing the priming of nodes and improving the structure of the semantic network (Ashcraft 2002, Weber 1997).

Table 3 Relating Conditions in the Good Decomposition Model to Human Understanding  
![](/api/attachments/VX3F44DV/fulltext/images/b680114d3bc88c9ba0e3c9757dc037bc21861815e7e817ce6f5fc9763974804f.jpg)

The second exception is when individuals have existing knowledge of the domain represented in the model. In such cases, individuals internalize concepts in the model by integrating them with concepts in their existing semantic network of the domain (Mayer 1989, Pretz et al. 2003). Thus, if a conceptual model suffers from GDM violations, individuals may use their existing domain knowledge to identify problems in the model and infer or conclude a more plausible interpretation of the terms or relationships in the model when internalizing it (Burton-Jones and Weber 1999). Research on the influence of domain knowledge is complex and ongoing (Khatri et al. 2006), but a reasonable conclusion based on current evidence is that empirical tests of the effect of decomposition quality on analysts’ understanding of conceptual models may not find significant effects if analysts are allowed substantial time to consider the models or if analysts have substantial knowledge of the domain shown in the model (Weber 2001).

## 5. Experiment

With the implications regarding the empirical tests above in mind, we set out to test whether UML analysis diagrams that manifest better decompositions increase analysts’ understanding. Following recent studies, we tested this across two measures of actual understanding (a problem-solving test and a cloze or “fill-in-the-blanks” test) and one measure of perceived understanding (Gemino and Wand 2003, Gemino 2004). This led to our study’s proposition and hypotheses:

Proposition. UML analysis diagrams that manifest better decompositions will increase analysts’ understanding of a domain. This increased understanding will be reflected in:

• Higher scores in problem-solving tests about the domain (Hypothesis 1).

• Higher scores in cloze tests about the domain (Hypothesis 2).

• Higher perceptions regarding the ease of understanding the UML diagrams (Hypothesis 3).

We ran a laboratory experiment to test these hypotheses. Analysts’ understanding of conceptual models is influenced by many syntactic, semantic, pragmatic, and social factors (Shanks 1999); a controlled experiment helped us test the impact of good decomposition principles alone.

## 5.1. Experimental Design

The experiment used a 1∗3 between-groups design, in which each individual received three UML diagrams that either complied with GDM criteria (good), violated three of the criteria (moderate), or violated all of them (bad). We randomly assigned participants across groups and randomly assigned the order of tasks to control for learning effects.<sup>2</sup>

## 5.2. Participants

Fifty-seven senior-level students studying OO design (OOD) at a large U.S. university participated. The sample size was small but compares favorably to other similar experiments (e.g., N 28; Kim and March 1995). Attendance was voluntary, but subjects received academic credit and prizes of \$20 were offered for the top performer in each group. All students took an OO analysis (OOA) course as a prerequisite, and both OOA and OOD courses used UML. Participants reported that they first learned UML (on average) six months prior. Their average self-reported UML experience was 3.5 out of 7 and their average domain knowledge was 3.4 out of 7 (where 4 represents an average practitioner). Overall, subjects were familiar with UML and the domain, but they were not experts.

## 5.3. Materials

Participants received three diagrams (a use case diagram, class diagram, and state chart) based on Conger’s (1994) TCI case. We chose these diagrams because together they specify a system’s function, structure, and behavior. We created three versions of each one, labeled good, moderate, and bad (see the online supplement for the diagrams: Burton-Jones and Meso 2006). The good version served as the base case. We created the moderate version by modifying the good model to violate minimality, losslessness, and determinism. The bad version violated all five conditions. We only violated minimality, losslessness, and determinism in the moderate version because Chidamber and Kemerer (1994) based their OOD metrics suite on GDM, but they excluded these three criteria from their suite. By including a condition with just these criteria violated, we could test their relevance for OOA. Figures 9–11 show the bad class diagram, use case diagram, and state chart.

Because no research has operationalized GDM criteria in OOA, we used definitions in past studies (Chidamber and Kemerer 1994, Parsons and Wand

1997, Weber 1997) to manipulate each condition. As Figures 9–11 show, manipulations were made to specific areas of the diagrams to maximally isolate their effects. To improve validity, an independent academic expert reviewed all of the manipulations and we made changes on the basis of this feedback.

We manipulated minimality by including redundant attributes in the applicant and job contract classes (Figure 9). Losslessness was also manipulated in the class diagram. It was manipulated in the 1n relationships between the applicant <sub>→</sub> employee-contract and the client <sub>→</sub> job classes. The good diagram included “overall performance rating” and “overall satisfaction rating” in the applicant and client classes. These

Figure 9 Class Diagram—Bad Decomposition  
![](/api/attachments/VX3F44DV/fulltext/images/a5f6e687a1a99587bed3e43f6bf76478f93c1e11394a6c11033a0e489e58bf91.jpg)

Figure 10 Statechart—Bad Decomposition  
![](/api/attachments/VX3F44DV/fulltext/images/377b91b0f94dd09944be2af39b436d7379112e2c63ae4e59061f14c6a3f99cca.jpg)  
<sub>External</sub> <sub>event:</sub> <sub>Details</sub> <sub>the</sub> <sub>name</sub> <sub>of</sub> <sub>the</sub> <sub>external</sub> <sub>class</sub> <sub>and</sub> <sub>its</sub> <sub>state</sub> <sub>variable</sub> <sub>that</sub> <sub>triggers</sub> <sub>the</sub> <sub>change</sub> <sub>of</sub> <sub>state</sub> <sub>shown.</sub>.-

emergent properties were lost in the bad diagram, with only the hereditary properties of “job satisfaction” and “contract performance” remaining (Figure 9). Figure 10 shows how we manipulated determinism in the state chart. We underspecified the external events (“job status” and “employee contract status”) and made the internal events (“skill in demand” and “status update”) indeterminate. Thus, for three states (in demand, on call, and requested), two internal events emerged from the subsequent state. We manipulated strong cohesion by using more aggregated use cases (Figure 11), and by collapsing service and applicant classes into one class and the sample and final interview subclasses into one class, reducing the similarity of methods (Figure 9). Finally, we manipulated weak coupling in the class diagram by inserting methods that (a) maintained coordination between classes while reducing cohesion, e.g., placing “skill-in-demand” in the job class, and (b) increased coordination between classes, e.g., “record client interview result” and “record sample interview quality” in the client and applicant classes rather than in the interview class (Figure 9).

Figure 11 Use Case Diagram—Bad Decomposition  
![](/api/attachments/VX3F44DV/fulltext/images/725eab407142ac8a654fc69c3e4ca55ed3a26cbf0bb409f76d1de1849d0b9359.jpg)

We must mention one final issue regarding the diagrams. In the context of intragrammar studies of the mapping process (per Figure 1b), Parsons and Cole (2004) argue that diagrams in such studies should: (1) be devoid of semantics (e.g., include only Greek letters), and (2) have information equivalence (i.e., the diagrams should contain the same information). As our study examines the outcome of the identification phase, not the mapping phase, neither criterion applies. In relation to semantics, we designed the diagrams to include real-world semantics (per Gemino and Wand 2004) because it improves construct and external validity. In relation to information equivalence, manipulations of GDM create information inequivalence. For example, violations of minimality result in additional (redundant) attributes in the diagrams whereas violations of losslessness result in lost (emergent) attributes. Rather than invalidate the experiment, such inequivalence is required because it is important to test whether (and if so, how much) these differences actually affect understanding. For example, participants may be able to use their existing domain knowledge to ignore redundant attributes and infer lost attributes in the diagrams. Thus, the experiment directly tests the affect of manipulating GDM conditions.

## 5.4. Dependent Variables (DVs)

The DVs measured actual and perceived understanding (see the online supplement for the measures: Burton-Jones and Meso 2006). We selected two measures of actual understanding (a problem-solving test and a cloze test) designed to capture individuals’ ability to reason about the domain represented in the model rather than simply recall concepts from memory or answer simple comprehension questions. In the context of studying student understanding of causal diagrams in education, Mayer (1989) found that such tests of deep processing were better tests of understanding than tests of shallow processing (e.g., recall or comprehension). Our application of Mayer’s work to IS research is consistent with recent studies (Bodart et al. 2001, Gemino and Wand 2003).

Problem-solving performance was measured by participants’ number of acceptable answers to problemsolving questions asked about the domain. Each question asked for a selection of answers to a business problem and an explanation of each answer. Each answer-explanation pair was worth one mark (half a mark for each part). For example, one problem was ICI has a number of applicants with skills in high demand but who are not yet contracted with a client. From the information provided in the models, list up to six possible causes for this and explain how each might have led to this situation.

We assessed participants’ answers by creating a set of “acceptable” answers to each question (Mayer 1989) (see the online supplement: Burton-Jones and Meso 2006). As in recent studies (Bodart et al. 2001, Gemino and Wand 2003), questions required subjects to use information explicated in the model (e.g., attribute names) together with inferences from the model (e.g., potential implications of different attribute values) to answer questions. For example, acceptable answers to the above question included: “low quality in sample interview” and “clients cancel jobs before contract starts.”

Performance in the cloze test was measured by participants’ ability to complete a narrative of the domain that the model represented. Participants were assessed by the number of blanks they filled with a correct word/synonym (Gemino 1998, Gemino and Wand 2004). The following is an extract of this assessment (see the online supplement for full details: Burton-Jones and Meso 2006):

Applicants’ is recorded as when their applications are received. If their are they are moved to an state.

Consistent with the assumptions of our tests (see §4), the tasks were designed to be challenging. Students had 35 minutes to complete the problemsolving test (allowing 3.2 minutes per problem) and 25 minutes to complete the cloze test (requiring approximately 4.8 blanks per minute). Students were advised to do their best, but not to worry if they could not finish.<sup>3</sup>

<sup>3</sup> As Reviewer 1 noted, an inherent limitation of the problemsolving and cloze tests is that participants might be able to use their existing knowledge of the domain represented in the diagrams

To measure perceived ease of understanding, we adapted four items from the ease-of-use scale in prior studies (Moore and Benbasat 1991, Gemino 1998). For example, one item was “trying to understand the UML diagrams of ICI required a lot of mental effort.” We expected that the results of actual and perceived understanding would be consistent. That is, if subjects found the diagrams more difficult to understand (reflected in their performance on the tests of actual understanding), then subjects would perceive the diagrams to be harder to understand.

## 5.5. Procedures

Participants were first given five minutes to review a summary of UML syntax together with a prequestionnaire to gauge their UML experience and existing knowledge of the domain modeled in the diagrams. They then had 10 minutes to answer a set of comprehension questions about the diagrams. These questions were not a DV, but merely a way of engaging participants and helping them become familiar with the diagrams before the experimental tasks. Next, participants received either the cloze test or problem-solving test (test assignment was random). The instructions explained that all three diagrams would be useful. Those with the cloze test had 25 minutes to complete it; those with the problemsolving test had 35 minutes. After the allotted time, we collected the first test and provided the second test (whichever one the participant had not seen). After completing both tests, participants completed the ease-of-understanding scale. The entire experiment took approximately 1 hour, 15 minutes. Six Ph.D. students participated in a pretest, and their feedback was used to make minor changes to the materials and procedures.

Recent research has adopted two approaches to test diagram-based problem solving. In one approach, researchers take away the diagrams before the experimental tasks begin to force participants to work from memory (Gemino 1998, Bodart et al. 2001). In a second approach, participants work through the diagrams when problem solving (Kim et al. 2000). We adopted the second approach. As was true in past research using this method (Kim et al. 2000), our diagrams contained more elements than the first approach typically uses. Taking away the diagrams would have made it unlikely that participants could recall enough details to perform effectively. A weakness in the second approach is that participants might be able to answer some questions by simply copying information from the diagrams, without engaging in deep thinking. We addressed this by requiring participants to explain each answer in the problem-solving test and by requiring them to integrate material from multiple diagrams to complete the cloze test.

## 5.6. Replication

A replication was performed to validate the experiment (Berthon et al. 2002). Four threats were possible: (1) participants may not have been representative because they were from a single class of students, (2) the ease-of-understanding scale may have lacked validity because it was given on its own rather than the items being randomized among other items (Goodhue and Loiacono 2002), (3) our problemsolving and cloze results may have lacked validity because there was no full-scale pilot test, and (4) the operationalizations of each condition may have been biased by the particular way the violations were performed. A replication helped address these threats.

Sixty-six students (22 per group) participated in the replication. To allow variation in instruction and experience, we obtained participants from four classes. Most students came from OOA classes and had less UML experience than those in the first experiment. We also added items from another scale to our easeof-understanding scale and randomized the items. Finally, an independent expert reviewed the diagrams again, and we consequently changed the way we manipulated determinism and losslessness. For determinism, we removed the violation for external events, instead of having it for both internal and external events. For losslessness, we removed the prior manipulation and added an aggregation relationship because aggregation relationships are another way to manipulate losslessness. We did not add emergent attributes to the good diagrams, but we gave the subparts meaningful names so that analysts could infer the emergent nature of each subpart. By subsuming the attributes into the aggregate, the bad diagram lost this emergent information about each subpart.

## 5.7. Process Tracing

Despite the high internal validity of experiments, the experiment and replication cannot provide conclusive evidence to support the proposed cognitive process by which decomposition quality affects understanding.<sup>4</sup> A process-tracing study was used to collect this data (Todd and Benbasat 1987). Following Vessey and Conger (1994), six students participated. Three students received the good diagrams and three received the bad diagrams (based on random assignment). Such small samples are appropriate for process tracing because of the rich data collected (Ericsson and Simon 1993, Kim et al. 2000). Each student used the materials deployed in the experiment. Students completed a prequestionnaire regarding their domain knowledge and UML experience and their scores were comparable between groups.<sup>5</sup> Because of the need to verbalize answers, students were given an additional 10 minutes to perform each task (i.e., 45 minutes for the cloze test and 55 minutes for the problem-solving test). Audiovisual recordings were taken of each subject and data were subjected to a protocol analysis (Ericsson and Simon 1993). The procedure was pretested with four students to ensure that it was clear and that it allowed comparability with the experiment.

## 6. Results

The data analysis proceeded in two steps. We first examine the results of the experiment and replication. We then examine the results of the process-tracing study.

## 6.1. Results of the Experiment and Replication

We first examine the descriptive statistics and the reliability and validity of the instrumentation. We then examine the results for testing the study’s proposition.

Table 4 Descriptive Statistics

<table><tr><td colspan="6">Experiment</td></tr><tr><td></td><td>Mean</td><td>Std. dev.</td><td>Range</td><td>Skew</td><td>Kurt</td></tr><tr><td>UML</td><td>3.5</td><td>1.3</td><td>5</td><td>0.10</td><td>-0.72</td></tr><tr><td>DomK</td><td>3.4</td><td>1.4</td><td>6</td><td>0.24</td><td>-0.35</td></tr><tr><td> $Cloze^†$ </td><td>35.0</td><td>21.9</td><td>85</td><td>0.67</td><td>-0.37</td></tr><tr><td> $ProbS^†$ </td><td>8.4</td><td>5.9</td><td>28</td><td>1.48</td><td>2.80</td></tr><tr><td>PercU</td><td>4.2</td><td>0.6</td><td>2</td><td>0.49</td><td>-0.57</td></tr><tr><td colspan="6">N=57 (3 groups * 19 per cell)</td></tr><tr><td colspan="6">Replication</td></tr><tr><td>UML</td><td>2.6</td><td>1.4</td><td>5</td><td>0.99</td><td>0.06</td></tr><tr><td>DomK</td><td>2.6</td><td>1.3</td><td>5</td><td>0.50</td><td>-0.44</td></tr><tr><td> $Cloze^†$ </td><td>30.4</td><td>18.1</td><td>70</td><td>0.62</td><td>-0.53</td></tr><tr><td> $ProbS^†$ </td><td>6.3</td><td>3.5</td><td>18</td><td>0.96</td><td>1.50</td></tr><tr><td>PercU</td><td>3.3</td><td>1.1</td><td>5</td><td>0.05</td><td>-0.04</td></tr><tr><td colspan="6">N=66 (3 groups * 22 per cell)</td></tr></table>

Note. Variables: UML UML experience, DomK domain knowledge, Cloze fill-in-the-blanks test, ProbS problem-solving test, PercU perceived ease of understanding.  
<sup>†</sup>Maximum scores: 120 for cloze, 49 for problem solving (Experiment), 110 for cloze, 46 for problem solving (Replication).

6.1.1. Descriptive Statistics. Table 4 reports descriptive statistics for the experiment and replication. In terms of control variables, subjects’ UML experience and domain knowledge were not high, as expected. They were also lower in the replication than in the experiment. In terms of DVs, the replication subjects scored lower than the experiment subjects. Consistent with the challenging nature of the tests, the scores for the problem-solving and cloze tests were much lower than the maximum possible scores, as Table 4 shows. The skewness and kurtosis for the DVs indicated potential violations of normality. There are three groups and three DVs. Two of the nine distributions showed evidence of nonnormality. Such violations are not normally problematic when groups have equal sizes and more than 12 subjects in each group, as in our study (Kirk 1995). The distributions improved when we omitted outliers, but as they did not affect the results, we included outliers in the final tests. Table 5 shows the correlation matrix. The table shows significant correlations  <sub>=</sub> 005- in the expected direction for cloze and problem-solving tests but no significant differences across groups for perceived ease of understanding. Participants’ experience in UML appeared to improve their problem-solving performance in the experiment but hinder their performance in the cloze test in the replication. Participants’ domain knowledge had no apparent effect on any dependent variable. There appeared to be a learning effect on the cloze test because the order of tasks was significant. The problem-solving results did not suffer a learning effect.

Table 5 Correlation Matrix

<table><tr><td colspan="7">Experiment</td></tr><tr><td></td><td>Group</td><td>Order</td><td>UML</td><td>DomK</td><td>Cloze</td><td>ProbS</td></tr><tr><td>Order</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UML</td><td>0.30*</td><td>0.02</td><td></td><td></td><td></td><td></td></tr><tr><td>DomK</td><td>0.06</td><td>0.08</td><td>0.53**</td><td></td><td></td><td></td></tr><tr><td>Cloze</td><td>0.25*</td><td>0.35**</td><td>-0.13</td><td>-0.09</td><td></td><td></td></tr><tr><td>ProbS</td><td>0.54**</td><td>0.13</td><td>0.25*</td><td>0.02</td><td>0.50**</td><td></td></tr><tr><td>PercU</td><td>0.03</td><td>0.16</td><td>0.13</td><td>-0.07</td><td>0.02</td><td>0.04</td></tr></table>

∗Significant at 0.05; ∗∗significant at 0.01 1-tailed.

<table><tr><td></td><td colspan="6">Replication</td></tr><tr><td>Order</td><td>0.07</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UML</td><td>-0.04</td><td>-0.10</td><td></td><td></td><td></td><td></td></tr><tr><td>DomK</td><td>0.01</td><td>-0.11</td><td>0.58**</td><td></td><td></td><td></td></tr><tr><td>Cloze</td><td>0.30**</td><td>0.24*</td><td>-0.31**</td><td>-0.13</td><td></td><td></td></tr><tr><td>ProbS</td><td>0.34**</td><td>-0.10</td><td>-0.03</td><td>0.05</td><td>0.34**</td><td></td></tr><tr><td>PercU</td><td>-0.18</td><td>-0.18</td><td>0.27*</td><td>0.18</td><td>0.10</td><td>0.18</td></tr></table>

∗Significant at 0.05; ∗∗significant at 0.01 1-tailed.  
Note. Variables: Group: 1 Bad; 2 Moderate; 3 Good; Order: 1 fillin-the-blanks first, 2  fill-in-the-blanks second; UML  UML experience; DomK domain knowledge, Cloze fill-in-the-blanks test, ProbS problem-solving test; PercU <sub>=</sub> perceived ease of understanding.

Table 6 reports instrument validity and reliability. The data for the ease-of-understanding scale appeared to be valid and reliable because all items loaded highly on the desired construct and alpha values were higher than the minimum value of 0.6 (Nunnally 1967). For the problem-solving and cloze tests, prior research indicates that these are valid tests of understanding (Mayer 1989, Gemino and Wand 2004, Bodart et al. 2001). The validity and reliability of the data from these instruments were harder to verify, as traditional tests such as Cronbach’s alpha and factor analysis do not apply.<sup>6</sup> Thus, to test validity and reliability we used a combination of (a) inter-rater reliability, (b) MANOVA, and (c) comparisons of the results between the experiment and replication. For inter-rater reliability, an independent coder and one researcher coded the experiment’s problem-solving and cloze results; two independent coders coded the replication’s results. The coding scheme appeared reliable because the coders’ scores for the problemsolving results correlated highly $( r = 0 . 8 7 - 0 . 9 7$ in the experiment; $r = 0 . 7 5 - 0 . 9 5$ in the replication). The cloze test was much more objective r <sub>=</sub> 099-. Given the reliable coding, we used the independent coder’s scores for the experiment and the mean of the coders scores for the replication. A MANOVA supported the problem-solving test’s convergent validity. As shown later in Table 8, fewer results were significant in the replication than in the experiment, but the directions were consistent. Finally, in terms of criterion validity, the IV <sub>→</sub> DV effect sizes varied between experiment and replication but, as shown later in Tables 7 and 8, the consistency of the results supports criterion validity. We were, thus, satisfied with reliability and validity.

Table 6 Evidence for Instrument Validity and Reliability

<table><tr><td colspan="3">Experiment</td></tr><tr><td></td><td>Validity</td><td>Reliability</td></tr><tr><td>Cloze</td><td>Replication*</td><td>Interreliability $r = 0.99$ </td></tr><tr><td>ProbS</td><td>MANOVA replication*</td><td>Interreliability $r = 0.87 - 0.97$  per problem</td></tr><tr><td>PercU</td><td>Factor loadings0.78, 0.73, 0.77, 0.82</td><td>Cronbach&#x27;s alpha0.64</td></tr><tr><td colspan="3">Replication</td></tr><tr><td>Cloze</td><td>Experiment*</td><td>Interreliability $r = 0.99$ </td></tr><tr><td>ProbS</td><td>MANOVA experiment*</td><td>Interreliability $r = 0.75 - 0.95$  per problem</td></tr><tr><td>PercU</td><td>Factor loadings**0.58, 0.81, 0.79, 0.68</td><td>Cronbach&#x27;s alpha0.76</td></tr></table>

∗The entries “replication” and “experiment” indicate that the criterion valid ity of the cloze and problem-solving tests are supported because the results obtained from testing the study’s proposition in the Experiment are consistent with those in the Replication and vice versa (as shown later in Tables 7 and 8).  
∗∗In the Replication, items for PercU were randomized among other items. The loadings supported convergent and discriminant validity as the items fo PercU loaded highest on PercU and other items loaded least on PercU.

Table 7 Tests of Proposition—One-Way ANOVAs

<table><tr><td colspan="6">Experiment</td></tr><tr><td>Test</td><td>Dep. var.</td><td>df</td><td>Means (std. deviations)*</td><td>F</td><td>Sig.**</td></tr><tr><td rowspan="3">Good &gt; Bad</td><td>Cloze</td><td>1, 36</td><td> $41.8 (25.2)_{G} > 28.7 (14.7)_{B}$ </td><td>3.82</td><td>0.03</td></tr><tr><td>ProbSolv</td><td>1, 36</td><td> $12.8 (7.1)_{G} > 5.0 (3.2)_{B}$ </td><td>19.24</td><td>0.00</td></tr><tr><td>PercUnd</td><td>1, 35</td><td> $4.2 (0.7)_{G} > 4.1 (0.7)_{B}$ </td><td>0.45</td><td>0.42</td></tr><tr><td rowspan="3">Good &gt; Mod</td><td>Cloze</td><td>1, 36</td><td> $41.8 (25.2)_{G} > 34.5 (23.5)_{M}$ </td><td>0.86</td><td>0.18</td></tr><tr><td>ProbSolv</td><td>1, 36</td><td> $12.8 (7.1)_{G} > 7.3 (3.9)_{M}$ </td><td>8.75</td><td>0.00</td></tr><tr><td>PercUnd</td><td>1, 35</td><td> $4.2 (0.5)_{G} = 4.2 (0.7)_{M}$ </td><td>0.44</td><td>0.42</td></tr><tr><td rowspan="3">Mod &gt; Bad</td><td>Cloze</td><td>1, 36</td><td> $34.5 (23.5)_{M} > 28.7 (14.7)_{B}$ </td><td>0.82</td><td>0.19</td></tr><tr><td>ProbSolv</td><td>1, 36</td><td> $7.3 (3.9)_{M} > 5.0 (3.2)_{B}$ </td><td>4.14</td><td>0.03</td></tr><tr><td>PercUnd</td><td>1, 36</td><td> $4.2 (0.7)_{M} > 4.1 (0.7)_{B}$ </td><td>0.23</td><td>0.32</td></tr></table>

<table><tr><td>Prop.</td><td>Dep. var.</td><td>df</td><td>Means (std. deviations)*</td><td>F</td><td>Sig.**</td></tr><tr><td rowspan="3">Good &gt; Bad</td><td>Cloze</td><td>1, 42</td><td> $38.5 (22.5)_{G} > 25.4 (14.0)_{B}$ </td><td>5.39</td><td>0.01</td></tr><tr><td>ProbSolv</td><td>1, 42</td><td> $7.8 (3.7)_{G} > 4.9 (2.3)_{B}$ </td><td>9.79</td><td>0.00</td></tr><tr><td>PercUnd</td><td>1, 41</td><td> $3.1 (1.1)_{G} < 3.6 (1.0)_{B}$ </td><td>0.45</td><td>0.07</td></tr><tr><td rowspan="3">Good &gt; Mod</td><td>Cloze</td><td>1, 42</td><td> $38.5 (22.5)_{G} > 27.4 (14.2)_{M}$ </td><td>3.81</td><td>0.03</td></tr><tr><td>ProbSolv</td><td>1, 42</td><td> $7.8 (3.7)_{G} > 6.1 (3.9)_{M}$ </td><td>2.23</td><td>0.07</td></tr><tr><td>PercUnd</td><td>1, 42</td><td> $3.1 (1.1)_{G} < 3.4 (1.2)_{M}$ </td><td>0.87</td><td>0.18</td></tr><tr><td rowspan="3">Mod &gt; Bad</td><td>Cloze</td><td>1, 42</td><td> $27.4 (14.2)_{M} > 25.4 (14.0)_{B}$ </td><td>0.23</td><td>0.32</td></tr><tr><td>ProbSolv</td><td>1, 42</td><td> $6.1 (3.9)_{M} > 4.9 (2.3)_{B}$ </td><td>4.14</td><td>0.11</td></tr><tr><td>PercUnd</td><td>1, 41</td><td> $3.4 (1.2)_{M} < 3.6 (1.0)_{B}$ </td><td>0.23</td><td>0.31</td></tr></table>

Note. We conducted ANCOVAs and regressions to test the effect of domain knowledge, UML experience, and order of tasks. None of these control variables affected the results. We do not show these results due to space constraints.  
Key. ∗Subscripts G, M, and B refer to good, medium, and bad diagrams. ∗∗Bold cells indicate a significant difference at p < 005 (one-tailed).

6.1.2. Results of Testing the Proposition. Tables 7 and 8 report tests of the study’s proposition that UML analysis diagrams that manifest better decompositions will increase analysts’ understanding of a domain. Tables 7 and 8 report the results for this test across the three treatments: good, moderate, and bad.

The results support the study’s proposition for actual but not perceived understanding. The cloze and problem-solving results are stronger for the good bad comparison than for the good moderate and moderate <sub>→</sub> bad comparisons, as expected (Table 7). The problem-solving test appeared to be more sensitive than the cloze test in the experiment, but not in the replication (Tables 7 and 8). The ease-ofunderstanding results show no difference across groups in any test, although they approach significance in the opposite direction in the replication (p <sub>=</sub> 007, Table 7).

To provide further confidence in the results, we tested the consistency of the problem-solving results across each question (see Table 8). The results are consistent because the score for each question in the experiment and for 9 of 10 questions in the replication were in the hypothesized direction. The results for the replication were weaker, with only 3 of 10 questions significant compared to 8 of 11 in the experiment. These weaker results were reflected in the replication’s MANOVA, which was significant when comparing the good and bad groups, but not when including the entire sample $( p = 0 . 1 3$ in the good, bad, moderate (G, B, M) section of Table 8). However, although the replication’s results were weaker, they were consistent with those of the experiment and the effect sizes were medium to large (e.g., eta squared values of 0.18 and 0.38) (Cohen 1988).

Because the result for the perceived ease-ofunderstanding scale was not significant, we performed a post hoc power test for the experiment and replication. The test indicated that the post hoc power of the experiment was 0.45 while that for the replication was 0.5. If we assume a moderate effect size, these results suggest that we would have needed 210 subjects in both the experiment and replication to have a high probability of rejecting the null hypothesis (with an alpha of 0.05). Thus, while the lack of a significant effect for the perceived ease-ofunderstanding scale in our study is consistent with results in many past studies (Batra et al. 1990, Gemino 1998, Gemino and Wand 2004), we cannot be certain whether the result simply reflects Type 2 error due to the small sample sizes in our study or whether it reflects another factor (e.g., a true lack of consistency between measures of actual and perceived understanding). We return to this issue in the discussion (§7).

## 6.2. Protocol Analysis Results

The aim of the protocol analysis was to examine the process by which GDM violations affect understanding. Two independent coders (Ph.D. students with UML expertise) examined the process. As coding was somewhat subjective, the coders conducted practice coding until they gave reliable scores. The final interrater reliability was adequate (ranging from 66%–86%, see the online supplement: Burton-Jones and Meso 2006).

Table 8 Sensitivity Test—MANOVA of Problem Solving Results

<table><tr><td colspan="17">Overall MANOVA for problem-solving results</td></tr><tr><td colspan="9">Experiment</td><td colspan="8">Replication</td></tr><tr><td>Groups*</td><td colspan="4">F (Pillai&#x27;s trace)</td><td colspan="2">Sig.**</td><td>Eta sq.</td><td>Groups*</td><td colspan="4">F (Pillai&#x27;s trace)</td><td colspan="2">Sig.**</td><td colspan="2">Eta sq.</td></tr><tr><td>G, B</td><td></td><td colspan="3">2.39</td><td colspan="2">0.02</td><td>0.50</td><td>G, B</td><td></td><td colspan="3">2.03</td><td colspan="2">0.03</td><td colspan="2">0.38</td></tr><tr><td>G, B, M</td><td></td><td colspan="3">2.02</td><td colspan="2">0.01</td><td>0.33</td><td>G, B, M</td><td></td><td colspan="3">1.21</td><td colspan="2">0.13</td><td colspan="2">0.18</td></tr><tr><td colspan="17">Per problem results</td></tr><tr><td rowspan="3">Prob.</td><td colspan="6">Means (M) and std. dev. (SD)</td><td rowspan="3">Dir.***G &gt; B</td><td rowspan="3">Sig.**G, M, B</td><td rowspan="3">Prob.</td><td colspan="5">Means (M) and std. dev. (SD)</td><td rowspan="2">Dir.***G &gt; B</td><td rowspan="3">Sig.**G, M, B</td></tr><tr><td colspan="2">G</td><td colspan="2">M</td><td colspan="2">B</td><td colspan="2">G</td><td colspan="2">M</td><td>B</td></tr><tr><td>M</td><td>SD</td><td>M</td><td>SD</td><td>M</td><td>SD</td><td>M</td><td>SD</td><td>M</td><td>SD</td><td>M</td><td>SD</td></tr><tr><td>1</td><td>2.6</td><td>1.9</td><td>1.4</td><td>1.2</td><td>1.3</td><td>1.2</td><td>✓</td><td>0.01</td><td>1</td><td>1.7</td><td>1.3</td><td>1.3</td><td>1.2</td><td>1.3</td><td>1.0</td><td>✓</td></tr><tr><td>2</td><td>0.6</td><td>0.7</td><td>0.5</td><td>0.6</td><td>0.3</td><td>0.4</td><td>✓</td><td>0.07</td><td>2</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.8</td><td>0.4</td><td>0.4</td><td>✓</td></tr><tr><td>3</td><td>0.6</td><td>0.4</td><td>0.5</td><td>0.5</td><td>0.4</td><td>0.5</td><td>✓</td><td>0.11</td><td>3</td><td>1.0</td><td>0.7</td><td>0.6</td><td>0.8</td><td>0.6</td><td>0.5</td><td>✓</td></tr><tr><td>4</td><td>1.8</td><td>1.7</td><td>1.2</td><td>1.0</td><td>1.0</td><td>1.1</td><td>✓</td><td>0.07</td><td>4</td><td>1.0</td><td>0.9</td><td>1.1</td><td>0.9</td><td>1.0</td><td>0.8</td><td></td></tr><tr><td>5</td><td>1.9</td><td>1.8</td><td>1.2</td><td>1.0</td><td>0.7</td><td>0.7</td><td>✓</td><td>0.02</td><td>5</td><td>0.6</td><td>0.7</td><td>0.4</td><td>0.6</td><td>0.4</td><td>0.7</td><td>✓</td></tr><tr><td>6</td><td>0.9</td><td>0.9</td><td>0.7</td><td>0.9</td><td>0.1</td><td>0.3</td><td>✓</td><td>0.01</td><td>6</td><td>0.5</td><td>0.7</td><td>0.6</td><td>0.6</td><td>0.3</td><td>0.5</td><td>✓</td></tr><tr><td>7</td><td>0.9</td><td>1.0</td><td>0.2</td><td>0.4</td><td>0.3</td><td>0.6</td><td>✓</td><td>0.00</td><td>7</td><td>0.7</td><td>1.0</td><td>0.4</td><td>0.5</td><td>0.4</td><td>0.4</td><td>✓</td></tr><tr><td>8</td><td>1.5</td><td>1.7</td><td>0.5</td><td>0.6</td><td>0.4</td><td>0.6</td><td>✓</td><td>0.00</td><td>8</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.9</td><td>0.3</td><td>0.5</td><td>✓</td></tr><tr><td>9</td><td>0.6</td><td>0.9</td><td>0.2</td><td>0.6</td><td>0.1</td><td>0.3</td><td>✓</td><td>0.05</td><td>9</td><td>0.7</td><td>0.7</td><td>0.4</td><td>0.5</td><td>0.2</td><td>0.4</td><td>✓</td></tr><tr><td>10</td><td>0.9</td><td>0.9</td><td>0.6</td><td>0.6</td><td>0.2</td><td>0.3</td><td>✓</td><td>0.00</td><td>10</td><td>0.6</td><td>0.8</td><td>0.3</td><td>0.5</td><td>0.1</td><td>0.2</td><td>✓</td></tr><tr><td>11</td><td>0.5</td><td>0.9</td><td>0.5</td><td>0.7</td><td>0.1</td><td>0.3</td><td>✓</td><td>0.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Key. ∗Groups: G good, M moderate, and B bad diagram.  
∗∗Significance: Italic cells indicate a significant difference at p < 005 (one-tailed). Bold cells indicate a significant difference under the conservative Bonferroni test in which the alpha (0.05) is divided by the number of tests (11 in the experiment; 10 in the replication) to control for an inflated risk of Type 1 error.  
∗∗Direction: <sup></sup> is shown if the mean for G > mean for B.

The coders examined two aspects of the process. First, they examined the cognitive difficulties or “breakdowns” that subjects experienced when working on the problem-solving and cloze tests (Vessey and Conger 1994). In §4, we described a multistage process by which decomposition quality affects understanding, i.e., better decomposition enables individuals to construct a better mental representation of the domain shown in the diagram, which enables them to construct a more effectively structured problem space, which enables them to solve problems more effectively (Pretz et al. 2003). On this basis, we define a cognitive breakdown in this study as a failure suffered by a person when searching his/her problem space (Newell and Simon 1972).

Cognitive breakdowns are likely in difficult tasks. When breakdowns occur, subjects may either cycle back to an earlier stage of the problem-solving process to overcome the breakdowns, or if they cannot overcome them, give up on the problem (Newell and

Simon 1972, Pretz et al. 2003). This suggests that the benefit of having a good decomposition should be evident in either (1) the total number of breakdowns a subject suffers and/or (2) the number of breakdowns that s/he overcomes.

The results in Table 9 show that subjects in both groups suffered a similar number of breakdowns. However, subjects who received the “bad” diagrams were less able, on average, to overcome the breakdowns they suffered. While this finding only applies to the average of the subjects’ results (e.g., Subject 6 overcame most of his breakdowns), it is consistent with and complements the experimental results. It also suggests a more precise link between decomposition quality and understanding. That is, it suggests that conceptual models that manifest good decompositions enable subjects to construct a more effectively structured problem space, which improves their ability to reason about the domain, which improves their ability to overcome cognitive breakdowns, which finally enables them to obtain better scores in tests of understanding.

Table 9 Protocol Analysis: Analysis of Cognitive Breakdowns

<table><tr><td rowspan="2">Group</td><td rowspan="2">Subject</td><td colspan="3">Breakdowns: Problem solving</td><td colspan="3">Breakdowns: Cloze (fill-in-the-blanks)</td></tr><tr><td># breakdowns</td><td># breakdowns overcome</td><td># breakdowns not overcome</td><td># breakdowns</td><td># breakdowns overcome</td><td># breakdowns not overcome</td></tr><tr><td rowspan="5">Good</td><td>1*</td><td>6.0</td><td>5.5</td><td>0.5</td><td>10.0</td><td>8.5</td><td>1.5</td></tr><tr><td>2</td><td>6.0</td><td>6.0</td><td>0.0</td><td>8.0</td><td>7.0</td><td>1.0</td></tr><tr><td>3</td><td>10.0</td><td>8.0</td><td>2.0</td><td>22.0</td><td>20.0</td><td>2.0</td></tr><tr><td>Mean</td><td>7.33</td><td>6.50</td><td>0.83</td><td>13.33</td><td>11.83</td><td>1.50</td></tr><tr><td></td><td colspan="3">Avg. proportion of breakdowns overcome: 89%</td><td colspan="3">Avg. proportion of breakdowns overcome: 89%</td></tr><tr><td rowspan="5">Bad</td><td>4*</td><td>6.5</td><td>2.0</td><td>4.5</td><td>11.0</td><td>7.0</td><td>4.0</td></tr><tr><td>5</td><td>5.0</td><td>1.0</td><td>4.0</td><td>13.0</td><td>3.0</td><td>10.0</td></tr><tr><td>6</td><td>10.0</td><td>10.0</td><td>0.0</td><td>19.0</td><td>17.0</td><td>2.0</td></tr><tr><td>Mean</td><td>7.17</td><td>4.33</td><td>2.83</td><td>14.33</td><td>9.00</td><td>5.33</td></tr><tr><td></td><td colspan="3">Avg. proportion of breakdowns overcome: 61%</td><td colspan="3">Avg. proportion of breakdowns overcome: 63%</td></tr></table>

∗The scores for these rows contain decimal values (e.g., 5.5) because they are the averages of the coders’ scores.

The second aspect of the process that we examined was to verify that the differences in results were indeed caused by GDM violations rather than other factors. To perform this test, protocol data were coded to reflect the sources of knowledge from which subjects derived answers. Participants could use multiple sources of knowledge when answering questions: information in the diagram, inferences from the diagram, information in the narrative of the question, prior questions answered, guess work, and common knowledge (where the answer was apparently obvious to the subject thus not requiring a search among other knowledge sources). For each question in the problemsolving task and for each blank in the cloze test, coders examined each segment of participants’ verbal protocol and scored the sources of knowledge that the participants utilized.

Table 10 gives the results for knowledge sources. The results indicate that participants primarily sourced knowledge from the diagrams, whether information in the diagrams or inferred from the diagrams. This was expected and is consistent with the Khatri et al. (2006) description of the type of tasks in our study as “inferential” problem-solving tasks. For the cloze test, participants appeared to supplement knowledge from the diagrams with knowledge from the narrative. This is not a threat to the study because the narrative was the same for both groups. Overall, the results in Table 10 suggest that participants did not rely significantly on other sources of knowledge (such as common sense knowledge unrelated to the diagram or guess work) when answering questions.

Table 10 Protocol Analysis: Summary of Knowledge Sources

<table><tr><td rowspan="2">Group</td><td rowspan="2">Subject</td><td colspan="6">Knowledge sources: Problem-solving task</td><td colspan="6">Knowledge sources: Cloze task</td></tr><tr><td>D (%)</td><td>I (%)</td><td>N (%)</td><td>Q (%)</td><td>C (%)</td><td>G (%)</td><td>D (%)</td><td>I (%)</td><td>N (%)</td><td>Q (%)</td><td>C (%)</td><td>G (%)</td></tr><tr><td rowspan="4">Good</td><td>1</td><td>90</td><td>81</td><td>19</td><td>14</td><td>24</td><td>24</td><td>78</td><td>57</td><td>44</td><td>0</td><td>9</td><td>28</td></tr><tr><td>2</td><td>100</td><td>100</td><td>0</td><td>18</td><td>0</td><td>9</td><td>97</td><td>86</td><td>66</td><td>0</td><td>0</td><td>3</td></tr><tr><td>3</td><td>73</td><td>82</td><td>0</td><td>9</td><td>9</td><td>27</td><td>76</td><td>69</td><td>76</td><td>0</td><td>17</td><td>48</td></tr><tr><td>Mean</td><td>88</td><td>88</td><td>6</td><td>14</td><td>11</td><td>20</td><td>83</td><td>71</td><td>62</td><td>0</td><td>9</td><td>27</td></tr><tr><td rowspan="4">Bad</td><td>4</td><td>100</td><td>86</td><td>0</td><td>0</td><td>14</td><td>0</td><td>74</td><td>54</td><td>44</td><td>0</td><td>11</td><td>27</td></tr><tr><td>5</td><td>100</td><td>91</td><td>0</td><td>0</td><td>18</td><td>27</td><td>95</td><td>65</td><td>51</td><td>0</td><td>8</td><td>27</td></tr><tr><td>6</td><td>100</td><td>100</td><td>0</td><td>0</td><td>50</td><td>30</td><td>82</td><td>85</td><td>35</td><td>0</td><td>9</td><td>29</td></tr><tr><td>Mean</td><td>100</td><td>92</td><td>0</td><td>0</td><td>27</td><td>19</td><td>84</td><td>68</td><td>44</td><td>0</td><td>9</td><td>28</td></tr><tr><td>Mean</td><td></td><td>94</td><td>90</td><td>3</td><td>7</td><td>19</td><td>20</td><td>84</td><td>69</td><td>53</td><td>0</td><td>9</td><td>27</td></tr></table>

Key. Knowledge sources: D directly from the diagrams; I inferences from the diagrams; N narrative of the question or cloze test; Q answers to other questions; C common sense, G guess work.  
%: The % values indicate the number of questions/blanks (out of the total number of questions/blanks that a subject answered) in which s/he used information from a particular knowledge source. For example, the top-left cell indicates that in 90% of the problem-solving questions, Subject 1 used information explicitly shown in the diagrams.

As a final manipulation check, the coders examined the audiovisual records of subjects who received the bad diagrams to identify the aspects of the diagrams that subjects were examining at the precise point when they suffered a breakdown. Because each question in the problem-solving task and “blank” in the cloze test was designed to test the effects of one or more GDM violations, and because the violations were located in different parts of the diagrams, we could explore whether the violations that we implemented in the diagrams led to the breakdowns that we expected subjects to suffer. Table 11 summarizes the results. The table indicates the proportion of times that a violation was expected to lead to a breakdown where it did in fact lead to a breakdown. The results demonstrate that the experiment’s manipulations were coarse rather than precise, i.e., on average, the violations manipulated in the diagrams only affected subjects 50% of the time that we expected the violations to affect them. Despite the coarse manipulations, Table 11 shows that the results were not driven by a mere subset of violations; all five types of violations in the bad UML models appeared to have an effect. Together with Table 10, the results in Table 11 provide a useful manipulation check to support the causal link between GDM criteria and understanding.

## 6.3. Summary of Results

Table 12 summarizes the results. Although there were differences in the results between the experiment and replication, the overall pattern of results was consistent: the proposition received support for both measures of actual understanding, but not for measures of perceived ease of understanding. We discuss the implications of these results next.

## 7. Discussion and Concluding Comments

We discuss four issues in turn: this study’s limitations, its contributions to research, its contributions to practice, and opportunities for future research. This study’s limitations can be understood with reference to traditional criteria for validity. Internal validity was relatively strong due to our use of randomized experiments and our collection of data regarding the process by which decomposition quality affects understanding. Nonetheless, the external validity of our study is limited because participants were less experienced and likely less motivated than practicing analysts and had relatively homogenous levels of domain and modeling knowledge. In terms of construct validity, we violated each GDM criterion in limited ways, used a limited number of tests of understanding, and examined just three UML diagrams. Finally, in terms of statistical conclusion validity, our samples were small, so the lack of results for the ease-ofunderstanding scale may represent a Type 2 error. Moreover, as noted earlier (§5.4), the problem-solving and cloze tests may inherently lack power, so the results for these tests may understate the benefit of good decompositions on understanding.

Despite these weaknesses, this study makes several contributions. It contributes to research in two ways. First, although the importance of decomposition has long been known in IS, there is no agreement on the relevant criteria for determining whether a decomposition is good, or even the meaning of “decomposition” (Parnas 1972). Various decomposition criteria have been advanced (such as criteria for “functional” decomposition), but many are poorly defined, not explicated, and not supported by theory (Briand et al. 1999). Thus, analysts have to rely on tacit knowledge and experience to recognize and construct good decompositions (Lieberman 2003). Simon (1996) argues that researchers should search for general theories of decomposition. To our knowledge, GDM is the only general theory of decompositions in IS. Our study reveals GDM’s potential value and the importance of extending it and developing alternative/competing theories.

Table 11 Proportion of Times that a Violation Led to a Problem-Solving Breakdown

<table><tr><td rowspan="2">Treatment</td><td rowspan="2">Subject</td><td colspan="5">Proportion of times that a violation was expected to lead to a breakdown where it did, in fact, lead to a breakdown</td></tr><tr><td>Coupling (%)</td><td>Cohesion (%)</td><td>Losslessness (%)</td><td>Determinism (%)</td><td>Minimality (%)</td></tr><tr><td>Bad</td><td>S4</td><td>33.3</td><td>27.8</td><td>30.0</td><td>38.9</td><td>37.5</td></tr><tr><td>Bad</td><td>S5</td><td>50.0</td><td>33.3</td><td>60.0</td><td>44.4</td><td>50.0</td></tr><tr><td>Bad</td><td>S6</td><td>83.3</td><td>62.50</td><td>60.0</td><td>33.3</td><td>87.5</td></tr><tr><td></td><td>Averages</td><td>55.5</td><td>41.2</td><td>50</td><td>38.9</td><td>58.3</td></tr><tr><td colspan="7">Overall average: 48.8%</td></tr></table>

Table 12 Summary of Results

<table><tr><td>Dependent variable</td><td>Good &gt; Bad</td><td>Good &gt; Moderate</td><td>Moderate &gt; Bad</td><td>Proposition supported?</td></tr><tr><td rowspan="2">Problem solving (Hypothesis 1)</td><td>Yes (experiment)</td><td>Yes (experiment)</td><td>Yes (experiment)</td><td>Yes</td></tr><tr><td>Yes (replication)</td><td>No (replication)</td><td>No (replication)</td><td></td></tr><tr><td rowspan="2">Cloze (fill-in-the-blanks) (Hypothesis 2)</td><td>Yes (experiment)</td><td>No (experiment)</td><td>No (replication)</td><td>Yes</td></tr><tr><td>Yes (replication)</td><td>Yes (replication)</td><td>No (replication)</td><td></td></tr><tr><td rowspan="2">Ease of understanding (Hypothesis 3)</td><td>No (experiment)</td><td>No (experiment)</td><td>No (experiment)</td><td>No</td></tr><tr><td>No (replication)</td><td>No (replication)</td><td>No (replication)</td><td></td></tr></table>

The second main contribution is that our study “brings up” decomposition issues from systems design to systems analysis. Prior to this study, GDM had only been operationalized in systems design (Paulson and Wand 1992, Chidamber and Kemerer 1994) and programming (Weber 2001). Like Yourdon (1989) and Bansiya and Davis (2002), we believe in the value of “bringing up” issues from design to analysis to help analysts comprehend the system and identify errors before they are carried through to later phases of design and coding where they are much more costly to fix (Yourdon 1989). In addition to being the first application of GDM to systems analysis, our study was also the first full test of GDM. Even though the value of decompositions may appear to be self-evident, little empirical research has been conducted to verify whether the expected benefits of good decompositions are actually realized. Our study contributes to research by providing a first step in this direction in OO systems analysis.

For practitioners, GDM provides a parsimonious and widely applicable set of criteria. Because UML has such a massive collection of techniques (Wieringa

1998, Kobryn 1999), a parsimonious metric can help practitioners focus on how each technique adds or detracts from an overall system decomposition. The study’s results appear resilient enough for practitioners to consider adopting GDM as an OOA quality metric. The conditions could be used to train analysts and students to develop good decompositions and help them to recognize and overcome GDM violations when conducting the identification and mapping phases of conceptual modeling.

In addition to these contributions, this study reveals many research opportunities. Perhaps the most obvious way to extend the research would be to address the study’s limitations. For example, more research is needed to test the full range of ways that GDM violations can occur because we only tested very simple, direct operationalizations. More research is also needed to create alternative ways of measuring understanding and to determine if the theory is robust to changes in experimental conditions, e.g., if the experiment uses participants with more expertise and/or gives them more time to answer questions (per §4). It would also be valuable to conduct a much more detailed protocol analysis. While the results of our protocol analysis confirmed and complemented our experimental results, the sample size was very small, so the results can only be considered indicative, not definitive. Finally, researchers need to test the effects of different patterns of GDM manipulations. For example, our diagrams included several different violations spread across a set of diagrams. An earlier study of program understanding found weak effects when testing each violation on its own (Weber 2001). Although the difference in results between the earlier study and our study could be due to different tasks or procedures, it may also be due to stronger effects when violations interact.

Another way to extend the study would be to investigate why we obtained certain results. For example, one might investigate why we found no effect for perceived ease of understanding. In addition to the risk of a Type 2 error, there appears to be several possibilities. One possibility is that the no-effect result is “true” and that actual understanding is a more sensitive diagnostic than perceived understanding. A second alternative, however, is that our instrument tapped into the wrong construct, e.g., it may need to make a firmer distinction between semantic and syntactic understanding or between a person’s initial difficulties when interpreting a model and a person’s subsequent ability to overcome his/her difficulties with the model. Finally, it might simply be an experimental design problem: a within-groups test may allow subjects to determine the diagrams’ relative quality more easily. Studying these different possibilities would be very valuable because if there is no strong relationship between conceptual modeling principles and users’ perceptions, this does not augur well for the adoption of these principles in practice (Moore and Benbasat 1991).

Another worthy question for research is how complexity affects the benefit of good decomposition. Decompositions are used to simplify complex structures (Simon 1996), but our diagrams were small, so our results might understate the benefit of good decompositions. We tried to simulate complexity by using inexperienced subjects and tight time constraints, but the difficult task led many participants to perform poorly and if time limits were tighter and subjects less experienced, there might not have been enough variation to identify any effect. Future empirical tests in this area may need to move away from traditional conceptual modeling experiments that test “toy” diagrams toward longitudinal experiments and larger, more realistic diagrams (Moody 2002).

A fourth opportunity would be to redesign the study for a practitioner environment. We know that practitioners do not use conceptual models in the manner prescribed by academics (Dawson and Swatman 1999), but we do not know precisely what decomposition principles they use or what benefit they have. A Delphi approach could be used to determine whether expert analysts implicitly use GDM criteria or, instead, alternative criteria. A related study would be to examine systems analysis and design methodologies in practice and determine whether there is a correlation between the degree to which these methodologies address GDM criteria (or alternative decomposition criteria) and the degree to which these methodologies are successful in practice.<sup>7</sup>

A fifth research direction would be to apply GDM to OO design. Chidamber and Kemerer (1994) applied GDM to OO design, but they only operationalized two of GDM’s five criteria. Given that our results support the usefulness of all five criteria, a logical next step would be to investigate whether all five criteria can apply to systems design. The ultimate aim would be to construct a consistent and integrated metrics suite from analysis through to design.

A final valuable direction would be to extend this study to incorporate design science (Hevner et al. 2004). Our study was an empirical evaluation only. Paulson and Wand’s (1992) test of GDM included the development of a tool to create good decompositions. Although some design science researchers have developed systems to create good data models (Storey et al. 1997, Antony and Batra 2002), the same has not been done for designing good conceptual models, for example, in UML. This offers a great opportunity for researchers and practitioners alike.

## Acknowledgments

This paper has benefited from presentations at the University of British Columbia and the University of Georgia. The authors are indebted to Andrew Gemino, Dale Goodhue, Kannan Mohan, Bala Ramesh, Veda Storey, Yair Wand, and Ron Weber for helpful comments, and Jeff Hubona and Carl Stucke for access to student subjects. An earlier version of this manuscript was awarded the Best Research Paper at the Twenty-Third International Conference on Information Systems. The authors thank Senior Editor Rob Austin and the anonymous associate editor and reviewers at ICIS for very helpful comments. They also thank Senior Editor Sal March and the AE and reviewers for Information Systems Research for exemplary reviews that greatly enhanced the quality of the paper. All errors or omissions are the authors’.

## References

Agarwal, R., A. P. Sinha, M. Tanniru. 1996. Cognitive fit in requirements modeling: A study of object and process methodologies. J. Management Inform. Systems 13(2) 137–164.

<sup>7</sup> We thank Reviewer 2 for helping us to identify this research opportunity.

Aho, A. V., C. Beeri, J. D. Ullman. 1979. The theory of joins in relational databases. ACM Trans. Data Base Systems 4(3) 297–314.

Antony, S. R., D. Batra. 2002. CODASYS: A consulting tool for novice database designers. Data Base Advances Inform. Systems 33(3) 54–68.

Ashcraft, M. H. 2002. Cognition. Prentice Hall, Upper Saddle River, NJ.

Bandi, R. K., V. K. Vaishnavi, D. E. Turk. 2003. Using objectoriented design complexity metrics to predict maintenance performance. IEEE Trans. Software Engrg. 29(1) 77–87.

Bansiya, J., C. G. Davis. 2002. A hierarchical model for objectoriented design quality assessment. IEEE Trans. Software Engrg. 28(1) 4–17.

Batra, D., J. A. Hoffer, R. P. Bostrom. 1990. Comparing representations with relational and EER models. Comm. ACM 33(2) 126–140.

Berthon, P., L. Pitt, M. Ewing, C. L. Carr. 2002. Potential research space in MIS: A framework for envisioning and evaluating research replication, extension, and generation. Inform. Systems Res. 13(4) 416–427.

Bodart, F., M. Sim, A. Patel, R. Weber. 2001. Should optional properties be used in conceptual modelling? A theory and three empirical tests. Inform. Systems Res. 12(4) 385–405.

Briand, L. C., J. W. Daly, J. K. Wüst. 1999. A unified framework for coupling measurement in object-oriented systems. IEEE Trans. Software Engrg. 25(1) 91–121.

Bunge, M. 1977. Treatise on Basic Philosophy: Vol. 3: Ontology I: The Furniture of the World. Reidel, Boston, MA.

Bunge, M. 1979. Treatise on Basic Philosophy: Vol. 4: Ontology II: A World of Systems. Reidel, Boston, MA.

Burton-Jones, A., P. Meso. 2006. Online supplement to “Conceptualizing Sytems for Understanding: An Empirical Test of Decomposition Principles in Object-Oriented Analysis.” Inform. Systems Res. 17(1). http://www.informs.org/Pubs/ Supplements/ISR/1526-5536-2006-17-01-0038-app.pdf.

Burton-Jones, A., R. Weber. 1999. Understanding relationships with attributes in entity-relationship diagrams. Proc. 20th Internat. Conf. Inform. Systems, Charlotte, NC, 214–228.

Chen, P. P. S. 1976. The entity-relationship model: Toward a unified view of data. ACM Trans. Database Systems 1(1) 9–36.

Chidamber, S. R., C. F. Kemerer. 1994. A metrics suite for objectoriented design. IEEE Trans. Software Engrg. 20(6) 476–493.

Coad, P., E. Yourdon. 1991. Object Oriented Analysis. Yourdon Press, Englewood Cliffs, NJ.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences, 2nd ed. Lawrence Erlbaum, Hillsdale, NJ.

Collins, A. M., M. R. Quillan. 1969. Retrieval time from semantic memory. J. Verbal Learn. Behavior 8 240–247.

Conger, S. 1994. The New Software Engineering. Wadsworth Publishing Company, Belmont, CA.

Davies, I., P. Green, M. Rosemann, M. Indulska, S. Gallo. 2006. How do practitioners use conceptual modeling in practice? Data & Knowledge Engrg. In press.

Davis, G. B. 1992. Systems analysis and design: A research strategy and macro-analysis. W. W. Cotterman, J. A. Senn, eds. Challenges and Strategies for Research in Systems Development. John Wiley & Sons, Chichester, England, 9–21.

Dawson, L., P. Swatman. 1999. The use of object-oriented models in requirements engineering: A field study. Proc. 20th Internat. Conf. Inform. Systems, Charlotte, NC, 260–273.

Dobing, B., J. Parsons. 2005. UML in practice: A survey of UML use. Comm. ACM. Forthcoming.

Dromney, R. G. 1996. Cornering the chimera. IEEE Software 13(1) 33–43.

El-Emam, K. 2002. Object-oriented metrics: A review of theory and practice. Advances in Software Engineering. Springer-Verlag, New York, 23–50.

Ericsson, K. A., H. A. Simon. 1993. Protocol Analysis: Verbal Reports as Data. MIT Press, Cambridge, MA.

Gemino, A. 1998. To be or may to be: An empirical comparison of mandatory and optional properties in conceptual modeling. Proc. Annual Conf. Admin. Sci. Assoc. of Canada, Saskatoon, Canada, 33–44.

Gemino, A. 2004. Empirical comparisons of animation and narration in requirements validation. Requirements Engrg. 9(3) 153–168.

Gemino, A., Y. Wand. 2003. Evaluating modeling techniques based on models of learning. Comm. ACM 46(10) 79–84.

Gemino, A., Y. Wand. 2004. A framework for empirical evaluation of conceptual modeling techniques. Requirements Engrg. 9(4) 248–260.

Goguen, J., F. J. Varela. 1979. Systems and distinctions: Duality and complementarity. Internat. J. General Systems 5(1) 31–43.

Goodhue, D., E. Loiacono. 2002. Randomizing question order versus grouping questions by construct in survey research: An empirical test of the impact on apparent reliabilities and LISREL determined path coefficients. Proc. Hawaii Internat. Conf. Inform. Systems HICSS-, Hawaii.

Harel, D. 1987. Statecharts: A visual formalism for complex systems. Sci. Comput. Programming 8 231–274.

Hevner, A., S. March, J. Park, S. Ram. 2004. Design science in information systems research. MIS Quart. 28(1) 75–105.

Johnson, R. A. 2002. Object-oriented systems development: A review of empirical research. Comm. AIS 8 65–81.

Khatri, V., V. Ramesh, I. Vessey, P. Clay, S.-J. Park. 2006. Understanding conceptual schemas: Exploring the role of application and IS domain knowledge. Inform. Systems Res. 17(1) 81–99.

Kim, J., J. Hahn, H. Hahn. 2000. How do we understand a system with (so) many diagrams? Cognitive integration processes in diagrammatic reasoning. Inform. Systems Res. 11(3) 284–303.

Kim, Y. G., S. T. March. 1995. Comparing data modeling formalisms. Comm. ACM 38(6) 103–115.

Kirk, R. E. 1995. Experimental Design: Procedures for the Behavioral Sciences, 3rd ed. Brooks/Cole Publishing, Pacific Grove, CA.

Kobryn, C. 1999. UML 2001: A standardization odyssey. Comm. ACM 42(10) 29–37.

Kung, C. H., A. Solvberg. 1986. Activity modelling and behavior modelling. T. W. Olle, H. G. Sol, A. A. Verrijn-Stuart, eds. Information Systems Design Methodologies: Improving the Practice. IFIP, North-Holland, Amsterdam, The Netherlands, 145–171.

Lackoff, G. 1987. Women, Fire, and Dangerous Things: What Categories Reveal about the Mind. Chicago University Press, Chicago, IL.

Larman, C. 2001. Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and the Unified Process. Prentice Hall, Englewood Cliffs, NJ.

Lieberman, B. 2003. The art of modeling: Part 1: Constructing an analytical framework. Rational Edge (August).

Mayer, R. 1989. Models for understanding. Rev. Educational Res. 59 43–64.

Moody, D. L. 2002. Complexity effects on end user understanding of data models: An experimental comparison of large data model representation methods. Proc. 10th Eur. Conf. Inform. Systems ECIS-, Gdansk, Poland, 482–496.

Moore, G. C., I. Benbasat. 1991. Development of an instrument to measure the perceptions of adopting and information technology innovation. Inform. Systems Res. 2 192–222.

Murata, T. 1989. Petri nets: Properties, analysis and applications. Proc. IEEE 77(4) 541–579.

Newell, A., H. A. Simon. 1972. Human Problem Solving. Prentice Hall, Englewood Cliffs, NJ.

Nunnally, J. C. 1967. Psychometric Theory. McGraw-Hill, New York.

Olle, T. W., J. Hagelstein, I. G. Macdonald, C. Rolland, H. G. Sol, F. J. M. Van Assche, A. A. Verrijn-Stuart. 1988. Information Systems Methodologies: A Framework for Understanding. Addison-Wesley, IFIP, Wokingham, England.

Parnas, D. L. 1972. On the criteria to be used in decomposing systems into modules. Comm. ACM 15(12) 1053–1058.

Parsons, J. 1996. An information model based on classification theory. Management Sci. 42(10) 1437–1453.

Parsons, J. 2002. Effects of local versus global schema diagrams on verification and communication in conceptual data modeling. J. Management Inform. Systems 19 155–184.

Parsons, J., Y. Wand. 1997. Using objects for systems analysis. Comm. ACM 40 104–110.

Paulson, D., Y. Wand. 1992. An automated approach to information systems decomposition. IEEE Trans. Software Engrg. 18(3) 174–189.

Pretz, J. E., A. J. Naples, R. J. Sternberg. 2003. Recognizing, defining, and representing problems. J. E. Davidson, R. J. Sternberg, eds. The Psychology of Problem Solving. Cambridge University Press, Cambridge, U.K., 3–30.

Purao, S., V. K. Vaishnavi. 2003. Product metrics for object-oriented systems. ACM Comput. Surveys 35(2) 191–221.

Rumbaugh, J., I. Jacobson, G. Booch. 1999. The Unified Modeling Lan guage Reference Manual. Addison Wesley, Reading, MA.

Shanks, G. 1999. Representation in information systems. Presented to the IS Foundations Workshop, Department of Computing, Macquarie University, Sydney, Australia.

Shanks, G., E. Tansley, R. Weber. 2004. Representing composites in conceptual modeling. Comm. ACM 47(7) 77–80.

Simon, H. A. 1996. The Sciences of the Artificial. MIT Press, Cambridge, MA.

Sircar, S., S. P. Nerur, R. Mahapatra. 2001. Revolution or evolution? A comparison of object-oriented and structured systems development methods. MIS Quart. 25(4) 457–471.

Storey, V. C., R. H. L. Chiang, D. Dey, R. C. Goldstein, S. Sundaresan. 1997. Database design with common sense business reasoning and learning. ACM Trans. Database Systems 22(4) 471–512.

Todd, P. A., I. Benbasat. 1987. Process tracing methods in decision support systems research: Exploring the black box. MIS Quart. 11(4) 493–512.

Vessey, I., S. A. Conger. 1994. Requirements specification: Learning object, process, and data methodologies. Comm. ACM 37(5) 102–113.

Wand, Y., R. Weber. 1990. An ontological model of an information system. IEEE Trans. Software Engrg. 16 1282–1292.

Wand, Y., R. Weber. 2002. Information systems and conceptual modeling—A research agenda. Inform. Systems Res. 13(4) 363–376.

Weber, R. 1997. Ontological Foundations of Information Systems. Coopers & Lybrand and Accounting Assoc. of Australia and New Zealand, Melbourne, Australia.

Weber, R. 2001. Comprehending decompositions: A theory and two empirical tests. Working paper, Monash University, Victoria, Australia.

Wieringa, R. 1998. A survey of structured and object-oriented software specification methods and techniques. ACM Comput. Surveys 30(4) 459–527.

Yourdon, E. 1989. Modern Structured Analysis. Prentice Hall, Englewood Cliffs, NJ.

Yourdon, E., L. L. Constantine. 1979. Structured Design: Fundamentals of a Discipline of Computer Program and System Design. Prentice Hall, Upper Saddle River, NJ.
