---
otero_id: 20895
otero_key: "FNYTZNHU"
title: "A hypermedia-based group decision support system to support collaborative medical decision-making"
authors: "G.R Rao; M Turoff"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00096-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hypermedia-based group decision support system to support collaborative medical decision-making

G.R. Rao <sup>a</sup>, M. Turoff <sup>b,)</sup>

Quantum Enterprises, Inc., Kearny, NJ 07032, USA

<sup>b</sup> CIS Department, New Jersey Institute of Technology NJIT , Newark, NJ 07103, USA ( )

## Abstract

The systematic evolution of a hypermedia-based group decision support system GDSS architecture to supportŽ . collaborative medical decision-making MDM is presented in this paper. This GDSS is for subsequent use by designers andŽ . researchers in the GDSS<sup>r</sup>medical informatics arena who can use several or parts of the presented architecture for effecting collaborative MDM. The GDSS design also supports various levels of inference-based medical support ranging from the lower diagnostic levels to the higher clinical levels. The evolution of this architecture incorporated systematic research and investigation of the basic elements of the MDM process, associated procedures, tools and the potential impact of different characteristics of medical groups. This architecture incorporates clinical reasoning and problem-solving features identified through an analysis of the schools of MDM from a GDSS perspective. Identification of inadequacies from a collaborative MDM perspective of existing GDSS research frameworks and architectures has also influenced current architecture development. The inexact nature of cognitive processes that are inherent in MDM necessitated the incorporation of Acognitive-aid structuresB and the Acognitive appropriation processesB architectural components. The MEDICALWAREe<sup>1</sup> component, integrated with a GDSS is designed to provide problem-solving support, access to clinical algorithms and procedures, expert inference support and several MDM support tools with hypermedia functionality. Hypertext templates with semantic nodes and links provide group members the ability to modify templates for accommodating expected or unexpected variations in decision-making criterion in handling a clinical case. Group members can thus ascertain whether they have followed all required procedures and algorithms, and modify diagnostic procedures if necessary. Several facets of the GDSS architecture can be prototyped and field-tested, incorporating clinical algorithms and related diagnostic support tools. The GDSS architecture presented can also be used for empirical studies in collaborative MDM. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: GDSS; Medical decision-making; Diagnostic reasoning; Collaborative MDM; MEDICALWAREe; Hypermedia-based GDSS; Hypertext morphology; Cognitive processes; GDSS architecture

## 1. Introduction

The systematic effort involved in the development of a group decision support system GDSS architec-Ž . ture for collaborative medical decision-making Ž . MDM , requires a review and synthesis of the essential facets of a GDSS with the MDM process. This integration should retain the essence of the MDM process while simultaneously drawing on the benefits of a GDSS. Several treatises deal with the evolution of GDSSs and aspects related to the design, framework, and empirical studies 7,10,11,15, <sup>w</sup> 21,27,40–42,44,46,63,67,97 . One of the first formal<sup>x</sup> definitions of a GDSS, evolved from the research of DeSanctis and Gallupe:

A GDSS combines communication, computing, and decision support technologies to facilitate formulation and solution of unstructured problems by a group of people Ref. 18 , p. 589 .Ž <sup>w</sup> <sup>x</sup> .

DeSanctis and Gallupe identify three environmental contingencies as critical to GDSS design: group size, member proximity, and group task. The GDSS foundation framework, which incorporates these contingencies proposed by DeSanctis and Gallupe 18<sup>w</sup> <sup>x</sup> in 1987, can be considered as a working model for GDSS research. This GDSS research framework triggered a number of major GDSS theoretical research contributions in framework and architecture development. A GDSS can be considered as a system, which evolves over time, to realize its full capabilities. A group according to their needs can exploit the capabilities of a GDSS. These include features embedded in menus and use of rule-based structured decision models, which facilitate structured group processes in decision-making. The advancement of technology related to the areas of communication, computers, and decision support methodologies has further ad vanced GDSS research. Several GDSS research frameworks and architectures that have evolved since the foundation framework in 1987 have influenced current GDSS architecture development.

Although the medical literature describes the MDM process using different models indicative of the same goal, for purposes of the current research, a validated model, namely, the select and test ST -Ž . model for diagnostic reasoning Fig. 1 64,90 isŽ . <sup>w</sup> <sup>x</sup> chosen and described here. Diagnostic reasoning can be described as a process-based phased transformation from clinical evidence to a relevant diagnosis, where several types of inference-based reasoning such as deduction, induction, abstraction and abduction are at play at different stages 64,90 . During<sup>w</sup> <sup>x</sup> this transformation, cognitive processes are known to play a vital role 64,89,90 . Several instances of<sup>w</sup> <sup>x</sup> these processes can be present at any given time, involving the interplay of clinical reasoning, medical knowledge and evidence 102 . Raw patient data, usually incomplete is abstracted into clinical evidence Fig. 1 . UsingŽ . abduction, clinical evidence is then related to a set of pursuable hypotheses. Deduction is used to narrow down on deciding which clinical manifestation is prominent for certain hypotheses to be true. In this process, new laboratory or clinical examinations are requested to verify unobserved or unexpected disease manifestations.

![](/api/attachments/FNYTZNHU/fulltext/images/996b2aaa2a59f0f22b33688fdb232a1ad8e9095b383d30ac7134d5416e23fe20.jpg)  
Fig. 1. The ST-model for diagnostic reasoning Ref. 90 , p. 14 . Ž <sup>w</sup> <sup>x</sup> .

In an effort to provide easy traversal using the hypermedia nodes and links in the GDSS architecture, the natural hypermedia connotation that the ST-model Fig. 1 lends itself to has been utilized.Ž . The ST-model links are indicative of inference-based reasoning, namely, abduction, induction, deduction and abstraction. The observed data, expected data, clinical evidences and diagnostic hypotheses compartments can be viewed as hypermedia nodes, linked by inferential type nodes. These are simplistic or macro-level representations of clinical case information. These inferential links coupled with a universal system for classifying hypermedia nodes, namely, hypertext morphology Appendix B , have been used Ž . for link typing in the GDSS architecture. Without losing the essence of information navigation and representation of the ST-model, hypermedia nodes are definable Figs. 1, 4 for representing a clinicalŽ . case. These nodes can be mapped to various nodes of the ST-model Sec. 4 . Ž .

Fig. 2 has been derived from a literature review on the spectrum of medical reasoning and task support levels 5,90 . This revealed that different levels <sup>w</sup> <sup>x</sup> are characterized by varied techniques and reasoning constructs. These inferential-reasoning based diagnostic support levels have been derived from an analysis of the structure of the sciences using constructs related to exact<sup>r</sup>inexact theories–quantitative<sup>r</sup>qualitative scientific observation 5,90 . An<sup>w</sup> <sup>x</sup> analysis of Fig. 2 reveals that the lower levels of support dealing mainly with quantitative processvariables necessitate use of mathematical techniques, simulation models, etc. These may be indicative of causality such as observed in translating physiological processes into compartmental models 9,49 .<sup>w</sup> <sup>x</sup> The intermediate level of medical support is representative of a mixture of causal and associative reasoning and is characterized by mixed formalisms of traditional qualitative and quantitative models. At the clinical level, more of associative reasoning seems to be indicated, rather than causal reasoning due to the lack of generalizable models to represent disease-patterns observed in clinical data 5 . At this<sup>w</sup> <sup>x</sup> level, causality becomes hard to distinguish, manipulate, correct and control for. Associative reasoning between objects and processes seems to fill the void left by causality at the clinical level 5 . Although statistical tools cannot be applied for all problems that occur at the clinical level, mathematical and statistical results, combined with personal judgment and course of action are used in clinical decisionmaking.

Given the applicability of various techniques and reasoning methods at different levels of medical support, current GDSS architecture development efforts incorporated an analysis of the schools of MDM techniques from a GDSS perspective. The objective of this analysis Sec. 2 is to provide a medical group Ž .

![](/api/attachments/FNYTZNHU/fulltext/images/060deb3bdd9ebbd7e3ec934ed1c5a2fada03343b5d9431cd269c3dcfd00e2f36.jpg)  
Fig. 2. Medical support levels and associated properties of prominent interacting features.

the flexibility to choose from a variety of MDM techniques depending on the nature of reasoning. Facilitating integrated functioning of MDM techniques coupled with GDSS interaction can cater to different levels of medical support and also assist in group member adaptation to a spectrum of medical group and problem-solving patterns. The GDSS architecture Sec. 5 does not conform to either a strictŽ . causal or associative-reasoning based connotation, due to the influence of the three support levels that the architecture attempts to interact with Fig. 2 . Ž . These support levels combined with the interacting features are applicable to the design of any medical reasoning system or architecture.

Medical personnel such as physicians, interns, nurses, diagnostic<sup>r</sup>research laboratory personnel and social workers provide varied degrees of support at different stages of the diagnostic reasoning process Ž . Fig. 1 . Within the physician category, several classes such as the field of expertise and years of experience play a critical role. A physician’s expertise can range from family medicine to several subspecialties in internal medicine such as cardiology, endocrinology, immunology and infectious diseases. The practicalities of information exchange between medical group members Fig. 1 , necessitatesŽ . synchronous Ž . Žsame time or asynchronous different time exchange of clinical data. This is more so for. clinical support in medical specialties such as cardiology, urology, and several clinical complications, especially those of multi-system<sup>2</sup> diseases whose pathophysiology and nature of origin necessitates examination of results of several diagnostic procedures 17 . The sharing of knowledge among certain<sup>w</sup> <sup>x</sup> or all the group members is an effort towards arriving at a group consensus related to a relevant diagnosis, effecting follow-up or diagnostic intervention procedures. Apart from this information exchange, in practice, relevant decision-making tools and techniques also assist the MDM process at various reasoning stages Fig. 1 . These decision-making toolsŽ . and techniques can be related to one or several schools of MDM Table 2 . A GDSS for MDMŽ . should include customizable support structures for handling these issues. In traditional GDSS use outside the health-care arena, such requirements may not arise, thus, making the collaborative MDM problem-domain unique in many ways.

Apart from the issues mentioned above, current research has identified several GDSS support features for the collaborative MDM process Table 1 .Ž . The structures and support processes for a hypermedia-based GDSS architecture for MDM should draw upon the mutual features listed in Table 1. Designers and researchers in the GDSS<sup>r</sup>medical informatics arena can use one or several features supported by this architecture Sec. 5 . This architecture can caterŽ . to clinicians orchestrating their diagnostic skills augmented by their acquired medical knowledge and experience.

GDSS support for a problem-solving dimension should attempt to provide GDSS structures and mechanisms to lower a problem’s complexity level <sup>w</sup> <sup>x</sup> 44 . In this context, the asynchronous problem-solving dimension necessitates a different perspective compared to the synchronous dimension Sec. 3.1Ž . <sup>w</sup> <sup>x</sup> 44 . The cognitive appropriation mechanism described in Sec. 5.3 is designed to facilitate the asynchronous problem-solving effort through the use of cognitive-aid structures by a group. The task domain has been characterized by contributions from several researchers with different perspectives, due to the nature of different problem-domains 44,56,57,84 .<sup>w</sup> <sup>x</sup>

Given the support levels that a GDSS for MDM can ideally cater to, technologies with varying degrees of impact, ranging from the Internet, expert systems, hypermedia-based diagnostic information retrieval tools and analytical MDM procedures<sup>r</sup>tools necessitate integration. Apart from a technology perspective, other basic collaborative decision-making features that necessitate architecture integration include context of decision-making, medical group member characteristics, and clinical reasoning features with respect to different medical tasks 84 . <sup>w</sup> <sup>x</sup> Currently, medical collaboration 12 is not sup- <sup>w</sup> <sup>x</sup> ported by formal guidelines. Although prior research has focused on the development of a DSS framework <sup>w</sup> <sup>x</sup> 74 , GDSS research at NJIT has enriched the development efforts of this architecture 40,44,96,97 . Re-<sup>w</sup> <sup>x</sup> search on hypermedia-support structures 73,75,98 <sup>w</sup> <sup>x</sup> for management of hyper-link issues has also influenced the current architecture development. Depending on the context and MDM problem being deliberated upon, trade-off between GDSS architecture design and leadership issues is addressable. A GDSS need not be necessarily viewed as leader-oriented, provided the software component augments the required architecture or process guidance that a leader can provide 44,97 .<sup>w</sup> <sup>x</sup>

Table 1  
Salient collaborative MDM features and supporting GDSS featur

<table><tr><td></td><td colspan="2">Salient collaborative MDM features</td><td>Supporting GDSS feature</td><td>Selected author(s) for MDM/GDSS</td></tr><tr><td>1</td><td colspan="2">Temporal representation</td><td>Customizable GDSS temporal markers, list-features, GDSS/database interaction.</td><td>Kahn [47], Rennels [80], Hiltz and Turoff[40], Turoff [97]</td></tr><tr><td>2</td><td colspan="2">Prior research/factual reference</td><td>Ability to support integration of hypermedia links and development of semantic templates interacting with knowledge bases and databases.</td><td>Breslow [8], DeSanctis and Gallupe [18], Lindley [52], Dempster et al. [20], Rennels [80], Turoff et al. [99]</td></tr><tr><td>3</td><td colspan="2">Knowledge-base interaction</td><td>Ability to support integration of structured decision-making rules, domain-specific knowledge bases and expert-system shells.</td><td>Efraim [23], Shortliffe et al. [86], DeSanctis and Gallupe [18]</td></tr><tr><td>4</td><td colspan="2">Multiple criteria decision-making (MCDM)</td><td>Ability to support integration of MCDM techniques, decision-making techniques.</td><td>Rubinstein [83], Zachary [106], DeSanctis and Gallupe [18]</td></tr><tr><td>5</td><td colspan="2">Medical task integration support</td><td>Ability to support and define task-types based on complexity levels, task nature uncertainty levels.</td><td>DeSanctis and Gallupe [18], Golden [31], McGrath [57], Mennecke and Wheeler [56], Sampson and Marthas [84], DeSanctis [18]</td></tr><tr><td>6</td><td colspan="2">Emergent/hidden decision profiles</td><td>Ability to tailor structures for the support of mechanisms such as structuration theory-based mechanisms, e.g., adaptive structuration theory (AST) and cognitive appropriation (Sec. 5.3). These can capture emergent/hidden decision profiles.</td><td>DeSanctis and Poole [19], Poole and DeSanctis [71], Fjermestad and Hiltz [27], Giddens [29], Hiltz et al. [43], Appendix A</td></tr><tr><td>7</td><td colspan="2">Individual decision-making styles</td><td>Ability to support methods that encourage individual member participation. These include, response activity, notebooks, messages, information exchange using pen names and anonymous reply, personal conference areas and facilitator monitored group activities.</td><td>Kahneman and Tversky [48], Tversky and Kahneman [101], Hiltz and Turoff [40,44], Turoff [97]</td></tr><tr><td rowspan="4">8</td><td rowspan="4">Group cognition support</td><td>Cognitive/decision models</td><td>Ability to integrate structured decision support methods such as the Delphi, NGT, social judgment analysis, etc., that support generation of simulation, mathematical, and cognitive models.</td><td>Patel et al. [64], Patel and Groen [65] Cirincione [16], Hiltz and Turoff [44], Sengupta and Te’eni Dov [85], Turoff and Hiltz [100], Linstone [53]</td></tr><tr><td>Collective intelligence</td><td>With the support accorded by cognitive or decision models, ability to provide an appropriate communication structure for use by a group of humans, using which a group can exhibit a collective decision capability at least as good as or better than any single member of the group.</td><td>Hiltz and Turoff [44]</td></tr><tr><td>Collective judgment</td><td>With appropriate built-in structured decision rules and structures, the ability of a GDSS to provide for interacting groups to reach the level of accuracy of judgment comparable to their most capable members.</td><td>Hackman and Morris [35], Cirincione [16], Gallupe [28], Hiltz and Turoff [44]</td></tr><tr><td>Cognitive feedback</td><td>With the support accorded by techniques used to generate cognitive, decision or judgment models, ability to generate feedback, using which groups can work incrementally toward a judgment policy that all members believe reflects the best accommodation of their intuition and analysis.</td><td>Blazer et al. [4], Cirincione [16], Gallupe [28], Sengupta and Te’eni Dov [85]</td></tr></table>

Efforts towards the creation of a system to demonstrate key concepts of the presented GDSS architecture are underway for a specific MDM problem. Several successful past and current GDSS systems based on salient characteristics of the current architecture deserve mention 97 . Some of these are <sup>w</sup> <sup>x</sup> Emergency Management Information System and Reference Index EMISARI , Electronic InformationŽ . Exchange System IIEIESŽ . <sup>r</sup>EIES II , TOURS-Hypertext and Virtual Classroom-Hypermedia EIES II Ž . VC-Hypermedia EIES II 44,97 .<sup>w</sup> <sup>x</sup>

Having provided an introduction to the theoretical implications of the different support levels and other related GDSS issues, the subsequent sections present the GDSS architecture development methodology in a systematic manner in six sections. Sec. 2 focuses on the results of an analysis of the schools of MDM from a GDSS perspective. This analysis leads to Sec. 3, which presents MEDICALWAREe, an integral part of the GDSS architecture. Sec. 4 discusses the role and methodology used for the development of semantic hypermedia links for the support of diagnostic reasoning tasks. In Sec. 5, the GDSS architecture is presented. Sec. 6 presents the potential benefits that can be realized through the implementation of a prototype, which supports key elements of the architecture.

## 2. An analysis of the schools of MDM from a collaborative communication perspective

The analysis presented in this section preceded the GDSS architecture development in order to elucidate strengths and weaknesses of MDM techniques from a GDSS perspective. The following two aspects were chosen for this analysis:

Ž .a selection of prominent collaborative MDM features and

Ž . b support for the selected collaborative MDM features by MDM techniques.

2.1. Selection of prominent collaboratiÕe MDM features

The medical<sup>r</sup>GDSS literature does not explicitly isolate a set of prominent collaborative MDM features. This necessitated efforts towards identification of a set of prominent collaborative MDM features. The selection methodology involved a two-step process. The first step involved identification of prominent collaborative MDM features when a medical group interacts, with subsequent verification of the support that can be accorded for these features by a GDSS Table 1 . The second step, which involvedŽ . the verification process, involved a synthesis, comparison, and integration of the collaborative MDM features with supporting GDSS characteristics identified in the GDSS literature. In the first step, several characteristics could be isolated such as temporal representation, prior research<sup>r</sup>factual connotation support, use of multiple criteria decision-making Ž . MCDM techniques, etc. The impact of these characteristics on a group using a clinical algorithm with GDSS-support technologies is described with examples later in this section.

When medical group members interact at various stages of the diagnostic reasoning process Fig. 1 Ž . several collaborative MDM features listed in Table 1 are at play, due to the presence of several instances of this process. Current research on the high-level design of hypermedia nodes for representing a clinical case Fig. 4 and the subsequent mapping forŽ . establishing a relationship with the diagnostic reasoning process also provided assistance in isolating prominent collaborative MDM features. The synthesis and integration of the cognitive nature of the diagnostic reasoning process 65,90 , and cognitive<sup>w</sup> <sup>x</sup> studies in GDSS 16,44,85,100 resulted in the iden-<sup>w</sup> <sup>x</sup> tification of the group cognition feature. Cognition features such as collectiÕe intelligence, collectiÕe judgment, cognitiÕe feedback and cognitiÕe<sup>r</sup>decision model support have been grouped under group cognition support Table 1 . These features essen- Ž . tially deal with their ability to influence a group’s decision-making capability. Cognitive processes are encountered at several stages of the diagnostic reasoning process. Cognitive processes can overwhelm clinicians when it becomes difficult for them to find clues related to the identification of a clear-cut method for associating different types of clinical data.

The cognitive problem facing the physician is how to take the available clinical data in a given case, which are disparate in kind and reliability and to wring from them in the light of personal knowledge the appropriate conclusions, whether they pertain to diagnosis, treatment choice or case management Ref. 5 , p. 847 .Ž <sup>w</sup> <sup>x</sup> .

Acquired medical knowledge and experience plays a leading role in inferring the condition of a patient and to relate different types of data with various active or inactive hypotheses 24,25 . Cognitive pro-<sup>w</sup> <sup>x</sup> cesses are dependent on the information complexity in a clinical case and the nature of these processes cannot be generalized due to the inherent specificity of clinical cases 24,25,61,93 .<sup>w</sup> <sup>x</sup> MEDICALWAREe features Fig. 3 are intended to minimize this speci- Ž . ficity component by providing relevant diagnostic reasoning and computational tools.

Emphasis was placed by more than one school of MDM Table 2 on aspects related to group cogni- Ž . tion. Collective judgment, also known as group judgment in GDSS literature can be described as the ability of interacting groups to reach the level of accuracy of judgment comparable to their most capable members 35 . Collective Intelligence can be<sup>w</sup> <sup>x</sup> defined as a group characteristic with

. . . the possibility for a group of humans utilizing an appropriate communication structure to exhibit a collective decision capability at least as good as or better than any single member of the group ŽRef. 44 , p. 44 .<sup>w</sup> <sup>x</sup> .

## Cognitive feedback, can be described as

. . . the feedback available from sources such as judgment or decision models, using which groups can work incrementally toward a judgment policy that all members believe reflects the best accommodation of their intuition and analysis 4,16,28 .<sup>w</sup> <sup>x</sup>

An appropriate communication structure effected by the cognitive appropriation mechanism Sec. 5.3Ž . is provided to facilitate these group cognition features.

The basic information gathering that a physician deals with religiously has been represented in the form of hypermedia nodes in Fig. 4. Key medical concepts related to the features listed in Table 1 can be explained with examples using a clinical algorithm 14 Fig. 5 . A patient presenting with symp-  Ž . toms of heart failure can have a history of visits to a hospital. The recording of information Fig. 4 dur-Ž . ing these visits necessitates storage of patient diag nostic information such as ECGs, angiograms, etc. using temporal representation for subsequent retrieval and reference. In evaluating and treating patients with heart failure, several experts can be involved 14 . Before reaching the stage of decisions related to significant positive findings with respect to physiological tests, several prior decision points require use of medical knowledge listed in the algorithm. The knowledge used in reaching intermediate decision points, potentially generates decision mod els such as diastolic dysfunction at a specific visit Ž . ejection fraction , alternative diagnoses identified with respect to symptoms of heart failure, etc. 14 .<sup>w</sup> <sup>x</sup> These decision models are nothing but models of medical knowledge and can be considered as cognitive models due to the use of personal judgment, knowledge, and experience in generating these models. Using the GDSS architecture presented, complicated heart failure cases coupled with other multi-system diseases such as blood pressure, hypertension, kidney-related diseases, etc. can be deliber ated upon synchronously or asynchronously. Due to the diversity of group members who handle such clinical cases Fig. 6 , a GDSS can influence issuesŽ . related to individual decision-making styles, collec tive intelligence, collective judgment, cognitive feedback and support generation of cognitive<sup>r</sup>decision models Table 1 . Parts or the entire algorithm listedŽ . in Fig. 5 can be accorded rule-based expert-system support for the generation of decisions. This interaction can enrich a knowledge base with new facts and a group’s expert feedback. Use of MCDM techniques for handling cases with manifestations of multi-system diseases, can benefit from probability weights on various decision points. The decision points can be associated with generated decision models, thereby facilitating choice of the best course of treatment. Several other examples and basic concepts of clinical cases can be found in classic medical textbooks and clinical literature 2,8,94 . Combin-<sup>w</sup> <sup>x</sup> ing hypermedia support, a group member using cognitive models can intuitively request for and verify several treatment and diagnostic options. This effort provides the ability to explore plausible options before choosing the optimal or best action based on interacting patient data.

![](/api/attachments/FNYTZNHU/fulltext/images/656936bb98d5cb3e6a28c70e59981a2069ef3a39294ba8f0514eb35c85fc6726.jpg)  
Fi<sub>g</sub>. 3 . A GDSS <sub>an</sub>d MEDICALWARE <sup>e</sup> f<sub>or</sub> b<sub>u</sub>ildi<sub>ng mo</sub>d<sub>e</sub>l<sub>s o</sub>f <sub>me</sub>di<sub>ca</sub>l k<sub>now</sub>l<sub>e</sub>d<sub>ge an</sub>d di<sub>agnos</sub>ti<sub>c pro</sub>bl<sub>em</sub>-<sub>so</sub>l<sub>v</sub>i<sub>ng</sub>.

Table 2  
A comparison of the various schools of MDM with salient GDSS features

<table><tr><td rowspan="3">School of decision-making</td><td rowspan="3">Sub-schools of decision-making</td><td rowspan="3"></td><td colspan="11">Salient group decision support perspectives</td></tr><tr><td rowspan="2">a</td><td rowspan="2">b</td><td rowspan="2">c</td><td rowspan="2">d</td><td rowspan="2">e</td><td rowspan="2">f</td><td rowspan="2">g</td><td colspan="4">h</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Cognitive psychology</td><td></td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="3">Decision analysis</td><td>Decision trees</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="2">Sensitivity/specificity methods</td><td>Predictive value criterion</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Roc analysis</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Utility theory</td><td>Multiple attribute utility model (MAUM)</td><td></td><td>x</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>x</td></tr><tr><td rowspan="6">Forecasting</td><td rowspan="2">Qualitative methods</td><td>Delphi method</td><td>✓</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Panel consensus</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>✓</td><td>x</td></tr><tr><td>Causal methods</td><td>Regression model</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="3">Time-series methods</td><td>Box-jenkins</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Exponential smoothing</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Moving average</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="7">Statistics</td><td rowspan="2">Statistical models</td><td>Bayesian model</td><td>✓</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>✓</td></tr><tr><td>Regression analysis</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>✓</td><td>x</td></tr><tr><td>ANOVA</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Cluster analysis</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Discriminant analysis</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Factor analysis</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Non-parametric methods</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Mathematics</td><td></td><td></td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="2">Simulation</td><td>Monte-Carlo method</td><td></td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>✓</td></tr><tr><td>Markov models</td><td></td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>✓</td></tr><tr><td>Algorithmic</td><td></td><td></td><td>x</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Artificial intelligence (AI)</td><td></td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

Ž . Ž . Ž . Ž . a Temporal representation support; b prior research<sup>r</sup>factual connotation support; c support for knowledge-base interaction; d multiple-criteria decision-making; e medical task integration support; f support for emergentŽ . Ž . Ž . <sup>r</sup>hidden decision profiles; g support for individual decision-making styles; and h group cognition support. Ž .  
Ž . Ž . Ž . Ž . h.1 Cognitive<sup>r</sup>decision models; h.2 collective intelligence; h.3 collective judgment; and h.4 cognitive feedback.

## 2.2. Support for the selected collaboratiÕe MDM features by MDM techniques

In order to isolate prominent techniques belonging to the various MDM schools, research into state-ofthe-art MDM techniques and associated clinical reasoning processes were performed 76 . This research<sup>w</sup> <sup>x</sup> involved a literature search 1960–1996 using theŽ . FULLMEDLINE<sup>w</sup> database and prominent biomedical information technology-oriented literature and books. The analysis also utilized the classification of decision-making techniques adopted in classic textbooks 39,54 . The analysis Table 2 was primarily <sup>w</sup> <sup>x</sup> Ž . based on the potential that an MDM technique has for lending support to the collaborative MDM features listed in Table 1. The analysis revealed that several schools of MDM have emerged Table 2 Ž . since the first instance of providing logical and computer support for medical diagnosis in 1955 using Mathematical and computational tools 54,55 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/FNYTZNHU/fulltext/images/d4ff7eabce3e3f2e1c1dcf8234e47e843ebb44b4b51472a45afbbefe9ff38d93.jpg)  
Fig. 4. Representative higher-level classification of hypertext nodes for depicting a clinical case.

Due to the lack of classification methods in at least one school of MDM, namely, the Forecasting school, techniques pertaining to this school were viewed from an Operations research perspective 39 . This<sup>w</sup> <sup>x</sup> analysis and review led to the identification of nine major schools of MDM with several sub-schools representative of MDM Table 2 . Since the lateŽ . 1950s, due to overlap in perspectives between schools of MDM, a clearly demarcated boundary between the schools of MDM could not be identified TableŽ 2 . However, Mathematical theory and logic were. identified as the basis for Simulation and Mathematical models 105 . A number of techniques Table 2<sup>w</sup> <sup>x</sup> Ž . can be classified in one or more of the Forecasting, Statistics, Simulation and Mathematical schools. To illustrate this perspective, the work of authors such as Carson 9 , Leaning 51 and Summers 91 on<sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> physiological modeling and CPN Causal Probabilis-Ž tic Networks can be classified as belonging to the . Forecasting, Simulation and Mathematical schools of MDM. Analysis efforts are underway to summarize the results of this literature review 79 .<sup>w</sup> <sup>x</sup>

The analysis revealed that simulation of several facets of the MDM process can be performed with the aid of techniques from different schools of MDM thought 3,4,6,9,32,50,51,54,55,88,91,93,103,104 .<sup>w</sup> <sup>x</sup> Several techniques such as the Delphi method 100<sup>w</sup> <sup>x</sup> have been used as a formal method of decision-making since the mid-1970s to support collaborative decision-making. The Delphi method and techniques from the AI school support group cognition features due to their group-cognition oriented nature TableŽ

![](/api/attachments/FNYTZNHU/fulltext/images/5b62b6c13f084ccb0673d4b6663684cecb87775144a1a1b4cbf6be5e5bdf2c26.jpg)  
Fig. 5. Clinical algorithm for evaluation and care of patients with heart failure Ref. 14 , p. 114 .Ž <sup>w</sup> <sup>x</sup> .

2 . This analysis also revealed that statistical meth-. ods provide little or no support for collaborative MDM. No single technique or school of MDM can be regarded as the most suitable for collaborative MDM Table 2 and there are a number of benefitsŽ . as well as shortcomings associated with these techniques. However, these techniques assist in the translation of medical phenomena into interpretable decision-making<sup>r</sup>cognitive models for the generation of plausible solutions to counter one or several phenomena, occurring synchronously or asynchronously. Such simulation attempts have not addressed the handling of collaborative synchronous<sup>r</sup> asynchronous communication issues. Although group decision-making is wide spread in medicine, limitations in technology and other factors inhibited the growth of GDSS for MDM 75 . MDM also entails<sup>w</sup> <sup>x</sup> varied problem contexts and interaction of several medical specialties representing unique complexities related to reasoning and problem solving.

Given such complexities in collaborative MDM, a GDSS architecture-based approach to integrate and operationalize various aspects with respect to tasks, context, groups, decision-making tools and procedures, cognitive issues Table 1 ,Ž . synchronous<sup>r</sup> asynchronous group communication issues, etc. is necessary. A GDSS architecture-based approach also places in perspective other issues in MDM such as information validation, reliability, temporal representation 47,80 , medical knowledge representation <sup>w</sup> <sup>x</sup> standards 45 , medical literature search necessities, <sup>w</sup> <sup>x</sup> expert inference mechanisms 87 , use of hyperme-<sup>w</sup> <sup>x</sup> dia-supported medical procedures, etc.

![](/api/attachments/FNYTZNHU/fulltext/images/09d45bee2352d55f74af84aa27376338f749ee8e4bf20da1e88fff7cbe06c948.jpg)  
Fi<sub>g</sub> . 6. A h<sub>yperme</sub>di<sub>a</sub>-b<sub>ase</sub>d GDS S <sub>arc</sub>hit<sub>ec</sub>t<sub>ure</sub> f<sub>or co</sub>ll<sub>a</sub>b<sub>ora</sub>ti<sub>ve me</sub>di<sub>ca</sub>l d<sub>ec</sub>i<sub>s</sub>i<sub>on</sub>-<sub>ma</sub>ki<sub>ng</sub> .

In this context, a summary of critical issues that forms the basis for the development of the GDSS architecture for MDM are listed below 58,60 :<sup>w</sup> <sup>x</sup>

v Need for synchronous same time or asyn-Ž . chronous different time access to a relevant clini- Ž . cal problem-solving tool to proceed from medical evidence to diagnostic reasoning.

v The difficulties faced in the selection of relevant formal model s for problem solving. Ž .

v The lack of an intelligent electronic communication medium for comparison of clinical data using different problem-solving approaches based on contextual factors.

v The lack of an electronic communication medium for accommodating varied information-processing styles among different physicians.

v The difficulties faced in eliciting expert consultation in various medical disciplines, due to the asynchronous nature of medical groups.

v The micro-level cognitive complexities in clinical reasoning.

v Integration of various computer resources such as expert systems, simulation<sup>r</sup>modeling, and other computational tools used in MDM.

v Rising cost of telemedicine incorporating formal collaboration.

The analysis presented in Table 2 was extended to a review of major GDSS frameworks and architectures. Table 3 details a comparison of major GDSS research frameworks<sup>r</sup>architectures reviewed based on prominent features relevant for MDM. This comparison Table 3 was used as a basis for the de-Ž . velopment of the hypermedia based medical-GDSS architecture. The comparison is by no means an exhaustive one. This essentially represents the essence of the field from a MDM perspective. The reader is referred to Fjermestad and Hiltz 27 for an<sup>w</sup> <sup>x</sup> exhaustive comparison of GDSS frameworks, related research and empirical variables used by various authors in GDSS experimental research. In addition to general GDSS characteristics Table 3 , salient Ž .

features used in the analysis of the schools of MDM were used in the comparison of these frameworks<sup>r</sup> architectures Table 3 . This comparison was a majorŽ . referential influence on the GDSS architecture presented in this paper. For future validation purposes, features of these frameworks<sup>r</sup>architectures reflect what the current architecture will be measured against. Several GDSS frameworks<sup>r</sup>architectures, assisted this research in adapting features offered by a GDSS, while simultaneously allowing for customizations required from a collaborative MDM perspective.

A key outcome of the analysis, namely, the shortcomings of the schools of MDM from a GDSS perspective, motivated the development of the MED-ICALWAREe concept with hypermedia functionality. The architecture, design features of the MEDI-CALWAREe component and interaction issues with the GDSS architecture are presented in Sec. 3.

## 3. MEDICALWAREe: architecture and GDSS integration issues

The information base associated with the field of medicine and its several specialties has been doubling every 5 to 10 years 17 . Hence, the number of<sup>w</sup> <sup>x</sup> medical sub-specialties has also been growing, while the number of physicians knowledgeable in a multitude of specialties has been declining. In addition, handling diagnostic reasoning problems related to varied clinical manifestations, different physiological systems, and clinical complications, especially those of multi-system diseases whose pathophysiology origin may be unclear 17 , necessitates some degree of<sup>w</sup> <sup>x</sup> flexibility of access to procedures, tools, and algorithms.

The design of an integral GDSS component for MDM, for handling different medical support levels Ž . Fig. 2 , should not only encompass procedures and algorithms from various medical sub-specialties, but also provide access to relevant tools. Adaptability of a decision-making tool is required to successfully provide insight into a clinical problem. In this context, the MEDICALWAREe component Fig. 3 , an Ž . integral part of the GDSS architecture encompassing several of the salient aspects mentioned above is discussed here. The MEDICALWAREe component can be described as follows:

T<sub>a</sub>bl<sub>e</sub> 3  
Comparison of maj or GDS S research architecturesrframeworks reviewed

<table><tr><td rowspan="2">Framework</td><td rowspan="2">a</td><td rowspan="2">b</td><td colspan="8">Cognitive-aid structures</td><td>d</td><td>e</td><td>f</td></tr><tr><td>c.1</td><td>c.2</td><td>c.3</td><td>c.4</td><td>c.5</td><td>c.6</td><td>c.7</td><td>c.8</td><td></td><td></td><td></td></tr><tr><td>DeSanctis and Gallupe, 1987 [18]</td><td>Three factors (group size, member proximity, task type)</td><td>Yes (member proximity, group size)</td><td>x</td><td>✓</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>✓</td><td>Levels 1, 2, 3</td><td>McGrath/activity-driven</td><td>x</td></tr><tr><td>Jelassi and Beauclair, 1987 [46]</td><td>Two factors (Time [synchronous-asynchronous], member proximity [ftf, dispersed])</td><td>Partial (member proximity [ftf, dispersed], time [synchronous, asynchronous, teleconferencing to e-mail])</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td>Levels 1, 2</td><td>McGrath/technique-driven</td><td>x</td></tr><tr><td>Hiltz et al., 1991 [43]</td><td>Three factors (group size, member proximity [ftf, dispersed, asynchronous], task type)</td><td>Modified contingency perspective (group size, member proximity [ftf, dispersed, asynchronous])</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>✓</td><td>Levels 1, 2, 3</td><td>McGrath/activity-driven</td><td>x</td></tr><tr><td>Hiltz et al., 1991 [43]</td><td>Seven factors (GDSS, task, individual, group, group/process adaptation characteristics, resultant communication dimensions, outcome variables)</td><td>Modified contingency perspective (proximity [ftf, dispersed], group size, time [synchronous-asynchronous])</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>Levels 1, 2, 3</td><td>McGrath/activity-driven</td><td>x</td></tr><tr><td>Chen and Liou, 1991 [10]</td><td>Six factors (technology, group, task, process, organization and environment variables)</td><td>Modified contingency perspective (group size, proximity [ftf, non-ftf], time [synchronous, asynchronous])</td><td>✓</td><td>✓</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>Levels 1, 2, 3</td><td>Modified McGrath/activity-driven</td><td>x</td></tr><tr><td>Dennis et al., 1988 [21]</td><td>Six factors (group, task, context and EMS characteristics, group process and group meeting outcome variables)</td><td>Modified contingency perspective (proximity [multiple individual sites, one group site, multiple group sites], time dispersion [same time, different time], group size)</td><td>x</td><td>✓</td><td>✓</td><td>x</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>Levels 1, 2, 3</td><td>Modified McGrath/activity-driven</td><td>x</td></tr><tr><td>Pinsonneault and Kraemer, 1989 [67,68]</td><td>Four factors (contextual, group process, task outcome and group outcome variables)</td><td>Modified contingency perspective (group and room size, interpersonal distance)</td><td>x</td><td>x</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>Not applicable</td><td>McGrath/Keen&#x27;s structural dimension</td><td>x</td></tr><tr><td>Hatcher, 1990 [38]</td><td>Four factors (decision tools, information extraction, decision philosophy and information exchange)</td><td>Modified contingency perspective (synchronous, asynchronous)</td><td>x</td><td>✓</td><td>✓</td><td>x</td><td>x</td><td>x</td><td>x</td><td>✓</td><td>Levels 1, 2, 3</td><td>Activity-driven</td><td>✓</td></tr></table>

Ž . Ž . Ž . Ž . Ž . Ž . a B asic framework factors <sub>;</sub> b su<sub>pp</sub>ort for contin<sub>g</sub>enc<sub>y p</sub>ers<sub>p</sub>ective <sub>;</sub> c co<sub>g</sub>nitive-aid structures : c . 1 h<sub>yp</sub>ermedia- su<sub>pp</sub>ort<sub>;</sub> c . 2 <sub>g</sub>eneration of decisionrco<sub>g</sub>nitive model s <sub>;</sub> Ž . Ž . Ž . Ž . Ž . Ž . c . 3 tem<sub>p</sub>oral markers su<sub>pp</sub>ort<sub>;</sub> c .4 semantic h<sub>yp</sub>ertext-based re<sub>p</sub>resentation <sub>;</sub> c . 5 ex<sub>p</sub>ert-inference su<sub>pp</sub>ort<sub>;</sub> c . 6 <sub>p</sub>rior research findin<sub>g</sub>s <sub>;</sub> c . 7 co<sub>g</sub>nitive feedback<sub>;</sub> c . 8 multi-criteria decisions <sub>;</sub> d decision level so<sub>p</sub>histication <sub>;</sub> e task t<sub>yp</sub>e Ž . Ž . Ž . r activit<sub>y</sub>-based su<sub>pp</sub>ort<sub>;</sub> and f s<sub>p</sub>ecific for medical a<sub>pp</sub>lications rdecision-makin<sub>g</sub> .

An integrated tool-chest of medical problem-solving tools, clinical algorithms and procedures, assembled from various medical specialties and schools of medical decision making. Working in conjunction with a hypermedia-supported collaborative communication environment and a database, MEDICALWAREe provides insight and solutions for clinical decision-making by supporting the generation of cognitive<sup>r</sup>decision models of medical knowledge and providing for several clinical reasoning support tools, with hypermedia functionality.

Depending on the level of medical support required, MEDICALWAREe allows for the selective use of tools from different sub-components. The four major MEDICALWAREe sub-components that interact with each other are:

Ž .a problem-solving support sub-component;

Ž . b clinical algorithms and procedures sub-component;

Ž .c expert inference support sub-component; and Ž . d other hypermedia-supported MDM support tools.

These are described below.

## 3.1. Problem-solÕing support sub-component

Problem-solving support derived from simulation tools Monte-Carlo method, Markov process-based, Ž etc. 49,88 , utility theory tools MCDM techniques , <sup>w</sup> <sup>x</sup>. Ž . statistical interventions, etc. allow for the analysis of patient data. Use of decision analysis tools decision Ž tree generators, etc. , provides support for decision- . making under conflict, risk, certainty and uncertainty <sup>w</sup> <sup>x</sup> 83 with the added benefits of a GDSS synchronous <sup>r</sup>asynchronous interaction. The integrated use of techniques in this sub-component captures events that have usually more than one outcome. For specific clinical problems, several tools can be custom programmed. This process can subsequently lead to further refinement of tools, where the tools for a specific problem domain attain a certain level of maturity. Interacting with the clinical algorithms and procedures sub-component, the clinical content and case-specific cognitive models have several attributes. These attributes are related to the treatment time-points, author, versions, location of information used for cognitive model generation, tools used, relationship with other objects used-by, strength,Ž creator, level of agreement, popularity of link , infor-. mation currency, model relevancy with diagnoses made, completeness of model, uniqueness and so on. This can generate varied perspectives about a patient’s state in a clinical algorithm.

Different categories of models such as static, dynamic, and transient models evolve in this process. Conventions for the model building process such as when, where, and how to build and use these models will be dependent on the medical problem. A core set of rules however need to be developed, which can assist group members on the basics of collaborative model building, the nature of the model being generated etc. A selected tool from the schools of MDM, need to be assigned attributes such as associated techniques, language, and decision model assembly methods used. These will be related to group member responses to a series of questions on the nature of available data, requirements, expectations, etc. A static model is one whose nature will not change when different sets of the same data are reapplied to it. Dynamic models when retrieved at a later context, with different sets of data will be able be regenerate itself using the same sequence steps that were used to generate the original model. Transient models are intermediate models that evolve during static or dynamic model generation. Model generation sequences can be repeatable for model building. The recommender and generator features discussed in Sec. 3.4 can be customized for model validation purposes.

There is no guarantee that a cognitive model will be useful for a group. This drawback can be minimized by the inclusion of rules in the model generation step, that specify use of validated data, methods of physiological simulation, model complexity indices, model splitting techniques in case a model becomes too complex and inter-model relationships.

The asynchronous problem-solving process is quite different from the synchronous process. Hiltz and Turoff 44 describe the classic real-world asyn-<sup>w</sup> <sup>x</sup> chronous problem-solving process using the threefactor dimension model. The three factor dimensions are the complexity, Õalidity, and the coordination dimensions. Several parts of the medical problem described in Sec. 2.1 are classifiable using factors in the complexity dimension such as structured, semistructured, unstructured and wicked. The Õalidity dimension uses factors related to deductive and inductive processes in addition to factors such as relative, negotiated, and conflictive 44 . The <sup>w</sup> <sup>x</sup> coordination dimension represents possible different approaches for the coordination and synchronization of group activities. These include parallel, pooled, sequential and reciprocal 44 . The interaction between<sup>w</sup> <sup>x</sup> the problem-solving and clinical algorithm sub-components provides valuable referential decision-making support for group members for ensuring that all the critical aspects of a clinical algorithm have been addressed and accounted for. This approach is indicative of a combination of the sequential and reciprocal factors of the coordination dimension of the three-factor model 44 . This essentially imposes<sup>w</sup> <sup>x</sup> phases on the problem-solving process that must be adhered to in a sequential manner by group members, before proceeding to the next stage. The semantic hypertext template-based approach Sec. 3.2 sup-Ž . ports this strategy.

The problem-solving process attempts to lower a problem’s complexity level by using tailored structures. Use of appropriate structures and their relationships is an arbitrary and subjective decision of the group facilitator, a group’s leader, the collective group or certain group members 97 . In several less<sup>w</sup> <sup>x</sup> complex clinical cases, the requirement for a problem-solving tool may not arise. The MEDICAL-WAREe component is best utilized for providing analysis methods and on-going support for complex clinical cases that require synchronous<sup>r</sup>asynchronous collaboration modes. For handling clinical cases of lesser complexity, where problem-solving tools are not necessitated, the temporal feature associated with the database in MEDICALWAREe can be used. This feature can be customized to display a patient’s progress over a period of time with related complications and treatment methods that need to be affected. A patient’s diagnostic laboratory procedures and results such as EEGs, EKGs, X-rays, pathology-associated test results, etc. can be associated with this temporal feature 80,94 . Interval-based models and<sup>w</sup> <sup>x</sup> time-point based models constitute two of the widely used MDM temporal marker models 47 . If two<sup>w</sup> <sup>x</sup> temporal markers are identified in a clinical problem, then two models are required for decision support. These models are not necessarily indicative of a clinician’s reasoning methods, where spoken and written languages produce different temporal variations 47 .<sup>w</sup> <sup>x</sup>

The relationships that transpire between medical group members and the reasoning methodology followed can become complex and difficult to manage without appropriate decision-making tools and relationship management tools. MEDICALWAREe attempts to fill this void. MEDICALWAREe use can improve the quality of decisions made by a medical group. Integration of techniques can possibly exhibit the capability of Collective Intelligence 44 . Al- <sup>w</sup> <sup>x</sup> though the experimental results are mixed in supporting the Collective Intelligence factor in a non-MDM context, there is sufficient proof to point to the fact that the final outcome is dependent on the task nature, the social, and communications structures that transpire, besides a number of other factors 44 .<sup>w</sup> <sup>x</sup>

## 3.2. Clinical algorithms and procedures sub-component

This MEDICALWAREe sub-component allows for the incorporation of domain-specific clinical decision-making algorithms in the form of semantic hypermedia templates. Semantic hypermedia templates can be viewed as hypermedia templates with the added value of attributes, which provide knowledge and utility for collaborative MDM. Some of these attributes, were listed in the previous section. These hypermedia-supported templates of clinical algorithms Figs. 3 and 4 , can be customized forŽ . domain-specific needs of medical sub-specialties. This decision-aid can be used in associating relevant clinical-case related information with a specific clinical algorithm being deliberated upon by group members. These templates represent a discourse-structure in a specific problem-domain. Group members can choose to add other nodes or links that a template may lack once an understanding or consensus has been reached, thereby bypassing equivocality problems 75 .<sup>w</sup> <sup>x</sup>

To represent a clinical case using hypermedia nodes Fig. 4 and to monitor on-going patient-re-Ž . lated progress, this hypermedia functionality of MEDICALWAREe can be used. Semantic links can be generated between hypermedia templates stored in several of these nodes to assist in decision-making Ž . refer to Sec. 4 for more details .

Representative node content for depicting relevant clinical case details is shown in Fig. 4 2,94 . These<sup>w</sup> <sup>x</sup> nodes have several attributes such as specialty type and associated links. Depending on the clinical case complexity, specific work-related functionality and attributes could be assigned to group member nodes. Content-specific sub-nodes can also be incorporated in these nodes. For example, the past medical history node can have a general description about the past history with appropriate hypertext links to previous examinations, hospitalization records, prior illnesses, allergies, drug reactions, medication history and so on. The advantage of using such a classification scheme is the ability to relate objects of relationships using semantic links in a clinical case. Although a relational database system can be used for such purposes, semantic relationships cannot be represented explicitly.

Hypermedia-driven, template-based procedures can virtually be of assistance at all levels of MDM. For example, in the treatment of patients with heart failure Fig. 5 14 , a series of procedures is necessi-Ž . <sup>w</sup> <sup>x</sup> tated which involves measurement and analysis of ventricular volumes indicating left ventricular function such as ejection fraction. Evaluation of parameters such as ejection fraction leads to consideration of possibilities such as diastolic dysfunction, which in turn necessitates follow-up with a series of procedures. These procedures often require expert interpretation of several physiological tests such as coronary angiograms 14 . Clinical aspects mentioned in<sup>w</sup> <sup>x</sup> Fig. 5, addressed by group members who pertain to different specialties can be supported synchronously or asynchronously by such hypermedia-driven, template-based procedures.

Typed hypermedia links discussed in Sec. 4Ž . between treatment algorithms stored in hypermedia nodes and patient diagnostic parameters Fig. 4 canŽ .

suggest the next course of action for group members. Commonly requested diagnostic laboratory information Fig. 4 can be associated with specific linkŽ . types with appropriate parts of a treatment algorithm Ž . Fig. 5 2,94 . Two categories of semantic hyperme-<sup>w</sup> <sup>x</sup> dia templates are identified for this purpose. The first category of templates represents general clinical workflow aspects as shown in Fig. 5. The second category of templates is related to clinical algorithm specifics. In this case, these templates deal with representation of knowledge related to the etiologic and clinical classification of the cardiomyopathies, clinical factors to be considered as evaluation criterion, diagnostic laboratory results and studies related to EKGs, chest X-rays, catheterization and so on. The two categories of templates working with each other suggest decision points, the best course of action, and eventually the diagnosis criterion with the support of tools from the other MEDICAL-WAREe sub-components. The diagnosis criterion can suggest relevant diagnoses, which can be finally validated against referential validation templates. If necessary, diagnosis criterion can be reconsidered against critical workflow aspects, in the event of a major discordance in findings. Such an approach blends with the inferential-reasoning ability provided by the hypertext links, using hypertext morphology <sup>w</sup> <sup>x</sup> 73 Appendix B .Ž . MEDICALWARE’s hypermediasupported templates of clinical algorithms and procedures are envisioned to grow over a period of time as support is extended for a wide range of medical specialties.

## 3.3. Expert inference support sub-component

AI techniques support features that exhibit intelligence associated with human behavior, such as understanding, language, learning, reasoning and problem solving 13 . Due to the cognitive orientation of<sup>w</sup> <sup>x</sup> the GDSS architecture and the support that AI principles lend to cognitive features, integration of AI mechanisms strengthens this cognitive orientation. Although several AI techniques can be used in MDM problems, current research indicated that expert system technology is the most widely used for MDM <sup>w</sup> <sup>x</sup> 13,59,86,87 . AI methods can also assist medical reasoning, which involves interplay of temporal and contextual variables 80 . The integration of intelli-<sup>w</sup> <sup>x</sup> gent decision-making procedures with the GDSS architecture is necessitated due to the following reasons:

v need for cross-referencing standards between medical disciplines in the generation of diagnoses;

v intelligent medical information appropriation to hypertext nodes and intelligent link typing using hypertext morphology for collaborative MDM;

v intelligent selection of formal problem-solving and decision-making techniques;

v intelligent medical information navigation incorporating AI<sup>r</sup>expert system and hypertext methods;

v inference mechanisms for validation of clinical results using domain-specific knowledge bases; and

v intelligent selection of decision models based on decision model attributes.

The above features are necessitated due to the presence of a host of applicable decision-making techniques and models for a specific diagnostic problem modeling. The use of any morphology for appropriation for information to hypertext nodes, involves a certain degree of tediousness. This tediousness can be minimized for appropriate problem-domains by identification of suitable inference mechanisms that can be mature over time. The sophistication of the reasoning method built in an expert system is responsible for generating an outcome based on the input clinical data. Current research on AI-based reasoning methods, revealed that the PIP expert system 66,95 uses one of the most sophisticated rea-<sup>w</sup> <sup>x</sup> soning methods. This was built as an experimental system to demonstrate that an expert system can reason based on principles of human cognition. Diagnosis of renal disease is the main domain of PIP’s expert programs 66,95 . Also, PIP’s reasoning strat- <sup>w</sup> <sup>x</sup> egy has been tested successfully with modifications, to represent reasoning strategies in other areas such as systems diagnosis, identification, and diagnosis of systems-related problems 92 . Several expert system<sup>w</sup> <sup>x</sup> inference mechanisms and storage schema use modifications of $\mathrm { P I P } ^ { \prime } \mathrm { s }$ reasoning strategy, based on categorical and probabilistic reasoning methods and Minsky’s 60 knowledge-frame structures based on<sup>w</sup> <sup>x</sup> disease categories. These knowledge-frames are populated by properties of disease categories, semantic relationships, logical relationships, inference mechanisms and rules.

An inference-mechanism such as the one used by PIP can be integrated in this MEDICALWARE TM sub-component using an expert system shell. PIP operates using a combination of hypothesis-directed questioning mechanism with an extensive human reasoning strategy. Based on the large sets of input patient complications, PIP generates a separate set of hypotheses 66 . The hypotheses are correlated<sup>w</sup> <sup>x</sup> against a set of findings to validate the hypotheses. Results reported by a user are matched against the set of findings. In the event of a match, a hypothesis’s rank is revised. $\mathrm { P I P } ^ { \prime } \mathrm { s }$ program has a sophisticated method of representing hypotheses based on cognitive characteristics. The ‘active’ hypotheses represent those that a physician was consciously thinking, the ‘inactive’ hypotheses refer to those in the background. The ‘semi-active’ hypotheses are the ones that were in the back of the physician’s mind 95 .<sup>w</sup> <sup>x</sup>

Although it is tedious to implement the entire above-mentioned expert reasoning features, it can be worthwhile to implement certain features, based on the MDM problem-domain.

## 3.4. Other hypermedia supported MDM support tools

Hypermedia-supported templates can be created prior to a group’s collaborative process begins through a preliminary analysis of a clinical case. However, group members should have the ability to create or modify hypermedia nodes and links that a template’s discourse structure may lack. Such ability is provided by this component.

It is meaningful for a physician to develop mechanisms to relate temporal markers such as patient visit dates with patient data relating critical variables such as medication attributes Ždose, frequency, route, time-span., physical examination history, review of systems information, and other diagnostic laboratory reports Fig. 4 . Although a physician can relate this Ž . in his<sup>r</sup>her mind for a group of patients or a certain patient, it becomes extremely tedious to abstract information for larger groups of patients. This abstraction is problem-domain specific, such as in the treatment of leukemia and AIDS patients, or a combination of problems related to neural and immune system disorders.

Working closely with such physicians, who have a very good understanding of this information abstraction requirement in their problem-domain and clinical research areas, hypertext mechanisms can be embedded in a GDSS to abstract information for various levels of clinical support. These mechanisms can be embedded for different problem-domains in the generator component and linked to the database and temporal marker features. This also establishes a good database structure for information gathering, failing which essential information that a physician requires for information abstraction will not be avail able at the time of crucial decision-making. The generator thus, links input and outcome requirements based on an understanding of the problem areas.

The method listed above necessitates manual inference, after abstraction, using a clinician’s judgment, experience and knowledge of information about different patients and clinical problems. This meaningful inference of the record of events representing various patient profiles extracted from medical and clinical records, can be accorded the support of expert system techniques. This is accomplished using the recommender feature. The medical and clinical record abstraction can be represented with hypermedia templates, using ICD-9 codes for diagnosis classification, medication attributes, non-standard treatment procedures adopted which indicate unusual complications, patient response towards a treatment profile, the group members involved with their involvement represented using node and link attribute weightage and so on.

The approach presented in this section is an attempt to minimize drawbacks related to the applicability of several MDM techniques in a collaborative mode for building models of medical knowledge. The hypermedia-supported GDSS and MEDICAL-WAREe integration can lower a problem’s complexity level using features of the three-factor dimension model explained earlier. Further research is required on the medical dimension complexity through an analysis of several levels of medical tasks for improving our knowledge on medical task complexity ambiguities. The next section discusses the relevance of and the necessity for providing a semantic links typing methodology.

## 4. Developing semantic links for a medical reasoning task

For collaborative MDM, a GDSS architecture should provide the ability for group members to modify templates. This is to accommodate expected or unexpected variations in decision-making criterion during decision-making phases. For this purpose, the GDSS architecture provides for modifiable hypermedia templates composed of semantic nodes and links Ž . Sec. 3.2 . The nature of modifications to algorithms or procedures based on patient profiles in a semantic hypermedia template can be arrived at using consensus mechanisms 100 . A universal hypertext classifi-<sup>w</sup> <sup>x</sup> cation schema used for appropriating information in hypertext nodes and for typing semantic links, based on hypertext morphology Appendix B 73,98 can Ž . <sup>w</sup> <sup>x</sup> assist in this regard. Using this approach for collaborative MDM requires application of a validated, diagnostic classification model representable using hypermedia nodes and links. As described earlier, the ST-model meets this requirement 64 .<sup>w</sup> <sup>x</sup>

Using hypertext morphology, information is appropriated, stored and hypertext links typed, based on the nature of node and link usage. Such an approach while providing for intelligent appropriation and retrieval of information, does not hinder the use of hypermedia templates for decision-making. In the event of ambiguities in information appropriation to nodes or link classification, clarification can be solicited from a group member. For example, handling inferential-type conÕergent links can be addressed by displaying a list of synonyms for Inference listed below Appendix B 73,98 .Ž . <sup>w</sup> <sup>x</sup>

1. Deduction 2. Induction 3. Influence 4. Support 5. Cause 6. Conclusion 7. Implication 8. Endorse 9. Pro 10. Evidence

This can be related to the nature of information assigned to a hypermedia node. Exhausting all available resources for prudent decision-making requires referential support from a clinical information classification model such as the ST-model Fig. 1 . A setŽ . of hypotheses can be tested in a systematic manner with support of tools provided by cognitive-aid structures and components of the GDSS architecture. Links and nodes of the ST-model mapped to a hypermedia-driven model Figs. 1 and 4 , presents Ž . clinical information in a coherent manner usable by a medical group. This also conforms to the appropriation of information to nodes based on a close understanding of the way a physician assembles information during reasoning 64,90 . This approach also<sup>w</sup> <sup>x</sup> provides a formal architecture for the evaluation of clinical evidence in a systematic manner.

A clinical task can be translated to conform to the specifications listed above, with appropriate assignment of nodes and typed links indicating the role and group member tasks. Details of this translation using convergent and divergent links are part of a working paper 77 . The GDSS architecture, which incorpo-<sup>w</sup> <sup>x</sup> rates features presented in earlier sections, is discussed below.

## 5. The GDSS architecture

The GDSS architecture can be described in four sections Fig. 6 as follows: Ž .

1. GDSS architecture input

2. GDSS architecture structures

3. Cognitive appropriation mechanisms

4. GDSS-supported group outcome classification

Given the various support levels this GDSS architecture is designed to interact with, a realistic classification for the GDSS architecture would be that of a diagnostic reasoning process-based architecture. Sec. 5.1 dealt with details on the general nature of the GDSS architecture. The architecture blends itself with the diagnostic reasoning process described earlier in Sec. 1. The GDSS input provides valuable data, the appropriate technology, besides other group-related input. Using this input, a group has the ability to use the Cognitive-Aid or GDSS technology support structures components. Features such as MEDICALWAREe Ž . Fig. 6 provide insight into a clinical problem and trigger linear or non-linear production processes. These processes are appropriated using the cognitive appropriation and Other Appropriation processes components. A group facilitated by these appropriation processes, generates outcome pertinent to input data Fig. 6 . Dissatisfaction withŽ . group outcome can lead to the re-appropriation of production processes for re-evaluation. This cycle continues until a satisfactory group outcome has been reached.

## 5.1. GDSS architecture input

The input categories Fig. 6 , 1 Technology, 2Ž . Ž . Ž . Task, 3 Context and 4 Group are discussed be-Ž . Ž . low.

## 5.1.1. Technology

Technology plays a vital role in collaborative MDM. Technology refers to the presence or absence of a hypermedia-supported GDSS. Several aspects of technology are addressed through the other components of the architecture such as cognitive-aid structures, which are essentially features, or functions of technology.

## 5.1.2. Task

Task is the driving force for GDSS design <sup>w</sup> <sup>x</sup> 18,36,56,57 . The GDSS foundation framework used McGrath’s task classification scheme 18 . McGrath’s<sup>w</sup> <sup>x</sup> task scheme categorizes various group tasks according to their nature, as one of generate, choose or negotiate <sup>w</sup> <sup>x</sup> 57 . An identification of medical task categories Fig. 6 led to the medical task inventory Ž . of six different types of medical tasks developed through a series of field experiments by Golden 31 .<sup>w</sup> <sup>x</sup> These tasks cannot be strictly classified per Mc-Grath’s task model due to the transient nature of medical tasks and sub-tasks and can be applied only to chunks of medical problems. The asynchronous problem dimension necessitates use of models such as the three-factor dimension model for task classification 44 . Thus, a mapping of medical tasks per<sup>w</sup> <sup>x</sup> McGrath’s task-types may be inaccurate and nonrepresentative of the complexities in medical tasks. Medical tasks are comprised of several micro-level tasks, which have to be formulated and completed in a methodical and precise manner in varying time spans. Apart from task-type classifications, activitybased or technique-based classifications have also been used Table 3 , due to the presence of softwareŽ . tools in a GDSS 62 . The presence of software-driven<sup>w x</sup> components such as MEDICALWAREe, enables the GDSS architecture to be classified as actiÕity-driÕen or technique-driÕen or process-driÕen. This also assists in the development of cognitive-aid structures, which are cognitively tailorable, based on features of different schools of MDM 59 and clini-<sup>w</sup> <sup>x</sup> cal cases. The task variables are listed in Fig. 6.

## 5.1.3. Context

Contextual variables Fig. 6 relate to featuresŽ . such as comfort in using GDSS technology and computer-assisted decision-making. Contextual features that can influence MDM also include any pre-existing social<sup>r</sup>professional networks or power <sup>r</sup>status relationships as in managed health care. Medical tasks in managed health care can conform to specified rules and regulations. Thus, a clinician belonging to social <sup>r</sup> professional networks, although trained to perform medical tasks in a certain manner may have to conform to rules and regulations such as the number of tests ordered on a patient, the length of stay of a patient and so on. Social<sup>r</sup>professional networks can influence medical outcomes.

## 5.1.4. Group

Medical group members are composed of members with diverse education and responsibilities. These groups interact as a team of nurses, clinicians, residents, fellows, interns, social workers, laboratory personnel, research<sup>r</sup>clinical study coordinators, health-care administrators, etc. In the clinician category, there exists another specialist clinician category due to specialized training and expertise. Due to the spectrum of diseases present in medicine, it is not possible for a clinician to be an expert in several sub-specialties. Thus, expert clinicians of different sub-specialties are inter-dependent. Group member characteristics used in the GDSS architecture are listed in Fig. 5. Medical group member interaction is not necessarily linear 84 . Non-linear group pro- <sup>w</sup> <sup>x</sup> cesses related to clinical reasoning can be traced in group member interaction 64 . Group characteristics<sup>w</sup> <sup>x</sup> chosen Fig. 6 reflect the diverse nature and struc-Ž . ture of group members, representing a broad spectrum of expertise, education, experience, training, problem-solving skill and cognitive style 33 . Sec.<sup>w</sup> <sup>x</sup> 5.2 discusses the GDSS architecture structures.

## 5.2. GDSS architecture structures

Two classes of structures form part of the GDSS architecture. These are:

1. cognitive-aid structures and

2. GDSS technology and group-process support structures.

## 5.2.1. CognitiÕe-aid structures

Cognitive-aid structures Fig. 6 facilitate compre-Ž . hension of cognitive features Sec. 2.1 related to aŽ . diagnostic reasoning problem. This is accomplished by the use of components of cognitive-aid structures and the cognitiÕe appropriation process mechanism described below. All the support features of cognitive-aid structures listed in Table 3 are supported by this architecture. Using elements of this structure, it is possible to generate and reuse semantic hypertext templates for certain etiologies, navigate for medical information retrieval, create nodes and links for collaboration, access expert-inference mechanisms for domain-specific problems and use MEDICAL-WAREe tools for diagnostic reasoning. This approach is necessitated due to a need for intelligent templates and decision models of medical knowledge for hypothesis generation in a collaborative mode <sup>w</sup> <sup>x</sup> 75,78 . The attributes of decision models discussed in Sec. 3.1 play a prominent role in the use of these models. Expert inference support can compliment a physician’s skill in differential diagnosis, due to a plethora of categories of diseases 1 . The hyperme-<sup>w</sup> <sup>x</sup> dia environment for representing clinical cases Fig.Ž 4 , provides support for a group’s natural thought . processes related to medical reasoning. Features of cognitive-aid structures also support confirmation of the pathogenesis and etiology of an established diagnosis 1 by providing access to a relevant body of <sup>w</sup> <sup>x</sup> medical information and theory. The differential diagnosis process necessitating a medical group to rely on a system of disease classification such as ICD-9- CM codes 45 is also supported by cognitive-aid<sup>w</sup> <sup>x</sup> structures Figs. 3 and 4 .Ž .

## 5.2.2. GDSS technology and group-process support structures

This component accommodates GDSS structures designed to reduce information overload 40 and<sup>w</sup> <sup>x</sup> provide for rules and resources for effective group collaboration. Rules and norms that form part of the social ritual in this case, practice of MDM Ap- Ž . Ž pendix A 30,78 can be incorporated for patient- . <sup>w</sup> <sup>x</sup> specific and environment-specific needs. Although rules and norms form the building block for any social interaction, modifications can be necessitated in a GDSS architecture for MDM due to factors such as ethical and legal issues involved in patient care and respect for a patient’s rights based on social and cultural considerations. Appropriation processes this component can address, are related to rules and norms, structural features designed to reduce information-overload, nature of medical group composition, influence of contextual and external factors, etc. Features related to contingency theory and AST <sup>w</sup> <sup>x</sup> 41,43 , are applicable to this component. In short, contingency theory and AST state that the reaction of group members to different contexts can generate appropriation mechanisms leading to varied appropriation of group-support structures and thereby outcome 19,43 .<sup>w</sup> <sup>x</sup>

To facilitate comprehension of the relationship between cognitive-aid structures and cognitive processes, the cognitiÕe appropriation mechanism, based on the Structuration Theory Appendix AŽ . <sup>w</sup> <sup>x</sup> 69,70,72,78 is described in Sec. 5.3.

## 5.3. CognitiÕe appropriation mechanisms

The concept of cognitiÕe appropriation to establish a theoretical foundation to relate cognitive-aid structures and cognitive processes is presented.

Cognitive Appropriation deals with the appropriation of linear and non-linear cognitive processes and group member interaction complexities encountered in medical decision-making using the elements of Cognitive-Aid structures by an individual or a group. Cognitive-Aid structures thus facilitate appropriation and comprehension of linear and non-linear cognitive processes during collaborative medical decision-making by interaction with the factors related to human cognition and can influence a group member’s cognitive ability in performing a medical task. The use of rules and resources for the production and reproduction of static and dynamic cognitive<sup>r</sup>decision models and other Cognitive-Aid structures oriented by-products, enrich the Cognitive-Aid structures component because they can be subsequently reused by group members.

In handling clinical cases such as those whose pathophysiology origin may be unclear 17 , several<sup>w</sup> <sup>x</sup> cognitive processes related to hypothesis generation, refinement, and associated investigation of relevant clinical evidence are at play. These cognitive processes can be supported by appropriate use of the cognitive-aid structures component. Facilitating such cognitive processes also depend on a variety of factors related to group interaction complexities in a clinical case, the cognitive style, experience, and familiarity with cognitive-aid structures of group members and hidden decision-making profiles. CognitiÕe appropriation patterns can assist in handling information related to physiological systems, current health status, physical examination, etc. 94 by assisting the creation of emergent cognitive models at various phases of the MDM process.

Structuration theory based mechanisms such as AST, facilitate group efforts in moving a task to different factors of the complexity dimension, which represent lower complexity levels 44 . Similarly, <sup>w</sup> <sup>x</sup> cognitive appropriation aims at assisting a group in traversing through a dynamic decision profile using cognitive-aid structures and other supporting GDSS structures, thereby lowering a problem’s complexity level.

GDSS research has proved that interpersonal and cognitive processing complexities should be addressed simultaneously to improve the accuracy of group outcome such as collective judgment Fig. 6Ž . <sup>w</sup> <sup>x</sup> <sup>w x</sup> 16,28,35 . Hackman and Morris’ 35 research has shown that procedure-oriented interventions can improve cognitive processing abilities, but are difficult to integrate with current group processes. Also, improving interpersonal interventions alone have an inverse relationship with cognitive processing abilities 35 . In this context, <sup>w</sup> <sup>x</sup> cognitiÕe appropriation mechanisms 78 can facilitate integration, process- <sup>w</sup> <sup>x</sup> ing, and comprehension of linear and non-linear cognitive processes with respect to cognitive processing abilities.

It should be noted that there is no clear demarcation between the clinical problem-solving and human judgment, clinical reasoning<sup>r</sup>experience components Ž . Fig. 7 . To narrow the gap between these components, the support of MEDICALWAREe combined with cognitiÕe appropriation can be used. Different elements of cognitive-aid structures can have varying levels of influence during cognitiÕe appropriation. Based on the ST-model of diagnostic reasoning Fig.Ž 1 , and hypertext morphology Appendix B 73,98 ,. Ž . <sup>w</sup> <sup>x</sup> it is possible to produce convergent or divergent appropriation for a clinical reasoning task. Cognitive models generated by a medical group help in overcoming the impact of micro-cognitive processes in a clinical problem. Hypertext methods support subsequent retrieval of all forms of information used in the generation of such cognitive models.

Features associated with cognitiÕe appropriation are shown in Fig. 6. To demonstrate the nature of these processes, two examples are discussed briefly in the following section.

## 5.3.1. Number of alternatiÕes considered

Immediate access to and establishing an association between information related to different physiological systems coupled with a systematic method for the generation, evaluation, and validation of differential diagnosis could potentially increase the number of alternative diagnoses being considered at any given time. Use of traditional non-automated methods for handling medical information can limit the differential diagnostic hypotheses space. Access to hypermedia-based information storage and retrieval methods with semantic links based on human cognition can help in the identification of different perspectives, thus, leading to the generation of a number of diagnostic alternatives. In addition, the GDSS architecture supports the use of Delphi-mediated process, which can encourage group participation and help generate varied perspectives of individual group members. From these perspectives, a Delphimediator can assist in ascertaining the assumptions and uncertainties of group members in each Delphiround 100 using GDSS structures to administer the<sup>w</sup> <sup>x</sup> Delphi rounds. Consensus generation methods such as Delphi and nominal group technique NGT , func-Ž . tion with the basic assumption that all conventional and verbal communication have been eliminated <sup>w</sup> <sup>x</sup> 22,53,100 . Delphi-based techniques are currently used for MDM 76 and can be administered using a<sup>w</sup> <sup>x</sup> GDSS for MDM.

![](/api/attachments/FNYTZNHU/fulltext/images/17877c7abe3012f09665f0e62e69409b43699fea80fb13bd0ae39a735a82117e.jpg)  
Medicalware supported tools + Cognitive Appropriation mechanism support  
Fig. 7. The nature of clinical problem-solving and the human reasoning components.

## 5.3.2. Influence of collectiÕe judgment

For any group to successfully handle cognitive complexities, the group members must collectively respond to a given task in the same manner as the groups’ expert member would handle the task <sup>w</sup> <sup>x</sup> 28,37,81,82 . Collective judgment can be defined as the ability of a medical group to consistently outperform the judgment of the group’s best member <sup>w</sup> <sup>x</sup> 16,28,44 . Interaction process losses involving cognitive overhead can occur during medical group collaboration. These losses tend to negate a group’s performance. Hence, the methodology adopted by a group for evaluating patient signs, symptoms and proceed with the differential diagnosis process can influence group outcome.

Collective judgment can be influenced by a variety of factors such as the diversity of a medical group, temporal diagnostic information, and the influence of high domain knowledge vs. low domain knowledge clinicians 26 , and so on. During the<sup>w</sup> <sup>x</sup> course of medical collaboration and decision-making, several hidden patient profiles can impose varied implications. CognitiÕe appropriation effected through mediated or non-mediated mechanisms can assist in identifying such hidden profiles. Several mediated and non-mediated techniques can be used to monitor the dynamic process of group interaction to ensure member participation and uniformity in contribution. Such techniques are intended to increase the accuracy of collective judgment 16 . Al-<sup>w</sup> <sup>x</sup> though this discussion is restricted to two facets of cognitiÕe appropriation, other related aspects mentioned in Fig. 6 can be incorporated to support the collaborative MDM process.

## 5.4. GDSS-supported group outcome classification

The GDSS architecture supported group outcome is listed in Fig. 6. Group outcome has been classified into four categories. They are:

1. a general category such as the number of alternative diagnoses considered Fig. 6 ;Ž .

2. collective intelligence;

3. collective judgment; and

4. interpersonal information exchange features.

The variables that are associated with the above categories are listed in Fig. 6.

## 6. Conclusion

The efforts involved in the development of the GDSS architecture incorporated systematic research and investigation covering a broad spectrum of areas related to medical reasoning, MDM schools of thought, tools and techniques, clinical algorithms and data representation features, hypermedia techniques, medical group characteristics, and so on. This was necessitated due to lack of prior GDSS research in the MDM area and the varied impact of these areas on the design of a GDSS for MDM. The GDSS architecture presented in this paper can be used by designers and researchers in the GDSS<sup>r</sup>medical informatics arena. This GDSS is designed to support collaborative MDM for various medical support levels. Clinical algorithms such as the one discussed in the paper, related to the treatment of patients with heart failure, can be automated and tested. For this purpose, patient diagnostic data associated with heart failure related clinical cases could be stored using the hypermedia nodes described in this paper. Implementing several aspects of the GDSS architecture can promote effective utilization of resources and diagnostic information for collaborative MDM and administration of diagnostic procedures. This architecture was compared, based on five major categories Table 3 with major GDSS research frame-Ž . works and architectures. Through an analysis of Table 3, it can be seen that the GDSS architecture reflects current MDM research and covers several issues not addressed by other researchers in the GDSS-MDM area. Several features of cognitive-aid structures are unique to this GDSS architecture. Cognitive appropriation, relating appropriation patterns of cognitive processes with cognitive-aid structures, can provide an improved understanding of the role of cognitive processes for medical collaboration and health-care delivery. This architecture can assist in exchanging and sharing resources and information related to clinical problems and also utilize the expertise of medical experts worldwide using formal collaborative mechanisms.

## Acknowledgements

The authors wish to express their gratitude to several distinguished researchers, physicians, and academicians who have provided valuable feedback and encouragement towards this research. These include Professors Suresh Rao, Evert Carson, Swamy Laxminarayan, Roxanne Hiltz, Michael Bieber, David Kristol, Julian Sher M.D., Suresh Raina M.D. and Vijay Kalaria. Thanks are also due to various authors who provided valuable feedback regarding the nature of their research.

## Appendix A. Influence of structuration theory on cognitive appropriation

The structuration theory was first proposed by Giddens 29 in 1976. The concept of structuration<sup>w</sup> <sup>x</sup> was referred to as the

process of production and reproduction of social systems via the application of generative rules and resources 29 .<sup>w</sup> <sup>x</sup>

In structuration theory, the term structure subsumes a dual character, being referred to as the medium and the outcome of social action. Structure is referred to as a medium in the interaction of group members, because they use the medium to infer rules and use resources and produce social practices 69 .<sup>w</sup> <sup>x</sup> The process of structuration is initiated when group members use rules and resources to produce practices. These rules or resources are influenced by other rules or resources within the boundary of the social system being studied 29 .<sup>w</sup> <sup>x</sup>

Arguing on the lines of Gidden’s social practice, collaborative MDM can be classified as a social practice and structures should be provided for any social practice until the practice is formally completed over a period of time 29,69 . Structures can be viewed as properties of interaction systems 69 . <sup>w</sup> <sup>x</sup> The concept of structuration unfolds as group members use rules and resources for action. In this process, multiple rules and resources can be used to fulfill an action. The interaction of rules and resources define and produce both static and dynamic scenarios 29,69 . The essence of an action relies on<sup>w</sup> <sup>x</sup> its relationship with the domain of actions related to the on-going social practice. On-going social practices such as MDM associated with the practice of medicine continue to exist, because of its use in a social system.

When group members are in the process of participating in a social practice such as medicine, it is not the objective of structuration theory to present these structures as cognitive maps to individual group members. Rather, these structures are present in a virtual medium and as interaction unfolds, the dual nature or character of the structures is subsumed <sup>w</sup> <sup>x</sup> 29 . The first aspect of this dual nature uses cognitive-aid structures as the medium, since they allocate rules and resources medical group members must use for sensible medical collaboration and decision-making. The second aspect of the dual character considers cognitive-aid structures as the outcome of the practice of MDM, since rules and resources present in cognitive-aid structures exist through application and acknowledgment via group member interaction. As cognitive-aid structures are used, interaction of rules and resources produce static and dynamic cognitive<sup>r</sup>decision models, templates and other cognitive-aid structures oriented end-products. The production and reproduction of these cognitive<sup>r</sup>decision models and other end-products that emerge via use of rules and resources can be considered as part of the cognitive-aid structures component for subsequent use by medical group members.

Stability and change are not assumed as a basic state by structuration theory 29 . These have to be<sup>w</sup> <sup>x</sup> explained in terms of precise mechanisms or processes, which create and reproduce them. Several aspects of stability and change related to MDM are known to occur. Structuration theory requires that these aspects related to stability and change in MDM be explained by a suitable mechanism or a process. In doing so, due to the cognitive orientation of MDM, the current research focuses on the development of a process based on cognitive characteristics to explain aspects related to stability and change. In this context, cognitiÕe appropriation can explain aspects related to stability and change from an MDM perspective.

## Appendix B. Introduction to hypertext morphology

Recent research at NJIT on the development of a hypertext morphology focused on several features of cognition as represented by Guilford’s theory of the intellect 33,34 . Hypertext morphology classified <sup>w</sup> <sup>x</sup> hypertext nodes as follows Table 4 98 .Ž . <sup>w</sup> <sup>x</sup>

Hypertext morphology aims at the creation of a universal set of hypertext nodes Table 1 in aŽ . hypertext system. This also aims at the development of a common implementation model 73,98 . The <sup>w</sup> <sup>x</sup> most important reason for the development of this hypertext morphology is the Aestablishment of a classification system for all nodes and linksB <sup>w</sup> <sup>x</sup> 98 . The reasons for such a classification system are 98 :<sup>w</sup> <sup>x</sup>

1. common implementation model;

2. powerful semantic and network analysis possibilities; and

3. collaboration for creation of knowledge-bases.

Hypertext morphology research at NJIT has revealed that several existing semantic models can be mapped in the defined node types 73,98 . These<sup>w</sup> <sup>x</sup> nodes are intended to store varied categories of information Table 1 . Thus, information is stored inŽ . a hypertext system according to the specific category it belongs to 98 . Hypertext morphology also leads<sup>w</sup> <sup>x</sup> to the creation of specific types of hypertext links, which can be used to categorize the nature of information flow between hypertext nodes. These links are listed in Table 1. In addition to the definition of types of links, hypertext morphology also deals with attributes with respect to hypertext links. These include 98 :<sup>w</sup> <sup>x</sup>

1. the strength of a link;

2. the creator of a link or node;

3. the leÕel of agreement on a link or node; and

4. the popularity of a link or node 98 .<sup>w</sup> <sup>x</sup>

Hypertext morphology also promotes collectiÕe intelligence <sup>w</sup> <sup>x</sup> 44,98 . This is made possible by the hypertext-based communication structures, human roles, and creation of collaborative expert systems. Collaborative expert system characteristics include the following 98 :<sup>w</sup> <sup>x</sup>

1. extensive cognitive hypertext linkages;

2. voting and scaling models;

3. adaptive content, integrated in group processes; and

4. group memory 98 . <sup>w</sup> <sup>x</sup>

Hypertext morphology also promotes and provides collectiÕe intelligence features 44 such as:

1. the capturing of individual knowledge;

2. formation of a group synthesis;

3. provide feedback to a group;

4. provide for evaluation by the group;

5. provide methods for the evolution and adoption by a group;

6. use by the group for the group and this GDSS shall not perish; and

7. integration of computer resources power to the group.

Table 4  
Hypertext morphology: hypertext node types, links, and relationship with cognition variables Rao and Turoff 73 , Turoff et al. 98 Ž <sup>w x</sup> <sup>w x</sup>.

<table><tr><td>Cognition</td><td>Description of node</td><td>Convergent production</td><td>Divergent production</td></tr><tr><td>Node type</td><td></td><td>Links</td><td>Links</td></tr><tr><td>Detail</td><td>Fact, definition, reference</td><td>Specification</td><td>Elaboration</td></tr><tr><td>Collection</td><td>Group, heading, aggregation, set</td><td>Membership</td><td>Opposition</td></tr><tr><td>Proposition</td><td>Assumption, belief, axiom, law</td><td>Association</td><td>Speculation</td></tr><tr><td>Summary</td><td>Generalization, overview, template</td><td>Path</td><td>Branch</td></tr><tr><td>Issue</td><td>Question, problem, concern, vision</td><td>Alternative</td><td>Lateral</td></tr><tr><td>Observation</td><td>Conclusion, decision, action, policy</td><td>Inference</td><td>Extrapolation</td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 D.A. Albert, R. Munson, M.D. Resnik, Reasoning in Medicine: An Introduction to Clinical Inference, Johns Hopkins Univ. Press, 1988, ISBN: 0-8018-3426-0 alk. Ž paper ..

<sup>w</sup> <sup>x</sup> 2 B. Bates, A Guide to Physical Examination and History Taking, 6th edn., J.B. Lippincott, 227 East Washington Square, Philadelphia, PA 19106-3780, 1995, ISBN: 0-397- 55053-7 alk. paper . Ž .

<sup>w</sup> <sup>x</sup> 3 J.R. Beck, S.G. Pauker, The Markov process in medical prognosis, Medical Decision Making 3 1983 419–458. Ž .

<sup>w</sup> <sup>x</sup> 4 W.K. Blazer, M.E. Doherty, R. O’Connor Jr., The effects of cognitive feedback on performance, Psychological Bulletin 106 1989 410–433.Ž .

<sup>w</sup> <sup>x</sup> 5 M.S. Blois, Medicine and the nature of vertical reasoning, New England Journal of Medicine 318 13 1988 847–851,Ž . Ž . March 31.

<sup>w</sup> <sup>x</sup> 6 U. Bockenholt, E.U. Weber, Use of formal methods in medical decision making: a survey and analysis, Medical Decision Making 12 1992 298–306.Ž .

<sup>w</sup> <sup>x</sup> 7 R.P. Bostrom, R.T. Watson, S.T. Kinney Eds. , ComputerŽ . Augmented Teamwork: A Guided Tour Van Nostrand-Reinhold, New York, 1992, VNR Computer Laboratory, ISBN 0-442-00277-7.

<sup>w</sup> <sup>x</sup> 8 N.E. Breslow, Biostatistics and Bayes with discussion ,Ž . Statistical Science 5 3 1990 269–298.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 E.R. Carson, in: E.E. Carson, D.G. Cramp Eds. , Comput- Ž . ers and Control in Clinical Medicine, Plenum, New York, 1985.

<sup>w</sup> <sup>x</sup> 10 M. Chen, Y.I. Liou, The design of an integrated group support environment, Proceedings of the Twenty-Forth Hawaii International Conference on Systems Science, 1991, pp. 333–342.

<sup>w</sup> <sup>x</sup> 11 L. Chidambaram, R.P. Bostrom, B.E. Wynne, A longitudinal study of the impact of group decision support systems on group development, Journal of Management Information Systems 7 3 1991 7–25.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 C. Christensen, J.R. Larson Jr., Collaborative medical decision making, Medical Decision Making 13 1993 339–346. Ž .

<sup>w</sup> <sup>x</sup> 13 W.J. Clancey, E.H. Shortliffe, Readings in Medical Artificial Intelligence: The First Decade, Addision-Wesley Publishing, 1984, ISBN 0-201-10854-2.

<sup>w</sup> <sup>x</sup> 14 Clinical Practice Guideline. Number 11, Heart Failure: Evaluation and Care of Patients With Left-Ventricular Systolic Dysfunction. US Department of Health and Human Services Publication.

<sup>w</sup> <sup>x</sup> 15 D. Coleman, R. Khanna Eds. , Groupware TechnologiesŽ . and Applications, Prentice-Hall, Englewood Cliffs, NJ, 1995.

<sup>w</sup> <sup>x</sup> 16 Patricia Reagan-Cirincione, Combining group facilitation, decision modelling, and information technology to improve the accuracy of group judgment, Proceedings of the 25th Hawaii International Conference on System Sciences, IEEE Computer Society Press, Los Alamitos, CA, 1992, pp. 232–243.

<sup>w</sup> <sup>x</sup> 17 P. Cutler, Problem Solving in Clinical Medicine: From Data to Diagnosis, 1st edn., The Williams and Wilkins, Baltimore, MD, 1980, ISBN 0-683-0225-2.

<sup>w</sup> <sup>x</sup> 18 G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 Ž . Ž . 5 1987 589–609, May.

<sup>w</sup> <sup>x</sup> 19 G. DeSanctis, M.S. Poole, Capturing the complexity in advanced technology use: adaptive structuration theory, Organization Science 5 2 1994 121–147, May.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 A.P. Dempster, M.R. Selwyn, B.J. Weeks, Combining historical and randomized controls for assessing trends in proportions, Journal of the American Statistical Association 78 1983 221–227.Ž .

<sup>w</sup> <sup>x</sup>21 A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker Jr., D.R. Vogel, Information technology to support electronic meetings, MIS Quarterly 12 4 1988 591–624.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 A.R. Dennis, J.S. Valacich, J.F. Nunamaker Jr., Group, sub-group and nominal group idea generation in an electronic meeting environment, in: J.F. Nunamaker Ed. , Pro-Ž . ceedings of the 24th Hawaii International Conference on System Sciences, vol. 3, IEEE Computer Society Press, Los Alamitos, CA, 1991.

<sup>w</sup> <sup>x</sup> 23 T. Efraim, Decision support and expert systems: management support systems, Chapter 9: Group Decision Support Systems, 3rd edn., MacMillan, New York, 1993, pp. 351– 390.

<sup>w</sup> <sup>x</sup> 24 A.S. Elstein, L.S. Shulman, S.A. Sprafka, Medical Problem Solving: An Analysis of Clinical Reasoning, Harvard Univ. Press, Cambridge, MA, 1978.

<sup>w</sup> <sup>x</sup> 25 A.S. Elstein, Cognitive processes in clinical inference and decision making, in: D.C. Turk, P. Salovey Eds. , Reason- Ž . ing, Inference and Judgment in Clinical Psychology, Free Press<sup>r</sup>Macmillan, New York, 1988.

<sup>w</sup> <sup>x</sup> 26 A.S. Elstein, B. Kleinmuntz, M. Rabinowitz, R. McAuley, J. Murakami, P.S. Heckerling, J.M. Dod, Diagnostic reasoning of high- and low-domain-knowledge clinicians: a reanalysis, Medical Decision Making 13 1993 21–29.Ž .

<sup>w</sup> <sup>x</sup> 27 J. Fjermestad, S.R. Hiltz, An assessment of group support systems experimental research: methodology and results, Journal of Management Information Systems 15 3Ž . Ž . 1998<sup>r</sup>99 7–149, Winter.

<sup>w</sup> <sup>x</sup> 28 B.R. Gallupe, Suppressing the contribution of the group’s best member: is GDSS use appropriate for all group tasks? Proceedings of the 23rd Hawaii International Conference on System Sciences, vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1990, pp. 13–22.

<sup>w</sup> <sup>x</sup> 29 A. Giddens, New Rules of Sociological Method, Basic Books, New York, 1976.

<sup>w</sup> <sup>x</sup> 30 A. Giddens, The Constitution of Society, Univ. California Press, Berkeley, CA, 1984.

<sup>w</sup> <sup>x</sup>31 A.S. Golden, An Inventory For Primary Health Care Practice, Ballinger Publishing, Cambridge, MA, 1976, ISBN 0-88410-134-7.

<sup>w</sup> <sup>x</sup> 32 G.A. Gorry, Modelling the diagnostic process, Journal of Medical Education 45 1970 293–302, May. Ž .

<sup>w</sup> <sup>x</sup> 33 J.P. Guilford, The structure of intellect, Psychological Bulletin 53 4 1956 July.Ž . Ž .

34 J.P. Guilford, The Nature of Human Intelligence, McGraw-Hill, New York, 1967.

<sup>w</sup> <sup>x</sup> 35 J.R. Hackman, C.G. Morris, Group tasks, group interaction processes and group performance effectiveness: a review and proposed integration, in: L. Berkowitz Ed. , AdvancesŽ . in Experimental and Social Psychology, vol. 8, Academic Press, New York, 1975, pp. 45–99.

<sup>w</sup> <sup>x</sup> 36 J.R. Hackman, K.R. Brousseau, J.A. Weiss, The interaction of task design and group performance strategies in determining group effectiveness, Organizational Behavior and Human Performance 16 1976 350–365.Ž .

<sup>w</sup> <sup>x</sup> 37 J. Harmon, J. Rohrbaugh, Social judgment analysis and small group decision-making: cognitive feedback effects on individual and collective performance, Organizational Behavior and Human Decision Processes 46 1990 34–54.Ž .

<sup>w</sup> <sup>x</sup> 38 M. Hatcher, Uniqueness of group decision support systems Ž . GDSS in medical and health applications, Journal of Medical Systems 14 6 1990 351–364, Plenum Publish- Ž . Ž . ing.

<sup>w</sup> <sup>x</sup> 39 F.S. Hillier, G.J. Lieberman, Introduction to Operations Research, 4th edn., Holden-Day, Oakland, CA, 1986, ISBN: 0-8162-3871-5.

<sup>w</sup> <sup>x</sup> 40 S.R. Hiltz, M. Turoff, Structuring computer-mediated communication systems to avoid information overload, Communications of the ACM 28 7 1985 682–689, July.Ž . Ž .

<sup>w</sup> <sup>x</sup> 41 S.R. Hiltz, Productivity enhancement from computer-mediated communication: a systems contingency approach, Communications of the ACM 31 12 1988 1438–1454, De-Ž . Ž . cember.

<sup>w</sup> <sup>x</sup> 42 S.R. Hiltz, K. Johnson, Measuring acceptance of computermediated communication systems, Journal of the American Society for Information Science 40 6 1989 386–397.Ž . Ž .

<sup>w</sup> <sup>x</sup> 43 S.R. Hiltz, D. Dufner, M. Holmes, S. Poole, Distributed group support systems: social dynamics and design dilemmas, Journal of Organizational Computing 2 1 1991Ž . Ž . 135–159.

<sup>w</sup> <sup>x</sup> 44 S.R. Hiltz, M. Turoff, The Network Nation: Human Communication via Computer, The MIT Press, Cambridge, MA, 1993, Revised edition, with foreword by Suzanne Keller, ISBN 0-262-08219-5.

<sup>w</sup> <sup>x</sup> 45 ICD-9-CM Handbook, International Classification of Diseases, 9th Revision, Clinical Modification Handbook, 1995.

<sup>w</sup> <sup>x</sup> 46 M.T. Jelassi, R.A. Beauclair, An integrated framework for group decision support systems design, Information and Management 13 1987 143–153.Ž .

<sup>w</sup> <sup>x</sup> 47 M.G. Kahn, Modeling time in medical decision-support programs, Medical Decision Making 11 1991 249–264.Ž .

<sup>w</sup> <sup>x</sup> 48 D. Kahneman, A. Tversky, On the psychology of prediction, Psychological Review 80 1973 237–251.Ž .

<sup>w</sup> <sup>x</sup>49 R.W. Klein, R.S. Dittus, S.D. Roberts, J.R. Wilson, Simulation modelling and health-care decision making, Medical Decision Making 13 4 1993 347–354, Oct–Dec.Ž . Ž .

<sup>w</sup> <sup>x</sup> 50 J.C. Kunz, E.H. Shortliffe, B.G. Buchanan, E.A. Feigenbaum, Computer-assisted decision making in medicine, Journal of Medicine and Philosophy 9 1984 135–160.Ž .

<sup>w</sup> <sup>x</sup> 51 M.S. Leaning, E.R. Carson, Renal modelling, in: D.G.

Cramp, E.R. Carson Eds. , The Circulatory System: Mea- Ž . surement in Medicine Series, vol. 1, Croom Helm, London, 1986, pp. 271–312, Chap. 7, ISBN: 0-7099-3452-1.

<sup>w</sup> <sup>x</sup> 52 D.V. Lindley, The 1988 wald memorial lectures: the present position in bayesian statistics, Statistical Science 5 1Ž . Ž .1990 44–89.

<sup>w</sup> <sup>x</sup> 53 H. Linstone, M. Turoff, The Delphi Method: Techniques and Applications, Addison-Wesley, Reading, MA, 1975, pp. 503–507, ISBN: 0-201-04293-2.

<sup>w</sup> <sup>x</sup> 54 L.B. Lusted, Introduction to Medical Decision Making, Charles C. Thomas Publisher, Springfield, IL, 1968, Lib.of.Cong.Cata 68-13767.

<sup>w</sup> <sup>x</sup> 55 L.B. Lusted, Some roots of clinical decision making, in: B.I. Blum, K. Duncan Eds. , A History of Medical Infor-Ž . matics, Addison-Wesley Publishing, ACM Press, 1990, ISBN 0-201-50128-7.

<sup>w</sup> <sup>x</sup>56 B.E. Mennecke, B.C. Wheeler, Tasks matter: modeling group task processes in experimental CSCW research, IEEE 1993 1993 71–80.Ž .

<sup>w</sup> <sup>x</sup> 57 J.E. McGrath, Groups: Interaction and Performance, Prentice-Hall, Englewood Cliffs, NJ, 1984.

<sup>w</sup> <sup>x</sup> 58 M.N. Meeker, Structure of the intellect: its interpretation and uses, in: N.C. Kephart Ed. , Charles E. Merrill Publish-Ž . ing, A Bell and Howell Company, 1969, Library of Congress Catalog Number: 69-17296.

<sup>w</sup> <sup>x</sup> 59 R.A. Miller, Medical diagnostic decision support systemspast, present and future: a threaded bibliography and brief commentary, Journal of the American Medical Informatics Association 1 1994 8–27.Ž .

<sup>w</sup> <sup>x</sup> 60 M. Minsky, in: Winston Ed. , A Framework for Represent- Ž . ing Knowledge,1975.

<sup>w</sup> <sup>x</sup> 61 G.R. Norman, Problem-solving skills, solving problems and problem-based learning, Medical Education 22 1988 279–Ž . 286.

<sup>w</sup> <sup>x</sup> 62 J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 7 1991Ž . Ž . 40–61, July.

63 J.F. Nunamaker Jr., R. Briggs, D. Mittleman, D.R. Vogel, P. Balthazard, Lessons from a dozen years of group support systems research: a discussion of lab and field findings, Journal of Management Information Systems 13 3 1996–Ž . Ž 1997 163–207, Winter..

<sup>w</sup> <sup>x</sup> 64 V.L. Patel, D.A. Evans, G.J. Groen, Biomedical knowledge and clinical reasoning, in: D.A. Evans, V.L. Patel Eds. ,Ž . Cognitive Science in Medicine: Biomedical Modeling, MIT Press, Cambridge, MA, 1989, pp. 53–112.

<sup>w</sup> <sup>x</sup> 65 V.L. Patel, G.J. Groen, Cognitive frameworks for clinical reasoning: application for training and practice, in: D.A. Evans, V.L. Patel Eds. , Proceedings of the NATO Ad-Ž . vanced Research Workshop on Advanced Models of Cognition for Medical Training and Practice, ll Ciocco, Barga, Italy, June 19–22, Springer-Verlag, 1991, pp. 193–211, Published in cooperation with NATO Scientific Affairs Division, ISBN 3-540-55884-5.

<sup>w</sup> <sup>x</sup> 66 S.G. Pauker, G.A. Gorry, J.P. Kassirer, W.B. Schwartz,

Towards the simulation of clinical cognition. Taking a present illness by computer, American Journal of Medicine 60 1976 981–996.Ž .

<sup>w</sup> <sup>x</sup> 67 A. Pinsonneault, K.L. Kraemer, The impact of technological support on groups: an assessment of the empirical research, Decision Support Systems 5 1989 197–216.Ž .

<sup>w</sup> <sup>x</sup> 68 A. Pinsonneault, K.L. Kraemer, The effects of electronic meetings of group processes and outcomes: an assessment of the empirical research, European Journal of Operational Research 46 1990 143–161.Ž .

<sup>w</sup> <sup>x</sup> 69 M.S. Poole, D.R. Seibold, R.D. McPhee, Group decision Making as a structurational process, Quarterly Journal of Speech 71 1985 74–102.Ž .

<sup>w</sup> <sup>x</sup> 70 M.S. Poole, G. DeSanctis, Use of group decision support systems as an appropriation process, Proceedings of the Twenty Second Annual Hawaii Conference on System Sciences vol. IV1989, pp. 149–157.

<sup>w</sup> <sup>x</sup> 71 M.S. Poole, G. DeSanctis, Understanding the use of group decision support systems: the theory of adaptive structuration, in: J. Fulk, C. Steinfield Eds. , Organizations andŽ . Communication Technology, Sage Publications, Beverly Hills, CA, 1990, pp. 173–193.

<sup>w</sup> <sup>x</sup> 72 M.S. Poole, Group communication and the structuring process, in: R.S. Cathcart, L.A. Samovar Eds. , Group Deci- Ž . sion Making: Structure and Performance, from Small Group Communication: A Reader, William C. Brown Publishers, 1992, pp. 147–157, Chapt. 3, ISBN 0-697-08644-5.

<sup>w</sup> <sup>x</sup> 73 U. Rao, M. Turoff, Hypertext functionality: a theoretical framework, International Journal of Human Computer Interaction 4 1 1990 333–358.Ž . Ž .

<sup>w</sup> <sup>x</sup> 74 G.R. Rao, B.A. Suresh, S. Laxminarayan, T.N. Denny, Towards a framework for a decision support system for integrated information retrieval in biomedical computing, Proceedings of the IEEE-EMBS 15th Annual Conference, 1993, pp. 586–587, October.

<sup>w</sup> <sup>x</sup> 75 G.R. Rao, B.A. Suresh, M. Turoff, S.R. Hiltz, Issues in the development of a computer mediated communication system framework for collaborative medical decision making, Proceedings of the IEEE-EMBS 16th Annual Conference, vol. 16, 1994, pp. 1354–1355.

<sup>w</sup> <sup>x</sup> 76 G.R. Rao, Towards a group decision support system framework for medical decision making, A Medical Decisionmaking and GDSS State-of-the-Art Review, May,1996.

<sup>w</sup> <sup>x</sup> 77 G.R. Rao, B.A. Suresh, M. Turoff, Working Paper a1: The development of Semantic Links for Representing a Medical Problem using Hypertext Morphology, November 1997.

<sup>w</sup> <sup>x</sup> 78 G.R. Rao, B.A. Suresh, M. Turoff, A group decision support system framework for medical decision making incorporating cognitive-aid structures and cognitive appropriation, Proceedings of the 30th Annual Hawaii International Conference on System Sciences, IEEE Computer Society Press, 1997.

<sup>w</sup> <sup>x</sup> 79 G.R. Rao, B.A. Suresh, M. Turoff, Working Paper a2: Analysis of the Schools of MDM, January 1997.

<sup>w</sup> <sup>x</sup> 80 G.D. Rennels, A computational model of reasoning from

the literature, Computer Methods and Programs in Biomedicine 24 1987 139–149.Ž .

<sup>w</sup> <sup>x</sup> 81 J. Rohrbaugh, Improving the quality of group judgment: social judgment analysis and the delphi technique, Organizational Behavior and Human Performance 24 1979 73–Ž . 92.

<sup>w</sup> <sup>x</sup> 82 J. Rohrbaugh, Improving the quality of group judgment: social judgment analysis and the nominal group technique, Organizational Behavior and Human Performance 28 1981Ž . 272–288.

<sup>w</sup> <sup>x</sup> 83 M.F. Rubinstein, Patterns of Problem-Solving, Prentice-Hall, Englewood Cliffs, NJ, 1975, ISBN 0-13-654251-4.

<sup>w</sup> <sup>x</sup> 84 E.E. Sampson, M. Marthas, Group Process for the Health Professions, 3rd edn., Delmar Publishers, Albany, NY, 1990, ISBN 0-8273-4352-3.

<sup>w</sup> <sup>x</sup> 85 K. Sengupta, Te’eni Dov, Cognitive feedback in GDSS: improving control and convergence, MIS Quarterly 1993Ž . 87–113, March.

<sup>w</sup> <sup>x</sup> 86 E.H. Shortliffe, B.G. Buchanan, E.A. Feigenbaum, Knowledge engineering for medical decision-making: a review of computer-based clinical decision aids, Proceedings of the IEEE 67 1979 1207–1224.Ž .

<sup>w</sup> <sup>x</sup>87 E.H. Shortliffe, Medical informatics and clinical decision making: the science and the pragmatics, Medical Decision Making 11 1991 S2–S14 suppl. . Ž . Ž .

<sup>w</sup> <sup>x</sup> 88 F.A. Sonnenberg, J.R. Beck, Markov models in medical decision making: a practical guide, Medical Decision Making 13 1993 322–338.Ž .

<sup>w</sup> <sup>x</sup> 89 H.C. Sox Jr., M.A. Blatt, M.C. Higgins, K.I. Marton, Medical Decision Making, Butterworths, 1988, ISBN 0- 409-90091-5.

<sup>w</sup> <sup>x</sup> 90 M. Stefanelli, M. Ramoni, Epistemological constraints on medical knowledge-based systems, in: D.A. Evans, V.L. Patel Eds. , Proceedings of the NATO Advanced ResearchŽ . Workshop on Advanced Models of Cognition for Medical Training and Practice, ll Ciocco, Barga, Italy, June 19–22, Springer-Verlag, 1991, pp. 3–20, Published in cooperation with NATO Scientific Affairs Division, ISBN 3-540-55884- 5.

<sup>w</sup> <sup>x</sup> 91 R. Summers, E.R. Carson, S. Andreassen, Causal probabilistic modelling for clinical decision support in the highdependency environment, Proceedings of the 14th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, vol. 3, 1992, pp. 869–870, October 29–November 1.

<sup>w</sup> <sup>x</sup> 92 B.A. Suresh, M.R. Tanniru, A knowledge based approach for problem diagnosis in information systems, Proceedings of the 1990 Annual Meeting: Decision Sciences Institute, vol. 1, 1990, pp. 279–281, November.

<sup>w</sup> <sup>x</sup>93 D.B. Swanson, Issues in assessment of practical skills in medicine, Professional Education Research Quarterly 12 Ž . 1990 3–6.

<sup>w</sup> <sup>x</sup> 94 M.H. Swartz, Textbook of Physical Diagnosis: History and Examination, W.B. Saunders, 1989, ISBN: 0-7216-2475-8.

<sup>w</sup> <sup>x</sup> 95 P. Szolovits, S.G. Pauker, Categorical and probabilistic

reasoning in medical diagnosis, Artificial Intelligence 11 Ž .1978 115–144.

<sup>w</sup> <sup>x</sup> 96 M. Turoff, S.R. Hiltz, Computer support for group versus individual decisions, IEEE Transactions On Communications Com-30 1 1982 January.Ž . Ž .

<sup>w</sup> <sup>x</sup> 97 M. Turoff, Computer-mediated communication requirements for group-support, Journal of Organizational Computing 1 1991 85–113.Ž .

<sup>w</sup> <sup>x</sup> 98 M. Turoff, U. Rao, S.R. Hiltz, Collaborative hypertext in computer mediated communications, Proceedings of the Twenty-Fourth Annual Hawaii International Conference on System Sciences, vol. 4, 1991, pp. 357–366.

<sup>w</sup> <sup>x</sup> 99 M. Turoff, S.R. Hiltz, V. Balasubramanian, The human element in collaborative hypertext<sup>r</sup>hypermedia, Position paper in CSCW Computer Supported Cooperative Work Ž . Conference, 1994.

<sup>w</sup> <sup>x</sup> 100 M. Turoff, S.R. Hiltz, A computer-based Delphi process, in: M. Adler, E. Ziglio Eds. , Gazing into the Oracle: TheŽ . Delphi Method and its Application to Social Policy and Public Health, Jessica Kingsley Publishers, 116 Pentonville Road, London N19JB, 1995, ISBN 1 85302 1040, October.

<sup>w</sup> <sup>x</sup> 101 A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 1974 1124–1131,Ž . September.

<sup>w</sup> <sup>x</sup> 102 J.H. Tyrer, M.J. Eadie, The Astute Physician: How to Think in Clinical Medicine, Elsevier, 1976, ISBN: 0-444-41425-8.

<sup>w</sup> <sup>x</sup> 103 D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge Univ. Press, Cambridge, 1986.

<sup>w</sup> <sup>x</sup> 104 S.R. Watson, D.M. Buede, Decision Synthesis: The Principles and Practice of Decision Analysis, Cambridge Univ. Press, Cambridge, 1987.

<sup>w</sup> <sup>x</sup> 105 L.E. Widman, K.A. Loparo, N.R. Nielsen Eds. , ArtificialŽ . Intelligence, Simulation and Modeling, Wiley, 1989, ISBN 0-471-60599-9.

<sup>w</sup> <sup>x</sup> 106 W. Zachary, A cognitively based functional taxonomy of decision support techniques, Human–Computer Interaction 2 1986 25–63.Ž .

Dr. Gururajan Rao obtained his PhD in MIS from Rutgers University, Graduate School of Management, Newark, NJ in May 2000. The research presented in this paper is part of his doctoral thesis work related to medical informatics. He has over 14 years of health-care related industrial and academic experience in DSS design and implementation, medical decision-making, health-care information systems and knowledge-based systems analysis and design. In 1996, he founded Quantum Enterprises, a consulting company specializing in the design and development of document management applications, health-care information systems, Intranet- and Internet-based applications. He is currently on a consulting assignment with the Clinical Research Information Systems group at Merck Research Laboratories, Rahway, NJ.

Dr. Murray Turoff is a distinguished professor of Computer and Information Science at the New Jersey Institute of Technology. He is a recipient of the Electronic Frontiers Foundation Pioneer 1994 award for his development of the first Group Communications system in 1971. He is the co-author of the award-winning book, The Network Nation MIT Press . He has been working on Ž . the development and design of systems to facilitate human communications since the late 1960s and has been currently working in the areas of asynchronous learning networks and group decision support systems Homepage: http: Ž . <sup>rr</sup>eies.njit.edu<sup>r ;</sup> turoff<sup>r</sup> .
