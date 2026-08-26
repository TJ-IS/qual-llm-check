---
otero_id: 12812
otero_key: "XTYPU72P"
title: "The Effect of Risk Representation Using Colors and Symbols in Business Process Models on Operational Risk Management Performance"
authors: "Tyge-F. Kummer; Jan Mendling"
year: "2021"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00676"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 22 Issue 3

Article 7

2021

# The Effect of Risk Representation Using Colors and Symbols in Business Process Models on Operational Risk Management Performance

Tyge-F. Kummer , t.kummer@qut.edu.au

Jan Mendling , jan.mendling@wu.ac.at

Follow this and additional works at: https://aisel.aisnet.org/jais

# The Effect of Risk Representation Using Colors and Symbols in Business Process Models on Operational Risk Management Performance

Tyge-F. Kummer<sup>1</sup>, Jan Mendling<sup>2</sup>

<sup>1</sup>QUT Business School, Queensland University of Technology, Australia, t.kummer@qut.edu.au <sup>2</sup>Vienna University of Economics and Business, Austria, jan.mendling@wu.ac.at

## Abstract

The operational management of risk and internal controls (RIC) makes increasing use of visual representations to support tasks such as risk assessment and control activity definition. The strengths and weaknesses of different representations are typically assessed by cognitive theories that assume an analytical and an intuitive mode of information processing. Previous research has focused mainly on the analytical risk assessment while intuitive information processing has largely been neglected. We develop a theoretical argument based on dual-process theory, which explains why RIC representational alternatives influence different levels of information processing. We test our hypotheses with the help of an online experiment using accountants and operation managers recruited via MTurk (N = 166). Our results suggest that highlighting risk and controls in business process modeling and notation (BPMN) by using color improves risk understanding, control understanding, and the identification of control improvements, which help reduce the risk in a given process. Furthermore, we do not find evidence that the inclusion of color leads to perception biases. This has implications for information systems research, which has primarily addressed the analytical processing of conceptual models. Our findings extend cognitive research on such models by adding an intuitive processing path that can improve the user’s risk management performance. For practitioners, our findings are particularly relevant because colors can be easily added as a secondary notation element without disguising the factual risk situation in processes.

Keywords: Business Process Management, Internal Controls, Risk Management, Operational Risks, Experiment

Alexander Mädche was the accepting senior editor. This research article was submitted on February 19, 2019 and underwent four revisions.

## 1 Introduction

The modeling of business processes can be used to analyze information systems (Davies et al., 2006), in process redesign (Davies et al., 2006; Figl, Recker et al., 2013), and for the assessment of risks and internal control information as part of (enterprise) risk management (Kelton et al., 2010). For many organizations, effective risk management support is of vital importance for the following reasons. First, operational risks such as machine downtimes or insufficient health and safety procedures can cause severe damage to an organization and its employees (Power, 2007, p. 110 ). Second, operational risk includes accidental errors as well as intentional fraudulent behavior. In 2016/17, for instance, the latter alone caused a median loss of \$130,000 per case and damages that exceeded \$7 billion (ACFE, 2018). Third, government regulations such as the Sarbanes-Oxley Act (SOX) force organizations to file formal

reports on the effectiveness of internal controls for demonstrating compliance (SOX, 2002, Section 302).

The understanding of risks and internal controls (RIC) is crucial to improving the organizational risk situation. Risk management supports organizations, helping them to deal effectively with uncertainty, associated risk, and opportunity in order to enhance the capacity to build value (COSO, 2004). Operational risk managers devise appropriate control activities at the process level to minimize the impact of risks.

Operational risk managers’ understanding of RIC can benefit from concepts commonly used in business process management (BPM), including concepts involving the documentation of business processes that use process models. These models are increasingly used for the assessment of RIC information as part of the internal control system (Boritz et al., 2012). BPM relies heavily on standardized visualizations such as business process modeling and notation (BPMN). However, no standard for the visualization of RIC information has been established thus far. Various representational alternatives have been suggested, ranging from pure text to solely visual diagrams, and the effectiveness of these different representations, as well as their mutual efficacy, is subject to ongoing research (Kelton et al., 2010). Empirical evidence on the relative benefits of textual representation formats and visual representations in diagrams is provided by Dunn and Gerard (2001), Carnaghan (2006), Boritz et al. (2012), and Ritchi et al. (2020).

The focus of prior research on the dichotomy of textual descriptions and visual representations in diagrams and outcome measures comes with important limitations: First, there are alternatives for the visual representation of risks and controls in business processes. We can roughly distinguish extensions of the primary notation and secondary notation. Extensions of the primary notation define new visual elements. For instance, Krishnan et al. (2005) developed a process-oriented ontology to improve data reliability and suggested new symbols for RIC elements. Also, Strecker et al. (2011) defined new elements in order to support IT risk assessment in processes. Conversely, secondary notation refers to the usage of visual cues such as coloring, annotation, or positioning (La Rosa et al., 2011a; Reijers et al., 2011a). Mueller-Wickop and Schultz (2013) developed such a secondary notation extension for financial accounting based on BPMN artifacts. However, these suggestions have not been empirically validated.

Second, prior research has focused on performance outcomes measured by surface and deep understanding problem-solving tasks (Gemino & Wand, 2005). This implicitly assumes that visual representation can affect rational problem solving, but it cannot explain why specific visualizations result in better understanding performance than others. We thus focus on the mechanisms that explain these differences. In this context, we use the dual-process theory of information processing (Slovic et al., 2002; Slovic et al., 2005), which emphasizes that information representation has an impact on both analytical and intuitive processing. While analytical information processing is responsible for the understanding and completion of rational tasks, intuitive information processing is driven by emotions and intuition and it is mostly unconscious (Evans, 2003). Moreover, intuitive information processing can support analytical tasks, as it provides an additional channel for information processing performance. However, it can also cause biases in analytical judgment and decision-making, thereby resulting in nonoptimal decisions (Hammond & Parkinson, 2009; Khatri & Ng, 2000; Lipshitz & Shulimovitz, 2007).

In this paper, we contribute to research on conceptual models by investigating how intuitive stimuli affect the analytical assessment of RIC information in business process models. In addition, we follow the call of Browne and Parsons (2012) and explore the impact of framing effects and related cognitive biases on conceptual modeling in the context of risk assessment. More specifically, we address the following research questions:

RQ1: How does the representation format of RIC information in BPMN affect the risk assessment of operational risk managers?

RQ2: How does the representation format of RIC information in BPMN affect the control activities of operational risk managers?

To answer these research questions, we develop a theoretical argument and corresponding hypotheses based on cognitive theories. We test these hypotheses via an online experiment (N = 166). Our results reveal that the secondary notation, color, has an effect not only on risk assessment but also on control activities. Furthermore, we do not find evidence for biases in relation to intuitive cognitive processes and risk perception when associative color highlighting is used.

The paper is structured as follows. First, we outline the theoretical framework of our study and provide an overview of RIC representations in business processes, followed by the development of our hypotheses on the analytical and intuitive processing of RIC information. Next, we describe the design of the experiment and the results. We discuss our findings and emphasize the implications for research and practice before concluding with a reflection on limitations and a summary of contributions.

## 2 Background

This section presents the theoretical background of our research. We first provide a general overview of the role of operational risk managers and their tasks and then outline the different notions of primary and secondary notation and address how they have been discussed in prior research. This is followed by a discussion of cognitive theories on information processing and their implications for organizational decision-making.

## 2.1 Operational Risk Management

Organizations manage risks for several reasons. First, risk management provides several benefits, including increased firm value (Krause & Tse, 2016) and performance (Gordon et al., 2009). Second, risk management and related concepts such as internal controls are also enforced by legislation (e.g., SOX, 2002, Section 302). Typically, risk is anchored at various levels within an organization. While terms such as “enterprise” or “organizational risk management” refer to a company-wide approach to identifying, assessing, and managing risk (Kleffner et al., 2003). We focus specifically on operational risk management at the process level and neglect strategic risk management, which examines the aggregating and weighting of broad risk types for decision-making by top management (Bromiley et al., 2015).

Frameworks released by the Committee of Sponsoring Organizations (COSO) and the International Organization for Standardization (ISO 31000:2018) support risk management activities. Over the last few years, the COSO Enterprise Risk Management— Integrated Framework has become the dominant standard (Hayne & Free, 2014). According to this framework, risk management activities are conducted at all levels, from the chief executive officer—who is ultimately responsible—down to the personnel accountable for the execution of enterprise risk management (COSO, 2004, 2013). Those responsible at an operational level of risk management are typically line managers with a background in accounting or operations management (Soin & Collier, 2013). We refer to these individuals as operational risk managers—a role supporting “risk management processes via ad hoc analyses to stimulate risk thinking and creativity in risk-response development” (Stephen, 2001).

Operational risk managers are responsible for a variety of tasks, with risk assessment and control activities (COSO, 2013) being arguably the most critical examples (similar to risk analysis and risk treatment in ISO 31000:2018). The risk assessment task requires the identification and analysis of risks and their implications. In this context, risks are defined as the possibility that an event will occur and negatively affect the achievement of objectives (COSO, 2013). Control activities refer to the selection and development of control activities that contribute to the mitigation of risks (COSO, 2013).

Business process models are often used to support risk assessment and control activities, and their effective usage by operational risk managers builds on several prerequisites. First, the analysis of risks in a process model requires developing a risk understanding. This includes the identification of the likelihood of risk events and their consequences. Second, the operational risk manager must be able to determine how risks are managed. This control understanding requires knowledge of existing risks in combination with the effects of existing controls on these risks. To that end, control understanding requires risk understanding. Third, risk managers have to improve the process by developing new control activities. This risk management task requires higher-order thinking (Norris & Ennis, 1989; Weiss, 2003). Fourth, subjective risk perception is the basis for determining whether the control situation needs to be improved. According to Bromiley et al. (2015), objective and subjective risk can differ substantially, and decisions are often made based on beliefs rather than on objective measures. Therefore, perceptional biases can influence decisions in relation to control activities. Each of these four prerequisites must be addressed carefully in order for risk assessment and control activities to be effective.

## 2.2 Representation of Business Processes for Risk Assessment

Internal controls address operational risks embedded in business processes. Several proposals have been made to leverage insights from BPM and business process modeling for the assessment of RIC information (Bai et al., 2013; Rosemann & zur Muehlen, 2005). Business process models are specific visual representations of some features of a specific realworld domain (Bera, 2012; Burton-Jones & Weber, 2014). This representation typically contains visual depictions of process steps, agents, actors, roles, and artifacts that together constitute a business process (Curtis et al., 1992). Semi-formal visual notations such as BPMN are used to facilitate communication among analysts and domain experts by establishing a shared understanding of organizational business processes (Curtis et al., 1992; Dumas et al., 2018; Recker & Dreiling, 2011). BPMN is an official standard of the Object Management Group and the most prominent notation in this domain (OMG, 2012); it does not include notational elements for risks and control, but it does provide extension mechanisms, which can be defined on the level of the primary notation and the secondary notation.

Table 1. Extensions for RIC Analysis Tasks in Process Models, by Author(s), in Alphabetical Order

<table><tr><td>Author</td><td>Focus</td><td>Grammar</td><td>Notation</td><td>Mechanism</td><td>RIC information</td><td>RIC Symbols</td></tr><tr><td>Cope et al. (2010)</td><td>Risk extensions</td><td>BPMN</td><td>Primary notation</td><td>Definition of metamodel extensions</td><td>Risk severity, transitional probabilities,</td><td>Not included</td></tr><tr><td>Krishnan et al. (2005)</td><td>Data reliability of AIS</td><td>Unspecific (BPMN example)</td><td>Primary notation</td><td>Development of a process-oriented ontology.</td><td>Error classes at risk, control error classes covered, general ledger accounts target error classes</td><td>Loosely based on BPMN (e.g., circle, oval, dashed square).</td></tr><tr><td>Mueller-Wickop &amp; Schultz (2013)</td><td>Financial Audits</td><td>BPMN</td><td>Secondary notation</td><td>BPMN extension for financial statement line items</td><td>Account, credit/debit, balance, account entries</td><td>BPMN elements (group, text annotation, and data object)</td></tr><tr><td>Radloff et al. (2015)</td><td>Process audits</td><td>EPC</td><td>Primary notation</td><td>Empirically grounded extension (laboratory experiment)</td><td>Control objective, risk, detective control means, preventive control means</td><td>New symbols (checked box, exclamation mark, magnifying glass, shield)</td></tr><tr><td>Sadiq et al. (2007)</td><td>Control objectives</td><td>Formal Contract Language (FCL)</td><td>Primary notation</td><td>Connection of control models and BPM via control tags.</td><td>Resource, data, time, flow</td><td>New symbols (stick figure, letter d, clock, arrow)</td></tr><tr><td>Schultz &amp; Radloff (2014)</td><td>Process audits</td><td>BPMN</td><td>Primary notation</td><td>Empirically grounded extension (laboratory experiment)</td><td>Control means (preventive, detective, manual)</td><td>New symbols (magnifying glass, shield, and hand)</td></tr><tr><td>Sienou et al. (2007)</td><td>Business process risks</td><td>Unspecific (EPC elements used)</td><td>Primary notation</td><td>Definition of metamodel and modeling language</td><td>Risk, risk situation, event, risk factor, handling activity</td><td>Mainly reused EPC symbols (e.g., ellipse, rounded rectangle, hexagon)</td></tr><tr><td>Strecker et al. (2011)</td><td>IT risk assessment process</td><td>Multi-perspective enterprise modeling (MEMO)</td><td>Primary notation</td><td>Definition of metamodel extensions</td><td>Risk, assignment, probability, measure, measure impact</td><td>New symbols (circle, exclamation mark, question mark, rectangle)</td></tr></table>

The first stream of research on risk extensions focuses on primary notation elements (Green & Petre, 1996) such as symbol sets and shapes. The definition of such additional elements requires a formal definition of semantics (Figl, Recker et al., 2013; La Rosa et al., 2011b; Recker, 2013). Krishnan et al. (2005) develop a process-oriented ontology of an accounting information system to specify requirements for data reliability assessment, while Strecker et al. (2011) define the RiskM metamodel based on Frank’s (2008) multiperspective enterprise modeling (MEMO) approach. Additionally, Sienou et al. (2007) support risk and process management with a risk modeling language, and Sadiq et al. (2007) propose a formal contract language (FCL) in order to provide compliance with rules and regulations. Cope et al. (2010) define execution semantics for BPMN with formal risk extensions, concentrating on the definition of elements, the specification of attributes, and the relations between elements; however, they do not proffer any visual representations of these elements. Schultz and Radloff (2014) and Radloff et al. (2015)

define a formal control extension for auditing purposes, using BPMN and EPCs, respectively. They also report experimental evaluation results suggesting that the identification of RIC information is faster in models with extension elements. These different works propose extension elements for risk (severity, probability, factors, impact), errors (at risk, covered, ledger relevant), and controls (objectives, preventive, detective, manual, assignment).

A second stream focuses on mechanisms of secondary notation such as layout, color highlighting, annotations, and labeling (e.g., La Rosa et al., 2011a; Mendling et al., 2010; Reijers et al., 2011b). Benefits of such secondary notation result from additional visual cues that support understanding of the process model. They are not part of the formal notation (Green & Petre, 1996) and do not affect the semantics of the grammar constructs in the process model. The only publication on secondary notation extensions for risk assessment is Mueller-Wickop and Schultz (2013), who examine the information requirements of business process auditors. Using expert interviews, they identify a need for the visual representation of financial statement line items and define a corresponding extension for BPMN, using secondary notation. To that end, the existing symbols for group, text annotation, and data object were modified to represent financial statement line items.

Table 1 summarizes the different process model extensions employed to support RIC information. We note the following: First, most research on risk extensions for process models centers on the primary notation. Second, BPMN as the de facto standard is the preferred modeling language for these works. Third, extensions mostly introduce representations for risks and controls, including question and exclamation marks, magnifying glasses, colors, and annotations. Fourth, empirical evidence on the effectiveness of the extensions is scarce and partially inconclusive, so further research is required to understand how RIC extensions influence analytical and intuitive information processing. We shall elaborate on this aspect in the following section.

## 2.3 Cognitive Theories on Information Processing in Visualizations

In this section, we introduce theories that explain the effects of notation on the ability to process information. Cognitive research is instrumental in investigating the effectiveness of risk management using business process models with RIC representations. Prior research on conceptual models has largely focused on analytical task performance dimensions (Gemino & Wand, 2004; Wand & Weber, 2002), which is in line with classical psychological research on the cognitive processes involved in decision-making (Evans, 2008) and problem solving within an organizational context (Akinci & Sadler‐Smith, 2012).

Cognitive load theory is a theoretical framework that builds on the human limitations of working memory capacity, which in turn impedes the performance of process model understanding in certain conditions (Bera, 2012; Figl, Recker et al., 2013; Mayer, 2009; Recker & Dreiling, 2011; Recker et al., 2014). Three types of cognitive load are distinguished:

Intrinsic cognitive load refers to the inherent level of difficulty. For instance, it is easier to aggregate two numbers than to solve a differential equation. Similarly, higher-order thinking requires a more intrinsic cognitive load than simpler thinking forms such as a recall task.

Extraneous cognitive load refers to the presentation of the information. Visual cues can make information more accessible and, therefore, reduce the extraneous load.

Germane cognitive load refers to the processing effort required for constructing permanent schemas. This type of cognitive load supports the effective completion of tasks.

While the intrinsic load cannot be changed, tasks can be designed to reduce extraneous load to a minimum and promote germane load (Cierniak et al., 2009; DeLeeuw & Mayer, 2008). In the context of our study, this means that RIC representations should be designed as clearly as possible, to reduce extraneous load and thus support risk management tasks.

Visual cues are highly effective, but they can also create decision-making biases. Evans (2003) and Kahneman (2011) postulate “two minds in one brain” with two fundamentally different information processing systems. Corresponding approaches that address this phenomenon are commonly referred to as the dual-process theory of information processing (Evans, 2003; Evans, 2008; Stanovich, 2004). The existence of these separate systems is supported by neuroscience, showing that different brain regions are activated according to which type of process takes control of behavior (Evans, 2011). Information processing in the first mode (System 1) is largely unconscious, contextually dependent, intuitive, automatic, associative, implicit, and fast. In contrast, the second mode (System 2) is conscious, contextually independent, analytical, explicit, rule based, and relatively slow (Evans, 2008; Slovic et al., 2005).

The systems have different origins and require different cognitive effort. System 2 is considered evolutionarily recent, as it is distinctively human. It requires the ability to abstract and allows us—unlike animals—to apply normative reasoning and consequential decision-making by imagining possible future outcomes that result from our actions. System 2 requires the limited resources of working memory for cognitive information processing and is driven by the individual’s general intelligence as well as the capability of experimental learning (Evans, 2011; Frankish & Evans, 2009). System 1, in contrast, is based on intuition. Both systems do not necessarily operate separately. Lipshitz and Shulimovitz (2007) found that loan officers in a large Israeli bank determined the credit rating of loan applicants based on both analytical and intuitive aspects. They also identified intuitive reactions to the application as more valid indicators of creditworthiness. Similar observations have been made for CEOs of oil companies, who appear to rely on an interplay between rational analysis and intuition for their decisionmaking (Woiceshyn, 2009).

The affect heuristic provides a theoretical explanation for intuitive processing. In human minds, objects and events are tagged with different degrees of affect, which establishes a connection with emotions and feelings based on previous experiences. During judgment and decision-making, an individual consults the affect pool that contains all the positive and negative tags consciously or unconsciously associated with visual cues (Evans, 2003; Slovic et al., 2002). At this stage, it is possible that a rational decision-making process in System 2 is influenced by visual cues processed in System 1. In fact, rational information processing in System 2 is often not possible without the rapid processing of visual and language cues of System 1 (Evans, 2011); instead, System 1 provides an unconscious support system offering pragmatic solutions for the relevant context based on feelings and intuition (Evans, 2011). The individual can hardly control the initial affective impression, as the tags create mental shortcuts that cannot be easily disabled. This thinking mode establishes the affect heuristic, which is extremely efficient and requires almost no mental effort (Evans, 2003; Slovic et al., 2005). Individuals use the affect heuristic automatically to deal with complexity and save cognitive effort for System 2 processing, which means that rational judgment is also influenced by System 1. In the context of our study, System 1 creates an initial response to the visual cues in a given representation, thereby influencing the extraneous cognitive load in System 2. This effect explains why some visualizations result in a better task understanding than others.

Research in the area of business process management has investigated the key factors of model understanding and found that representational factors play an important role (Figl, 2017; Recker, 2013). The number of diagram elements that a human mind can comprehend at any one time is limited by the capacity of the working memory (Moody, 2009), and when this limit is exceeded, a state of cognitive overload is reached, and comprehension degrades rapidly (Baddeley, 2012). For this reason, it is the aim of research in this area to reduce extraneous cognitive load, i.e., an unnecessary cognitive load that results from ineffective representation. In addition to cognitive load theory, the theory of effective visual notations provides a framework for analyzing symbols and symbol sets based on properties such as semantic transparency and perceptual discriminability (Moody, 2009). These properties describe how clear (i.e., transparent) the meaning of a model element is to a user, and how easy it is to distinguish (i.e., discriminate) elements with different meanings from each other. Both of these factors have been found to improve task performance (Figl, 2017; Figl, Mendling et al., 2013; Recker, 2013).

Risk assessment and control activities can be supported using visual representations such as process models, which can be extended by visual cues such as colors or symbols to convey RIC information (see section 2.2). Colors are rapidly recognized at the preattentive stage in which the brain collects all information about the basic features of the observed object. This information is then integrated, such that the whole object is perceived (Treisman & Gelade, 1980). The speed of this recognition has the advantage that colors help objects “pop-out” immediately in a representation, which then draws attention and stirs information processing into moving in a particular direction. In addition, colors are ubiquitous perceptual stimuli that convey meaning as postulated in color-incontext theory (Elliot & Maier, 2012). This theory explains relations between color, affect, cognition, and behavior, with colors influencing psychological functioning as part of intuitive information processing. The meaning of colors can be learned (stereotypically, girls are dressed in feminine pink and boys in masculine blue) or be part of biological processes (Elliot & Maier, 2012); the color red, for instance, seems to have evolutionary characteristics as a warning color (Stevens & Ruxton, 2012).

Beyond color, there are also other visual cues that can influence rational decision-making in System 2. This includes learned symbols such as quotation marks and warning triangles that commonly refer to risks and associated meanings that are salient for information processing. For instance, visual cues have been successfully applied in public health research concerning tobacco warnings (Hammond, 2011; Hammond & Parkinson, 2009). Pictures that illustrate the negative consequences of smoking elicit strong emotional responses such as disgust and anxiety, thus increasing the perceived risk of tobacco and triggering an avoidance reaction. In contrast, a warning text that explains the negative effects of smoking does not trigger the same shortcuts and is less effective (Hammond, 2011; Hammond & Parkinson, 2009). These examples emphasize that intuitive information processing can influence risk assessment, and visual cues might improve effectiveness or create biases.

We conclude that the assessment of RIC information requires cognitive reasoning and is therefore part of the analytical information processing in System 2. However, the rapid processing of visual cues presumably establishes a potential influence of the intuitive System 1. It remains unclear which cues stimulate analytical and intuitive information processing and whether these visual signals bias the risk assessment.

## 3 Hypothesis Development

So far, we have outlined that colors and symbols can be used to support the assessment of RIC information in process models. Two types of information processing are involved. First, System 2 is associated with the rational processing of RIC information in process models, which requires working memory for assessing risks and control activities.

![](/api/attachments/XTYPU72P/fulltext/images/4e8e6b408d853100351c13c1222f9b088308ea5fce6c395d51099045568d6251.jpg)  
Figure 1. Effect of Representation on Analytical and Intuitive Information Processing

Second, intuitive processing of System 1 can become involved when visual cues trigger cognitive shortcuts that influence operative risk management activities. While the analytical impact on the understanding of performance is based on manipulating cognitive load, intuitive processing can be explained with the affect heuristic.

In accordance with dual-process theory, we assume that intuitive information processing represents an additional path outside the working memory (Evans, 2011). Information cues containing RIC information may trigger intuitive information processing when they are reconciled with the affect pool (see section 2.3), which can be regarded as a further unconscious part of the long-term memory, as the individual has no control over or knowledge of its content. Depending on the information stored in the affect pool, an emotional response can emerge, and this can trigger analytical information processing or solely intuitive decisionmaking. Figure 1 summarizes the research framework.

## 3.1 Influence of Primary Notation Extensions on RIC Understanding and Improvement

We develop hypotheses on the effect of primary and secondary notation in the context of RIC based on the principles of the theory of effective visual notations (Moody, 2009). First, we consider primary notation, which includes symbols for RIC information that extend the BPMN set of elements. If they do not violate the principle of semantic transparency, these symbols can be perceived directly and easily learned (Moody, 2009; Petre, 1995). Research on icon design suggests that desired behavior is facilitated when the visual design matches a user’s mental image (Kosslyn et al., 2006); for this reason, the choice of a suitable symbol is highly important. Only if a semantically transparent symbol establishes an association with the right mental image in the affect pool does it trigger an affect that influences information processing (as depicted in Figure 1). We postulate that adequate RIC symbols improve understanding performance thanks to intuitive recognition and the support of the analytical model. As a result, the extraneous cognitive load is reduced and the model is easier to understand; however, this requires that RIC representations follow the theory of effective visual notations by ensuring semantic transparency and perceptual discriminability. Otherwise, the RIC representation may distract or confuse the user, resulting in a higher extraneous cognitive load and potentially reduced understanding performance. This means that users of the process model with adequate RIC elements will gain a better understanding of the risks in the process model. Formally, we state:

H1a: Conveying RIC information in process models by extensions of the primary notation (additional RIC symbols) improves risk understanding compared to models without these extensions.

The RIC elements will also support a better understanding of control activities. This task is more complex because it requires the concurrent processing of risks and control elements. Formally, we state:

H2a: Conveying RIC information in process models by extensions of the primary notation (additional RIC symbols) improves control understanding compared to models without these extensions.

Ultimately, we postulate that the improved understanding of process models with RIC symbols also facilitates the development of new controls to improve the risk situation. We regard this as higher-order thinking, as it requires a deep understanding of the business process and the application of reasonable, reflective thinking that focuses on the future. We thus state:

H3a: Conveying RIC information in process models by extensions of the primary notation (additional RIC symbols) improves the identification of control improvements compared to models without these extensions.

## 3.2 Influence of Secondary Notation Extensions on RIC Understanding and Improvement

An alternative to the extension of BPMN’s primary notation is the inclusion of secondary notation elements that convey RIC information—in particular, colors. Coloring has been suggested as a mechanism to improve the perceptual discriminability of modeling elements (Reijers et al., 2011b; Te’eni, 2001). Additionally, colors can be used to convey semantic meaning without changing the formal notation (e.g., risks can be visualized in red, to strengthen semantic transparency). Previous research suggests that color highlighting can reduce visual searching in a diagram, with the effect of increased understanding efficiency (Kummer et al., 2016; Petrusel et al., 2016). Presumably, secondary-notation cues can also improve the understanding performance of RIC. More specifically, we postulate that colors can be used in such a way that the extraneous cognitive load is reduced.

Color-in-context theory provides an explanation for why colors influence intuitive information processing (Elliot and Maier, 2012) toward an immediate understanding of the RIC elements. The affect pool is filled with socially learned and biologically acquired color associations that result in an affect supporting analytical information processing (Figure 1). Consequently, less effort for visual search is required, and therefore less extraneous cognitive load is generated. This means that less cognitive capacity is required for developing the analytical model, and this capacity becomes available for other information processing, which eventually results in improved understanding performance (Reijers et al., 2011a). These observations are consistent with Moody’s (2009) principle of perceptual pop-out, and again, we postulate that this effect influences risk understanding performance: We state:

H1b: Conveying RIC information in process models by secondary notation elements (RIC colors) improves risk understanding compared to models without these elements.

Furthermore, we argue that the RIC representation influences understanding performance at different levels, including the understanding of risk and controls as well as of the effect of controls on these risks. However, unlike the symbols, the effects of colors on cognitive information processes are ambiguous. According to Elliot et al. (2007), the association of the color red with warnings and the marking of errors can stimulate an avoidance motivation that impairs cognitive performance. In our context, we use the color red to alert the user and support related risk avoidance. This semantic meaning allows for an intuitive interpretation of the colored elements and improves understanding, while the pop-out effect also reduces search time. The latter relationship is in line with previous findings suggesting a positive impact of the color red on cognitive tasks requiring detail-oriented work (Mehta & Zhu, 2009). A red-green color scheme seems particularly suitable because while red is associated with avoidance motivation, green is the chromatic contrast to red, carrying the approachoriented meaning “go” because of its use in traffic lights (Elliot et al., 2007). Therefore, we postulate a positive effect of colors on performance. Formally, we state:

H2b: Conveying RIC information in process models by secondary notation elements (RIC colors) improves control understanding compared to models without these elements.

The anticipated effects regarding higher-order thinking are similar. In addition to the effects outlined to derive H2b, we also need to consider the influence of red and green colors on creative thinking. The common understanding is that red creates an avoidance reaction that impairs creativity, while green facilitates creativity (Lichtenfeld et al., 2012; Mehta & Zhu, 2009). However, according to Rook (2014), the context is highly relevant, as red can stimulate creative thinking in approach settings. In our study, participants are encouraged to approach the risks in the process models and find new ways to reduce their negative consequences. Thus, we postulate a positive effect of RIC colors on higher-order thinking tasks. We thus state:

H3b: Conveying RIC information in process models by secondary notation elements (RIC colors) improves the identification of control improvements compared to models without these extensions.

## 3.3 Influence of RIC Representations on Subjective Risk Assessment

A particularly relevant aspect concerning risk management is subjective risk perception (Bromiley et al., 2015). While the objective risk relates to analytical risk calculation, the subjective risk refers to the perception that the control situation needs to be improved and is primarily based on beliefs (Bromiley et al., 2015). Therefore, risk perception is strongly influenced by information processing in System 1. Figure 1 shows this influence as the direct relationship between the affect and information processing. Previous studies have focused on the performance of analytical, deliberate information processing and, to the best of our knowledge, no study has examined how visual stimuli can bias a user’s risk perception of conceptual models. We address this research gap and explore how different RIC representation formats influence risk perception in accordance with the affect heuristic.

As outlined above, previous research suggests that pictures illustrating the negative consequences of smoking elicit strong emotional affects such as disgust and anxiety, which increase the perceived risk of smoking and trigger an avoidance reaction. In contrast, a warning text that explains the harmful effects of smoking does not trigger the same affective shortcuts and is less effective (Hammond, 2011; Hammond & Parkinson, 2009). This means that textual risk information, and percentages in particular, appear to have limited influence on subjective risk perceptions. In contrast, visual stimuli can be used to trigger shortcuts that increase risk perception (Slovic et al., 2005). The inclusion of risk symbols adds additional messages compared to a purely textual description. Traffic or warning symbols, for instance, can act as stimuli to increase risk perception (Chen et al., 2015). We postulate that these findings can be applied to RIC symbols in process models, resulting in an affect that increases the subjective risk perception. Formally, we state:

H4a: Conveying RIC information in process models by extensions of the primary notation (additional RIC symbols) increases perceived risk compared to models without these extensions.

Colors are also strong risk stimuli in their own right, and specific colors are often used to indicate warnings, suggesting they are tagged to feelings of higher alertness (Griffith & Leonard, 1997; Riley, 2014). Griffith and Leonard (1997) have shown in experiments that red leads to the highest perceived risk. This notion is in line with Westinghouse’s (1981) taxonomy that ranks red as the color with the highest risk perception (followed by orange and yellow). A possible explanation is that these colors are associated with basic information in traffic signals worldwide, thereby leading to a social learning effect in the risk heuristic (Riley, 2014). In addition, evolutionary development could play a role, as even animals perceive long-wavelength colors such as red as riskier (Stevens & Ruxton, 2012). The effect is particularly strong when combined with loss-framed messages matching the risk focus of our study (Gerend & Sias, 2009). In this regard, we state:

H4b: Conveying RIC information in process models by secondary notation elements (RIC colors) increases perceived risk compared to models without these elements.

## 4 Research Method

We used a controlled laboratory experiment to test our hypotheses. Experiments are an established method in modeling research for investigating causality (e.g., Burton-Jones et al., 2009; Figl, Mendling et al. 2013; Parsons, 2011; Recker, 2013). So far, there is limited insight into the effectiveness of RIC information in process models, and our primary objective was thus to maximize internal validity.

## 4.1 Design

We selected a crossover design in which each participant received a sequence of different treatments because this approach requires fewer experimental participants compared to a between-subject design (Vegas et al., 2016). Moreover, the crossover design further strengthens reliability in that the influence of confounding covariates is reduced because each participant serves as his/her own control and can be considered in the statistical analysis. A crossover design also provides increased experiment sensitivity because it can still control between-subject variations (Jones & Kenward, 2003). We followed the design guidelines established by Vegas et al. (2016) and applied a factorial crossover design, in which the number of periods equals the number of treatments. The design choice allows each participant to receive each treatment exactly once (Vegas et al., 2016). The within-group factor (representation) with three levels (base model, base model with colors, and base model with symbols) acts as the treatment and is measured in three periods in which participants assess the risk and the control activities of a different process. In this way, the process represents a blocking variable with three levels (online shop, insurance claim, and goods receipt).

Order effects are particularly problematic in repeated measure experiments (Vegas et al., 2016). For instance, there is the threat that the first representation will cause an anchor effect bias that influences the perception of the following treatments (McNicol & Pennington, 1973). Also, learning effects might occur. Crossover designs address these threats by altering sequences of treatment and blocking variables. We selected a design balanced for carryover effects in which each treatment follows each other treatment the same number of times (Kuehl, 2000; Vegas et al., 2016). For three treatments, this implies six treatment sequences in which each treatment follows each other treatment exactly three times (see Table 4). In addition, we varied the sequence of the blocking variable to avoid possible carryover effects in relation to the process model order. This yielded six times three sequences altogether.

As mentioned above, the factor representation had three levels. The first was the base model, the second the base model with extra symbols for highlighting risks and internal controls, and the third the base model with additional colors for highlighting risks and internal controls. Instantiation validity refers to the extent to which a design feature in an artifact is faithful to a design principle (Lukyanenko et al., 2014, 2015). Our hypotheses suggest an effect of colors and symbols on RIC performance and perception. Therefore, we need to justify that our specific treatment choices for colors and symbols in the experiment are consistent with more general design principles outlined in the hypotheses development section. To this end, we now explain why we regard the selected colors and symbols as adequate representations of risk and internal controls.

The base model serves as a control and contains the same annotation for risks and internal controls in black and white only. The model does not contain RIC symbols (exclamation marks and magnifying glasses).

The base model with symbols includes icons for risk (triangle with exclamation mark) and controls (magnifying glass with a checked item). Previous research suggests that combined visual cues are more effective than isolated cues (Zender & Mejia, 2013). For this reason, we selected icons containing two visual cues from prior research. Radloff et al. (2015) suggest using the symbol of an exclamation mark for risks and a magnifying glass for detective controls. Strecker et al. (2011) also use an exclamation mark to represent RIC information, and Schultz and Radloff (2014) use a magnifying glass for detective controls (see Section 2.2).

We believe that these symbols are useful in supporting RIC information. To improve effectiveness, we combined the exclamation mark with the symbol of a warning triangle—a universal symbol for risk included in ISO 7010 as a general warning sign (W001). It is also common in software applications (Unicode: U+26A0), and many countries use it as a traffic sign and as a portable hazard warning sign for car breakdowns. The magnifying glass is frequently used to indicate search functionality in software applications (e.g., Google, Windows 10, Unicode U+1F50D). The magnifying glass is also associated with detective fiction—mainly because of its association with Sherlock Holmes—indicating close observation as a key skill (Field, 2013). To that end, the magnifying glass often symbolizes the detection of materialized risks, for instance in relation to fraud (e.g., PWC, 2018). In order to ensure that the participants would not associate the magnifying glass with zooming, we combined the symbol with the “checkmark” (or “tick”) (Unicode: U+2713), a symbol commonly used to indicate that an item has been dealt with. Together, the meaning represents a detective control (search for items that have been dealt with). The additional icons extend the formal notation and convey semantic meaning in line with what is included in textual annotations.

The base model with colors uses consistent colors with an intuitive interpretation (risks are always red and controls are always green), which is in line with previous research indicating that red results in a particularly highrisk perception, while green is the complementary color of red and not associated with risk (Griffith & Leonard,

1997; Riley, 2014). The color combination is common in risk visualization around the world (e.g., in traffic lights) and supports the model’s semantics, as the colors convey meaning within the model (see Sections 3.2 and 3.3).

Representations must be information equivalent in avoiding experimental biases. Two models are informationally equivalent if all of the information in one model is inferable from the other, and vice versa (Larkin & Simon, 1987; Siau, 2004). We maintain informational equivalence in all treatment variations (base model, base model with color, base model with symbols) by using textual annotations explaining the risks and internal controls as well as the financial implications. Consequently, the colors and symbols provide additional visual cues of information already included, albeit these additional cues may improve perceptual discriminability between different types of model constructs (Figl, Mendling et al. 2013; Moody, 2009).

Treatments were tested in two pretests with 131 and 125 participants, respectively. Based on the results, the use of colors was intensified after the first pretest (in the pretest, only the elements’ edges were colored compared to color-filled elements used in the actual experiment). The second pretest resulted in a reduction in visual cue combinations to simplify the experimental design. Table 2 illustrates the different representation treatments, using the goods receipt process.

## 4.2 Measures

In order to provide for external validity, we aligned the operationalization of the dependent variables with the COSO framework tasks for risk identification and control activities. First, we measured risk understanding, which is the ability to determine the existing risks in the BPMN model. Participants responded to five calculation tasks concerning the likelihood of risk events and their potential damages (e.g., “The risk concerning packing can cause damage of \$ .”). We regard this measure as objective because exactly one correct answer exists.

The task control understanding is more demanding in terms of cognitive load because the controls act as a response to reduce selected risks in the model, which means that several elements have to be considered simultaneously, including the risk, the related control, and the remaining risk (e.g., “The internal controls reduce the anticipated cost for making a wrong decision upon acceptance by \$ ”). Again, the participants completed five understanding tasks, and the measure is objective, as exactly one correct answer exists. These task types and the corresponding performance measures are frequently used in studies of domain understanding from conceptual models (Burton-Jones & Meso, 2008; Gemino & Wand, 2005; Recker & Dreiling, 2011; Recker et al., 2014). Both understanding tasks were presented as open questions to avoid guessing.

Table 2. Manipulation of the Representation Exemplified, Using the Goods Receipt Process  
![](/api/attachments/XTYPU72P/fulltext/images/02157dfffc3d6d1fccb3c265cd9d2b2519c94439433bc35b487aeb3a0e145f06.jpg)

Table 3. Definition and Operationalization of the Dependent Variables

<table><tr><td>Dependent Variable</td><td>Origin</td><td>Definition</td><td>Measurement</td></tr><tr><td>Risk understanding</td><td>Based on common risk assessment practices (Gelinas &amp; Dull, 2010, p. 219)</td><td>Ability to correctly understand the risks included in a BPMN model</td><td>Performance index: Score based on five questions addressing risk elements in the BPMN model</td></tr><tr><td>Control understanding</td><td>Based on common risk assessment practices (Gelinas &amp; Dull, 2010, p. 219)</td><td>Ability to correctly understand the controls in a BPMN model</td><td>Performance index: Score based on five questions addressing control elements in the BPMN model</td></tr><tr><td>Control improvement</td><td>Self-developed</td><td>Ability to apply higher-order thinking to improve the controls in the model</td><td>Performance index: Score based on up to five control improvement ideas</td></tr><tr><td>Perceived risk</td><td>Adapted from Sitkin and Weingart (1995)</td><td>Subjective perception that the controls in the model adequately address the risks</td><td>Psychological construct (latent variable) based on 4 question items measured with 7-point- bipolar scales</td></tr></table>

Next, we measured control improvement. Participants were asked to write down up to five ideas on how risks in the process could be further reduced. This type of task requires higher-order thinking because it combines knowledge of risks, controls, and processes, as much as critical and reflective thinking with a focus on what to do (Norris & Ennis, 1989; Weiss, 2003). A coding scheme was developed in which participants received a score of 1 for every idea that aimed at a specific part of the related process and was suitable to reduce the overall risk. A score of 0.5 was assigned if the idea was not specific enough but still suitable to reduce risk. Ideas that were not suitable for risk reduction received a score of 0. The sum of these scores operationalizes the construct control improvement. Two researchers (one author and a research assistant not previously involved in the project) applied the coding scheme independently, resulting in 85.81% consistent results. The remaining differences were discussed until both researchers reached agreement. Definitions and measures for the dependent variables are outlined in Table 3, while models and questions are provided in Appendix A.

Finally, the participants assessed the risk situation of the process. In contrast to the previous tasks, this variable reflects the user perception of whether the risks in the process are adequately addressed. We refer to this variable as perceived risk. Participants answered four questions on the risk situation displayed in the process model. The questions were adapted from the perceived risk measure developed by Sitkin and Weingart (1995) and measured on 7-point bipolar scales (e.g., “How would you characterize the insurance claim process? 1 = very well controlled to 7 = very risky). Appendix A contains the research instrument with all question items.

In order to determine the validity and reliability of our dependent variables, we first distinguish between performance indexes (risk understanding, control understanding, and control improvements) as well as psychometric constructs (perceived risk). Performance indexes are common in experiments with risk understanding (Asare et al., 2000) or cognitive information processing (Bodart et al., 2001; Gemino & Wand, 2005; Kummer et al., 2016; Recker & Dreiling, 2011). Given that the questions directly related to the risks and control activities in the processes, we conclude that face validity is adequate. Performance questions were developed by two experienced researchers with expertise in this area and tested in multiple rounds of pretesting with 131 and 125 participants, which led to changes that were again tested with 15 academics before data collection commenced. The psychometric construct of perceived risk developed by Sitkin and Weingart (1995) is a latent variable based on four reflective question items. The unstandardized latent variable scores were determined using confirmatory factor analysis in SmartPLS 3 (Gefen & Straub, 2005). The findings show a Cronbach’s alpha of 0.70 and composite reliability of 0.82, suggesting that indicator reliability is provided.

## 4.3 Materials

We used two sets of materials in our experiment. The first set of materials contained questions referring to numbers shown on two Ishihara color blindness plates (green on red and red on green). Participants had to answer these questions correctly in order to proceed. Next, we collected demographic information from the participants, including country of origin, familiarity with the process modeling grammar BPMN (Recker, 2010), and business process management.

The second set of materials comprised a general explanation of risks and controls followed by three process diagrams, one for each trial. The order of the process and the representation treatment were randomly assigned to the participant. Consequently, each participant received one out of six possible orders for the three representation treatments (e.g., model with colors, base model, and model with symbols), and each participant received the three process models in one of six possible orders (e.g., 1. online shopping process, 2. goods receipt process, 3. insurance claim process). Altogether, 18 different combinations of representation and process model order were possible (Table 4).

The process models were created using BPMN grammar (OMG, 2012) because of its position as the industry standard for process modeling. To reduce model complexity as a potentially confounding variable, we kept measures regarding model size, connection, and complex behavior within a narrow range (Mendling, 2008). The models were of similar complexity (see Table 5). Additional textual descriptions explaining the process were included as annotations. The online shopping process contained in total 73 elements (including seven RIC elements), the insurance claim process 71 (including six RIC elements), and the goods receipt process 73 (including seven RIC elements).

## 4.4 Procedure

A moderate time pressure of five minutes was applied for the five risk and five control questions. A timer was displayed that began counting down 300 seconds once the participant had answered three general true/false questions on the process. These questions were included to allow the participants to become familiar with the process and were not part of the data analysis. The second timer of three minutes was used to limit the working time for the identification of possible control improvements.

The reasons that a moderate time pressure was used were threefold: First, it gave participants an indication of what was expected and ensured that they completed the experiment within the estimated time frame, which was important in order to stop them from responding in a too detailed way in response to the open improvement questions. In this way, the time limit reduced the risk of dropouts and fatigue effects, which could bias results.

Second, a time limit makes the tasks more authentic. In the real world, some kind of time pressure is usually present. For instance, the time to prepare for a meeting is limited, or other urgent matters require attention, thus reducing the available time for risk assessment and control activities. Third, the relationship between information processing performance and time pressure follows an inverted U-shape (Paul & Nazareth, 2010). Time pressure directly increases task difficulty, as the cognitive load has to be processed more quickly. Tasks without a time limit can be perceived as too easy, while very high time pressure results in stress with negative consequences on performance. Moderate time pressure has a stimulating effect on performance and supports intuitive information processing (Chuang, 2013; Rice & Trafimow, 2012).

The time limits were determined based on the pre-tests, to ensure that they challenged the participants while providing sufficient time to complete the task. Once the time was up, the timer changed color and shifted from counting down to counting up. Then, a message was displayed, instructing the participant to submit their responses. The approach simulated how time pressure often occurs in the real world and ensured that all answers were collected.

## 4.5 Participants

The experiment was conducted using a self-developed website for online experiments. Participants were recruited using Amazon Mechanical Turk (MTurk). We applied a job description filter “Accounting and Finance” and “Operations,” as these groups are the closest to the main stakeholder groups of operational risk managers. The description on MTurk stated that individuals with color blindness could not participate. Furthermore, a minimum screen size of 13-inch was required to participate. Participants were assigned randomly to one of the 18 different treatment and model order combinations, and a payout of \$4 incentivized participation.

In total, 166 MTurk workers participated in October and November 2019. Of this cohort, 41 dropped out before they completed questions for all three processes. Dropouts are common in repeated measures experiments and handling them depends on the specific circumstances. We assume that the dropouts were related to study fatigue rather than a particular treatment, process, or order and therefore consider them to be random and independent of the unobserved measurements.

The demographic statistics in Table 6 show that the sample contains almost equally male and female participants; most are US citizens (77.71%) and the majority have a degree in accounting (59.64%). In all, 68.68% stated that they had experience in BPM, but only 21.69% knew BPMN.

Table 4. Overview of the Three-Treatment Factorial Crossover Design and Three-Level Blocking Variable

<table><tr><td>Sequence</td><td>Treatment sequence</td><td>Blocking sequence</td><td>Period 1</td><td>Period 2</td><td>Period 3</td><td>Allocated participants</td></tr><tr><td>1</td><td>1</td><td>1</td><td>Treatment A; Object 1</td><td>Treatment B; Object 2</td><td>Treatment C; Object 3</td><td>9 (5.42%)</td></tr><tr><td>2</td><td>2</td><td>2</td><td>Treatment A; Object 1</td><td>Treatment C; Object 3</td><td>Treatment B; Object 2</td><td>9 (5.42%)</td></tr><tr><td>3</td><td>3</td><td>3</td><td>Treatment B; Object 2</td><td>Treatment A; Object 1</td><td>Treatment C; Object 3</td><td>11 (6.63%)</td></tr><tr><td>4</td><td>4</td><td>4</td><td>Treatment B; Object 2</td><td>Treatment C; Object 3</td><td>Treatment A; Object 1</td><td>7 (4.22%)</td></tr><tr><td>5</td><td>5</td><td>5</td><td>Treatment C; Object 3</td><td>Treatment A; Object 1</td><td>Treatment B; Object 2</td><td>8 (4.82%)</td></tr><tr><td>6</td><td>6</td><td>6</td><td>Treatment C; Object 3</td><td>Treatment B; Object 2</td><td>Treatment A; Object 1</td><td>6 (3.61%)</td></tr><tr><td>7</td><td>1</td><td>5</td><td>Treatment A; Object 3</td><td>Treatment B; Object 1</td><td>Treatment C; Object 2</td><td>7 (4.22%)</td></tr><tr><td>8</td><td>2</td><td>6</td><td>Treatment A; Object 3</td><td>Treatment C; Object 2</td><td>Treatment B; Object 1</td><td>9 (5.42%)</td></tr><tr><td>9</td><td>3</td><td>2</td><td>Treatment B; Object 1</td><td>Treatment A; Object 3</td><td>Treatment C; Object 2</td><td>7 (4.22%)</td></tr><tr><td>10</td><td>4</td><td>1</td><td>Treatment B; Object 1</td><td>Treatment C; Object 2</td><td>Treatment A; Object 3</td><td>12 (7.23%)</td></tr><tr><td>11</td><td>5</td><td>4</td><td>Treatment C; Object 2</td><td>Treatment A; Object 3</td><td>Treatment B; Object 1</td><td>8 (4.82%)</td></tr><tr><td>12</td><td>6</td><td>3</td><td>Treatment C; Object 2</td><td>Treatment B; Object 1</td><td>Treatment A; Object 3</td><td>11 (6.63%)</td></tr><tr><td>13</td><td>1</td><td>4</td><td>Treatment A; Object 2</td><td>Treatment B; Object 3</td><td>Treatment C; Object 1</td><td>10 (6.02%)</td></tr><tr><td>14</td><td>2</td><td>3</td><td>Treatment A; Object 2</td><td>Treatment C; Object 1</td><td>Treatment B; Object 3</td><td>10 (6.02%)</td></tr><tr><td>15</td><td>3</td><td>6</td><td>Treatment B; Object 3</td><td>Treatment A; Object 2</td><td>T: Symbols; Object 1</td><td>10 (6.02%)</td></tr><tr><td>16</td><td>4</td><td>5</td><td>Treatment B; Object 3</td><td>Treatment C; Object 1</td><td>Treatment A; Object 2</td><td>11 (6.63%)</td></tr><tr><td>17</td><td>5</td><td>1</td><td>Treatment C; Object 1</td><td>Treatment A; Object 2</td><td>Treatment B; Object 3</td><td>11 (6.63%)</td></tr><tr><td>18</td><td>6</td><td>2</td><td>Treatment C; Object 1</td><td>Treatment B; Object 3</td><td>Treatment A; Object 2</td><td>10 (6.02%)</td></tr><tr><td colspan="7">Note: Treatment A: base model; Treatment B: base model with colors; Treatment C: base model with symbols; Object 1: online shop process; Object 2: insurance claim process; Object 3: goods receipt process)</td></tr></table>

Table 5. Complexity of the Three Business Processes

<table><tr><td>Process</td><td>Online shopping</td><td>Insurance claim</td><td>Goods receipt</td></tr><tr><td>Activities</td><td>12</td><td>12</td><td>14</td></tr><tr><td>Gateways</td><td>7</td><td>6</td><td>5</td></tr><tr><td>Events</td><td>3</td><td>2</td><td>3</td></tr><tr><td>Flow arcs</td><td>24</td><td>22</td><td>23</td></tr><tr><td>Textual annotations</td><td>20</td><td>23</td><td>21</td></tr><tr><td>Risks</td><td>5</td><td>4</td><td>4</td></tr><tr><td>Internal controls</td><td>2</td><td>2</td><td>3</td></tr><tr><td>Elements (total)</td><td>73</td><td>71</td><td>73</td></tr></table>

Table 6. Demographic Statistics (RIC: Risk and Internal Control)

<table><tr><td>Variable (nominal)</td><td colspan="3"></td></tr><tr><td>Gender</td><td colspan="3"></td></tr><tr><td>Male</td><td colspan="3">82 (49.40%)</td></tr><tr><td>Female</td><td colspan="3">83 (50.00%)</td></tr><tr><td>Other</td><td colspan="3">1 (0.60%)</td></tr><tr><td>Citizenship</td><td colspan="3"></td></tr><tr><td>USA</td><td colspan="3">129 (77.71%)</td></tr><tr><td>India</td><td colspan="3">22 (13.25%)</td></tr><tr><td>Canada</td><td colspan="3">5 (3.01%)</td></tr><tr><td>Other</td><td colspan="3">11 (6.02%)</td></tr><tr><td>Highest Education</td><td colspan="3"></td></tr><tr><td>High school diploma or the equivalent</td><td colspan="3">14 (8.43%)</td></tr><tr><td>Trade/technical/vocational training</td><td colspan="3">23 (13.86%)</td></tr><tr><td>Professional degree</td><td colspan="3">5 (3.01%)</td></tr><tr><td>Bachelor&#x27;s degree</td><td colspan="3">93 (56.02%)</td></tr><tr><td>Master&#x27;s degree</td><td colspan="3">31 (18.67%)</td></tr><tr><td>Degree in accounting</td><td colspan="3">99 (59.64%)</td></tr><tr><td>BPM knowledge</td><td colspan="3">114 (68.68%)</td></tr><tr><td>Work experience with BPMN</td><td colspan="3">36 (21.69%)</td></tr><tr><td>Variable (scale)</td><td>Scale</td><td>Mean</td><td>St. Dev.</td></tr><tr><td>Age</td><td>No. of years</td><td>36.57</td><td>10.11</td></tr><tr><td>Years of work experience in accounting (if applicable)</td><td>No. of years</td><td>8.11</td><td>7.18</td></tr><tr><td>BPM familiarity (if applicable)</td><td>0-6 (Likert)</td><td>4.03</td><td>1.30</td></tr><tr><td>BPMN familiarity (if applicable)</td><td>0-6 (Likert)</td><td>4.62</td><td>0.79</td></tr><tr><td>RIC explanation understandable</td><td>0-6 (Likert)</td><td>5.08</td><td>0.97</td></tr></table>

The average age was 36.57 years with a relatively high standard deviation of 10.11, suggesting strong diversity. The same can be observed regarding the work experience of participants with an accounting background. The average working experience was 8.11 years, but the relatively high standard deviation of 7.18 suggests substantial heterogeneity within the sample. Those familiar with BPM and BPMN evaluated themselves as highly familiar with the topic (means of 4.03 and 4.62, respectively).

In the experiment, we explained basic risk management concepts, which included risk likelihood, expected damage, control costs, and remaining damage after a control is implemented. The text was accompanied by a control question asking if the explanation was understandable. The mean of 5.08 on a Likert scale ranging from 0 to 6 indicates that this was the case.

## 5 Results

This section presents the results of our data analysis, based on a linear mixed model. Linear mixed models are a common approach for experimental within-group design with repeated measures (e.g., Hansen & Walden, 2013; Jenkins et al., 2019) and are recommended in crossover designs in which the treatment sequence and other factors (such as the blocking variable sequence) could influence the results (Vegas et al., 2016). Moreover, unlike traditional repeated-measures ANOVA, the likelihood-based analysis of linear mixed models can handle random missing data through dropouts (Judd et al., 2017; Verbeke & Molenberghs, 2000, p. 213). Therefore, no further data were removed, and no imputation procedure was applied. However, as linear mixed models include only a single dependent variable (DV), we conducted four separate analyses (one for each DV).

We controlled for carryover effects in our experimental design through the randomization of treatment and blocking variables, as well as statistically in our analysis, by including three additional random effects per DV: The treatment sequence, the process model sequence (blocking variable), and the process model. The potential confounding impact of these variables is automatically adjusted in mixed-method analysis, and the influence of carryover effects is therefore excluded. Because of the random group assignment and the repeated measures design, we did not control for the influence of individual characteristics (e.g., BPM knowledge).

To gauge whether the sample size was sufficient, we estimated desired statistical power, using Cohen’s statistical power (Cohen, 1988) in R, following Snijders (2005). A linear mixed model analysis with an expected moderate effect size (0.15), an α error probability of 0.05, 18 cluster groups, and a significance level of 0.05 require a sample size greater than 79 to achieve a statistical power that exceeds the threshold of 0.8. Consequently, we conclude that our sample size of 166 is adequate. In the following, we analyze our results in two steps. First, we examine the descriptive statistics and then present the statistical tests to assess our hypotheses.

Table 7. Descriptive Results

<table><tr><td colspan="2"></td><td colspan="2">Base model</td><td colspan="2">Model with symbols</td><td colspan="2">Model with colors</td></tr><tr><td></td><td>Scale</td><td>Mean</td><td>St. Dev.</td><td>Mean</td><td>St. Dev.</td><td>Mean</td><td>St. Dev.</td></tr><tr><td>Risk understanding</td><td>Score: 0-5</td><td>2.94</td><td>1.51</td><td>3.13</td><td>1.47</td><td>3.35</td><td>1.45</td></tr><tr><td>Control understanding</td><td>Score: 0-5</td><td>1.81</td><td>1.31</td><td>1.97</td><td>1.34</td><td>2.17</td><td>1.40</td></tr><tr><td>Control improvements</td><td>Score: 0-5</td><td>0.84</td><td>1.03</td><td>0.90</td><td>1.02</td><td>1.28</td><td>1.18</td></tr><tr><td>Perceived risk</td><td>Scale: 0-6</td><td>3.09</td><td>1.02</td><td>3.02</td><td>0.97</td><td>2.99</td><td>0.99</td></tr></table>

Table 8. Linear Mixed Model Results—F-Values

<table><tr><td></td><td colspan="4">Dependent variable</td></tr><tr><td>Factor</td><td>Risk understanding</td><td>Control understanding</td><td>Control improvement</td><td>Risk perception</td></tr><tr><td>Intercept</td><td>1,252.16***</td><td>462.63***</td><td>217.90***</td><td>2706.68***</td></tr><tr><td>Representation</td><td>5.10**</td><td>5.26**</td><td>15.49***</td><td>0.34</td></tr><tr><td colspan="5">Note: *** p &lt; 0.001, ** p &lt; 0.01, * p &lt; 0.05</td></tr></table>

## 5.1 Descriptive Statistics

Because we conducted a controlled experiment, group assignment was random, and nontreatment differences between the groups can be ignored. The descriptive data suggest differences between the dependent variables, and a clear pattern emerges. Risk understanding, control understanding, and control improvements are always lowest in the base model, while the model with colors achieves the highest scores. The model with symbols is continuously in the middle, and only perceived risk does not seem to follow this pattern, as it is lowest in the model with colors. However, the differences seem to be smaller compared to the other dependent variables. Table 7 summarizes the descriptive statistics.

## 5.2 Hypotheses Testing

As a second step, we conducted the statistical tests for our hypotheses by running four linear mixed model analyses (one for each DV). We included a within-group factor representation (with three levels) as a fixed effect, random effects for the blocking variable process model domain (with three levels), a treatment sequence (with six levels), and a blocking variable sequence (with six levels). In addition, participants were added as a random effect and therefore interpreted as a random sample of the population (Judd et al., 2017).

The model assumes unstructured correlations for repeated effects—a particularly flexible approach that allows every term to be different—and heterogeneous compound symmetry for random effects, implying that the variance along the diagonal of the covariance matrix does not have to be the same (Kincaid, 2005). The tests were computed using IBM SPSS Statistics Version 25.0, and Table 8 provides the test results. We did not perform a Bonferroni correction because of the relatively small number of tests and the confirmatory research design (Armstrong, 2014). In summary, we found that the representation treatment yielded significant differences between the treatment groups.

The results confirm significant differences in relation to risk and control understanding, as well as the development of improvement ideas. However, we do not observe a significant effect on risk perception, so we reject H4a and H4b. The remaining results summarized in Table 8 do not allow for a straightforward interpretation, because it is unclear which differences between the three groups are significant. Therefore, we performed a post hoc analysis to break down the significant main effects (Singh, 2007). The multiple-group comparison is based on the estimated marginal means and the Fisher least significant difference (LSD) test. These analyses clarify the findings of particular hypotheses tests and answer ancillary questions that arose during hypotheses testing. We discuss the post hoc results for each set of hypotheses. Figure 2 depicts the results of the linear mixed model analyses. These values are adjusted by the fixed and random variables in the model in order to exclude a potential carryover effect.

Concerning risk understanding, significant differences were observed (Table 8). The post hoc comparison in Table 9 reveals that the model with colors outperforms both the base model (mean difference = 0.35, p < 0.01) and the model with symbols (mean difference = 0.22, p < 0.05), which means that the colors as part of the secondary notation can be used to improve the understanding of risk information in BPMN models. H1b is therefore supported. However, we did not find a significant difference between the model with symbols and the base model; as a result, H1a is rejected.

The results in relation to control understanding in Table 9 further support the assumption that additional visual cues in the form of colors improve the understanding of controls in BPMN models compared to the base model (mean difference = 0.32, p < 0.01). Hypothesis 2b is therefore supported. While the use of symbols improves control understanding, this effect is not significant in our experiment; consequently, H2a is rejected.

![](/api/attachments/XTYPU72P/fulltext/images/1253572155e226ee8fd5caa104b3a005756c6e74eb101b399134f93436d72e6d.jpg)

![](/api/attachments/XTYPU72P/fulltext/images/adc48210a48354c4df1a7db4251001254383ed923e1117fa91c0e902dc27d61e.jpg)

![](/api/attachments/XTYPU72P/fulltext/images/1090f770227e262a2cb8ea644a9fa47dce8002aaac8fa40b93314de1f7804e44.jpg)

![](/api/attachments/XTYPU72P/fulltext/images/7d7a04509e599d996f93dfce37f0e1dd63959f077b9465942fcd6fddaeb54b3e.jpg)  
Figure 2. Differences Between RIC Information Representation Variations  
(95% Lower Bound, Mean, 95% Upper Bound) Based on the Results of the Linear Mixed Model Analysis

Table 9. Post Hoc Comparison between Groups

<table><tr><td></td><td></td><td colspan="2">Risk understanding</td><td colspan="2">Control understanding</td><td colspan="2">Improvement concepts</td></tr><tr><td>Reference group</td><td>Compared group</td><td>Mean difference (I-J)</td><td>St. error</td><td>Mean difference (I-J)</td><td>St. Error</td><td>Mean difference (I-J)</td><td>St. error</td></tr><tr><td rowspan="2">Base</td><td>Colors</td><td>-0.35**</td><td>0.11</td><td>-0.32**</td><td>0.10</td><td>-0.45***</td><td>0.08</td></tr><tr><td>Symbols</td><td>-0.13</td><td>0.11</td><td>-0.16</td><td>0.10</td><td>-0.10</td><td>0.08</td></tr><tr><td rowspan="2">Colors</td><td>Base</td><td>0.35**</td><td>0.11</td><td>0.32**</td><td>0.10</td><td>0.45***</td><td>0.08</td></tr><tr><td>Symbols</td><td>0.22*</td><td>0.11</td><td>0.15</td><td>0.10</td><td>0.35***</td><td>0.08</td></tr><tr><td rowspan="2">Symbols</td><td>Base</td><td>0.13</td><td>0.11</td><td>0.16</td><td>0.10</td><td>0.10</td><td>0.08</td></tr><tr><td>Colors</td><td>-0.22*</td><td>0.11</td><td>-0.15</td><td>0.10</td><td>-0.35</td><td>0.08</td></tr><tr><td colspan="8">Note: *** p &lt; 0.001, ** p &lt; 0.01, * p &lt; 0.05</td></tr></table>

The identification of additional control improvements is also positively influenced by the use of colors compared to the base model (mean difference = 0.45, $p < 0 . 0 0 1 )$ ; H3b is therefore supported. Interestingly, colors also outperform symbols (mean difference = 0.35, $p < 0 . 0 0 1 ,$ . Again, the performance of the base model with symbols is between the model with colors and the base model, but the difference is not significant, and we thus formally reject H3a.

## 6 Discussion

## 6.1 Summary of Results

We set out to examine how the representation format can support the performance of risk assessment and control activity tasks commonly conducted by risk managers. In this context, we compare different representation formats for highlighting RIC information in process models (colors and symbols). The results provide insights into the applicability of the dual-process theory of information processing and suggest that visual representations of process models can be used to improve analytical risk management performance without any biases that could impair related judgment and decision-making.

A clear pattern regarding the influence of primary and secondary notation RIC extensions on risk assessment and control activities emerged (Table 10): secondary RIC extensions using colors outperformed primary notation extensions using symbols.

Table 10. Summary of the Results

<table><tr><td></td><td>Risk understanding</td><td>Control understanding</td><td>Control improvement</td><td>Perceived risk</td></tr><tr><td rowspan="2">Symbols</td><td>H1a: Extensions of the primary notation (additional RIC symbols) improve risk understanding.</td><td>H2a: Extensions of the primary notation (additional RIC symbols) improve control understanding.</td><td>H3a: Extensions of the primary notation (additional RIC symbols) improve control improvement.</td><td>H4a: Extensions of the primary notation (additional RIC symbols) increase perceived risk.</td></tr><tr><td>Rejected</td><td>Rejected</td><td>Rejected</td><td>Rejected</td></tr><tr><td rowspan="2">Color</td><td>H1b: Secondary notation elements (RIC colors) improve risk understanding.</td><td>H2b: Secondary notation elements (RIC colors) improve control understanding.</td><td>H3b: Secondary notation elements (RIC colors) improve control improvement.</td><td>H4b: Secondary notation elements (RIC colors) increase perceived risk.</td></tr><tr><td>Supported</td><td>Supported</td><td>Supported</td><td>Rejected</td></tr></table>

Because we also assessed the effects on subjective risk perception, we conclude that neither colors nor symbols bias the ability to evaluate the risk situation in a BPMN model. This is particularly relevant because we used the color red, a strong visual cue for danger. However, in combination with green for controls, the results do not support any judgment biases.

## 6.2 Implications for Cognitive IS Research

Our research has implications for cognitive IS research on representational alternatives for RIC information. The results contribute to the existing literature on process model understanding. Previous findings have found mixed results regarding the understanding performance of business process models (Figl, 2017; Kummer et al., 2016; Mendling et al., 2012; Petrusel et al., 2016; Recker, 2013). With respect to secondary notation, the findings by Kummer et al. (2016) and Petrusel et al. (2016) indicate that colors reduce the time required to understand process tasks but they do not influence performance in settings with an infinite amount of time. Our results extend the literature by showing that this secondary notation element can increase the understanding performance of RIC information in process models in a more authentic scenario with moderate time pressure. We also found support that colors increase analytical information processing, likely because they carry intuitive semantics relevant for RIC management. Typically, red is associated with risks, while controls relate to green, which is consistent with the principle of semantic transparency and its effect of reducing cognitive load via built-in mnemonics that facilitate either direct perception or ease of learning (Lohse, 1993; Petre, 1995). Our results further contradict findings from other domains indicating that the red color causes a negative effect on performance (Elliot et al., 2007). We conclude that the overall extraneous cognitive load was reduced through the color treatment in our experiments. Moreover, RIC color coding aids understanding performance at different risk management levels, including higher-order thinking.

Concerning primary notation, the results do not support the implicit assumption that such extensions improve the understanding performance behind initiatives to integrate symbolic RIC information into process models (e.g., Cozgarea & Cozgarea, 2013; Krishnan et al., 2005; Radloff et al., 2015; Sonnenberg & vom Brocke, 2014). We find performance improvements only in relation to the extension of the secondary notation and not the primary notation. It is important to emphasize that previous research has focused mainly on primary notations (see Section 2.3). Our results suggest that there is no need to add new symbols such as warning triangles and magnifying glasses to the BPMN syntax as part of the primary notation. While we do not observe negative implications, the results also do not indicate any significant benefits. In this way, they contribute to the understanding of primary and secondary notation in process models and guide practitioners.

Furthermore, our results provide new insights into the mechanisms of cognitive RIC information processing and, in particular, the influence of intuitive information processing in System 1. This direction of inquiry is rare in IS research on conceptual models, which has previously focused mainly on analytical information processing in System 2. One participant in the experiment stated in the comments: “I liked the way the insurance claims chart was set up with the colors, it made it much more easy to visualize and understand the risks and controls.” Our results support this statement, and we use color-in-context theory to explain how colors can create an intuitive response, which can facilitate analytical information processing and support operational risk managers by using RIC colors. Our results extend cognitive-based concepts— as postulated in Figure 1. Secondary RIC extensions that are based on prior knowledge (e.g., alerting colors such as red) can improve information processing performance. Consequently, less working memory is used within the analytical processing of RIC information. Apparently, intuitive information processing offers an additional path outside working memory that supports this process.

The models with the three different risk and control representations for each process entailed identical RIC information, and the process models were informationally equivalent. At the same time, sensory memory was manipulated and contained different intuitive cues that were reconciled with information stored in the affect pool.

Color-in-context theory provides a theoretical explanation for how colors stimulate intuitive information processing because they are perceived faster than other visual elements. In this way, the affective response helped the participants gain an immediate, intuitive understanding of the risks and controls in the model, resulting in improved understanding performance. Interestingly, this effect covers different levels of understanding, from basic element identification (e.g., highest risk in the model), to more advanced questions on control activities (e.g., remaining expected damage when a control is in place), and even higher-order thinking (where the participants had to apply reasonable, reflective thinking to develop future control improvements).

Finally, our findings further contribute to the literature on framing effects in cognitive IS (Browne & Parsons, 2012). While previous studies have examined textual message framing (e.g., Wei et al., 2003), we found that intuitive information processing in relation to colors and symbols does not necessarily cause framing effects, which is particularly relevant because recent findings in other domains suggest that visual cues can increase risk perception (Hammond, 2011; Hammond & Parkinson, 2009). The color red is particularly prone to causing perception biases because it is used in various contexts such as traffic signals to create high alertness (Riley, 2014). Our findings do not confirm risk perception bias associated with the color red and RIC information. A possible explanation could be that the use of the color green for controls counteracts the red, or that the analytical information processing overrides the initial intuitive response. Because we measured risk perception after the participants had already answered the understanding and improvement questions, they had already gained a deep understanding of the process, and an analytical assessment therefore might have replaced the intuitive initial response. Another possible explanation could be that the model with colors may have caused dissonance between analytical and intuitive information processing, as the colors resulted in the highest understanding performance. Lewis-Evans and Rothengatter (2009), for instance, found a relation between task difficulty and risk perception within the context of driving. In line with these findings, it is possible that the understanding improvement may have reduced perceived difficulty, which in turn counteracted increased perceived risk. Risks associated with easier tasks are perceived as more controllable and therefore less dangerous. Further research is needed to explore whether risk perception biases occur in alternative settings.

In summary, our findings pave the way for future research on analytical and intuitive information processing in relation to conceptual modeling and related information representations. While our study refers to RIC representations in a business process, future studies should examine further application areas and representation formats. We also call for more research on the interaction between analytical and intuitive processing. In addition, further research is needed to understand these effects and how they influence one another in order to avoid perception biases under specific circumstances. In this way, our results provide a foundation for future research in cognitive neuroscience IS (NeuroIS). The automatic and hidden processes identified in our study could be measured objectively with brain image tools showing brain activation (Dimoka et al., 2011), which would be particularly useful for validating our reasoning on intuitive and analytical information processing.

## 6.3 Implications for Practice

Our study has two major implications for practice. First, it demonstrates how business process models can be used to support risks and internal control assessment. We focus on operational risk management at the process level and risk management activities outlined in the ISO 31000:2018 and the COSO Enterprise Risk Management—Integrated Framework. Often, line managers with a background in accounting or operations management perform these risk management tasks. They are responsible for risk assessment and related control responses, including, for example, the understanding of risks in relation to unintentional errors, fraud risks, or other operational risks to decide whether they are adequately addressed and develop ideas to improve the risk situation further. Our results indicate that RIC representations in business processes matter and that color should be used to support operational risk managers. Using red for risks and green for controls facilitates the understanding of risks and related controls as well as the development of new control activities. We did not find any biases in risk perception based on RIC representations and therefore recommend that practitioners take advantage of colors in their operational risk management activities.

Second, our results are also relevant for tool vendors. At this stage, business process modeling tools offer facilities to change the color of each activity separately. Our research underlines the requirements of supporting the use of color for specific subclasses of activities, such as risk and control activities. The systematic usage of color could be implemented by a parameterized display of activities. So far, manipulations of process model displays have been proposed and evaluated in research prototypes (see e.g., Jošt et al., 2017) but not yet integrated into commercial tools.

## 6.4 Limitations

Our findings and implications are associated with the following limitations. First, the participants in our experiment were MTurk workers with a background in accounting or business operations. While we regard the sample as suitable for our analysis, it does not represent the general population; future research is needed to determine whether the observed effects occur in more specialized user groups, such as BPMN professionals, who might be more capable of assimilating information from extensions of the primary notation than BPMN novices. In addition, information processing might differ between user groups, as BPMN novices could rely more on System 1, resulting in improved performance in process models using color to highlight RIC information. Further research should address these questions on the generalizability of the results and their implications for other application areas, such as the design of modeling languages.

Another potential limitation of research that explores color effects is color vision deficiency. While, on average, 8% of men and 0.5% of women suffer from some type of color vision deficiency, these are in most cases vision anomalies (anomalous trichromacy) caused by malfunctioning cones (Simunovic, 2010). These individuals usually have difficulties in differentiating between all shades of green, red, or blue because of altered spectral sensitivity. We excluded individuals with vision deficiency by stating in the instructions that anyone affected by color blindness could not participate. Additionally, a color blindness test was included at the beginning of the experiment. While this did reduce possible bias, it also potentially reduced the external validity of our results; however, because we excluded color vision deficiency in our sample, future research is needed to understand its influence on our results.

Moreover, our findings may be limited based on the selection of model cases. We used three models with similar complexity yet all three models can be regarded as rather simple when compared to industry-sized models. Further research is needed to explore whether the results can be confirmed in more complex models.

It also should be emphasized that we only investigated one set of RIC colors (red and green) and one set of symbols (a warning triangle and a magnifying glass), and while we believe that these representations are adequate instantiations of the treatment, we did not consider other treatments or combinations of the treatment (e.g., colors and symbols). Each additional treatment would have required another process model in the experiment’s within-group design, resulting in a potentially higher dropout rate as well as fatigue biases. Further research is thus needed to investigate the effect of alternative RIC representations.

Finally, we did not measure the cognitive mechanisms of intuitive and analytical information processing in System 1 and System 2. Instead, we used established theories to interpret our results through the lens of dual-process theory. However, our explanation remains hypothetical, as we did not determine actual brain activation using brain imaging tools. As outlined above, this should be undertaken by future research in cognitive neuroscience IS.

## 7 Conclusion and Future Research

Our findings contribute to the field of cognitive studies on process modeling. We set out to explore how intuitive information representation of RIC information in BPMN can improve analytical information processing. Our findings show how operational risks can be visualized in BPMN, using primary and secondary notations to improve risk understanding and risk perception. The results suggest that colors improve the understanding of risk and controls and support the identification of control improvements, without causing any perception biases. Primary notation extensions that introduce new symbols, however, do not seem to cause any understanding improvements. Consequently, model designers should use secondary notation element colors whenever a process model contains RIC information.

In addition, the results have implications for the development of new RIC extensions, such as researchers should compare RIC representation formats with default models without any RIC representations. Based on our findings, it would be preferable to compare the results with models containing the suggested RIC colors to determine the incremental benefit and justify inclusions in the BPMN standard.

Furthermore, it needs to be stated that our results indicate that it is not possible to use different risk visualization formats to disguise actual risk levels within a process. Regardless of whether a BPMN model contains RIC colors or symbols, the perceived risk in the particular control situation appears to be unaffected. Overall, our results indicate that it is possible to take advantage of intuitive information processing, using colors to improve operational risk management performance. Future IS research should investigate other user groups, application areas, and further intuitive stimuli that support information processing.

## References

Akinci, C., & Sadler‐Smith, E. (2012). Intuition in management research: A historical review. International Journal of Management Reviews, 14(1), 104-122.

Armstrong, R. A. (2014). When to use the Bonferroni correction. Ophthalmic Physiological Optics, 34, 502-508.

Asare, S. K., Trompeter, G. M., & Wright, A. M. (2000). The effect of accountability and time budgets on auditors’ testing strategies. Contemporary Accounting Research, 17(4), 539-560.

Baddeley, A. (2012). Working memory: Theories, models, and controversies. Annual Review of Psychology, 63(1), 1-29.

Bai, X., Krishnan, R., Padman, R., & Wang, H. J. (2013). On risk management with information flows in business processes. Information Systems Research, 24(3), 731-749.

Bera, P. (2012). Does cognitive overload matter in understanding BPMN models? Journal of Computer Information Systems, 52(4), 59-69.

Bodart, F., Patel, A., Sim, M., & Weber, R. (2001). Should optional properties be used in conceptual modelling? A theory and three empirical tests. Information Systems Research, 12(4), 384-405.

Boritz, J. E., Borthick, A. F., & Presslee, A. (2012). The effect of business process representation type on assessment of business and control risks: Diagrams versus narratives. Issues in Accounting Education, 27(4), 895-915.

Bromiley, P., McShane, M., Nair, A., & Rustambekov, E. (2015). Enterprise risk management: Review, critique, and research directions. Long Range Planning, 48(4), 265-276.

Browne, G. J., & Parsons, J. (2012). More enduring questions in cognitive IS research. Journal of the Association for Information Systems, 13(12), 1000-1011.

Burton-Jones, A., & Meso, P. N. (2008). The effects of decomposition quality and multiple forms of information on novices’ understanding of a domain from a conceptual model. Journal of the Association for Information Systems, 9(12), 784-802.

Burton-Jones, A., Wand, Y., & Weber, R. (2009). Guidelines for empirical evaluations of conceptual modeling grammars. Journal of the

Association for Information Systems, 10(6), 495-532.

Burton-Jones, A., & Weber, R. (2014). Building conceptual modeling on the foundation of ontology. In H. Topi & A. Tucker (Eds.), Computing Handbook: Information systems and information technology (3rd ed., pp. 15.11- 15.24). CRC Press.

Carnaghan, C. (2006). Business process modeling approaches in the context of process level audit risk assessment: An analysis and comparison. International Journal of Accounting Information Systems, 7(2), 170-204.

Chen, C.-F., Liu, T., & Huang, K.-C. (2015). Characteristics of warning labels for drug containers and their effects on perceived hazardousness. Safety Science, 78, 149-154.

Chuang, S. C. (2013). Time pressure and the endowment effect. Journal of Applied Social Psychology, 43(6), 1313-1323.

Cierniak, G., Scheiter, K., & Gerjets, P. (2009). Explaining the split-attention effect: Is the reduction of extraneous cognitive load accompanied by an increase in germane cognitive load? Computers in Human Behavior, 25(2), 315-324.

Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Erlbaum.

Cope, E. W., Küster, J., Etzweiler, D., Deleris, L., & Ray, B. (2010). Incorporating risk into business process models. IBM Journal of Research and Development, 54(3), Article 4.

COSO. (2004). Enterprise risk management— Integrated framework: Executive summary. https://www.coso.org/Documents/COSO-ERM-Executive-Summary.pdf

COSO. (2013). Internal control—Integrated framework: Executive summary. https://www. coso.org/Documents/990025P-Executive-Summary-final-may20.pdf

Cozgarea, G., & Cozgarea, A. (2013). BPMN patterns used in management information systems. Annales Universitatis Apulensis Series Oeconomica, 15(1), 15-23.

Curtis, B., Kellner, M. I., & Over, J. (1992). Process modeling. Communications of the ACM, 35(9), 75-90.

Davies, I., Green, P., Rosemann, M., Indulska, M., & Gallo, S. (2006). How do practitioners use conceptual modeling in practice? Data & Knowledge Engineering, 58(3), 358-380.

DeLeeuw, K. E., & Mayer, R. E. (2008). A Comparison of three measures of cognitive load: Evidence for separable measures of intrinsic, extraneous, and germane load. Journal of Educational Psychology, 100(1), 223-234.

Dimoka, A., Pavlou, P. A., & Davis, F. D. (2011). Research commentary—NeuroIS: The potential of cognitive neuroscience for information systems research. Information Systems Research, 22(4), 687-702.

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). Fundamentals of business process management (2nd ed.). Springer

Dunn, C. L., & Gerard, G. J. (2001). Auditor efficiency and effectiveness with diagrammatic and linguistic conceptual model representations. International Journal of Accounting Information Systems, 2(4), 223-248.

Elliot, A. J., & Maier, M. A. (2012). Color-in-context theory. In P. Devine & P. A. (Eds.), Advances in Experimental Social Psychology. (vol. 45, pp. 61-125).

Elliot, A. J., Maier, M. A., Moller, A. C., Friedman, R., & Meinhardt, J. (2007). Color and psychological functioning: the effect of red on performance attainment. Journal of Experimental Psychology, 136(1), 154-168.

Evans, J. S. B. T. (2003). In two minds: Dual-process accounts of reasoning. Trends in Cognitive Sciences, 7(10), 454-459.

Evans, J. S. B. T. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. Annual Review of Psychology, 59(1), 255-278.

Evans, J. S. B. T. (2011). Dual-process theories of reasoning: Contemporary issues and developmental applications. Developmental Review, 31(2), 86-102.

Field, A. J. (2013). The case of the multiplying millions: Sherlock Holmes in advertising. In S. Vanacker & C. Wynne (Eds.), Sherlock Holmes and Conan Doyle: Multi-media afterlives (pp. 19-35). Palgrave Macmillan UK.

Figl, K. (2017). Comprehension of Procedural Visual Business Process Models - A Literature Review. Business & Information Systems Engineering, 59(1), 41-67.

Figl, K., Mendling, J., & Strembeck, M. (2013). The Influence of Notational Deficiencies on Process Model Comprehension. Journal of the Association for Information Systems, 14(6), 312- 338.

Figl, K., Recker, J., & Mendling, J. (2013). A study on the effects of routing symbol design on process model comprehension. Decision Support Systems, 54(2), 1104-1118.

Frank, U. (2008). The MEMO meta modelling language (MML) and language architecture. https://ideas.repec.org/p/zbw/udeicb/43.html

Frankish, K., & Evans, J. S. B. T. (2009). The duality of mind: An historical perspective. In J. S. B. T. Evans & K. Frankish (Eds.), In two minds: Dual processes and beyond (pp. 1-30). Oxford University Press.

Gefen, D., & Straub, D. (2005). A practical guide to factorial validity using PLS-graph: Tutorial and annotated example. Communications of the Association for Information Systems, 16, 91-109.

Gelinas, U., & Dull, R. (2010). Accounting information systems. South-Western Cengage Learning.

Gemino, A., & Wand, Y. (2004). A framework for empirical evaluation of conceptual modeling techniques. Requirements Engineering, 9(4), 248-260.

Gemino, A., & Wand, Y. (2005). Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data & Knowledge Engineering, 55(3), 301-326.

Gerend, M. A., & Sias, T. (2009). Message framing and color priming: How subtle threat cues affect persuasion. Journal of Experimental Social Psychology, 45(4), 999-1002.

Gordon, L. A., Loeb, M. P., & Tseng, C.-Y. (2009). Enterprise risk management and firm performance: A contingency perspective. Journal of Accounting and Public Policy, 28(4), 301-327.

Green, T. R. G., & Petre, M. (1996). Usability analysis of visual programming environments: A “cognitive dimensions” framework. Journal of Visual Languages and Computing, 7(2), 131- 174.

Griffith, L. J., & Leonard, S. D. (1997). Association of colors with warning signal words. International Journal of Industrial Ergonomics, 20(4), 317- 325.

Hammond, D. (2011). Health warning messages on tobacco products: A review. Tobacco Control, 20, 327-337.

Hammond, D., & Parkinson, C. (2009). The impact of cigarette package design on perceptions of risk. Journal of Public Health, 31(3), 345-353.

Hansen, J., & Walden, E. (2013). The role of restrictiveness of use in determining ethical and

legal awareness of unauthorized file sharing. Journal of the Association for Information Systems, 14(9), 521-549.

Hayne, C., & Free, C. (2014). Hybridized professional groups and institutional work: COSO and the rise of enterprise risk management. Accounting, Organizations and Society, 39(5), 309-330.

ISO. (2018). ISO 31000:2018 Risk management: Guidelines. In. Jenkins, J., Proudfoot, J., Valacich, J., Grimes, G., & Nunamaker, J. (2019). Sleight of hand: Identifying concealed information by monitoring mouse-cursor movements. Journal of the Association for Information Systems, 20(1), 1-32.

Jones, B., & Kenward, M. G. (2003). Design and analysis of cross-over trials (2nd ed.). Chapman & Hall/CRC.

Jošt, G., Huber, J., Heričko, M., & Polančič, G. (2017). Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights. Decision Support Systems, 103, 58- 69.

Judd, C. M., Westfall, J., & Kenny, D. A. (2017). Experiments with more than one random factor: designs, analytic models, and statistical power. Annual Review of Psychology, 68(1), 601-625.

Kahneman, D. (2011). Thinking, fast and slow. Macmillan.

Kelton, A. S., Pennington, R. R., & Tuttle, B. M. (2010). The effects of information presentation format on judgment and decision making: A review of the information systems research. Journal of Information Systems, 24(2), 79-105.

Khatri, N., & Ng, H. A. (2000). The role of intuition in strategic decision making. Human Relations, 53(1), 57-86.

Kincaid, C. (2005). Guidelines for selecting the covariance structure in mixed model analysis. Proceedings of the SAS Users Group International.

Kleffner, A. E., Lee, R. B., & McGannon, B. (2003). The effect of corporate governance on the use of enterprise risk management: Evidence From Canada. Risk Management and Insurance Review, 6(1), 53-73.

Kosslyn, S. M., Thompson, W. L., & Ganis, G. (2006). The case for mental imagery. Oxford University Press.

Krause, T. A., & Tse, Y. (2016). Risk management and firm value: Recent theory and evidence. International Journal of Accounting & Information Management, 24(1), 56-81.

Krishnan, R., Peters, J., Padman, R., & Kaplan, D. (2005). On data reliability assessment in accounting information systems. Information Systems Research, 16(3), 307-326.

Kuehl, R. O. (2000). Design of experiments: Statistical principles of research design and analysis (2nd ed.). Duxbury Thomson Learning.

Kummer, T.-F., Recker, J., & Mendling, J. (2016). Enhancing understandability of process models through cultural-dependent color adjustments. Decision Support Systems, 87, 1-12.

La Rosa, M., ter Hofstede, A. H. M., Wohed, P., Reijers, H. A., & van der Aalst, W. M. P. (2011a). Managing process model complexity via concrete syntax modifications. IEEE Transactions on Industrial Informatics, 7(2), 255-265.

La Rosa, M., Wohed, P., Mendling, J., ter Hofstede, A. H. M., Reijers, H. A., & van der Aalst, W. M. P. (2011b). Managing process model complexity via abstract syntax modifications IEEE Transactions on Industrial Informatics, 7(4), 614-629.

Larkin, J. H., & Simon, H. A. (1987). Why a diagram is (sometimes) worth ten thousand words. Cognitive Science, 11, 65-99.

Lichtenfeld, S., Elliot, A. J., Maier, M. A., & Pekrun, R. (2012). Fertile green: Green facilitates creative performance. Personality and Social Psychology Bulletin, 38, 784-797.

Lipshitz, R., & Shulimovitz, N. (2007). Intuition and emotion in bank loan officers’ credit decisions. Journal of Cognitive Engineering and Decision Making, 1(2), 212-233.

Lohse, G. L. (1993). A cognitive model for understanding graphical perception. Human-Computer Interaction, 8(4), 353-388.

Lukyanenko, R., Evermann, J., & Parsons, J. (2014). Instantiation validity in IS design research. In M. C. Tremblay, D. VanderMeer, M. Rothenberger, A. Gupta, & V. Yoon (Eds.), Advancing the impact of design science: Moving from theory to practice: DESRIST 2014. (pp. 321-328). Springer.

Lukyanenko, R., Evermann, J., & Parsons, J. (2015). Guidelines for establishing instantiation validity in IT artifacts: A survey of IS research. In B. Donnellan, M. Helfert, J. Kenneally, D. VanderMeer, M. Rothenberger, & R. Winter (Eds.), New horizons in design science: broadening the research agenda: DESRIST 2015. (pp. 430-438). Springer.

Mayer, R. E. (2009). Multimedia learning (2nd ed.): Cambridge University Press.

McNicol, D., & Pennington, C. W. (1973). Sensory and decision processes in anchor effects and aftereffects. Journal of Experimental Psychology, 100(2), 232–238.

Mehta, R., & Zhu, R. J. (2009). Blue or red? Exploring the effect of color on cognitive task performances. Science, 323(5918), 1226-1229.

Mendling, J. (2008). Metrics for process models: Empirical foundations of verification, error prediction, and guidelines for correctness. Springer

Mendling, J., Reijers, H. A., & Recker, J. (2010). Activity labeling in process modeling: Empirical insights and recommendations. Information Systems, 35(4), 467-482.

Mendling, J., Strembeck, M., & Recker, J. (2012). Factors of process model comprehension: Findings from a series of experiments. Decision Support Systems, 53(1), 195-206.

Moody, D. L. (2009). The “physics” of notations: Toward a scientific basis for constructing visual notations in software engineering. IEEE Transactions on Software Engineering, 35(6), 756-779.

Mueller-Wickop, N., & Schultz, M. (2013). Modelling concepts for process audits: Empirically grounded extension of BPMN. Proceedings of the European Conference on Information Systems.

Norris, S. P., & Ennis, R. H. (1989). Evaluating critical thinkingMidwest Publications.

OMG. (2012). Business process model and notation. http://www.bpmn.org/

Parsons, J. (2011). An experimental study of the effects of representing property precedence on the comprehension of conceptual schemas. Journal of the Association for Information Systems, 12(6), 401-422.

Paul, S., & Nazareth, D. L. (2010). Input information complexity, perceived time pressure, and information processing in GSS-based work groups: An experimental investigation using a decision schema to alleviate information overload conditions. Decision Support Systems, 49(1), 31-40.

Petre, M. (1995). Why looking isn’t always seeing: Readership skills and graphical programming. Communications of the ACM, 38(6), 33-44.

Petrusel, R., Mendling, J., & Reijers, H. A. (2016). Task-specific visual cues for improving process

model understanding. Information and Software Technology, 79, 63-78.

Power, M. (2007). Organized uncertainty: Designing a world of risk management. Oxford University Press.

PWC. (2018). PwC’s Global Economic Crime and Fraud Survey 2018: Pulling fraud out of the shadows: A spotlight on the Middle East. https://www.pwc.com/m1/en/publications/docu ments/economic-crime-fraud-survey-2018.pdf

Radloff, M., Schultz, M., & Nüttgens, M. (2015). Extending different business process modeling languages with domain specific concepts: The case of internal controls in EPC and BPMN. In J. Kolb (ed.), Enterprise modelling and information systems architectures (pp. 45-58). Bonn Gesellschaft für Informatik.

Recker, J. (2010). Continued use of process modeling grammars: The impact of individual difference factors. European Journal of Information Systems, 19(1), 76-92.

Recker, J. (2013). Empirical investigation of the usefulness of gateway constructs in process models. European Journal of Information Systems, 22(6), 673-689.

Recker, J., & Dreiling, A. (2011). The effects of content presentation format and user characteristics on novice developers’ understanding of process models. Communications of the Association for Information Systems, 28, 65-84.

Recker, J., Reijers, H. A., & van de Wouw, S. G. (2014). Process model comprehension: The effects of cognitive abilities, learning style, and strategy. Communications of the Association for Information Systems, 34, 199-222.

Reijers, H. A., Freytag, T., Mendling, J., & Eckleder, A. (2011a). Syntax highlighting in business process models. Decision Support Systems, 51(3), 339- 349.

Reijers, H. A., Freytag, T., Mendling, J., & Eckleder, A. (2011b). Syntax highlighting in business process models. Decision Support Systems, 51(3), 339- 349.

Rice, S., & Trafimow, D. (2012). Time pressure heuristics can improve performance due to increased consistency. The Journal of General Psychology, 139(4), 273-288.

Riley, D. (2014). Mental models in warnings message design: A review and two case studies. Safety Science, 61, 11-20.

Ritchi, H., Jans, M. J., Mendling, J., & Reijers, H. A. (2020). The influence of business process

representation on performance of different task types. Journal of Information Systems, 34(1), 167-194.

Rook, L. (2014). Exposure to the color red enhances creative thinking depending on appetitiveaversive cues. Creativity Research Journal, 26(1), 124-130.

Rosemann, M., & zur Muehlen, M. (2005). Integrating risks in business process models. Proceedings of the Australasian Conference on Information Systems.

Sadiq, S., Governatori, G., & Namiri, K. (2007). Modeling control objectives for business process compliance. Proceedings of the 5th International Conference on Business Process Management.

Schultz, M., & Radloff, M. (2014). Modeling concepts for internal controls in business processes: An empirically grounded extension of BPMN. In S. Sadiq, P. Soffer, & H. Völzer (Eds.), BPM 2014 (pp. 184-199). Springer.

Siau, K. (2004). Informational and computational equivalence in comparing information modeling methods. Journal of Database Management, 15(1), 73-86.

Sienou, A., Lamine, E., Karduck, A., & Pingau, H. (2007). Conceptual model of risk: Towards a risk modelling language. Proceedings of the International Conference on Web Information Systems Engineering.

Simunovic, M. P. (2010). Colour vision deficiency. Eye, 24, 747-755.

Singh, K. (2007). Quantitative social research methods. SAGE.

Sitkin, S. B., & Weingart, L. R. (1995). Determinants of risky decision-making behavior: a test of the mediating role of risk perceptions and propensity. The Academy of Management Journal, 38(6), 1573-1592.

Slovic, P., Finucane, M., Peters, E., & MacGregor, D. G. (2002). The affect heuristic. In T. Gilovich, D. Griffin, & K. D. (Eds.), Heuristics and biases: The psychology of intuitive judgment. Cambridge University Press.

Slovic, P., Peters, E., Finucane, M. L., & Macgregor, D. G. (2005). Affect, risk, and decision making. Health Psychology, 24(4), 35-40.

Snijders, T. A. B. (2005). Power and sample size in multilevel linear models. In B. S. Everitt & D. C. Howell (eds.), Encyclopedia of statistics in behavioral science. Wiley.

Soin, K., & Collier, P. (2013). Risk and risk management in management accounting and

control. Management Accounting Research, 24(2), 82-87.

Sonnenberg, C., & vom Brocke, J. (2014). The missing link between BPM and accounting. Business Process Management Journal, 20(2), 213-246.

Stanovich, K. E. (2004). The robot’s rebellion: Finding meaning in the age of Darwin. Chicago.

Stephen, W. (2001). Exploring the role of the corporate risk manager. Risk Management, 3(1), 7-25.

Stevens, M., & Ruxton, G. D. (2012). Linking the evolution and form of warning coloration in nature. Proceedings Biological Sciences, 279(1728), 417-426.

Strecker, S., Heise, D., & Frank, U. (2011). RiskM: A multi-perspective modeling method for IT risk assessment. Information Systems Frontiers, 13(4), 595-611.

Te'eni, D. (2001). Cognitive-affective model of organizational communication for designing IT. MIS Quarterly, 25(2), 251-312.

Vegas, S., Apa, C., & Juristo, N. (2016). Crossover designs in software engineering experiments: Benefits and perils. IEEE Transactions on Software Engineering, 42(2), 120-135.

Verbeke, G., & Molenberghs, G. (2000). Linear mixed models for longitudinal data. Springer.

Wand, Y., & Weber, R. (2002). Research commentary: Information systems and conceptual modeling— A research agenda. Information Systems Research, 13(4), 363-376.

Wei, K.-K., Tan, B. C. Y., & Heng, C.-S. (2003). Willingness to continue with software projects: Effects of feedback direction and optimism under high and low accountability conditions. Journal of the Association for Information Systems, 4(1), Article 9.

Weiss, R. (2003). Designing problems to promote higher-order thinking. New Directions for Teaching and Learning, 95, 25-31.

Westinghouse. (1981). Product safety label handbook. Westinghouse Electric Corporation, Westinghouse Printing Division.

Woiceshyn, J. (2009). Lessons from “good minds”: How CEOs use intuition, analysis and guiding principles to make strategic decisions. Long Range Planning, 42(3), 298-319.

Zender, M., & Mejia, G. M. (2013). Improving icon design: Through focus on the role of individual symbols in the construction of meaning. Visible Language, 47(1), 66-89.

## Appendix A: Research Instrument

The data collection was conducted using a self-developed online experiment. In the following, the instrument design will be outlined (notes are in italics). Then, we will illustrate the technical implementation with screenshots.

## A Comparison of Risks and Internal Controls in Business Process Depictions

This exercise is part of a research project on risks and internal controls in process depictions. Several different techniques exist but it is unclear which approach i best. This research project addresses this question. The following exercise contains two parts:

● Part 1 gathers some general information about you and your background.

• Part 2 provides you with three process depictions entailing risks and internal controls. You will be asked questions about each of them.

Please answer all questions to the best of your judgment and in the order they are presented as it is not possible to return to earlier questions.

Participation in the exercise will take approximately 25 minutes and is completely anonymous.

Note: Next, detailed participation information in accordance with the requirements of the ethics office were provided, and the participants had to give consent that they would like to take part.

The survey contains red and green colors. The following questions ensure that you can see these colors correctly. Please enter the numbers that you see in the fields.

## Colors

![](/api/attachments/XTYPU72P/fulltext/images/11a970f40f96fc0e8f357202251b59ee645b9e9b36741f6ec8e726d6e09a20c1.jpg)  
What number do you see?

![](/api/attachments/XTYPU72P/fulltext/images/768daaab5067ce5edc502d7ad388df60d3562a89dfe8daed0a3cd317e65bbc5a.jpg)

What number do you see?

Part 1) Background Questions

1.1 Please specify your gender:

• Female

Male

• Other

1.2 How old are you? \_\_\_\_

1.3 Please list your citizenship(s): (Separate multiple citizenships by comma.)

1.4 What is the highest degree or level of school you have completed?

• No schooling completed

High school graduate, diploma, or the equivalent

Trade/technical/vocational training

Bachelor degree

• Master degree

• Professional degree

• Doctorate degree

1.5 Do you have a degree in Accounting? (Yes/No)

1.6 Do you have work experience as an Accountant? (Yes/No)

1.6.1 How many years of work experience do you have in Accounting? \_ (conditional question; only if the participant answered question 1.6 with yes)

1.7 Do you have any knowledge about Business Process Management (e.g., through training or work experience)? (Yes/No)

1.8 Have you ever worked with Business Process Model and Notation (BPMN)? (Yes/No)

1.9 For how many years and months have you worked with BPMN? (conditional question; only if the participant answered question 1.8 with yes)

Please rate your agreement with the following statements

1.10 I am very familiar with the Business Process Management. (7-point Likert scale, conditional question; only if the participant answered question 1.7 with yes)

1.11 Overall, I am very familiar with the BPMN. (7-point Likert scale, conditional question; only if the participant answered question 1.8 with yes)

## Part 2) Risks and Internal Controls in Processes

In the following, you will see process depictions that contain information about risks and controls.

Risk:

Information regarding how often a process is executed is provided as an annotation in the model (e.g., 1,000 claims). A risk occurs in relation to specific tasks (e.g., 10% that someone makes a mistake). The costs per incident (CPI) list the damage if the negative event occurs (e.g., \$25 per event). The total expected damage (TED) is the amount that results from the number of negative events and the damage per event.

In this example:

Number / how often the process occurs: 1,000

Risk: 10%

Costs per incident (CPI): \$25

Total expected damage (TED) = 1,000 x 0.1 x \$25 = \$2,500

Controls:

Risks can be addressed by internal controls. Controls may be applied to some or all instances of the process. For instance, if a risk exists that a transaction contains errors, then it would be possible to let a second person approve this transaction. This would cause additional cost of \$1 per transaction. However, it would reduce the risk of errors by 5% (10% - 5% = 5%).

In the example above this would change the costs as follows:

New expected damage: 1,000 x 5% x \$25 = \$1,250

Costs for internal controls: 1,000 x \$1 = \$1,000

Total costs: \$2,250

The internal controls reduce the total costs by \$250 (\$2,250 instead of \$2,500).

Indicate your agreement with the following statement: The explanation of risks and related control costs in processes was understandable. (7-point Likert scale)

Note: Each participant received an online shop process, an insurance claim process, and a goods receipt process in random order. Additionally, each participant received randomly one of these processes with the base model representation, one with the base model representation and RIC symbols, and one with the base model representation and RIC colors. In the following, the order: 1. Online shop, 2. insurance claim, and 3. goods receipt process is selected, and all RIC representation variations are provided for each BPMN process.

Online Shop Process: Base Model

![](/api/attachments/XTYPU72P/fulltext/images/0dd035f81d592da774fb7e9de10f9d88c8c83171c2b2cc403b649fbc0978249a.jpg)

## Online Shop Process: Base Model with Symbols

![](/api/attachments/XTYPU72P/fulltext/images/7d1626f48bab8501e3c1d61f8f71a14832a9219df63071283ef37b906708868e.jpg)

Online Shop Process: Base Model with Colors  
![](/api/attachments/XTYPU72P/fulltext/images/cc1367fbf9ed344e756b0d218872a7cf70671e1ab68cb903080b37f37520796f.jpg)

Note: First, participants completed three true-false questions. These focused on the general process and were not related to specific risk and internal control aspects. This gave the participants time to familiarize themselves with the process. The timer began once the participant had answered the three questions.

The process model depicts an online shopping process. Please read the process model carefully and answer the following questions:

P.1 Customers have to confirm the order after entering address data. (Yes/No)

P.2 The process may end because the customer cancels the order. (Yes/No)

P.3 For each order a delivery note is created. (Yes/No)

## Part 2.1

In the following, you will be given questions related to the depicted business process. Please answer these questions to the best of your knowledge within the given time limit (5 minutes)

CPI: Cost Per Incident, TED: Total Expected Damage

Note: The following five questions were used to determine risk understanding.

R.1 How many risks are described in the model?

R.2 The risk concerning packing can cause damage of \$

R.3 The risk of incorrect address data is \_\_\_\_% within the process.

R.4 What are the cost that incur when items of an order are not correctly picked from the warehouse? \$

R.5 What is the highest total expected damage in the process? \$

Note: The following five questions were used to determine control understanding.

C.1 How many controls are described in the process?

C.2 What are the control cost per order to reduce picking risk? \$\_\_\_\_\_\_\_per order.

C.3 The risk of errors in relation to order picking can be reduced by % by internal controls.

C.4 Internal controls reduce the total anticipated cost for technical problems by \$

C.5 What is the remaining total expected damage when the control to check orders is in place? \_

Note: The following question was used to determine control improvement. The timer was reset and counted down 180 seconds (3 min).

List up to five ideas how the risks in the process could be further reduced (e.g., by additional controls, changes of existing controls, or process changes) and explain how the improvement would work:

I.1 Idea 1

I.2 Idea 2

I.3 Idea 3

I.4 Idea 4

I.5 Idea 5

Note: The following questions were used to determine perceived risk. Questions are presented in a table with 7-point answers.

How would you characterize the online shopping process?

S.1 The process is

very well controlled (1) … very risky (7)

S.2 The process contains

substantial potential for accidental errors (1) … no potential for accidental errors (7)

S.3 The process depicts a

S.4 What is the likelihood of accidental errors within the depicted process

positive control situation (1) … negative control situation (7)

very likely (1) … very unlikely (7)

Insurance Claim Process: Base Model  
![](/api/attachments/XTYPU72P/fulltext/images/23ac1ca2f9458e23fdfa0d772f16d925349c1ee0bfa368399fe60bcf8e7a5a1f.jpg)

## Insurance Claim Process: Base Model with Symbols

![](/api/attachments/XTYPU72P/fulltext/images/366f9178460454faedcc4887f138c9176366cd3e3b9d62cc3fc914bf18e5abff.jpg)

Insurance Claim Process: Base Model with Colors  
![](/api/attachments/XTYPU72P/fulltext/images/9dfafd2fc21c3e14e0a9302da3b14226f8bed8577762ec476f8c003c8ad2b48f.jpg)

Note: Again, participants completed three true-false questions. These focused on the general process and were not related to specific risk and internal control aspects. This gave the participants time to familiarize themselves with the process. The timer began once the participant had answered the three questions.

The process model depicts an insurance claim process. Please read the process model carefully and answer the following questions:

P.1 Each claim is registered. (Yes/No)

P.2 At the end of the process, the claim is archived. (Yes/No)

P.3 A claim can be rejected at multiple stages in the process. (Yes/No)

## Part 2.2

In the following, you will be given questions related to the depicted business process. Please answer these questions to the best of your knowledge within the given time limit (5 minutes)

CPI: Cost Per Incident, TED: Total Expected Damage

Note: The following five questions were used to determine risk understanding.

R.1 How many risks are described in the process?

R.2 The risk of fraud in relation to overcharging within the process is \_\_\_\_%.

R.3 The risk of missing documents can cause a total damage of \$

R.4 What is the highest total expected damage in the process? \$

R.5 What is the cost per incident incurred when an assessment error is made? \$

Note: The following five questions were used to determine control understanding.

C.1 How many controls are described in the process?

C.2 The controls for missing documents cost \$\_\_\_ per claim.

C.3 The risk of assessment errors can be reduced by \_ % through a second assessment.

C.4 The internal controls reduce the anticipated cost of assessment errors by \$

C.5 What is the remaining total expected damage when the control to double-check the obtained documentation is in place? \$

Note: The following question was used to determine control improvement. The timer was reset and counted down 180 seconds (3 min).

List up to five ideas how the risks in the process could be further reduced (e.g., by additional controls, changes of existing controls, or process changes) and explain how the improvement would work:

I.1 Idea 1

I.2 Idea 2

I.3 Idea 3

I.4 Idea 4

I.5 Idea 5

Note: The following questions were used to determine perceived risk. Questions are presented in a table with 7-point answers.

How would you characterize the online shopping process?

S.1 The process is

S.2 The process contains

S.3 The process depicts a

S.4 What is the likelihood of accidental errors within the depicted process

very well controlled (1) … very risky (7)

substantial potential for accidental errors (1) … no potential for accidental errors (7)

positive control situation (1) … negative control situation (7)

very likely (1) … very unlikely (7)

Goods Receipt Process: Base Model  
![](/api/attachments/XTYPU72P/fulltext/images/122cd0d3ac204eb727b2c2bfed37dce032dd4ff0be240bf5c6425f35bd3b55bd.jpg)

Goods Receipt Process: Base Model with Symbols  
![](/api/attachments/XTYPU72P/fulltext/images/54c5c296d0d425795c9b214e44e863bcf3e63d10e3e92f3b9e2196026202b0b4.jpg)

## Goods Receipt Process: Base Model with Colors

![](/api/attachments/XTYPU72P/fulltext/images/fb71da1f0c59a90aad6b6fd6a9b654161f5f7c59843a3315e67ea7dd6972f185.jpg)

Note: Again, participants completed three true-false questions. These focused on the general process and were not related to specific risk and internal control aspects. This gave the participants time to familiarize themselves with the process. The timer began once the participant had answered the three questions.

The process model depicts a goods receipt process. Please read the process model carefully and answer the following questions:

P.1 The process can only end by placing goods in stock. (Yes/No)

P.2 Goods are received by trucks. (Yes/No)

P.3 The booking clerk is contacted when the delivery does not match a purchase order. (Yes/No)

## Part 2.3

In the following, you will be given questions related to the depicted business process. Please answer these questions to the best of your knowledge within the given time limit (5 minutes).

CPI: Cost Per Incident, TED: Total Expected Damage

Note: The following five questions were used to determine risk understanding

R.1 How many risks are described in the process?

R.2 The risk that the booking clerk makes a wrong acceptance decision is \_\_\_\_%.

R.3 The risk to accept goods with poor quality causes damage of \$\_\_\_\_\_\_ per incident.

R.4 What is the highest total expected damage in the process? \$

R.5 Errors in the vendor selection cause a total damage of \$

Note: The following five questions were used to determine control understanding

C.1 How many controls are described in the process?

C.2 The controls to validate the vendor selection cost \$\_\_\_ per order.

C.3 The risk to accept goods with poor quality can be reduced by \_\_\_\_% by inspections.

C.4 The internal controls reduce the anticipated cost for making a wrong decision upon acceptance by \$

C.5 The remaining risk that a cheaper vendor exists despite the validation of the vendor selection causes the total damage of \$

Note: The following question was used to determine control improvement. The timer was reset and counted down 180 seconds (3 min).

List up to five ideas how the risks in the process could be further reduced (e.g., by additional controls, changes of existing controls, or process changes) and explain how the improvement would work:

I.1 Idea 1

I.2 Idea 2

I.3 Idea 3

I.4 Idea 4

I.5 Idea 5

Note: The following questions were used to determine perceived risk. Questions are presented in a table with 7-point answers.

How would you characterize the online shopping process?

S.1 The process is

S.2 The process contains

very well controlled (1) … very risky (7)

S.3 The process depicts a

substantial potential for accidental errors (1) … no potential for accidental errors (7)

S.4 What is the likelihood of accidental errors within the depicted process

positive control situation (1) … negative control situation (7)

very likely (1) … very unlikely (7)

F.1 Please enter any further comments or suggestions. (open question)

Many thanks for your participation.

![](/api/attachments/XTYPU72P/fulltext/images/055b61f96e79430e0b096535f58535632fcad4d752df6c2a95bc5fe595f6b640.jpg)  
Figure A1. Screenshot of the Risk and Control Explanation

In the following, you will be given questions related to the depicted business process. Please answer these questions to the best of your knowledge within the given time (5 minutes). CPI: Cost Per Incident; TED: Total Expected Damage

![](/api/attachments/XTYPU72P/fulltext/images/792f1e88ee36442d962e9a3cb49eb5a560e862688be175feea5eb77837c65587.jpg)

Time Left for first 10 Questions: 300s

R4) What is the highest total expected damage in the process? \$

C4) The internal controls reduce the anticipated cost for making a wrong decision upon acceptance by \$

Figure A2. Screenshot of the Risk and Control Understanding Questions for the Goods Receipt Process in the Online Experiment

![](/api/attachments/XTYPU72P/fulltext/images/010eb8b4fbcad1206cf0c85ced1158324bf53cb1b94ffc71cbcd711b45986dc4.jpg)  
Figure A3. Screenshot of the Control Improvement Question in the Online Experiment

## About the Authors

Tyge-F. Kummer is an associate professor at the Queensland University of Technology (QUT), Australia. His research interests comprise judgment and decision-making, accounting information systems, business process management, and fraud detection and prevention. His research has been published in journals including Decision Support Systems, Information & Management, Business & Information Systems Engineering, International Journal of Information Management, Communications of the Association of Information Systems, as well as in proceedings of internationally recognized conferences.

Jan Mendling is a full professor at Wirtschaftsuniversität Wien (WU Vienna), Austria. His research interests include business process management and information systems. He is co-author of the textbooks Fundamentals of Business Process Management and Wirtschaftsinformatik. He has published more than 400 research papers and articles. He is a member of several international journals, a member of the board of the Austrian Society for Process Management (http://prozesse.at), a co-founder of the Berlin BPM Community of Practice (http://www.bpmb.de), and a member of the IEEE Task Force on Process Mining.

Copyright © 2021 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
