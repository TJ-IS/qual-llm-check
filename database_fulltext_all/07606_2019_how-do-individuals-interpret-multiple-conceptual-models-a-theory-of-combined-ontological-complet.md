---
otero_id: 7606
otero_key: "9ESHKXZG"
title: "How do Individuals Interpret Multiple Conceptual Models? A Theory of Combined Ontological   Completeness and Overlap"
authors: "Jan Recker; Peter F. Green"
year: "2019"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00565"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
ISSN 1536-9323

# How do Individuals Interpret Multiple Conceptual Models? A Theory of Combined Ontological Completeness and Overlap

Jan Recker<sup>1</sup>, Peter F. Green<sup>2</sup>

<sup>1</sup>University of Cologne, Germany / Queensland University of Technology, Australia, jan.recker@wiso.uni-koeln.de <sup>2</sup>Queensland University of Technology, Australia, p.green@qut.edu.au

## Abstract

When analyzing or designing information systems, users often work with multiple conceptual models because each model articulates a different, partial aspect of a real-world domain. However, the available research in this area has largely studied the use of single modeling artifacts only. We develop a new theory about interpreting multiple conceptual models that details propositions for evaluating how individuals select, understand, and perceive the usefulness of multiple conceptual models. We detail implications of our theory development for empirical research on conceptual modeling. We also outline practical contributions for the design of conceptual models and for choosing models for systems analysis and design tasks. Finally, to stimulate research that builds on our theory, we illustrate procedures for enacting our theory and discuss a range of empirically relevant boundary conditions.

Keywords: Conceptual Modeling, Representation Theory, Combined Ontological Completeness, Ontological Overlap, Model Interpretation, Model Selection, Domain Understanding, Perceived Usefulness.

Sandeep Purao was the accepting senior editor. This research article was submitted on September 28, 2015, and underwent four revisions.

## 1 Introduction

When analyzing or designing information systems (IS), professionals such as process analysts, systems designers, and software developers frequently develop and use representations of the relevant features of a real-world domain that the IS is intended to support. These representations, called conceptual models, describe someone’s or some group’s understanding of a real-world domain and the relevant features or phenomena in that domain (Wand & Weber, 2002).

Conceptual models are developed using grammars— that is, sets of constructs and the rules used to combine them (Wand & Weber, 2002). The traditional focus of the academic literature on conceptual modeling has been on how the quality of grammars and models might be evaluated and improved (Burton-Jones, Wand, & Weber, 2009: Siau & Rossi, 2011). However, the academic literature is inconsistent with practice. IS professionals typically do not use just one conceptual modeling grammar, let alone one conceptual model, in their analysis and design tasks. As we will discuss, they use multiple models, often designed with different grammars, in their systems analysis and design practices. Yet, the extant literature offers no comprehensive theory to explain how practitioners would work with these models or to answer questions such as: Which models should practitioners choose as a representation to help them in an analysis or design task? How should practitioners read multiple models in conjunction with each other? Which models are useful in tandem and which are not?

In this paper, we develop a new theory to analyze and explain the interpretation of multiple conceptual models in combination. We generate research models that specify detailed propositions regarding three important decisions when interpreting multiple models: selecting which models to use, determining how much domain understanding can be generated from multiple models, and explaining the perceived usefulness of conceptual model combinations. Because our aim is to invite future empirical research on conceptual modeling on the basis of theory, we also provide an illustration of the procedures with which the theory can be applied, and we discuss moderator variables that might be relevant in empirical research designs to establish boundary conditions.

To the best of our knowledge, this paper is the first paper to propose a theory that explains the interpretation of multiple conceptual models and is anchored in properties of the models themselves. This issue is important because, generally, when users model system requirements to ensure they clearly understand the requirements, they use many different models. For example, for stakeholders trying to get a sense of the system as a whole, the combination of models and the symbolic constructs within the models may not provide the full picture because they may fail to adequately represent a critical concept; alternatively, they may confuse the stakeholders if different symbols in different models actually represent the same concept. Our work attempts to clearly determine the conditions under which any set of conceptual models can be viewed by stakeholders in a way that minimizes the problem of insufficient or obfuscated understanding. Moreover, while theoretical, our work also informs practice. By clarifying how multiple conceptual models might be meaningfully combined, we provide guidance to modeling practitioners on which model combinations are better for understanding domains, which are worse, and which do not apply to various domains. Our work also informs model designers about model combinations that will likely be of most benefit to future users.

We make one note about the theory development reported in this paper. The theory we produce is not grounded or derived inductively from data (Urquhart & Fernandez, 2013). Rather, it largely builds on established theory (Wand & Weber, 1990, 1993, 1995) and it derives new logic deductively from the premises of that theory. However, our theorizing also uses both formal and informal empirical data sources as the empirical matters that inspire our problematization of both the reported phenomena and the literature available purportedly explaining it (Alvesson & Kärreman, 2007, p. 1265). We rely on our own observations of conceptual modeling practices that we have gathered during many years of fieldwork (e.g., Green, Rosemann, Indulska, & Recker, 2011, Jabbari Sabegh & Recker, 2017) as an informal source of theorizing (Fiske, 2004). We also rely on published cases involving the same practices that inspired us to attempt an explanation of what we believe is a realworld question (Byron & Thatcher, 2016, p. 4): How do analysts and designers interpret multiple models? To answer this question, we engaged in thought experiments seeking explanations that could satisfy our curiosity (Corley & Gioia, 2011). This paper reports the outcomes of this process.

We proceed as follows: First, we review the background relevant to our theorizing—in particular, the available empirical evidence on the use of multiple conceptual models and the available theory base in conceptual modeling research. Next, we formulate our new theory and develop its key propositions in three research models. Finally, we discuss the scope and contributions of our theory and propose a range of implications.

## 2 Background

Two streams of literature inform our theory development. One is the literature that covers the research area of conceptual modeling as a whole. We review this literature first because it helps to position our theory development within the contributions of existing research. Second, we review empirical knowledge on the use of (multiple) conceptual models specifically, because our theory development addresses challenges that stem from an inconsistency between available theoretical knowledge and reported practice when dealing with multiple models.

## 2.1 Research on Conceptual Modeling

Conceptual modeling concerns the development and use of representations of relevant features of a realworld domain that an IS is intended to support (Wand & Weber, 2002). It is an active research area in information systems research with contributions consistently appearing in our top journals (e.g., Parsons, 2011; Recker, 2013; Bera, Burton-Jones, & Wand, 2014; Clarke, Burton-Jones, & Weber, 2016; Khatri & Vessey, 2016; Lukyanenko et al., 2017). Two broad research streams can be distinguished: First, there is a stream of research on the design of representations of relevant features of a real-world domain through the use of conceptual modeling grammars and methods. For example, several studies have focused on how a conceptual model can be created, especially how to design a “better” model (e.g., Gemino & Wand, 2005; Shanks, Tansley, Nuredini, Tobin, & Weber, 2008; Recker, 2013; Clarke et al., 2016). Studies have also demonstrated how the representation that a conceptual model offers can be augmented through design features like colors (Masri, Parker, & Gemino, 2008), text (Gemino & Parker, 2009), and other customizations (Samuel, Watkins, Ehle, & Khatri, 2015). Finally, some studies have examined how practitioners use methods or grammars for the design of conceptual models (Dawson & Swatman, 1999; Purao, Rossi, & Bush, 2002; Recker, Indulska, Rosemann, & Green, 2010).

Second, there is a stream of research on how previously built conceptual models are used for purposes of problem solving or decision-making. Much of this research has focused on how users understand a conceptual model in its entirety (Figl, Mendling, & Strembeck, 2013; Bera et al., 2014), or various elements within it (Bodart, Patel, Sim, & Weber, 2001; Parsons, 2011). Fewer studies have focused on how practitioners interpret a conceptual model for specific analysis and design tasks (Bowen, O’Farrell, & Rohde, 2006; Allen & Parsons, 2010; Figl & Recker, 2016).

With our theory, we contribute to the second broad stream of research on conceptual modeling. Our explicit focus on multiple models, rather than just one model, is a key extension to the conceptual modeling literature. Common to the studies in both streams is a focus on a single artifact—one model or grammar. Studies that employed multiple models or grammars were usually compared to evaluate which one was “better.”

## 2.2 Empirical Evidence on the Use of Multiple Conceptual Models

The starting point for our investigation is an inconsistency between conceptual modeling practice and academic theory. It is common for practitioners to use several conceptual models when analyzing or designing information systems, and they appear to be equipped with some intuition about which models can be combined in purposeful ways. For example, entityrelationship models (Chen, 1976) describe real-world domains in terms of the entities that make up a domain, the attributes that characterize these entities, and the relationships that may exist between the entities. Process models like the business process model and notation (BPMN, OMG, 2011) describe real-world domains in terms of events that occur and the sequences of activities that are triggered and executed in response to those events. It seems intuitive that entity-relationship models differ from BPMN models: one addresses form and substance, and the other, behavior and change (Burton-Jones & Weber, 2014). It also seems logical that both substance and change are important to understand when one examines what an information system represents and what it is meant to do. This logic is also evident when one considers prominent conceptual modeling methods. For instance,

UML features fourteen grammars to describe structure, behavior, and interactions of a system from a variety of perspectives (Fowler, 2004). Other longstanding methodologies, such as Multiview (Avison & Wood-Harper, 1986), have promoted multiple models for thirty years.

Not surprisingly in this situation, evidence from both surveys and case studies indicates that practitioners indeed frequently work with multiple models, often constructed with different grammars (Dobing & Parsons, 2008; Petre, 2013; Jabbari Sabegh & Recker, 2017). Moreover, evidence suggests that they do so not to substitute models but to combine them. For example, 90% of UML practitioners reportedly work with at least two different models in at least a third of their projects, and nearly three quarters use at least two of the models in two thirds of their projects (Dobing & Parsons, 2008, p. 6). Similarly, Grossman, Aronson, and McCarthy (2005, p. 393) report that over 60% of their surveyed UML users worked with use case, class, sequence, chart, and activity diagrams, at a minimum. Petre (2013) reports that many professional software engineers use different UML models and even integrate other models into their work, such as those developed using DFD, ERD, BPMN and other grammars (p. 728). In a similar manner, case studies of model-driven engineering practices illustrate how practitioners use multiple types of models as a means of reference and communication during systems development (e.g., Cherubini, Venolia, DeLine, & Ko, 2007, p. 561). Other cases detail the issues users encounter when working with multiple models (Baker, Loh, & Weil, 2005, pp. 483-487).

Of course, one might believe that the use of multiple models during systems analysis and design is no longer current or relevant, but this assertion seems incorrect. While modern approaches to systems development, such as agile, have certainly gained popularity (Conboy, 2009), this situation does not mean that model-based systems development practices have disappeared. For example, model-driven engineering is practiced widely in many industries and across organizations both large and small (e.g., Mohagheghi, Gilani, Stefanescu, & Fernandez, 2013; Hutchinson, Whittle, & Rouncefield, 2014, Whittle, Hutchinson, & Rouncefield, 2014). In these projects, vast amounts of modeling techniques and models are reportedly in use (e.g., Grossman et al., 2005, Petre, 2013). A recent study showed that all interviewed IS practitioners used more than one type of conceptual model in their systems analysis and design tasks (Jabbari Sabegh & Recker, 2017). Clearly, in practice, models developed with various grammars appear to be used in combination. Yet, in the literature, studies with an explicit focus on multiple models are sparse. Table 1 summarizes literature that explicitly focuses on combinations of conceptual models.

Table 1. Literature on the Use of Combinations of Conceptual Models

<table><tr><td>Reference</td><td>Object of study</td><td>Summary of research</td><td>Implications for this paper</td></tr><tr><td>Kim, Hahn, &amp; Hahn (2000)</td><td>Usability of multiple models as part of a systems development methodology</td><td>The research examined representation aids that assist users in using multiple models to solve problems during systems development. It shows that visual cues and contextual information in multiple models assist users in searching for related information and developing hypotheses about the target system.</td><td>This study proposed an alternative theory with potential for conjunction: The study examined external aids that are not inherent to the models themselves and that may interact with the explanatory mechanisms we develop.</td></tr><tr><td>Siau &amp; Lee (2004)</td><td>Interpretation of class diagrams and use case diagrams in UML</td><td>The research showed that use case diagrams and class diagrams depict different aspects of a problem domain. To users, the models appear to have very little overlap in the information captured, and both are perceived as necessary in requirements analysis.</td><td>This study suggested two relevant properties of model combinations: that they do not overlap and that they are complementary. However, the study did not identify from where complementarity or overlap in the models would stem.</td></tr><tr><td>Dobing &amp; Parsons (2008)</td><td>Use of UML diagram types</td><td>Modeling practitioners use multiple types of UML diagrams in most projects. More than 50% of users report that they use five or more types of diagrams in at least a third of their software development projects.</td><td>This study established the ecological validity of our theory, that is, that practitioners use multiple models in combination.</td></tr><tr><td>Gemino &amp; Parker (2009)</td><td>Interpretation of textual use cases with use case models</td><td>The research showed that participants who receive supporting diagrams develop higher levels of domain understanding than they did with a textual use case description alone.</td><td>This study indicated that benefits may accrue from multiple models that are redundant: use case diagrams aided the text by displaying the same information in a different way.</td></tr><tr><td>Jabbari Sabegh &amp; Recker (2017)</td><td>The use of multiple conceptual models during systems analysis and design</td><td>The research interviewed systems analysis and design practitioners to establish how and why multiple models are used in practice.</td><td>This study showed that the use of multiple models during systems analysis and design remains current. It also suggested that selection and use of multiple models can be influenced by several factors. However, the study did not offer a theory to explain the findings.</td></tr></table>

We highlight two main points about the literature summarized in Table 1. On the one hand, the few empirical studies on multiple conceptual models mention findings such as:

“the information depicted by the two diagram types is sufficiently different and not overlapping” (Siau & Lee, 2004, p. 235);

“integration of information from the multiple perspectives was indeed necessary to thoroughly understand the business case” (Kim et al., 2000, p. 289); and

“while the use case diagram does not seem to add new information…, [it] helps users better understand sets of use cases”…“Use cases augmented with a use case diagram provide a more effective communication of system information than use cases alone” (Gemino & Parker, 2009, p. 15-16).

“all of our interviewees (15 out of 15) reportedly used more than one type of models in their design and analysis tasks.… Multiple interrelated models were used to represent different aspects of the system” (Jabbari Sabegh & Recker, 2017, p. 64- 66).

These passages make three important points. First, they suggest that multiple models are frequently used (Jabbari Sabegh & Recker, 2017) because they maximize the amount of information about a real-world domain. Second, this effect is not unequivocal, because models have to be “sufficiently different” (Siau & Lee, 2004, p. 235). Third, models that do not contain different, complementary information may still offer benefits (Gemino & Parker, 2009), likely because they establish “correspondence” between the representations (Jabbari Sabegh & Recker, 2017, p. 69).

On the other hand, none of the studies provided explanatory mechanisms rooted in the models themselves—i.e., none of the research focused on the artifacts. For example, Kim et al. (2000) demonstrated the benefits of external aids for understanding multiple models, such as visual cues to aid the transition between diagrams, or a context diagram to position the relative importance of individual items. There is no theory on which attributes that are inherent to conceptual models explain how best to combine them for use.

We draw three primary conclusions from this literature review:

1. There is evidence that suggests that practitioners prefer working with multiple models (Grossman et al., 2005; Dobing & Parsons, 2008; Mohagheghi et al., 2013; Whittle et al., 2014) and obtain benefits from them (Siau & Lee, 2004; Gemino & Parker, 2009). However, we do not yet fully understand how and why that is the case.

2. We do not yet fully understand which properties of the models themselves make them more or less appropriate for combination.

3. While extant studies have indicated that “representation” aspects or attributes of models may matter, which of these properties dominate is not yet entirely clear.

In the theory development that follows, we develop solutions to these problems. To provide a plausible basis for our assumptions, we build on representation theory (Wand & Weber, 1990, 1993, 1995), which has become a central theory used by researchers to make predictions about conceptual modeling (Moody, 2009, Siau & Rossi, 2011). Because we draw on it extensively, we provide a brief description in Appendix A. A more detailed account of representation theory, including its origins and development over time, is provided in Burton-Jones, Recker, Indulska, Green, & Weber (2017) and Recker, Indulska, Green, Burton-Jones, & Weber (2019).

## 3 Theory Development

In describing the development of our new theory about the interpretation of multiple conceptual models, we follow three main steps (Whetten, 1989, Weber, 2012). First, we introduce constructs that conceptualize our independent variable—namely, conceptual model combinations. Then, we present the interpretation of multiple models, which are constructs that conceptualize our main dependent variable. Finally, we develop propositions that describe the associations between these constructs. Table A1 summarizes relevant construct definitions.

## 3.1 Completeness and Overlap of Conceptual Model Combinations

We start by illustrating combined ontological completeness and ontological overlap in conceptual models (Figure 1). In Figure 1, the large circle describes a set of real-world phenomena to be represented. The representations required to develop a faithful (i.e., clear, complete, and accurate—see Weber, 1997, p. 83) description of these phenomena is indicated by the black dots, which symbolize different ontological constructs (e.g., Which things are of relevance? What are their properties? Which events occur that change the states of these things?). The two shaded circles describe the level of representation of these phenomena achieved in two conceptual models: A and B. Each model provides some partial representation of the phenomena—that is, each model has some level of ontological completeness.

To describe the combination of models (A and B), we define two constructs:

1. Combined ontological completeness: the level of representational coverage a set of multiple models provides about some real-world phenomenon. The level of combined ontological completeness is defined as the sum of ontological construct representations available in each of the models (Figure 1).

2. Ontological overlap: the set of redundant representations across a set of models—i.e., the extent to which a (partial) representation of some real-world phenomenon in one model is already available in another model. The level of ontological overlap is defined as the sum of ontological construct representations shared between the models (Figure 1).

Figure 1 also illustrates the notion of remaining construct deficit, which clarifies the level of combined ontological completeness that is achievable. Models are created using grammars that provide constructs that describe the semantics of real-world phenomena. However, because, as detailed in Appendix A, no available conceptual modeling grammar is complete, no single grammar offers constructs to develop a full representation of a realworld phenomenon. Therefore, all grammars have a representational limit defined by their extent of construct deficit, which is the maximal ontological completeness (MOC) offered by a grammar. Therefore, any one model is, at best, maximally ontologically complete (but not fully complete). In fact, models are often less than maximally complete, most only contain a small subset (zur Muehlen & Recker, 2008). In other words, the actual level of completeness of a conceptual model is often less than its potential level of completeness.

Theoretically, two or more models in combination could achieve a full representation of all required real-world phenomena, but the level of combined ontological completeness depends on selecting models for combination that maximize the completeness of the representation. The combined ontological completeness of the models is also constrained by the maximal ontological completeness of the grammars used to create the models: for example, no number of BPMN models, however large, will ever offer a full representation of a real-world domain because the BPMN grammar is ontologically incomplete (Recker et al., 2010).

![](/api/attachments/9ESHKXZG/fulltext/images/55b0a27ee83a6ca75cc17105387653756b1610057a8c7750414b300e2bce5dd0.jpg)  
Figure 1. Illustration of Combined Ontological Completeness and Overlap of Two Conceptual Models. In Analogy to Weber (1997, p. 102)

## 3.2 Interpretation of Conceptual Model Combinations

Interpretation of one or more conceptual models, as the core phenomenon of our theory explains, is primarily a task of model readers (sometimes also called model interpreters—see Gemino & Wand, 2004)—that is, those users who during analysis and design engage in solving problems and making decisions with the use of previously built conceptual models, as opposed to those who develop conceptual models (i.e., model creators or simply modelers, see Gemino & Wand, 2004). <sup>1</sup> Addressing model readers is important because system failures often stem from communication failures between analysts and users in the early stages of system analysis and design (Lauesen & Vinter, 2001).

The answer to the question of how individuals interpret or “read” conceptual models is not straightforward. Research has established the purposes of interpreting conceptual models, such as supporting communication between developers and users, helping analysts understand a domain, providing input for systems design processes, and documenting requirements for future reference (Kung & Sølvberg, 1986; Wand & Weber, 2002). It has also examined the intended or reported benefits derived from interpreting conceptual models, such as input to organizational redesign and improved documentation of operational processes (e.g., Indulska, Green, Recker, & Rosemann, 2009). Some studies have identified the extent of conceptual model interpretation by practitioners in tasks such as database design and management, software development, business process improvement, or enterprise architecture design (Davies, Green, Rosemann, Indulska, & Gallo, 2006; Fettke, 2009).

These findings demonstrate that the purposes and application areas of conceptual models are varied. However, independent of purpose and application, all uses of conceptual models involves interpreting their content (Burton-Jones & Meso, 2008), although it remains unclear what interpreting conceptual models as an act involves. Burton-Jones et al. (2009, p. 498) suggest that model interpretation can be examined from two perspectives: interpretational fidelity (how faithfully—i.e., completely, clearly, and accurately— the interpretation of one or more conceptual models represents the denotational semantics in the models intended by their creators) and interpretational efficiency (what resources are used to interpret one or more conceptual models). While this distinction has been widely applied in the literature to distinguish different outcome variables—for example, scores on problem solving questions as a measure of interpretational fidelity, or time taken to complete a problem solving task as a measure of interpretational efficiency (e.g., Bodart et al., 2001, Gemino & Wand, 2005, Shanks et al., 2008, Recker & Dreiling, 2011, Bera et al., 2014)—it does not elaborate on the act of interpretation per se.

We approach such an elaboration by suggesting that conceptual model interpretation is a goal-directed activity that involves the user (the subject), the model(s) (the object), and the task (the organizational action that requires the interpretation of one or more conceptual models). We assume that (1) the user is an individual person who interprets a conceptual model for a task,<sup>2</sup> (2) conceptual models are tangible artifacts that provide a representation of a real-world domain that is relevant to the user given a particular task (Wand & Weber, 1990), and (3) the task is a goaloriented activity, so task outcomes can be compared to predefined task requirements (Zigurs & Buckland, 1998).

This definition stresses that interpreting models occurs as part of a particular task, rather than for its own sake—i.e., “just to read them.” A task goal might be to identify system requirements from a domain model in order to express relevant functional requirements completely and clearly. Or, a task goal might involve specifying database queries accurately and efficiently, which may require the models to be not only expressive but also parsimonious (Bowen et al., 2006). Task goals may even differ to the extent that incomplete and/or inaccurate conceptual models may be required. Independent from the nature of the task goal, however, model interpretation is inevitably characterized by task goals. Therefore, requirements associated with the interpretation of one or more conceptual models in support of the task can be defined a priori.

Moreover, according to this definition, interpretation of one or more conceptual models is a means to an end, rather than an end in itself. The tasks and task goals against which interpretational fidelity or efficiency must be evaluated may vary, but independent of the specific tasks, the act of interpreting one or more conceptual models always entails at least three components: selection, action, and evaluation. The basis for these components stems from research on cognitive representation and control of action processes (e.g., Beach & Mitchell, 1978; Locke & Latham, 1990): people engage in behavior, driven by a mental representation that links higher-level goals (such as those imposed by a task) to specific actions (such as the selection of models for reading) that are instrumental in achieving these goals. In doing so, people evaluate the performance expectancy of any object they may use in these actions, perform the actions, and then compare the achieved performance against their expectations. When faced with multiple options (e.g., multiple models), people perform profitability tests to compare acceptable options (Beach & Mitchell, 1978). <sup>3</sup> Following this line of reasoning, we next define the selection, action, and evaluation components of conceptual model interpretation.

Selection: deciding which conceptual models to read. Prior to engaging in a task involving the interpretation of a set of available conceptual models, the user will have expectations about what performance gains will be derived from reading the conceptual models. These expectations are similar to those ascribed to other IS artifacts (e.g., built information systems) involving, for example, an artifact’s ability to improve the speed, quality, and efficiency of task performance (Venkatesh & Davis, 2000; Brown, Venkatesh, & Goyal, 2012). If a user has a variety of conceptual models that can potentially assist with model-based tasks, user performance expectations will determine how to test the models (Beach & Mitchell, 1978) to choose the most profitable candidate or combination. This test will manifest in a selection decision about which model or model combination to read for an upcoming task. For instance, if an analysis task involves the redesign of an organizational procedure to minimize the use of resources, the user may select models that convey information about workflow processes and role allocations, such as activity charts and swimlane diagrams. On the other hand, if a task involves presenting an overview to senior managers who need to grasp a domain quickly, the user may select models that convey only essential information on a high level of abstraction, such as use case diagrams or class diagrams.

Action: generating domain understanding from the conceptual models. Having selected a conceptual model combination, the user engages in the modelbased task and evaluates it in terms of whether and how many performance gains stem from interpreting the conceptual models. Conceptual models can support many tasks (e.g., systems analysis, communication, design, project management, end-user querying, process redesign, organizational change management) (Kung & Sølvberg, 1986; Wand & Weber, 2002; Figl & Recker, 2016); thus, defining the performance gains will vary depending on the task. For example, during database design, a conceptual model might be read with the goal of identifying the constraints required for SQL expressions (Bowen et al., 2006).

In any case, however, conceptual models must be interpreted in order to realize performance gains from them (Aguirre-Urreta & Marakas, 2008, p. 12; Burton-Jones et al., 2009, p. 499). Therefore, for all tasks, the interpretation of conceptual models necessarily and unequivocally involves reading the model to construct knowledge about the depicted domain. Hence, one key evaluation of performance gains must be how much domain understanding can be generated from interpreting a conceptual model combination during a task (Gemino & Wand, 2004, Shanks et al., 2008, Burton-Jones et al., 2009, Recker & Dreiling, 2011). Domain understanding is generated when model readers organize and integrate the information presented in the conceptual models with their own experience and mental models (Mayer, 1989), thereby constructing new knowledge about the elements in a real-world domain (surface understanding) and the actual and possible relationships between these elements (deep understanding) (Mayer, 2009). The user then applies this domain understanding in completing the task they set out to do.

Evaluation: appraising the usefulness of the conceptual models. A key finding of the research on cognitive representation and control of action processes is that people continuously update the mental representations that govern their actions as part of a progressing decision (e.g., Beach & Mitchell, 1978; Beach, 1993). They reflect on the options selected and the action outcomes achieved to evaluate the compatibility between the two. For example, people update their expectations about behaviors (e.g., how they approach a task) based on their own past behaviors that either confirmed or disconfirmed their previous expectations (Oliver, 1977). The adjusted perceptions then provide the basis for subsequent behaviors (Bem, 1972). In this vein, model readers who employ a conceptual model combination perform a cognitive appraisal, evaluating the performance gains from interpreting the conceptual models for a particular task by reflecting on their expectations that led to the initial profitability test and determining whether their pre-task expectations were confirmed (Oliver, 1977; Recker, 2010).

Performance gains from interpreting conceptual models depend on the nature of the task. For instance, one might evaluate whether reading conceptual models during a systems analysis task increased the user’s task efficiency (e.g., by comparing task completion times). However, independent of any task-specific performance metric, performance gains should also manifest as beliefs about the performance resulting from the object in use (Venkatesh, Morris, Davis, & Davis, 2003), so that they can be measured as the perceived usefulness of the chosen conceptual models in supporting the task at hand. In this context, perceived usefulness can be defined as the degree to which a model reader believes that a particular conceptual model combination was effective in achieving the intended task objectives (Davis, 1989; Maes & Poels, 2007).

## 3.3 Proposition Development

Having described the constructs in our theory, we now develop propositions that describe the associations between the constructs. Figure 2 shows the key associations—the main propositions—we explore in this section. The three variables visualized in the dashed part of Figure 2—i.e., environmental uncertainty, task nature, and prior domain knowledge—describe possible boundary conditions situated in the conceptual modeling context. We discuss these in Appendix C.

## 3.3.1 Predicting the Selection of Conceptual Model Combinations.

The selection proposition concerns which models from a set of available models with different levels of ontological completeness users will select to complete an upcoming task. Figure 3 illustrates this proposition. It suggests that individuals will start selecting multiple conceptual models if available, but only up to a certain point.

The literature on cognitive fit (Vessey & Galletta, 1991; Agarwal, Sinha, & Tanniru, 1996; Khatri, Vessey, Ramesh, Clay, & Sung-Jin, 2006) suggests that individuals select models to aid their tasks based on a mental model of the problem space confronting them. For example, for symbolic tasks they would choose a tabular representation of the domain (Vessey & Galletta, 1991). As stated above, the interpretation of models is likewise characterized by task goals. Specifically, conceptual models aid in the task of requirements analysis for some problem context. However, cognitive fit theory implies that unless the combination of models semantically represents all the elements of the problem task, both the user’s mental representation and performance will be degraded.

![](/api/attachments/9ESHKXZG/fulltext/images/db80766c3828fbc3802c8ad6fffa2105137305eb25854711f2600269d5d9a4bb.jpg)  
Figure 2. Summary of Theory Propositions

Therefore, notwithstanding an initial model selection, and based on the assumption that multiple models about a real-world domain are available to model readers, we predict that, prima facie, individuals will select additional models to complement their initial choice because they desire a maximal level of ontological completeness of the combined representation of some focal real-world problem presented in the scope of some task. They do so because any one model will contain construct deficit. In other words, if available, users will likely select additional models in order to compensate for the impoverished representation inherent to any one model (Weber, 1997, pp. 95-96). One typical manifestation of an impoverished representation is a conceptual model that focuses on a particular design dimension (say, data structures) but omits a different dimension (say, system behavior). Intuitively, these different models each provide a partial level of representation. Combining them provides a more complete representation, which appears at face value desirable to a user because by increasing the level of combined ontological completeness of a domain’s representation, more information will be available for integration into a mental model of the real-world phenomenon being represented. Therefore, we propose initially:

P1a. Given one conceptual model, users will select additional models for use in their tasks such that the combined ontological completeness of the model combination will be maximized.

Yet, as visualized in Figure 3, the selection logic will not be linear. At some point, users will stop selecting additional models when the models appear to convey the same information, even if the additions would provide an increased level of completeness. We next describe our reasoning.

Selecting additional models increases the chance that the ontological overlap between models will increase. This situation decreases the clarity of the combined representation because several constructs are in the set of models that describe the same real-world phenomenon. This situation may lead to confusion when users inspect the available models: users might wonder why certain constructs appear multiple times and/or might assume that a redundant construct stands for some other type of phenomenon (Weber, 1997, p. 99). In either case, the models will appear “complex.” Therefore, to mitigate the anticipated additional effort that is associated with generating understanding from conceptual models, we argue that model users will follow a law of diminishing returns, choosing additional models that maximize the combined ontological completeness only until they reach a level of bearable overlap they can tolerate. Should this level of overlap be exceeded, we predict that users will deselect models, even lowering the combined ontological completeness that can be achieved. Otherwise, the domain representation achieved will be undermined by lack of clarity and it will require too much cognitive load when users interpret the models, as the bearable level of combined ontological overlap is constrained by users’ cognitive processing capacity (Miller, 1956).

Because of their limited overall cognitive capacity, users do not refer to the entire set of models at once as a single chunk of information (Ward & Sweller, 1990). Instead, they screen each model for local information and thus they can anticipate the cognitive demands of information processing very quickly. Therefore, users will not select additional models even if adding another model would increase combined ontological completeness. We propose:

P1b. Users will select additional models for use in their tasks only until their bearable level of ontological overlap of the combined representation is reached.

![](/api/attachments/9ESHKXZG/fulltext/images/e9c59fb8f0e3c78622d3353e0074d55d8dc15c35b4d8676b6a7992ad23affff1.jpg)  
Figure 3. Selection of Model Combinations as a Function of Combined Ontological Completeness and Overlap

## 3.3.2 Predicting the Development of Domain Understanding from Conceptual Model Combinations

The domain understanding proposition concerns which model combinations maximize the ability of model readers to gain understanding about the real-world domain represented by their interpretations. Figure 4 illustrates this proposition.

When reading models, users create a mental model representation of the domain based on the information the models provide (Gemino & Wand, 2005). They identify and internalize constructs in the model by integrating them with concepts in their mental representations of the domain (Mayer, 1989, Pretz, Naples, & Sternberg, 2003), thereby updating their existing knowledge and constructing new knowledge. A complete mental representation of the domain is a key driver of a user’s ability to reason about the domain during problem solving (Newell & Simon, 1972).

When interpreting conceptual models, the construct deficit that is inherent in any single model is a noted issue: users lack relevant information about a realworld domain, which diminishes the level of understanding a user can generate about a phenomenon (e.g., Bajaj, 2004; Parsons, 2011). However, if a combination of models has more ontological completeness than any one model alone, the combination of models offers more representational elements that convey meaning about the phenomenon in a real-world domain. In such a case, more information is available for assimilation into the user’s mental representation about the focal phenomenon, thus improving the level of domain understanding that can be gained from the models. Thus, we maintain:

P2a. Model users who read a combination of models that have a high level of combined ontological completeness will generate higher levels of domain understanding than will users who read a combination of models that have a low level of combined ontological completeness.

The level of domain understanding that can be derived from a selected set of models is moderated by the level of ontological overlap between the models. Model combinations with higher levels of ontological overlap

introduce additional extraneous cognitive load (Sweller, 1988; Gemino & Wand, 2005) in two ways: First, model users must identify the overlapping constructs. Identifying redundant constructs complicates readers’ cognitive search process (i.e., the process of locating visual constructs in a model and identifying relevant attributes and relationships) (Larkin & Simon, 1987). Second, model users must reconcile their meaning. This situation adds complexity because users have to compare the semantics of constructs. The heightened cognitive demand to understand redundant constructs across different models diminishes the capacity to absorb information and, hence, the ability to generate domain understanding. Therefore, we argue:

P2b. The positive impact of combined ontological completeness of model combinations on users’ ability to gain domain understanding decreases as the ontological overlap in the combination of models increases.

![](/api/attachments/9ESHKXZG/fulltext/images/32b5e8917ebd6a6d84801c90a579e2a6d5d95484c3341bb25a550838140d6629.jpg)  
Figure 4. Level of Domain Understanding from Model Combinations as a Function of Combined Ontological Completeness and Overlap

## 3.3.3 Predicting the Perceived Usefulness of Conceptual Model Combinations

Our third proposition concerns how model users evaluate performance gains derived from interpreting multiple models. Figure 5 illustrates this proposition.

We predict that users’ perceptions of the usefulness of model combinations will be more positive when the combined ontological completeness of a representation is high. Perceived usefulness can be understood as the extent to which a person believes that a particular model is effective in achieving the intended task objectives (Davis, 1989; Recker, Rosemann, Green, & Indulska, 2011). The evaluation of how useful conceptual models are for a task depends on how well the model makes necessary and sufficient manifestations of relevant real-world phenomena available to the user. If there are deficits in the desired representations, the available representations will be less effective for solving problems (Gemino & Wand, 2004). Therefore, users are unlikely to find multiple models with impoverished quality useful (Lindland, Sindre, & Sølvberg, 1994; Maes & Poels, 2007). As such, we posit:

P3a. Users perceive a combination of models with a high level of combined ontological completeness as more useful in model-interpretation tasks than a combination of models with a lower level of combined ontological completeness.

However, model combinations with increased ontological completeness and increased ontological overlap will be evaluated as less useful because the additional complexity of the representation will offset the gains in representational effectiveness by requiring more cognitive effort to reconcile the conveyed meaning (Wand & Weber, 1993). Ontologically overlapping models add confusion, which adds complexity to user tasks. As the extent of overlap

increases, the perceived usefulness of the combination decreases. A clear (i.e., nonoverlapping) interpretation of conceptual models will allow a user to glean meaning from the models more easily and, thus, retain cognitive capacity to complete the task at hand. Conversely, if additional effort must be invested in interpreting the models because of a high degree of overlap, less capacity is available for the problemsolving task. Such perceptions of effort will undermine the perception of usefulness (Recker, 2010). We expect that the detrimental impact of ontological overlap on perceived usefulness is stronger than the positive impact of ontological completeness. Users deem parsimonious models more useful for their tasks than complete and complex representations because of the computational advantage that parsimonious models provide in information processing (Larkin & Simon, 1987). Therefore, we propose:

P3b. User perceptions of the usefulness of conceptual model combinations decrease as the level of ontological overlap of the combinations increase, such that the negative effect of ontological overlap is stronger than the positive effect of combined ontological completeness.

![](/api/attachments/9ESHKXZG/fulltext/images/43cc1a989c1d70cef3f77983e3522adae360ee208b3832fd9fbd72d04ac5b681.jpg)  
Figure 4. Perceived Usefulness of Model Combinations as a Function of Combined Ontological Completeness and Overlap

## 4 Discussion

## 4.1 Summary of the Scope and Contributions of Our Theory

We developed new theory about how individuals interpret multiple conceptual models, positing that two attributes of model combinations, combined ontological completeness and ontological overlap, are key determinants for users’ selection, understanding, and perceived usefulness of models. Having done so, we now delineate the boundary conditions of our theorizing. We start by identifying the scope of our theory as limited by its assumptions. We developed a specific theory (how users interpret multiple models) based on Wand and Weber’s (1995) more general theory of information systems as representations.

Therefore, like their work, our theorizing describes a model of the artifacts that define an information system’s deep structure. As such, it focuses on the semantics of conceptual models and grammars (Bera et al., 2014; Clarke, Burton-Jones, & Weber, 2016). The choice of visual syntax (e.g., a rectangle or a circle—see Moody, 2009) is not part of our theory. Also, our theory does not describe in detail the psychological, linguistic, or cognitive processes employed by users to engage with conceptual models for the purpose of understanding real-world domains (Truex & Baskerville, 1998: Evermann, 2005). In addition, our theory does not address pragmatic factors (e.g., tasks, knowledge, external conditions) that would describe their use. However, as we discuss in Appendix C, such factors can be brought into the theory’s focus.

A second boundary to the scope of our theory stems from its position in the stream of conceptual modeling literature. Our theory concerns the selection and interpretation of combinations of previously built conceptual models by practitioners for the purpose of analyzing and understanding systems requirements. It is not a theory of conceptual model creation, even though we believe design principles could possibly be derived from our explanations. It is also not a theory about the use of methods and grammars for the design of conceptual models (Purao et al., 2002).

Third, our theory of model interpretation bears some resemblance to theories of information behavior in general because it conceptualizes some specific aspect of “how people need, seek, manage, give and use information in different contexts” (Fisher, Erdelez, & McKechnie, 2005, p. xix). However, with its focus on the role of models as representations of an information system’s deep structure (Wand & Weber, 1995; Burton-Jones et al., 2017) it is both much narrower than general models of information seeking (e.g., Leckie, 2005) or acquiring (e.g., Rioux, 2005), and more specific, in that it focuses on artifacts more so than on information-seeking behavior (e.g., Wilson, 1999, p. 251).

Finally, our theory is also bounded because its predictions have not yet been tested. Describing operationalization and measurement strategies for our theory in full would require an entire paper. However, to motivate and guide potential future empirical research that would evaluate, refute, extend, or otherwise improve our theory, we offer two suggestions for how empirical research could be carried out. First, in Appendix B we provide an illustration of how our theory could be applied to the analysis of multiple available models presented to an individual. Second, in Appendix C, we discuss what we believe might be important moderator variables (Figure 2) that should be included in an empirical research design used to test our theory.

In evaluating the contributions our new theory offers, we consider the knowledge provided by the extant representation theory on which it is founded and the empirical research program it has supported to date. Our theory development may be construed as “dropping the theoretical tools, holding the concepts lightly and updating them frequently” (Holmström & Truex, 2011): consider the two principles of maximal ontological completeness (MOC) and minimal ontological overlap (MOO). We adapted these principles from Green, Rosemann, Indulska, & Manning (2007) and Weber (1997) and transferred their application from grammars to models and from model design to model interpretation. This adaptation is “interesting” (Davis, 1971) because it highlights two tensions related to the original concepts described next.

## 4.1.1 The Tension Between Ontological Completeness and Overlap

We started our theorizing by appropriating two established concepts: MOC and MOO (e.g., Green et al., 2007, 2011). In what followed, our theorizing highlighted a potential conflict between these two notions that has not been surfaced earlier. Our theory suggests that sometimes combined ontological completeness and ontological overlap may conflict. For instance, imagine a set of models that together maximizes the representation of real-world phenomena and also shares a large set of common representational constructs—i.e., a combination with high levels of combined ontological completeness and overlap. Then, imagine a second model combination with a lower level of combined ontological completeness but also a lower level of ontological overlap. Which of these two combinations should be selected, interpreted, and deemed more useful? This question is far from trivial. Green et al. (2011) argue that the primary principle for grammar selection as part of model design should be MOC, but whether that is true for the selection and interpretation of models remains in question. Could model interpretation be governed by principles of clarity (i.e., minimizing construct overload and/or redundancy) over completeness? There is some evidence that suggests that the simplicity of a representation may be more useful than its completeness. For instance, Siau and Lee (2004) show that users prefer diagrams that are easier to use and that such diagrams enable them to obtain a more complete representation. Samuel et al. (2015) also demonstrate that practitioners often rationalize the volume of information in models to achieve a simpler, rather than fuller, understanding of the relevant domain.

## 4.1.2 The Tension Between Model Design and Interpretation

Weber (1997) and Green et al. (2007, 2011) argue that MOC and MOO are criteria that guide designers in their choice of grammars for model creation. We developed a theory about the choice of models for model interpretation, but the relationship between design choices made in creating models and the interpretation choices available to users is important. For readers of conceptual models, it is not the grammar and its potential maximal coverage of real-world phenomena that matters, but the actual maximal coverage of real-world phenomena that is available in any combination of models produced by a grammar or grammars. A model’s actual maximal coverage is limited by the number and type of constructs in a grammar, so model designers have potentially unlimited choices available to create complete and clear representations of real-world phenomena: designers may choose from available or recommended grammars, may opt to use alternatives like free text or additional documents adjacent to the models (Green et al., 2011), or may even alter construct semantics or invent new semantics (Recker et al., 2010). These design choices are not available to the readers of these models, who seek a complete and clear interpretation of a focal real-world phenomenon. One key difference is that model designers should be able to create ontologically complete representations, whereas, provided that multiple models are available, model readers can, at best, select a maximally (not necessarily fully) ontologically complete representation.

The questions about the opposition of MOC and MOO and the correlation of design and interpretation ultimately require empirical work to resolve. Our theory offers an explanatory logic to guide such work and identifies some of the conditions under which the relationship between MOC and MOO can be examined. Further, Appendix C introduces three moderator variables that may be useful to identify contexts in which the relationship between MOC and MOO differ.

Our new theory also contributes in several ways to the broader literature on conceptual modeling. This theory is the first to analyze and explain the interpretation of conceptual models in combinations. Also, our theory focuses on the artifacts (i.e., the models) themselves. Finally, unlike empirical accounts broadly describing the use of conceptual models (Dobing & Parsons, 2008; Petre, 2013; Jabbari Sabegh & Recker, 2017), our theory offers principles concerning how and why users might select different sets of conceptual models to complete their tasks, how much domain understanding these different sets might generate, and how useful users perceive sets of models to be.

## 4.2 Implications for Research

Because the focus of this paper is theory development, the implications of our research relate primarily to future research seeking to enact or evaluate our theory through empirical research. We see several ways in which our theory could be advanced.

First, our three research models suggest the presence of limits and thresholds. For example, Proposition 1 argues that users will select additional models until they reach a bearable level of ontological overlap that is constrained by users’ cognitive processing capabilities. Cognitive processing is, however, both volatile and contextual (Gobet & Clarkson, 2004). Therefore, our theory has no basis for speculating ex ante what the thresholds will be for different users; as such, we cannot offer a hypothesis on this element of the proposition. Instead, the existence and extent of the thresholds are empirical questions.

Second, the range of predictions could be extended beyond the three core evaluations on which we focus.

A promising direction would be to develop predictions about the design of model combinations, rather than their interpretation.

A third direction flows from a broader examination of the tasks and the associated goals related to the models interpreted during these tasks. We focused on the development of domain understanding because any subsequent interpretation of a model for other analysis and design tasks (say, software specification versus system configuration versus process redesign) ultimately depends on how well individuals can understand the modeled domain (Burton-Jones & Meso, 2008). Still, similar to existing research on using conceptual models for specific tasks, such as the development of database queries (Bowen et al., 2006), it would be useful to see how model combinations could assist with different kinds of specific problemsolving tasks.

Fourth, we see a promising research direction in the development of appropriate measurements for our theory. For example, because users evaluate grammars differently based on perceptions of the grammars ontological completeness and clarity (Recker et al., 2011), it will be important to clarify how the perceived level of completeness and clarity of a set of models affect user evaluations and the behaviors of the users who read them. We focused on perceived usefulness as a performance-evaluation metric because it is a wellestablished measure in the literature. Other suitable metrics include the perceived semantic quality of model combinations (Maes & Poels, 2007) and satisfaction with models (Nolte, Bernhard, Recker, Pittke, & Mendling, 2016), to name just two.

Fifth, our theory focuses on attributes of models as artifacts. These could be combined with other elements (e.g., factors that describe the context of conceptual model interpretation) to account for variations in the theory’s predictions. We provide a brief discussion of three context factors in Appendix C. A more comprehensive analysis of the context would benefit from programmatic efforts and it could build on Wand and Weber’s (2002) taxonomy of context factors.

## 4.3 Implications for Practice

Two principal implications for practice emerge from our theory. First, we developed theoretical models that can explain and guide choices available to the end users of conceptual models when they seek to interpret these models during systems analysis and design tasks. Our theory suggests that two guiding principles— combined ontological completeness and ontological overlap—inform the selection, understanding, and usefulness of multiple models. In essence, our theory suggests that model readers should be mindful of whether they require a parsimonious or a complete representation of the real world to effectively complete their tasks.

A second implication arises about the design of multiple conceptual models. We assume that the purpose of creating conceptual models is to create faithful (i.e., complete, clear, and accurate) representations of a real-world domain. However, as we discuss in Appendix C, under some conditions, such as environmental uncertainty, when working with explorative tasks that involve conceptual model use, or when designing models for users with very high or very low domain knowledge, tradeoffs between completeness and clarity may have to be taken into account during model design in order to make the models suitable for interpretation. For example, designers may wish to create partially redundant representations to maximize combined ontological completeness at the expense of ontological overlap or, conversely, create representationally deficient conceptual models in order to maximize clarity and simplicity. Indeed, in new and emerging domains such as virtual reality or the Internet of things, there may be a need for designers to combine models at different levels of ontological completeness in order to account for the different components required in these domains—for example, infrastructural, logical or interactional components. However, given our focus on model interpretation rather than creation, we have not studied these implications and, thus, they require further analysis.

## 4.4 Limitations

We acknowledge two important limitations. First, we reported on theory development void of any systematic empirical data collection or evaluation. Our suggested logic and explanations thus remain speculative until empirical work is performed. To invite and guide such work, we provide an illustration of procedures for enacting our theory in Appendix B. In Appendix C, we discuss several important boundary conditions that might be relevant to empirical study design. We hope through these means it will become clear how an empirical analysis of practitioner interpretation of multiple models could be carried out.

Second, we wish to acknowledge the subjectivity of interpretation mappings that are required in ontological analyses of grammar constructs in conceptual models (Rosemann, Recker, Green, & Indulska, 2009). As we illustrate in Appendix B, potential interpretation bias could be mitigated in two ways: similar to Recker, Rosemann, Indulska, & Green (2009), the starting point should be the literature on published analyses of the grammars used in the models. Then, researchers should follow our lead and engage in an iterative process based on principles of dialogical reasoning and suspicion (Klein & Myers, 1999)—interpretation mapping drafts should be formulated between multiple researchers who question each of the suggested mappings and then iterate between these two steps to tease out biases and distortions in order to construct a jointly agreed-upon result such as that shown in Table B1.

## 5 Conclusions

Systems analysis and design practitioners often work with multiple conceptual models, rather than just one. We propose a theory that can be used to examine which combinations of conceptual models are more likely to be suitable for interpretation by model readers. Our theory offers fellow scholars a way to generate more research on conceptual modeling as a theory in use and, in turn, increase the relevance of this important traditional stream of IS research. We hope that fellow scholars will join us in empirically testing and refining our theory.

## Acknowledgments

An earlier version of the theory development provided in this paper was presented at the Australasian Conference on Information Systems 2014 in Auckland, New Zealand. The preparation of this paper was supported in part by funding from two Australian Research Council Discovery Grants (DP130102454 and DP140101815). We thank the senior editor and the three reviewers for their helpful comments.

## References

Agarwal, R., Sinha, A. P., & Tanniru, M. (1996). Cognitive fit in requirements modeling: A study of object and process methodologies. Journal of Management Information Systems, 13(2), 137-162

Aguirre-Urreta, M. I., & Marakas, G. M. (2008). Comparing conceptual modeling techniques: A critical review of the EER vs. OO empirical literature, The DATA BASE for Advances in Information Systems, 39(2), 9-32

Alexander, P. A. (1992). Domain knowledge: Evolving themes and emerging concerns, Educational Psychologist 27(1), 33-51

Allen, G., & Parsons, J. (2010). Is query reuse potentially harmful? Anchoring and adjustment in adapting existing database queries, Information Systems Research, 21(1), 56-77

Alvesson, M., & Kärreman, D. (2007). Constructing mystery: Empirical matters in theory development, Academy of Management Review, 32(4), 1265-1281

Avison, D. E., & Wood-Harper, A. T. (1986). Multiview: An exploration in information systems development, Australian Computer Journal, 18(4), 174-179

Bajaj, A. (2004). The effect of the number of concepts on the readability of schemas: An empirical study with data models, Requirements Engineering, 9(4), 261-270

Baker, P., Loh S., & Weil, F. (2005). Model-driven engineering in a large industrial context: motorola case study. Proceedings of Model Driven Engineering Languages and Systems Conference (pp. 476-491).

Beach, L. R. (1993). Image theory: an alternative to normative decision theory, Advances in Consumer Research, 20(1), 235-238

Beach, L. R., & Mitchell, T. R. (1978). A contingency model for the selection of decision strategies, Academy of Management Review, 3(3), 439- 449

Bem, D. J. (1972). Self perception theory, Advances in Experimental Social Psychology (pp. 1-62). New York, NY: Academic

Bera, P., Burton-Jones, A., & Wand, Y. (2011). Guidelines for designing visual ontologies to support knowledge identification, MIS Quarterly, 35(4), 883-908

Bera, P., Burton-Jones, A., & Wand, Y. (2014). How semantics and pragmatics interact in understanding conceptual models. Information Systems Research, 25(2), 401- 419.

Bodart, F., Patel, A., Sim, M., & Weber, R. (2001). Should optional properties be used in conceptual modelling? A theory and three empirical tests. Information Systems Research, 12(4), 384-405.

Bowen, P. L., O’Farrell, R. A., & Rohde, F. (2006). Analysis of competing data structures: Does ontological clarity produce better end user query performance. Journal of the Association for Information Systems, 7(8), 514-544.

Brown, S. A., Venkatesh, V., & Goyal, S. (2012). Expectation confirmation in technology use. Information Systems Research, 23(2), 474- 487.

Bunge, M. A. (1977). Treatise on basic philosophy volume 3: Ontology I—The furniture of the world. Dordrecht, The Netherlands: Kluwer Academic Publishers.

Bunge, M. A. (1979). Treatise on basic philosophy volume 4: Ontology II—A world of systems. Dordrecht, The Netherlands: Kluwer Academic Publishers.

Burton-Jones, A., & Meso, P. (2008). The effects of decomposition quality and multiple forms of information on novices’ understanding of a domain from a conceptual model. Journal of the Association for Information Systems, 9(12), 784-802.

Burton-Jones, A., Recker, J., Indulska, M., Green, P., & Weber, R. (2017). Assessing representation theory with a framework for pursuing success and failure. MIS Quarterly, 41(4), 1307-1333.

Burton-Jones, A., Wand, Y., & Weber, R. (2009). Guidelines for empirical evaluations of conceptual modeling grammars. Journal of the Association for Information Systems, 10(6), 495-532.

Burton-Jones, A., & Weber, R. (2014). Building conceptual modeling on the foundation of ontology. In H. Topi & A. Tucker (Eds.), Computing handbook, third edition: Information systems and information technology (pp. 15-11-15-24). Boca Raton, FL: CRC.

Byron, K., & Thatcher, S. M. B. (2016). Editors comments: “What i know now that I wish I knew then”—teaching theory and theory

building. Academy of Management Review, 41(1), 1-8.

Chandler, P., & Sweller, J. (1991). Cognitive load theory and the format of instruction. Cognition and Instruction, 8(4), 293-332.

Chen, P. P.-S. (1976). The entity relationship model: Toward a unified view of data. ACM Transactions on Database Systems, 1(1), 9- 36.

Cherubini, M., Venolia, G., DeLine, R., & Ko, A. J. (2007). Let's go to the whiteboard: How and why software developers use drawings. Paper presented at the SIGCHI Conference on Human Factors in Computing Systems, San Jose, California, USA.

Clarke, R., Burton-Jones, A., & Weber, R. (2016). On the ontological quality and logical quality of conceptual-modeling grammars: The need for a dual perspective. Information Systems Research, 27(2), 365-382.

Conboy, K. (2009). Agility from first principles: Reconstructing the concept of agility in information systems development. Information Systems Research, 20(3), 329- 354.

Corley, K. G., & Gioia, D. A. (2011). Building theory about theory building: What constitutes a theoretical contribution? Academy of Management Review, 38(1), 12-32.

Davies, I., Green, P., Rosemann, M., Indulska, M., & Gallo, S. (2006). How do practitioners use conceptual modeling in practice? Data & Knowledge Engineering, 58(3), 358-380.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.

Davis, M. S. (1971). That's interesting: Towards a phenomenology of sociology and a sociology of phenomenology. Philosophy of the Social Sciences, 1(4), 309-344.

Dawson, L., & Swatman, P. (1999). The use of objectoriented models in requirements engineering: A field study. Paper presented at the 20th International Conference on Information Systems, Charlotte, North Carolina, USA.

Dess, G. G., & Beard, D. W. (1984). Dimensions of organizational task environments. Administrative Science Quarterly, 29(1), 52- 73.

Dobing, B., & Parsons, J. (2008). Dimensions of uml diagram use: A survey of practitioners.

Journal of Database Management, 19(1), 1- 18.

Edwards, J. R., & Berry, J. W. (2010). The presence of something or the absence of nothing: Increasing theoretical precision in management research. Organizational Research Methods, 13(4), 668-689.

Erickson, J., Lyytinen, K., & Siau, K. (2005). Agile modeling, agile software development, and extreme programming: The state of research. Journal of Database Management, 16(4), 88- 100.

Evermann, J. (2005). Towards a cognitive foundation for knowledge representation. Information Systems Journal, 15(2), 147-178.

Evermann, J., & Wand, Y. (2006). Ontological modeling rules for UML: An empirical assessment. Journal of Computer Information Systems, 46(5), 14-29.

Fettke, P. (2009). How conceptual modeling is used. Communications of the Association for Information Systems, 25(43), 571-592.

Fickinger, T., & Recker, J. (2013). Construct redundancy in process modelling grammars: Improving the explanatory power of ontological analysis. Paper presented at the 21st European Conference on Information Systems, Utrecht, The Netherlands.

Figl, K., Mendling, J., & Strembeck, M. (2013). The influence of notational deficiencies on process model comprehension. Journal of the Association for Information Systems, 14(6), 312-338.

Figl, K., & Recker, J. (2016). Process innovation as creative problem-solving: An experimental study of textual descriptions and diagrams. Information & Management, 53(6), 767-786.

Fisher, K. E., Erdelez, S., & McKechnie, L. (Eds.). (2005). Theories of information behavior. Medford, NJ: Information Today.

Fiske, S. T. (2004). Mind the gap: In praise of informal sources of formal theory. Personality and Social Psychology Review, 8(2), 132-137.

Fowler, M. (2004). Uml distilled: A brief guide to the standard object modelling language (3rd ed.). Boston, MA: Addison-Wesley Longman.

Fowler, M., & Highsmith, J. (2001). The agile manifesto. Software Development, 9(8), 28- 32.

Gemino, A., & Parker, D. C. (2009). Use case diagrams in support of use case modeling:

Deriving understanding from the picture. Journal of Database Management, 20(1), 1- 24.

Gemino, A., & Wand, Y. (2004). A framework for empirical evaluation of conceptual modeling techniques. Requirements Engineering, 9(4), 248-260.

Gemino, A., & Wand, Y. (2005). Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data & Knowledge Engineering, 55(3), 301-326.

Gobet, F., & Clarkson, G. (2004). Chunks in expert memory: Evidence for the magical number four … or is it two? Memory, 12(6), 732-747.

Gray, P. H., & Cooper, W. H. (2010). Pursuing failure. Organizational Research Methods, 13(4), 620-643.

Green, P. (1996). An ontological analysis of isad grammars in upper case tools (Unpublished PhD Thesis, The University of Queensland, Brisbane, Australia).

Green, P., & Rosemann, M. (2001). Ontological analysis of integrated process models: Testing hypotheses. Australasian Journal of Information Systems, 9(1), 30-38.

Green, P., Rosemann, M., Indulska, M., & Manning, C. (2007). Candidate interoperability standards: An ontological overlap analysis. Data & Knowledge Engineering, 62(2), 274- 291.

Green, P., Rosemann, M., Indulska, M., & Recker, J. (2011). Complementary use of modeling grammars. Scandinavian Journal of Information Systems, 23(1), 59-86.

Gregor, S. (2006). The nature of theory in information systems. MIS Quarterly, 30(3), 611-642.

Grossman, M., Aronson, J. E., & McCarthy, R. V. (2005). Does uml make the grade? Insights from the software development community. Information and Software Technology, 47(6), 383-397.

Holmström, J., & Truex, D. P. (2011). Dropping your tools: Exploring when and how theories can serve as blinders in is research. Communications of the Association for Information Systems, 28(19), 283-294.

Hutchinson, J., Whittle, J., & Rouncefield, M. (2014). Model-driven engineering practices in industry: Social, organizational and managerial factors that lead to success or failure. Science of Computer Programming, 89(Part B), 144-161.

Indulska, M., Green, P., Recker, J., & Rosemann, M. (2009). Business process modeling: Perceived benefits. In S. Castano, U. Dayal & A. H. F. Laender (Eds.), Conceptual modeling: ER 2009 (pp. 458-471). Gramado, Brazil: Springer.

Irwin, G., & Turk, D. (2005). An ontological analysis of use case modeling grammar. Journal of the Association for Information Systems, 6(1), 1- 36.

Jabbari Sabegh, M. A., & Recker, J. (2017). Combined use of conceptual models in practice: An exploratory study. Journal of Database Management, 28(2), 56-88.

Kendall, K. E., & Kendall, J. E. (2008). Systems analysis and design (7th ed.). Upper Saddle River, NJ: Prentice Hall.

Khatri, V., & Vessey, I. (2016). Understanding the role of is and application domain knowledge on conceptual schema problem solving: A verbal protocol study. Journal of the Association for Information Systems, 17(12), 759-803.

Khatri, V., Vessey, I., Ramesh, V., Clay, P., & Sung-Jin, P. (2006). Understanding conceptual schemas: Exploring the role of application and is domain knowledge. Information Systems Research, 17(1), 81-99.

Kim, J., Hahn, J., & Hahn, H. (2000). How do we understand a system with (so) many diagrams? Cognitive integration processes in diagrammatic reasoning. Information Systems Research, 11(3), 284-303.

King, W. R., & He, J. (2005). Understanding the role and methods of meta-analysis in is research. Communications of the Association for Information Systems, 16(32), 665-686.

Klein, H. K., & Myers, M. D. (1999). A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Quarterly, 23(1), 67-94.

Kung, C. H., & Sølvberg, A. (1986). Activity modeling and behavior modeling of information systems. In T. W. Olle, H. G. Sol & A. A. Verrijn-Stuart (Eds.), Information systems design methodologies: Improving the practice (pp. 145-171). Amsterdam: Elsevier.

Larkin, J. H., & Simon, H. A. (1987). Why a diagram is (sometimes) worth ten thousand words. Cognitive Science, 11(1), 65-100.

Lauesen, S., & Vinter, O. (2001). Preventing requirement defects: An experiment in process improvement. Requirements Engineering, 6(1), 37-50.

Leckie, G. J. (2005). General model of the information seeking of professionals. In K. E. Fisher, S. Erdelez & L. McKechnie (Eds.), Theories of information behavior (pp. 158-163). Medford, NJ: Information Today.

Lindland, O. I., Sindre, G., & Solvberg, A. (1994). Understanding quality in conceptual modeling. IEEE Software, 11(2), 42-49.

Locke, E. A., & Latham, G. P. (1990). A theory of goal setting and task performance. Englewood Cliffs, NJ: Prentice-Hall.

Lukyanenko, R., Parsons, J., & Wiersma, Y. F. (2014a). The impact of conceptual modeling on dataset completeness: A field experiment. Paper presented at the 35th International Conference on Information Systems, Auckland, New Zealand.

Lukyanenko, R., Parsons, J., & Wiersma, Y. F. (2014b). The iq of the crowd: Understanding and improving information quality in structured user-generated content. Information Systems Research, 25(4), 669- 689.

Lukyanenko, R., Parsons, J., & Wiersma, Y. F. (2016). Emerging problems of data quality in citizen science. Conservation Biology, 30(3), 447- 449.

Lukyanenko, R., Parsons, J., Wiersma, Y. F., Wachinger, G., Huber, B., & Meldt, R. (2017). Representing crowd knowledge: Guidelines for conceptual modeling of usergenerated content. Journal of the Association for Information Systems, 18(4), 297-339.

Maes, A., & Poels, G. (2007). Evaluating quality of conceptual modelling scripts based on user perceptions. Data & Knowledge Engineering, 63(3), 769-792.

March, J. G. (1991). Exploration and exploitation in organizational learning. Organization Science, 2(1), 71-87.

Masri, K., Parker, D. C., & Gemino, A. (2008). Using iconic graphics in entity-relationship diagrams: The impact on understanding. Journal of Database Management, 19(3), 22- 41.

Mayer, R. E. (1989). Models for understanding. Review of Educational Research, 59(1), 43- 64.

Mayer, R. E. (2009). Multimedia learning (2nd ed.). Cambridge, MA: Cambridge University Press.

Mendling, J., Strembeck, M., & Recker, J. (2012). Factors of process model comprehension — findings from a series of experiments. Decision Support Systems, 53(1), 195-206.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81-97.

Milliken, F. J. (1987). Three types of perceived uncertainty about the environment: State, effect, and response uncertainty. Academy of Management Review, 12(1), 133-143.

Mohagheghi, P., Gilani, W., Stefanescu, A., & Fernandez, M. A. (2013). An empirical study of the state of the practice and acceptance of model-driven engineering in four industrial cases. Empirical Software Engineering, 18(1), 89-116.

Moody, D. L. (2009). The “physics” of notations: Toward a scientific basis for constructing visual notations in software engineering. IEEE Transactions on Software Engineering, 35(6), 756-779.

Newell, A., & Simon, H. A. (1972). Human problem solving. Englewood Cliffs, NJ: Prentice-Hall.

Nolte, A., Bernhard, E., Recker, J., Pittke, F., & Mendling, J. (2016). Repeated use of process models: The impact of artifact, technological, and individual factors. Decision Support Systems, 88, 98-111.

Oliver, R. L. (1977). Effect of expectation and disconfirmation on postexposure product evaluations - an alternative interpretation. Journal of Applied Psychology, 62(4), 480- 486.

OMG. (2011). Business process model and notation (bpmn): Version 2.0 Retrieved from http://www.omg.org/spec/BPMN/2.0

Opdahl, A. L., & Henderson-Sellers, B. (2002). Ontological evaluation of the uml using the bunge-wand-weber model. Software and Systems Modeling, 1(1), 43-67.

Parsons, J. (2011). An experimental study of the effects of representing property precedence on the comprehension of conceptual schemas. Journal of the Association for Information Systems, 12(6), 401-422.

Petre, M. (2013). Uml in practice. Paper presented at the 2013 International Conference on Software Engineering, San Francisco, California.

Pretz, J. E., Naples, A. J., & Sternberg, R. J. (2003). Recognizing, defining, and representing problems. In J. E. Davidson & R. J. Sternberg (Eds.), The psychology of problem solving (pp. 3-30). New York, NY: Cambridge University Press.

Puolamäki, K., & Bertone, A. (2009). Introduction to the special issue on visual analytics and knowledge discovery. SIGKDD Explorations, 11(2), 3-4.

Purao, S., Rossi, M., & Bush, A. (2002). Towards an understanding of problem and design spaces during object-oriented systems development. Information and Organization, 12(4), 249- 281.

Recker, J. (2010). Continued use of process modeling grammars: The impact of individual difference factors. European Journal of Information Systems, 19(1), 76-92.

Recker, J. (2013). Empirical investigation of the usefulness of gateway constructs in process models. European Journal of Information Systems, 22(6), 673-689.

Recker, J., & Dreiling, A. (2011). The effects of content presentation format and user characteristics on novice developers’ understanding of process models. Communications of the Association for Information Systems, 28(6), 65-84.

Recker, J., Indulska, M., Green, P., Burton-Jones, A., & Weber, R. (2019). Information systems as representations: A review of the theory and evidence, Journal of the Association for Information Systems, 20(6), 735-786

Recker, J., Indulska, M., Rosemann, M., & Green, P. (2010). The ontological deficiencies of process modeling in practice. European Journal of Information Systems, 19(5), 501- 525.

Recker, J., Rosemann, M., Green, P., & Indulska, M. (2011). Do ontological deficiencies in modeling grammars matter? MIS Quarterly, 35(1), 57-79.

Recker, J., Rosemann, M., Indulska, M., & Green, P. (2009). Business process modeling: A comparative analysis. Journal of the Association for Information Systems, 10(4), 333-363.

Rioux, K. (2005). Information acquiring-and-sharing. In K. E. Fisher, S. Erdelez & L. McKechnie (Eds.), Theories of information behavior (pp. 169-173). Medford, NJ: Information Today.

Rosemann, M., Green, P., & Indulska, M. (2004). A reference methodology for conducting ontological analyses. In H. Lu, W. Chu, P. Atzeni, S. Zhou & T. W. Ling (Eds.), Conceptual modeling: ER 2004 (Vol. 3288, pp. 110-121). Shanghai, China: Springer.

Rosemann, M., Recker, J., Green, P., & Indulska, M. (2009). Using ontology for the representational analysis of process modeling techniques. International Journal of Business Process Integration and Management, 4(4), 251-265.

Samuel, B. M., Watkins III, L. A., Ehle, A., & Khatri, V. (2015). Customizing the representation capabilities of process models: Understanding the effects of perceived modeling impediments IEEE Transactions on Software Engineering, 41(1), 19-39.

Samuelson, P. A., & Nordhaus, W. D. (2001). Microeconomics (17th ed.). Boston, MA: McGraw-Hill/Irwin.

Scott, J. (2000). Rational choice theory. In G. Browning, A. Halcli & F. Webster (Eds.), Understanding contemporary society: Theories of the present (pp. 126-138). Thousand Oaks, CA: SAGE.

Shanks, G., Tansley, E., Nuredini, J., Tobin, D., & Weber, R. (2008). Representing part–whole relations in conceptual modeling: An empirical evaluation. MIS Quarterly, 32(3), 553-573.

Siau, K., & Lee, L. Y. (2004). Are use case and class diagrams complementary in requirements analysis: An experimental study on use case and class diagrams in UML. Requirements Engineering, 9(4), 229-237.

Siau, K., & Rossi, M. (2011). Evaluation techniques for systems analysis and design modelling methods - a review and comparative analysis. Information Systems Journal, 21(3), 249-268.

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257-285.

Truex, D. P., & Baskerville, R. (1998). Deep structure or emergence theory: Contrasting theoretical foundations for information systems development. Information Systems Journal, 8(2), 99-118.

Tuovinen, J. E., & Sweller, J. (1999). A comparison of cognitive load associated with discovery learning and worked examples. Journal of Educational Psychology, 91(2), 334-341.

Urquhart, C., & Fernandez, W. D. (2013). Using grounded theory method in information systems: The researcher as blank slate and other myths. Journal of Information Technology, 28(3), 224-236.

Venkatesh, V., & Davis, F. D. (2000). A theoretical extension of the technology acceptance model: Four longitudinal field studies. Management Science, 46(2), 186-204.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.

Vessey, I., & Galletta, D. F. (1991). Cognitive fit: An empirical study of information acquisition. Information Systems Research, 2(1), 63-84.

Wand, Y., & Weber, R. (1989). An ontological evaluation of systems analysis and design methods. In E. D. Falkenberg & P. Lindgreen (Eds.), Information system concepts: An indepth analysis. Proceedings of the ifip tc 8/wg 8.1 working conference on information system concepts (pp. 79-107). Amsterdam: Elsevier.

Wand, Y., & Weber, R. (1990). An ontological model of an information system. IEEE Transactions on Software Engineering, 16(11), 1282-1292.

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information systems analysis and design grammars. Journal of Information Systems, 3(4), 217-237.

Wand, Y., & Weber, R. (1995). On the deep structure of information systems. Information Systems Journal, 5(3), 203-223.

Wand, Y., & Weber, R. (2002). Research commentary: Information systems and conceptual modeling - a research agenda. Information Systems Research, 13(4), 363-376.

Ward, M., & Sweller, J. (1990). Structuring effective worked examples. Cognition and Instruction, 7(1), 1-39.

Weber, R. (1997). Ontological foundations of information systems. Melbourne, Australia: Coopers & Lybrand and the Accounting Association of Australia and New Zealand.

Weber, R. (2012). Evaluating and developing theories in the information systems discipline. Journal of the Association for Information Systems, 13(1), 1-30.

Weber, R., & Zhang, Y. (1996). An analytical evaluation of Niam’s grammar for conceptual schema diagrams. Information Systems Journal, 6(2), 147-170.

Whetten, D. A. (1989). What constitutes a theoretical contribution? Academy of Management Review, 14(4), 490-495.

Whiteley, D. (2013). An introduction to information systems. London: Palgrave Macmillan.

Whittle, J., Hutchinson, J., & Rouncefield, M. (2014). The state of practice in model-driven engineering. IEEE Software, 31(3), 79-85.

Wilson, T. D. (1999). Models in information behaviour research. Journal of Documentation, 55(3), 249-270.

Wood, C., Sullivan, B., Iliff, M., Fink, D., & Kelling, S. (2011). Ebird: Engaging birders in science and conservation. PLoS Biology, 9(12), e1001220.

Xue, L., Ray, G., & Gu, B. (2011). Environmental uncertainty and it infrastructure governance: A curvilinear relationship. Information Systems Research, 22(2), 389-399.

Yourdon, E. (1989). Modern structured analysis. Upper Saddle River, NJ: Prentice-Hall.

Zhang, H., Kishore, R., Sharman, R., & Ramesh, R. (2007). Agile integration modeling language (aiml): A conceptual modeling grammar for agile integrative business information systems. Decision Support Systems, 44(1), 266-284.

Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. MIS Quarterly, 22(3), 313-334.

zur Muehlen, M., & Indulska, M. (2010). Modeling languages for business processes and business rules: A representational analysis. Information Systems, 35(4), 379-390.

zur Muehlen, M., & Recker, J. (2008). How much language is enough? Theoretical and practical use of the business process modeling notation. In M. Léonard & Z. Bellahsène (Eds.), Advanced information systems engineering: CAISE 2008 (pp. 465-479). Montpellier, France: Springer.

## Appendix A: Background to Representation Theory and Definitions of Key Constructs

Representation theory (Wand & Weber, 1990, 1993, 1995) addresses the question how well conceptual modeling grammars can generate faithful (i.e., clear, complete, and accurate—see Weber, 1997, p. 83) representations of relevant real-world phenomena. To identify relevant types of real-world phenomena, the theory adopts and modifies an ontological theory of the real world proposed by Bunge (1977, 1979). Representation theory suggests a mapping between the set of existing constructs in a conceptual modeling grammar that is available to the user to model aspects of the real world, and the set of constructs in a benchmark ontology (such as Bunge’s) that is required and sufficient to describe real-world phenomena.<sup>4</sup> Based on this mapping, Wand and Weber (1993) suggest two basic criteria: A good modeling grammar—or, indeed, a good conceptual model—should be ontologically complete (i.e., exhibit no construct deficit) and ontologically clear (i.e., exhibit no construct overload, redundancy, or excess) in order to accurately and unambiguously represent all required real-world phenomena in the business domain that the IS supports.

Relevant construct definitions of Wand and Weber’s theory are provided in Table A1. Since Burton-Jones et al. (2017) and Recker et al. (2019) review the theory and the literature it supports, we do not discuss it in detail here. However, three observations about this literature are relevant to our paper:

1. This theory has been subjected to various tests and applications (Burton-Jones et al., 2017). However, the research has largely been on single grammars or single models, examining questions such as whether ontological deficiencies in a grammar lower perceptions of its usefulness (Recker et al., 2011), whether ontological deficiencies in a grammar inhibit users’ ability to faithfully model a particular real-world phenomenon (e.g., Bodart et al., 2001; Shanks et al., 2008; Parsons, 2011), and whether users’ ability to understand a real-world domain is inhibited by deficiencies in the conceptual model (e.g., Gemino & Wand, 2005; Bowen et al., 2006; Evermann & Wand, 2006; Bera, Burton-Jones, & Wand, 2011).

2. All theory-based evaluations of conceptual modeling grammars (e.g., UML, OML, OPM, ERD, DFD, BPMN, Petri nets, MibML, WSDL, BPEL, and others) to date have shown that no available grammar is ontologically complete (e.g., Wand & Weber, 1993; Weber & Zhang, 1996; Opdahl & Henderson-Sellers, 2002; Irwin & Turk, 2005; Green et al., 2007; Recker et al., 2009). Therefore, even users who want to create models that fully represent all aspects of the real-world phenomena they want to represent cannot. As such, no single conceptual model offers a full representation of a real-world domain. Green (1996) and Weber (1997, pp. 100-102) thus make two predictions, suggesting that users will employ modeling grammars in combination to address deficits in any one grammar. First, model designers will select grammar combinations with maximal ontological completeness—that is, a combination that minimizes total construct deficit and covers as many aspects of the focal real-world phenomenon as possible. Second, model designers will select grammar combinations with minimal ontological overlap—that is, combinations that minimize the grammars’ overlap concerning representations of real-world phenomena that can be modeled.

While researchers have developed propositions and gathered data about which grammar combinations designers might select (Green et al., 2007; zur Muehlen & Indulska, 2010; Green et al., 2011), this work has not been extended to examine model readers’ interpretations of combinations of models (rather than the grammars used to construct them).

3. The existing empirical work has demonstrated that ontological deficiencies can predict weaknesses in the use of conceptual models or grammars. However, these effects are not uniform or consistent. On the one hand, implications of ontological incompleteness appear clear: The lack of potentially relevant information about a real-world domain diminishes the level of understanding users can generate (e.g., Bajaj, 2004; Parsons, 2011), which often leads them to seek workarounds and customizations (Recker et al., 2010; Green et al., 2011, Samuel et al., 2015). They devise new grammatical constructs, access additional grammars or “aids,” or refer to additional documentation to provide the meaning missing from the model. On the other hand, deficiencie of ontological clarity—in particular, redundancy—do not always have clear effects (Fickinger & Recker, 2013). Construct redundancy can have positive consequences for users (Green & Rosemann, 2001), no apparent consequences (Recker et al., 2010), or only partially negative consequences (Recker et al., 2011). Therefore, redundancy of representations between models may be either beneficial or a detriment.

These observations indicate at least one nontrivial dialectical logic involved in how individuals might interpret multiple models in combination: On the one hand, it seems logical for users to seek multiple models if these models would provide a more complete representation of a real-world domain. On the other hand, because information from one model may also be contained in a second model, multiple models are often at least partially redundant, and the representations may thus partially overlap. It remains unclear whether this situation yields an advantage or an issue: Wand and Weber’s theory predicts a lack of clarity from redundancy, but the empirical evidence from single grammars (Recker et al., 2010, Recker et al., 2011) and even multiple grammars (Green & Rosemann, 2001; Gemino and Parker, 2009) suggests that users may sometimes experience benefits from redundancies. Our theory development provides an attempt to unpack this dialectic.

Table A1. Key Construct Definitions

<table><tr><td>Construct</td><td>Definition</td><td>Relevant reference</td></tr><tr><td>Representation</td><td>A model of someone&#x27;s or some group&#x27;s perception of the meaning of a real-world phenomenon.</td><td>Wand &amp; Weber (1995, p. 207)</td></tr><tr><td>Real-world phenomenon</td><td>The aggregation of constituent things and their properties that exist in the real world, as perceived by someone or some group.</td><td>Weber (1997, p. 34, p. 72)</td></tr><tr><td>Conceptual model</td><td>The script (i.e., a meaningful, orderly collection of symbols) that embodies the description of the real-world phenomenon as perceived by someone or some group.</td><td>Weber (1997, p. 75)</td></tr><tr><td>Combined ontological completeness</td><td>The extent to which a conceptual model combination of two or more scripts provides a full representation of someone&#x27;s or some group&#x27;s perception of the meaning of some real-world phenomenon.</td><td>Newly developed construct</td></tr><tr><td>Ontological overlap</td><td>The extent to which two or more scripts in a conceptual model combination share model constructs that provide the same representation of some real-world phenomenon.</td><td>Newly developed construct</td></tr><tr><td>Maximal ontological completeness</td><td>The fullest level of representation of someone&#x27;s or some group&#x27;s perception of the meaning of some real-world phenomenon attained by one out of several combinations of conceptual models.</td><td>Newly developed construct</td></tr><tr><td>Minimal ontological overlap</td><td>The lowest level of shared representations of someone&#x27;s or some group&#x27;s perception of the meaning of some real-world phenomenon in one out of several combinations of conceptual models.</td><td>Newly developed construct</td></tr><tr><td>Interpretation of conceptual models</td><td>The extent to which reading one or more conceptual models provides an individual user with a complete, clear, and accurate understanding of the meaning of the described real-world phenomenon in a goal-directed activity.</td><td>Newly developed construct</td></tr><tr><td>Selection of model combination</td><td>The decision to choose to employ one set of two or more conceptual models for a given task from a larger set of available conceptual models.</td><td>Newly developed construct</td></tr><tr><td>Domain understanding</td><td>The new knowledge that readers generate about the elements in a real-world domain and the actual and possible relationships between these elements through the organization and integration of information content in the conceptual models that are presented to them with their own previous experience and existing mental models.</td><td>Adapted from Mayer (2009)</td></tr><tr><td>Perceived usefulness of model combination</td><td>The degree to which a reader believes that a particular conceptual model combination was effective in achieving the intended task objectives.</td><td>Adapted from Maes &amp; Poels (2007, p. 709)</td></tr></table>

## Appendix B: Illustrating Procedures for Enacting the Theory

Here we describe procedures for applying our theory to the analysis of multiple models. To keep this illustration simple, we use materials from an established textbook for systems analysis and design: the High-Peak Bicycles case described by Whiteley (2013, pp. 228-263). We chose this case because the textbook features a wide selection of models for this scenario.

The case describes the composition of an information system to maintain records of bicycle rentals, with requirements that the system allows for maintaining a bike register, renting out and returning rentals, allocating bikes, processing transactions, and other functionalities. We focus on four types of models used in the case: use case, entity-relationship, data flow, and sequence diagram (Figure B1).<sup>5</sup>

The procedure for analyzing the four models used in the High-Peak Bicycles case involves three steps: (1) performing an interpretation mapping, (2) establishing levels of maximal ontological completeness and minimal ontological overlap, and (3) deriving hypotheses from the analysis. We describe each, in turn.

![](/api/attachments/9ESHKXZG/fulltext/images/ec7e495e53b80627e85431e4c43dbaaaa07d05380d5bd6219fb05adee9b2e5c0.jpg)  
Figure B1. Conceptual models for the High-Peak Bicycles case (Whiteley, 2013, pp. 228-263)

## B1. Performing Interpretation Mappings

The first step, interpretation mapping (Wand & Weber, 1993, p. 221), involves matching grammar constructs featuring in each of the models to an ontological benchmark such as Bunge’s (1977, 1979) ontological theory. The constructs described in Bunge’s ontology as used in representation theory are summarized by Recker et al. (2009). A detailed description of these constructs is provided by Weber (1997). Guidelines for carrying out interpretation mappings are also available (Rosemann, Green, & Indulska, 2004; Rosemann et al., 2009). For the four models in the High-Peak Bicycles case, we conducted the interpretation mapping in three steps:

1. We identified the published ontological analyses for the grammars used to create the four diagrams. Irwin and Turk (2005) evaluated the use case modeling grammar; Wand and Weber (1989) evaluated the data flow diagramming grammar; Green et al. (2011) evaluated the entity-relationship modeling grammar; and Opdahl and Henderson-Sellers (2002) evaluated sequence diagrams as part of the UML grammar.

2. For each grammar, we identified all grammar constructs included in the models shown in Figure B1. For instance, the use case diagram in the case includes the constructs “Actor” and “Use Case” but not the constructs “System” or “Extend” (Irwin & Turk, 2005, p. 5).

3. For each construct, we reviewed the grammar mappings and corresponding mapping rationale in the original analyses to confirm that they applied to the models in Figure B1. This task was important especially for grammar constructs that are overloaded in terms of grammar specification (i.e., it mapped to at least two ontological constructs—see Wand & Weber, 1993). In such instances, it was important to evaluate which meaning was ascribed to the construct in the model in order to identify the corresponding ontological construct present in the model. This step was important because interpretation mappings, in general, are not just a 1:1 correspondence of ontological to grammatical constructs. Therefore, in any model, overloaded grammar constructs could have more than one ontological interpretation. Still, for validity and replicability purposes, we used the interpretations from the literature (Point 1 above) whenever possible.

Table B2 details the rationales behind each mapping, and Table B3 summarizes the mapping results. Across the four diagrams, a total of ten distinct ontological constructs are represented.

Table B2. Ontological Evaluations of Conceptual Model Constructs in the Case

<table><tr><td>Conceptual model type</td><td>Grammar construct</td><td colspan="2">Example construct symbol</td><td>Ontological construct</td><td>Rationale</td></tr><tr><td rowspan="4">Use case diagram</td><td>Actor</td><td colspan="2"><img src="/api/attachments/9ESHKXZG/fulltext/images/fe9bc47b34ac7cf08cf355faa8e4bfd7b6aa4dcd24bf58c767c7df767bf98579.jpg"/>Staff</td><td>Class</td><td>Staff and Customer are roles that describe specific types of things (e.g., humans). See Irwin and Turk (2005, p. 13).</td></tr><tr><td>Use case</td><td colspan="2"><img src="/api/attachments/9ESHKXZG/fulltext/images/23dc2ac0a0fa1bc2b26479adeedfdd6558cfccf185900d1560744428196914b8.jpg"/></td><td>Transformation</td><td>Use cases describe sets of actions as mappings that will change the state of the system.</td></tr><tr><td>Association</td><td colspan="2"></td><td>Binding mutual property</td><td>Associations draw links between actors and use cases, such as which role is authoritative for carrying out an action.</td></tr><tr><td>Generalization</td><td colspan="2"></td><td>Excess</td><td>Generalization between use cases does not carry an ontological meaning because it violates the “kind of” relationship that can exist between things (but not between processes and changes of states. See Irwin and Turk (2005, p. 13).</td></tr><tr><td rowspan="2">Data flow diagram</td><td>External entity</td><td colspan="2"><img src="/api/attachments/9ESHKXZG/fulltext/images/8ff948abcecf24698c47710353cac34c62470cb11d8df9631835fafd91788ccc.jpg"/></td><td>Class</td><td>External entities represent types of a thing that share similar properties.</td></tr><tr><td>Data store</td><td>D3</td><td>customer</td><td>State</td><td>Data stores represent information about the state of a thing (e.g., the current values of relevant variables about a customer). See Wand and Weber (1989, p. 92).</td></tr><tr><td rowspan="3"></td><td>Data flow</td><td colspan="2"> $rental$ </td><td>Event</td><td>Data flows can represent external events (e.g., rental) or internal events (e.g., nonreturn).</td></tr><tr><td rowspan="2">Process</td><td>02</td><td>shop</td><td rowspan="2">Transformation</td><td rowspan="2">Processes describe mappings that define how things change from one state into another.</td></tr><tr><td colspan="2">maintain rental rates</td></tr><tr><td rowspan="5">Entity-relationship diagram</td><td rowspan="2">Entity type</td><td colspan="2">Customer</td><td rowspan="2">Class and property</td><td rowspan="2">Entity types represent types of a thing that share similar properties in general (e.g., customers share the common property of being customers of a particular company). See Green et al. (2011, p. 6).</td></tr><tr><td colspan="2">custNo custName custTel</td></tr><tr><td rowspan="2">Relationship type</td><td colspan="2">Bike Class</td><td rowspan="2">Coupling and binding mutual property</td><td rowspan="2">Relationship types describe the binding mutual properties that couple two classes of things.</td></tr><tr><td colspan="2">classCode classDesc</td></tr><tr><td>Cardinality of relationship</td><td colspan="2">1..1</td><td>State law</td><td>Cardinality constraints represent a state law that constrains the values of a binding mutual property to certain conditions.</td></tr><tr><td rowspan="6">Sequence diagram</td><td>Object</td><td colspan="2">a Customer</td><td>Thing, state, and event</td><td>Some objects (e.g., a bike or a customer) in the UML sequence diagram are actual, physical things whose properties are modified over the course of sequence.Other objects (e.g., rent out, control) describe events that occur and lead to state changes.Finally, some objects (e.g., a rental rate) describe the current state vector of some thing (in this case, the current value for a rental rate for a particular bike).</td></tr><tr><td>Object lifeline</td><td colspan="2"></td><td>History</td><td>The lifeline represents the history of events and state changes that occur to a thing (e.g., a bike).</td></tr><tr><td>Message</td><td colspan="2"></td><td rowspan="3">Coupling and binding mutual property</td><td rowspan="3">Messages describe how a thing acts on another thing by changing the binding mutual property between them. See Opdahl and Henderson-Sellers (2002, p. 55). Ontologically, messages, return messages, and self-messages all denote types of binding mutual properties and are, therefore, redundant.</td></tr><tr><td>Return message</td><td colspan="2">&lt;----&gt;</td></tr><tr><td>Self-message</td><td colspan="2"></td></tr><tr><td>Guard condition</td><td colspan="2">haveCust = check()→</td><td>State Law</td><td>Guard conditions describe properties that restrict the functions of a mutual property between things to a lawful subset.</td></tr><tr><td colspan="6">Notes: Terms in bold are constructs and labels used in the diagrams in Figure 6. Italic terms are constructs in representation theory (Weber, 1997) as defined by Recker et al. (2009, p. 361).</td></tr></table>

Table B3. Summary of Interpretation Mapping of the Four Conceptual Models

<table><tr><td>Ontological construct</td><td>Use case diagram</td><td>Data flow diagram</td><td>Entity-relationship diagram</td><td>Sequence diagram</td></tr><tr><td>Thing</td><td></td><td></td><td></td><td>√</td></tr><tr><td>Property in general</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Binding mutual property</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Class</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>State</td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>State law</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Event</td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>History</td><td></td><td></td><td></td><td>√</td></tr><tr><td>Coupling</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Transformation</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Sum</td><td>3 out of 10</td><td>4 out of 10</td><td>5 out of 10</td><td>7 out of 10</td></tr></table>

Table B4. MOC and MOO of Pairwise Combinations of Conceptual Models in the High-Peak Bicycles Case

<table><tr><td>Diagram type</td><td>Use case diagram</td><td>Data flow diagram</td><td>Entity-relationship diagram</td><td>Sequence diagram</td></tr><tr><td>Use case diagram</td><td>0</td><td>2</td><td>2</td><td>1</td></tr><tr><td>Data flow diagram</td><td>5</td><td>0</td><td>1</td><td>2</td></tr><tr><td>Entity-relationship diagram</td><td>6</td><td>8</td><td>0</td><td>3</td></tr><tr><td>Sequence diagram</td><td>9</td><td>9</td><td>9</td><td>0</td></tr></table>

Note: MOC of the combinations is given in the darker grey cells below the diagonal; MOO is given in the lighter grey cells above the diagonal.

Table B5. MOC and MOO of 3-Way and 4-Way Combinations of Conceptual Models in the High-Peak Bicycles Case

<table><tr><td>1 Use case diagram2 Data flow diagram3 Entity-relationship diagram</td><td>1 Use case diagram2 Data flow diagram3 Sequence diagram</td><td>1 Use case diagram2 Entity-relationship diagram3 Sequence diagram</td><td>1 Data flow diagram2 Entity-relationship diagram3 Sequence diagram</td><td>1 Use case diagram2 Data flow diagram3 Entity-relationship diagram4 Sequence diagram</td></tr><tr><td>MOC: 8</td><td>MOC: 9</td><td>MOC: 10</td><td>MOC: 10</td><td>MOC: 10</td></tr><tr><td>MOO: 3</td><td>MOO: 5</td><td>MOO: 4</td><td>MOO: 6</td><td>MOO: 7</td></tr></table>

## B2. Determining the Levels of MOC and MOO

The next step in in applying our theory involves determining the levels of MOC and MOO of the possible combinations of conceptual models. This is done by computing the sum of covered ontological constructs represented in any combination (MOC) and the sum of shared ontological constructs (MOO) in any combination. Table B4 and Table B5 summarize these results.

Having determined the levels of MOC and MOO of the possible combinations of conceptual models, we can now evaluate which combinations are preferable. Because conceptual model interpretation is a goal-directed activity occurring as part of some task, we will assume in what follows that the task is systems analysis and design (Kendall & Kendall, 2008).

We examine pairwise combinations first. The best model combination in terms of maximal ontological completeness is the sequence diagram with a choice of the use case, the data flow, or the entity-relationship diagram (Table B4). All three pairs cover nine of ten ontological constructs (Table B3). The worst combination is the use case diagram and the data flow diagram, which covers only five ontological constructs. In terms of minimal ontological overlap, either the combination of the entity-relationship diagram with the data flow diagram or the combination of the sequence diagram with the use case diagram achieves an overlap of one construct (class and binding mutual property, respectively; see Table B3). The worst combination is the entity-relationship diagram with the sequence diagram, which shares representations for three ontological constructs (binding mutual property, state law, and coupling). In terms of both maximal ontological completeness and minimal ontological overlap, Table B4 suggests that the best pairwise combination is the use case diagram and the sequence diagram (MOC: 9. MOO: 1) because both remaining maximally ontologically complete pairs have an overlap of two constructs.

An examination of all other potential 3-way and 4-way model combinations (Table B5) suggests that the optimal combination is the triple—the use case, entity-relationship, and sequence diagram—because it achieves MOC (all ten constructs) with MOO (four constructs). From the viewpoint of maximal ontological completeness, the worst combination is the triple—the use case, the data flow, and the entity-relationship diagram (MOC: 8). From the viewpoint of minimal ontological overlap, the worst combination is the triple data flow, the entity-relationship, and the sequence diagram (MOO: 6). Note that the combination of all four models (MOC: 10, MOO: 7) is worse for interpretation than the noted optimal triple because it achieves the same level of ontological completeness while having higher levels of ontological overlap.

## B3. Deriving Propositions

The final step in applying our theory is to derive propositions about users’ selection, understanding, and perceived usefulness of conceptual model combinations (for the task of systems analysis and design) from the analysis summarized in Table B4 and Table B5.

Regarding Proposition 1, our theory suggests that users will select from the set of diagrams in the following order: first, the sequence diagram and the entity-relationship diagram (because this combination has the highest increase in ontologica completeness); and second, the addition of the use case diagram (because in this combination ontological overlap increases to a lesser extent than it does with the data flow diagram, while both additions increase ontological completeness in the same way). Should the data flow diagram be selected in addition, the theory suggests that users will discard this diagram from the combination in order to decrease the level of ontological overlap.

Regarding Proposition 2, our analysis suggests, first, that users will generate the highest level of domain understanding when interpreting the triple-use case diagram, the entity-relationship diagram, and the sequence diagram and, second, that interpreting this triple will allow users to generate more domain understanding than will interpreting all four diagrams together because the triple exhibits less ontological overlap while exhibiting the same level of completeness.

Regarding Proposition 3, our analysis suggests, first, that users will evaluate the triple—the use case diagram, the entityrelationship diagram, and the sequence diagram—as the most useful combination. Our analysis also suggests that the perceived usefulness of all four diagrams will be lower than the perceived usefulness of said triple. Finally, users will perceive the pair—use case diagram and sequence diagram—as more useful than all four diagrams together. This situation occurs because, even though the combined ontological completeness is lower in the pair, the ontological overlap is much lower than it is between all four models. Our theory suggests that practitioners will evaluate this pair as “useful enough” for the task at hand.

To summarize, we provided this illustration of procedure to demonstrate how to apply our theory to generate empirically falsifiable predictions—i.e., testable hypotheses. It was not our intent to demonstrate that the hypotheses are unequivocally correct but rather to show that the theory we formulated allows both for analysis (i.e., What are the ontological properties of various combinations of conceptual models?) and explanation (i.e., Which combinations do users evaluate as faithful?) (Gregor, 2006).

## Appendix C: Establishing Boundary Conditions through Empirical Research

Recall that our theory describes a model of properties vested in conceptual models as artifacts. This focus entails several assumptions that limit the scope of contexts in which our theory holds. We describe several potential boundary conditions in the Discussion section of this paper. Still, we wish to encourage researchers to seek out even more boundaries because through such work greater faith can be placed in a theory from the knowledge of the conditions where and why predictions of the theory succeed or fail (Gray & Cooper, 2010).

One way to tease out a theory’s boundaries further would be through the use of meta-analysis to quantitatively assess whether a theory’s assumptions and predictions hold under a wide range of circumstances (King & He, 2005). This approach, however, requires a large sample of empirical studies. Another way is to investigate how potential moderators affect the associations stipulated in a theory (Edwards & Berry, 2010, p. 676). Given that our theory has not yet been tested empirically, we find this approach more useful because contemplating potential moderator variables could feature in the design of empirical studies to evaluate our propositions. In what follows, we describe what we believe are three relevant variables that should be incorporated into research designs as potential moderators, and we present arguments concerning how they might influence what we regard as the principal proposition in our theory: the development of domain understanding derived from interpreting multiple conceptual models. We leave the exploration of variations on the other propositions to another time. Of course, our speculations remain tentative at this stage: the role of the variables may also be as control, interaction, or mediation terms. Still, they remain important to the design of a study.

## C1. Environmental Uncertainty

One assumption is central to our theory: the primary aim for the interpretation of conceptual models in isolation or in combination is to obtain a complete, clear, and accurate representation of the relevant real-world phenomenon (Wand & Weber, 1990, 1993). This assumption might be challenged in some contexts, as “complete, clear and accurate” might not necessarily be a central aim for certain tasks.<sup>6</sup> For example, practices that involve system analysis and design have changed. One apparent shift is the move away from legacy systems and packaged software toward agile approaches to systems development (Fowler & Highsmith, 2001).

Agile approaches to systems development embrace readiness “to rapidly or inherently create change, proactively or reactively embrace change, and learn from change while contributing to perceived customer value (economy, quality, and simplicity), through its collective components and relationships with its environment” (Conboy, 2009, p. 340). This context presents challenges to traditional uses of conceptual modeling (Erickson, Lyytinen, & Siau, 2005, Zhang, Kishore, Sharman, & Ramesh, 2007) because the environment in which conceptual models are used is more fluid, emergent, complex, and dynamic: models of systems are rapidly being translated into running prototypes; new system structures and features emerge through constant and frequent feedback, and requirements changes are embraced. In turn, analysts and designers cannot fully anticipate how a system will evolve, what new functionality might be added, or what purposes the system might need to satisfy in the real-world domain. Overall, the context for the use of conceptual models in such settings is characterized by environmental uncertainty.<sup>7</sup>

In task settings that are characterized by environmental uncertainty, the clarity of representation provided by conceptual models might be more important than their completeness. If the context in which individuals interpret representations as they perform tasks is unclear, users encounter more stimuli to process (e.g., task, representation, changing requirements, different stakeholders, evolving features, changing deep structure). In such situations, any way to reduce cognitive load will help users select, process, and integrate relevant information in their mental representations and perform their tasks (Mayer, 2009). Cognitive load in the interpretation of conceptual models stems from the number of representational elements provided (which can be reduced by decreasing the combined ontological completeness of conceptual models) and the representational elements’ lack of clarity (which can be increased by lowering the ontological overlap of conceptual models). Therefore, in task contexts characterized by high environmental uncertainty, the positive impact of a model combination’s combined ontological completeness on users ability to generate domain understanding might be diminished and the negative impact of a model combination’s ontological overlap on users’ ability to generate domain understanding might be strengthened.

## C2. Task Nature

Tasks that involve the processing of information conveyed in models are also changing. For example, an article in this journal from April 2017 discusses challenges to common conceptual modeling assumptions that flow from organizations’ increasing reliance on externally produced information, such as online user-generated content (Lukyanenko et al., 2017).

This and other apparent shifts in information processing tasks can be described as a move in emphasis from exploitative to explorative tasks (March, 1991). Explorative tasks are characterized by a search for novel and innovative ways of doing things and are associated with experimentation, play, innovation, and/or discovery (March, 1991). In such tasks, available information may be used for purposes other than those for which the information was originally collected or the representation of the information was developed (Lukyanenko, Parsons, & Wiersma, 2014b). For example, citizen science projects involve mining user-generated content about some real-world domain (e.g., observations of native birds in some region) for unanticipated, novel, and interesting insights (Wood, Sullivan, Iliff, Fink, & Kelling, 2011). Likewise, in the organizational redesign of operational procedures, analysts read conceptual models with the aim of finding creative solutions about how operational processes might be improved (Figl & Recker, 2016), without knowing ex ante what the solution might look like. The lack of predefined outcomes and unanticipated expectations about the informational needs has important implications for conceptual modeling: quality of information is no longer defined only by precision, accuracy, or other traditional metrics (Lukyanenko, Parsons, & Wiersma, 2016) but must include an evaluation of the ability “to spot something interesting, unexpected, or novel” (p. 448).

It is likely that in contexts in which the nature of the task setting moves from exploitation to exploration, the strength of the associations between combined ontological completeness and ontological overlap on an individual’s ability to generate domain understanding varies as well. For example, in model interpretation settings characterized by explorative rather than exploitative tasks, the completeness of representation that conceptual models provide might be more important than their clarity because informational needs are difficult to anticipate and may even be fluid. What constitutes a relevant aspect of some real-world phenomenon cannot always be predefined. For example, Lukyanenko et al. (2014a, p. 6) observe how even small citizen science projects concerned with conservation in local, confined geographic areas may find it impossible to develop a classification model suitable to describe everything that might be observed because distributions of plants and animals are simply not static.

In settings where tasks are geared toward exploration, excluding some such aspect in a representation could potentially lead to inaccurate uses (e.g., misidentifications), failure to spot relevant insights, and thus misinformation. Indeed, Lukyanenko, Parsons, & Wiersma, (2014a, p. 11) report on several observed patterns of mismatching and misclassification stemming from the way that the information about the relevant phenomena (here: animal species observed by citizens) was described in the conceptual model underlying the database structure.

Potential deficiencies in a representation’s clarity, by contrast, may not differ much between task settings of an explorative or exploitative nature, because they can likely be mitigated. For example, many explorative tasks such as knowledge discovery do not act on models or data schema directly but are supported by tools that build on visual analytics (Puolamäki & Bertone, 2009) to convey and communicate information about a real-world domain in a variety of representation formats (e.g., static or interactive, tables versus graphs, with or without transformations into new, semantically meaningful forms). The clarity of these representations may vary; however, given a complete representation, it will always be possible to apply formats that provide unambiguous, non-redundant, and non excessive information about some real-world phenomena, whereas no modeling tool, however clear in the meaning of its constructs, can make an impoverished representation more complete. Therefore, in task settings of an explorative, rather than exploitative nature, the positive impact of combined ontological completeness of model combinations on users’ ability to generate domain understanding might be strengthened, whereas the negative impact of ontological overlap of model combinations on users’ ability to generate domain understanding might be diminished.

It is also likely that these variations are not absolute. For example, when the demands for combined ontological completeness increase in task settings of an explorative nature, so does the cognitive load associated with processing that information presented to the user (Sweller, 1988). It is likely that there will be a tipping point in the positive impact of combined ontological completeness of model combinations on users’ ability to generate domain understanding from a set of models, much like in the law of diminishing returns in economics (e.g., Samuelson & Nordhaus, 2001, p. 110): as the number of representations about a focal real-world phenomenon covered through conceptual models increases, the relative gains in domain understanding will diminish, once the bearable level of cognitive load is surpassed (Miller, 1956). This effect is likely higher in task settings of explorative rather than exploitative nature, because the intrinsic load of these tasks is higher due to their emphasis on discovery learning over schema application (Tuovinen and Sweller, 1999), meaning less information processing capacity remains available in the working memory to process the external information in the models (Sweller, 1988; Chandler & Sweller, 1991).

## C3. Prior Domain Knowledge

A third variable relates to the influence of individual-level attributes characterizing the model reader. As we discuss above, our theory is not a theory of pragmatics or cognitive psychology that would explain how individuals come to learn new knowledge from conceptual models—the theory merely states why attributes of models influence users interpretation (Shanks et al., 2008, Bera et al., 2014, Burton-Jones et al., 2017).

There has been some work that demonstrated that individual-level variables influence the extent to which users develop domain understanding from conceptual models. Among variables such as grammar familiarity (Recker, 2010), modeling experience (Mendling, Strembeck, & Recker, 2012), schema expertise (Khatri & Vessey, 2016) and analyst role (Samuel et al., 2015), prior domain knowledge (Khatri et al., 2006, Bera et al., 2014) stands out as the most widely studied user characteristic in this context.

Prior domain knowledge captures the realm of knowledge an individual has about a particular real-world domain (Alexander, 1992). It describes the mental model individuals have about a domain, and which they use as a basis for internalizing new knowledge presented to them through one or more conceptual models about the domain. In other words, prior domain knowledge determines how much “new information” a model or set of models holds for the person reading it (Mayer, 2009).

Recent evidence about the influence of prior domain knowledge on individuals’ ability to generate domain understanding from interpreting a conceptual model suggests a nonlinear moderation effect in the form of a downward concave curve (Bera et al., 2014): too little or too much prior domain knowledge renders the information in a model either too complex or too redundant if the model is not completely clear.

A similar variation may occur when individuals with very high levels of prior domain knowledge interpret multiple conceptual models: as the level of combined ontological completeness increases, the likelihood that information is added that is already present in the mental model of the reader also increases, in turn only adding nonessential, redundant information that not only fails to add new knowledge for internalization but also renders the information processing more difficult as more cognitive effort must be devoted to identifying additional representational elements and matching them to those already stored in the working memory. Yet, ontological overlap of multiple models may not affect individuals with very high levels of prior domain knowledge much because they can use their knowledge to overcome any such ambiguities (Bera et al., 2014).

However, when individuals with very low levels of prior domain knowledge interpret multiple conceptual models, higher levels of combined ontological completeness and ontological overlap might both have the same effect—that of adding extraneous load to a working memory already operating at capacity (Miller, 1956). Readers with little to no domain knowledge already have difficulties internalizing even a clear single conceptual model because they “have an insufficiently developed mental model to incorporate much meaning…at all” (Bera et al., 2014, p. 403). When assimilation of a relatively small set of new information fails to occur, it is unlikely that the provision of a more complete and thus larger set of new information, let alone one that contains overlap, will be of any benefit.

## About the Authors

Jan Recker is an AIS fellow, Alexander-von-Humboldt fellow, chaired professor of information systems and systems development at the University of Cologne, and adjunct professor at Queensland University of Technology. He is presently editor in chief of the Communications of the Association for Information Systems. His research focuses on systems analysis and design, digital innovation and entrepreneurship, and digital solutions for sustainability challenges.

Peter F. Green is a professor in the School of Accountancy, Queensland University of Technology. From 1999-2013, he was a professor of eCommerce at the University of Queensland. Peter has qualifications in accounting, computer science, and a PhD in commerce (information systems) from the University of Queensland. Peter’s research interests focus on representation theory and its application to many different areas, including accounting information systems. His publications have appeared in journals such as MIS Quarterly, European Journal of Information Systems, Information Systems, Journal of the Association for Information Systems, and others.

Copyright © 2019 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via email from publications@aisnet.org.
