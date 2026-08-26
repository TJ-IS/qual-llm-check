---
otero_id: 824
otero_key: "QVJEWBME"
title: "The pragmatic quality of Resources- Events-Agents diagrams: an experimental evaluation"
authors: "Geert Poels; Ann Maes; Frederik Gailly; Roland Paemeleire"
year: "2011"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2007.00253.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The pragmatic quality of Resources-Events-Agents diagrams: an experimental evaluation

Geert Poels,\* Ann Maes,<sup>†</sup> Frederik Gailly<sup>‡</sup> & Roland Paemeleire<sup>§</sup>

Department of Management Information, Operations Management and Technology Policy, Faculty of Economics and Business Administration, Ghent University, Tweekerkenstraat 2, 9000 Gent, Belgium, \*email: geert.poels@ugent.be, <sup>†</sup>email: a.maes@ugent.be, <sup>‡</sup>email: frederik.gailly@ugent.be, and <sup>§</sup>email: roland.paemeleire@ugent.be

Abstract. The Resources-Events-Agents (REA) model is a semantic data model for the development of enterprise information systems. Although this model has been proposed as a benchmark for enterprise information modelling, only few studies have attempted to empirically validate the claimed benefits of REA modelling. Moreover, these studies focused on the evaluation of REA-based system implementations rather than directly assessing the REA-modelled conceptual schemas that these systems are based on. This paper presents a laboratory experiment that measured the user understanding of diagrammatic conceptual schemas developed using the REA model. The theoretical foundation for the hypotheses are cognitive theories that explain pattern recognition phenomena and the resulting reduction in cognitive effort for understanding conceptual schemas. The results of the experiment indicate a more accurate understanding of the business processes and policies modelled when users recognize the REA model’s core pattern of enterprise information in the diagram. The implication for modelling practice is that the use of the REA model improves the requirements engineering process by facilitating the user validation of conceptual schemas produced by analysts, and thus helps ensuring the quality of the enterprise information system that is developed or implemented.

Keywords: enterprise information systems, conceptual modelling, modelling pat terns, schema quality, user comprehension

## INTRODUCTION

The Resources-Events-Agents (REA) model (McCarthy, 1982) is a semantic data model originating in the accounting field. The model was conceived in the early eighties as a design technique for enterprise-wide accounting databases that store disaggregated transactional data.

An enterprise is seen as a value chain of interrelated business processes, where each process is decomposed into its constituent elements. The REA model provides a template to describe these elements and their associated data. Given its origin and purpose, the model takes a data-oriented view of a business process, meaning that the business process structure is used to provide structure to the database (hence the adjective ‘semantic’). It should be noted, however, that the REA model was not intended to describe business process behaviour or system workflow. It is only very recently that some extensions towards the modelling of dynamic process aspects have been suggested (McCarthy, 2004; Geerts & McCarthy, unpublished; Parker et al., 2005).

For almost 20 years, the REA model was widely used as an educational instrument for teaching business students how to design accounting databases (McCarthy, 2003), while its use in system development practice was limited to a few companies (McCarthy, 1999). Recently there has been a remarkable increase in researchers’ and practitioners’ interest in the model because of two reasons. First, the REA model developers were involved in a number of international standardization efforts for e-collaboration systems (e.g. ISO Open-ED initiative, UN/CEFACT, OAG, eBTWG). This participation has resulted in the adoption of (parts of) the REA model as a business process ontology in the UN/CEFACT Modeling Methodology (UMM) business process and information model construction methodology (UN CEFACT, 2003) and the E-Commerce Integration Meta-Framework (ECIMF) system interoperability enabling methodology (ECIMF Project Group, unpublished). Second, the REA mode has been proposed as a theoretical basis and normative enterprise model for the reference models that underlie Enterprise Resource Planning (ERP) systems (David et al., 1999; O’Leary, 2004). Both developments are witnesses of the REA model’s importance in the current and future enterprise systems landscape.

The core of the REA model is a recurring pattern of relationships between the three kinds of entities (i.e. resources, events and agents) that are involved in any exchange (e.g. sales, acquisition) or conversion (e.g. manufacturing) process. This core pattern (described in the Basic REA Template shown in Figure 1) contains three kinds of relationships. Stockflow relationships associate resources (i.e. things having economic value for the enterprise) with the events that effectuate the flows in and out of these resources. The core pattern prescribes that for each event effectuating an inflow of some resource there is a corresponding event effectuating an outflow of the same or another resource. This dual nature of an economic exchange or conversion is modelled by an economic duality relationship between the pair of resource increment and resource decrement events. Finally, participation relationships associate the events involved in an economic exchange or conversion with their participating agents. Such agents can be internal to the company, like a salesperson or a purchase agent (i.e. inside participation) or external, like a customer or a vendor (i.e. outside participation).

Although the use of the REA model is not tied to a particular data modelling formalism (Dunn & McCarthy, 1997), the Entity-Relationship (ER) model (Chen, 1976), as used in the Basic REA Template (Figure 1), is its preferred and most often used format (Dunn et al., 2005). A REA diagram can thus be defined as a diagrammatic ER representation of a business process that is obtained through the use of the Basic REA Template (Romney & Steinbart, 2006).<sup>1</sup> Figure 2 shows, for instance, a REA diagram of the acquisition/payment process in a retail company.

![](/api/attachments/QVJEWBME/fulltext/images/21ea519144ade2c6e708969b0ba763006ede481fabdfad5af6fd3a8728e48d23.jpg)  
Figure 1. The Basic REA Template

The instantiation of the generic pattern that is captured in the Basic REA Template is the main activity in the REA modelling of a business process. The repeated use of this modelling pattern for establishing an enterprise-wide information model is also the most distinguishing feature of REA modelling (Dunn & McCarthy, 1997). Subsequent REA modelling activities include specifying structural constraints on the REA diagram relationships to express business rules (by means of cardinality constraints), describing the properties of the modelled entities and relationships (by means of attributes), and integrating the separately developed business process schemas into a global conceptual schema of the enterprise information system.

Dunn & McCarthy (1997) argue that the REA model is the only enterprise information model with a structuring orientation in the sense that a normative structure (i.e. the REA core pattern) is imposed on the conceptual schema of a business process. They therefore contend that any research outputs that ignore the contributions of the REA model to the conceptual modelling of enterprise systems would not be justifiable as advances in the field. Supported by March &

![](/api/attachments/QVJEWBME/fulltext/images/2061cff525abf1b57ebc2cf1ca7042e192dced6189a3fcc7f5bacb4b272bb486.jpg)  
Figure 2. REA diagram of the acquisition/payment process in a retail company.

Smith’s (1995) IT research framework, Dunn and McCarthy further argue that researchers proposing alternative models should demonstrate that their alternatives ‘evaluate’ well against the REA model on some definite performance metrics.

Dunn & McCarthy (1997) admit, however, that the benefits of having a structuring orientation are only hypothesized and have not been subjected to empirical testing. Empirical evidence for this and related claims such as high semantic expressiveness (Dunn & Grabski, 2000) and the improved readability of REA diagrams due to an indexing mechanism inherent in the Basic REA Template (Dunn & Gerard, 2001; Romney & Steinbart, 2006) is scarce. Dunn & Grabsk (2000) demonstrated experimentally that accounting users perceive an enterprise system based on the REA model as more semantically expressive than a system based on the Debit-Credit-Account (DCA) model. They also showed that higher perceived semantic expressiveness is associated with higher task accuracy in information retrieval. However, the study did not directly compare the REA model against the DCA model. The participants were given proxy system implementations in the form of a relational logical database model (for REA) and sample journals and ledger accounts (for DCA). Moreover, example source documents turned out to be necessary to retrieve some of the required information when the DCA-based system was used (Summers, 2000). In a related study, Dunn & Grabski (2001) showed that the structuring orientation of the REA model resulted in a greater degree of localization (i.e. the grouping together of the information that must be retrieved) and better user performance in information retrieval tasks, as compared with a DCA-based system. As in their previous study, the experimental materials included the conceptual schema (REA diagrams vs. a complete chart o accounts), relational table definitions (as an implementation of the REA-based system) and sample source documents.

It should be noted that the experiments of Dunn and Grabski did not evaluate the REA mode as a conceptual modelling technique for enterprise information systems. Conceptual modelling is the cornerstone of requirements engineering (Siau & Tan, 2005b). Conceptual schemas are used to represent the user information requirements that system analysts have elicited and specified. One of the main purposes of conceptual schemas is to facilitate the communication between systems analysts and the future system end-users (Siau, 1999; Topi & Ramesh, 2002; Parsons & Cole, 2005). When the analysts have represented the requirements, the users can validate the results of the requirements specification by checking the conceptual schemas. The discrepancies detected between the requirements as represented in the schemas and the ‘real’ requirements as perceived by the users, provide useful inputs for further requirements specification and negotiation activities. This iterative process should eventually lead to completely specified, formally represented and commonly agreed upon information system requirements (Pohl, 1994), providing the basis for successful information systems development or implementation.

It is our position that before the REA model is accepted as a benchmark against which new models are evaluated, it needs proper evaluation itself, even if many of its claimed benefits seem natural and logical. Further evidence of the quality of the REA model as a foundation for (interorganizational) enterprise systems is also highly desired given its impact on modelling methodologies such as UMM and ECIMF.

This paper contributes towards a systematic evaluation of the REA model as a technique to construct problem space representations of business processes. It reports on a laboratory experiment that was conducted to compare the user comprehension of informationally equivalent REA and non-REA diagrams. Two diagrams are informationally equivalent if all information in one diagram is inferable from the other and vice versa (Larkin & Simon, 1987). For the purpose of this paper, we define a non-REA diagram as an ER diagram that is not obtained through the instantiation of the generic pattern captured in the Basic REA Template. Hence, the research question investigated in this paper is whether the REA model adds value to the ER model that is generally used as its operational modelling formalism. This question was approached from the perspective of the conceptual schema user (instead of a schema developer point of view).

The structure of the paper is the following. Section 2 presents the theoretical background of the study presented in this paper. Section 3 describes the design and execution of the experiment. The analysis and interpretation of the results is presented in section 4. Finally, section 5 summarizes the contribution of this paper and discusses the limitations and future research opportunities.

## THEORETICAL BACKGROUND, PREVIOUS RESEARCH AND PROPOSITION

A basis for the systematic evaluation of the REA model can be found in the framework for conceptual schema quality of Lindland et al. (1994). This framework is grounded in semiotic theory, which has been used as a foundation for quality frameworks in various domains, e.g.

![](/api/attachments/QVJEWBME/fulltext/images/9b30f0ac46ac9680b41e3aa782cf8f956483cbcc248718dd794c679a8e01fb21.jpg)  
Figure 3. Lindland et al.’s framework for quality in conceptual modelling (Lindland et al. 1994).

ontology development (Burton-Jones et al., 2005), information quality assurance (Price & Shanks, 2005) and software evaluation (Kitchenham et al., 2005). According to Lindland et al. (1994), modelling is making statements in some language. The REA model is in this sense a language, whereas a REA schema is a collection of statements. A REA diagram is a REA schema represented in a diagrammatic format following the graphical ER modelling formalism.

Lindland et al.’s framework distinguishes three types of quality based on the correspondence between four sets of statements: Language, i.e. the set of statements allowed by the language; Domain, i.e. the set of statements that would be correct and relevant for describing the problem domain; Schema, i.e. the set of statements actually contained in the conceptua schema; and User Interpretation, i.e. the set of statements that users think the conceptua schema contains (Figure 3). Syntactic quality describes how well the schema follows the rules of the language. Semantic quality describes how well the schema corresponds to the problem domain. Finally, pragmatic quality describes how well the schema is understood by its users. For each of these quality types, goals are formulated and means to achieve or improve the goals are identified. Quality achievement/improvement means include modelling activities and language or schema properties.

The framework suggests that a systematic evaluation of the REA model would consider syntax, semantics and pragmatics. In conceptual modelling research and practice, the assurance of syntactic quality is well understood and supported by automated tools (Poels et al., 2003). Therefore, the main evaluation effort should be directed towards semantic and pragmatic quality.

The goals for semantic quality are validity and completeness, meaning that the set of statements contained in the conceptual schema is the same as the set of statements that would be correct and relevant for describing the problem domain (i.e. Schema = Domain). Lindland et al. (1994) contend that improvements in pragmatic quality can improve semantic quality by making it easier to detect invalidity (i.e. Schema\Domain ≠ ø) and incompleteness (i.e. Domain\Schema ≠ ø). A complete and accurate understanding of conceptual schemas by future system users, which are the primary stakeholders in the conceptual modelling process concerned with understandability (Moody & Shanks, 2003), is therefore essential in the process of validating the user requirements captured in the schemas. If REA diagrams improve the users’ understanding of the requirements that have been specified by system analysts, then users should find it easier to detect requirements specification errors and provide relevan feedback for analysts to enhance the semantic quality of the schemas. Also outside a systems development or implementation context, types of business users exist that need to understand conceptual schemas. For instance, auditors need to understand representations of business reality in order to make inferences upon that reality (like identifying the need for internal controls). Consequently, we decided to focus our attention towards the evaluation of the pragmatic quality of REA diagrams, from a business user’s point of view.

Previous research on Conceptual Modeling Quality (CMQ) offers some support for the REA model as a quality assurance tool for the pragmatic quality of conceptual business process schemas. Structure, for instance, has been mentioned by Lindland et al. (1994) as a quality carrying property of a schema directed specifically towards a better understanding. In his quality model for ER diagrams, Kesh (1995) postulates a causal relationship between suitability of structure, i.e. how well the structure of the diagram reflects the structure of the problem domain, and usability.

We also mentioned before the implicit presence of an indexing mechanism in the Basic REA Template. This indexing mechanism is formed by a diagram layout where the entities representing resources, events and agents are placed in, respectively, a left, middle and right column of the diagram. Additionally, the top-down ordering of the entities that represent events may be used to reflect the sequence of event occurrences (i.e. temporal relationships between the ‘event’ entities).

According to Romney & Steinbart (2006), these placement conventions produce REA diagrams that are easy to read. Some support for this claim can also be found in the CMQ literature. Krogstie et al. (1995), for instance, list graph aesthetics and diagram layout among the means to achieve pragmatic quality. The Guidelines of Modeling of Schütte & Rotthowe (1998) also include layout design in the ‘Principle of Clarity’ and consider it as an element supporting the lucidity, and hence comprehensibility of a schema. Finally, in their research agenda fo information systems and conceptual modelling, Wand & Weber (2002) postulate that the physical rearrangement of the entities and relationships on an ER diagram affects user comprehension.

The particular placement of entities on a REA diagram explained above is a diagrammatic convention, not a mandatory rule of REA modelling. It should be noted, however, that wellknown textbooks on enterprise information modelling that promote the use of the REA model such as Dunn et al. (2005) and Romney & Steinbart (2006), adhere as much as possible to these placement conventions. Furthermore, these conventions are incorporated in the Basic REA Template, hence automatically applied when instantiating the REA core pattern. It could even be argued that enforcing this diagram layout helps to provide a modelling framework for the use of the REA core pattern. So when we evaluate the pragmatic quality of REA diagrams, we do not distinguish between the effect of the normative structure (which is part of the REA model) and the arrangement factor (which is part of ‘best practices’ in REA modelling).

The quality-carrying properties ‘diagram structuredness’ and ‘diagram aesthetics’ mentioned in CMQ research are thus properties assured by the structuring orientation and diagrammatic conventions of the REA model. To explain why and how these schema properties affect user understanding, we need to recognize that conceptual modelling involves human cognition. According to Siau & Tan (2005b), conceptual modelling is characterized by an ongoing sense-making process in which different stakeholders such as end-users and system analysts participate. Theories of cognition, and in particular those that take a human information-processing perspective, help understanding the representation and use of knowledge by humans (Siau, 1999). Given the limitations of the human information-processing system (e.g. it is well accepted that humans can attend to only a few information elements at the same time), a conceptual schema with good pragmatic quality has been described as a schema that can be interpreted with little cognitive effort (Siau & Tan, 2005b). Hence, the question is how can the REA modelling of a conceptual schema reduce the user’s cognitive effort involved in understanding the schema?

We believe the answer must be found in a mental process called pattern recognition. Batra & Wang (2004) and Antony & Mellarkod (2004) refer to schema theories and production system theories like the Adaptive Control of Thought framework (Anderson, 1996) and templatematching theories like Structure-Mapping Theory (Gentner & Medina, 1998) to explain when and how conceptual data modelling patterns are recognized. Schema theories and production system theories describe the processes involved in the storing and retrieval of structures of information elements from long-term memory and the matching of retrieved information structures with the contents of working memory. Template-matching theories present mental mechanisms by means of which information structures are activated in working memory. Two of these mechanisms are useful for explaining how users match REA diagrams to the REA core pattern template:

• Abstraction: the mental process by means of which a conceptual schema is mapped into a more abstract, deeper structure, that is subsequently compared with the pattern template. It is plausible that the structuring orientation of the REA model and the resulting greater degree of localization in REA diagrams (Dunn & Grabski, 2001) facilitate this abstraction process.

• Analogy mapping: the mental process of finding parallels between the conceptual schema and the pattern template. Compared with abstraction, analogy emphasizes more the ‘overal picture’ that is common to the schema and the pattern. It is likely that the diagrammatic conventions of the REA model help triggering this analogy mapping process.

The recognition of the REA core pattern in a diagram thus facilitates sense-making. Users can now interpret the diagram elements in terms of the different ontological constructs of the REA model (i.e. events, agents, resources, stockflow relationships, economic duality relationships, participation relationships). After pattern recognition, the diagram they need to understand corresponds better to their frame of reference (Siau & Tan, 2005a), hence reduces the cognitive effort needed in understanding. When confronted with a non-REA diagram, however, users will not reap the benefits of pattern recognition and the cognitive effort involved in understanding the diagram will be higher (i.e. lower pragmatic quality). Therefore, we formulate the following proposition:

The user comprehension of a REA diagram is better than the user comprehension of an informationally equivalent non-REA diagram.

The specification of information equivalence of the two types of diagrams is required as otherwise differences in information content may confound differences in user comprehension (Parsons & Cole, 2005). But when the REA and non-REA diagram convey exactly the same information about the business process modelled, the proposition postulates that the REA diagram user acquires a better understanding of the process modelled than the non-REA diagram user.

We realize that it is unfeasible to demonstrate this proposition for all possible diagram structures and layouts that satisfy information equivalence with the REA diagram. Informationally equivalent non-REA diagrams could be structured according to many different structuring schemes, and it is not our intent to test all other ontological and/or spatial structures. When we operationalize the concept of non-REA diagram (to test the proposition), we must avoid introducing other structuring principles as potential confounding variables contaminating the study.

## DEFINITION, PLANNING, AND OPERATION OF THE EXPERIMENT

To test the proposition, we conducted an evaluation study in the form of a laboratory experiment. This section describes the design and execution of the experiment. The next section pre sents and discusses the results of the statistical tests on the collected data.

## Treatments

In the experiment, participants were given diagrammatic conceptual schemas of business processes on which they had to perform a comprehension task. The task consisted of answering a number of questions about a business process, as represented by the diagram. As this diagram was their only source of information about the business process, the comprehension task was designed to assess the business process understanding that participants acquired through the use of the diagram.

The factor under investigation in the experiment was the use of the REA model for modelling exchange or conversion business processes. As the REA modelling of a business process is done through instantiation of the REA core pattern (as captured in the Basic REA Template), the experimental treatments were the administration of a REA diagram vs. the administration of an informationally equivalent non-REA diagram.

## Dependent variables

There are at least two dimensions upon which to compare conceptual modelling grammars:<sup>2</sup> effectiveness and efficiency (Gemino & Wand, 2003). It must be noted that a grammar (e.g. the REA model) cannot be effective or efficient per se; it is the use of a grammar (i.e. REA mod elling) that determines its effectiveness and efficiency with respect to a conceptual modelling task. Effectiveness can in this context be defined as the extent to which a method improves the quality of the task outcome (Moody, 2001). Efficiency is the extent to which a method reduces the effort to perform the task (Moody, 2001).

It can be argued that effectiveness is the more important evaluation criterion. ‘Better’ user comprehension (as stated in the proposition) then primarily means that a REA diagram creates a more correct perception of the business process in the mind of the user (Gemino & Wand, 2003). Recognizing the pattern occurrence in the REA diagram may also speed up understanding, which means that time (and thus money) is saved. According to Parsons (2003, p. 163), ‘time may be a useful secondary measure of the “naturalness” of a representation if treatments do not yield significant differences in accuracy’. Therefore, we evaluated REA modelling with respect to both its effectiveness and efficiency in user comprehension, although we acknowledge that accuracy of understanding is a more relevant criterion than speed of understanding.

In practice, a better comprehension may be compromised by a faster comprehension (e.g. because of time pressure) (Bodart et al., 2001). There might thus be a trade-off between the effectiveness and efficiency dimensions of user comprehension. Therefore, we also operationalized the concept of pragmatic quality using a third variable, efficacy, which is a concept analogous to productivity (i.e. relating an output variable to an input variable) (Moody, 2001). Hence, for the purpose of the experiment, efficacy was defined as the ratio of effectiveness to efficiency.<sup>3</sup>

## Measures

Our choice of measures for the dependent variables was guided by previous empirical CMQ research (see Topi & Ramesh (2002), Wand & Weber (2002), Gemino & Wand (2003) and Parsons & Cole (2005) for recent overviews). As in Bodart et al. (2001), Shoval et al. (2002) and Parsons (2003), comprehension time was chosen as a measure of the efficiency of user comprehension. Comprehension time was defined as the time required to complete a comprehension task. This time includes reading the questions that were formulated to assess user comprehension, solving the problems posed by these questions through analysis of the experimental object (i.e. a REA or non-REA diagram), and answering the questions by writing down the solutions. The effectiveness of user comprehension was measured by the accuracy of comprehension, which is defined as the ratio of the number of correctly answered questions to the total number of questions that make up the comprehension task (Kim & March, 1995; Siau et al., 1997; Bodart et al., 2001; Shoval et al., 2002; Burton-Jones & Weber, 2003; Parsons,

<sup>3</sup>The concept of efficacy also reflects the idea that a perfect comprehension is not necessarily the end goal for pragmatic quality. In Lindland et al.’s framework, this idea is taken further by the concept of feasible comprehension (Lindland et al., 1994), which is achieved when the benefit of rooting out remaining misunderstandings does not exceed the cost of taking that effort.

2003). Finally, the efficacy of user comprehension was measured with the normalized accuracy measure that was defined by Bodart et al. (2001) as the ratio of the accuracy of comprehension to the comprehension time.

## Selection of participants

The participants in our experiment were 30 graduate students enrolled in an Accounting Information Systems course. Prior to the experiment, these business students were introduced to the conceptual modelling of enterprise systems using the ER model. They were also taught the basic principles of the REA model and learned how to use the Basic REA Template to create REA core pattern occurrences.

As part of the course exercises, the students were required to analyse diagrammatic conceptual schemas of various kinds of business processes for different types of companies, answering questions similar to the comprehension questions used in the experiment. Some of these diagrams were constructed using the Basic REA Template, others were not or instantiated only parts of the REA core pattern. The modelling formalism was in all cases the ER model.

During the course, information systems were mainly studied from a user perspective. The students were forced into the roles of accountants, auditors and business analysts that need to work with enterprise system conceptual schemas in order to validate the schemas with respect to end-user or business requirements (e.g. business rules) and to analyse the modelled business processes.

## Experimental design

At the beginning of the course, the students completed a questionnaire to obtain demographic data. We noticed that personal characteristics that are likely to have an impact on the ability to perform the comprehension task, like years of working experience, type of working experience and number of Management Information System (MIS) courses taken before, differed considerably among participants. In order to control for these differences, a within-subjects design was chosen. In such a design, each participant contributes an observation for each treatment

The REA and non-REA treatments for each participant relate to two different business processes. The chosen processes, hereafter referred to as ‘debt financing’ and ‘equity financing’, were similar in scope and serve the same goal, i.e. acquiring funds for the company. They were not studied before in the course, to avoid possible persistence effects. It could not be determined a priori that one of them was intrinsically more comprehensible to the students than the other one. Therefore, to alleviate a potential instrumentation effect, four experimental objects were created, meaning that each of the two financing processes was represented by a REA diagram and an informationally equivalent non-REA diagram.

To cancel out likely learning effects because of the use of the same graphical modelling formalism (the ER model) and similarities in the two types of financing processes, the business process (debt financing and equity financing) and treatment (non-REA diagram and REA diagram) were counterbalanced. The resulting experimental design is shown in Table 1. Participants were randomly allocated to two equal-size groups, hereafter referred to as group A and group B. Within each group, the order of the comprehension tasks was reversed for about half of the students. For instance, within group A, part of the participants performed first the comprehension task required for the non-REA diagram of the debt financing process, and next the comprehension task required for the REA diagram of the equity financing process, whereas this order was reversed for the rest of the group A members.

Table 1. Experimental design

<table><tr><td>Type of diagram</td><td>Non-REA</td><td></td><td>REA</td><td></td></tr><tr><td>Business process</td><td>Debt financing</td><td>Equity financing</td><td>Debt financing</td><td>Equity financing</td></tr><tr><td>Group</td><td>Group A</td><td>Group B</td><td>Group B</td><td>Group A</td></tr></table>

REA, Resources-Events-Agents

## Instrumentation

The four experimental objects are included in Appendix A. The diagrams show cardinality constraints for specifying business rules that hold for the process modelled. However, they do not include attributes for representing properties of entities and relationships. Hence, the diagrams should be considered as enterprise schemas, rather than data schemas. Accordingly, the experimental task was not aimed at information retrieval, but focused on assessing the participant’s understanding of business process structure (i.e. the what, who and why of the process) and business logic (i.e. the common business practices and specific business policies that govern the process).

The two diagrams used as objects for the REA treatment qualify as REA diagrams in the sense that they are instantiations of the generic transaction pattern portrayed in the Basic REA Template. The non-REA diagrams were derived from the REA diagrams by modifying them. The transformation from REA to non-REA aimed at creating diagrams in which the REA core pattern occurrence was no longer easily and quickly recognizable to diagram users that are familiar with REA modelling. The transformation was constrained, however, by the requirement of information equivalence, meaning that no information may be added to or deleted from the REA diagram. Furthermore, the transformation should avoid as much as possible to add other ontological and spatial structuring elements to the diagrams, as introducing such elements may confound the study results. We therefore decided to use a limited set of modifications that focus on the most essential and distinctive features of the REA core pattern as shown in the Basic REA Template.

The consequent pairing of a resource increment event with a resource decrement event in every business process schema is the most intriguing structuring idea of the REA mode (O’Leary, 2000). Other parts of the REA core pattern (like the stockflow and participation relationships) can be found in other modelling patterns for transactions (see, e.g. Hay (1996) and Fowler (1997)). But the explicit identification of an economic duality relationship within every economic exchange or conversion process is probably a unique feature of the REA model.<sup>4</sup> Because the explicit representation of economic duality would directly reveal the presence of a REA core pattern occurrence (probably more than any other feature), we decided to hide it by reifying the relationship between the increment and decrement event entities in the REA diagrams. Reifying the economic duality relationship (i.e. Payment\_for in Figures A1 and A3) creates a new entity (i.e. Share in Figure A2 and Loan in Figure A4) which is related by two new relationships to the increment and decrement event entities.<sup>5</sup> The new entity materializes the economic duality and hence makes it less recognizable to diagram users that expect to find a direct relationship between the increment and decrement event entities (as in the Basic REA Template).

A second modification was the physical repositioning of the entities and relationships on the diagrams. By no longer adhering to the usual placement conventions for REA diagrams, we intended to further hide the underlying REA core pattern occurrence. Hence, the readability guidelines for REA diagrams were deliberately violated. The physical rearrangement involved organizing the diagram entities into three layers: a top layer for the agent entities, a middle layer for the event entities, and a bottom layer for the resource entities. This rearrangement was basically obtained by a 90 degrees left turn of the diagram. Next, entities were connected as in the REA diagrams (except for the reified economic duality relationship). The result is a dia gram that looks different, but is not intrinsically less natural than the original REA diagram (though it might be perceived as less readable by people that are trained in REA modelling as it does not match their frame of reference).

The transformation did not intend to create ‘anti-REA’ diagrams. Any conceptual schema with the same semantic quality as the REA diagrams used in the experiment would contain elements that represent the essential business concepts (i.e. transactions and the resources and parties involved) of the processes modelled. The point is that REA modelling mandates the use of a preset pattern of relationships and entities to represent these concepts. Therefore, the non-REA diagrams should not show too obviously the presence of a REA core pattern occurrence. To test our hypotheses, it is sufficient that the non-REA diagrams look as if they were not developed using the Basic REA Template.

## Design of experimental tasks

Each comprehension task involved answering a questionnaire. The comprehension questions were designed to reflect typical cases of schema validation or interpretation by domain experts or future system end-users. Validating or interpreting a schema requires understanding what is represented in the schema and it is exactly this understanding that the questions intended to test.

Six questions were binary questions requiring a ‘Yes’ or ‘No’ answer. To prevent guessing, a negative score was associated to a wrong answer. In the binary questions, participants were asked if the business process as modelled in the schema conformed to some statement about a business rule. Alternatively, they were asked about the completeness of the schema with respect to reality. An example in the first category is ‘Is the conceptual model that is depicted in the diagram correct given that in reality each dividend payment transaction relates to exactly one stock issuance?’ An example of the second category is ‘Is the transaction cycle that is modeled in the diagram complete in the sense that for every business activity there is an employee that can be hold accountable?’ These questions reflect typical problems to be solved during schema validation.

The other six questions were of the open kind and assessed the understanding that accountants or auditors develop when analysing business process models. They ranged from fundamental accounting issues like ‘List the positions in the value cycle that is modelled in the diagram’ to specific accounting system design questions like ‘What entity type plays a centra role when integrating this diagram with other diagrams representing other transaction cycles?’. These questions require interpreting the schema based on prior (though general) accounting knowledge, referring to concepts such as value cycles, transaction cycles, give-to-get relationships, assets, events and positions, all of which were concepts reviewed during the course. These questions do not aim at schema validation as no statement on the modelled reality is provided.

All questions were formulated such that they were identical for the non-REA and REA diagrams of a same financing business process. But also across the equity and debt financing processes, most of the questions were identical, as they were formulated in domainneutral terms. Three questions related to validity checking and business rule interpretation referred to specific entity names on the diagrams and hence existed in two variants (one for equity financing; the other for debt financing). The only difference between these variants were the entity names referred to. The questions used in the experiment are included in Appendix B.

## Operational procedures

The experiment was organized as an individual class room exercise for which credits could be earned (as part of the final examination). At the start of the experiment, each participating student was randomly allocated to a group and received the experimental materials for the first experimental run of the within-subjects experiment. When a participant finished the first comprehension task, all experimental materials including the answers to the questions were handed in and the materials required for the second part of the experiment were given to the participant. Participants could take whatever time they thought was necessary (within reasonable limits determined by practical considerations such as the duration of a typical course session). During the experiment, the student comprehension times (i.e. time between receiving the experimental materials of a run and handing in the answers) were measured by the experimenters.

After the experiment, the answers were corrected by the course teacher and doublechecked by the experimenters. The answer to a binary (i.e. ‘Yes’ or ‘No’) question was considered correct if the appropriate choice between ‘Yes’ and ‘No’ was made. In case the wrong choice was made or no answer was given, the answer was considered incorrect.<sup>6</sup> The answer to an open-ended question was compared with a model answer, that contained the right solu tion to the problem presented. An answer was considered correct only if it matched to the right solution, meaning that all elements of the model answer were present. If one or more required elements were missing, the answer was considered incorrect. Also when wrong or irrelevant elements were given, the answer was considered incorrect. For instance, the model answer for ‘List the events in the value cycle that is modelled in the diagram’ and the equity financing REA diagram is (Issue\_stock, Pay\_dividend). Only when these two events were mentioned in the answer, and no more or other than these events, the answer was considered correct.

To calculate the accuracy score per student/treatment, the questions correctly answered were counted and this count was subsequently divided by the number of questions in the questionnaire. No weights were used, so the contribution of each correctly answered question was the same. To calculate the normalized accuracy score, the accuracy score was divided by the comprehension time that we measured.

## Operational hypotheses

For ease of reference, we end this section by summarizing the operational hypotheses and the stated direction effects:

$\mathsf { H } _ { \mathsf { e f f e c t i v e n e s s } } .$ : The accuracy of comprehension of a REA diagram is higher than the accuracy of comprehension of a non-REA diagram.

$\mathsf { H } _ { \mathsf { e f f i c i e n c y : } }$ : The comprehension time for a REA diagram is less than the comprehension time for a non-REA diagram.

$\mathsf { H } _ { \mathsf { e f f i c a c y } } ,$ : The normalized accuracy of comprehension of a REA diagram is higher than the nor malized accuracy of comprehension of a non-REA diagram.

## DATA ANALYSIS AND INTERPRETATION

In this section, the data collected from the experiment are described and the hypotheses are tested. Descriptive statistics (mean, median and standard deviation) for accuracy of comprehension, comprehension time and normalized accuracy are shown in Table 2. The sample size in each cell is 30.

Table 2. Descriptive statistics by treatment

<table><tr><td></td><td>REA</td><td>non-REA</td></tr><tr><td colspan="3">Time (minutes)</td></tr><tr><td>Mean</td><td>24.13</td><td>27.33</td></tr><tr><td>Median</td><td>25.50</td><td>28.00</td></tr><tr><td>SD</td><td>6.329</td><td>5.467</td></tr><tr><td colspan="3">Accuracy</td></tr><tr><td>Mean</td><td>0.6512</td><td>0.5666</td></tr><tr><td>Median</td><td>0.6538</td><td>0.5384</td></tr><tr><td>SD</td><td>0.1710</td><td>0.1984</td></tr><tr><td colspan="3">Normalized accuracy</td></tr><tr><td>Mean</td><td>0.0293</td><td>0.0217</td></tr><tr><td>Median</td><td>0.0281</td><td>0.0202</td></tr><tr><td>SD</td><td>0.0116</td><td>0.0088</td></tr></table>

REA, Resources-Events-Agents; SD, standard deviation

Table 3. Results of Wilcoxon signed rank test

<table><tr><td>Hypothesis and hypothesized direction of the effect</td><td>z</td><td>Significance (one-tailed)</td><td>Hypothesis supported?</td></tr><tr><td> $H_{\text{effectiveness}}$ : accuracy REA &gt; accuracy non-REA</td><td>-3.057</td><td>0.001</td><td>Yes</td></tr><tr><td> $H_{\text{efficiency}}$ : time REA &lt; time non-REA</td><td>-1.739</td><td>0.041</td><td>No</td></tr><tr><td> $H_{\text{efficacy}}$ : normalized accuracy REA &gt; normalized accuracy non-REA</td><td>-2.520</td><td>0.006</td><td>Yes</td></tr></table>

REA, Resources-Events-Agents

## Hypothesis testing

Although for all dependent variables the differences in paired observations were normally distributed, the non-parametric Wilcoxon signed rank test was used to test the hypotheses (Table 3). For small sample sizes, parametric tests are less robust (Harwell, 1988). Furthermore, for normal distributions and small sample sizes, the statistical power of the Wilcoxon signed rank test is higher than that of the parametric paired samples t-test (Tanizaki, 1997).

The results indicate that $\mathsf { H } _ { \mathsf { e f f e c t i v e n e s s } }$ is supported $( P < 0 . 0 0 1 )$ ), meaning that the accuracy of comprehension is significantly higher if a REA diagram is used instead of a non-REA diagram (with a statistical power of 0.91 according to the method and tables in Cohen (1988)).

The difference in comprehension time is not significant $( P < 0 . 0 4 1 )$ . For two-tailed tests, the generally accepted significance cut-off is 0.05. For one-tailed tests, however, a significance cutoff of 0.025 is common. Furthermore, a statistical power analysis revealed that the power of the hypothesis test is only 0.41, which makes it difficult to show an effect if there is one. Therefore, based on the experimental data, it cannot be concluded that REA diagrams are faster understood than non-REA diagrams.

Finally, the difference in normalized accuracy scores between the two types of diagram is significant $( P < 0 . 0 0 6 )$ and therefore $\mathsf { H } _ { \mathsf { e f f i c a c y } }$ is supported (with a statistical power of 0.84, which is acceptable). This result indicates that for a same amount of comprehension time spent, participants acquired a more accurate understanding of the REA diagrams than the informationally equivalent non-REA diagrams.

## Post-tests of confounding effects

Counterbalancing diagram type (non-REA or REA) and business process alleviates possible learning and maturation effects. Such effects can still bias the results, for instance, when there are differential learning rates for the two treatments (Bodart et al., 2001; Dunn & Gerard, 2001). Therefore, the observations were regrouped according to which treatment (non-REA o REA) was administered first. Next the non-parametric Mann–Whitney U-test was used to evaluate differences in comprehension times, accuracy scores and normalized accuracy scores between the group of participants that received a non-REA diagram first and next a REA diagram (16 participants) and the group that started with a REA diagram and continued with a non-REA diagram (14 participants). The results of the Mann–Whitney U-test are shown in Table 4. Results of between-group tests should, however, be interpreted with caution as dif ferences in human capability to perform the experimental task are no longer controlled for.

The analysis shows that for the same type of diagram comprehension times are lower in the second experimental run. If it is assumed that participants have learned from their task performed during the first experimental run, then this learning effect affects the efficiency dimension of user comprehension. Learning did not affect the effectiveness dimension (measured with the accuracy of comprehension measure). However, a differential learning rate for efficacy was observed. The normalized accuracy of comprehension of the non-REA diagrams in the second experimental run was significantly higher than in the first run, but this learning effect was not observed for the REA diagrams. A possible explanation of the differential learning rate is that participants that were confronted with a REA diagram in the first phase of the experiment might find it easier to recognize the hidden REA core pattern occurrence in the non-REA diagram they received next. It is possible that they applied the just learned REA concepts to the non-REA diagram in order to better understand it. These participants therefore score better than the participants that started with a non-REA diagram. As this effect of learning holds only for the non-REA diagram, it plays against the hypothesis $\mathsf { H } _ { \mathsf { e f f i c a c y } }$ , which was supported by the experimental results. We therefore do not consider it as a threat to the validity of our study.

Table 4. Results of Mann–Whitney U-test for effect of experimental run

<table><tr><td></td><td>Mean 1st run</td><td>Mean 2nd run</td><td>z</td><td>Significance (two-tailed)</td></tr><tr><td>Accuracy non-REA</td><td>0.51</td><td>0.64</td><td>-1.722</td><td>0.093</td></tr><tr><td>Accuracy REA</td><td>0.67</td><td>0.64</td><td>-0.420</td><td>0.697</td></tr><tr><td>Time non-REA</td><td>30.88</td><td>23.29</td><td>-3.743</td><td>&lt;0.001</td></tr><tr><td>Time REA</td><td>28.21</td><td>20.56</td><td>-3.457</td><td>&lt;0.001</td></tr><tr><td>Normalized accuracy non-REA</td><td>0.02</td><td>0.03</td><td>-3.413</td><td>0.001</td></tr><tr><td>Normalized accuracy REA</td><td>0.03</td><td>0.03</td><td>-1.871</td><td>0.061</td></tr></table>

REA, Resources-Events-Agents.

Table 5. Result of Mann–Whitney U-test for differences in comprehension time before learning

<table><tr><td></td><td>Mean non-REA</td><td>Mean REA</td><td>z</td><td>Significance (two-tailed)</td></tr><tr><td>Time</td><td>30.88</td><td>28.21</td><td>-1.719</td><td>0.086</td></tr></table>

REA, Resources-Events-Agents

Table 6. Result of Mann–Whitney U-test for differences in comprehension time after learning

<table><tr><td></td><td>Mean non-REA</td><td>Mean REA</td><td>z</td><td>Significance (two-tailed)</td></tr><tr><td>Time</td><td>23.29</td><td>20.56</td><td>-1.209</td><td>0.227</td></tr></table>

REA, Resources-Events-Agents

Because of the demonstration of a learning effect for comprehension time, the participants comprehension times for non-REA and REA diagrams, both before and after the learning took place, were compared. Tables 5 and 6 show test results, respectively, before learning (taking into account only the observations of the first run) and after learning (using only the observations obtained in the second run). Similar results were found as in the within-groups analysis with counterbalancing (i.e. hypothesis $\mathsf { H } _ { \mathsf { e f f i c i e n c y } }$ is not supported).

Similar analyses were carried out to investigate possible differences in understanding caused by the financing process modelled. Here only one significant difference in performance was found between the diagrams for debt financing and equity financing. It took significantly more time to understand the non-REA diagram of the debt financing process than the non-REA diagram of the equity financing process $( \mathsf { M e a n } _ { \mathsf { d e b t } } = 2 9 . 4 0$ $\mathsf { M e a n } _ { \mathsf { e q u i t y } } = 2 5 . 2 7$ , Mann–Whitney U-test: $Z = - 2 . 1 4 9$ , significance: $P < 0 . 0 3 2 )$ . As the results of the other five tests were not significant, it is unlikely that the debt financing process is inherently less comprehensible than the equity financing process.

## SUMMARY AND DISCUSSION

Investigating the effectiveness and efficiency of conceptual modelling grammars is identified as a major information systems research opportunity by Wand & Weber (2002). Their literature review did not identify studies that investigate or compare the use of patterns in conceptua modelling. According to Batra (2005), work in this area has just started.

This paper reported upon an empirical study that evaluated REA modelling, which is a pattern-driven approach to enterprise information modelling that is increasingly being adopted in internationally developed methodologies and frameworks for modelling e-business collaborations and as a proposed theoretical foundation for ERP systems. The research question addressed was whether conceptual schemes of business processes, in the form of ER diagrams, have a higher pragmatic quality when the REA approach was used to develop them. The concept of pragmatic quality was taken from Lindland et al.’s (1994) framework for conceptual schema quality, and refers to how well schemas are understood by their users. The users that we envisioned in our study were business users such as accountants, auditors and business analysts.

To investigate the research question, a laboratory experiment with graduate business stu dents was conducted to assess and compare their understanding of REA diagrams with that of non-REA diagrams. A REA diagram was defined as an ER diagram that is obtained through the use of the Basic REA Template. The outcome of the experiment indicates that the comprehension of a REA diagram is better in the sense that it is more accurate. Our study suggests that business users acquire a more accurate understanding of the business processes and pol icies modelled when they recognize the REA core pattern in the conceptual schema. The study could not show that REA diagrams are faster understood than non-REA diagrams. On the other hand, the normalized accuracy measurements point out that the better user understanding with REA diagrams is not offset by spending more time in understanding the diagrams. This result indicates overall efficacy of REA modelling with respect to the user comprehension of diagrammatic conceptual schemas of business processes.

The scientific contributions of our work are: (1) the gathering of empirical evidence to substantiate previously made (but not empirically demonstrated) claims about the understandabil ity of REA diagrams; (2) the demonstration of benefits (i.e. improved user comprehension) related to the use of conceptual modelling patterns (as exemplified by the REA core pattern).

The practical implication of our research results is that they support the REA modelling of business processes as well as the use of modelling methodologies such as UMM and ECIMF that have adopted major ontological constructs of the REA model. We showed that the use of the REA core pattern increases the pragmatic quality of conceptual schemas, meaning that the users’ interpretation of the domain semantics conveyed by the schemas is closer to what was intended by the system analysts. In a system development context, the improved analyst–user communication helps ensuring the success of the requirements validation task. Users that accurately understand the conceptual schemas produced by the system analysts can also better detect incompleteness and invalidity in the requirements specification (Lindland et al., 1994). The higher pragmatic quality of REA-modelled conceptual schemas thus has a ripple effect on the quality of the end product (i.e. the enterprise information system) (Siau & Tan, 2005b).

## Limitations

The average completion time of the comprehension task was about 10% lower with the REA diagrams. However, this difference was not statistically significant. As commented before, the statistical power of the test of the efficiency hypothesis was low, which might explain the lack of support for $\mathsf { H } _ { \mathsf { e f f i c i e n c y } } .$ Another limitation for the evaluation of the hypothesized efficiency of user comprehension were the operational procedures of the experiment. Students were moti vated to perform well by the promise of course credits. However, they were told that they would be evaluated based on their scores, not on how fast they finished the tasks. With hindsight, we could have told the students that both accuracy and time would be used to determine their task performance (in order to gain credits). The reason for not putting them under time pressure was our primary focus on the evaluation of the effectiveness variable (which we considered more important). The use of the efficacy variable guarantees a balanced approach towards the evaluation of the effectiveness and efficiency dimensions of user comprehension, even if (some) students make trade-offs (like sacrificing correctness of answers for speed of answering).

We are also aware that the constraint of comparing informationally equivalent diagrammatic representations did not allow testing the full strength of the REA model. The evaluation was based on the assumption of a passive use of the diagrams, as can be expected from business users that are not actively engaged in the modelling process (as information analysts or system developers would be (Kim & March, 1995)). To test if any pragmatic quality effects on business users would result from the use of the Basic REA Template, the diagrams that were compared had to have the same information content, hence the requirement of information equivalence. To ensure information equivalence, the differences imputed were restricted to the removal of the economic duality relationship (by reifying it) and a physical rearrangement of entities and relationships (based on a left-hand turn of the diagram layout). Because we jointly applied both modifications, we cannot tell whether only one of them, or both, caused the higher accuracy o comprehension observed with the REA diagrams. Also, we cannot rule out that another operationalization of the concept of non-REA diagram would lead to different results. On the other hand, we believe that the applied modifications were effective in hiding the essence of the ontological and spatial structure of the REA core pattern occurrence in the non-REA diagrams, while satisfying the information equivalence constraint for a fair comparison of the treatments.

The experimental materials used also limit the external validity of the study results. To investigate the proposition, relatively small and simple conceptual schemas were used, that portrayed only the transactional core of the business processes modelled. The REA core transaction pattern does not fit other business process elements such as commitment events, instigation events, reversal events and type-level policies (see Dunn et al. (2005) for examples). Therefore, the REA and non-REA treatments as defined here (i.e. relative to the evaluation of the REA model’s core pattern) cannot be compared with respect to the user comprehension of conceptual schema elements that fall outside the scope of the REA core pattern. Since conceptual modelling techniques should be evaluated according to the purpose they serve (Parsons & Cole, 2005), the schemas used directed the attention of the study participants towards the transactional core of the business process. Consequently, we do not extend our conclusion (i.e. more accurate user comprehension with schemas showing a REA core pattern occurrence) to conceptual schemas that are not centred around an economic exchange or conversion process. Neither does our conclusion hold for schemas that contain much more elements than just the transactional core of the process (as in that case the beneficial effect of the REA core pattern occurrence on overall user comprehension might be marginal).

Finally, we wish to note that the experimental participants studied first the ER modelling formalism and next the REA model. We are aware of the danger of an order of learning effect tha might explain why the experiment, organized at the end of the course, showed a better comprehension of the REA diagrams. We wish to note that conceptual schemas developed according to the REA model must be represented in some format. Of course, students could have been introduced first to the REA model, making them familiar with other representation formats (e.g. UML class diagrams), before teaching them how to represent a REA schema as an ER diagram. However, to date the ER model is the most frequently used representation format for REA schemas, so teaching them first the ER model was a deliberate choice.

Another option was to teach the REA model to only part of the students participating in the experiment. The spatial structuring of the elements in the REA diagram (as a result of the use of the Basic REA Template) could perhaps be beneficial to the schema understanding of users having no prior experience or training in REA modelling. But on the other hand, it is hard to see how the REA core pattern could contribute towards a better understanding if users have no knowledge of the ontological elements of the REA model. The cognitive theories reviewed imply that for a pattern to be recognized, it needs to be present in long-term memory. There fore, knowledge of the REA model was essential for testing our proposition.

## Lessons learned and future research

In this experiment, the evaluation of the pragmatic quality of REA diagrams was done using performance-based measures. One lesson learned is that participants need to be motivated to complete their tasks as accurately and quickly as possible to evaluate simultaneously the effectiveness and efficiency dimensions of user comprehension. Future experiments with sufficient power (e.g. taking the currently observed effect size for comprehension time as the expected effect size to calculate the required number of participants) might then indicate whether the currently observed non-significant finding for $\mathsf { H } _ { \mathsf { e f f i c i e n c y } }$ was due to a low power leve or whether the efficiency effect is, in reality, negligible. Student approaches to test taking are, however, hard to control by the experimenter. Another option is to use perception-based mea surements (e.g. ease of use, user information satisfaction), which may provide a complementary perspective on pragmatic quality. This is the question of computational equivalence (Larkin & Simon, 1987). Even if two schemas are informationally equivalent, inferences might be drawn easier and quicker from the information that is explicitly presented in one of them, meaning that this schema might be easier to use than the other (Gemino & Wand, 2003). According to Siau (2004), computational equivalence is a valuable measure for comparing the efficiency of modelling methods from the same paradigm, which provides an interesting perspective fo the evaluation of REA modelling (and pattern-driven modelling approaches in general).

A systematic evaluation of the REA model also requires the evaluation of other quality prop erties, in particular the semantic quality of REA diagrams. Does the use of the REA model result in conceptual schemas that are more valid and/or complete with respect to the problem domain modelled? Such an evaluation effort can be undertaken in the context of a schema cre ation task, where the pattern-driven approach promoted by REA modelling is contrasted against the use of other approaches (or no defined approach at all).<sup>7</sup> It could also be examined whether participants perform differently, before and after they receive training in REA modelling.

It should also be noted that the REA model, as it is referred to in e-business system modelling methodologies such as UMM and ECIMF, is an updated and extended version of the original model published in McCarthy (1982). Additional modelling patterns have been proposed for a more complete (and not exclusively accountability- and control-oriented) description of business processes (Geerts & McCarthy, unpublished). Further research is needed to investigate the effect of using these new patterns on the quality of resultant schemas.

## REFERENCES

Anderson, J.R. (1996) The Architecture of Cognition. Har vard University Press, Cambridge, MA, USA.

Antony, S. & Mellarkod, V. (2004) A methodology for using data-modeling patterns. In: Proceedings of the Third Annual Symposium on Research in Systems Analysis and Design. St. John’s, NF, Canada.

Batra, D. (2005) Conceptual data modeling patterns: representation and validation. Journal of Database Man agement, 16, 84–106.

Batra, D. & Wang, T.W. (2004) A research agenda for eval uating and improving data modeling patterns. In: Proceedings of the Third Annual Symposium on Research in Systems Analysis and Design. St. John’s, NF, Canada.

Bodart, F., Patel, A., Sim, M. & Weber, R. (2001) Should optional properties be used in conceptual modelling? A theory and three empirical tests. Information Systems Research, 12, 384–405.

Burton-Jones, A. & Weber, R. (2003) Properties do not have properties: investigating a questionable conceptua modeling practice. In: Proceedings of the Second Annual Symposium on Research in Systems Analysis and Design. Miami, FL, USA.

Burton-Jones, A., Storey, V.C., Sugumaran, V. & Ahluwa lia, P. (2005) A semiotic metrics suite for assessing qual ity of ontologies. Data and Knowledge Engineering, 55, 84–102.

Chen, P. (1976) The Entity-Relationship model: toward a unified view of data. ACM Transactions on Database Systems, 1, 9–36.

Cohen, J. (1988) Statistical Power Analysis for the Behav ioral Sciences. Erlbaum, Hillsdale, NJ, USA.

David, J.D., Dunn, C.L. & McCarthy, W.E. (1999) Enter prise resource planning systems research: the necessity of explicating and examining patterns in symbolic form.

In: Proceedings of the First International Workshop on Enterprise Management, Resource Planning Systems: Methods, Tools and Architecture. Venice, Italy.

Dunn, C.L. & Gerard, G.J. (2001) Auditor efficiency and effectiveness with diagrammatic and linguistic con ceptual model representations. International Journal o Accounting Information Systems, 2, 223–248.

Dunn, C.L. & Grabski, S.V. (2000) Perceived semantic expressiveness of accounting systems and task accu racy effects. International Journal of Accounting Infor mation Systems, 1, 79–87.

Dunn, C.L. & Grabski, S.V. (2001) An investigation of local ization as an element of cognitive fit in accounting mode representations. Decision Sciences, 32, 55–94.

Dunn, C.L. & McCarthy, W.E. (1997) The REA accountin model: intellectual heritage and prospects for progress. Journal of Information Systems, 11, 31–51.

Dunn, C.L., Cherrington, J.O. & Hollander, A.S. (2005) Enterprise Information Systems. A Pattern-Based Ap proach, 3rd edn. McGraw-Hill, New York, NY, USA.

Fowler, M. (1997) Analysis Patterns: Reusable Objec Models. Addison-Wesley, Workingham, UK.

Gemino, A. & Wand, Y. (2003) Foundations for empirica comparisons of conceptual modeling techniques. In: Proceedings of the Second Annual Symposium on Research in Systems Analysis and Design. Miami, FL, USA.

Gentner, D. & Medina, J. (1998) Similarity and the devel opment of rules. Cognition, 65, 263–297.

Harwell, M.R. (1988) Choosing between parametric and nonparametric tests. Journal of Counseling and Devel opment, 67, 35–38.

Hay, D.C. (1996) Data Model Patterns: Conventions of Thought. Dorset House Publishing, New York.

Kesh, S. (1995) Evaluating the quality of entity relationship models. Information and Software Technology, 37, 681– 689.

Kim, Y. & March, S.T. (1995) Comparing data modeling formalisms. Communications of the ACM, 38, 103–115.

Kitchenham, B. & Linkman, S. (2005) Experiences of using an evaluation framework. Information and Software Technology, 47, 761–774.

Krogstie, J., Lindland, O.I. & Sindre, G. (1995) Defining quality aspects for conceptual models. In: Proceedings of the 3rd IFIP8.1 Working Conference on Information Systems, pp. 216–231. Marburg, Germany.

Larkin, J. & Simon, H. (1987) Why a diagram is (sometimes) worth ten thousands words. Cognitive Science, 11, 65–99.

Lindland, O.I., Sindre, G. & Sølvberg, A. (1994) Understanding quality in conceptual modeling. IEEE Software, 11, 42–49.

McCarthy, W.E. (1982) The REA accounting model: a generalized framework for accounting systems in a shared data environment. The Accounting Review, 57, 554– 578.

McCarthy, W.E. (1999) Semantic modeling in accounting education, practice, and research: some progress and impediments. In: Conceptual Modeling: Current Issues and Future Directions, Akoka, J., Kangassalo, H. & Thalheim, B. (eds), pp. 144–153. Springer-Verlag, Berlin.

McCarthy, W.E. (2003) The REA modeling approach to teaching accounting information systems. Issues in Accounting Education, 18, 427–441.

McCarthy, W.E. (2004) The evolution toward REA accountability infrastructures for enterprise systems. Keynote Speech 1st International Conference on Enterprise Systems and Accounting (Icesacc’04), Thessaloniki, Greece.

March, S.T. & Smith, G.F. (1995) Design and natural science research on information technology. Decision Support Systems, 15, 251–266.

Moody, D.L. (2001) Dealing with complexity: a practical method for representing large entity relationship models. PhD Dissertation. Department of Information Systems, University of Melbourne.

Moody, D.L. & Shanks, G. (2003) Improving the quality of data models: empirical validation of a quality management framework. Information Systems, 28, 619– 650.

O’Leary, D.E. (2000) Different firms, different ontologies, and no one best ontology. IEEE Intelligent Systems, September/October, 72–78.

O’Leary, D.E. (2004) On the relationship between REA and SAP. International Journal of Accounting Informa tion Systems, 5, 65–81.

Parker, R.K., Trimmer, K. & LeRouge, C. (2005) The REA ontology to supplement teaching data flow diagrams. In: Proceedings of the Americas Conference on Information Systems (AMCIS’05). Omaha, NE, USA.

Parsons, J. (2003) Effects of local versus global schema diagrams on verification and communication in concep tual data modeling. Journal of Management Information Systems, 19, 155–183.

Parsons, J. & Cole, L. (2005) What do the pictures mean? Guidelines for experimental evaluation of representation fidelity in diagrammatical conceptual modeling techniques. Data and Knowledge Engineering, 55, 327– 342.

Poels, G., Nelson, J., Genero, M. & Piattini, M. (2003) Quality in conceptual modeling. New research directions. Lecture Notes in Computer Science, 2784, 243– 250.

Pohl, K. (1994) The three dimensions of requirements engineering: a framework and its applications. Information Systems, 19, 243–258.

Price, R. & Shanks, G. (2005) A semiotic information qual ity framework: development and comparative analysis. Journal of Information Technology, 20, 88–102.

Romney, M.B. & Steinbart, P.J. (2006) Accounting Information Systems, 10th edn. Pearson Education International, Upper Saddle River, NJ.

Schütte, R. & Rotthowe, T. (1998) The guidelines of modeling – an approach to enhance the quality in information models. Lecture Notes in Computer Science, 1507, 240–254.

Shoval, P., Danoch, R. & Balaban, M. (2002) Hierarchical ER diagrams (HERD) – the method and experimenta evaluation. Lecture Notes in Computer Science, 2784, 264–274.

Siau, K. (1999) Information modeling and method engi neering: a psychological perspective. Journal of Database Management, 10, 44–50.

Siau, K. (2004) Informational and computational equiva lence in comparing information modeling methods. Journal of Database Management, 15, 73–86.

Siau, K. & Tan, X. (2005a) Technical communication in information systems development: the use of cognitive mapping. IEEE Transactions on Professional Communication, 48, 269–284.

Siau, K. & Tan, X. (2005b) Improving the quality of conceptual modeling using cognitive mapping techniques. Data and Knowledge Engineering, 55, 343–365.

Siau, K., Wand, Y. & Benbasat, I. (1997) The relative importance of structural constraints and surface seman tics in information modeling. Information Systems, 22, 155–170.

Summers, S.L. (2000) Discussion of perceived semantic expressiveness of accounting systems and task accuracy effects. International Journal of Accounting Information Systems, 1, 88–90.

Tanizaki, H. (1997) Power comparison of non-parametric tests: small-sample properties from Monte Carlo exper iments. Journal of Applied Statistics, 45, 603–632.

Topi, H. & Ramesh, V. (2002) Human factors research on data modeling: a review of prior research, an extended framework and future research directions. Journal of Database Management, 13, 3–19.

UN/CEFACT (2003) UN/CEFACT Modeling Methodology (UMM) User Guide. Technical report CEFACT/TMG N093.

Wand, Y. & Weber, R. (2002) Information systems and conceptual modeling: a research agenda. Information Systems Research, 13, 363–376.

## Biographies

Geert Poels is a Professor with the rank of Lecturer at the Department of Management Information, Operations Management and Technology Policy of Ghent University (Bel gium). He holds degrees in Business Engineering and Computer Science, and a PhD in Applied Economic Sciences. His research interests include software metrics, conceptual modelling and accounting information systems. Dr Poels has published in IEEE Transactions on Software Engineering, Data & Knowledge Engineering, Software and Systems Modelling, Information and Software Tech nology, and Lecture Notes in Computer Science, and pre sented at conferences such as ER & CAiSE. In 2002, 2003, 2006 and 2007, he co-organized the IWCMQ/QoIS workshops on conceptual model and information system quality at the ER conference.

Ann Maes is a Teaching Assistant at the Faculty of Eco nomics and Business Administration of Ghent University. She received her degree in Applied Economics in 2002. Her research interests include conceptual modelling and human–computer interaction. Mrs Maes has published in Lecture Notes in Computer Science and her research was presented at the ER conference and at symposia such as the International Research Symposium on Accounting Information Systems (IRSAIS) and the Annual Pre-ICIS Workshop on Human–Computer Interaction Research in Management Information Systems (HCI/MIS).

Frederik Gailly is a doctoral candidate at the Depart ment of Management Information, Operations Manage ment and Technology Policy of Ghent University. He holds degrees in Applied Economics (2001) and Applied Com puter Science (2007). His research interests include conceptual modelling, business domain ontologies and semantic web technologies. His doctoral research con cerns the representation, formalization and operationa lization of business domain ontologies. Mr Gailly has published in Lecture Notes in Computer Science. He pre sented at the International Conferences on Business Information Systems (BIS) and Enterprise Systems and Accounting (ICESAcc) and at workshops organized within the International Semantic Web and CAiSE conferences.

Roland Paemeleire is a Full Professor at the Faculty o Economics and Business Administration of Ghent Univer sity. He is President of the Department of Managemen Information, Operations Management and Technology Policy. He received his PhD from Ghent University, spe cializing in Economic Sciences. He studied Compute Auditing at the University of Toronto and was Visiting Research Scholar at Stanford University and Harvard Uni versity. He is the founder and Chief-Editor of ‘Kwar taalschrift Accountancy en Bedrijfskunde’ (Kluwer). Fo the past 5 vears he served as Dean of the Faculty o Economics and Business Administration. His main research interests are Management Accounting, Auditing, Budgeting, Management Information Systems and Accounting Information Systems.

## APPENDIX A

The experimental objects used in the study are shown in Figures A1–A4.

![](/api/attachments/QVJEWBME/fulltext/images/fe13d89065206385631e51b0730e10b34823f56732bbf2ac91d1933d1e641173.jpg)  
Figure A1. REA diagram equity financing.

![](/api/attachments/QVJEWBME/fulltext/images/09165dd9989a0bc272b4bbc430d1c09bd065394081e7a596fe10de585b9cad85.jpg)  
Figure A2. Non-REA diagram equity financing.

![](/api/attachments/QVJEWBME/fulltext/images/7c005b125e1c1525576d5bdd07ab59ec40c42896a4473153774ba1c6f1d6ce1d.jpg)  
Figure A3. REA diagram debt financing.

![](/api/attachments/QVJEWBME/fulltext/images/49757a41aeb3c41595551ee7afcf6e803d717a2fcf0e0a531a8ac88d925c6d51.jpg)  
Figure A4. Non-REA diagram debt financing

## APPENDIX B

List of comprehension questions for the equity financing business process diagrams:

• What transaction or business cycle is modelled in the diagram?

• What give-to-get relationship is modelled in the diagram?

• List the events in the value cycle that is modelled in the diagram.

• List the positions in the value cycle that is modelled in the diagram.

• Is there a dividend payment for each stock issuance?

• What entity type plays a central role when integrating this diagram with other diagrams representing other business or transaction cycles?

• Do the structural constraint(s) on the relationships between stock issuance and dividend payments reflect common business practices?

• Is the business or transaction cycle that is modelled in the diagram complete in the sense that for every business activity there is an employee that can be hold accountable?

• Is the business or transaction cycle that is modelled in the diagram complete in the sense that for every business activity there is an outside (or external) party?

• Is the business or transaction cycle that is modelled in the diagram complete in the sense that for every business activity there is at least one asset (i.e. something with economic value to the company) that is affected by the activity?

• Identify (types of) transactions for which the economic dual (type of) transaction is not mod elled in the diagram?

• Is the conceptual model that is depicted in the diagram correct given that in reality each div idend payment transaction relates to exactly one stock issuance?

List of comprehension questions for the debt financing business process diagrams:

• What transaction or business cycle is modelled in the diagram?

• What give-to-get relationship is modelled in the diagram?

• List the events in the value cycle that is modelled in the diagram

• List the positions in the value cycle that is modelled in the diagram

• Is there a loan repayment for each acquisition of capital?

• What entity type plays a central role when integrating this diagram with other diagrams representing other business or transaction cycles?

• Do the structural constraint(s) on the relationships between capital acquisitions and loan repayments reflect common business practices?

• Is the business or transaction cycle that is modelled in the diagram complete in the sense that for every business activity there is an employee that can be hold accountable?

• Is the business or transaction cycle that is modelled in the diagram complete in the sense that for every business activity there is an outside (or external) party?

• Is the business or transaction cycle that is modelled in the diagram complete in the sense that for every business activity there is at least one asset (i.e. something with economic value to the company) that is affected by the activity?

• Identify (types of) transactions for which the economic dual (type of) transaction is not mod elled in the diagram?

• Is the conceptual model that is depicted in the diagram correct given that in reality each loan repayment transaction may relate to several capital acquisitions?
