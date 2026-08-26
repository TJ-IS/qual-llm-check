---
otero_id: 6060
otero_key: "JD9QZFBC"
title: "Diagrammatic Attention Management and the Effect of Conceptual Model Structure on Cardinality Validation"
authors: "Cheryl Dunn; Gregory Gerard; Severin Grabski"
year: "2011"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00272"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
8-30-2011

# Diagrammatic Attention Management and the Effect of Conceptual Model Structure on Cardinality Validation

Cheryl L. Dunn , dunnc@gvsu.edu

Gregory J. Gerard

, ggerard@cob.fsu.edu

Severin V. Grabski

, grabski@msu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Jourņal of the Asşociation for Information Systems JAIS

Research Article

# Diagrammatic Attention Management and the Effect of Conceptual Model Structure on Cardinality Validation\*

Cheryl L. Dunn Grand Valley State University dunnc@gvsu.edu

Gregory J. Gerard Florida State University ggerard@cob.fsu.edu

Severin V. Grabski Michigan State University grabski@msu.edu

## Abstract

Diagrams are frequently used to document various components of information systems, from the procedures established for user-system interaction, to the structure of the database at the system’s core. Past research has revealed that diagrams are not always used as effectively as their creators intend. This study proposes a theory of diagrammatic attention management to contribute to the exploration of diagram effectiveness. Based upon diagrammatic attention management, this study demonstrates that the type of diagram most commonly used to represent conceptual models is less effective than three other alternatives for validating the models cardinalities. Most conceptual models are documented using entity-relationship diagrams that include a full transaction cycle or module on a single page, i.e., an aggregate diagrammatic format. Participants in this study using three alternative representations (disaggregate diagrammatic, aggregate sentential, and disaggregate sentential) outperformed users of the aggregate diagrammatic format for cardinality validation. Results suggest that to facilitate effective use of aggregate diagrams, users need a mechanism by which to direct their attention while using the diagrams. If such an attention direction mechanism is not inherent in a diagram, it may need to be applied as an external tool, or the diagram may need to be disaggregated to facilitate use.

Keywords: Diagrammatic Attention Management, Conceptual Data Models, Cardinality Validation, Entity Relationship Diagrams.

# Diagrammatic Attention Management and the Effect of Conceptual Model Structure on Cardinality Validation

## 1. Introduction

Pictures may be worth 1,000 words, but research suggests that diagrammatic representations are surprisingly difficult and cumbersome to use (Larkin & Simon, 1987; Moher, Mak, Blumenthal, & Leventhal, 1993; Petre, 1995; Kim, Hahn, & Hahn, 2000). Information systems documentation includes many types of diagrams, such as Entity-Relationship (ER) diagrams, Data Flow Diagrams (DFD), and Unified Modeling Language (UML) diagrams (see, e.g., Chen, 1976; Yourdon, 1989; Rumbaugh, Jacobson, & Booch, 1999). This study examines diagrammatic attention management in the context of ER diagrams because of their convertibility into equivalent sentential representations. Manipulating the conceptual model structure and measuring cardinality validation performance, this study calls into question the implicit assumption that aggregate diagrammatic conceptual models are appropriate for all tasks.

The information system development process typically begins with requirements gathering and assimilation of those requirements into a conceptual model. The conceptual model serves as a communication tool between system users and developers; it also provides input for the system design process, promotes domain understanding for analysts, and becomes the foundation for the enterprise database management system (Kung & Sølvberg, 1986).

Conceptual models can facilitate system design error detection and may reduce the cost of correcting such errors (Wand & Weber, 2002). Conceptual models are also used to promote understanding and communication about parts of the physical and social environment (Mylopolous, 1992). High quality conceptual models must reflect accurate syntax, semantics, and pragmatics (Lindland, Sindre, & Sø lvberg, 1994). That is, they must be structured according to the modeling language and faithfully represent the underlying reality in a format consistent with users’ perceptions of that reality.

Prior research identifies localization (visual contiguity or close physical proximity of related objects) as a key characteristic of good diagrams (see, e.g., Larkin & Simon, 1987; Dunn & Grabski, 2001; Mayer, 2001; Mayer & Moreno, 2002; and Reed, 2006). Localization, while perhaps necessary, may not be a sufficient condition to facilitate diagram use. Studies that showed benefits of localization used tasks that directed users to look at specific places on the diagrams (e.g., Larkin & Simon, 1987; Dunn & Grabski, 2001; Mayer, 2001; Mayer & Moreno, 2002; and Reed, 2006). At least one study (Petre, 1995) observed users who were not provided with an attention direction mechanism trying to develop their own mechanism to track content already evaluated.

We propose a theory that diagrammatic attention management requires both localization and an attention direction mechanism to guide users’ diagram navigation. Localization alone is insufficient because it is task-specific. A single representation may not include physically proximate combinations of related objects to meet all possible information needs. Tasks that require inspection of more physical places on a diagram than working memory can store will be especially difficult, as users may be overwhelmed trying to remember what they have already examined and where they need to look next.

Cardinality validation is a task that requires users to attend to every object in the conceptual model and has no inherent attention direction mechanism. Validation is a crucial task as highlighted by Arlow, Emmerich, and Quinn (1999), who note that graphical models do not distinguish between cardinality requirements that represent critical business rules with significant economic impact and cardinality requirements that represent rules with minor impacts. When cardinality requirements reflect critical business rules, one cardinality mistake can result in a huge economic cost. Dobing and Parsons (2006, 2008) lend credence to the fact that clients are asked to validate analysis diagrams (particularly UML class diagrams, which are analogous to ER diagrams). Wastell (1996) further bolsters this with evidence that analysts do sometimes provide users with entire pieces of documentation and ask them to validate all of the information rather than instructing them to focus on specific items in the documentation.

Given that (1) users in practice are sometimes given system documentation (including conceptual models) and are asked to validate all of it, (2) mistakes made in such validation can be extremely costly, and (3) diagrammatic conceptual models can be constructed in informationally equivalent sentential formats, we use this context to develop and test hypotheses derived from the theory of diagrammatic attention management. In practice and in information systems textbooks, conceptual models are prepared and used in aggregate diagrammatic form, implicitly assuming that this format is appropriate for all tasks. However, aggregate diagrammatic conceptual models provide less inherent attention direction and, thus, less effective attention management than do the other three types: disaggregate diagrammatic, aggregate sentential, and disaggregate sentential. This study provides evidence that for cardinality validation, either an attention direction mechanism needs to be added to the aggregate diagrammatic conceptual model, or one of the other three formats should be used. The next section of this paper proposes hypotheses based on a discussion of the conceptual and theoretical background. We then describe the research methodology, analyze the results, discuss implications of the results, suggest future research directions, and provide conclusions.

## 2. Conceptual and Theoretical Background

Various people use diagrams for many different purposes, yet the perceived difficulty of using diagrams in some contexts remains a mystery to those who understand the diagrams well. Teenage automobile drivers who insist on using turn-by-turn directions instead of maps have frustrated many parents. Students who just can’t seem to comprehend the information communicated by a specific graph have mystified many mathematics and physics professors. More than one information system manager has been aghast that a misinterpretation of an asterisk on a UML diagram could have resulted in a multi-million dollar error (Arlow et al., 1999).

## 2.1. Diagrams and Attention Management

Several cognitive theories explain various aspects of effective diagram use in decision making. Cognitive load theory states that working memory limits users to processing only a few elements at any one time (Mayer & Moreno, 2002). Individuals learn more deeply when their working memories are not overloaded. Multi-tasking students perform more poorly than students who focus on the task at hand (Glenn, 2010). Larkin and Simon (1987) identify localization as a necessary ingredient for effective diagram use, as adjacent placement of needed information on a diagram facilitates information processing operators. Cognitive fit theory (Vessey, 1991; 1994; 2006) suggests that a user’s mental representation (i.e., the way a problem is represented in human working memory) is more easily formed and leads to better problem solutions when the problem representation and the problem-solving task match. Spatial representations yield better performance for spatial tasks; symbolic representations yield better performance for symbolic tasks. Multimedia learning theory (Mayer, 2001) suggests that to enhance learning from diagrams, diagrams should be paired either with words placed in close proximity to the diagram or with verbal narration.

Diagrammatic attention management theory draws on all of these theories but is different from all of them. Diagrammatic attention management theory suggests that to effectively use any diagram for any task (spatial or symbolic), a user’s attention must be directed to the location(s) on the diagram that contains the needed information. Such a mechanism should guide users through the diagram, helping them track what they have already looked at and what they still have to examine. Localization without attention direction is insufficient; users need to know how to get to the part of the representation in which the needed information is localized. Attention may be managed via an inherent navigation path, such as that found in the binary diagram condition, and the diagram need not include additional words or verbal narration. Other research also suggests that attention may be managed via an external navigation path, such as the notations added to spreadsheets to illustrate chaining in Goswami, Chan, and Kim (2008).

Petre (1995) reported on several experiments that evaluated comprehension of nested conditional structures using graphics and text. Users of the graphic representation took longer than textual representation users and never outperformed the textual users. The slower usage may have resulted from the lack of an attention direction mechanism:

“… it is apparent that even the expert reader of graphical notations is doing a hard job. (Said one expert: This is hard work… There‟s no easy way. It‟s going to be very difficult to explore all this maze in finite time.) The sight of subjects crawling over the screen with mouse or fingers, talking aloud to keep their working memory updated, was remarkable. One of the distinctions between expert and novice behavior was that the experts made better use of their fingers, occasionally using all ten to mark points along a circuit.” (Petre, 1995, p. 38).

Moher et al. (1993) discovered that performance using graphical representations depended on their layout and that the efficiency of any graphical representation is both task specific and sensitive to layout. This is consistent with our proposal that diagrammatic attention management requires both localization and an attention direction mechanism to assist with navigation.

## 2.2. Conceptual Model Research

Conceptual models have been the topic of many studies because of their importance in system design. They serve as input to logical database design and are used for early detection of errors. Conceptual models are created to map real-world needs and are validated with stakeholders to verify their needs have been correctly specified (Siau & Tan, 2005). Validation of conceptual models to identify design errors early in the system development life cycle decreases error correction costs (Boehm, 1989; Moody, 1998). Conceptual model validation should examine syntax, semantics, and pragmatism. In other words, the model must use correct syntax, the model must accurately represent the underlying reality, the user must be able to understand what the model is communicating, and the user must be able to verify that the model accurately portrays the environment (Lindland et al., 1994; Kim & March, 1995).

Researchers have studied user comprehension of conceptual models along a number of dimensions: as a function of problem decomposition (Burton-Jones & Meso, 2006), understanding of optional properties versus subtypes with mandatory properties (Bodart, Patel, Sim, & Weber, 2001; Gemino & Wand, 2005), ontological complexity and clarity (Gemino & Wand, 2005), and effectiveness and efficiency for generating scripts (Burton-Jones, Wand, & Weber, 2009). Gemino and Parker (2009) found that users retained more information and solved problems better when using case diagrams presented together with text than when using case text alone. Results of these studies indicated the specific effects of user understanding vary depending on the factors examined and the measures used. Most conceptual models provide limited information processing guidance: If such guidance is not inherent in the model and is not provided externally, performance degradation is expected.

## 2.3. Conceptual Models for Studying Diagrammatic Attention Management

Conceptual models may be represented in non-diagrammatic formats, allowing investigation of whether performance differences are due to representation (diagram versus sentential, i.e., text format) or to composition (aggregate or disaggregate). In practice and in information systems textbooks, conceptual models are primarily prepared and used in diagrammatic/aggregate form, implicitly assuming that this format is appropriate for all tasks. However, diagrammatic/aggregate conceptual models provide less inherent attention direction and, thus, less effective attention management than do the other three combinations: diagrammatic/disaggregate, sentential/aggregate, and sentential/disaggregate. Thus, conceptual models are a useful context in which to study diagrammatic attention management.

Table 1 presents an overview of the representation and composition of the conceptual modeling approaches examined in this research, while Figure 1 presents a very simple instantiation of the two factors of conceptual model structure. The first factor, representation, is whether the conceptual model has a diagrammatic or sentential structure (the sentential structure follows Batini, Ceri, and Navathe, 1992, p. 35; they refer to it as a Backus-Naur form grammar). The second factor, composition, is whether the conceptual model is aggregate (with all entities and relationships shown in a single diagram) or disaggregate (with all entities and relationships disaggregated into a series of binary relationships).

In Figure 1, note that for the sentential structures, (a) the aggregate structure on the left l ists all entities and then all relationships, and (b) the disaggregate structure on the right partitions the information into a series of separate binary relationships. Dunn and Gerard (2001) investigated user performance on search, inference, and recognition tasks as a function of informationally equivalent diagrammatic/aggregate versus sentential/aggregate ER models. They presented participants with a series of directed queries for which the answers could be derived from the models. Query examples include ―What is the primary key of X?‖ and ―What information is needed to determine Z?‖ Dunn and Gerard (2001) found no difference in accuracy, but they did find an effect for time. Participants receiving the diagrammatic/aggregate ER models were faster than those receiving other treatments, suggesting a difference in computational equivalence.

Table 1. Overview of the Representation and Composition of the Conceptual Modeling Approaches

<table><tr><td></td><td colspan="2">Conceptual Model Composition</td></tr><tr><td>Conceptual Model Representation</td><td>Aggregate</td><td>Disaggregate</td></tr><tr><td>Diagrammatic</td><td>Traditional Diagrammatic Conceptual Data Modeling Techniques</td><td>Presentation of Diagrammatic Conceptual Data Models in Binary Sets</td></tr><tr><td>Sentential</td><td>Backus-Naur Presentation of Entire Conceptual Model</td><td>Backus-Naur Presentation of Conceptual Model in Binary Sets</td></tr></table>

The directed tasks used in Dunn and Gerard (2001) do not require an exhaustive search through all cardinalities in the model and are facilitated through localization (as predicted by Larkin and Simon, 1987) within the diagram. Their results are also consistent with the contiguity principle, which states that better performance results when corresponding words and images are presented simultaneously (Mayer, 2001). However, localization is not sufficient when the task becomes nondirected, such as ―validate every cardinality in this model.‖ In this type of task, some type of diagrammatic attention management device is required to provide the decision maker with an effective and efficient method of identifying and categorizing the items that have been attended to. For localization to occur (or for the contiguity principle to apply) there must be some type of control mechanism that provides direction for where to look. The use of graphical notation requires the user to identify an appropriate inspection strategy. Graphical representations that do not inherently contain a linear flow provide little guidance to users as to how they should navigate that diagram. Rather than guaranteeing clarity and superior performance, graphical representations may be more difficult to use (Petre, 1995). Simply providing a map and telling someone to find a particular city does not provide any advantages associated with localization or contiguity. However, if X and Y grid coordinates are provided, then these advantages can be obtained, and the graphical representation may prove superior to a textual representation.

Wastell (1996) provided evidence that system analysts provide entire pieces of documentation to users and subsequently ask them to validate the whole thing. The systems analysts may even provide it in a very impersonal way with no attempt to help the user through the validation process. Consider Wastell’s observation:

“SSADM is not a replacement for social skills … a lot of people wanted to avoid talking to users … they would send the documentation through the internal post with a request such as „check these please and tell me by Friday if there are any errors…‟. Who would do that? A lot of people did that though, they liked to rely on the procedure. It was a defensive attitude… I‟ll send this out, get on with the next thing, let them see all the work I have been doing. Sign-off was a ritual… users just did not understand all the documentation that we threw at them.” (Wastell, 1996, p. 27).

![](/api/attachments/JD9QZFBC/fulltext/images/e145058472d5c7e3e30d2549c8ba0040a2150131f24ffe683e494a1095ed934f.jpg)

Entity: Customer Attributes: Customer # Last Name First Name Identifier: Customer #

![](/api/attachments/JD9QZFBC/fulltext/images/e6ec867a93c8a416b65c70797981d6876500f3d79ca50fed9203bc96542d0699.jpg)

Entity: Sale Attributes: Sale # Date Amount Identifier: Sale #

Entity: Salesperson Attributes: Employee # Last Name First Name Identifier: Employee #

Entity: Salesperson Attributes: Employee # Last Name First Name Identifier: Employee #

Relationship: Assign Connected Entities: (0,N) Salesperson (1,1) Customer

Relationship: Control 1 Connected Entities: (1,1) Sale (0,N) Salesperson

Relationship: Control 2 Connected Entities: (1,1) Sale (1,N) Customer

Entity: Customer Attributes: Customer # Last Name First Name Identifier: Customer #

Relationship: Assign Connected Entities: (0,N) Salesperson (1,1) Customer

Entity: Sale Attributes: Sale # Date Amount Identifier: Sale #

Entity: Salesperson Attributes: Employee # Last Name First Name Identifier: Employee #

Relationship: Control 1 Connected Entities: (1,1) Sale (0,N) Salesperson

Entity: Sale Attributes: Sale # Date Amount Identifier: Sale # Entity: Customer Attributes: Customer # Last Name First Name Identifier: Customer # Relationship: Control 2 Connected Entities: (1,1) Sale (1,N) Customer

Conceptual models provide a meaningful context in which to study diagrammatic attention management. Conceptual models can be depicted in informationally equivalent diagrammatic and sentential formats, and they can be presented whole or in parts, allowing us to identify the contribution of attention direction. Figure 1 illustrates two important features of the different ER models resulting from crossing representation with composition. First, all four structures are informationally equivalent (consistent with the suggestions of Siau (2004), Gemino and Wand (2004), and Parsons and Cole (2005)). Second, with the exception of the diagrammatic/aggregate structure, the other three structures have an innate linear search path. For the task of cardinality validation, the person performing the validation has to consider all cardinalities, which is facilitated by a linear search path.

As noted by Petre (1995, p. 37) (and related only to the diagrammatic/aggregate structure because the other three structures have an inherently linear inspection strategy), ―unlike text, which is always amenable to a straight, serial reading, graphics requires [sic] the reader to identify an appropriate inspection strategy.‖ Diagrammatic/disaggregate, sentential/disaggregate, and sentential/aggregate are all amenable to a straight, serial reading (see Figure 1). In large, complex diagrams (diagrammatic/aggregate), it is difficult to derive an appropriate inspection strategy due to working memory limitations. Because of humans’ working memory limitations (Miller, 1956; Cowan, 2001) a diagrammatic attention management system is necessary. A diagram can facilitate attention management with an inherent sequence (e.g., a flowchart) or with a directed task and the localization of needed information (Larkin & Simon, 1987; Dunn & Grabski, 2001; Mayer, 2001; Mayer & Moreno, 2002; and Reed, 2006).

The cardinality validation task is particularly amenable for the study of diagrammatic attention management. We are able to provide informationally equivalent representations (so as to rule out information content differences). We are able to present diagrams that either do or do not possess a diagrammatic attention management mechanism. We are able to compare a diagram with an inherent attention management mechanism to a non-diagrammatic representation that also possesses an inherent attention management mechanism. Further, the cardinality validation task can be seeded with two types of errors: syntax (e.g., a maximum cardinality can never be 0; a minimum can never be N) based upon Batini et al. (1992); and semantic (e.g., a salesperson can only be associated with one and only one sale) based upon general business rules. An examination of the syntax errors that are not identified will allow for a stringent test of whether a diagrammatic attention management mechanism is required. All representations are informationally equivalent, all representations present the information contiguously (the information is localized), and the only difference is whether an attention management mechanism is present.

## 2.4. Proposed Theory and Hypotheses

Based upon the preceding sections, we propose a theory of Diagrammatic Attention Management. If users are directed, based upon the task presented to them, to examine a particular area of a diagram, and if all the required information is presented in a contiguous area on the diagram (i.e., localization exists), the users will be able to complete the task in an efficient and effective manner. If users, based upon the task presented to them, are not directed to a particular area on a diagram but, rather, must inspect the entire diagram, the users will be less effective and efficient.

The first part of the proposed theory has been tested in other papers (e.g., Dunn, Gerard, & Grabski, 2005; Dunn & Gerard, 2001; Dunn & Grabski, 2001). In those studies users were presented with informationally equivalent diagrams and other materials. When directed to look for specific information, novices were able to perform with more (or the same) effectiveness and efficiency than experienced participants when they were provided with diagrams that had localized (contiguous) information compared to other representation forms. Those studies did not specifically examine what would happen in a non-directed task setting, or in a setting in which there is no diagrammatic attention mechanism present. In this study we present a non-directed task of cardinality validation and focus on the effectiveness of a diagrammatic attention mechanism. We compare the graphical representation to an informationally equivalent sentential representation. As presented in Figure 1 and Table 1 (above), we compare aggregated and binary (disaggregated) graphical and sentential representations. The binary graphical representation has an inherent diagrammatic attention direction mechanism, i.e., the user is forced to focus on only one binary set at a time, and the user does not need to keep track of which sets have already been evaluated. The aggregated graphical representation does not possess any inherent diagrammatic attention mechanism. The sentential representations possess an inherent linear attention direction mechanism, irrespective of binary or aggregate presentation.

To test whether there is a need for a diagrammatic attention direction mechanism in a non-directed task, we examine the cardinality validation task and propose the following hypothesis:

H1: Users of the diagrammatic aggregate ER representation will perform worse in identifying cardinality errors than users of representations that possess an attention direction mechanism. Further, users of informationally equivalent representations that possess an attention direction mechanism will perform in an equivalent manner. Stated differently:

$$
\begin{array}{l} M I S T A K E _ {d i a g, a g g} > M I S T A K E _ {s e n t, a g g} = M I S T A K E _ {s e n t, d i s a g g} = M I S T A K E _ {d i a g, d i s a g g} \\ \text {wherein MISTAKE indicates mistakes made in identifying seeded cardinality errors.} \end{array}
$$

H1 alone is insufficient to draw conclusions regarding attention management. Participants may make mistakes in identifying illogical cardinalities as a result of not attending to them; however, they may just as likely have attended to the cardinalities but not recognized them as erroneous. Such seeded errors are analogous to the moderate or difficult questions that instructors include on exams to differentiate those who have studied and gained a deep understanding of the course concepts from those who have exerted minimal effort and can answer only the easy exam questions. The seeding of cardinalities representing illegal syntax errors in the models is similar to the inclusion of the easiest of exam questions.

Every participant in the study demonstrated knowledge of the allowed values for maximum cardinalities (1 and N) and for minimum cardinalities (0 and 1). Therefore, any failure on their part to identify the ―illegal‖ seeded errors (i.e., minimum cardinalities stated as N or maximum cardinalities stated as 0) must be a result of the participants not attending to these cardinalities. Such syntax errors, simply put, should be identified. However, based on the discussion above, we maintain that when the ER model structure is diagrammatic and aggregate, participants will not effectively manage their attention and will make mistakes identifying illegal syntax errors. A more stringent test of the diagrammatic attention management theory is to examine evidence that the impairment on cardinality validation is due to lack of attention (rather than misunderstandings or logic errors). Hence we specifically examine the validation of syntactically disallowed cardinalities and propose:

H2: Users of the diagrammatic aggregate ER representation will perform worse in identifying illegal syntax cardinality errors than the users of representations that possess an attention direction mechanism. Further, users of informationally equivalent representations that possess an attention direction mechanism will perform in an equivalent manner. Stated differently:

$$
I L L E G A L _ {d i a g, a g g} > I L L E G A L _ {s e n t, a g g} = I L L E G A L _ {s e n t, d i s a g g} = I L L E G A L _ {d i a g, d i s a g g}
$$

wherein ILLEGAL indicates mistakes made in identifying illegal syntax cardinality errors.

## 3. Research Method

## 3.1. Design

The experimental design in this study is a 2 x 2 between-subjects design with participants randomly assigned to treatments. The first factor is ER representation: diagrammatic or sentential. The second factor is ER composition: aggregate or disaggregate. We measured participants’ cardinality knowledge and included it as a covariate in the statistical analysis. Figure 2 depicts the research model.

## 3.2. Participants

The participants were 87 graduate students (all had approximately one year of auditing experience) and 113 undergraduate students (none of whom had significant work experience, although a few had auditing internships) enrolled in information systems courses. Participants completed the task as an inclass exercise and received class credit for participation. The participants were enrolled in similar courses at two different universities, and were taught by the same instructor, who is one of this study’s authors. All students were in their first information systems course (subsequent data analysis revealed no differences between undergraduate and graduate students). Conceptual modeling was the common theme running through both courses, and students received a high level of exposure to conceptual modeling concepts. As part of the students' course work, they were taught ER modeling in both diagrammatic and sentential formats, and were held accountable for interpreting both the diagrammatic and sentential representations on exams. While students were held responsible for both formats, most of the class examples (and homework assignments) used the diagrammatic aggregate format (which, if anything, would bias against our hypotheses), consistent with the textbook and most other information systems courses. In conjunction with ER modeling, students were taught the Resources-Events-Agents (REA) domain ontology for accounting (McCarthy, 1982; Geerts & McCarthy, 1999; 2000; 2002; 2005). This ontology provides specific guidance for what entities and relationships are expected to exist in business conceptual models, and outlines common participation cardinalities for those relationships.

![](/api/attachments/JD9QZFBC/fulltext/images/296b3c851357897f4b67532eb240b9175454fb88f425c806433191f076239d47.jpg)

## Figure 2. Research Model

Recent research (e.g., Parsons & Cole, 2005; Khatri, Vessey, Ramesh, Clay, & Park, 2006) has addressed the effect of background knowledge on the interpretation and understanding of conceptual models. To control for our participants background knowledge, we rely on random assignment to treatments to randomly distribute the effect of background knowledge. Additionally, as noted in the discussion of variables below, we statistically control for cardinality knowledge with a covariate.

## 3.3. Task and Materials

The task involved validating cardinalities in an ER conceptual model of an acquisition cycle. Each of the four treatments had the same conceptual model (the models were informationally equivalent), but with the representation and composition manipulated. The conceptual models had a set of 16 relationships into which illegal (i.e., a minimum cardinality of ―N‖ or a maximum cardinality of ―0‖) and illogical (e.g., a purchasing agent only relating to at most one purchase requisition, or maximum cardinality of ―1‖ instead of ―N‖) errors had been seeded. The participants received the following instructions: ―Please examine the partial REA model carefully and identify all cardinality errors that exist. Circle each incorrect minimum and/or maximum cardinality, AND write in the correct cardinality. Leave unmarked any cardinality you believe is correct.‖ The following key points were emphasized in the instructions:

• This model is only one part of an enterprise-wide model, that is, some of the entities in this model may also be part of other business processes in the enterprise-wide model.

• For relationships between an internal agent and an event, assume there is never an alternative internal agent performing the same function with respect to that event. There may be an additional internal agent performing a different function and, therefore, participating in a different relationship with that event.

• All inventory is ―catalog‖ style inventory, i.e., pens, CDs, etc. (as opposed to specifically identified inventory) and, therefore, is called ―inventory type.‖

• No unreasonable/irrational business policies should be assumed.

• Some relationships may contain multiple cardinality errors; some relationships may contain just one cardinality error; some relationships may contain zero cardinality errors.

The research instruments for the diagrammatic/aggregate and sentential/aggregate treatments are shown in Appendices A and B, respectively. The diagrammatic/disaggregate and sentential/disaggregate treatments are not shown but can be inferred from Appendices A and B and the illustration in Figure 1. The research instruments were available to participants for the duration of the task.

## 3.4. Variables

The dependent variables are the total number of mistakes, and total number of illegal mistakes, made in the validation task (identifying the seeded cardinality errors). The seeded errors included both illogical and illegal types described below. To develop the grading scale, we asked an expert who was blind to the research question to identify cardinality errors in each of the relationships. The expert (an information systems professor familiar with the REA ontology who has been teaching conceptual modeling for more than 20 years) identified and classified the errors as illegal, illogical, or debatable. Illegal errors were defined as those that are not allowed in participation cardinalities. For example, an entity is not allowed to have minimum participation in a relationship of many (―N‖) – the only legal values are ―0‖ (zero) and ―1‖ (one). Although a minimum cardinality greater than one may be appropriate for some situations, these participants had been taught that the only legal values for minimum cardinalities are zero and one (the convention used in Batini et al., 1992). An entity is not allowed to have maximum participation in a relationship of zero (only one and many are legal values for maximum participation). A maximum cardinality of a specific number may be appropriate in some cases, however, the participants were taught that the only legal values for maximum cardinalities are ―1‖ (one) and ―N‖ (many).

Illogical errors were defined as those that do not conform to common business practice and are incorporated into the REA domain ontology. Because the REA ontology is for modeling business exchanges, it requires some specific treatments of cardinalities. For example, maximum participation of employees (e.g., a salesperson) in relationships with accounting transactions (e.g., sales) should be ―many‖ rather than ―one.‖ A maximum of one would indicate that the enterprise has forbidden its employees to make more than one accounting transaction (and a salesperson needs to be able to make more than one sale). A second example is that when an accounting transaction (e.g., a sale) occurs, it must involve an employee (e.g., a salesperson) for accountability purposes. A third example is that when inventory is represented as a type (e.g., an ISBN for a book), the REA ontology requires that it be modeled with a maximum cardinality of ―many‖ when involved with sale or purchase transactions. Illogical errors were seeded based on all of these examples. The expert was given an option of using ―debatable‖ as a classification for those errors that were illogical for most common business enterprises but for which exceptions are reasonable (the expert identified only one cardinality as debatable, and we excluded it from our analysis). All participants demonstrated an understanding that a minimum cardinality cannot be ―N‖ and that a maximum cardinality cannot be ―0‖ in a pre-test. Therefore, any of the illegal seeded errors not identified may be assumed to result from inhibited processing of those cardinalities; they did not attend to them. There were a total of 10 illogical and four illegal seeded errors.

We included participants’ knowledge of cardinalities as a covariate. We measured cardinality knowledge as participants’ scores on a set of multiple-choice questions that tested their ability to identify either the correct cardinality notation to correspond to a narrative or the correct narrative to correspond to cardinality.

## 4. Results

Before testing the hypotheses, we examined the data for group differences between the undergraduates and graduates. As there was no statistically significant difference between the groups, we combined undergraduate and graduate data for hypothesis testing. We also evaluated assumptions underlying ANCOVA including homogeneity of variance and homogeneity of regression, and we determined that it was appropriate to use ANCOVA.

The first hypothesis predicts that a lack of an attention directing mechanism will result in an interaction between ER representation and ER composition and will affect the number of mistakes that people will identify when validating participation cardinalities. Specifically, Hypothesis 1 predicts that more validation mistakes will be made when the ER structure is diagrammatic/aggregate and that there will be no difference between the other three ER structures (sentential/aggregate, sentential/disaggregate, and diagrammatic/ disaggregate).

To test the first hypothesis, we performed an analysis of covariance (ANCOVA). Mistakes in identifying cardinality errors were analyzed as a function of ER representation and ER composition with cardinality knowledge as a covariate. Table 2 presents the two main effects, interaction, and covariate. We tested for interactions between the covariate and the two main effects. There were no statistically significant interactions involving the covariate, so Table 2 reports the reduced model without covariate interactions. The interaction between representation and composition is statistically significant [F (1, 195) = 4.3, p < .05]. We analyzed the interaction by graphing the least squares means and tests of their differences. The covariate adjusted least squares means are shown in Table 3, panel A and plotted in Figure 3.

Table 2. Analysis of Covariance of Total Mistakes as a Function of Representation and Composition, With Cardinality Knowledge as Covariate

<table><tr><td>Source</td><td>df</td><td>MS</td><td>F</td><td>p</td></tr><tr><td colspan="5">Covariate:</td></tr><tr><td>Cardinality Knowledge</td><td>1</td><td>69.8</td><td>15.1</td><td>&lt; 0.001</td></tr><tr><td colspan="5">Main Effects:</td></tr><tr><td>Representation</td><td>1</td><td>11.3</td><td>2.4</td><td>0.120</td></tr><tr><td>Composition</td><td>1</td><td>16.4</td><td>3.6</td><td>0.061</td></tr><tr><td colspan="5">Interaction:</td></tr><tr><td>Representation x Composition</td><td>1</td><td>20.0</td><td>4.3</td><td>0.039</td></tr><tr><td>Residual</td><td>195</td><td>4.6</td><td></td><td></td></tr></table>

As Table 3 and Figure 3 illustrate, the least squares mean number of validation mistakes made in the diagrammatic/aggregate condition $( \mathsf { L S M } = 3 . 0 , ^ { \cdot } \mathsf { S E } = 0 . 3 ;$ Cell A in Table 3) is greater than in the other three conditions; Cell B (LSM = 1.9, SE = 0.3), Cell C (LSM =1.8, SE = 0.3), and Cell D (LSM = 2.0, SE = 0.3). Table 3, panel B shows the p-values testing the null hypothesis that the least squares means of the cells are equal (bivariate comparisons). The difference between diagrammatic/aggregate and the other three conditions is statistically significant. The above analysis supports Hypothesis 1, that a lack of diagrammatic attention directing mechanism results in worse performance than when a diagrammatic attention directing mechanism is present.

The second hypothesis is a more stringent test of the diagrammatic attention direction theory, and focuses only on the illegal mistakes that participants should identify (and which all participants understood were illegal in a pre-test). Hypothesis 2 predicts the same pattern of results as Hypothesis 1, except that only illegal mistakes were examined.

![](/api/attachments/JD9QZFBC/fulltext/images/ad11283bf93a2c86dc68c1515a45e26adb846719fb0cb3ebcdfe44c4dc55f744.jpg)  
Figure 3. Graph of Representation X Composition Interaction

Table 3. Panel A: Covariate Adjusted Least Squares Means (Standard Errors) [n] of Total Mistakes by Treatment

<table><tr><td rowspan="2"></td><td colspan="2">Representation</td></tr><tr><td>Diagrammatic</td><td>Sentential</td></tr><tr><td>Composition</td><td>LSM(SE)[n]Cell</td><td>LSM(SE)[n]Cell</td></tr><tr><td>Aggregate</td><td>3.0(0.3)[48]Cell A</td><td>1.9(0.3)[51]Cell B</td></tr><tr><td>Disaggregate</td><td>1.8(0.3)[50]Cell C</td><td>2.0(0.3)[51]Cell D</td></tr></table>

Table 3. Panel B: P-values from Testing Null Hypotheses that the Least Squares Means of Table 2 Cells are Equal (Bivariate Comparisons)

<table><tr><td></td><td>Cell A</td><td>Cell B</td><td>Cell C</td></tr><tr><td>Cell A</td><td></td><td></td><td></td></tr><tr><td>Cell B</td><td>0.015</td><td></td><td></td></tr><tr><td>Cell C</td><td>0.006</td><td>0.722</td><td></td></tr><tr><td>Cell D</td><td>0.011</td><td>0.896</td><td>0.823</td></tr></table>

To test the second hypothesis, we again performed an analysis of covariance (ANCOVA). We analyzed mistakes in identifying illegal syntax cardinality errors as a function of ER representation and ER composition, with cardinality knowledge as a covariate. Table 4 presents the two main effects, interaction, and covariate. As above, we tested for interactions between the covariate and the two main effects. Again, there were no statistically significant interactions involving the covariate. Consequently, Table 4 reports the reduced model without covariate interactions. The interaction between representation and composition is not statistically significant at conventional significance levels [F (1, 195) = 3.1, p > .05]. We analyzed the interaction by examining least squares means and testing their differences. Table 5, panel A shows the covariate adjusted least squares means, and Table 5, panel B shows the p-values for the testing of the null hypothesis that the least squares means of the cells are equal (bivariate comparisons).

Table 4. Analysis of Covariance of Total Illegal Mistakes as a Function of Representation and Composition, With Cardinality Knowledge as Covariate

<table><tr><td>Source</td><td>df</td><td>MS</td><td>F</td><td>p</td></tr><tr><td colspan="5">Covariate:</td></tr><tr><td>Cardinality Knowledge</td><td>1</td><td>0.2</td><td>0.7</td><td>0.414</td></tr><tr><td colspan="5">Main Effects:</td></tr><tr><td>Representation</td><td>1</td><td>0.5</td><td>1.5</td><td>0.227</td></tr><tr><td>Composition</td><td>1</td><td>2.0</td><td>5.6</td><td>0.019</td></tr><tr><td colspan="5">Interaction:</td></tr><tr><td>Representation x Composition</td><td>1</td><td>1.1</td><td>3.1</td><td>0.079</td></tr><tr><td>Residual</td><td>195</td><td>0.4</td><td></td><td></td></tr></table>

Table 5. Panel A: Covariate Adjusted Least Squares Means (Standard Errors) [n] of Total Illegal Mistakes by Treatment

<table><tr><td rowspan="2"></td><td colspan="2">Representation</td></tr><tr><td>Diagrammatic</td><td>Sentential</td></tr><tr><td>Composition</td><td>LSM(SE)[n]Cell</td><td>LSM(SE)[n]Cell</td></tr><tr><td>Aggregate</td><td>0.8(0.1)[48]Cell A</td><td>0.2(0.1)[51]Cell B</td></tr><tr><td>Disaggregate</td><td>0.1(0.1)[50]Cell C</td><td>0.2(0.1)[51]Cell D</td></tr></table>

Table 5. Panel B: P-values from Testing Null Hypotheses that the Least Squares Means of Table 4 Cells are Equal (bivariate comparisons)

<table><tr><td></td><td>Cell A</td><td>Cell B</td><td>Cell C</td></tr><tr><td>Cell A</td><td></td><td></td><td></td></tr><tr><td>Cell B</td><td>0.012</td><td></td><td></td></tr><tr><td>Cell C</td><td>0.004</td><td>0.704</td><td></td></tr><tr><td>Cell D</td><td>0.038</td><td>0.661</td><td>0.420</td></tr></table>

As detailed in Table 5, the least squares mean number of validation mistakes made in identifying illegal participation cardinalities is greater in the diagrammatic/aggregate condition, (LSM = 0.8, SE = 0.1; Cell A in Table 5) than in the other three conditions; Cell B (LSM = 0.2, SE = 0.1), Cell C (LSM = 0.1, SE = 0. 1), and Cell D $\mathsf { L S M } = 0 . 2 , \mathsf { S E } = 0 . 1 )$ . The difference between diagrammatic/aggregate and the other thr ee conditions is statistically significant as shown in Table 5, panel B, supporting Hypothesis 2.

Although the results for the total mistakes and total illegal mistakes support the hypotheses, the effect size was relatively low. Since the participants had a reasonable understanding of the domain and the diagrams were small, we did not expect a large effect size. However, with the much larger diagrams used in practice, our theory would suggest a correspondingly larger effect size.

We performed additional analysis using Poisson regression and negative binomial regression (models for count dependent variables). Results from this analysis were consistent with the ANCOVA analysis presented above and, hence, are not reported in this paper. We also conducted additional analysis to determine whether one specific seeded error was accountable for the results. To do this, we repeated the above ANCOVA analysis. Specifically, we re-estimated 14 models in which one specific seeded error (varying across models) was excluded from one ANCOVA model. For example, the first model was estimated without the first seeded error (and with the 13 other seeded errors), then in the second model, we added back the first seeded error and dropped the second seeded error from the analysis, and so on (recall there were 14 errors in total, so each of the re-estimated models had 13 possible mistakes instead of 14). If one specific error was accountable for the results, then the pattern of results should have changed when that specific error was excluded from analysis. However, that did not happen. For all 14 models that were re-estimated, we found exactly the same pattern of results: on average, participants in the diagrammatic/aggregate condition made more errors than participants in the other three conditions (and the three conditions did not differ from each other).

As a result of this analysis, one conclusion we can draw is that the overlapping relationship lines (see the participate5 and participate6 relationships in Appendix A) that are a feature of the diagrammatic/aggregate condition (but not features of the other three conditions) are not influencing the results. We are not suggesting that overlapping relationship lines do not interfere with the search process, but at least in this setting, that one difference is not responsible for the results. Rather, the results are driven by the lack of a diagrammatic attention management mechanism in the diagrammatic/aggregate condition. All other factors are equal between cells.

## 5. Discussion, Future Research Directions, and Conclusion

This research proposes and tests a theory of diagrammatic attention management. In particular, when individuals are asked to perform a non-directed task using a diagram with no inherent attention directing mechanism, they will perform worse than individuals who are provided with a diagrammatic attention directing mechanism. This performance difference exists even when all the information that is needed for each individual step in the task is localized on the diagram (i.e., is presented contiguously). This research extends prior research that focused only on the need for contiguous presentation of information (e.g., Larkin & Simon, 1987; Dunn & Grabski, 2001; Mayer, 2001; Mayer & Moreno, 2002; and Reed, 2006).

In this research, we specifically examined the effects of conceptual model structure in the form of representation (diagrammatic or sentential) and composition (model is presented as an aggregate model or disaggregated into a series of binary relationships) for cardinality validation tasks. We selected this task because it had been used in a variety of contexts (e.g., Siau, Wand, & Benbasat, 1997; Dunn & Gerard, 2001; Dunn et al., 2005). Further, the task is non-trivial, and incorrect cardinalities can result in significant dollar impacts (Arlow et al., 1999), and realistic with respect to system analysis in practice (Wastell, 1996). We report that decision performance in validating conceptual model cardinality decreases in only one treatment, the diagrammatic/aggregate conceptual model, compared to the other three treatments. Participants in the diagrammatic/disaggregate, sentential/aggregate, and sentential/disaggregate treatments performed significantly better than those in the diagrammatic/aggregate treatment, and the performances of the latter three were not significantly different from each other. Furthermore, the performance degradation does not appear to be related to information overload, as informationally equivalent models were presented in all treatment conditions. What did differ was the absence (presence) of an attention directing mechanism. The diagrammatic/disaggregate structure possesses an attention direction mechanism; the user attends to one binary set and then proceeds to the next binary set. The sentential aggregate and disaggregate representations possess an inherent linear attention directing mechanism. Only the diagrammatic aggregate representation lacks an attention directing mechanism, and it is in this setting that participants performed the worst.

An important implication of this research is that the usual practice employed by both researchers and practitioners of creating and using conceptual models with a diagrammatic/aggregate structure is not appropriate for all tasks. When a high level perspective of the information system is required, diagrammatic/aggregate structures may be appropriate. On the other hand, the diagrammatic/aggregate structure does not seem to be appropriate for cardinality verification. The ER model used in this study contained only 10 entities and 16 relationships. Such a model would be considered relatively small and simple in practice. Therefore, our results most likely underestimate the significance of the effect. Future research could investigate models of different complexity and of different, perhaps less familiar, domains. Furthermore, this effect occurred within a domain ontology familiar to the participants. They only needed to attend to the validation task; they did not need to learn about the domain as in Gemino (2004). As future research continues to identify different tasks by conceptual model structure interactions, researchers could employ design science methods to develop tools to match the model structure to a specific task. For example, if the task is conceptual model validation, the tool could present the user with a model that is structured to support linear search such as the diagrammatic/disaggregate structure in this paper. Alternatively, a tool could be developed to present diagrammatic/aggregate models for other purposes such as facilitating model comprehension or determining the completeness of a model. It is also possible that users may prefer different formats (e.g., text versus diagram) and tools could be developed to translate between formats to allow users to choose their preferred format.

An implication of this research is that ER diagrams (and potentially any conceptual model) should be presented in a disaggregate structure, or in a sentential structure for validation tasks. This is particularly true for cardinality validation. There is evidence that for some types of tasks (search, recognition, and inference), ER diagrams are more efficient than sentential representations (Dunn & Gerard, 2001). Furthermore, experience with patterned diagrammatic/aggregate ER models is associated with designers’ memory organization (Gerard, 2005). A key benefit of diagrammatic/aggregate conceptual models is that users can see each entity’s participation in multiple relationships. As an example, if a sale event could be handled by a manager or a clerk, and the manager and clerk are represented as separate entities, viewing separate binary relationships may lead to changing the zero minimum participation on the event to one when it really should be zero; whereas, if the relationships are viewed simultaneously, the user may realize that the minimum participation should be zero. In this study we controlled for this situation by specifying in the instructions that only one type of internal agent participates in each event. In practice, however, this cannot be controlled or assumed away. Although we disaggregated our diagrammatic and sentential representations by binary relationships, it might not be necessary to do this. Future research could investigate alternative methods of decomposing conceptual models.

Given the prevalence of diagrammatic/aggregate design representation techniques (e.g., ER diagrams, Data Flow Diagrams, UML Diagrams, Business Process Diagrams), the findings of this research have implications for any information systems documentation approach. Other modeling approaches should be examined to determine how structure affects users’ performance and how performance can be improved. For example, researchers have examined user query performance as it relates to conceptual models (e.g., Borthick, Bowen, Jones, & Tse, 2001; Debreceny & Bowen, 2005). Can conceptual model structure improve query performance? Researchers have also used conceptual models as a key part of ontology research (e.g., Wand & Weber, 1993; 1995; Weber, 1997; Bodart et al., 2001; Bowen, O’Farrell, & Rhode, 2006). Much of the ontology research has implications for conceptual models with more ontological clarity. However, ontologically clear conceptual models can end up having more constructs that could lead to information overload. It is possible that the increase in constructs could be controlled via representations that support linear information search to enhance user performance.

More complete specification and tests of the theory of diagrammatic attention management are needed to examine whether results are similar in other contexts and with other types of diagrams such as graphs, maps, charts, or technical drawings. While additional testing is needed, the results of this study are compelling and contribute to our understanding of cardinality validation as affected by conceptual model structure.

## References

Arlow, J., Emmerich, W., & Quinn, J. (1999). Literate modelling — Capturing business knowledge with the UML. In J. Bézivin & P. A. Muller (Eds.) UML '98, Lecture Notes in Computer Science (1618), 189-199. London: Springer-Verlag.

Batini C., Ceri, S., & Navathe, S. B. (1992). Conceptual database design: An entity-relationship approach. Redwood City, California: Benjamin/Cummings.

Bodart, F., Patel, A., Sim, M., & Weber, R. (2001). Should optional properties be used in conceptual modeling? A theory and three empirical tests. Information Systems Research, 12(4), 384-405.

Boehm, B. W. (1989). Software risk management. Washington, DC: IEEE Computer Society Press.

Borthick, A. F., Bowen, P. L., Jones, D. R., & Tse, M. H. K. (2001). The effects of information request ambiguity and construct incongruence on query development. Decision Support Systems, 32(1), 3-25.

Bowen, P. L., O’Farrell, R. A., & Rhode, F. H. (2006). Analysis of competing data structures: Does ontological clarity produce better end user query performance. Journal of the Association for Information Systems, 7(8), 514-544.

Burton-Jones, A., & Meso, P. N. (2006). Conceptualizing systems for understanding: An empirical test of decomposition principles in object-oriented analysis. Information Systems Research, 17(1), 38-60.

Burton-Jones, A., Wand, Y., & Weber, R. (2009). Guidelines for empirical evaluations of conceptual modeling grammars. Journal of the Association for Information Systems, 10(6), 495-532.

Chen, P. P. (1976). The entity-relationship model – Toward a unified view of data. ACM Transactions on Database Systems, 1(1), 9-36.

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. Behavioral and Brain Science, 24(1), 87-114.

Debreceny, R. S., & Bowen, P. L. (2005). The effects on end-user query performance of incorporating object-oriented abstractions in database accounting systems. Journal of Information Systems, 19(1), 43-74.

Dobing, B., & Parsons, J. (2006). How UML is used. Communications of the ACM, 49(5), 109-113.

Dobing, B., & Parsons, J. (2008). Dimensions of UML diagram use: A survey of practitioners. Journal of Database Management, 19(1), 1-18.

Dunn, C. L., & Gerard, G. J. (2001). Auditor efficiency and effectiveness with diagrammatic and linguistic conceptual model representations. International Journal of Accounting Information Systems, 2(4), 223-248.

Dunn, C. L., Gerard, G. J., & Grabski, S. V. (2005). Critical evaluation of conceptual data models. International Journal of Accounting Information Systems, 6(2), 83-106.

Dunn, C. L., & Grabski, S. V. (2001). An investigation of localization as an element of cognitive fit in accounting model representations. Decision Sciences, 32(1), 44-94.

Geerts, G., & McCarthy, W. E. (1999). An accounting object infrastructure for knowledge-based enterprise models. IEEE Intelligent Systems & Their Applications, 14(4), 89-94.

Geerts, G., & McCarthy, W. E. (2000). Augmented intensional reasoning in knowledge-based accounting systems. Journal of Information Systems, 14(2), 127-150.

Geerts, G., & McCarthy, W. E. (2002). An ontological analysis of the primitives of the extended-REA enterprise information architecture. International Journal of Accounting Information Systems, 3(1), 1-16.

Geerts, G., & McCarthy, W. E. (2005). The ontological foundation of REA enterprise information systems. Working paper, Michigan State University.

Gemino, A. (2004). Empirical comparisons of animation and narration in requirements validation. Requirements Engineering, 9(3), 153-168.

Gemino, A., & Parker, D. (2009). Use case diagrams in support of use case modeling: Deriving understanding from the picture. Journal of Database Management, 20(1), 1-24.

Gemino, A., & Wand, Y. (2004). A framework for empirical evaluation of conceptual modeling techniques. Requirements Engineering, 9(4), 248–260.

Gemino, A., & Wand, Y. (2005). Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data & Knowledge Engineering, 55(3), 301-326.

Gerard, G. J. (2005). The REA pattern, knowledge structures, and conceptual modeling performance. Journal of Information Systems, 19(2), 57-77.

Glenn, D. (2010). Divided attention. The Chronicle of Higher Education. http://chronicle.com/article/Scholars-Turn-Their-Attention/63746/

Goswami, S., Chan, H. C., & Kim, H. W. (2008). The role of visualization tools in spreadsheet error correction from a cognitive fit perspective. Journal of the Association for Information Systems, 9(6), 321-343.

Khatri, V., Vessey, I., Ramesh, V., Clay, P., & Park, S. (2006). Understanding conceptual schemas: Exploring the role of application and IS domain knowledge. Information Systems Research, 17(1), 81-99.

Kim, J., Hahn, J., & Hahn, H. (2000). How do we understand a system with (so) many diagrams? Cognitive integration processes in diagrammatic reasoning. Information Systems Research, 11(3), 284-303.

Kim, Y., & March, S. T. (1995). Comparing data modeling formalisms. Communications of the ACM, 38(6), 103-115.

Kung, C. H., & Sø lvberg, A. (1986). Activity modeling and behaviour modeling. In T. W. Olle, H. G. Sol, & A. A. Verrijn-Stuart (Eds.) Information system design methodologies: Improving the practice (pp. 145-171). The Netherlands: North-Holland.

Larkin, J. H., & Simon, H. A. (1987). Why a diagram is (sometimes) worth ten thousand words. Cognitive Science, 11(1), 65-99.

Lindland, O. I., Sindre, G., & Sølvberg, A. (1994). Understanding quality in conceptual modeling. IEEE Software, 11(2), 42-49.

Mayer, R. E. (2001). Multimedia Learning. Cambridge, UK: Cambridge University Press.

Mayer, R. E., & Moreno, R. (2002). Aids to computer-based multimedia learning. Learning and Instruction, 12(1), 107-119.

McCarthy, W. E. (1982). The REA accounting model: A generalized framework for accounting systems in a shared data environment. The Accounting Review, 57(3), 554-578.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81-97.

Moher, T. G., Mak, D. C., Blumenthal, B., & Leventhal, L. M. (1993). Comparing the comprehensibility of textual and graphical programs: The case of Petri Nets. In C. R. Cook, J. C. Scholtz, & J. C. Spohrer (Eds.) Empirical Studies of Programmers: Fifth Workshop (pp. 137-161) December, Palo Alto, California.

Moody, D. L. (1998). Metrics for evaluating the quality of entity relationship models. In T. W. Ling, S. Ram, & M. L. Lee (Eds.) Proceedings of the International Conference on Conceptual Modeling (ER ‟98), Lecture Notes in Computer Science (pp. 211-225). Berlin: Springer-Verlag.

Mylopoulos, J. (1992). Conceptual modeling and telos. In P. Loucopoulos, & R. Zicari (Eds.) Conceptual modeling, databases, and CASE: An integrated view of information systems development (pp. 49-68). New York: John Wiley & Sons.

Parsons, J., & Cole, L. (2005). What do the pictures mean? Guidelines for experimental evaluation of representation fidelity in diagrammatical conceptual modeling techniques. Data & Knowledge Engineering, 55(3), 327-342.

Petre, M. (1995). Why looking isn’t always seeing: Readership skills and graphical programming. Communications of the ACM, 38(6), 33-44.

Reed, S. K. (2006). Cognitive architectures for multimedia learning. Educational Psychologist, 41(2), 87-98.

Rumbaugh, J., Jacobson, I., & Booch, G. (1999). The unified modeling language reference manual. Reading, MA: Addison-Wesley.

Siau, K. (2004). Informational and computational equivalence in comparing information modeling methods. Journal of Database Management, 15(1), 73-86.

Siau, K., & Tan, X. (2005). Improving the quality of conceptual modeling using cognitive mapping techniques. Data & Knowledge Engineering, 55(3), 343-365.

Siau, K., Wand, Y., & Benbasat, I. (1997). The relative importance of structural constraints and surface semantics in information modeling. Information Systems, 22(2-3), 155-170.

Vessey, I. (1991). Cognitive fit: A theory-based analysis of the graphs versus tables literature. Decision Sciences, 22(2), 219-240.

Vessey, I. (1994). The effect of information presentation on decision making: A cost-benefit analysis. Information and Management, 27(2), 103-119.

Vessey, I. (2006). The theory of cognitive fit: One aspect of a general theory of problem solving? In P. Zhang & D. Galletta (Eds.), Human-computer interaction and management information systems: Foundations (pp. 141-183). Armonk, NY: M.E. Sharpe.

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information system analysis and design grammars. Information Systems Journal, 3(4), 217-237.

Wand, Y., & Weber, R. (1995). On the deep structure of information systems. Information Systems Journal, 5(3), 203-223.

Wand, Y., & Weber, R. (2002). Research commentary: Information systems and conceptual modeling – A research agenda. Information Systems Research, 13(4), 363-376.

Wastell, D. G. (1996). The fetish of technique: Methodology as a social defense. Information Systems Journal, 6(1), 25-40.

Weber, R. (1997). Ontological foundations of information systems. Melbourne, Australia: Coopers & Lybrand.

Yourdon, E. (1989). Modern structured analysis. Englewood Cliffs, NJ: Prentice-Hall.

## Appendix

Appendix A. Acquisition Cycle ER Model in Diagram Format (Diagram/ Aggregate).

![](/api/attachments/JD9QZFBC/fulltext/images/6fb29fde8d0b9a90b4533ce66a6bed2011cfd7529132a114f69ea65a63844ee6.jpg)

## Figure A-1. Acquisition cycle ER model in diagram format (diagram/aggregate).

Entity: Accounts Payable Clerk Entity: Department Supervisor Entity: Cash Entity: Cash Disbursement Entity: Inventory Type Entity: Purchase Entity: Purchase Order Entity: Purchase Requisition Entity: Purchasing Agent Entity: Vendor

(continued on next page)

Journal of the Association for Information Systems Vol. 12 Issue 8 pp.585-605 August 2011

<table><tr><td>Relationship:</td><td>Duality</td></tr><tr><td>Connected Entities:</td><td>(0,1) Purchase(N,1) Cash Disbursement</td></tr><tr><td>Relationship:</td><td>Fulfillment1</td></tr><tr><td>Connected Entities:</td><td>(1,0) Purchase Order(0,1) Purchase Requisition</td></tr><tr><td>Relationship:</td><td>Fulfillment2</td></tr><tr><td>Connected Entities:</td><td>(1,1) Purchase(0,1) Purchase Order</td></tr><tr><td>Relationship:</td><td>Participate1</td></tr><tr><td>Connected Entities:</td><td>(1,1) Purchase Requisition(1,N) Department Supervisor</td></tr><tr><td>Relationship:</td><td>Participate2</td></tr><tr><td>Connected Entities:</td><td>(0,1) Purchase Requisition(0,N) Vendor</td></tr><tr><td>Relationship:</td><td>Participate3</td></tr><tr><td>Connected Entities:</td><td>(1,1) Purchase Requisition(0,1) Purchasing Agent</td></tr><tr><td>Relationship:</td><td>Participate4</td></tr><tr><td>Connected Entities:</td><td>(0,1) Purchase Order(0,N) Purchasing Agent</td></tr><tr><td>Relationship:</td><td>Participate5</td></tr><tr><td>Connected Entities:</td><td>(1,N) Purchase Order(0,N) Vendor</td></tr><tr><td>Relationship:</td><td>Participate6</td></tr><tr><td>Connected Entities:</td><td>(1,1) Purchase(1,0) Purchasing Agent</td></tr><tr><td>Relationship:</td><td>Participate7</td></tr><tr><td>Connected Entities:</td><td>(1,1) Purchase(0,N) Vendor</td></tr><tr><td>Relationship:</td><td>Participate8</td></tr><tr><td>Connected Entities:</td><td>(1,1) Cash Disbursement(0,N) Vendor</td></tr><tr><td>Relationship:</td><td>Participate9</td></tr><tr><td>Connected Entities:</td><td>(1,1) Cash Disbursement(0,1) AP Clerk</td></tr><tr><td>Relationship:</td><td>Proposition</td></tr><tr><td>Connected Entities:</td><td>(1,N) Purchase Requisition(0,1) Inventory Type</td></tr><tr><td>Relationship:</td><td>Reservation</td></tr><tr><td>Connected Entities:</td><td>(N,N) Purchase Order(0,N) Inventory Type</td></tr><tr><td colspan="2">(continued on next page)</td></tr><tr><td>Relationship:</td><td>Stockflow1</td></tr><tr><td>Connected Entities:</td><td>(1,1) Purchase(0,N) Inventory Type</td></tr><tr><td>Relationship:</td><td>Stockflow2</td></tr><tr><td>Connected Entities:</td><td>(1,N) Cash(1,1) Cash Disbursement</td></tr></table>

## About the Authors

Cheryl L. DUNN is an Associate Professor at Grand Valley State University. She earned her PhD at Michigan State University and was a faculty member at Florida State University prior to her current position. Her primary research interests are conceptual modeling, enterprise information system design, semantic technology, and transformation of financial reporting. She has published in scholarly journals such as Decision Sciences, Journal of Information Systems, International Journal of Accounting Information Systems, and Issues in Accounting Education. She is lead author on the textbook "Enterprise Information Systems: A Pattern-Based Approach", 3e, published by Irwin-McGraw Hill. She has served as book review editor for Journal of Information Systems and on the editorial boards of Issues in Accounting Education, Journal of Database Management, and the International Journal of Accounting Information Systems.

Gregory J. GERARD is an Associate Professor at Florida State University. He is the director of the master of accounting (MAcc) program at FSU. He earned his PhD at Michigan State University. His primary research interests are conceptual modeling, and the design, use, and audit of enterprise information systems. He has published in scholarly journals such as Journal of Information Systems, International Journal of Accounting Information Systems, Auditing: A Journal of Practice & Theory, Review of Accounting and Finance, and Issues in Accounting Education. He was the editor of a special issue of Issues in Accounting Education that focused on information technology. He is an associate editor for the Journal of Emerging Technologies in Accounting and on the editorial board of Journal of Information Systems.

Severin V. GRABSKI is an Associate Professor at Michigan State University. He was a visiting professor at the University of Tasmania. He earned his PhD at Arizona State University. His primary research interests are conceptual modeling and enterprise information system design and use. He has published in scholarly journals such as Decision Sciences, MIS Quarterly, Information Technology & People, Journal of Information Systems, International Journal of Accounting Information Systems, and the Journal of Applied Social Psychology. He has also published chapters in multiple research monographs. He is an associate editor for the International Journal of Accounting Information Systems and for the Journal of Emerging Technologies in Accounting. He is also on the editorial boards of Journal of Information Systems, Journal of Database Management, and Accounting & Finance.
