---
otero_id: 26477
otero_key: "PPDDN3JA"
title: "Research Commentary: Information Systems and Conceptual Modeling—A Research Agenda"
authors: "Yair Wand; Ron Weber"
year: "2002"
journal: "Information Systems Research"
doi: "10.1287/isre.13.4.363.69"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/PPDDN3JA/fulltext/images/1727484480c60ebf049371c6b89d9f51b2920d34a8324648084880f339459de8.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Commentary: Information Systems and Conceptual Modeling—A Research Agenda

Yair Wand, Ron Weber,

To cite this article:

Yair Wand, Ron Weber, (2002) Research Commentary: Information Systems and Conceptual Modeling—A Research Agenda. Information Systems Research 13(4):363-376. http://dx.doi.org/10.1287/isre.13.4.363.69

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2002 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/PPDDN3JA/fulltext/images/442c6ddf20afdf24fd39949c4e695bb05960e514e368c81d30de5b9f144887e4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Commentary: Information Systems and Conceptual Modeling— A Research Agenda

Yair Wand • Ron Weber

Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, Canada V6T 1Z2 Faculty of Business, Economics, and Law, The University of Queensland, Australia 4072 yair.wand@ubc.ca • weber@commerce.uq.edu.au

W ithin the information systems field, the task of conceptual modeling involves building a representation of selected phenomena in some domain. High-quality conceptualmodeling work is important because it facilitates early detection and correction of system development errors. It also plays an increasingly important role in activities like business process reengineering and documentation of best-practice data and process models in enterprise resource planning systems. Yet little research has been undertaken on many aspects of conceptual modeling. In this paper, we propose a framework to motivate research that addresses the following fundamental question: How can we model the world to better facilitate our developing, implementing, using, and maintaining more valuable information systems? The framework comprises four elements: conceptual-modeling grammars, conceptual-modeling methods, conceptual-modeling scripts, and conceptual-modeling contexts. We provide examples of the types of research that have already been undertaken on each element and illustrate research opportunities that exist.

(Conceptual Modeling; Information Systems Development; Ontology)

## 1. Introduction

The requirements analysis phase that occurs during information systems development often involves use of models called conceptual models. These models, which are mostly graphic, are used to represent both static phenomena (e.g., things and their properties) and dynamic phenomena (e.g., events and processes) in some domain. They have at least four purposes: (1) supporting communication between developers and users, (2) helping analysts understand a domain, (3) providing input for the design process, and (4) documenting the original requirements for future reference (Kung and Solvberg 1986).

The importance of conceptual modeling was understood as early as the mid to late 1960s. Information systems developers recognized that faulty requirements analysis was a major reason for project failure. They believed, therefore, that benefits would accrue from using a formal approach to eliciting and articulating user requirements. They recognized, also, that the cost of fixing errors grows exponentially as a function of elapsed time to discovery (Moody 1998). Potentially, high-quality conceptual modeling would enable early detection and correction of errors.

Faulty requirements analysis still remains a major problem during systems development (Standish Group 1995). In this paper, therefore, we seek to motivate research addressing the following fundamental question: How can we model the world to better facilitate our developing, implementing, using, and maintaining more valuable information systems? Our goal is to identify research topics that address this question and to structure them in such a way that a compelling research agenda unfolds.

In the sections below, we first provide some background and motivation. Next, we articulate a framework for research on conceptual modeling that comprises four major elements. We then discuss each element in more detail and provide examples of the types of research that might be done. Finally, we present some brief conclusions.

## 2. Background and Motivation

During the 1970s and 1980s, much research was done on conceptual modeling. Most involved development of modeling techniques (e.g., Chen 1976). It was spurred mainly by substantial developments in, and rapid adoption of, database systems and systemsanalysis techniques.

During the 1990s, research on conceptual modeling languished somewhat. For several reasons, however, renewed interest in conceptual modeling research has occurred:

• the emergence of the object-oriented approach,

• the challenges faced in eliciting requirements when user cohorts are large, diffuse, and unknown (e.g., as with many business-to-consumer e-commerce systems),

• the use of data and process models for enterprise resource planning systems,

• the potential of conceptual models to assist business process reengineering,

• the desire to reuse software components by identifying reusable specifications,

• the need to understand the broader social context of system development,

• the belief that a sounder theoretical base for conceptual modeling is emerging.

Despite the importance of conceptual modeling, anecdotal and research evidence suggest that it is not done well. Practitioners report that conceptual modeling is difficult and that it often falls into disuse within their organizations. Experimental research (Batra et al. 1990, Goldstein and Storey 1990, Prietula and March 1991) and survey research (Batra and Marakas 1995, Hitchman 1995, Maier 1996) confirm these views.

## 3. A Framework for Research on Conceptual Modeling

Figure 1 presents a framework to structure the way we might think about research on conceptual modeling. The framework comprises four elements:

• A conceptual-modeling grammar provides a set of constructs and rules that show how to combine the constructs to model real-world domains. For example, the entity-relationship modeling grammar has the constructs “entity” and “relationship.” A rule in the grammar specifies that two entities can be associated only via a relationship.

• A conceptual-modeling method provides procedures by which a grammar can be used. Usually one major aspect of a method prescribes how to map observations of a domain into a model of the domain. Ideally, methods provide procedures to identify instances of all phenomena that can be modeled via a grammar.

• A conceptual-modeling script is the product of the conceptual-modeling process. For example, the scripts generated by the entity-relationship grammar are entity-relationship diagrams (ERDs). Each script is a statement in the language generated by the grammar.

• The context is the setting in which conceptual modeling occurs and scripts are used. In this paper, we focus on just three contextual factors that seem critical: (a) individual difference factors—These include stakeholders’ experience, training, and cognitive abilities; (b) tasks factors—Grammars and scripts are used for different information systems-related tasks; and (c) social agenda factors—Grammars and scripts are often used within a wider context that involves organizational change.

Figure 1 Framework for Research on Conceptual Modeling  
![](/api/attachments/PPDDN3JA/fulltext/images/887aeec573de4689d00c2633603a7b7356bd36d5c7dca6ee9368c8f41855e603.jpg)  
Information Systems Research Vol. 13, No. 4, December 2002

In the following sections, we survey some research that has been undertaken on each element of our framework and suggest opportunities for further research. Although the elements interact in important ways, we examine each individually to help structure our discussion. Our review of research is not intended to be comprehensive. We simply seek to illustrate the kinds of work that have been done and the research opportunities available.

## 4. Conceptual-Modeling Grammars

Research on conceptual-modeling grammars focuses on developing new grammars as well as understanding, evaluating, and improving existing grammars.

## 4.1. Overview of Some Existing Research

Early work on conceptual-modeling grammars focused primarily on developing new grammars (e.g., Chen 1976). The choice of constructs and rules in these grammars usually reflected their developers’ intuition and experience. In the absence of theory, new grammars began to proliferate during the 1970s and 1980s. Each was supposedly better than the rest. Many researchers became frustrated with the situation. The pejorative term, “YAMA,” arose—“Yet Another Modeling Approach” (Oei et al. 1992).

Some researchers attempted to evaluate competing grammars by comparing their similarities and differences (e.g., Olle et al. 1982, 1983, 1986). Others undertook case-study evaluations (e.g., Floyd 1986). In the absence of theory, however, it was difficult to determine whether the results were valid. In the late 1980s and early 1990s, therefore, attempts were made to establish a theoretical basis for conceptual-modeling grammars. For example, Wand and Weber (1993) proposed that conceptual-modeling grammars should be based on a theory of ontology—that is, a theory that articulates those constructs needed to describe the structure and behavior of the world in general (see also Wimmer and Wimmer 1992, Ashenhurst 1996). The ontological expressiveness of the grammar could then be evaluated by comparing its constructs against the constructs in an ontology. Such analysis might reveal several types of grammatical deficiencies:

• Construct overload—Several ontological constructs map to one grammatical construct.

• Construct redundancy—Several grammatical constructs map to one ontological construct.

• Construct excess—A grammatical construct might not map to any ontological construct.

• Construct deficit—An ontological construct might not map to any grammatical construct.

The existence of these types of deficiencies potentially undermines a grammar’s usefulness. When construct overload and redundancy exist, users may become confused about the meaning of scripts that the grammar generates. In essence, they confront problems of homonymy and synonymy (Mylopoulos 1998). Construct excess might confuse users about the nature and purposes of the excess constructs. Construct deficit might hinder a modeler’s ability to represent some real-world phenomena.

Other theoretical bases besides ontology have been used to evaluate grammars. For example, Parsons (1996) has used concept theory, Auramaki et al. (1988) have used speech-act theory, and Stamper (1987) has used semiotics. In all cases, the goal has been to anchor the grammar’s constructs and rules to theories of representation or communication.

Theoretical work has also been undertaken on the use of multiple conceptual-modeling grammars. Most grammars do not provide a sufficient set of constructs to model all phenomena in a domain. Furthermore, in most grammars certain phenomena can be modeled easier than others (see, e.g., Agarwal et al. 1999). Even if a grammar could model all phenomena equally well, the cognitive demands placed on users to generate and interpret scripts may be too high. Consequently, multiple grammars may be needed to model a domain completely. When this outcome occurs, Green (1996) argues that grammars should be chosen to achieve two criteria. First, minimum ontological overlap (MOO) is achieved when the same ontological construct cannot be represented via alternative grammars. MOO reduces the likelihood of producing conflicting domain representations. Second, maximum ontological coverage (MOC) is achieved if the grammars in combination cover all phenomena to be modeled. MOC increases the likelihood of producing complete domain representations.

The empirical work that has been undertaken so far to evaluate grammars can be categorized into three groups: between (inter-) grammar comparisons, within (intra-) grammar evaluations, and multigrammar studies examining issues of combining several grammars (Table 1). Much early work is empirical rather than theoretical (e.g., Brosey and Shneiderman 1978). For example, two different grammars were used to generate scripts for the same domain. The scripts’ effectiveness was then evaluated empirically in some way. Much of this work also confounds conceptual-modeling issues and data-modeling issues.

Later empirical work is more theory-driven and better focused on conceptual-modeling issues. For example, Gemino (1999) and Bodart et al. (2001) empirically test predictions about the effects of the optional property construct in the entity-relationship grammar. They argue that optional properties are an instance of construct excess because things in the world either possess or do not possess properties. Their empirical results show that users of conceptual models were better able to solve problems about domains if optional properties were proscribed and replaced instead by subclasses with only mandatory properties.

## 4.2. Some Future Research Opportunities

In general, future theoretical and empirical research on grammars should investigate their effectiveness or efficiency. These goals can be pursued in the context of either script creation or script interpretation tasks. Ideally, grammars allow users, with minimum resources, to (a) create a “faithful” representation of domains and (b) “faithfully” interpret representations so that the semantics of domains are understood. For creation tasks, the focus is a tangible product—the script itself. For interpretation tasks, the focus is an intangible product—the domain understanding invoked by a script. Therefore, the latter type of research is more difficult to undertake.

More specifically, however, we propose that further research on grammars can be undertaken in at least eight areas:

(1) Evaluation of ontologies. The outcomes of any evaluations of a grammar for ontological expressiveness depend on which constructs are present or absent in the ontological theory used. For various reasons, Wand and Weber have chosen Bunge’s (1977) ontological theory to evaluate grammars, but others might be used.

For example, Milton and Kazmierczak (1999) have used Chisholm’s (1996) ontology and Ashenhurst (1996) has used a hybrid of ontologies. Ultimately, the usefulness of ontologies can only be determined empirically. Two types of evaluation can be undertaken. First, ontologies can be evaluated to determine how well they account for users’ experiences with different grammars. Second, scripts generated via grammars using ontologically based modeling rules (e.g., Evermann and Wand 2001, Wand and Woo 1993) can be evaluated to determine their usefulness.

(2) Evaluation of grammars. Evaluating the ontological expressiveness of grammars provides a basis for understanding their likely strengths and weaknesses. For example, Green and Rosemann (2000) have evaluated Scheer’s (1999) Architecture of Integrated Processes, which forms the basis for the ARIS Toolset 4.1, a CASE tool with over 14,000 licences worldwide. They predict that ARIS users will encounter certain difficulties when constructing models. Similarly, Opdahl and Henderson-Sellers (1999) report their work on ontological expressiveness of OML (object modeling language) and UML (unified modeling language). Both are key grammars in current object-oriented conceptual-modeling work. They have discovered instances of construct overload, redundancy, excess, and deficit. Another example is the evaluation of ARIS and Object-Process Modeling (OPM) as a basis for analysing off-the-shelf software requirements (Soffer et al. 2001). Empirical work could now be done to determine the impacts, if any, that these deficiencies have on users of these grammars. Because a grammar’s effectiveness is evaluated via the use of scripts generated by the grammar, care must be taken in empirical tests not to confound grammar quality with script quality (see §6.2 below).

(3) Assigning real-world semantics to grammars. Grammars often are first created to support software design. Thus, their constructs represent software elements, not real-world elements. Design grammars can be extended to facilitate their use in conceptual modeling by assigning ontological meaning to the grammar’s constructs. For example, the entity-relationship grammar was developed to support database design (Chen 1976). Subsequently it has been extended to represent modeling concepts such as generalization (Teorey et al. 1986). In addition, Wand et al. (1999) have assigned ontological meaning to some of the grammar’s constructs. Similarly, UML was created to support software design. Evermann and Wand (2001) show how UML can be extended to facilitate conceptual modeling by mapping its constructs to ontological concepts.

Table 1 Categorization of Some Empirical Work on Modeling

<table><tr><td>Nature of work</td><td>Details</td><td>Authors</td></tr><tr><td>IntergrammarType of Grammars</td><td>Grammars or Constructs</td><td></td></tr><tr><td>Database models</td><td>Comparing the relational and hierarchical models</td><td>Brosey and Schneiderman (1978)</td></tr><tr><td>Semantic data models compared to data models</td><td>The entity-relationship model in various forms compared to the relational data model</td><td>Jarvenpaa and Machesky (1989) Batra et al. (1990)</td></tr><tr><td>Semantic (conceptual) modeling methods</td><td>Extended entity relationship diagrams and NIAM</td><td>Kim and March (1995)</td></tr><tr><td>Process modeling methods</td><td>Dataflow diagrams and IDEFO (Intgerated definition for functional decomposition)</td><td>Yadav et al. (1988)</td></tr><tr><td rowspan="2">Object-oriented and structured analysis methods</td><td>OOA vs DFDs</td><td>Vessey and Conger (1994) Agarwal et al. (1996) Agarwal et al. (1999) Gemino (1999)</td></tr><tr><td>OOA vs DFDs and ERDs</td><td>Gemino and Wand (2001)</td></tr><tr><td>IntragrammarGrammar</td><td>Construct Studied</td><td>Authors</td></tr><tr><td>Entity-relationship diagrams</td><td>Use of structural constraints</td><td>Siau et al. (1997)</td></tr><tr><td>Entity-relationship diagrams</td><td>Comparing the use of optional and mandatory properties</td><td>Gemino (1999) Bodart et al. (2001)</td></tr><tr><td>ERD or OOA</td><td>Alternative representations of the relationship construct</td><td>Siau et al. (1995)</td></tr><tr><td>MultigrammarPurpose of Study</td><td>What was examined</td><td></td></tr><tr><td>How users combine grammars</td><td>CASE tools</td><td>Green (1996)</td></tr><tr><td>Use of multiple diagrams</td><td>Object-oriented diagrams (OMT and UML)</td><td>Kim et al. (2000)</td></tr></table>

Based on a table in Gemino and Wand (2001).

(4) Better use of grammars. When a grammar’s constructs are mapped to ontological constructs, improved ways of using the grammar to model realworld phenomena may become apparent (e.g., Wand and Woo 1993). Rules can be devised to guide the modeling process. For example, the entity-relationship grammar can be used to represent the same fact via different constructs. Ontologically based rules provide more precise guidance on which construct should be used under particular circumstances (Wand et al. 1999).

(5) Study of ontological issues. A number of important ontological problems that have implications for the design of conceptual-modeling grammars still must be solved. For example, the meronymic (part-of) relation is an important real-world phenomenon that often needs to be modeled (e.g., in a bill-of-materials application). Supposedly, part-of relations are transitive, irreflexive, and antisymmetical (Varzi 1996). Winston et al. (1987) argue that different types of meronymic relations must be recognized, however, and that not all support transitivity. To the best of our knowledge, no conceptual-modeling grammar exists that provides different constructs to model the different types of meronymic relations, nor rules to prevent their use in ways that lead to apparent intransitivity (see also Artale et al. 1996).

(6) Empirical testing of theoretical predictions and rules. Substantial work needs to be done to test predictions made about the strengths and weaknesses of grammars based on their ontological expressiveness. For example, Weber (1997, pp. 103–130) identifies instances of construct overload, redundancy, excess, and deficit that exist in the entity-relationship grammar. Little research has been conducted, however, to evaluate their effects on users of conceptual models (as opposed to database models) produced by the grammar. Similarly, the usefulness of ontologically based modeling rules needs to be tested. How such research should be designed and conducted is still unclear. Research results obtained with the “toy” conceptual models sometimes used in experiments may not generalize to practice. Undertaking empirical work in more realistic settings, however, involves substantial difficulties. The psychological models that should be used to evaluate the effects of a grammar’s strengths and weaknesses on users are also unclear. Several have been tried with mixed success: Norman’s (1986) theory of action (Gemino 1999), Hutchins et al.’s (1985) notion of semantic distance (e.g., Batra et al. 1990, Siau 1996), Newell and Simon’s (1972) ideas of cognitive fit (Agarwal et al. 1996, 1999), Larkin and Simon’s (1987) concepts of informational and computational equivalence (Agarwal et al. 1999, Kim et al. 2000, Siau 1996), Anderson’s (1983, 1995) models of cognition (Siau 1996), and Mayer’s (1989) theory of learning (Bodart et al. 2001, Gemino 1999).

(7) Use of multiple grammars. Research needs to be undertaken to investigate the impact of using combinations of grammars to provide representations of a domain. Following Green (1996), ontological theories can be used to predict which combinations of grammars best support users. These predictions can then be tested empirically. Other approaches might be used, however. For example, Kim et al. (2000) use theories of diagrammatic reasoning (Larkin and Simon 1987) to predict which combinations of object-modeling grammars generate scripts that best support users.

(8) Implications of grammar deficiencies. As discussed above, construct deficit and overload can reduce the effectiveness of a grammar. For example, Wand and Weber (1995) argue that the entity-relationship grammar lacks constructs to support system decompositions. The impact of such deficiencies needs to be tested empirically.

## 5. Conceptual-Modeling Methods

While grammars provide ways to model real-world phenomena, users still need to know the method of applying the grammar. Creating a faithful representation with a grammar entails two activities: identifying the phenomena to be modeled and mapping the phenomena into the grammar’s constructs. Often grammars are well formalized, but their creators provide neither a detailed nor unambiguous way of using them (UML is one example). For this reason, research on modeling methods focuses on developing new methods of using grammars as well as understanding, evaluating, and improving existing methods.

## 5.1. Overview of Some Existing Research

Script creation via a grammar has technical and behavioral aspects. Technically, stakeholders must be able to identify and classify different phenomena if they are to be able to create scripts that faithfully describe their domain of concern. They must also be able to model these phenomena accurately and completely using appropriate grammatical constructs. Thus, researchers have sought to show stakeholders how to identify and model:

• things, objects, entities, and properties/attributes (e.g., Wand and Woo 1993);

• classes and class structures (e.g., Parsons 1996);

• couplings/interactions and mutual properties/ relationships (e.g., Wand et al. 1999);

• meronymic or part-of relationships (e.g., Storey 1991, Opdahl et al. 2001);

• decompositions and level structures (e.g., Paulson and Wand 1992);

• events, processes, and workflows (e.g., Curtis et al. 1992, Basu and Blanning 2000, van der Aalst et al. 2000).

Behaviorally, stakeholders must be able to elicit knowledge about a domain and to conceive of this knowledge in ways that allow it to be described via a grammar. Values and beliefs about how conceptual modeling works should be done underpin conceptualmodeling methods. A method may make explicit or implicit assumptions about how stakeholders interpret phenomena in the world (epistemological assumptions). These assumptions, in turn, affect how knowledge is elicited using the method.

Some researchers have articulated explicitly the values and beliefs that underlie the conceptual-modeling methods they have developed. For example, in his Soft Systems Methodology (SSM), Checkland (1981) has the stakeholders in a system formulate “root definitions” and draw “rich pictures” of “human activity systems.” These models help stakeholders learn about their domain and help them to decide on a model that will form the basis of an implemented information system (Doyle et al. 1993). Thus, conceptual-modeling activities in SSM are founded on subjectivist, sense-making values and beliefs.

Hirschheim et al. (1995) provide an extensive account of the values and beliefs that either explicitly or implicitly underlie conceptual-modeling methods. They classify methods into two schools: (a) fact based—This school assumes conceptual models are based on objective facts, and (b) rule based—This school assumes conceptual models are based on socially constructed views of the world.

## 5.2. Some Future Research Opportunities

We propose that further research on conceptualmodeling methods can be undertaken in at least four areas:

(1) Performance of alternative methods. A method must enable stakeholders to elicit knowledge about a domain and to conceive this knowledge so it can be described via a grammar. The effectiveness and efficiency of a method in accomplishing this task is an important issue for empirical research.

(2) Methods to identify types of phenomena. A critical task in conceptual modeling is the identification of relevant phenomena in the modeled domain. To illustrate the problem, consider interaction. How can stakeholders in a conceptual-modeling process identify all relevant interactions in a domain? Some researchers suggest speech act theory as a basis for identifying relevant interactions (Winograd and Flores 1987, Wand et al. 1995). Speech act theory analyzes human communicative acts—acts whereby one person communicates meaning to another person and/or seeks to evoke an action/event in another person (Searle 1969). Two things engaged in “communicative” acts, however, might also be machines or software agents. Thus, speech act theory appears to hold promise as a means of identifying interactions.

(3) Methods to classify phenomena. Stakeholders must also classify relevant phenomena in the modeled domain. To illustrate the problem of classifying phenomena, consider the constructs of “things” and “properties of things.” Determining whether a certain phenomenon should be designated as a thing or a property is often difficult. For example, should the color “red” be modeled as a thing with properties (e.g, hue) or a property of some other thing (e.g., a car)? Some researchers adopt a relativist viewpoint. They argue that users should be allowed to choose which construct to use (e.g., Halpin 1995). Others assert that a phenomenon must be either a thing or a property of a thing—it cannot be both (Weber 1996). Researchers who adopt this latter stance need to provide guidance to practitioners, therefore, on how to distinguish things from properties of things (e.g., Wand and Woo 1993).

(4) The effects of values and beliefs. As Hirschheim et al. (1995) point out, in many cases we are only just beginning to understand the nature and implications of the values and beliefs that underlie different conceptual-modeling methods. We know little about how well stakeholders assimilate these values and beliefs into their actions or the impact on their conceptual-modeling work. Much scope exists for further theoretical and empirical work.

## 6. Conceptual-Modeling Scripts

Research on conceptual-modeling scripts focuses on determining those properties of scripts that facilitate or inhibit the tasks that the scripts are intended to support. The grammar that generates the scripts is taken as “given.” The goal is to determine how to produce the “best” scripts via the grammar.

6.1. Overview of Some Existing Research Recall that conceptual-modeling scripts are the “sentences” generated by conceptual-modeling grammars.

Like sentences in spoken English, the same information may be conveyed in different ways. Research on scripts is akin to investigating whether certain properties of English sentences facilitate or inhibit comprehension of real-world phenomena among English speakers. For example, a sentence framed in the passive voice often communicates less well than a sentence framed in the active voice, even though both capture the same semantics.

There is a paucity of research on conceptualmodeling scripts. Perhaps the closest related work focuses on metrics for evaluating the quality of conceptual models. For example, Moody and Shanks (1998) propose a number of “quality factors” to evaluate conceptual models—completeness, integrity, feasibility, understandability, correctness, simplicity, integration, and implementability. Lindland et al. (1994) evaluate conceptual models using three bases: (a) syntactic quality—the extent to which the model conforms to the rules of the modeling grammar; (b) semantic quality— the extent to which the model provides a valid and complete representation of a domain; and (c) pragmatic quality—the extent to which users can comprehend the model. Kesh (1995) proposes another set of quality factors based on “behavior” (usability, maintainability, accuracy, performance) and “ontology” (suitability, soundness, consistency, conciseness, completeness, cohesiveness, validity).

One problem with the above research is that the different lists of quality factors need to be reconciled. A second problem is that the research confounds scriptquality factors with (a) the process of generating a conceptual model and (b) the capabilities of the conceptual-modeling grammar used. Nonetheless, the research follows the approach we advocate—namely, to first identify the properties of scripts that might impact users and then to theorize about these properties. In addition, consistent with prior quality research, the research recognizes that different properties of scripts may become more or less salient depending on the task and stakeholder involved.

## 6.2. Some Future Research Opportunities

A script might not be effective for two reasons. First, it might not be a good representation of the script creator’s conception of the phenomena to be modeled.

Second, a “reader” of the script might not be able to create a “correct” conception of the phenomena the script is intended to convey. These two reasons match Norman’s (1986) “Gulf of Execution” and “Gulf of Evaluation.” These gulfs arise due to complex interactions between the grammar’s characteristics, the task requirements, the script creator’s characteristics (e,g., modeling experience and cognitive abilities), and the script interpreter’s characteristics (e.g., prior exposure to conceptual models). The study of such gulfs forms one basis for future research on scripts.

More specifically, however, we propose that future research on scripts can be done in at least four areas.

(1) Intragrammar evaluation of scripts. Often a grammar can be used to generate several scripts to describe the same phenomena. Competing scripts could then be evaluated to determine which one better supports the task at hand. For example, data-flow diagrams with alternative “levellings” are “informationally equivalent” (i.e., they represent the same set of domain semantics). Nonetheless, they might differ in their ability to support a particular task that a stakeholder has to complete. Similarly, physical rearrangement of the entities and relationships in an entity-relationship diagram can affect stakeholders’ comprehension of the diagram.

(2) Intergrammar evaluation of scripts. Two or more grammars might be used to generate alternative scripts that are intended to describe the same phenomena. The competing scripts can be evaluated to determine which one better supports the task at hand. Again, the competing scripts are assumed to be “informationally equivalent.”

(3) Evaluation of multigrammar scripts. When multiple grammars are employed, it might be possible to generate alternative scripts to describe the same phenomena with at least one of the grammars in the combination used to generate different representations. Such alternative representations need to be evaluated.

(4) Theoretical analyses. The above three streams of research require a theory to facilitate understanding and predicting how humans use scripts to accomplish various tasks. Such a theory would identify the properties of scripts that impact stakeholder performance. As well, it would serve to generate a set of mutually independent criteria for script evaluation. For the most part, the scripts generated using grammars are diagrammatic in nature. In this light, theories of diagrammatic reasoning (e.g., Larkin and Simon 1987) provide one possible base. As we indicated in §4.2 above, Kim et al. (2000) used such theories to evaluate the scripts produced using different object-oriented grammars. Theories of mental models (e.g., Gentner and Stevens 1983, Mayer and Gallini 1990) also might be used. These theories predict that good “illustrations” clearly show (a) the system’s topology (components of the system) and (b) the behavior of components and interactions among components.

## 7. Conceptual Modeling in Context

Creation and use of conceptual models are undertaken within a particular context (e.g., organizational and task context). We need to understand better how the context affects modeling work and, in turn, how modeling and use of models affect elements of the context.

## 7.1. Overview of Some Existing Research

As we indicated in §3, we will focus on just three elements of the context—individual difference factors, task factors, and social agenda factors.

7.1.1. Individual Contextual Factors. Batra and Davis (1992), Sutcliffe and Maiden (1992), and Shanks (1997) have investigated novice versus expert behavior in conceptual-modeling tasks. They found that (a) experts spend more time trying to develop a holistic understanding of requirements, (b) experts produce higher-quality solutions in terms of accuracy, completeness, innovativeness, and adaptability, and (c) both experts and novices tend to use individual constructs in a grammar appropriately.

Certain cognitive characteristics of individuals may also bear on the quality of conceptual-modeling work undertaken. For example, Dunn and Grabski (1998) found that field-independent individuals (those who could disembed objects from their greater context) performed better at conceptual-modeling tasks than fielddependent individuals (those who encounter difficulty when they have to disembed objects from their greater context).

7.1.2. Task Contextual Factors. As we noted above, grammars, methods, and scripts are likely to have differential strengths and weaknesses in supporting different tasks. Some work has been done already to identify which grammars are best suited to different types of tasks. For example, based on Vessey’s (1991) cognitive-fit theory, Agarwal et al. (1999) predicted that users of object-oriented grammars would perform better on comprehension tasks that focussed primarily on structure and that users of data-flow grammars would perform better on comprehension tasks that focussed primarily on behavior. Empirically, they obtained mixed support for their predictions.

7.1.3. Social Agenda Factors. As noted in §5.1 above, some preliminary research has been done on the values and beliefs associated with conceptual modeling and how they might impact the modeling process. This research was motivated in part by the positivist-interpretivist debates that occurred in the information systems field throughout the 1980s and 1990s (e.g., Nissen et al. 1991). Many existing grammars and methods were criticized because (a) supposedly they implied a realist view of the world, and (b) they adopted positivistic, nomothetic, means-end values and beliefs about the nature of the world. On the other hand, interpretivists argued that perceptions about the world were a social construction. The phenomena to be modeled, therefore, were “created” not “discovered.” Indeed, some interpretivists contended that conceptual-modeling grammars and methods helped generate or create the worlds perceived by stakeholders.

An important outcome of this research was a recognition of the need to better understand the social con text in which modeling was conducted or models used. Hirschheim et al. (1995) used Burrell and Morgan’s (1979) framework to suggest four social contexts:

(1) Functionalist. Functionalists are realists who seek to account for an independent world using positivistic methods. They search for order in an objective world.

(2) Social Relativist. Social relativists seek to account for the subjective worlds created by humans. They use interpretive methods to analyze these worlds.

(3) Radical Structuralist. Radical structuralists seek out economic and power structures that they believe have objective, independent existence in the worlds they study. They focus on ways to replace these structures with “better” economic and social orders.

(4) Neohumanist. Neohumanists focus on change, participation, emancipation, and the realization of human potential. They strive to mitigate factors that prevent humans from reaching their full potential (e.g., social constraints and unequal power distributions).

Hirschheim et al. (1995) provide an extensive account of how they believe these four contexts have impacted the development of conceptual-modeling grammars and methods and their likely effects on the ways grammars, methods, and scripts will be used in practice.

## 7.2. Some Future Research Opportunities

The three contextual factors we have examined above also provide a basis for articulating the sorts of future research that might be undertaken on context.

7.2.1. Individual Contextual Factors. At least three types of research might be undertaken on individual contextual factors:

(1) Improving individuals’ performance. The goals of expert-novice difference research have been to (a) develop better training and education to support conceptual modeling, (b) develop appropriate knowledge-based support tools, and (c) improve conceptual-modeling grammars and methods to mitigate limitations observed in expert and novice behaviors. Little research has been done so far, however; hence, substantial research opportunities remain. For example, knowledgebased tools might be built to prevent modelers using the relationship construct incorrectly (Batra et al. 1990). Similarly, methods might be articulated in more detail to provide better guidance to modelers on how multiple grammars should be used in concert to produce high-quality scripts to represent a domain.

(2) Studying the effects of cognitive characteristics. Both script creation and interpretation sometimes involve high levels of cognitive complexity for modelers and users of scripts. Future research might investigate whether certain types of cognitive variables are salient to task outcomes that occur. For example, whether users of scripts are field-dependent or field-independent individuals might impact their ability to elicit the semantics represented by a script.

(3) Studying the effects of personality characteristics. The social context in which conceptual modelers work is sometimes difficult. For example, stakeholders in a system may have conflicting goals, or the system requirements may be uncertain and require careful discernment. Thus, the social skills that conceptual modellers possess (e.g., their ability to develop rapport with the users of a system) may affect the outcomes that arise. Little is known about how a script creator’s or script reader’s personality characteristics impact performance during conceptual-modeling tasks.

7.2.2. Task Contextual Factors. Conceptual-modeling grammars, methods, and scripts need to be examined systematically in the context of different information systems tasks: development, implementation, use, and maintenance. For example, can conceptual models play a useful role when analysts must evaluate whether an enterprise resource-planning package meets the needs of their organization? If so, what role? What types of models (e.g., models that focus on static phenomena or models that focus on dynamic phenomena) are best suited to that role? Similarly, are conceptual models useful when end users query a database using SQL? If yes, what types of models (e.g., those that are “pure” conceptual models or those that manifest some of the data-modeling decisions that have been made) are best suited to that role?

## 7.2.3. Social Agenda Factors. At least four types of research might be undertaken on social agenda factors:

(1) Studying underlying values and beliefs. Much research needs to be done on the values and beliefs that underlie conceptual-modeling work. In this regard, Hirschheim et al.’s (1995) analysis opens up several rich opportunities. For example, how well do Burrell and Morgan’s (1979) “paradigms” characterize conceptualmodeling work done in practice? Do the stakeholders in a conceptual-modeling exercise tend to operate from a functionalist perspective or some other perspective? Do certain perspectives tend to dominate under different circumstances?

(2) Effects of adopting alternative perspectives. Little is known about the effects of adopting each paradigmatic perspective on conceptual modeling. For example, does adoption of a social-relativist perspective during model construction lead to better outcomes than other perspectives? Should the choice of perspective be contingent on the task?

Table 2 Summary of Research Opportunities on Conceptual Modeling

<table><tr><td>Research Framework Element</td><td>Some Research Opportunities</td></tr><tr><td>Conceptual-modeling grammars</td><td>Evaluating ontologies based on empirical testing of their predictionsEvaluating grammars for ontological expressivenessAssigning ontological meaning to constructs of design grammars and generating ontologically motivated modeling rulesResolving outstanding ontological problems that impact conceptual modeling—e.g., nature of the part-of relationshipEmpirically testing predicted strengths and weaknesses in new and existing grammars based on their ontological expressivenessDetermining which combinations of grammars best support users who undertake conceptual-modeling workEmpirically testing the predicted implications of construct deficit and overload in grammars</td></tr><tr><td>Conceptual-modeling methods</td><td>Evaluating how well different methods allow users to elicit and model critical domain knowledgeDeveloping procedures to assist users of a grammar to identify and classify phenomena according to the grammar&#x27;s constructsDetermining the beliefs and values that underlie different methods and evaluating the consequences of these beliefs and values for practice</td></tr><tr><td>Conceptual-modeling scripts</td><td>Evaluating competing scripts generated via the same grammar to describe some phenomenonEvaluating competing scripts generated via different grammars to describe the same phenomenonEvaluating different combinations of scripts to determine which combination best supports the task at handDeveloping theory to predict and understand how humans use scripts to accomplish various tasks</td></tr><tr><td>Conceptual-modeling contextindividual differences</td><td>Development of knowledge-based tools to support conceptual modelingPredicting which cognitive and personality variables bear on a user&#x27;s ability to undertake conceptual-modeling workPredicting and testing empirically which social skills affect the outcomes of conceptual-modeling tasks</td></tr><tr><td>task</td><td>Evaluating the strengths and weaknesses of conceptual-modeling grammars, methods, and scripts in the context of different tasks</td></tr><tr><td>social agenda</td><td>Understanding which values and beliefs underlie conceptual-modeling work in practiceDetermining the costs and benefits of adopting different values and beliefs when undertaking conceptual-modeling workArticulating detailed conceptual-modeling procedures that are congruent with different beliefs and valuesUnderstanding how existing conceptual-modeling grammars and methods facilitate conceptual-modeling work under different values and beliefs</td></tr></table>

(3) Developing methods to support perspectives. Different paradigmatic perspectives might call for different modeling procedures. For example, Hirschheim et al. (1995) indicate the broad methods, values, and beliefs that should underlie modeling under social relativism. The detailed procedures to be used, however, have not been articulated.

(4) Fit between perspectives and grammars and methods. Little is known about how well existing grammars and methods support conceptual-modeling work under each paradigmatic perspective. For example, is the entity-relationship grammar better suited to a functionalist perspective to conceptual modeling or a radical-structuralist perspective?

## 8. Conclusions

Our analysis above was motivated by the question: How can we model the world to better facilitate our developing, implementing, using, and maintaining more valuable information systems? Table 2 summarizes the research opportunities we have identified to help answer this question. We reiterate that they are indicative rather than complete. Nevertheless, we hope they are sufficient to show the rich, exciting possibilities that exist.

There are other avenues for research on conceptual modeling that we have not explored, such as (1) linking conceptual-modeling research to work on ontologies in knowledge representation (Sowa 1999), (2) studying the conceptual-modeling needs of new applications like knowledge-management systems, and (3) studying conceptual-modeling methods for projects involving multiple organizations. These also provide fruitful opportunities for further research.

## Acknowledgments

This research was funded in part by the School of Commerce Research Fund, The University of Queensland, and the Natural Sciences and Engineering and Social Sciences and Humanities Research Councils of Canada. The authors thank Izak Benbasat for comments on an earlier version of this paper.

## References

Agarwal, R., P. De, A. P. Sinha. 1999. Comprehending object and process models: An empirical study. IEEE Trans. Software Engrg. 25(4) 541–556.

——, A. Sinha, M. Tanniru. 1996. Cognitive fit in requirements engineering: A study of object and process models. J. Management Inform. Systems 13(2) 137–162.

Anderson, J. R. 1983. The Architecture of Cognition. Harvard University Press, Cambridge, MA.

——. 1995. Learning and Memory: An Integrated Approach. Wiley, New York.

Artale, A., E. Franconi, N. Guarino, L. Pazzi. 1996. Part-whole relations in object-centered systems: An overview. Data & Knowledge Engrg 20 347–383.

Ashenhurst, R. L. 1996. Ontological aspects of information modeling. Minds and Machines 6 287–394.

Auramaki, E., E. Lehtinen, K. Lyytinen. 1988. A speech-act-based office modeling approach. ACM Trans. Office Inform. Systems 6(2) 126–152.

Basu, A., R. W. Blanning. 2000. A formal approach to workflow analysis. Inform. Systems Res. 11(1) 17–36.

Batra, D., J. G. Davis. 1992. Conceptual data modeling in database design: Similarities and differences between expert and novice designers. Internat. J. Man-Machine Stud. 37 83–101.

——, G. M. Marakas. 1995. Conceptual data modeling in theory and practice. Euro. J. Inform. Systems 4 185–193.

——, J. A. Hoffer, R. P. Bostrom. 1990. Comparing representations with relational and EER models. Comm. ACM 33 126–139.

Bodart, F, A. Patel, M. Sim, R. Weber. 2001. Should optional properties be used in conceptual modeling? A theory and three empirical tests. Inform. Systems Res. 12(4).

Brosey, M., B. Schneiderman. 1978. Two experimental comparisons of relational and hierarchical database models. Internat. J. Man-Machine Stud. 10 625–637.

Bunge, M. 1977. Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World. Reidel, Boston, MA.

Burrell, G., G. Morgan. 1979. Sociological Paradigms and Organisational Analysis: Elements of the Sociology of Corporate Life. Heinemann, London, U.K.

Checkland, P. 1981. Systems Thinking, Systems Practice. Wiley, Chichester, U.K.

Chen, P. P. S. 1976. The entity-relationship model: Toward a unified view of data. ACM Trans. Database Systems 1(1) 9–36.

Chisholm, R. M. 1996. A Realistic Theory of Categories—An Essay on Ontology. Cambridge University Press, Cambridge, U.K.

Curtis, B., M. I. Kellner, J. Over. 1992. Process modeling. Comm. ACM 35(9) 75–90.

Doyle, K. G., J. R. G. Wood, A. T. Wood-Harper. 1993. Soft systems and systems engineering: On the use of conceptual models in information systems development. J. Inform. Systems 3(3) 187– 198.

Dunn, C., S. Grabski. 1998. The effect of field dependence on conceptual modeling performance. Adv. Accounting Inform. Systems 6 65–77.

Evermann, J., Y. Wand. 2001. Towards ontologically based semantics for UML constructs. Proc. Internat. Conf. Conceptual Modeling (ER), Yokohama, Japan.

Floyd, C. 1986. A comparative evaluation of system development methods. T. W. Olle, H. G. Sol, and A. A. Verrijn-Stuart, eds. Information System Design Methodologies: Improving the Practice. North-Holland, Amsterdam, 19–54.

Gemino, A. 1999. Empirical methods for comparing system analysis modeling techniques. Ph.D. thesis, The University of British Columbia, Vancouver, Canada.

—, Y. Wand. 2001. Comparing object oriented with structured analysis techniques in conceptual modeling, Working paper 99-MIS-01, Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, Canada.

Gentner, D., A. L. Stevens, eds. 1987. Mental Models. Erblaum, Hillsdale, NJ.

Goldstein, R. C., V. Storey. 1990. Some findings on the intuitiveness of entity-relationship constructs. F. H. Lochovsky, ed., Entity-Relationship Approach to Database Design. Elsevier Science Publishers, B. V., North Holland, Amsterdam, 9–23.

Green, P. M. 1996. An ontological analysis of information systems analysis and design (ISAD) grammars in upper CASE tools. Unpublished Ph.D. thesis, The University of Queensland, Australia.

——, M. Rosemann. 2000. Integrated process modeling: An ontological evaluation. Inform. Sys. 25(2) 73–87.

Halpin, T. A. 1995. Conceptual Schema and Relational Database Design: A Fact Oriented Approach, 2nd ed. Prentice-Hall, Sydney, Australia.

Hirschheim, R., H. Klein, K. Lyytinen. 1995. Information Systems Development and Data Modeling: Conceptual Foundations and Philosophical Foundations. Cambridge University Press, Cambridge, U.K.

Hitchman, S. 1995. Practitioner perceptions of the use of some semantic concepts in the entity-relationship model. Euro. J. Inform. Systems 4 31–40.

Hutchins, E. L., J. D. Hollan, D. A. Norman. 1985. Direct manipulation interfaces. Human-Comput. Interaction 1 311–338.

Jarvenpaa, S. L., J. J. Machesky. 1989. Data analysis and learning: An experimental study of data modeling tools. Internat. J. Man-Machine Stud. 31 367–391.

Kesh, S. 1995. Evaluating the quality of entity-relationship models. Inform. Software Tech. 37(12) 681–689.

Kim, J., J. Hahn, H. Hahn. 2000. How do we understand a system with (so) many diagrams? Cognitive integration processes in diagrammatic reasoning. Inform. Systems Res. 11(3) 284–303.

Kim, Y. G., S. March. 1995. Comparing data modeling formalisms. Comm. ACM 38(4) 103–115.

Kung, C. H., A. Solvberg. 1986. Activity modeling and behaviour modeling. T. W. Olle, H. G. Sol, and A. A. Verrijn-Stuart, eds. Information System Design Methodologies: Improving the Practice. North-Holland, Amsterdam, The Netherlands, 145–171.

Larkin, J., H. A. Simon. 1987. When a diagram is (sometimes) worth ten thousand words. Cognitive Sci. 11(1) 65–99.

Lindland, O. I., G. Sindre, A. Sølvberg. 1994. Understanding quality in conceptual modeling. IEEE Software 11(2) 42–49.

Maier, R. 1996. Benefits and quality of data modeling—Results of an empirical analysis. Proc. 15th Internat. Conf. Entity-Relationship Approach, Cottbus, Germany, 245–260.

Mayer, R. E. 1989. Models for understanding. Rev. Educational Res. 59 43–64.

——, J. K. Gallini. 1990. When is an illustration worth a thousand words? J. Educational Psych. 82 715–726.

Milton, S., E. Kazmierczak. 1999. Enriching the ontological foundations of modeling in information systems. C. N. G. Dampney, ed. Proc. Inform. Systems Foundations Workshop—Ontology, Semiotics and Practice 1999, Department of Computing, Macquarie University, Sydney, Australia, 55–65.

Moody, D. L. 1998. Metrics for evaluating the quality of entity relationship models. Proc. 17th Internat. Conf. Conceptual Modeling, Singapore.

——, G. Shanks. 1998. Improving the quality of entity-relationship models: An action research programme. Australian Computer J. 30 129–138.

Mylopoulos, J. 1998. Information modeling in the time of the revolution. Inform. Systems 23 127–155.

Newell, A., H. A. Simon. 1972. Human Problem Solving. Prentice Hall, Englewood Cliffs, NJ.

Nissen, H.-E., H. K. Klein, R. Hirschheim, eds. 1991. Information Systems Research: Contemporary Approaches and Emergent Traditions. North-Holland, Amsterdam, The Netherlands.

Norman, D. 1986. Cognitive engineering. D. Norman and S. Draper, eds. User Centered Design: New Perspectives on Human Computer Interaction. Erlbaum, Hillsdale, NJ, 31–61.

Oei, J. L. H., L. J. G. T. van Hemmen, E. Falkenberg, S. Brinkkemper. 1982. The meta model hierarchy: A framework for information systems concepts and techniques. Technical Report No. 92–17,

Department of Information Systems, University of Nijmegen, The Netherlands.

Olle T. W., H. G. Sol, C. J. Tully, eds. 1983. Information System Design Methodologies: A Feature Analysis. North-Holland, Amsterdam, The Netherlands.

——, A. A. Verrijn-Stuart. 1982. Information System Design Methodologies: A Comparative Review. North-Holland, Amsterdam, The Netherlands.

—, ——, eds. 1986. Information System Design Methodologies: Improving the Practice. North-Holland, Amsterdam, The Netherlands.

Opdahl, A., B. Henderson-Sellers. 1999. Evaluating and improving OO modeling languages using the BWW-model. C. N. G. Dampney, ed. Proc. Inform. Systems Foundations Workshop—Ontology, Semiotics and Practice 1999, Department of Computing, Macquarie University, Sydney, Australia, 31–38.

, ——, F. Barbier. 2001. Ontological analysis of whole-part relationships in OO-models. Inform. Software Tech. 43 387–399.

Parsons, J. 1996. An information model based on classification theory. Management Sci. 42(10) 1437–1453.

Paulson, D., Y. Wand. 1992. An automated approach to information systems decomposition. IEEE Trans. Software Engrg. 18 174–189.

Prietula, M. J., S. T. March. 1991. Form and substance in physical database design: An empirical study. Inform. Systems Res. 2 287– 314.

Scheer, A.-W. 1999. Business Process Frameworks, 2nd ed. Springer, Berlin, Germany.

Searle, J. 1969. Speech Acts: An Essay in the Philosophy of Language. Cambridge University Press, New York.

Shanks, G. 1997. Conceptual data modeling: An empirical study of expert and novice data modelers. Australian J. Inform. Systems 4(2) 63–73.

Siau, K. 1996. Empirical studies in information modeling: Interpretation of the object relationship. Unpublished Ph.D. thesis, The University of British Columbia, Vancouver, Canada.

—, Y. Wand, I. Benbasat. 1995. A psychological study on the use of the relationship concept—Some preliminary findings. J. Iivari, K. Lyytinen, and M. Rossi, eds. Lecture Notes in Computer Science—Advanced Information Systems Engineering, 932. Springer-Verlag, Berlin, Heidelberg, Germany, 341–354.

——, ——. 1997. The relative importance of structural constraints and surface semantics in information modeling. Inform. Systems 22(2–3) 155–170.

Soffer, P., B. Golany, D. Dori, Y. Wand. 2001. Modeling off-the-shelf information systems requirements: An ontological approach. Requirements Engrg. 6 183–199.

Sowa, J. F. 1999. Knowledge Representation: Logical, Philosophical, and Computational Foundations. Brooks/Cole, Pacific Grove, CA.

Stamper, R. 1987. Semantics. R. J. Bolland, R. A. Hirschheim, eds., Critical Issues in Information Systems Research. John Wiley and Sons, New York, 43–78.

Standish Group. 1995. “Chaos.” Report on Information System Development. www.standishgroup.com/chaos.html- [version of July 1996].

Storey, V. 1991. Meronymic relationships. J. Database Admin. 2(3) 22– 35.

Sutcliffe, A. G., N. A. M. Maiden. 1992. Analysing the novice analyst: Cognitive models in software engineering. Internat. J. Man-Machine Stud. 36 719–740.

Teorey, T. J., D. Yang, J. P. Fry. 1986. A logical design methodology for relational databases using the extended entity-relationship model. ACM Comput. Surveys 18(2) 197–222.

van der Aalst, W. M. P., A. H. M. ter Hofstede, B. Kiepuszewski, A. P. Barros. 2000. Workflow patterns. Unpublished paper, www.tm.tue.nl/it/research/patterns/-.

Varzi, A. C. 1996. Parts, wholes, and part-whole relations: The prospects of mereotopology. Data & Knowledge Engrg 20 259–286.

Vessey, I. 1991. Cognitive fit: A theory-based analysis of the graphs versus tables literature. Decision Sci. 22(2) 219–240

——, S. Conger. 1994. Requirements specification: Learning object, process, and data methodologies. Comm. ACM 37(5) 102–113.

Wand, Y., R. Weber. 1993. On the ontological expressiveness of information systems analysis and design grammars. J. Inform. Systems 3 217–237.

—, ——. 1995. On the deep structure of information systems. Inform. Systems J. 5 203–223.

—, C. Woo. 1993. Object oriented analysis—Is it really that simple? Proc. Workshop on Inform. Technologies and Systems, Orlando, FL, 186–195.

——, V. Storey, R. Weber. 1999. An ontological analysis of the relationship construct in conceptual modeling. ACM Trans. Database Systems 24 494–528.

——, D. E. Monarchi, J. Parsons, C. C. Woo. 1995. Theoretical foundations for conceptual modeling in information systems development. Decision Support Systems 15 285–304.

Weber, R. 1996. Are attributes entities? A study of database designers’ memory structures. Inform. Systems Res. 7 137–162.

——. 1997. Ontological Foundations of Information Systems. Coopers & Lybrand, Melbourne, Australia.

Wimmer, K., N. Wimmer. 1992. Conceptual modeling based on ontological principles. Knowledge Acquisition 4 387–406.

Winograd, T., F. Flores. 1987. Understanding Computers and Cognition: A New Foundation for Design. Addison-Wesley, Reading, MA.

Winston, M. E., R. Chaffin, D. Herrman. 1987. A taxonomy of partwhole relations. Cognitive Sci. 11 417–444.

Yadav, S., R. Bravoco, A. Chatfield, T. Rajkumar. 1988. Comparison of analysis techniques for information requirements determination. Comm. ACM 31(9) 1090–1097.

Izak Benbasat, Senior Editor. This paper was received on August 1, 2001, and was with the authors 2 weeks for 1 revision.
