---
otero_id: 10662
otero_key: "NE4HX2PG"
title: "How quickly do we learn conceptual models?"
authors: "Palash Bera; Geert Poels"
year: "2019"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2019.1673972"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How quickly do we learn conceptual models?

Palash Bera & Geert Poels

To cite this article: Palash Bera & Geert Poels (2019): How quickly do we learn conceptual models?, European Journal of Information Systems, DOI: 10.1080/0960085X.2019.1673972

To link to this article: https://doi.org/10.1080/0960085X.2019.1673972

![](/api/attachments/NE4HX2PG/fulltext/images/1c913428d49d0d8f03ea6b3845ae21621b10392d350e3959a989571ccaeeb8a0.jpg)

Published online: 17 Oct 2019.

![](/api/attachments/NE4HX2PG/fulltext/images/bd5b19c508983c559c7e9f4872aa00cb420975509f6809673ea8e3c81db40c82.jpg)

Submit your article to this journal

![](/api/attachments/NE4HX2PG/fulltext/images/d23e4b827aebe222c564fba0e9ad76a5e279ed8e3ace3d7b6d004f7288794750.jpg)

Article views: 2

![](/api/attachments/NE4HX2PG/fulltext/images/a468cef6361e6071be4ce2e59d63fefff4a2ecb9256b40723544fd05fd0426d0.jpg)

View related articles

![](/api/attachments/NE4HX2PG/fulltext/images/36218ccf914386c8f6bcdc4b450d29e60aa65e8efe1bbc1efd654cedd35a2975.jpg)

View Crossmark data

EMPIRICAL RESEARCH

Check for updates

# How quickly do we learn conceptual models?

Palash Bera<sup>a</sup> and Geert Poels <sup>b</sup>

<sup>a</sup>John Cook School of Business, Saint Louis University, Saint Louis, USA; <sup>b</sup>Faculty of Economics and Business Administration, Ghent University, Ghent, Belgium

## ABSTRACT

In organisations, conceptual models are used for understanding domain concepts. Learning the domain from models is crucial for the analysis and design of information systems that are intended to support the domain. Past research has proposed theories to structure conceptual models in order to improve learning. It has, however, never been investigated how quickly domain knowledge is acquired when using theory-guided conceptual models. Based on theoretical arguments, we hypothesise that theory-guided conceptual models expedite the initial stages of learning. Using the REA ontology pattern as an example of theoretical guidance, we show in a laboratory experiment how an eye-tracking procedure can be used to investigate the e<sup>f</sup>ect of using theory-guided models on the speed of learning. Whereas our experiment shows positive e<sup>f</sup>ects on both outcome and speed of learning in the initial stages of learning, the real contribution of our paper is methodological, i.e. an eye-tracking procedure to observe the process of learning from conceptual models.

ARTICLE HISTORY Received 14 February 2017 Accepted 18 June 2019

ACCEPTING EDTOR Prof. Par Agerfalk

ASSOCIATE EDITOR Prof. Fredrik Karlsson

KEYWORDS REA ontology pattern; conceptual model; domain knowledge; learning; eyetracking

## 1. Introduction

A conceptual model describes a domain conceptualisation that represents an abstraction of the domain for some purpose. In science, conceptual models are used to guide research by providing a visual representation of constructs or variables and their theorised relationships. In information systems engineering, the main purpose of conceptual models is sharing the domain knowledge that is required for systems analysis and design (Ho<sup>f</sup>er, Prescott, & McFadden, 2008). Conceptual models created using techniques and languages like Entity Relationship Modelling (ERM), Uni<sup>fi</sup>ed Modelling Language (UML), Event-Driven Process Chains (EPC), and Business Process Model and Notation (BPMN), are developed by analysts to foster shared domain understanding with the other stakeholders in systems development (Maass, Storey, & Kowatsch, 2011). These other stakeholders (e.g. future system users, system architects, project leaders) acquire domain knowledge by comprehending and interpreting the models developed by the analysts. In other words, they learn the domain from the model.

To improve learning from conceptual models, theories have been proposed that o<sup>f</sup>er guidance on how to structure conceptual models. By structuring a conceptual model, we mean deciding how to use a modelling language or technique to represent domain concepts, relationships and constraints (i.e. choice of abstract syntax re<sup>fl</sup>ecting particular semantics) and/or how to present the model (i.e. choice of concrete syntax and, in case of a diagrammatic representation, choice of layout).

Predictions of improved learning using theoryguided conceptual models have been empirically demonstrated and explained using various theories of cognition (Bera, Burton-Jones, & Wand, 2011). Empirical studies have measured the acquisition of domain knowledge from using models by measuring model users’ understanding of the model. Such measurement typically involves evaluating users’ answers to semantic comprehension questions (i.e. assessing factual domain knowledge) (Khatri, Vessey, Ramesh, Clay, & Park, 2006). Whereas the focus of most of the research on theory-guided conceptual models was on the outcome of learning, in this paper we focus on the speed of learning. We de<sup>fi</sup>ne speed of learning as the rate at which domain knowledge is acquired.

A focus on speed of learning requires approaching learning from conceptual models as a process. A few studies have attempted to gain insights into the process of learning from models by means of perceptionbased measures requiring subjects to express their perception of the model’s ease (or di<sup>fi</sup>culty) of understanding or usefulness (Burton-Jones & Meso, 2008; Figl, Mendling, & Strembeck, 2013). Other studies have approximated speed of learning as the time taken to perform understanding-related tasks (Bodart, Patel, Sim, & Weber, 2001; Mendling, Strembeck, & Recker, 2012). Both types of measurement are taken after having users interacting with models and as such they provide only indirect insights into the process of learning.

As the speed of learning from a conceptual model has not been adequately measured before, we propose a way of observing and measuring the process of learning using an eye-tracking procedure. We further propose how to evaluate the e<sup>f</sup>ect on speed of learning from models when theory-guided conceptual models are used. Hence, the research questions addressed in this paper are:

(1) How to measure the speed of learning from conceptual models using eye-tracking?

(2) How to use eye-tracking to investigate whether conceptual models structured in a particular way expedite learning?

To demonstrate our proposed eye-tracking procedure, we conduct an empirical study using the REA ontology pattern (Dunn, Cherrington, & Hollander, 2005) as an example of theoretical guideline for structuring a conceptual model. Poels, Maes, Gailly, and Paemeleire (2011) showed that users of Entity Relationship Diagrams (ERDs) constructed using the REA ontology pattern acquire a more accurate understanding of policies governing business processes. In a follow-up study, Poels (2011) showed that such ERDs were also perceived as easier to interpret by users that are novices in modelling. However, these studies did not investigate the speed of learning from the models. Hence it is known whether learning from such models is also faster.

We emphasise that the intended contribution of our paper is the proposed procedure to observe and measure the process of learning. Although we develop theoretical arguments for e<sup>f</sup>ects on speed of learning from theory-guided conceptual models, we do not generalise the results of our empirical study on structuring models using the REA ontology pattern to other types of theory-guided models.

The paper is structured as follows: In the Background section, we introduce our terminology of “good representation” and “poor representation” models, depending on whether theoretical guidance for structuring conceptual models was used. We also present our theory-based hypotheses for the e<sup>f</sup>ects of “good representation” models on the outcome and speed of learning. Further, we review how past research has measured learning from conceptual models. Then in the Eye Tracking section, we present our proposed procedure for observing and measuring the process of learning from conceptual models. This procedure is demonstrated in the Empirical Study section by comparing learning from models that follow or do not follow the REA ontology pattern. The second to last section discusses our <sup>fi</sup>ndings and their implications for research and practice. The <sup>fi</sup>nal section is the conclusion.

## 2. Background

## 2.1. Good and poor representation models

Several theories have been proposed that o<sup>f</sup>er guidance for structuring conceptual models. Examples of such theories include the theory of ontological expressiveness (Wand & Weber, 1993), the Uni<sup>fi</sup>ed Foundational Ontology (Guizzardi, 2005), and the Physics of Notations (Moody, 2009). For instance, the theory of ontological expressiveness states that models are ontologically unclear if they contain instances of modelling language constructs that represent optional properties (Wand & Weber, 2017). Based on the theory, a prediction can be made that a model, for example an ERD, that shows optional attributes and relationships (i.e. using zero cardinalities) su<sup>f</sup>ers from ontological clarity, hence will impede understanding of the domain represented through the model.

To explain in general why structuring of conceptual models a<sup>f</sup>ects learning, we refer to Cognitive Fit Theory (CFT) (Shaft & Vessey, 2006; Vessey, 1991). Figure 1 shows how we apply this theory to theorybased structuring of conceptual models.

![](/api/attachments/NE4HX2PG/fulltext/images/994999082dccabffe240974cea67ea1e59cec2af00b866f23db9c6bd717056ab.jpg)  
E<sup>f</sup>ect of theory-based structuring of conceptual models in terms of cognitive <sup>fi</sup>t.

To perform a task requiring human information processing, humans create a mental representation of the task solution in their working memory (i.e. mental representation of Task Solution boxes in Figure 1) (Vessey, 1991). Problem-solving involves two distinct activities that need to be performed simultaneously to perform the task well – one related to the understanding of the task (i.e. what information is required for task resolution?) and the other related to the understanding of the application domain to which the task is performed (i.e. where and how to get the information required for task resolution?) (Vessey, 1991). CFT suggests that a good mental representation of the task solution is created if the mental representation of the task (i.e. mental representation of the Task boxes in Figure 1) and mental representation of the application domain (i.e. mental representation of the Application Domain boxes in Figure 1) emphasise the same type of information (i.e. a situation of cognitive fit) (Vessey, 1991). Cognitive <sup>fi</sup>t is highly relevant as the better the mental representation of the task solution, the better the task performance.

CFT has been used extensively in empirical studies on conceptual modelling (Bera, Burton-Jones, & Wand, 2014; Bera & Evermann, 2014; Bodart et al., 2001; Burton-Jones & Meso, 2008; Evermann & Wand, 2006; Gemino & Wand, 2005; Shanks, Tansley, & Weber, 2004). Tasks considered in such studies relate to understanding a domain as modelled (i.e. learning a domain from a model). For instance, a task may involve using the conceptual model to verify the truth about some statement about the domain. In this context, understanding which information is required to evaluate the statement and retrieving that information from the model are two activities to be performed for task resolution. For a task that requires domain understanding, cognitive <sup>fi</sup>t depends on the quality of the mental representation of the application domain (i.e. whether the information required for task resolution can be easily and accurately inferred from the conceptual model). If model users experience di<sup>fi</sup>culties in comprehending and interpreting a conceptual model, then they face a situation known as cognitive overload (Mayer & Moreno, 2003). In this situation, individuals are faced with a task that demands more from their cognitive resources (such as working memory) than they can sustain.

The focus of much of the empirical research in conceptual modelling is to demonstrate that a particular structuring of conceptual models eases model comprehension and interpretation such that a good mental representation of the application domain is created (i.e. the Good mental representation of the Application Domain box in the left-hand side of Figure 1), resulting in cognitive <sup>fi</sup>t and better task performance than when using models structured di<sup>f</sup>erently (i.e., the Poor mental representation of the Application Domain box in the right-hand side of Figure 1) (e.g. Bera et al., 2014). In the remainder of this paper we refer to such theory-guided models as good representation models and contrast them with poor representation models, which are not structured following a particular theory-based guideline.

## 2.2. Hypothesis development

Past studies (e.g. Khatri et al. (2006) and Burton-Jones, Wand, and Weber (2009)) suggest that good representation models result in better performance in tasks related to domain understanding compared to bad representation models. Theory-guided structuring of conceptual models thus a<sup>f</sup>ects the outcome of learning, i.e. the extent to which domain knowledge was acquired. Past studies have, however, not approached learning from conceptual models as a process. What these studies have in common is that the e<sup>f</sup>ect of using a good representation model on domain understanding has been measured only after the exposure to the model, i.e. after the tasks have been performed. This means that a dynamic view of domain knowledge acquisition by means of conceptual models is absent in the past research.

Learning is, however, not instantaneous. In cognitive psychology research, it has been demonstrated that items are better learned when they are repeated sequentially with time intervals (Pavlik & Anderson, 2005) rather than presented all at once (Challis, 1993). This phenomenon is called the spacing efect. The theory of encoding variability (Young & Bellezza, 1982) is often used to explain why learning is enhanced when spacing is provided. As per this theory, the more spaced two items are, the more likely it is that they will be encoded in learners’ mind di<sup>f</sup>erently and this encoding variability facilitates in providing more context and thus provides more retrieval cues (Richardson, 1973). Hence, referring to the CFT conceptual framework, when users get engaging tasks that require them to be exposed repeatedly to a model, then their mental representation of the application domain gets a<sup>f</sup>ected (i.e. the spacing e<sup>f</sup>ect) and so does the mental representation required for task solution, i.e. users understand the domain better and perform the tasks better. Repeated exposure to the model will thus eventually result in a situation of cognitive <sup>fi</sup>t, regardless whether a good or poor representation model is used.

Based on CFT, we thus hypothesise that the use of a good representation model will lead to an initial advantage in learning from a conceptual model. In later phases of model use, it is plausible that any initial di<sup>f</sup>erence in learning from good and poor representation models will fade away. We thus formulate the <sup>fi</sup>rst set of hypotheses related to the outcome of learning.<sup>1</sup>

H1: In the initial stages of model use, the extent to which domain knowledge is acquired from using a good representation model is higher than from a poor representation model.

H2: In the later stages of model use, the extent to which domain knowledge is acquired from using a good representation model is not di<sup>f</sup>erent than from a poor representation model.

In cognitive psychology, learning speed is de<sup>fi</sup>ned as the number of trials required for a learner to reach a state that enables recall or recognition of the learned material – the less trials, the faster the learning (Sandvik, 2013). Consistent with hypotheses 1 and 2, we hypothesise that related to the speed of learning, the use of a good representation model leads to an initial advantage only. We refer to the concept of learning curve to suggest how the speed of learning changes over time. The learning curve is a depiction of learning in a temporal setting where incremental learning improvements occur over a period of time (Linton & Walsh, 2013). Based on CFT, we expect that in the initial stages of model use, learning is faster using a good representation model as the theory-guided structuring will make the domain concepts that need to be understood for task resolution easier to locate and/or easier to interpret. In terms of the learning curve this means that we expect a steeper (or shorter) learning curve with the good representation model.<sup>2</sup> With repeated exposure of the models (i.e. the spacing e<sup>f</sup>ect), at a certain point of time, we expect that also users of poor representation models will be able to internalise the locations and interpretations of the modelled domain concepts that are needed for task resolution. Hence, after a while, in later stages of model use, users of poor representation models will catch up with the learning (i.e. the learning curves of good and poor representation models converge). Accordingly, we formulate a second set of hypotheses related to speed of learning from conceptual models.

H3: In the initial stages of model use, the rate at which domain knowledge is acquired from using a good representation model is higher than from a poor representation model.

H4: In the later stages of model use, the rate at which domain knowledge is acquired from using a good representation model is not di<sup>f</sup>erent than from a poor representation model.

## 2.3. Measuring learning from conceptual models

In past conceptual modelling studies, subjects were required to answer questions about the domain that is represented in a model in order to assess their learning from the model. Khatri et al. (2006) di<sup>f</sup>erentiate semantic comprehension questions (e.g. must an X always be related to an Y?) from syntactic comprehension questions (e.g. what are the attributes of X?). While syntactic comprehension questions merely assess the user’s comprehension of the model (depending on the user’s knowledge of the used syntax), semantic comprehension questions require a deep engagement with the model and require an interpretation of the model’s content in terms of domain concepts. Answering the latter type of questions requires knowledge of the semantics of the language or technique used to create the model.

A comprehension task does not allow for direct observation of the cognitive process of learning from models. To examine directly the underlying cognitive process of readers during learning from conceptual models, we propose the use of eye-tracking, which is a process-tracing technique. Another process-tracing technique that has been used before in empirical research with conceptual models is verbal protocol analysis (Burton-Jones & Meso, 2006), which requires subjects to verbalise their thought processes while performing tasks with the model. Another alternative to get direct observations of cognitive processing is the use of NeuroIS data collection techniques for measuring either central nervous system signals (e.g. PET, DMS, TDCS, EEG, fMRI and fNIRS for measuring brain activity) or instruments like electrocardiogram (heart beat), galvanometer (skin response), electromyography (facial muscular movement) and oculometry (pupil dilation) for measuring peripheral nervous system signals (Muller-Putz, Riedl, & Wriessnegger, 2015; Riedl & Léger, 2016; Vom Brocke & Liang, 2014).

Compared to eye-tracking, verbal protocol analysis is a more intrusive process-tracing technique. Furthermore, coding verbal protocol data is challenging, prone to error, and requires subjective interpretation (Burton-Jones & Meso, 2006). To investigate the mental processes of humans, self-reporting is insu<sup>fi</sup>cient as people are often unable and/or unwilling to self-report (Dimoka, Pavlou, & Davis, 2011). NeuroIS methods on the other hand provide a viable alternative to eye-tracking but are costly in terms of equipment and e<sup>f</sup>ort to apply (Riedl & Léger, 2016). Therefore, we developed an eye-tracking procedure to observe and measure the process of learning.

## 3. Eye tracking

To address our research questions, we developed an eye-tracking procedure. The speci<sup>fi</sup>c choice for using eye-tracking is that we are interested in what a user looks at when performing a task that requires understanding a domain as modelled and whether viewing patterns are di<sup>f</sup>erent between the use of good and poor representation models. According to the eyemind relationship (Petrusel, Mendling, & Reijers, 2017), we can only accurately perceive something when we pay attention to it, meaning <sup>fi</sup>xate it with our eyes and focus our minds on it. Eye-tracking is capable of detecting when we focus on and pay attention to speci<sup>fi</sup>c model areas and when we integrate information from di<sup>f</sup>erent model areas. Its strength is in objectively, accurately, and unobtrusively observing the cognitive process in terms of attention to information elements and integration of information elements. With eye-tracking we can observe whether a user e<sup>f</sup>ectively pays attention to the parts of the model that are relevant for performing some task.

For the type of task to be performed we choose for semantic comprehension questions. This task requires a user to deeply engage with the model and make a conscious e<sup>f</sup>ort to understand the modelled domain concepts in order to locate and interpret the relevant information required for answering the questions. Our eye-tracking procedure for observing learning from conceptual models thus combines eye-tracking measurements (explained in the next sub-section) with performance data of a semantic comprehension task, which allows measuring both the outcome of learning and the speed of learning. Furthermore, by collecting eye-tracking measurements and performance data at regular intervals during the execution of the semantic comprehension task (e.g. after every x questions – see Empirical Study section for the operationalisation used with the REA ontology pattern), we can observe the process of learning and compare the outcome and speed of learning between alternative models.

## 3.1. Eye-tracking measurements

Eye-tracking o<sup>f</sup>ers a window into how individuals read and scan information that is displayed to them (Rayner, 1998). During decision-making tasks where users view information relevant to the decision, eye movements reveal the distribution of attention (Glaholt & Reingold, 2011). By relating eye movements with decision-making data, one can obtain a picture of the decision-making process.

Two common eye movement observations are: eye <sup>fi</sup>xations and eye saccades (Sharif & Maletic, 2010). Eye movements are made up of short bursts of stationary visual display termed fixations and are <sup>fi</sup>lled up with rapid and continuous movements termed saccades (Jacob, 1995). During <sup>fi</sup>xations, eyes remain almost motionless, whereas saccades are movements from one <sup>fi</sup>xation to another. A typical <sup>fi</sup>xation lasts approximately 200–300 milliseconds and is generally understood to indicate where a viewer’s attention is directed (Rayner, 1998).

When eyes <sup>fi</sup>xate on a certain area, the brain starts to process the visual information received from the eyes (Rayner, 1998). Using eye-tracking it is possible to identify how much time a user has spent on a speci<sup>fi</sup>c area of the model (referred to as the Area Of Interest (AOI)) and how quickly a user views a particular AOI. Especially the latter aspect is of interest for addressing our research questions. Lai et al. (2013) analysed eye-tracking research in the education domain. They found that most educational research on eye tracking focuses on how users process information and that temporal metrics are the most commonly used eye tracking measures. Hence for our study, a relevant eye-tracking metric is the Time for First Fixation (TFF) (Poole & Ball, 2006). This metric indicates how quickly a user converges his/her eyes on a speci<sup>fi</sup>c AOI in the model. The TFF is usually measured starting from the time a user is exposed to the model.

Figure 2 provides a fragment of an example ERD where TFF is measured with reference to an AOI termed CFO – a dotted rectangle created around the entity “CFO” including the cardinality that speci<sup>fi</sup>es to how many “CFO” instances an “Acquire Loan” instance is minimally and maximally related via an “authorized by” relationship. Consider that a user is exposed to Figure 2 at time $\mathbf { t } _ { 0 } .$ Consider also that this user needs to evaluate the semantic comprehension question “Is it possible to acquire a loan without the authorization of a CFO?” (question 6 in our study, see Appendix B). To answer this question, the user needs to locate the “CFO” entity (possibly after <sup>fi</sup>rst locating the “Acquire Loan”

![](/api/attachments/NE4HX2PG/fulltext/images/00f030e52b885ca4574ec22535149b93584db2ed5614267b5b57da67cd668d4d.jpg)  
Example of <sup>fi</sup>xations within the CFO AOI.

entity and next following the direction indicated by the “authorized $\mathrm { { b y } ^ { \mathrm { { \Rightarrow } } } }$ relationship, although other reading sequences are possible) and interpret the cardinality speci<sup>fi</sup>cation within the CFO AOI. If the user’s eyes <sup>fi</sup>xate (i.e. eyes remain stationary for a minimum amount of time, e.g. 200 milliseconds) at any place inside the CFO AOI, then the eye-tracker detects a <sup>fi</sup>xation inside this AOI. The hollow dot and full dot in Figure 2 are examples of <sup>fi</sup>xations within the CFO AOI. If the full dot in Figure 2 presents the <sup>fi</sup>rst <sup>fi</sup>xation within this AOI since the model was shown, and this <sup>fi</sup>xation occurs at time $\mathbf { t } _ { 1 : }$ , then TFF for the CFO AOI is $\mathrm { t } _ { 1 } - \mathrm { t } _ { 0 } .$ For the example question, a second AOI is drawn around the “Acquire Loan” entity. If the <sup>fi</sup>rst <sup>fi</sup>xation within this AOI occurs at time $\mathbf { t } _ { 2 }$ (which may be sooner or later than $\mathrm { t _ { 1 } } )$ , then $\mathbf { t } _ { 1 } - \mathbf { t } _ { 0 }$ and $\mathbf { t } _ { 2 } - \mathbf { t } _ { 0 }$ are the TFFs to consider for answering the example question. Should the user’s eyes <sup>fi</sup>xate again on one of these AOI’s (e.g. the hollow dot in the CFO AOI), then this time is not taken into account for TFF.

The shorter the TFFs for all AOIs relevant to answering a semantic comprehension question, the better a user was in locating and interpreting the relevant domain information for answering the question. If we observe at a certain moment during a semantic comprehension task (e.g. after x questions) lower TFFs for question x + 1 when using model A than when using model B, then less trials to locate relevant model elements were needed with model A (i.e. less/shorter saccades and possibly less/shorter <sup>fi</sup>xations outside the AOIs relevant to question x + 1), signifying better recall or recognition of the learned material. Lower TFF values with model A than with model B thus indicate a higher rate of acquiring domain knowledge till that moment in the learning process. In other words, the TFF values indicate that at that moment in the learning process the learning curve when using model A is steeper than when using model B. Shorter TFFs thus indicate a higher speed of learning.

## 4. Empirical study

The empirical study that we present in this section aims at demonstrating how the eye-tracking procedure described in the previous section can be used to measure the speed of learning from conceptual models, and also how it can be investigated whether, as hypothesised (see the Hypothesis Development subsection), good representation models expedite learning of domain concepts, at least in the initial stages of model use. For this demonstration, we use the REA ontology pattern (Dunn et al., 2005) as an example of a theory-derived guideline for structuring conceptual models. By applying the REA ontology pattern to ERDs we obtain good representation REA models. We also explain how we develop poor representation

REA models as ERDs that do not follow the REA ontology pattern. We then use our eye-tracking procedure to compare the outcome and speed of learning from both types of model.

## 4.1. Structuring conceptual models: the REA ontology pattern

The REA ontology is a theory for conceptual modelling originating in a semantic data model for accounting. This semantic model conceptualises di<sup>f</sup>erent real business domain situations related to economic exchange (e.g. selling, buying, renting, employing) using a common conceptual structure of three ontologica categories: resources, events, and agents (McCarthy, 1982). The model was developed inductively by investigating massive amounts of transactional data, in which recurring sequences of resource-event-agent constellations were discovered (McCarthy, 1982). Later, the model was formalised as an ontology and was grounded in business process and value chain theories (Geerts & McCarthy, 2002).

The core concepts and relationships of the REA ontology have been speci<sup>fi</sup>ed as an ontology pattern (Ruy, Guizzardi, Falbo, Reginato, & Santos, 2017), called the REA ontology pattern, which can be represented using a template for ERDs that has a prede<sup>fi</sup>ned layout for positioning domain concepts classi<sup>fi</sup>ed according to the REA ontological categories (Dunn et al., 2005). The prede<sup>fi</sup>ned REA ontology pattern layout is one where resources, events, and agents are positioned in left, central, and right diagram regions respectively, such that the events that determine the essential “give” and “take” nature of the economic exchange form a central axis connecting the exchanged resources indirectly with the agents that exchange them. This layout possesses a number of properties that correspond well with principles from aesthetics-based computing research which, when adhered to, reduce the chance of cognitive overload (Petre, 2006; Purchase, 2014; Ware, Purchase, Colpoys, & McGill, 2002) (see Table 1). The REA ontology pattern (layout) thus serves as a guideline for structuring conceptual models as to obtain cognitive <sup>fi</sup>t and creating, what we call in the paper, good representation REA models. Figure 3 shows the good representation REA model used in our study.

To instantiate the poor representation REA model needed for our study, we broke the conventional arrangement of the REA ontology pattern layout. To do so we deliberately violated the principles of aesthetics-based computing research. As there could be many ways of violating the principles, we focus on three perceptual segregation principles – proximity, symmetry, and orientation (Bennett, Ryall, Spalteholz, & Gooch, 2007). These principles are based on the idea that objects or <sup>fi</sup>gures can be memorable if they are di<sup>f</sup>erentiated from the background. Table 1 explains how we created the poor representation REA model used in the study (Figure 4). By not adhering to the REA ontology pattern, we expect that users of the poor representation REA model face a higher chance of su<sup>f</sup>ering from cognitive overload. It is likely that their mental representation of the task solution is of lower quality than that of good representation REA model users, which according to the CFT conceptual framework will result in worse performance, i.e. a lower learning outcome and a more shallow (or long) learning curve (as we elaborated in the Hypothesis Development sub-section). However, as argued before, with repeated exposure to the models, the positive e<sup>f</sup>ect on learning from a good representation model will fade away and the learning curves of both groups will converge. Hence, we expect that the use of a good representation REA model has a positive e<sup>f</sup>ect on learning in the initial stages of model use only.

Principles of aesthetics-based computing.

<table><tr><td>Concept</td><td>Details</td><td>Effect on cognitive overload</td></tr><tr><td>Symmetry</td><td>Graph-based layouts where elements are placed more symmetrically have been found to be easier to read. The symmetry that can be observed in the good representation REA model (i.e. a spatial organisation where elements on the left are resources, elements at the middle are events, and elements on the right are agents) is broken in the poor representation REA model by positioning the elements in the diagram without any particular order.</td><td>The fixed position of REA ontological categories provides visual cues that help in identifying resources, events, agents, and their relationships. When these visual cues are missing then model users will have a higher chance of suffering from cognitive overload.</td></tr><tr><td>Use of locality (proximity)</td><td>When graphical elements that are logically related to each other are placed in close proximity, then it is easier to understand their connection. In the good representation REA model, all resource-event-agent constellations (i.e. which agent exchanges which resources with which other agent?) are modelled by entities located close to each other. Furthermore, these related entities are placed as rows in the diagram (as best as possible). In the poor representation REA model, we broke this row-oriented arrangement of the resource-event-agent constellations.</td><td>By locating entities of resource-event-agent constellations in close proximity to each other, as “rows” on the diagram, users are presented this information in perceptually and cognitively manageable chunks. These users will have less chance of cognitive overload when compared to users of the poor representation REA model, where the components of these constellations are spread out across the diagram.</td></tr><tr><td>Reading direction (orientation)</td><td>A good layout directs the reading of the elements in the model. In the good representation REA model, reading is directed from the middle where the events (as the ontological core of the transaction) are located to the right where the participating agents are found and to the left where the affected resources are found. But as the characteristic spatial organisation of the REA ontology pattern no longer exists in the poor representation REA model, no particular reading direction is suggested.</td><td>The reading direction provides a visual cue for easily locating related resources, events, and agents. The absence of this cue affects cognitive overload negatively.</td></tr></table>

It is important to note that the information content of the models shown in Figures 3 and 4 is the same, implying that the models are informationally equivalent (Gemino & Wand, 2005). Only the arrangement of the model elements has changed. This means that the same set of semantic comprehension questions could be used for both models, allowing for a direct comparison of the outcome and speed of learning from the models.

## 4.2. Operational hypotheses

After choosing the theory-based guideline (i.e. REA ontology pattern), creating the models to be used in the study, and de<sup>fi</sup>ning the measures for our dependent variables (i.e. number of correctly answered semantic comprehension questions for outcome of learning and TFF for speed of learning), we can now introduce the testable hypotheses:

H1: In the initial stages of model use, the number of correctly answered semantic comprehension questions when using the good representation REA model is higher than when using the poor representation REA model.

H2: In the later stages of model use, the number of correctly answered semantic comprehension questions when using the good representation REA model is not di<sup>f</sup>erent from when using the poor representation REA model.

H3: In the initial stages of model use, the TFF when using the good representation REA model is lower than when using the poor representation REA model.

H4: In the later stages of model use, the TFF when using the good representation REA model is not di<sup>f</sup>erent than when using the poor representation REA model.

What remains to be operationalised is the meaning of “initial” and “later” stages of model use. We show in the Results sub-section that this operationalisation is robust with respect to the chosen interval of measuring our dependent variables.

## 4.3. Experimental design

The study had a 1 × 2 between-subjects design where subjects were randomly assigned to one of two groups: good representation REA model and poor

![](/api/attachments/NE4HX2PG/fulltext/images/464c07779a683762c7c96a25baaaffd714150e3b672d02fda02fb804b1e32ec7.jpg)  
Good representation REA model used in the study.

![](/api/attachments/NE4HX2PG/fulltext/images/5654eb3f95129357a06822688608ca2a93641290a7fa63cae9a4cc2c839259b4.jpg)  
Poor representation REA model used in the study.

representation REA model. Forty-four graduate students (22 in each group) from a US university who enrolled in a graduate business analytics course over two terms participated in the study. For participation, these students received 2% of the course grade. We chose these students as study subjects as they learnt the basic concepts of conceptual modelling using ERDs. During the course, they were also introduced to the REA ontology, however, without showing them ERDs that followed the REA ontology pattern. Thus, when the subjects are provided with the ERDs used in the experiment (Figures 3 and 4), they are expected to have the required knowledge to be able to interpret the semantics of the model and thus perform a semantic comprehension task. We chose deliberately for working with a relatively simple debt <sup>fi</sup>nancing conceptual model constructed around a single business transaction (i.e. acquiring and repaying loans). A simple model combined with a large number of questions ensured that that the same AOIs had to be revisited many times, allowing us to assess learning.

Each subject was placed in front of a computer <sup>fi</sup>tted with an eye-tracker Tobii X2 60. At <sup>fi</sup>rst, subjects’ eyes were calibrated and validated (a standard procedure for eye-tracking) by asking them to follow a series of dots on the screen. After this procedure, the subjects accessed a web-based questionnaire to assess their familiarity with modelling and their knowledge of debt <sup>fi</sup>nancing. Following this, they were shown a comprehension question (stage 1) and then the ERD depending on the group they belonged to (either good representation REA model or poor representation REA model) (stage 2). Once the subjects viewed the ERD carefully, they clicked on to the next screen to answer the question (stage 3). Subjects could click the back button to view the ERD again and then proceed to answer the question. A subject need not go back to stage 1 from stage 2 as the question is repeated in stage 3. Therefore, a subject can go back and forth only between stages 2 and 3. The model (stage 2) and the question (stage 3) were intentionally separated so that accurate eye measurement of subjects focusing on the model can be obtained. Appendix A shows the three stages for the good representation REA model with a speci<sup>fi</sup>c semantic comprehension question example. The subjects were exposed to a set of 20 semantic comprehension questions, where for each question the 3-stage procedure explained before was repeated. The high number of questions asked for a relatively simple model ensured that the subjects get familiarised with the model after repeated exposure and thus the speed of learning from the model can be tracked across di<sup>f</sup>erent phases of the experiment.

As investigating our research questions requires comparing learning at di<sup>f</sup>erent phases of model use, we intentionally maintained the same level of di<sup>fi</sup>culty of the semantic comprehension questions throughout the study. If compared to the initial stages, questions at the later stages of the study are easier or more di<sup>fi</sup>cult to answer, then an observed evolution in task performance and TFF measurements cannot be solely attributed to the type of the model used. Hence, we pilot-tested the questions with 5 PhD students with excellent knowledge of English from a European university who were familiar with the REA ontology. Based on their feedback on the clarity and di<sup>fi</sup>culty level of the questions, some questions were modi<sup>fi</sup>ed for the study. Appendix B shows the <sup>fi</sup>nal list of questions that we used (in the order shown).

## 4.4. Results

As a preliminary note we state that in all statistical tests reported in this sub-section (Table 2, 3, and 4) and Appendix E (Table E.1), the data is normally distributed for both groups and there is homogeneity of variance as assessed by Levene’s Test for Equality of

Variances. In all tables, “Good” refers to the use of a good representation REA model and “Poor” refers to the use of a poor representation REA model.

Before testing the hypotheses, it is important to verify the e<sup>f</sup>ectiveness of the randomization. Di<sup>f</sup>erent levels of prior knowledge of the domain and familiarity with the modelling technique might a<sup>f</sup>ect subjects’ performance. Therefore, subjects prior domain knowledge and modelling familiarity was checked (see Appendix B for the measurement instrument used). Table 2 shows that the scores are not signi<sup>fi</sup>cantly di<sup>f</sup>erent between the two groups.

Two types of analyses are done in this study, one with the task performance data (i.e. correctness scores) and the other with the eye movement data (i.e. TFF values) registered for answering each question. To distinguish between initial and later stages of model use, the twenty questions are divided into four phases where each phase consists of answering 5 questions. Thus, in the <sup>fi</sup>rst phase subjects answer questions 1 to 5 and in the last phase they answer questions 16 to 20. To decrease the likelihood that this particular phasing decision has an impact on the results, we repeated all reported analyses for other groupings of questions. Appendix C shows that a similar pattern of results is obtained if questions were grouped per 2 or 3 (i.e. 7 phases) or per 4 (i.e. 5 phases).

To test the <sup>fi</sup>rst set of hypotheses related to the outcome of learning, the analysis is done separately for each of the four phases. The sum of correct answers in each phase is compared between the two groups (Table 3). For example, the mean sum of correct answers on the <sup>fi</sup>rst <sup>fi</sup>ve questions is 4.45 for the good representation REA model group. The corresponding number for the poor representation REA model group is 3.91. Independent sample t-tests show that the mean di<sup>f</sup>erences between the two groups are signi<sup>fi</sup>cant in the <sup>fi</sup>rst two phases but are not signi<sup>fi</sup>cant in the last two phases. Hence, based on these results we can accept hypotheses H1 and H2.

When all the questions are combined, the di<sup>f</sup>erence in mean sums of correct answers between the two groups is signi<sup>fi</sup>cant (i.e. the good representation REA model group performed better than the poor representation REA model group, $\mathrm { t } = 3 . 1 8 , \mathrm { p } = 0 . 0 0 1 ,$ ). A possible reason could be that, although the di<sup>f</sup>erence in mean sums of correct answers between the two groups is not statistically signi<sup>fi</sup>cant in the later phases, the values are still higher for the good representation REA model group. The following graph (Figure 5) demonstrates this where the mean sum of correct responses of both groups is plotted over the four phases. It can be noted that the gap between the two lines narrowed over the four phases, indicating that the advantage of working with the good representation REA model fades away after prolonged exposure to the model.

Analysis of the modelling familiarity and domain <sup>Table 2.</sup>knowledge of the subjects.

<table><tr><td>Groups</td><td>Modelling familiarity Mean (SD)</td><td>t- statistics</td><td>Domain knowledge Mean (SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>4.68 (0.90)</td><td>t = 0.16, p = 0.43</td><td>3.89 (1.14)</td><td>t = 0.62, p = 0.27</td></tr><tr><td>Poor</td><td>4.64 (0.95)</td><td></td><td>3.62 (1.72)</td><td></td></tr></table>

Scores are on Likert scales ranging from 1 (lowest level of knowledge/ familiarity) to 7 (highest level of knowledge/familiarity)

Task performance analysis.

<table><tr><td>Groups</td><td>Phase 1 (Q1-Q5) Sum (SD)</td><td>t- statistics</td><td>Phase 2 (Q6-Q10) Sum (SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>4.45 (0.59)</td><td> $t = 2.24, p = 0.01^a$ </td><td>4.68 (0.57)</td><td> $t = 1.89, p = 0.03^a$ </td></tr><tr><td>Poor</td><td>3.91 (0.97)</td><td></td><td>4.23 (0.97)</td><td></td></tr><tr><td>Groups</td><td>Phase 3 (Q11-Q15) Sum (SD)</td><td>t- statistics</td><td>Phase 4 (Q16-Q20) Sum (SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>4.50 (0.74)</td><td> $t = 1.37, p = 0.09$ </td><td>4.59 (0.50)</td><td> $t = 1.13, p = 0.13$ </td></tr><tr><td>Poor</td><td>4.18 (0.79)</td><td></td><td>4.36 (0.79)</td><td></td></tr></table>

<sup>a</sup> p < 0.05

To perform the TFF analysis (for testing hypotheses 3 and 4 related to the speed of learning), the models are divided into AOIs related to entities (along with the cardinalities as these cardinalities are also needed to answer the questions). These AOIs are of exact same size in both models. To answer a question, a subject must refer to speci<sup>fi</sup>c AOIs in the model. Each question has two AOIs (except the $2 0 ^ { \mathrm { t h } }$ question which has 3). The list of AOIs is provided along with the questions in Appendix B. For example, to answer the <sup>fi</sup>rst question “Is it possible to acquire a loan from places other than a bank?”, subjects need to refer to the AOIs “Acquire Loan” and “Bank”. The time it takes to look at these AOIs for the <sup>fi</sup>rst time after the model is exposed (i.e. when a user moves from stage 1 to stage 2) is the TFF for these AOIs. If a subject navigates to the answer screen (i.e. moving from stage 2 to stage 3) without viewing the AOI and then comes back to view the AOI (i.e. moving back from stage 3 to stage 2) then the TFF is long as the entire duration since the model was exposed for the <sup>fi</sup>rst time (i.e. moving from stage 1 to stage 2) till the subject has a <sup>fi</sup>xation in the AOI is calculated as TFF. For each subject, the TFF values for the AOIs relevant to each question were registered.

The TFF analysis requires calculating the average TFF for each phase. To understand how the average TFF for the <sup>fi</sup>rst phase is calculated, consider the AOIs “Acquire Loan” and “Bank” for the <sup>fi</sup>rst question. For the good representation REA model group, the TFF averaged over all subjects is 1.92 seconds for the “Acquire Loan” AOI and 4.46 seconds for the “Bank” AOI. For the poor representation REA model group these values are 4.66 seconds and 5.61 seconds respectively. Now, the average TFF for the 10 AOIs (2 for each question and for the <sup>fi</sup>rst <sup>fi</sup>ve questions) is calculated. This comes to 2.29 seconds for the good representation REA model group and 3.90 seconds for the poor representation REA model group. Similar averages were calculated for the other three phases and are compared in Table 4. It is found that for each phase the average TFF was lower for those in the good representation REA model group than those in the poor representation REA model group. This allows accepting H3 but not H4.

Between the two groups, the overall di<sup>f</sup>erence on average TFF for the AOIs for all the questions is also signi<sup>fi</sup>cant (t = 4.29, p = 0.00). Although the mean di<sup>f</sup>erence between the two groups narrows down over the phases, the di<sup>f</sup>erences remain signi<sup>fi</sup>cant in all four phases. Figure 6 demonstrates this where the average TFF of both groups is plotted over the four phases.

To get additional insights, we performed three additional analyses using the collected eye-tracking data. Appendix D shows some sample heat maps which are visual representations of fixation intensity using di<sup>f</sup>erent colours (red – the largest number of <sup>fi</sup>xations and green – the least number of <sup>fi</sup>xations) (Jacob & Karn, 2003). These maps suggest that as subjects answered more questions, they were able to focus better on the AOIs that were necessary to answer the questions. Compared to the poor representation REA model group, the good representation REA model group initially focused better on the relevant AOIs. However, towards the end of the study, users of both groups were able to quickly converge their eyes on the AOIs needed to answer the questions.

![](/api/attachments/NE4HX2PG/fulltext/images/92d56d8a9f1a8efef0d50ca9a69ab9ace2101d2b44659deec0a263edc36c1ab4.jpg)  
Comparison of task performance between good representation REA model users (solid line) and poor representation REA <sup>Figure 5.</sup>model users (dotted line). The maximum correct answer is 5 as each phase has 5 (Yes/No) questions.

Time for <sup>fi</sup>rst <sup>fi</sup>xation analysis.

<table><tr><td>Groups</td><td>Phase 1 (Q1-Q5)Mean in sec. (SD)</td><td>t- statistics</td><td>Phase 2(Q6-Q10)Mean in sec.(SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>2.29 (0.45)</td><td rowspan="2"> $t = 5.41, p = 0.00^a$ </td><td>2.03 (0.68)</td><td rowspan="2"> $t = 3.92, p = 0.00^a$ </td></tr><tr><td>Poor</td><td>3.90 (0.66)</td><td>3.03 (0.89)</td></tr><tr><td>Groups</td><td>Phase 3 (Q11-Q15)Mean in sec.(SD)</td><td>t- statistics</td><td>Phasev4(Q16-Q20)Mean insec. (SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>1.41 (0.50)</td><td rowspan="2"> $t = 4.26, p = 0.00^a$ </td><td>1.66 (0.60)</td><td rowspan="2"> $t = 1.97, p = 0.03^a$ </td></tr><tr><td>Poor</td><td>2.35 (0.90)</td><td>2.06 (0.74)</td></tr></table>

<sup>a</sup> p < 0.05

A second analysis we performed was visit count analysis (Table 5). Visit counts track the number of times a viewer goes back to the same AOI.

The visit count analysis showed that poor representation REA model users go back to the relevant AOI a greater number of times than the good representation REA model users. However, in line with the trend depicted in Figure 6, visit counts decreased for both groups when moving through the phases of the task. Overall for all 20 questions, the mean visit count for the good representation REA model is 2.65 (0.39) and for the poor representation REA model it is 3.34 (0.40), $( \mathrm { p } = 0 . 0 0 , \mathrm { t } = 5 . 7 5 )$ . Finally, Appendix E provides similar insights based on a mouse click count analysis.

## 5. Discussion

We recall that the goal of the empirical study was to demonstrate how to use our proposed eye-tracking procedure to measure, apart from outcomes, the speed of learning from conceptual models (i.e. our <sup>fi</sup>rst research question) and how it can be used to investigate whether a particular proposed way of structuring conceptual models expedite learning (i.e. our second research question). We <sup>fi</sup>rst discuss the results of the empirical study, followed by a more indepth discussion of how our proposed eye-tracking procedure addresses our research questions.

## 5.1. Theory-based structuring of conceptual models: the REA ontology pattern

The analyses of comprehension task accuracy (Table 3) and TFF values (Table 4) show that users of the good representation REA model have an initial advantage over users of the poor representation REA model in learning the domain from the model, both in terms of outcome and speed of learning. Contrary to our expectations, this advantage is persistent for speed of learning (i.e. rejection of H4). Although the di<sup>f</sup>erences in average TFF values remain signi<sup>fi</sup>cant over the course of the semantic comprehension task, the visual inspection of the TFF data (Figure 6), the heat map analysis (Appendix D), the visit count analysis and the mouse click count analysis (Appendix E) indicate that the advantage becomes smaller in the later stages of model exposure, which suggests that users of the poor representation REA model catch up with the learning (i.e. converging learning curves).

The bene<sup>fi</sup>ts of structuring conceptual models according to the REA ontology pattern have been investigated before (Fuller, Murthy, & Schafer, 2010; Gerard, 2005; Jones, Tsay, & Griggs, 2005). In particular for learning from such models, the studies of Poels et al. (2011) and Poels (2011) showed bene<sup>fi</sup>ts related to more accurate understanding and easier interpretation of model contents. Our empirical study con<sup>fi</sup>rms the <sup>fi</sup>nding of better domain understanding if models are structured following the REA ontology pattern. However, the acceptance of H2 shows that this advantage is only temporary. Furthermore, using a model that is structured following the REA ontology pattern not only improves domain understanding, but the learning is also more e<sup>fi</sup>cient, i.e. the REA ontology pattern structure leads to faster focusing on those model elements that provide the domain understanding needed to perform tasks requiring such understanding.

![](/api/attachments/NE4HX2PG/fulltext/images/e6b8cc0a11b44cadf13026fa1578501147330bcd3c86acee6833e969e2e74927.jpg)  
Comparison of time for <sup>fi</sup>rst <sup>fi</sup>xation between good representation REA model users (solid line) and poor representation <sup>Figure 6.</sup>REA model users (dotted line).

Visit count analysis.

<table><tr><td>Groups</td><td>Phase 1 (Q1-Q5)Frequency(SD)</td><td>t- statistics</td><td>Phase 2 (Q6-Q10)Frequency(SD)</td><td>t- statistics</td></tr><tr><td>REA</td><td>3.07 (0.78)</td><td> $t = 4.06, p = 0.00^a$ </td><td>2.79 (0.65)</td><td> $t = 3.42, p = 0.01^a$ </td></tr><tr><td>Non-REA</td><td>4.08 (0.86)</td><td></td><td>3.48 (0.68)</td><td></td></tr><tr><td>Groups</td><td>Phase 3 (Q11-Q15)Mean in sec. (SD)</td><td>t- statistics</td><td>Phasev4 (Q16-Q20)Mean in sec. (SD)</td><td>t- statistics</td></tr><tr><td>REA</td><td>2.52 (0.55)</td><td> $t = 3.36, p = 0.01^a$ </td><td>2.21 (0.56)</td><td> $t = 2.05, p = 0.04^a$ </td></tr><tr><td>Non-REA</td><td>3.21 (0.79)</td><td></td><td>2.60 (0.69)</td><td></td></tr></table>

<sup>a</sup> p < 0.05

We believe that compared to previous studies, our study provides unique insights into the cognitive process of learning from models. What is di<sup>f</sup>erent from other studies, is that we measure outcome and speed of learning at regular intervals during the learning exercise. We acknowledge that the demonstration of our eye-tracking procedure on models structured using the REA ontology pattern does not corroborate or falsify the general, theory-agnostic hypotheses on outcome and speed of learning that we developed based on CFT. Nevertheless, our empirical study suggests the possibility that the bene<sup>fi</sup>cial e<sup>f</sup>ects on learning of structuring conceptual models using theory-derived guidelines are not persistent. In other words, using theoretical guidelines to structure conceptual models might be advantageous when it comes to foster shared domain understanding amongst stakeholders in systems development, however, the bene<sup>fi</sup>t of using theory-guided models is relative. Deep engagement with the models will eventually result in domain understanding, regardless how the models are structured.

The managerial implication is that using theoretical guidelines for structuring conceptual models that have proven to be bene<sup>fi</sup>cial for learning, is a good choice as learning will be faster and more e<sup>f</sup>ective, however, the bene<sup>fi</sup>ts on the long term of such models should not be exaggerated. Nevertheless, for companies like IT consulting <sup>fi</sup>rms, which often have their consultants involved in information systems projects at client organisations, the bene<sup>fi</sup>ts of structuring conceptual models can be substantial as time is a scarce resource and a steep learning curve in acquiring domain knowledge frees up time for other activities. Such companies should insist on using theory-based guidelines for structuring conceptual models. The implication for researchers is that they should also evaluate proposed theoretical guidelines for e<sup>fi</sup>- ciency, and not just for e<sup>f</sup>ectiveness, as is usually the case now. Enabling faster learning is a quality dimension of conceptual models that is not to be neglected.

## 5.2. Eye-tracking to observe the process of learning from models

In a review of six studies that employed eye-tracking to investigate multimedia learning, Mayer (2010) <sup>fi</sup>nds that in all studies where a manipulation had an e<sup>f</sup>ect on learning outcomes it also had a corresponding e<sup>f</sup>ect on eye <sup>fi</sup>xation time. Our empirical study results indirectly corroborate this <sup>fi</sup>nding as in the initial stages of learning, the good representation REA model users were both more e<sup>fi</sup>cient in locating relevant model elements and more e<sup>f</sup>ective in solving the task that depended on domain understanding.

What makes our eye-tracking procedure special is that we can investigate whether these e<sup>f</sup>ects are persistent. Although many studies have investigated how theoryguided conceptual models help in acquiring domain understanding, the impact of using a good representation model on domain understanding has been measured only after model exposure. For instance, studies like (Burton-Jones & Meso, 2008; Figl et al., 2013; Poels, 2011) that have used perception-based measures require subjects to express their perception of the model’s ease (or di<sup>fi</sup>culty) of understanding or usefulness after task performance and as such they measure the process of learning only indirectly. Studies like (Bodart et al., 2001; Mendling et al., 2012) that have approximated speed of learning as the time taken to perform understandingrelated tasks include in this time also the time taken to form a mental representation of the task (i.e. understanding the question). Compared to time measurements, our eye-tracking procedure allows to observe learning more directly as it only considers the time taken for forming the mental representation of the application domain (i.e. understanding the domain as modelled) since $\mathrm { t } _ { 0 }$ in the calculation of TFF is the moment at which the model is exposed to the user.

Recently, the use of NeuroIS measurements has gained traction in IS research. Physiological measures such as heart rate (variability), brain activity, galvanic skin response and eye activity (i.e. pupil dilation and blink rate) have been proposed as indirect, real-time and objective measures of the cognitive processing required for understanding conceptual models (Weber, Sadiq, & Wang, 2018). In particular, such measurements can provide new insights into speci<sup>fi</sup>c e<sup>f</sup>ects on cognitive load (i.e. e<sup>f</sup>ort of the working memory to move knowledge to long-term memory) like the worked example e<sup>f</sup>ect, the split-attention e<sup>f</sup>ect, the expertise reversal e<sup>f</sup>ect and other e<sup>f</sup>ects predicted by Cognitive Load Theory (Sweller, 1988). While these measures may reveal the e<sup>f</sup>ect of theory-guided structuring of conceptual models on cognitive (over)load, they cannot be used to observe where a person looks at when learning from a model. In contrast, our eye-tracking procedure based on scan path measures (e.g. TFF, visit counts) and visual gaze analysis (e.g. heat maps) allows observing model viewing patterns and thus provides valuable insights on how users read models, which can be used to test predictions based on speci<sup>fi</sup>c theory-guided structuring of models.

For researchers, the implication is that using our eyetracking procedure, which combines task performance and eye-tracking measurements, a more comprehensive evaluation of theory-derived guidelines for structuring conceptual models can be done. In particular, our eyetracking procedure allows gaining insights into how the structuring of conceptual models, based on theory, helps in directing attention to those model elements that matter for acquiring the domain knowledge needed for the tasks to be performed using models.

## 5.3. Limitations and future research

We formulate the implications of our research with caution as we are aware of its limitations. First, the results of the empirical study with a model structuring following the REA ontology pattern cannot be generalised to theory-guided models in general. Structuring models can be done with respect to use of abstract syntax, concrete syntax, layout, or combinations of any of these. The REA ontology pattern only deals with diagrammatic layout. Hence, in our empirical study, two model versions were compared that were informationally equivalent. Comparing informationally equivalent models allows using the same comprehension task for both models. If theoretical guidance results in models not being informationally equivalent, then our proposed eye-tracking procedures is not applicable. Further research is needed to <sup>fi</sup>gure out how in such cases learning from domain models can be compared.

Second, we acknowledge that we did not formalise the precise relationship between a trend in TFF values over the course of a learning task (as in Figure 6) and the learning curve. Figure 6 shows that during the entire comprehension task, users of the good representation model are able to locate the model elements relevant for answering a semantic comprehension question quicker than the users of the poor representation model, indicating a steeper learning curve with the good repre sentation model. But it is hard to tell from our data whether (and when) the learning curves of the alternative models are converging. Our graph of TFF values (Figure 6) seems to corroborate the education literature on learning curves, as per this literature, the rate of learning generally slows down after initial learning (Linton & Walsh, 2013). The exact nature of the relationship of TFF as a measure of speed of learning and the learning curve is a topic for future research.

## 6. Conclusion

We presented a novel eye-tracking procedure to investigate how quickly we learn from conceptual models. This question has not been addressed in previous research, which did not approach learning from models as a process. Our procedure requires study subjects to perform a relatively lengthy semantic comprehension task that requires deep engagement with a conceptual model. By repeatedly measuring the time for <sup>fi</sup>rst <sup>fi</sup>xation on model areas that convey the domain information needed to perform the task, we can observe and track learning of the domain and evaluate the speed of learning. By also measuring comprehension task accuracy at regular intervals during the course of the comprehension task, we can further control for the outcome of learning.

We also reported on an empirical study in which we used our eye-tracking procedure to test the hypothesis that conceptual models that are structured following the REA ontology pattern expedite learning. Our study demonstrates that, using our research design and eyetracking procedure, researchers can investigate the hypothesised impact of theoretical guidelines for structuring models on users’ domain understanding during model use. Our experience shows that eye-tracking is a viable procedure to get unique insights into the process of learning from conceptual models. Such insights allow researchers to more comprehensively evaluate proposed theories and guidelines for structuring conceptual models.

## Notes

1. Note that these and the next set of hypotheses are not readily testable as they require further operationalisation, which is done in the Empirical Study section.

2. A steep or short learning curve does not indicate a di<sup>fi</sup>cult initial learning process as common language use of the phrase “steep learning curve” usually seems to imply. On the contrary, a shallow or long learning curve indicates a more di<sup>fi</sup>cult initial learning process, which is what we expect when using a poor representation model.

3. The model and the question were intentionally separated into two di<sup>f</sup>erent screens to get accurate eye movement data. If both question and model appeared in the same screen then it would have been di<sup>fi</sup>cult to track the eye movements over the model as the question will distract the user from viewing the model.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the authors.

## ORCID

Geert Poels http://orcid.org/0000-0001-9247-6150

## References

Bennett, C., Ryall, J., Spalteholz, L., & Gooch, A. (2007). The aesthetics of graph visualization. In W. Cunningham, G. Meyer, & L. Neumann (Eds.), Computational aesthetics ofin graphics visualization and imaging (pp. 1–8).

Bera, P., Burton-Jones, A., & Wand, Y. (2011). Guidelines for designing visual ontologies to support knowledge identi<sup>fi</sup>cation. MIS Quarterly, 35(4), 883–908.

Bera, P., Burton-Jones, A., & Wand, Y. (2014). How semantics and pragmatics interact in understanding conceptual models. Information Systems Research, 25 (2), 401–419.

Bera, P., & Evermann, J. (2014). Guidelines for using UML association classes and their e<sup>f</sup>ect on domain understanding in requirements engineering. Requirements Engineering Journal, 19(1), 63–80.

Bodart, F., Patel, A., Sim, A., & Weber, R. (2001). Should optional properties be used in conceptual modeling? A theory and three empirical tests. Information Systems Research, 12(4), 384–405.

Burton-Jones, A., & Meso, P. (2006). Conceptualizing systems for understanding: An empirical test of decomposition principles in object-oriented analysis. Information Systems Research, 17(1), 38–60.

Burton-Jones, A., & Meso, P. (2008). The e<sup>f</sup>ects of decomposition quality and multiple forms of information on novices’ understanding of a domain from a conceptual model. Journal of the Association for Information Systems, 9(12), 748–802.

Burton-Jones, A., Wand, Y., & Weber, R. (2009). Guidelines for empirical evaluations of conceptual modeling grammars. Journal of the Association for Information Systems, 10(6), 495–532.

Challis, B. H. (1993). Spacing e<sup>f</sup>ects on cued-memory tests depend on level of processing. Journal of Experimental Psychology: Learning, Memory, and Cognition, 19(2), 389–396.

Dimoka, A., Pavlou, P., & Davis, F. D. (2011). NeuroIS: The potential of cognitive neuroscience for information systems research. Information Systems Research, 22(4), 687–702.

Dunn, C., Cherrington, J. O., & Hollander, A. S. (2005). Enterprise information systems: A pattern based approach. McGraw-Hill.

Evermann, J., & Wand, Y. (2006). Ontological modelling rules for UML: An empirical assessment. Journal of Computer Information Systems, 47(1), 14–29.

Figl, K., Mendling, J., & Strembeck, M. (2013). The in<sup>fl</sup>uence of notational de<sup>fi</sup>ciencies on process model comprehension. Journal of the Association for Information Systems, 14(6), 312–338.

Fuller, R., Murthy, U., & Schafer, B. (2010). The e<sup>f</sup>ects of data model representation method on task performance. Information and Management, 47, 208–218.

Geerts, G., & McCarthy, W. E. (2002). An ontological analysis of the primitives of teh extended-REA enterprise information architecture. The International Journal of Accounting Information Systems, 3(1), 1–16.

Gemino, A., & Wand, Y. (2005). Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data and Knowledge Engineering, 55, 301–326.

Gerard, G. J. (2005). The REA pattern, knowledge structures and conceptual modeling: Comparison of mandatory and optional properties. Data and Knowledge Engineering, 55, 301–326.

Glaholt, M. G., & Reingold, E. M. (2011). Eye movement monitoring as a process tracing methodology in decision making research. Journal of Neuroscience, Psychology, and Economics, 4, 125–146.

Guizzardi, G. (2005). Ontological Foundations for Structural Conceptual Models (PhD). University of Twente, The Netherlands.

Ho<sup>f</sup>er, J. A., Prescott, M. B., & McFadden, F. R. (2008). Modern database management (8th ed.). Upper Saddle River, N.J.: Pearson Prentice Hall.

Jacob, R. (1995). Eye tracking in advanced interface design, in virtual environments and advanced interface design. New York: Oxford University Press.

Jacob, R., & Karn, K. (2003). Eye tracking in humancomputer interaction and usability research: Ready to deliver the promises. In R. Hyona (Ed.), The mind’s eye: Cognitive and applied aspects of eye movement research (pp. 573–605). Oxford, England: Elsevier.

Jones, R. A., Tsay, J. E., & Griggs, K. (2005). An empirical investigation of the task speci<sup>fi</sup>c relative strengths of selected accounting and information systems diagramming techniques. Journal of Computer Information Systems, 46, 99–114.

Khatri, V., Vessey, I., Ramesh, V., Clay, P., & Park, S. (2006). Understanding conceptual schemas: Exploring the role of application and is domain knowledge. Information Systems Research, 17(1), 81–99.

Lai, M., Tsai, M., Yang, F., Hsu, C., Liu, T., Lee, S., . . . Tsai, C. (2013). A review of using eye-tracking technology in exploring learning from 2000 to 2012. Educational Research Review, 10, 90–115.

Linton, J. D., & Walsh, S. T. (2013). Extracting value from learning curves: Integrating theory and practice. Creativity and Innovation Management, 22(1), 10–25.

Maass, W., Storey, V., & Kowatsch, T. (2011). Efects of external conceptual models and verbal explanations on shared understanding in small groups. Berlin, Heidelerg: Springer.

Mayer, R. E. (2010). Unique contributions of eye-tracking research to the study of learning with graphics. Learning and Instruction, 20, 167–171.

Mayer, R. E., & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. Educational Psychologist, 38(1), 43–52.

McCarthy, W. E. (1982). The REA accounting model: A generalized framework for accouting systems in a shared data environment. The Accounting Review, 57 (3), 554–578.

Mendling, J., Strembeck, M., & Recker, J. (2012). Factors of process model comprehension- <sup>fi</sup>ndings from a series of experiments. Decision Support Systems, 53, 195–206.

Moody, D. (2009). The physics of notations: Toward a scienti<sup>fi</sup>c basis for constructing visual notations in software engineering. IEEE Transactions on Software Engineering, 35(6), 756–779.

Muller-Putz, G., Riedl, R., & Wriessnegger, S. (2015). Electroencephalography (EEG) as a research tool in the information systems discipline: Foundations, measurement, and applications. Communications of the AIS, 37, 46.

Pavlik, P., & Anderson, J. (2005). Practice and forgetting e<sup>f</sup>ects on vocabulary memory: An activation-based model of the spacing e<sup>f</sup>ect. Cognitive Science, 29, 559–586.

Petre, M. (2006). Cognitive dimensions \`beyond the notation’. Journal of Visual Languages & Computing, 17(4), 292–301.

Petrusel, R., Mendling, J., & Reijers, H. A. (2017). How visual cognition in<sup>fl</sup>uences process model comprehension. Decision Support Systems, 96, 1–16.

Poels, G. (2011). Understanding business domain models: The e<sup>f</sup>ect of recognizing resource-event-agent conceptual modeling structures. Journal of Database Management, 22(1), 69.

Poels, G., Maes, A., Gailly, F., & Paemeleire, R. (2011). The pragmatic quality of resources-events-agents diagrams: An experiemental evaluation. Information Systems Journal, 21(1), 63–89.

Poole, A., & Ball, L. J. (2006). Eye tracking in humancomputer interaction and usability research: current status and future prospects. In C. Ghaoui (Ed.), Encyclopedia of human computer interaction (pp. 211–219). Hershey, PA: Idea Group.

Purchase, H. C. (2014). Twelve years of diagrams research. Journal of Visual Language Computing, 25(2), 57–75.

Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. Psychological Bulletin, 124(3), 372–422.

Richardson, J. (1973). E<sup>f</sup>ect of speed of learning and degree of learning on cue selection. Journal of Experimental Psychology, 98(2), 396–403.

Riedl, M., & Léger, P.-M. (2016). Fundamentals of NeuroIS. information systems and the brain. Berlin, Heidelerg: Springer.

Ruy, F. B., Guizzardi, G., Falbo, R. A., Reginato, C. C., & Santos, V. A. (2017). From reference ontologies to ontology

patterns and back. Data & Knowledge Engineering, 109, 41–69.

Sandvik, Ø. (2013). The interaction of learning speed and memory interference: When fast is bad (Masters of Philosophy). University of Oslo, Oslo.

Shaft, T., & Vessey, I. (2006). The role of cognitive <sup>fi</sup>t in the relationship between software comprehension and modi<sup>fi</sup>cation. MIS Quarterly, 30(1), 29–55.

Shanks, G., Tansley, E., & Weber, R. (2004). Representing composites in conceptual modeling. Communications of the ACM, 47(7), 77–80.

Sharif, B., & Maletic, J. (2010). An eye tracking study on the efects of layout in understanding the role of design patterns. Paper presented at the IEEE International Conference on Software Maintenance, Timisoara, Romania.

Sweller, J. (1988). Cognitive load during problem solving: E<sup>f</sup>ects on learning. Cognitive Science, 12(2), 257–285.

Vessey, I. (1991). Cognitive <sup>fi</sup>t: A theory-based analysis of the graphs versus tables literature. Decision Sciences, 22 (2), 219–240.

Vom Brocke, J., & Liang, T.-P. (2014). Guidelines for neuroscience studies in information systems research. Journal of Management Information Systems, 30(4), 211–234.

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information systems analysis and design grammars. Journal of Information Systems, 3, 217–237.

Wand, Y., & Weber, R. (2017). Thirty years later: Some re<sup>fl</sup>ections on ontological analysis in conceptual modeling. Journal of Database Management, 28, 1.

Ware, C., Purchase, H. C., Colpoys, L., & McGill, M. (2002). Cognitive measurements of graph aesthetics. Information Visualization, 1(2), 103–110.

Weber, B., Sadiq, S., & Wang, W. (2018). How to use neuro-physiological measurements in bpm research and practice. Paper presented at the 16th International Conference on Business Process Management, Sidney, Australia.

Young, D. R., & Bellezza, F. S. (1982). Encoding variability, memory organization, and the repetition e<sup>f</sup>ect. Journal of Experimental Psychology: Learning, Memory, and Cognition, 8(6), 545–559.

Appendix A. Procedure for answering semantic comprehension questions in the experiment

![](/api/attachments/NE4HX2PG/fulltext/images/1ff4ca2c3d2cd970c34c4ac7ac2723ee4a7195b27f3109622c0584c158b4e735.jpg)  
Appendix B. Semantic comprehension, domain knowledge and modelling familiarity

<table><tr><td>No</td><td>Semantic Comprehension Question</td><td>AOIs (number)</td></tr><tr><td>1</td><td>Is it possible to acquire a loan from places other than a bank?</td><td>Acquire loan (1), Bank (2)</td></tr><tr><td>2</td><td>Does a finance clerk process a loan repayment to a bank?</td><td>Repay loan (3), Finance Clerk (4)</td></tr><tr><td>3</td><td>Is loan acquisition processed by a finance clerk?</td><td>Acquire loan (5), Finance Clerk (6)</td></tr><tr><td>4</td><td>Does a CFO authorise a loan repayment?</td><td>CFO (7), Repay loan (8)</td></tr><tr><td>5</td><td>Is a loan repayment paid to a bank?</td><td>Repay Loan (9), Bank (10)</td></tr><tr><td>6</td><td>Is it possible to acquire a loan without the authorisation of a CFO?</td><td>Acquire loan (11), CFO (12)</td></tr><tr><td>7</td><td>Are the loan proceeds deposited to a specific account?</td><td>Acquire loan (13), Account (14)</td></tr><tr><td>8</td><td>Can a bank be associated with no loan repayment?</td><td>Repay loan (15), Bank (16)</td></tr><tr><td>9</td><td>Is it possible to deposit a specific loan proceed to more than one account?</td><td>Acquire loan (17), Account (18)</td></tr><tr><td>10</td><td>Can a bank be associated with no loan acquisition?</td><td>Bank (19), Acquire Loan (20)</td></tr><tr><td>11</td><td>Is it possible to trace the total amount of loan repayments for a loan with loan number?</td><td>Acquire loan (21), Repay loan (22)</td></tr><tr><td>12</td><td>Is it possible to repay a loan over a period of time?</td><td>Acquire loan (23), Repay loan (24)</td></tr><tr><td>13</td><td>Is it possible to repay a loan other than by using funds from an account?</td><td>Repay loan (25), Account (26)</td></tr><tr><td>14</td><td>Can an account be associated with no loan repayment?</td><td>Repay loan (27), Account (28)</td></tr><tr><td>15</td><td>Is it possible to obtain more than one loan from the same bank?</td><td>Acquire loan (29), Bank (30)</td></tr><tr><td>16</td><td>For a specific loan repayment, is it possible to withdraw funds from more than one account?</td><td>Repay loan (31), Account (32)</td></tr><tr><td>17</td><td>Can an account be associated with no loan acquisition?</td><td>Acquire loan (33), Account (34)</td></tr><tr><td>18</td><td>Can a CFO authorise more than one loan acquisition?</td><td>Acquire loan (35), CFO (36)</td></tr><tr><td>19</td><td>Can a specific repayment number have more than one loan number?</td><td>Acquire loan (37), Repay loan (38)</td></tr><tr><td>20</td><td>Is it possible to repay a loan using funds from an account that was also used to deposit the loan proceeds?</td><td>Acquire loan (39), Repay loan (40), Account (41)</td></tr></table>

## Questions for assessing modelling familiarity and domain knowledge

To what extent do you know data modelling concepts (such as entities and relationships)? To what extent do you have experience in using data modelling concepts (such as entities and relationships)? To what extent are you familiar with the processes of obtaining and repayment of bank loans? To what extent do you have experience with the processes of obtaining and repayment of bank loans?

## Appendix C. Data analysis for other phasings of the comprehension task

<table><tr><td>Groups</td><td>Performance difference between two groups</td><td>TFF difference between two groups</td></tr><tr><td>Q1-Q3</td><td>Yes</td><td>Yes</td></tr><tr><td>Q4-Q6</td><td>Yes</td><td>Yes</td></tr><tr><td>Q7-Q9</td><td>Yes</td><td>Yes</td></tr><tr><td>Q10-Q12</td><td>No</td><td>Yes</td></tr><tr><td>Q13-Q15</td><td>No</td><td>Yes</td></tr><tr><td>Q16-Q18</td><td>No</td><td>Yes</td></tr><tr><td>Q19-Q20</td><td>No</td><td>No</td></tr><tr><td>Q1-Q4</td><td>Yes</td><td>Yes</td></tr><tr><td>Q5-Q8</td><td>Yes</td><td>Yes</td></tr><tr><td>Q9-Q12</td><td>No</td><td>Yes</td></tr><tr><td>Q13-Q16</td><td>No</td><td>Yes</td></tr><tr><td>Q17-Q20</td><td>No</td><td>Yes</td></tr><tr><td>Q1-Q5</td><td>Yes</td><td>Yes</td></tr><tr><td>Q6-Q10</td><td>Yes</td><td>Yes</td></tr><tr><td>Q11-Q15</td><td>No</td><td>Yes</td></tr><tr><td>Q16-Q20</td><td>No</td><td>Yes</td></tr></table>

Note: As per the above analysis, it is di<sup>fi</sup>cult to pinpoint the exact question which the breaking point for the performance di<sup>f</sup>erence between the two groups is. Rather a range (Question 9- Question 10) is the probable point from where there is no di<sup>f</sup>erence in the performance between the two groups.

Appendix D. Heat map analysis (for sample heat maps)

<table><tr><td>Question</td><td>Good representation REA model group</td><td>Poor representation REA model group</td></tr><tr><td>5</td><td><img src="/api/attachments/NE4HX2PG/fulltext/images/b91aecd0ca98dff03fe5800456cf64a8e47e02e582bc8bb7cac496a066478378.jpg"/></td><td><img src="/api/attachments/NE4HX2PG/fulltext/images/29366a245e36dc9634e1a39bf068736587d07f21c65cc41100e39183b11dbff0.jpg"/></td></tr><tr><td>12</td><td><img src="/api/attachments/NE4HX2PG/fulltext/images/09d2f5f7ce0b803e5ca62435137128177f74821bb0cd4fa0074fb6ee2e8fcfce.jpg"/></td><td><img src="/api/attachments/NE4HX2PG/fulltext/images/09e7b1e5add9b419a85e2308225764ae9ec1d3af02eb115582a9bd7ec1622170.jpg"/></td></tr><tr><td>19</td><td><img src="/api/attachments/NE4HX2PG/fulltext/images/f0d2649fa24f0cdbf80639f052b0fa1f017c9175e050664eed8966ffd72e9385.jpg"/></td><td><img src="/api/attachments/NE4HX2PG/fulltext/images/c65355c2bfb06289e95810e48ff7b83446d5d330f88c5d5e577a7b96ef220704.jpg"/></td></tr></table>

## Appendix E. Mouse click count analysis

To formulate the hypotheses, we made an assumption that the internal representation of users gets modi<sup>fi</sup>ed by being exposed to an engaging task with the model (Shaft & Vessey, 2006). Learning takes place as this representation gets modi<sup>fi</sup>ed. If users have already created a good mental representation of the model, then they need not refer to the model frequently in answering the questions. This would be particularly true for those who used the good representation REA model. To check this assumption, we performed a mouse click count analysis. The Tobii eye tracker registered the number of times users click on a certain screen area (in this case the “back to the model” button- see Appendix A, stage 3).

After viewing the model (stage 2), users continued to view the question to answer it (stage 3). However, as the model was not visible while answering the question<sup>3</sup>, users had to click “back to the model” in order to see the model again. This process can be repeated till users form a good mental representation of the model required for task solution. If users did not form a good mental representation of the model then they would click on “back to the model” repeatedly.

Table E1 shows the resulting mouse click count analysis. The number 0.79 refers to the average frequency of clicking the “back to the model” button by the good representation REA model group for the <sup>fi</sup>rst <sup>fi</sup>ve questions. For example, subject 1 might have hit 3 times the back button for the <sup>fi</sup>rst <sup>fi</sup>ve questions (% hit is 0.6) and subject 2 might have hit 5 times the back button for the <sup>fi</sup>rst <sup>fi</sup>ve questions (% hit is 1.0). Thus, the average mouse click percentage for these two subjects is 0.8.

The analysis shows that the poor representation REA model group clicked on the “back to the model” button signi<sup>fi</sup>cantly more than the good representation REA model group in all phases. Figure E1 visually depicts this situation where the average click percentage is plotted for the two groups for all four phases.

The mouse click count data indicate that initially more iterations between model and question were required to create a good mental representation of the model. Thus, at the beginning of the study, when the subjects were not familiar with the model, they need to refer to the model more frequently to create the mental representation of it. This was more prominent for the poor representation REA model group. But as the experiment progressed, the mental representation of the model was more stable in both groups and therefore the number of times to refer back to the model decreased.

Mouse click count on “back to the model” analysis.

<table><tr><td>Groups</td><td>Phase 1 (Q1-Q5)Mean (SD)</td><td>t- statistics</td><td>Phase 2 (Q6-Q10)Mean (SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>0.79 (0.33)</td><td> $t = 3.06, p = 0.00^a$ </td><td>0.72 (0.20)</td><td> $t = 2.38, p = 0.01^a$ </td></tr><tr><td>Poor</td><td>1.08 (0.30)</td><td></td><td>0.89 (0.27)</td><td></td></tr><tr><td>Groups</td><td>Phase 3 (Q11-Q15)Mean (SD)</td><td>t- statistics</td><td>Phasev4 (Q16-Q20)Mean (SD)</td><td>t- statistics</td></tr><tr><td>Good</td><td>0.62 (0.30)</td><td> $t = 2.01, p = 0.02^a$ </td><td>0.50 (0.20)</td><td> $t = 2.06, p = 0.02^a$ </td></tr><tr><td>Poor</td><td>0.82 (0.35)</td><td></td><td>0.65 (0.26)</td><td></td></tr></table>

<sup>a</sup> p < 0.05

![](/api/attachments/NE4HX2PG/fulltext/images/db32e17415183e578c709fccbdefb7543a7255fe660108be61d1d3e7fce66072.jpg)  
Comparison of mouse click count between good representation REA model users (solid line) and poor representation <sup>Figure E1.</sup>REA model users (dotted line).
