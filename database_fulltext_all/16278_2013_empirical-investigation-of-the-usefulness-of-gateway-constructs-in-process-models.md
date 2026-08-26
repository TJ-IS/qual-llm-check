---
otero_id: 16278
otero_key: "4Y5NT8ZS"
title: "Empirical investigation of the usefulness of Gateway constructs in process models"
authors: "Jan Recker"
year: "2013"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2012.50"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Empirical investigation of the usefulness of Gateway constructs in process models

Jan Recker

Queensland University of Technology, QLD, Australia

Correspondence: Jan Recker, Woolworths Chair of Retail Innovation, Information Systems School, Science & Engineering Faculty, Queensland University of Technology, 126 Margaret Street, Brisbane QLD 4000, Australia. Tel.: þ 61 7 3138 9479; Fax: þ 61 7 3138 9390; E-mail: j.recker@qut.edu.au

## Abstract

Process modeling grammars are used to create scripts of a business domain that a process-aware information system is intended to support. A key grammatical construct of such grammars is known as a Gateway. A Gateway construct is used to describe scenarios in which the workflow of a process diverges or converges according to relevant conditions. Gateway constructs have been subjected to much academic discussion about their meaning, role and usefulness, and have been linked to both process-modeling errors and process-model understandability. This paper examines perceptual discriminability effects of Gateway constructs on an individual’s abilities to interpret process models. We compare two ways of expressing two convergence and divergence patterns – Parallel Split and Simple Merge – implemented in a process modeling grammar. On the basis of an experiment with 98 students, we provide empirical evidence that Gateway constructs aid the interpretation of process models due to a perceptual discriminability effect, especially when models are complex. We discuss the emerging implications for research and practice, in terms of revisions to grammar specifications, guideline development and design choices in process modeling. European Journal of Information Systems (2013) 22, 673–689. doi:10.1057/ejis.2012.50; published online 27 November 2012

Keywords: process modeling; visual expressiveness; process model comprehension; Gateway constructs

## Introduction

When analyzing or designing information systems, analysts frequently use graphical models of the relevant business domain to aid the determination of requirements. Recently, analysts have started to use conceptual models of business processes (process models) to assess or build information systems that are process-aware (Dumas et al, 2005). Process modeling is a primary reason to engage in conceptual modeling (Davies et al, 2006) and has been shown to be a key success factor in organizational and systems re-design projects (Kock et al, 2009).

Process models are specified using process modeling grammars (Recker et al, 2009). These grammars provide sets of graphical constructs, together with rules for how to combine these constructs, to express graphically relevant aspects of business processes, such as the tasks that have to be performed, the actors that are involved in the execution of these tasks, relevant data, and, notably, the control flow logic that describes the logical and temporal order in which tasks are to be performed (Mendling et al, 2012b).

One important aspect in the control flow logic of a business process is that processes often contain decision points where parallel or alternative paths might be taken, or where such paths merge. Such points characterize the convergence or divergence of control flows (Kiepuszewski et al, 2003).

In process modeling grammars, convergence or divergence semantics are typically expressed through grammatical constructs named ‘Gateways’, ‘Connectors’, or ‘Splits’ and ‘Joins’ (e.g., Scheer, 2000; Verbeek et al, 2007). These grammatical constructs have been subjected to much academic debate. For instance, some scholars have argued that these constructs are ill-defined both formally (e.g., Verbeek et al, 2007) and ontologically (Recker et al, 2009). They have also been found to be a key reason for modeling errors such as violation of deadlock and synchronization rules (Kindler, 2005), and may further lead to understandability problems with practitioners (Mendling et al, 2010a). Yet, other studies have shown that Gateway constructs are important elements in expressing important control flow patterns (Van der Aalst et al, 2003) and may further obtain an ontological meaning when seen in a composite context together with other constructs (Soffer et al, 2010).

One reason for the debate in academia stems from the fact that upon its release as version 1.0, the industry standard grammar for process modeling, the Business Process Model and Notation (BPMN, BPMI.org & OMG, 2006), allows a choice between the explicit use of Gateway constructs or the implicit articulation of the same semantics for some convergence and divergence scenarios.

Because of this design choice that is inherent in the grammar specification, opinions about the use of Gateway constructs have been varied and different practices have been proposed and are in use in industry. Some modeling conventions stipulate the use of Gateway constructs because of their ability to explicitly highlight convergence or divergence using dedicated visual symbols (e.g., Weske, 2007, pp. 128–131). Other guidelines (e.g., Silver, 2009, p. 109), however, recommend avoiding Gateway constructs in the expression of convergence and divergence scenarios such as Parallel Splits or Simple Merges and instead suggest implicit representation forms to be used:

Since the two diagrams [containing examples about Parallel split scenarios with and without a Gateway] are equivalent, which one should you use? It’s really a matter of preference. I prefer the one on the right, the implicit parallel split, without a Gateway. [y] Also, some flowcharting conventions use a notation similar to the one on the right to mean exclusive choice, not parallel split. That’s not illogical but it’s not BPMN.

Not only are these alternative modeling styles being advocated in the normative body of knowledge in the process-modeling industry, studies of process model use in practice show that the different styles (viz., the use of Gateway constructs, or implicit modeling) are quite widespread. For instance, reported statistics on process model collections such as those provided by Kunze et al (2011)

show that the use of Gateway constructs ranges from around 74% to only 50% of models in the collection. Thus, it is evident that different modeling practices are not only discussed in the literature but also established in practice.

Different modeling styles available and in use bear the complication that the interpretation of process models can be obstructed or biased by lack of understanding of the intended semantics. Implicit modeling styles rely on deep knowledge of the underlying semantics of the construct combinations; and a lack of this knowledge can potentially result in misinterpretations of the models and subsequently lead to flawed decision-making on the basis of the models.

The objectives in writing this paper are therefore (1) to examine the different modeling practices by offering a valid theoretical and empirical explanation for the effects they provide, and (2) to offer validated results that inform design choices in process modeling, the development of evidence-based modeling guidelines, and the ongoing development and revision of modeling grammars. To that end, we turn to a theory of effective visual notations (Moody, 2009), to discuss perceptual discriminability effects of Gateway construct usage in process models on the ability of model readers to effectively and efficiently interpret the process model. We then report on the design, conduct an analysis of the experimental study in which we tested our predictions with 98 Information Systems students.

We proceed as follows. We begin by reviewing the background to our study, and then draw on theory to hypothesise a set of implications about the use of Gateways in process modeling. We then outline an experiment to test these hypotheses, and discuss the results. Finally, we discuss the limitations of our study and its implications for research and practice before concluding the paper.

## Design choices in process modeling

Process modeling is a widely used approach for describing how businesses conduct their operations, as part of an effort to understand or analyze current operations (‘as is’ modeling), or as part of an effort to design improved blueprints for future operations (‘to be’ modeling). In either case, process modeling typically includes graphical depictions of at least the activities, events/states and control flow logic that constitute a business process (Recker et al, 2009).

The debate about Gateway constructs relates to the control flow logic of a business process. Key elements in the control flow logic are points where the workflow of a process diverges or converges according to relevant conditions of a business rule. Several divergence and convergence scenarios exist, known as control flow patterns (Van der Aalst et al, 2003). We focus on two basic patterns that are fundamental to most business processes:

A fundamental divergence scenario is known as a Parallel Split and is defined as the divergence of a branch into two or more parallel branches each of which execute concurrently (Van der Aalst et al, 2003). An example in a student enrollment process would be the situation ‘after completion of the capture enrolment task, run the create student profile and issue enrolment confirmation tasks simultaneously’.

A fundamental convergence scenario is known as a Simple Merge and is defined as the convergence of two or more branches into a single subsequent branch such that each enablement of an incoming branch results in the thread of control being passed to the subsequent branch (Van der Aalst et al, 2003). An example in a student enrollment process would be the situation ‘after completion of either the pay in cash or the complete credit card transaction task, run the issue confirmation of enrolment task’.

To express Parallel Split or Simple Merge scenarios in a process model, available modeling grammar has typically provided graphical ‘Gateway’ constructs, such as ‘Connectors’ (EPCs, see Scheer, 2000), or ‘Splits’ (YAWL, see van der Aalst & ter Hofstede, 2005).

The current standard grammar for process modeling, BPMN, however, allows for two different modeling styles to articulate Parallel Splits and Simple Merges in process models. Figure 1 shows these different modeling styles for divergence (a Parallel Split, see top-half of Figure 1) and convergence (a Simple Merge, see bottom-half of Figure 1). On the left-hand side of Figure 1, Parallel Split and Simple Merge are represented via explicit visual symbols, viz., the BPMN Gateway constructs (an AND Gateway, and an XOR Gateway). The right hand side of Figure 1 shows the alternative allowed representation form for expressing Parallel Splits and Simple Merges in BPMN, without the use of explicit visual symbols, that is, only via arrangements of flow constructs (the directed arcs).

![](/api/attachments/4Y5NT8ZS/fulltext/images/43ca0ef374cd64b104654ac2222aeaf33493f9e06b5208e61c24acbffc7b9ee2.jpg)  
Figure 1 Alternative representations for two convergence and divergence scenarios in BPMN.

As per original grammar specification (BPMI.org & OMG, 2006, p. 22 and pp. 72–73), the two modeling styles shown in Figure 1 carry equivalent semantics (the real-world meaning of the construct arrangements in a model). This means that the intention of the grammar designers was to offer two representational styles to express the same real-world semantics about processcontrol flow in a process model. The latest release of the BPMN standard, version 2.0, still allows Activity constructs to have multiple incoming or outgoing Sequence Flow constructs with or without the use of Gateway constructs (OMG, 2011, p. 153).

The two representation styles shown in Figure 1 differ in their visual syntax (the type, form and arrangements of the graphical symbols used for representation). The model designer is therefore offered a choice to use, or not to use, the graphical Gateway representation constructs to describe the points of convergence or divergence visually. This decision, essentially, is concerned with the syntax (form of representation) to be used to express certain semantics (e.g., Simple Merges or Parallel Splits). This design choice is crucial to the use of the process models because it can affect how well users working with the models are able to understand the business process modeled, which is important because being able to reach a faithful understanding of the content of a model is a prerequisite for making any decision on basis of the model, be it for workflow execution, systems design or process improvement (Recker & Dreiling, 2011). Indeed, all decisions made on the basis of a process model are dependent, first, on the model design choices made when creating the model, and second, how these design choices in the model are interpreted by the users of the models.

There is evidence to suggest that the design choice between explicit vs implicit visual syntax indeed has an impact on a reader’s ability to interpret the process model. Earlier research in other conceptual modeling domains suggests that implicit representational forms (e.g., implicit representation of composites in ER diagrams) may be difficult to understand (Shanks et al, 2008). Examining this question in the context of Gateway constructs in a process model will clarify whether process models with implicit Simple Merge and Parallel Splits are easier or more difficult to understand, which, in turn, yields insights for ongoing debate about the meaning of Gateway constructs (Recker et al, 2009; Soffer et al, 2010), and their relation to modeling errors (Kindler, 2005) and understandability concerns (Mendling et al, 2010a).

## Theory

## Interpretation of process models

The choice of using or not using Gateway constructs as explicit visual representational forms for Simple Merge and Parallel Split scenarios in process models can be studied from two angles, these being model creation (the design of process models) and model interpretation (the use of process models to build an understanding of the process depicted) (Gemino & Wand, 2004). We focus on model interpretation because this issue is relevant to all potential uses of a process model for different model application tasks, such as systems analysis, communication, design, organisational re-engineering, project management, end user querying and others (Recker et al, 2009).

We examine the question about how well denotational semantics that are built into a modeling grammar by its designers correspond to connotational semantics (Burton-Jones et al, 2009) – that is, how the semantics ascribed to explicit and implicit ways of modeling Parallel Splits and Simple Merges are being interpreted by model users.

Model interpretation can be studied from two perspectives, interpretation fidelity (how faithfully does the interpretation of the model allow the reader to comprehend the domain semantics in the model?) and interpretation efficiency (what resources are required to interpret the model?) (Burton-Jones et al, 2009). A process model is thus considered useful for a modeling-related task if the stakeholders performing these tasks are able to obtain a high-fidelity interpretation of the model in an efficient manner.

Interpretation fidelity is typically measured by examining comprehension task performance (Reijers & Mendling, 2011; Reijers et al, 2011a; Reijers et al, 2011b; Mendling et al, 2012b), that is, by assigning scores for the model users in a task that uses multiple questions to test how well they comprehended the content of a process model.

Interpretation efficiency is typically measured by examining comprehension task efficiency, defined as the time taken to complete the comprehension task (Reijers & Mendling, 2011; Reijers et al, 2011a; Reijers et al, 2011b; Mendling et al, 2012b).

These measures have been used in a variety of related studies. Reijers et al (2011a) examined the use of color highlighting in process models on comprehension task performance and comprehension task efficiency. They found that color highlighting assisted novices in gaining an accurate understanding; however, comprehension task efficiency was not significantly improved. Reijers & Mendling (2011) studied the effects of model complexity on comprehension task performance. They found that the density of a process model and its average connector degree significantly correlated with comprehension task performance; comprehension task efficiency was not considered. In a follow-up study, Mendling et al (2012b) examined the use of abstract vs concrete Activity labels on comprehension task performance and efficiency. They found that both control flow comprehension-task performance and comprehension-task efficiency were improved when Activity labels were omitted. Recker & Dreiling (2011) studied how novice analysts performed when examining familiar vs unfamiliar process models. They found that neither the model-comprehension-task performance nor the modelcomprehension-task efficiency was significantly affected by the choice of models.

## Visual discriminability of modeling grammars

As independent factors that affect the process of model interpretation in terms of both fidelity and efficiency (viz, comprehension task performance and comprehension task completion times), the design choices related to expressing Parallel Split and Simple Merge scenarios in a process model force a user selection of the syntax of a process modeling grammar, viz., the form and arrangement of visual constructs in a process modeling grammar.

Research in diagrammatic reasoning shows that the form of representations has an equal, perhaps even greater, influence on diagram interpretation than their content (Larkin & Simon, 1987; Siau, 2004). This is because human information processing is highly sensitive to the form in which information is presented to the senses. Even apparently minor changes in visual appearance are speculated to have dramatic impacts on understanding and problem-solving performance (Petre, 1995; Cheng et al, 2004). Empirical studies have further shown that the visual syntax of diagrammatic models significantly affects understanding especially by novices (Irani et al, 2001; Hitchman, 2002; Purchase et al, 2004). These findings suggest that visual effects on model interpretation are far from trivial and should be considered with as much attention (if not more) as semantic considerations.

We consider Moody’s (2009) work on the effective visual syntax of modeling grammars to theorise effects of visual syntax choices on process model interpretation. In this theory, principles are provided to define cognitively effective visual modeling grammars. Cognitive effectiveness is defined as the ease, speed and accuracy with which a model representation can be processed by the human mind (Larkin & Simon, 1987). Our interest specifically is in the principle of perceptual discriminability, which suggests that visual constructs in a modeling grammar should be clearly distinguishable from each other (Moody, 2009). Perceptual discrimination is the first step in human graphical information processing, whereby features of the retinal image (e.g., shape, line, color of model constructs) are detected by specialised feature detectors and the model is parsed into its constituent elements for active cognitive processing, where the visual constructs and their relationships are associated to their semantic meaning (Lohse, 1997). Perceptual discriminability is therefore a prerequisite for accurate model interpretation (Winn, 1990).

Perceptual discriminability is dependent on the visual distance between the graphical constructs in a process model, that is, by the construct differences in visual attributes such as size, brightness, color, texture, shape or orientation. The more variety is present in the visual attributes of the constructs in a process model, the greater the visual distance is between the constructs, and consequently, the faster and more accurately they will be recognized (Winn, 1993). This relationship holds for novice analysts more so than for experts because much finer perceptual discriminations can be made with experience (Britton & Jones, 1999).

The primary visual variable used in models to increase the visual distance between the graphical constructs used is shape (Moody, 2009). This is because constructs with different shapes (e.g., rectangles vs diamonds or circles) appear to ‘pop out’ from a model without much cognitive effort (Treisman & Gelade, 1980).

Turning to the different representational forms available in BPMN to model convergence and divergence in a process model, we assert that the explicit representational forms involving the use of Gateway constructs are more perceptually discriminable. These models involve specific graphical constructs that are visually distant form the other constructs in that they employ a different shape (a diamond shape) with an explicit graphical marker (a Plus or a Cross symbol). This would suggest that model readers could interpret this representation with more ease and accuracy. We believe these ‘pop out’ characteristics are even more important when considering large, more complex models.

## Hypothesis development

We now develop two hypotheses to investigate the effects of using Gateway constructs in process models on model readers’ ability to interpret the process model. Specifically, we discuss three expected effects on model interpretation stemming from the use of Gateway constructs in process models.

Our main contention is that both process model interpretation fidelity and efficiency (operationalised as users’ process model comprehension task performance and comprehension task completion time) will increase when Gateway constructs are presented in a process model. This is because the use of Gateway constructs in a process model activates a perceptual discriminability effect, which suggests that it will be easier for model readers to perceptually process the different components of the process model, thereby assisting the cognitive processing of the information presented. The perceptual discriminability effect can result in readers being able to more quickly identify semantically different elements of the process model, thereby increasing interpretational efficiency, and also assisting with the cognitive processing of the different model elements, which will yield increased comprehension performance.

H1: Comprehension task performance will be positively affected by the use of Gateway constructs to represent Parallel Splits and Simple Merge patterns in process models.

H2: Comprehension efficiency will be positively affected by the use of Gateway constructs to represent Parallel Splits and Simple Merge patterns in process models.

To further contextualise this proposition, we consider the complexity of the process models presented to the model reader. Prior studies (Hardgrave & Dalal, 1995; Liao & Palvia, 2000; Batra & Wishart, 2004) have shown that models with more, or more interconnected, model elements lead to an increase in the complexity of the model. More complex models, in turn, place heavier demands on the working memory of the model reader, which leads to an increase in the cognitive load (Chandler & Sweller, 1991), thereby leading to lower comprehension performance and efficiency (Reijers & Mendling, 2011).

The effects of model complexity are two-fold. More elements in a model and multiple points of control flow convergence and divergence increase the number of, and relationships between, semantic components of the process model that have to be perceptually processed and cognitively processed. Due to the limitations of the working memory of humans in terms of capacity (around seven elements, see Miller, 1956) and duration (Lohse, 1997), we can thus expect that model complexity will reduce both representational fidelity and efficiency, that is, participants will perform worse in comprehension tasks, and will take more time to perform comprehension tasks.

Model interpretation occurs in two stages (Newell & Simon, 1972), these being perceptual processing (seeing) and cognitive processing (understanding). During perceptual processing, computational offloading effects can occur that can aid the subsequent cognitive processing. Model elements that can be perceptually discriminated reduce the processing burden of the cognitive system because the parsing of model elements to different semantic components is performed by the perceptual sensors (Treisman & Gelade, 1980). Several studies suggest that perceptual processing largely explains differences in the effectiveness of the subsequent cognitive processes (Larkin & Simon, 1987; Petre, 1995).

These considerations suggest that the perceptual discriminability effect of an explicit visual syntax of Gateway constructs will be stronger when model complexity is increased. Previous studies have found that perceptual discriminability is a key requirement for novices (such as the subjects used in our study) much more so than for experts because experts are able to make much finer perceptual distinctions, and also have previous conceptual knowledge stored in their long-term memory, which they can activate in the interpretation of a model (Kosslyn, 1985; Britton & Jones, 1999). Perceptual discriminability is, therefore, key to a novice’s ability to interpret process models, especially in complex modeling scenarios. Model complexity affects novices because they need to consciously maintain the meanings of the graphical constructs in their working memory (Moody, 2009). When perceptual discrimination of all the constructs in a complex process model is not aided by the visual syntax (as in the case of an implicit representation for control flow divergence and convergence), cognitive overload ensues due to the limited capacity of the working memory, leading to rapidly decreasing comprehension (Miller, 1956). Therefore, we expect that, in the complex process models with multiple points of convergence and divergence, the increased perceptual discriminability of models through Gateway constructs will strengthen their positive effect on interpretational fidelity as well as efficiency. Formally, we state:

H3: The positive visual discriminability effects of Gateway constructs for describing Parallel Split and Simple Merge patterns on process model interpretational fidelity will be increased in more complex models.

H4: The positive visual discriminability effects of Gateway constructs for describing Parallel Split and Simple Merge patterns on process model interpretational efficiency will be increased in more complex models.

In the following, we describe design and results of an experimental study we conducted to test these hypotheses.

## Research method

## Experimental design

We used a 2\*3 mixed design with one between-group factor and one within-group factor. The between-group factor, ‘representation of convergence and divergence’ had two levels: a visually explicit representation using BPMN Gateway constructs, and a visually implicit representation using BPMN Sequence Flow constructs. The within-group factor, ‘complexity’ had three levels: low, average and high. The purpose of having three levels of model complexity was to determine, in accordance with our research hypotheses, whether the betweengroup effects were present, and different, at different levels of complexity. Further, by choosing model scenarios with different complexity, the external validity of the experiment was increased (Bodart et al, 2001).

We employed two dependent variables: performance and completion time. In line with our operationalisation of interpretational fidelity, we collected participants’ performance in three comprehension tests about the control flow logic of each modeled process. To measure interpretational efficiency, we collected the time taken to complete the comprehension tests, similar to Jarvenpaa & Machesky (1989); Gemino & Wand (2005); Recker & Dreiling (2011).

## Participants

To estimate a required sample size, a power analysis was conducted using the G\*Power 3 software (Faul et al, 2007). Given the parameters of the experimental design as set out above, and expecting desired effect sizes of f(U)40.40 with type-1 error probability of ao0.05, a sample size of N ¼ 56 was required to reach sufficient statistical power (f40.95).

We recruited 98 Information Systems students for voluntary participation. Student populations have been argued to be adequate proxies for novice analysts (e.g., Burton-Jones & Meso, 2008). Also, results from model comprehension tasks can be confounded by participants that are able to bring to bear significant levels of prior knowledge (Siau & Loo, 2006).

All students had previously completed about 3 months training in the process modeling grammar used in the experiment – BPMN – including training about different expression forms for process convergence and divergence. Participants were randomly assigned to treatment groups. Participation incentives were offered upfront and included access to a copy of the summarised study results and a \$100 store voucher to incentivise performance. The test was monitored to ensure that individuals completed the test independently.

## Materials and procedures

For our study, we implemented an online experimentation system. The appendix includes all of the experimental material used. We briefly describe important elements in the experiment below.

After collecting basic demographics, participants were asked about their self-reported knowledge of the BPMN grammar used in the study. To that end, we adopted the validated three-item grammar familiarity scale from Recker (2010). Next, we asked participants 10 true/false questions to establish their knowledge of fundamental aspects of control flow logic in process modeling. These questions concern grammatical rules of process-model logic, derived from fundamental work in this area (Kiepuszewski et al, 2003) and have been validated and used in Reijers et al (2011a); Reijers & Mendling (2011); Reijers et al (2011b); Mendling et al (2012b). These questions, notably, are grammar-independent, and address the important control flow criteria reachability (Verbeek et al, 2007), deadlocks (Puhlmann & Weske, 2006), liveness (Kindler & van der Aalst, 1999) and option to complete (Van der Aalst, 1998).

After the pre-test, each participant was presented with three models (as shown in the appendix), either containing visually explicit representation forms with Gateway constructs for process convergence and/or divergence, or visually implicit representation forms without Gateway constructs. The three models varied in levels of complexity (from low to average and high). We used an automatic randomisation mechanism, which ensured that participants received alternatively a visually explicit representation form and a visually implicit representation form. The randomisation mechanism also shuffled the order of the models in terms of complexity.

As shown in the appendix, the three models given to the students contained only events and activities with no domain semantics (i.e., they had abstract names such as task ‘A’ or task ‘B’). This was done to eliminate potential response bias stemming from the use of concrete Activity labels (Mendling et al, 2012b). Given that our study concerned comprehension of control flow logic only, we deemed it unnecessary to select process models about any particular industry domain (e.g., health, banking, insurance etc.), which would have confounded the results if participants had some levels of knowledge of these domains.

To manipulate the within-groups factor complexity, we took the following steps. First, we selected appropriate complexity metrics based on the set of metrics defined by Mendling (2008). The most important classes of metrics apply to the size of the models (most notably, arcs and nodes), and the connections within the models (most notably average connector degree) (Mendling et al, 2012a). Next, we defined three levels of complexity, viz., low, average and high. To that end, we computed the average complexity of process models found in industry practice. We considered the data reported by Kunze et al (2011), which represents a collection of BPMN process models from industry practice that is shared in an academic initiative to benefit research and education on process modeling. The collection comprises over 1400 process models and can thus be considered a representative collection of process models. Table 1 summarizes the average complexity of process models in this collection and also shows the metrics for the three models used in the experiments.

On the basis of the data displayed in Table 1, we defined an ‘average complexity’ model in our experiment as one that is roughly equivalent in complexity to the mean complexity of the models found in Kunze et al (2011). A ‘low complexity’ model was defined as one that is roughly half in complexity when compared to the industry collection. That is, our small model contained 10 arcs as compared to 17.7 arcs, and contained 7 nodes as compared to 12.2 nodes (which equals to 56% and 57% of the size of an average model). To examine our treatments in very large models, we defined a ‘high complexity’ as one that is roughly four times as complex as the average model in industry practice (viz., 61 arcs as compared to 17.7 arcs, and 50 nodes as compared to 12.2 nodes). Note that the connection complexity of our experimental models was equal and roughly equivalent to the average connection complexity of process models in industry (average connector degree of 3 vs 3.27). We have identical connection complexity between all models because our interest was in examining the way that divergence and convergence scenarios are articulated in process models. Divergence and convergence scenarios of varying complexity would have masked any effects stemming from the visual syntax representation.

For each of the three models, participants completed four model comprehension questions. The time taken to complete the comprehension questions was automatically recorded through the online experimentation system.

The model comprehension questions were similar to those asked in the pre-test in that they queried the participants’ understanding of four fundamental aspects of the control flow logic of the models presented, viz., reachability, deadlocks, liveness and option to complete. These four aspects together form the important soundness criterion for process models, a key requisite for defining an appropriate control flow logic in a process such that the control flow logic can be unambiguously interpreted by a workflow engine (Verbeek et al, 2007). For instance, to determine knowledge about process model reachability, we asked questions such as ‘Can this process be completed while Task [X] is still waiting to be activated?’ To answer the questions, participants were required to understand the logic underlying the points of divergence and/or convergence in the model. These questions were asked for each of the models presented.

Finally, after presenting each model, we asked the participants about their ease of understanding the process model depicted. To that end, we adopted the validated four-item model of perceived ease-ofunderstanding scale from Maes & Poels (2007). We collected these data for manipulation check purposes, as reported below.

## Results

The online experiment allowed us to automatically code the responses received from the experiment. We examined the data in three steps, as described in the following.

## Manipulation checks

To ascertain whether the manipulation treatment was effective, we consider the measures taken for comprehension task scores and the time taken to complete the comprehension tasks for the three model scenarios.

Table 1 Definition of the treatment factor ‘Complexity’

<table><tr><td rowspan="2">Model</td><td colspan="2">Size complexity metric</td><td>Connection complexity metric</td></tr><tr><td>Arcs</td><td>Nodes</td><td>Average connector degree</td></tr><tr><td>Average model in industry collections as per study in (Kunze et al, 2011)</td><td>17.7</td><td>12.2</td><td>3.27</td></tr><tr><td>Low complexity model in experiment</td><td>10 (56%)</td><td>7 (57%)</td><td>3 (92%)</td></tr><tr><td>Average complexity model in experiment</td><td>17 (96%)</td><td>13 (107%)</td><td>3 (92%)</td></tr><tr><td>High complexity model in experiment</td><td>61 (345%)</td><td>50 (410%)</td><td>3 (92%)</td></tr></table>

Table 2 Descriptive statistics

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std. deviation</td><td>Min</td><td>Max</td><td>Scale</td></tr><tr><td>Self-reported knowledge of BPMN (average total factor score)</td><td>98</td><td>4.22</td><td>2.04</td><td>1</td><td>7</td><td>1–7</td></tr><tr><td>Knowledge of control flow logic</td><td>98</td><td>5.78</td><td>1.89</td><td>2</td><td>9</td><td>0–10</td></tr><tr><td>Low complexity model comprehension task score (number of correct answers)</td><td>98</td><td>3.57</td><td>0.73</td><td>1</td><td>4</td><td>0–4</td></tr><tr><td>Average complexity model comprehension task score (number of correct answers)</td><td>98</td><td>2.78</td><td>1.06</td><td>0</td><td>4</td><td>0–4</td></tr><tr><td>High complexity model comprehension task score (number of correct answers)</td><td>98</td><td>2.27</td><td>1.18</td><td>0</td><td>4</td><td>0–4</td></tr><tr><td>Low complexity model comprehension task completion time (in seconds)</td><td>88</td><td>178.70</td><td>141.00</td><td>34</td><td>787</td><td>cont.</td></tr><tr><td>Average complexity model comprehension task completion time (in seconds)</td><td>86</td><td>173.26</td><td>111.00</td><td>45</td><td>922</td><td>cont.</td></tr><tr><td>High complexity model comprehension task completion time (in seconds)</td><td>82</td><td>121.54</td><td>146.90</td><td>30</td><td>875</td><td>cont.</td></tr></table>

Comprehension task scores were measured on a scale from 0 to 4, depending on the number of correct answers. Comprehension task completion time was measured in seconds. Table 2 summarises descriptive statistics. Note that in some instances, the online experimentation system did not capture task completion time stamps appropriately, leading to a number of incomplete entries for comprehension task completion times. Specifically, 10 instances of task completion times were missing for the low complexity model comprehension task (10.2%), 12 instances for the average complexity model comprehension task (12.2%) and 16 instances for the high complexity model comprehension task (16.3%).

On the basis of the date displayed in Table 2, we performed different manipulation checks. First, we evaluated the adequacy of our within- and betweengroups treatments. T-tests of the two treatment groups for task completion task scores showed the expected directionality (higher scores for the group of participants working with models that used Gateway constructs), with the significance of the differences ranging from P ¼ 0.17 (for the low complexity model) to Po0.01 (for the high complexity model). Interestingly, the t-tests did not identify significant differences in the comprehension task completion times (P-values ranged from P ¼ 0.10 for the medium complexity model to $P { = } 0 . 7 7$ for the high complexity model), raising questions about the effects of the use of Gateway constructs on interpretational efficiency.

Second, we conducted paired t-tests to compare model comprehension task scores between the low complexity models and the average complexity models, as well as between the average complexity models and the high complexity models. These tests again showed significant differences for the pairs (P ¼ 0.00 in both pair wise comparisons), suggesting that the within-subject factor ‘complexity’ was appropriately manipulated. Significant differences were also found when comparing comprehension task completion times for the pair average vs high complexity models $( P { = } 0 . 0 1 )$ but not for the pair low vs average complexity model $( P { = } 0 . 8 5 )$ . Overall, the manipulation check results suggest that our experimental manipulations were largely successful.

Next, we examined the scales used to measure selfreported knowledge of BPMN, adopted from (Recker,

2010), and the perceived ease of understanding of the three models, which was adopted from Maes & Poels (2007). The scales achieved Cronbach’s alpha coefficients of 0.97 (self-reported BPMN knowledge) and between 0.88 and 0.93 (PEOU), indicating sufficient reliability and validity.

To identify other important variables that should be used to eliminate potential bias stemming from nonequivalency between the two treatment groups, we conducted independent samples t-tests on two control variables (i.e., self-reported BPMN knowledge, and knowledge of control flow logic). To that end, we created two binary dummy variables based on a median split of the total factor score for self-reported BPMN knowledge and the knowledge of control flow logic score. For selfreported BPMN knowledge, we did not find significant differences in model-comprehension task scores or comprehension task completion times, suggesting that the variable need not be included as an additional factor. For knowledge of control flow logic, the t-tests showed significant differences in the comprehension task scores for average complexity models $( P { = } 0 . 0 1 )$ and the high complexity models $( P { = } 0 . 0 4 )$ . No significant differences were found in comprehension task completion times. Still, the results suggest that this variable should be included as an additional covariate in our ensuing analysis, to control for any potential bias if existent.

We ran further independent samples t-tests using other demographic variables (e.g., gender, under- vs post-graduate students) to test for bias. There were no significant biases in our random assignments of participants to treatment groups, based on these variables, indicating that the participants were effectively randomised across treatments.

To examine whether participants were biased due to a preference for one of the two representation formats, we ran t-tests on the average total factor score for perceived ease of understanding between the two experimental groups. The results were nonsignificant, suggesting that participants were not biased in their perception of the complexity of any of the models used.

Next, we examined the potential bias resulting from the missing cases of task completion times. To that end, we conducted t-tests on the model comprehension task scores and the knowledge of control flow logic as a covariate on the individual samples. For all three cases of missing task completion times for the low, average and high complexity model comprehension times, we found the differences in model comprehension task scores and knowledge of control flow logic to be insignificant. P-values for the differences in model comprehension task scores were 0.31 (low complexity model comprehension score), 0.31 (average complexity model comprehension score) and 0.61 (high complexity model comprehension score). P-values for the differences in knowledge of control flow logic scores were 0.76, 0.59 and 0.95, respectively. These results indicate that bias from missing entries is not significant.

Finally, we examined guessing as a potential response strategy. We tried to minimise learning effects and experiment fatigue bias by randomising the sequence of model comprehension tasks. Yet, participants may have still relied on guessing as an answer strategy. For instance, by relying on random chance, participants would have been able to score on average half of the comprehension questions. We performed one-sample t-tests of the model comprehension task scores against the value '2' to examine this potential source of bias. The average scores (see Table 2) were in all cases significantly different from the value ‘2’ (with P-values ranging from 0.00 to 0.03). Next, we compared good performers with bad performers in terms of task completion times to examine whether good performance resulted from guessing the right answers, which would be evident from lower task completion times. We created a binary dummy variable based on a median split of the total model comprehension score for all three model cases, and conducted t-tests for each of the three task completion times on the individual samples. While well-performing participants (total comprehension task score48) were significantly faster in completing the low complexity model task $( t = 2 . 0 9 , P = 0 . 0 2 )$ . they were not significantly faster in completing the average $( t = 0 . 8 9 , P = 0 . 3 8 )$ and high complexity model tasks $( t = 1 . 3 6 , \ P = 0 . 1 8 )$ . These results suggest that good comprehension scores were comparable in terms of the time investments into the tasks. Finally, we compared whether participants that received the low complexity model comprehension task prior to a high complexity comprehension task completed their comprehension tasks faster, and vice versa, which would indicate a form of experiment fatigue in which participants seek to quickly select answers only to complete the study. Forty-six participants received a low complexity model prior to receiving the high complexity model, and 52 participants vice versa. Independent samples t-tests between the groups showed that task completion times for the low and high complexity model were not significantly different across these two groups, although an effect for the high complexity model can be noted (t ¼ 0.46, P ¼ 0.64, and t ¼ 1.70, P ¼ 0.07, respectively). Overall, we posit that response bias is minimal in our study.

## Hypotheses tests

Data associated with interpretational fidelity – measured through comprehension task scores – were analyzed using a repeated measures Analysis of Covariance (AN-COVA) test, with the between-subject factor treatment (with two levels) and the within-subject factor complexity (with three levels), and using prior control flow knowledge as a covariate. The tests were computed using IBM SPSS Statistics Version 19.0.

Mauchly’s test of sphericity was significant $( \chi ^ { 2 } = 7 . 8 7 ,$ $P { = } 0 . 0 2 )$ , suggesting the use of Greenhouse-Geisser correction for sphericity of 0.93 (Hair et al, 2010). Table 3 shows average scores across all participants (mean) and standard deviations (std. deviation) and Table 4 describes the results from the repeated measures ANCOVA test, including the degrees of freedom (df), the results from the F-test (F), the resulting significance value P (sig.) and the effect size (partial eta squared). Table 4 also report the corrected degrees of freedom associated with the model error term (error) as per reporting guidelines in Hair et al (2010).

To examine differences in interpretational efficiency – measured through comprehension task completion times scores, we repeated the data analysis, viz., we again used a repeated measures ANCOVA test, with the same independent factors treatment and complexity, and using prior control flow knowledge as a covariate. As a dependent factor we considered the comprehension task completion times scores. Again, Mauchly’s test of sphericity was significant $( \chi ^ { 2 } = \stackrel { \_ } { 9 } . 1 5 , P = 0 . 0 \stackrel { \_ } { 1 } )$ , and thus we again used a Greenhouse-Geisser correction for sphericity of 0.93 (Hair et al, 2010). Table 5 shows mean values and standard deviations and Table 6 gives the results from the repeated measures ANCOVA test.

## Discussion

## Summary of results

Our empirical study set out to test four hypotheses about the effects of representational forms for convergence/ divergence and complexity of process models on the

Table 3 Means (standard deviations) for comprehension task scores

<table><tr><td>Type</td><td>Mean</td><td>Std. deviation</td></tr><tr><td>Low complexity model</td><td>3.57</td><td>0.73</td></tr><tr><td>with use of connectors</td><td>3.77</td><td>0.51</td></tr><tr><td>without use of connectors</td><td>3.35</td><td>0.88</td></tr><tr><td>Average complexity model</td><td>2.78</td><td>1.06</td></tr><tr><td>with use of connectors</td><td>2.92</td><td>1.12</td></tr><tr><td>without use of connectors</td><td>2.61</td><td>0.98</td></tr><tr><td>High complexity model</td><td>2.27</td><td>1.18</td></tr><tr><td>with use of connectors</td><td>2.31</td><td>1.15</td></tr><tr><td>without use of connectors</td><td>2.02</td><td>1.18</td></tr></table>

Table 4 Results of the repeated-measures ANCOVA for comprehension task scores

<table><tr><td>Factor</td><td>df</td><td>F</td><td>Sig.</td><td>Partial eta squared</td></tr><tr><td colspan="5">Between-subjects</td></tr><tr><td>Treatment</td><td>1</td><td>3.78</td><td>0.05</td><td>0.03</td></tr><tr><td>Control flow knowledge [covariate]</td><td>1</td><td>9.12</td><td>0.00</td><td>0.09</td></tr><tr><td>Error</td><td>95</td><td></td><td></td><td></td></tr><tr><td colspan="5">Within-subjects</td></tr><tr><td>Complexity</td><td>1.85</td><td>22.76</td><td>0.00</td><td>0.19</td></tr><tr><td>Complexity × treatment</td><td>1.85</td><td>4.85</td><td>0.03</td><td>0.05</td></tr><tr><td>Complexity × control flow knowledge [covariate]</td><td>1.85</td><td>8.21</td><td>0.01</td><td>0.08</td></tr><tr><td>Error</td><td>175.87</td><td></td><td></td><td></td></tr></table>

Table 5 Means (standard deviations) for comprehension task completion times

<table><tr><td>Type</td><td>Mean</td><td>Std. deviation</td></tr><tr><td>Low complexity model</td><td>178.70</td><td>141.00</td></tr><tr><td>with use of connectors</td><td>150.13</td><td>98.16</td></tr><tr><td>without use of connectors</td><td>210.00</td><td>179.19</td></tr><tr><td>Average complexity model</td><td>173.26</td><td>111.00</td></tr><tr><td>with use of connectors</td><td>202.48</td><td>226.35</td></tr><tr><td>without use of connectors</td><td>145.36</td><td>118.13</td></tr><tr><td>High complexity model</td><td>121.54</td><td>146.90</td></tr><tr><td>with use of connectors</td><td>120.50</td><td>173.16</td></tr><tr><td>without use of connectors</td><td>121.54</td><td>146.90</td></tr></table>

Table 6 Results of the repeated-measures ANCOVA for comprehension task completion times

<table><tr><td>Factor</td><td>df</td><td>F</td><td>Sig.</td><td>Partial eta squared</td></tr><tr><td colspan="5">Between-subjects</td></tr><tr><td>Treatment</td><td>1</td><td>0.31</td><td>0.58</td><td>0.00</td></tr><tr><td>Control flow knowledge [covariate]</td><td>1</td><td>0.07</td><td>0.80</td><td>0.00</td></tr><tr><td>Error</td><td>77</td><td></td><td></td><td></td></tr><tr><td colspan="5">Within-subjects</td></tr><tr><td>Complexity</td><td>1.88</td><td>0.45</td><td>0.63</td><td>0.01</td></tr><tr><td>Complexity × treatment</td><td>1.88</td><td>2.47</td><td>0.09</td><td>0.03</td></tr><tr><td>Complexity × control flow knowledge [covariate]</td><td>1.88</td><td>0.19</td><td>0.81</td><td>0.00</td></tr><tr><td>Error</td><td>144.48</td><td></td><td></td><td></td></tr></table>

interpretability of differently complex models in terms of their interpretational fidelity and efficiency.

In hypothesis H1 we speculated that the use of Gateway constructs will have a significant positive effect on interpretational fidelity (measured through comprehension task scores). Table 4 shows that the treatment variable (the use vs non-use of Gateway constructs) had a consistently significant effect on the comprehension task performance (F ¼ 3.78, P ¼ 0.05). The mean comprehension task scores shown in Table 3 further show that indeed in all cases interpretational fidelity was increased when Gateway constructs were used in the model. These results support hypothesis H1.

In hypothesis H3 we then speculated that the positive effects of Gateway constructs on model interpretational fidelity increase when model complexity is increased. The data displayed in Tables 3 and 4 shows that, first, interpretational fidelity decreased significantly (F ¼ 22.76, $P { = } 0 . 0 0 )$ when model complexity was increased, from an average comprehension task score of 3.57 (low complexity model) to 2.78 (average complexity model) and 2.27 (high complexity model). Table 4 further shows that the interaction effect between model complexity and treatment was significant (F ¼ 4.85, P ¼ 0.03), showing that the treatment effect increased when model complexity was increased. These results support hypothesis H3.

In hypothesis H2 we speculated that the use of Gateway constructs will have a significant positive effect on interpretational efficiency (measured by task completion time). The data in Table 5, however, show mixed results. For low complexity models, average task completion times were lower when Gateway constructs were used in the model (mean ¼ 139.79 vs mean ¼ 188.26), but for the average complexity models, the effect was reversed (mean ¼ 180.94 vs mean ¼ 134.52). For the high complexity models, differences were virtually nonexistent (mean ¼ 111.09 vs mean ¼ 111.05). Table 6 confirms that the treatment effect was insignificant (F ¼ 0.05, P ¼ 0.95). These results are contrary to hypothesis H2.

In hypothesis H4 we speculated that the positive perceptual discriminability effects of Gateway constructs on interpretation efficiency will increase for complex models. The data in Table 5 show, however, that comprehension task completion times decreased when model complexity was increased (from mean ¼ 162.66 to 159.03 and 111.07). The differences, however, were not significant (F ¼ 0.85, P ¼ 0.43). Likewise, the interaction effect Complexity - treatment was not yielding significant differences (F ¼ 2.47, P ¼ 0.09). These results are contrary to hypothesis H4.

Finally, we note that control flow knowledge was a significant covariate for explaining comprehension task performance but not for explaining comprehension task completion times. These results are largely in line with prior studies (Mendling et al, 2012b).

## Discussion

With respect to interpretational fidelity, our results show that both our hypotheses (H1 and H3) are fully supported from the data. Specifically, we found that a visually explicit representation form chosen to express convergence and divergence has a significant positive impact on the ability of readers to interpret process models, and that these effects are getting stronger even when process models get more complex. Given that typical process models found in industry practice are actually quite complex, and sometimes may even involve up to hundreds of activities and related objects such as data and applications (Mendling et al, 2010a), this finding is significant in that it underlines the importance of perceptual, visual considerations in the design of process models that are readily and intuitively perceptible by the intended audiences. On a broader level, we believe our findings suggest that the precision of the clarity of a process specification can be positively mitigated through appropriate visual means, for example, by selecting easily distinguishable shapes for better perceptual discrimination. This finding suggests the importance of design considerations made in the process of creating a process model. Our findings indicate that great effort should be placed in the selection of graphical constructs to express important aspects of process control flows, so as to warrant understandability of the outcome of the modeling process, that is, the resulting model.

One potential interpretation of these results is that process models present a high cognitive load on the user interpreting the models. Indeed, average models contain about 17 arcs and 10 nodes, which means that the number of graphical constructs in a model exceeds the typical capacity of the working memory of an individual (Miller, 1956). Thus, we speculate that model viewers will in most cases not be able to process the model as a whole in their working memory. Therefore, model viewers might be required to approach the model comprehension task in chunks rather than a whole, as suggested by Gemino & Wand (2005). This chunking process might be aided by the structuration of the model by Gateway constructs in blocks of convergence and divergence, in turn modularising the model, which can aid interpretation. Indeed, our results suggest that in such situations, the perceptual discriminability effect of Gateway constructs appears to outweigh the increased cognitive burden stemming from the increase in model elements.

With respect to interpretational efficiency, our results are inconclusive. Our data analysis shows that neither model complexity, nor existing control flow knowledge nor the use of Gateway constructs explained differences in comprehension task completion times. One interpretation could be that efficiency increases that may be present due to a perceptual offloading of cognitive processing in that Gateway constructs that are perceptually easier (and hence faster) to distinguish may be masked by the processing requirements of all other elements in the process model. Still, this interpretation is entirely speculative and thus we note that, from an efficiency perspective, advantages in model comprehension through the use of explicit Gateway representations appear to be marginal at best. Even more so, we note that task completion times decreased when model complexity was increased (see Table 5). We performed several manipulation checks to examine whether the decrease in task completion times should be attributed to learning effects or experiment fatigue bias, but the results reported above suggest that this is not the case. Still, to examine this effect further, we ran an additional post-hoc analysis in which we compared comprehension task performance and task completion time for the high complexity model against the order in which the participants received this task (first, second or last). Table 7 gives the results from the analysis.

The data in Table 7 showed that, indeed, comprehension task performance and task completion times were affected by the order in which participants received the model task, even though across all three comprehension tasks, tasks order did not affect the result. We note that those participants that received the highly complex task first spend significantly more time on completing the task (almost 4min: 222.45s on average) and also scored better results (2.64, on average) than when the highly complex model task was given to them second or last. These results suggest that highly complex model comprehension tasks may indeed induce an experiment fatigue effect if not shown first. Given the absence of additional data, we note this result as noteworthy and requiring further examination and follow-up study.

## Limitations

Several limitations pertain to our work. We examined one convergence and divergence scenario each – Parallel Split and Simple Merge – and their representation using AND-Split and XOR-Merge connectors, primarily because the implicit vs explicit modeling styles allowed by the BPMN grammar specification pertains to these two scenarios; also, these scenarios occur frequently in practice.

Table 7 Post-hoc MANOVA on high complexity model performance and completion times

<table><tr><td>Dependent variable</td><td>Task order</td><td>N</td><td>Mean</td><td>Std. deviation</td><td>F (Sig.)</td><td>Partial eta squared</td></tr><tr><td rowspan="3">Comprehension task performance</td><td>First</td><td>22</td><td>2.64</td><td>1.26</td><td>3.27</td><td>0.08</td></tr><tr><td>Second</td><td>30</td><td>2.47</td><td>1.28</td><td>(0.04)</td><td></td></tr><tr><td>Last</td><td>30</td><td>1.87</td><td>1.20</td><td></td><td></td></tr><tr><td rowspan="3">Comprehension task completion time</td><td>First</td><td>22</td><td>225.45</td><td>249.53</td><td>9.16</td><td>0.19</td></tr><tr><td>Second</td><td>30</td><td>92.00</td><td>53.27</td><td>(0.00)</td><td></td></tr><tr><td>Last</td><td>30</td><td>74.87</td><td>31.65</td><td></td><td></td></tr></table>

Still, other convergence and divergence scenarios exist (Van der Aalst et al, 2003) and modeling grammars also offer a wider range of constructs that can be chosen in process modeling (e.g., OMG, 2011). Also, the choice of constructs is dependent on the modeling objectives as well as the characteristics of the real-world domain being modeled and thus our study could only examine one specific design choice in process modeling.

The focus on Parallel Split and Simple Merge in our experiment also limits the external validity of our findings. Most models found in practice contain other, and more complex, scenarios of convergence and divergence (for example, Parallel Split and Synchronization, or Simple Choice and Simple Merge). Such scenarios would have required explicit representations in a process model (e.g., through AND-Merge and XOR-Split connectors), which would have confounded a study of explicit vs implicit representation forms. Thus, the decision to focus only on Parallel Split and Simple Merge in our study was required to establish sufficient internal validity of the findings.

Similar to other experimental studies (e.g., Burton-Jones & Meso, 2008; Shanks et al, 2008; Mendling et al, 2010b; Parsons, 2011; Recker & Dreiling, 2011), we studied a small number (three) of model cases with varying levels of complexity. In turn, the external validity of our findings is limited by the ability of experimental designs to consider different, more varied modeling scenarios. Cross-sectional research designs could be executed to overcome this limitation. For example, future research could conduct a survey of process models in the collections reported in Kunze et al (2011) and examine the occurrence of implicit vs explicit representation forms in (a) models of more varied levels of complexity or (b) patterns other than Simple Merges or Parallel Splits.

Finally, congruent to other studies (e.g., Gemino & Wand, 2005; Burton-Jones & Meso, 2008; Recker & Dreiling, 2011) we have examined our hypotheses in a laboratory experiment with university students. While this cohort has been argued to be an approximate proxy for novice business analysts (Burton-Jones & Meso, 2008), caution should be exerted in drawing generalised conclusions about, for example, the likely performance of experienced practitioners.

## Implications

## For research

Several research directions flow from the study reported in this paper.

For research streams investigating process model understanding (e.g., Mendling et al, 2010b; Reijers & Mendling, 2011), our study adds to the current body of knowledge by examining visual design characteristics of process modeling grammars, and their effects on process modeling interpretational fidelity and efficiency. We focused on one visual design aspect, perceptual discriminability and one class of model elements, Gateway constructs. Moody (2009) describes other important visual syntax elements in modeling grammars (e.g., semiotic clarity, semantic transparency) that may further assist comprehension of process models. Also, recent studies have started to examine other visual aspects such as color highlighting (Reijers et al, 2011a). Thus, opportunities exist for fellow scholars to examine different visual design characteristics of process models, and the impact these characteristics may have on the ability of individuals to understand the models. Similarly, other research could extend our work to other classes of process model elements (e.g., activities, events or other Gateway constructs), or combinations thereof. Our work was restricted to two key control flow patterns, viz., Simple Merge and Parallel Split (Van der Aalst et al, 2003). Further, more advanced patterns have also been defined, which could be examined based on Moody’s (2009) theory, such that relevant effects can be theorised and verified empirically.

Other research could extend our approach to measuring process model interpretability. In this paper we chose to examine comprehension of process control flow logic, similar to Mendling et al (2012b). Past research suggests that comprehension is a type of surface understanding, which is different from deep understanding (Gemino & Wand, 2005). In fact, both products of understanding can be seen as two ends of a continuum. We focused on individuals’ understanding of grammatical elements and their meaning in a process model (surface understanding), which is fundamental to being able to faithfully and efficiently interpret a process model. Future work could now extend this work and examine the deep understanding and performance of individuals who use process models to solve tasks such as organisational re-design, software specification, certification and others (Recker & Dreiling, 2011).

A third stream of research may examine extensions to the design of our study. For instance, we chose to peruse models with abstract labels to avoid bias stemming from different levels of domain knowledge. A recent study showed indeed that process model comprehension is affected by the use of textual task labels (Mendling et al, 2012b). An important question to be answered is how the findings from the two studies relate to another, that is, how the visual discriminability effects related to the use of connectors would affect the comprehension of real models with meaningful task labels. A different extension to our study would be the inclusion of relevant personal factors that influence performance in model comprehension tasks. There is a range of arguments that the inclusion of attributes pertaining to the model reader would be relevant to explaining model comprehension. For instance, a study by Reijers & Mendling (2011) found that students from different university backgrounds performed significantly different in their comprehension tests. Recker & Dreiling (2011) found that work and modeling experience were important factors in being able to retain information from a process model. The work in this paper adds some yet partially inconclusive arguments to this proposition. Knowledge of control flow logic aided interpretational fidelity but not efficiency. The concept of general mental ability (Schmidt & Hunter, 2004) might be able to resolve these differences. General mental ability characterises the general intelligence, aptitude, skill levels, traits and values of an individual. Research perusing this measure has been able to demonstrate that general mental ability is a key factor explaining and predicting knowledge as well as performance in a wide variety of tasks across different occupations. On the basis of these findings, it would appear promising to use general mental abilities as a characterisation of a model reader and examine their effect in model comprehension tasks.

A fourth stream of research may extend our work on interpretational efficiency. We observed that the visual discriminability effects of construct Gateways appear not to be present in a process model, and likewise, effects from model complexity do not appear to be consistent and unequivocal. One reason might lie in our operationalisation of interpretational efficiency through task completion times. Other measures of efficiency (Mendling et al, 2012b) or the use of perceptual cognitive complexity metrics (Marcus et al, 1996) may yield different results. We also note that task order might have led to experiment fatigue for those participants that received more complex model comprehension tasks at a later stage in the experiment. Model comprehension exerts significant cognitive load on participants, and it may be that different experimental strategies are in order to balance the cognitive load of model-based problem-solving tasks more appropriately. Overall, we believe our results on interpretational efficiency are an interesting research outcome and one that deserves further attention. It may be, for instance, that model characteristics such as modularity (Reijers et al, 2011b) or user characteristics such as experience (Recker & Dreiling, 2011) could contribute to interpretational efficiency. These suggestions require further examination.

## For practice

Our research informs one important aspect of process modeling. Namely, our results clarify one important question that forms part of process modeling conventions management and guideline development: Should Gateway constructs be used in process models? Our results clearly indicate that interpretation of process models is aided when Gateway constructs are present, and thus, conventions and guidelines should be updated to incorporate and stipulate their use.

One application of these findings is in the actual practice of process modeling. This practice is informed by our study about the design choices, and implications thereof that modelers are confronted within the process of creating process models. Specifically, our results suggest that attention should be paid to visual considerations, especially in complex modeling scenarios. Our findings suggest that additional visual cues (e.g., through the introduction of varied graphical forms and shapes)

can assist the interpretation experience by the model audience, thereby increasing the usefulness of the model for all application tasks.

Our findings also inform ongoing revisions to modeling grammars, as well as the development of coaching and training material for process modeling. For grammar specification, our results show that choices made in the specification of a grammar should be based on visual design aspects as well as principles of the underlying theory of systems being modeled. Our study showed, specifically, that behavioral elements of model systems (such as the Gateways that indicate control flow in a process) should have an explicit representation in a modeling grammar. Our study has shown that seemingly simpler, implicit representations lead to lowered comprehension, which in turn may lead to low consistencies, ambiguities and thus poor decisions made on the basis of the models.

For the development of training material, existing textbooks on process modeling (e.g., Debevoise & Geneva, 2008; White & Miers, 2008; Silver, 2009) should be carefully revisited about the guidelines they offer in respect to modeling convergence and divergence scenarios. More broadly, in training environments, emphasis should be added to the use of Gateway constructs as visual mechanisms to aid modularisation of models into ‘chunks’ that are more easily interpretable by a modeling audience. For designers of modeling grammars, the recommendation would be to revisit the allowed representation forms, for example, by deleting the possibility to allow for implicit representation forms to depict control flow convergence and divergence.

Finally, our results pertaining to the role of existing control flow knowledge further attest to the importance of modeling training. In line with prior studies (e.g., Recker & Dreiling, 2011; Mendling et al, 2012b), our findings suggest that it is essential to provide formal process modeling education to staff members who will be required to use the models in their day-to-day or project activities. The recommendations by Recker & Rosemann (2009) could guide the development of an appropriate training program.

## Conclusions

Using process modeling for the analysis and design of process-aware information systems is a relevant domain in conceptual modeling and IS analysis and design overall. We contribute to this body of knowledge by extending our understanding of Gateway constructs in process models, the visual design characteristics of these constructs and their effects on process model interpretability. Importantly, in this paper we were able to provide normative advice about how models should be designed in order to allow users to faithfully interpret the models. Our work also shows that sometimes design choices built into a modeling grammar may not necessarily result in effective modeling practice as they may induce more ambiguity than required or desired. In turn, our work contributes to understanding the effective design of modeling grammars.

Overall, our work adds to the growing body of knowledge on design choices in process modeling and their outcomes, and thus adds to the effort of supporting more successful process modeling for the analysis and design of process-aware information systems.

## About the author

Jan Recker is Full Professor and Woolworths Chair of Retail Innovation at Queensland University of Technology in Brisbane, Australia. Recker’s research interests focus on the use of process design in organizational practice, business transformations and organizational innovation. He has authored and edited several books, and co-authored over 100 academic papers in journals and conferences. His research has appeared, among others, in the MIS Quarterly, Journal of the Association for

## References

BATRA D and WISHART NA (2004) Comparing a rule-based approach with a pattern-based approach at different levels of complexity of conceptual data modelling tasks. International Journal of Human-Computer Studies 61(4), 397–419.

B F, P A, S M and W R (2001) Should optional properties be used in conceptual modelling? A theory and three empirical tests. Information Systems Research 12(4), 384–405.

BPMI.ORG and OMG (2006) Business Process Modeling Notation Specification. Final Adopted Specification. Object Management Group, [WWW document] http://www.bpmn.org/Documents/OMG\_Final\_ Adopted\_BPMN\_1-0\_Spec\_06-02-11.pdf, (accessed 20 February 2012).

BRITTON C and JONES S (1999) The untrained eye: how languages for software specification support understanding in untrained users. Human-Computer Interaction 14(1), 191–244.

BURTON-JONES A and MESO P (2008) The effects of decomposition quality and multiple forms of information on novices’ understanding of a domain from a conceptual model. Journal of the Association for Information Systems 9(12), 784–802.

BURTON-JONES A, WAND Y and WEBER R (2009) Guidelines for empirical evaluations of conceptual modeling grammars. Journal of the Association for Information Systems 10(6). 495–532.

CHANDLER P and SWELLER J (1991) Cognitive load theory and the format of instruction. Cognition and Instruction 8(4), 293–332.

CHENG PC-H, MARRIOTT K and SHIMOJIMA A (2004) Why diagrams are (sometimes) six times easier than words: benefits beyond locational indexing. In Diagrammatic Representation and Inference (BLACKWELL AF, Ed), pp 167–174, Springer, Cambridge, England.

DAVIES I, GREEN P, ROSEMANN M, INDULSKA M and GALLO S (2006) How do practitioners use conceptual modeling in practice? Data & Knowledge Engineering 58(3), 358–380.

DEBEVOISE T and GENEVA R (2008) The Microguide to Process Modeling in BPMN. BookSurge Publishing, Charleston, SC.

DUMAS M, VAN DER AALST WMP and TER HOFSTEDE AHM (Eds) (2005) Process Aware Information Systems: Bridging People and Software through Process Technology. John Wiley & Sons, Hoboken, NJ.

F F, E E, L A-G and A B (2007) G\*Power 3: a flexible statistical power analysis for the social, behavioral, and biomedica sciences. Behavior Research Methods 39(2), 175–191.

G A and W Y (2004) A framework for empirical evaluation of conceptual modeling techniques. Requirements Engineering 9(4), 248-260

## Acknowledgements

This research has been supported by a grant from the Australian Research Council (ARC DE120100776) and by a Fellowship from the Alexander-von-Humboldt Foundation.

Information Systems, Information Systems, European Journal of Information Systems, Information & Management, Scandinavian Journal of Information Systems and others. He is Associate Editor for Communications of the AIS, and a Senior Editor for the Journal of IT Theory and Application. He holds a Ph.D. in Information Systems from Queensland University of Technology and an MS in Information Systems from the University of Muenster, Germany.

GEMINO A and WAND Y (2005) Complexity and clarity in conceptua modeling: comparison of mandatory and optional properties. Data & Knowledge Engineering 55(3), 301–326.

HAIR JF, BLACK WC, BABIN BJ and ANDERSON RE (2010) Multivariate Data Analysis. Prentice Hall, Upper Saddle River, NJ.

HARDGRAVE BC and DALAL NP (1995) Comparing object-oriented and extended-entity-relationship data models. Journal of Database Management 6(3), 15–21.

HITCHMAN S (2002) The details of conceptual modelling notations are important – a comparison of relationship normative language. Communications of the Association for Information Systems 9(10), 167–179.

IRANI P, TINGLEY M and WARE C (2001) Using perceptual syntax to enhance semantic content in diagrams. IEEE Computer Graphics and Applications 21(5), 76–85.

JARVENPAA SL and MACHESKY JJ (1989) Data analysis and learning: an experimental study of data modeling tools. International Journal of Man-Machine Studies 31(4). 367–391.

KIEPUSZEWSKI B, TER HOFSTEDE AHM and VAN DER AALST WMP (2003)Fundamentals of control flow in workflows. Acta Informatica 39(3),143-209

KINDLER E (2005) On the semantics of EPCs: resolving the vicious circle. Data & Knowledge Engineering 56(1), 23–40.

KINDLER E and VAN DER AALST WMP (1999) Liveness, fairness, and recurrence. Information Processing Letters 70(6), 269–274.

KOCK N, VERVILLE J, DANESH-PAJOU A and DELUCA D (2009) Communication flow orientation in business process modeling and its effect on redesign success: results from a field study. Decision Support Systems 46(2), 562–575.

KOSSLYN SM (1985) Graphics and human information processing. Journal of the American Statistical Association 80(391). 499–512.

K M, L A, W M and W M (2011) Towards understanding process modeling – the case of the BPM academic initiative. In Business Process Model and Notation: 3rd International Workshop (DIJKMAN RM, HOFSTETTER J and KOEHLER J, Eds), pp 44–58, Springer, Lucerne, Switzerland.

L JH and S HA (1987) Why a diagram is (sometimes) worth ten thousand words. Cognitive Science 11(1), 65–100.

LIAO C and PALVIA PC (2000) The impact of data models and task complexity on end-user performance: an experimental investigation. International lournal of Human-Computer Studies 52(5). 831–845.

LOHSE GL (1997) The role of working memory on graphical information processing. Behaviour and Information Technology 16(6), 297–308.

MAES A and POELS G (2007) Evaluating quality of conceptual modelling scripts based on user perceptions. Data & Knowledge Engineering 63(3), 769–792.

MARCUS N, COOPER M and SWELLER J (1996) Understanding instructions. Journal of Educational Psychology 88(1), 49–63.

MENDLING J (2008) Metrics for Process Models: Empirical Foundations of Verification, Error Prediction and Guidelines for Correctness. Springer, Berlin, Germany.

MENDLING J, REIJERS H and VAN DER AALST WMP (2010a) Seven process modeling guidelines (7PMG). Information and Software Technology 52(2), 127–136.

MENDLING J, REIJERS HA and RECKER J (2010b) Activity labeling in process modeling: empirical insights and recommendations. Information Systems 35(4), 467–482.

MENDLING J, SANCHEZ-GONZALEZ L, GARCIA F and LA ROSA M (2012a) Thresholds for error probability measures of business process models. Journal of Systems and Software 85(5), 1188–1197.

MENDLING J, STREMBECK M and RECKER J (2012b) Factors of process model comprehension – findings from a series of experiments. Decision Support Systems 53(1), 195–206.

MILLER GA (1956) The magical number seven, plus or minus two: some limits on our capacity for processing information. Psychological Review 63(2), 81–97.

MOODY DL (2009) The ‘Physics’ of notations: toward a scientific basis for constructing visual notations in software engineering. IEEE Transactions on Software Engineering 35(6), 756–779.

NEWELL A and SIMON HA (1972) Human Problem Solving. Prentice-Hall, Englewood Cliffs, NJ.

OMG (2011) Business Process Model and Notation (BPMN) – Version 2.0. Object Management Group, [WWW document] http://www.omg.org/ spec/BPMN/2.0/, (accessed 17 March 2011).

PARSONS J (2011) An experimental study of the effects of representing property precedence on the comprehension of conceptual schemas. Journal of the Association for Information Systems 12(6), 401–422.

PETRE M (1995) Why looking isn’t always seeing: readership skills and graphical programming. Communications of the ACM 38(6), 33–44.

PUHLMANN F and WESKE M (2006) Investigations on soundness regarding lazy activities. In Business Process Management – BPM 2006 (DUSTDAR S, FIADEIRO JL and SHETH AP, Eds), pp 145–160, Springer, Vienna, Austria.

PURCHASE HC, WELLAND R, MCGILL M and COLPOYS L (2004) Comprehension of diagram syntax: an empirical study of entity relationship notations. International Journal of Human-Computer Studies 61(2), 187–203.

RECKER J (2010) Continued use of process modeling grammars: the impact of individual difference factors. European Journal of Information Systems 19(1), 76–92.

R J and D A (2011) The effects of content presentation format and user characteristics on novice developers’ understanding of process models. Communications of the Association for Information Systems 28(6), 65–84.

RECKER J and ROSEMANN M (2009) Teaching business process modeling – experiences and recommendations. Communications of the Association for Information Systems 25(32), 379–394.

RECKER J, ROSEMANN M, INDULSKA M and GREEN P (2009) Business process modeling: a comparative analysis. Journal of the Association for Information Systems 10(4), 333–363.

REIJERS HA, FREYTAG T, MENDLING J and ECKLEDER A (2011a) Syntax highlighting in business process models. Decision Support Systems 51(3), 339–349.

REIJERS HA and MENDLING J (2011) A study into the factors that influence the understandability of business process models. IEEE Transactions on Systems Man & Cybernetics, Part A 41(3), 449–462.

REIJERS HA, MENDLING J and DIJKMAN RM (2011b) Human and automatic modularizations of process models to enhance their comprehension. Information Systems 36(5), 881–897.

SCHEER A-W (2000) ARIS – Business Process Modeling. Springer, Berlin, Germany.

SCHMIDT FL and HUNTER J (2004) General mental ability in the world of work: occupational attainment and job performance. Journal of Personality and Social Psychology 86(1), 162–173.

SHANKS G, TANSLEY E, NUREDINI J, TOBIN D and WEBER R (2008) Representing part – whole relations in conceptual modeling: an empirical evaluation. MIS Quarterly 32(3), 553–573.

SIAU K (2004) Informational and computational equivalence in comparing information modeling methods. Journal of Database Management 15(1), 73–86.

S K and L P-P (2006) Identifying difficulties in learning UML. Information Systems Management 23(3), 43–51.

SILVER B (2009) BPMN Method and Style: A Levels-based Methodology for BPM Process Modeling and Improvement Using BPMN 2.0. Cody-Cassidy Press, Aptos, CA.

SOFFER P, KANER M and WAND Y (2010) Assigning ontological meaning to workflow nets. Journal of Database Management 21(3), 1–35.

TREISMAN AM and GELADE G (1980) A feature-integration theory of attention. Cognitive Psychology 12(1), 97–136.

VAN DER AALST WMP (1998) The application of petri nets to workflow management. The Journal of Circuits, Systems and Computers 8(1), 21–66.

VAN DER AALST WMP and TER HOFSTEDE AHM (2005) YAWL: yet another workflow language. Information Systems 30(4), 245–275.

V D A WMP, T H AHM, K B and B AP (2003) Workflow patterns. Distributed and Parallel Databases 14(1), 5–51.

VERBEEK HMV, VAN DER AALST WMP and TER HOFSTEDE AHM (2007) Verifying workflows with cancellation regions and OR-joins: an approach based on relaxed soundness and invariants. The Computer Journal 50(3), 294–314.

WESKE M (2007) Business Process Management: Concepts, Languages, Architectures. Springer, Berlin, Germany.

W SA and M D (2008) BPMN Modeling and Reference Guide. Future Strategies, Lighthouse Point, FL.

WINN WD (1990) Encoding and retrieval of information in maps and diagrams. IEEE Transactions on Professional Communication 33(3), 103–107.

W WD (1993) An account of how readers search for information in diagrams. Contemporary Educational Psychology 18(2), 162–185.

## Appendix

## Experimental material used

## 1. Demographics Gender (Male/Female)

Level of study (Undergraduate/Postgraduate)

Completion of Process Modeling Course at University (Yes/No)

Self-reported knowledge of the BPMN grammar (7-point scale from ‘Strongly disagree’ to ‘Strongly agree’), adapted from (Recker, 2010)

 Overall, I am very familiar with BPMN.

 I feel very confident in understanding process models created with BPMN.

 I feel very competent in using BPMN for process modeling.

Knowledge of Control Flow Logic in Process Models (True/ False), adapted from (Mendling et al, 2012b)

Please answer the following true/false questions about process modeling (correct answer in brackets):

1. After exclusive choices, at most one alternative path is executed (false).

2. Exclusive choices can be used to model repetition (true).

3. Synchronisation means that two activities are executed at the same time (false).

4. An inclusive OR can activate concurrent paths (true).

5. If two activities are concurrent, they have to be executed at the same time (false).

6. If an Activity is modeled to be part of a loop, it has to be executed at least once (false).

7. Having an AND-Split at the exit of a loop can lead to non-termination (true).

8. A deadlock is the result of an inappropriate combination of splits and joins (true).

9. Processes without loops cannot deadlock (false).

10. Both an AND-Join and an XOR-Join can be used as a correct counterpart of an OR-Split (false).

2. Treatment material Low Complexity Model (Explicit/ Implicit)

![](/api/attachments/4Y5NT8ZS/fulltext/images/ebe7030714fe6ed1d25f97c45568a82dc9e8ea223b51c0cfa043cf9dfafbd399.jpg)

![](/api/attachments/4Y5NT8ZS/fulltext/images/202fcb43ddf71d796e7873ae783651d12f406d993980b99e8ae0f226c5f96164.jpg)

Comprehension Questions

Please answer the following true/false questions about the model (correct answer in brackets):

 Task E can never be executed. (false)

 This process can be completed while Task B is still waiting to be activated. (true)

 Tasks D and E can be completed concurrently. (true)

 This model contains a deadlock. (false)

Ease of Understanding Questions (7-point scale from ‘Strongly disagree’ to ‘Strongly agree’), adapted from (Maes & Poels, 2007)

 It was easy for me to understand what the process model was trying to depict.

 Using the process model was frustrating.

 Overall, the process model was easy to use.

 Learning how to read the process model was easy.

Average Complexity Model (Explicit/Implicit)

![](/api/attachments/4Y5NT8ZS/fulltext/images/26c277c46165ef7764baa48a373176fcaa99ee8b0deeacf0a082ac3cc1af4b3d.jpg)

![](/api/attachments/4Y5NT8ZS/fulltext/images/3074eb57c572d02325adf4403d47d266df5cdfd369879be3acbd3a2a4dfdc04e.jpg)

Comprehension Questions

Please answer the following true/false questions about the model (correct answer in brackets):

 Task F can never be executed. (false)

 Task G can be executed while Task D is still waiting to be activated. (true)

 Tasks G and H can never be completed concurrently. (false)

 This model contains a deadlock. (false)

Ease of Understanding Questions (7-point scale from ‘Strongly disagree’ to ‘Strongly agree’), adapted from (Maes & Poels, 2007)

 It was easy for me to understand what the process model was trying to depict.

 Using the process model was frustrating.

 Overall, the process model was easy to use.

 Learning how to read the process model was easy.

High Complexity Model (Explicit/Implicit)

![](/api/attachments/4Y5NT8ZS/fulltext/images/77ee1f121be424f336cc53973dd792786d22d6ba2abde7593acd1bbef3d1b891.jpg)

Comprehension Questions

Please answer the following true/false questions about the model (correct answer in brackets):

 Task X can be activated while Task M is still waiting to be activated (true)

 Tasks H and Z can never be completed concurrently. (false)

 This process can be completed while Task M is still waiting to be activated. (true)

##  Tasks E, O and DD will always be executed. (false)

Ease of Understanding Questions (7-point scale from ‘Strongly disagree’ to ‘Strongly agree’), adapted from Maes & Poels (2007).

 It was easy for me to understand what the process model was trying to depict.

 Using the process model was frustrating.

 Overall, the process model was easy to use.

 Learning how to read the process model was easy.
