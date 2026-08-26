---
otero_id: 28608
otero_key: "8B6RPM9S"
title: "The ITEM Ontology: A Tool to Elucidate the Anatomy of Psychometric Indicators"
authors: "Kai R. Larsen; Roland M. Mueller; Dario Bonaretti; Diana Fischer-Preßler; James (Jim) Burleson; Nimisha Singh; Jeffrey Parsons; Jean-Charles Pillet; Lan Sang; Zhu (Drew) Zhang"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0257"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The ITEM Ontology: A Tool to Elucidate the Anatomy of Psychometric Indicators

Kai R. Larsen,<sup>a,</sup>\* Roland M. Mueller,<sup>b,c</sup> Dario Bonaretti,<sup>d</sup> Diana Fischer-Preßler,<sup>e,f</sup> James (Jim) Burleson,<sup>g</sup> Nimisha Singh,<sup>h</sup> Jeffrey Parsons,<sup>i</sup> Jean-Charles Pillet,<sup>j</sup> Lan Sang,<sup>k</sup> Zhu (Drew) Zhang<sup>l</sup>

<sup>a</sup> University of Colorado Boulder, Boulder, Colorado 80309; <sup>b</sup> Berlin School of Economics and Law, 10825 Berlin, Germany; <sup>c</sup> University of Twente, 7500 AE Enschede, Netherlands; <sup>d</sup> NEOMA Business School, 76130 Mont-Saint-Aignan, France; <sup>e</sup> Frankfurt University of Applied Sciences, 38106 Frankfurt, Germany; <sup>f</sup> Fraunhofer IAO, 74076 Heilbronn, Germany; <sup>g</sup> California Polytechnic State University, San Luis Obispo, California 93407; <sup>h</sup> School of Management, Bennett University, Greater Noida, Uttar Pradesh 201310, India; <sup>i</sup> Memorial University of Newfoundland, St. John’s, Newfoundland and Labrador A1C 5S7, Canada; <sup>j</sup> TBS Business School, 31000 Toulouse, France; <sup>k</sup> University of Colorado Boulder, Boulder, Colorado 80309; <sup>l</sup> University of Rhode Island, Kingston, Rhode Island 0288 \*Corresponding author

Contact: kai.larsen@colorado.edu, https://orcid.org/0000-0002-8812-9866 (KRL); roland.mueller@hwr-berlin.de, https://orcid.org/0000-0002-8706-7763 (RMM); dario.bonaretti@neoma-bs.fr, https://orcid.org/0000-0002-0859-3096 (DB); diana.fischer-pressler@fb3.fra-uas.de, https://orcid.org/0000-0002-5968-1299 (DF-P); jburleso@calpoly.edu, https://orcid.org/0000-0002-9579-8742 (J(J)B); nimisha.singh@bennett.edu.in, https://orcid.org/0000-0002-4868-1533 (NS); jeffreyp@mun.ca, https://orcid.org/0000-0002-4819-2801 (JP); jean-charles.pillet@tbs-education.fr, https://orcid.org/0000-0002-7247-2408 (J-CP); lan.sang@colorado.edu (LS); zhuzhang@uri.edu (Z(D)Z

Received: April 27, 2023 Revised: March 4, 2024; December 19, 2024; May 21, 2025 Accepted: May 24, 2025 Published Online in Articles in Advance: August 13, 2025

https://doi.org/10.1287/isre.2023.0257

Copyright: © 2025 INFORMS

Abstract. Survey-based research in information systems requires valid scales to advance the ory, and the discipline has developed rigorous procedures to assess scale validity. In principle, these procedures ensure that scales consist of clear indicators and faithfully represent the focal construct. However, the focus on the psychometric properties of scales has overshadowed the role of lexical and semantic elements in the validation process, leading to invalid scales. This overemphasis on psychometric properties will persist unless researchers have a systematic approach to analyzing the properties of indicators and share the outcome of such analyses in formats that can be peer-reviewed, critiqued, or corroborated by other researchers. Thus, the psychometric community needs a shared language and method to uncover the properties of indicators and identify validity problems that psychometric analysis fails to detect. Drawing on ontology development methods, we propose the Indicator Terminology for Explanation and Measurement (ITEM) Ontology, consisting of four high-level hierarchies of entities: objects, measurables, qualifiers, and response sets, each almost always found within an individual indicator. We develop an approach, a codebook, and a website for applying ITEM to psychometric indicators. Common approaches to ontology evaluation are then used to evaluate its expressiveness, utility, importance, accessibility, suitability, and external validity. We find that the ITEM Ontology is highly generative in that it can be used to address several previously unsolvable problems in survey science, polling, and theory testing.

History: Youngjin Yoo, Senior Editor; Heng Xu, Associate Editor. g

Funding: The authors thank the U.S. National Institutes of Health (NIH) for support under Grant 3U24AG052175-08S1, the Social Sciences and Humanities Research Council of Canada (SSHRC) for support under Grant 435-2020-0402, Joerg Evermann for assistance during the early stages of the project, and dozens of research assistants at the University of Colorado. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0257.

Keywords: scale development • ontology • content validity • indicator development • double-barreled

## 1. Introduction

For the past five decades, information systems (IS) scholars have used survey-based research to test theories of technology-related phenomena. These efforts have produced contributions within and beyond the field. For example, IS scholars have contributed to virtually all disciplines concerned with concepts such as technology acceptance (Rahimi et al. 2018, Granic´ and Marangunic ´ 2019). Nevertheless, even the most fundamental methodological aspects of scale development are continuously questioned, including how to phrase indicators appropriately, how to develop a set of indicators, how to adapt indicators from existing scales (Compeau et al. 2022), the correctness of modeling indicators as formative or reflective (Petter et al. 2007), and the ontological nature of indicators (Weber 2021). Although survey-based research is typically supported by robust statistical validation, the validity of psychometric scales has been questioned from a theoretical standpoint (Rossiter 2011, Webe 2021). However, such theoretical arguments have had a minimal effect on instrument validation procedures because of the lack of an alternative approach for articulating the theoretical, linguistic, and ontological issues affecting psychometric scales and their indicators. This research develops such an approach for survey researchers, where rather than considering indicators as an irreducible element, we decompose them to gain a more thorough understanding of their meaning.

To improve the transparency of indicator creation and revision, we reconceptualize the nature of indicators by developing an ontology of indicator components. We conceive indicators as units of meaning with distinguishable linguistic and ontological features rather than as unitary measurement artifacts, the properties of which are revealed through statistical procedures. An ontology-informed reconceptualization of indicators provides a common language for researchers to discuss the quality and conceptual appropriateness of indicators and construct definitions. In particular, we demonstrate the usefulness of the proposed ontology by evaluating that it is capable of operationally representing indicator concerns and that it enables a new kind of content validation. We evaluate the ontology’s reliability, representativeness, criterion model validity, and external validity. We conclude by discussing the contributions and implications of the ITEM Ontology.

## 2. Background and Motivation

It is distressingly easy to inadvertently write vague, confusing, or loaded indicators because there is little available evidence on how the brain processes indicators (Tourangeau et al. 2000). Such flawed indicators make respondents more likely to supply unreliable and invalid answers (Krosnick 1991), decrease the motivation to respond accurately (Khanna and Sood 2018), and increase the likelihood of common method bias (for a review, see MacKenzie and Podsakoff 2012). Hence, a large, scattered, and often inaccessible body of literature is concerned with indicator wording issues and their consequences, generally providing guidelines on improving indicator and definition quality (see, e.g., Krosnick 1991, Tourangeau et al. 2000, MacKenzie and Podsakoff 2012, and Saris and Gallhofer 2014). This literature discusses how wording issues, such as the use of vague, ambiguous, or difficult terms, unclear temporal coordinates, use of negation, or the use of hypothetical situations, can affect survey responses.

Whereas there are many introductory textbooks on survey design (see, e.g., Converse and Presser 1986, Edwards et al. 1997, and Saris and Gallhofer 2014), guidelines for writing or improving indicators are frequently perfunctory (see, e.g., Willis and Lessler 1999 and Chung et al. 2019), consisting mainly of “idiosyncratically selected rules for achieving good writing” (Osterlind 1998, p. 5).

In scale development, indicators are considered valid only if empirically evaluated. Empirical validity is achieved when indicators are deemed to be adequate “parameters” of a measurement model, meaning that the measurement model shows appropriate psychometric properties (MacKenzie et al. 2011). Unfortunately, current methods for statistical analysis cannot reliably detect semantic, lexical, and logical problems with indicators. Semantic similarity within a scale and dissimilarity to other scales may be contributing to good psychometric properties (see, e.g., Gefen and Larsen 2017, Gefen et al. 2020, and Arnulf et al. 2021), and such properties can be achieved even by meaningless indicators, including those measuring nonsensical constructs such as gavagai and lorem ipsum (Maul 2017). Such low sensitivity to semantic, lexical, and logical variation (the rules that, in combination, determine what parts exist within an indicator) raises questions about whether current psychometric validation procedures are sufficient to deem scales and indicators valid.

Researchers have recommended against starting scale evaluation by analyzing covariance patterns of responses to survey indicators. Before administration, an indicator should demonstrate content validity. For instance, Moore and Benbasat (1991) specified a structured approach to indicator development used by many high-impact psychometric papers published in the IS discipline (see, e.g., Taylor and Todd 1995, Wang and Strong 1996, Venkatesh et al. 2003, and Oliveira et al. 2016). By common agreement, scale development begins with validating the content of indicators—for example, using expert reviews, forms appraisal, cognitive interviews, and focus groups. These evaluation procedures alone can lead to the rejection or retention of indicators but are not designed to clarify why any indicator would fail an evaluation. This lack of guidance stems from focusing on the indicator as a whole rather than its components (Rothgeb et al. 2007). We posit that changing the level of analysis from the indicator to its components will enable procedures for scale development to be more transparent and auditable.

We are not the first to propose that indicators must be examined at a more granular level. Chin et al. (2008) argued that mapping the content of indicators onto four components (i.e., behavioral action, behavioral action context, causal verb linkage, and consequence) can facilitate updating IS measures. Xu and Zhang (2022) further facilitated the quantitative assessment of context effects and supplied researchers with a diagnostic tool to address these effects. Consistent with the insights of Chin et al. (2008) and Xu and Zhang (2022), we contend that shifting the focus to a within-indicator level of analysis allows for a more comprehensive understanding of indicator semantics and fosters precise communication, including the operationalization of common indicator errors (see, e.g., Guttman 1954, Chin et al.

2008, and Hackett 2021) and content validation (see, e.g., Hinkin and Tracey 1999 and MacKenzie et al. 2011).

However, the approach of Chin et al. (2008) lacks the specificity and definitional framework needed for comparison or extension, and Xu and Zhang (2022), although contributing to the understanding of context effects on privacy concerns, focused primarily on developing an integrative understanding of context effects.

Outside of the IS discipline, the C-OAR-SE method of Rossiter (2002, 2011) is, to date, the most comprehensive framework for analyzing the components of indicators. C-OAR-SE proposes three cardinal entities for designing content- and construct-valid indicators: object, attributes, and rater. Rossiter’s (2011) rater entity refers to the person or persons doing the rating and has the subtypes expert, coder, manager, consumer, and individual. According to Rossiter, raters speak about themselves (as the object) unless otherwise specified. An attribute is a dimension of judgment that reflects psychometric constructs, such as ease of use, usability, or data quality, and belongs to the rated object (concrete perceptual, concrete psychological, abstract achieved, and abstract dispositional). The four subtypes focus primarily on whether the information in the attribute is self-reportable, whether the rater and researcher understand the attribute, or whether the attributes are abstract or concrete. Although we share Rossiter’s goal of understanding indicators by examining their components, we note three limitations of his approach: (1) it considers only a few components, leaving most of the indicator unexplained; (2) it does not capture the relationships across those components; and (3) it is intended to develop single-indicator scales. Overcoming these limitations could improve expert psychometricians’ understanding of indicators and help determine accurate language for indicator wording.

More recently, Weber (2021) argued for rules to guide indicator design. Weber draws on an established ontological perspective, a synthesis and extension of Bunge’s (1977) ontology, sometimes referred to as the Bunge-Wand-Weber ontology (BWW). However, Weber’s work does not consider ontological structures within indicators. Although Rossiter offers a within-indicator view, his framework is incomplete and cannot model relationships between entities. Whereas Weber (2021) offered an internally consistent and complete ontological framework, it missed an opportunity to account for within-indicator ontological analysis. A third view is needed to address the limitations of these approaches by providing an ontological framework and language at the within-indicator level, creating the conceptual framing needed to ensure that psychometrics remains useful to researchers. This article aims to build and validate such a language—an ontology of indicator terminology for explanation and measurement.

## 3. An Ontology for Coding Indicators 3.1. The ITEM Ontology

An ontology is “a formal representation of knowledge by a set of concepts within a domain and the relationships between those concepts” (Man 2013, p. 43). Ontologies define a “common vocabulary for researchers who need to share information in a domain” (Noy and McGuinness 2001, p. 1). Ontology development follows similar rules as other conceptual modeling approaches (see, for example, Arp et al. 2015) and has been long established in IS (e.g., Wand and Weber 1988), including when discussing measurement and psychometrics (Noy and McGuinness 2001), and comes with a welldeveloped evaluation regime (McDaniel and Storey 2020).

Given the importance of language and cognition to indicator construction and interpretation, we base our ontology on the streamlined version of the Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE), called DOLCE Ultralight (Gangemi 2002). Gangemi et al. (2002, p. 167) described the purpose of DOLCE as capturing “ontological categories underlying natural language and human commonsense.” The claim to reflect language structure and human cognition (Gangemi et al. 2002, 2003) suggests a fit with the task of understanding the components of indicators.

Indicative of its appropriateness as a starting point, DOLCE has been accepted as an ISO standard (ISO/ IEC CD 21838-3) top-level ontology along with Basic Formal Ontology (BFO, Arp et al. 2015). We deemed DOLCE Ultralight appropriate as a starting point for ontological development and adapted it, as shown in Figure 1, to account for the domain- and survey-specific syntactic structures.

We term the ontological perspective introduced in this paper the Indicator Terminology for Explanation and Measurement ontology—or ITEM for short. We developed ITEM applying the elements of DOLCE Ultralight on a large set of IS indicators and pruned DOLCE (for example, the distinction between a natural person and a social person was removed). It was then extended according to the elements found in the indicators (for example, the entity respondent). This was an iterative process in which subteams annotated the indicators using a working version of ITEM. These subteams presented their work during the weekly project all-team meeting, where potential changes were discussed and approved through voting. The process took more than two years, until ITEM reached stability.

As the ontology stabilized, we created an ITEM Ontology Codebook with step-by-step rules, and five research assistants (RAs) were hired and trained in its use. Seventy-five indicators randomly selected from Information Systems Research, MIS Quarterly, and Journal of Management Information Systems were independently

Figure 1. (Color online) Map of ITEM Entities: Comparison of DOLCE, Toulmin, and ITEM  
![](/api/attachments/8B6RPM9S/fulltext/images/6d794e91f772432e035f70b94af3e96467d352f4d46c1b328b739d6a689394c3.jpg)

coded by pairs of research assistants and resolved through discussion. On a weekly basis, the RAs submitted comprehensive progress reports, delineating achievements and challenges. These were subsequently assessed by the pertinent subteam of authors, which had the authority to suggest modifications to both the ontological framework and the codebook. The proposed alterations were then presented to the project team for discussion and deliberation. Figure 1 shows ITEM’s final set of entities. Each branch of the hierarchy is a subtype of the highest-level entity in the ontology, simply called Entity. We start with the Object hierarchy, where we adopted and adapted most of ITEM’s entities from DOLCE Ultralight and DOLCE. We added the domain-specific entities Information System and Respondent to this category. Information System was added because it is fundamental to the discipline and frequently occurs in the indicators. Respondent was added to ITEM because indicators are directed toward respondents.

We added the second upper-level category, Measurable, and subcategories to capture all basic entities that tend to be the focus of measurement in indicators: Activity, Attribute, and Value, as well as the Cause/Enable entity, which represents relationship measurement. The third upper-level category of ITEM is Qualifier, integrating DOLCE with elements of Toulmin’s argumentation structure (Toulmin 2003). This enabled representations of underlying qualifications in indicators such as subsetting, generality, conditionality, and context. Finally, we added ontological elements that reflect response formats, captured in the fourth upperlevel category, Response Set and its subtypes. Figure 1 also indicates what parts of DOLCE Ultralight and

Toulmin were adopted/adapted and which parts were newly added to ITEM.

Our ontology, including definitions and indicator examples, is available on the Prote´ge ´ Ontology Portal at https://protege.stanford.edu and is downloadable in OWL format. This article illustrates several examples of ITEM’s use. We treat ITEM akin to other complex research artifacts and evaluate the full version, but we describe only the parts necessary for understanding its use and evaluation in this article.

In describing ITEM, we start with the Object hierarchy, which includes Agents. We show how the entities in an example indicator, “I feel busy due to use of ICTs at home [SD – SA<sup>1</sup>],” would be coded with ITEM. The BRAT rapid annotation tool (Stenetorp et al. 2012), initiated with ITEM codes, provides choices from among available entity and relationship options and was used for the indicator coding.

## 3.2. ITEM Ontology: Objects

The Object entity captures physical and nonphysical (conceptual) objects. The objects and their definitions were provided primarily by DOLCE Ultralight—the exceptions are Information and Information System, for which the team developed new and discipline-specific definitions. We consider Information to be a Nonphysical Object, but not a Social Object because, in principle, some information might exist independent of any social interpretation (Floridi 2013). In contrast, we consider Information System to be a type of Object on its own, because it consists of physical and nonphysical components (Faulkner and Runde 2019). The Agent entity is an agentive subtype of Physical Object. We coded as Respondent any instances of an Individual characterized by the act of assessing a situation. Exhibit 1 denotes ITEM’s use with “ICTs” coded as Information System and “I” coded as Respondent.

$$
\text { Respondent(s) } \quad \text { I } \quad \text { feel   busy   due   to   use   of   ICTs   at   home   [SD - SA] } \tag {1}
$$

## 3.3. ITEM Ontology: Measurables

All the IS indicators we coded focused on measuring an Activity, Attribute, Value of an attribute, or the Cause/ Enable (relationships) entity. We term these entities Measurables. Activity is an active, ongoing, conscious process, action, or operation. The “use” of a technology (denoted in Exhibit 2) is a commonly measured activity in the IS indicators we examined. An Attribute is a state, characteristic, feature, or property of an entity. Although the Activity of “use” may be measured in terms of whether it happened or not, the goal is typically measuring characteristics such as the ease or duration of such an Activity. We extended ITEM beyond

DOLCE with the subtype Mental Attribute, an attribute deemed to exist in an individual’s mind, and coded both mental attributes and mental processes as Mental Attributes.

<table><tr><td colspan="2">Respondent(s)</td><td colspan="2">Mental Attribute</td><td colspan="2">Activity</td><td>IS</td></tr><tr><td>I</td><td>feel</td><td>busy</td><td>due to</td><td>use</td><td>of ICTs</td><td>at home [SD-SA]</td></tr></table>

Cause/Enable signifies structures that ask respondents to appraise whether one entity causes (in the sense of “leading to” and “preceding”) or enables (by allowing) another entity (Exhibit 3). The entities linked through Cause/Enable are most often Attributes or Activities, but in some cases, Information Systems or Social Objects may link to the Cause/Enable entity—for example, “ICTs cause requests.”

![](/api/attachments/8B6RPM9S/fulltext/images/9238e64ba66a5bc524b1fbf77cc773892533f100d2c17fb5014babc4b3b5a1e4.jpg)

(3)

## 3.4. ITEM Ontology: Qualifiers

In Toulmin’s (2003, p. 93) argumentation structure, a qualifier describes the scope or modality of a statement. We adapted this concept in that the entity Qualifier sets a reference against which respondents process the content of an indicator. For example, temporal qualification is often crucial to ensuring accurate and consistent responses. Thus, the indicator, “How often did you use the software?” needs a precise and appropriate temporal scope (e.g., “in the last 2 weeks”).

In ITEM, we distinguish 13 different Qualifiers, classified into three main subtypes: Scope Qualifier, Conjectural Qualifier, and Cognitive Qualifier. The Scop Qualifier specifies the factual boundary of a question, the Conjectural Qualifier describes the modality or logical context, and the Cognitive Qualifier identifies the mental or emotional context. The definitions and use of each are described in Online Appendix A in the ITEM Codebook.

In the example indicator, the Spatial Qualifier specifies the location of one or more entities in the indicator, as denoted in Exhibit 4. The Cognitive Qualifier specifies the mental system (e.g., memory, emotion) used in responding. For example, when we compare the two indicators—“I find the system useful” and “The system is useful”—the former uses the Cognitive Qualifie “find” to evoke a more subjective evaluation than the latter indicator.

![](/api/attachments/8B6RPM9S/fulltext/images/d7882b150066a3ffed16bbce4d3a3dfae3f34193d8a6f1443d61a8ce436d764b.jpg)

(4)

## 3.5. ITEM Ontology: Response Sets

The last major type of entity, the Response Set, forms the structure for the respondent’s reaction to the indicator.

![](/api/attachments/8B6RPM9S/fulltext/images/eabf0c0acab9434718b1535916547438ecdd334a61d36cf1d41f2ea36943e81f.jpg)

There are three kinds of response sets: Nominal, Ordinal, and Continuous. Most relevant is the Ordinal Set, consisting of ordered categories and having subtypes, including the Agreement Set (Exhibit 5). One important contribution of the ontology is to specify by means of a relationship which entity or entities the response set most directly measures, which brings us to ITEM relationships.

(5)

## 3.6. ITEM Ontology: Relationships

The ITEM Ontology outlines the relationships between entities (the color coding in the exhibits is used as a key in the codebook to speed up the learning and interpretation of coded indicators). Entities will generally be connected to other entities through one or more relationships. The ITEM Codebook proceeds from coding entities to coding the relationships between them. Because Attributes must belong to another entity, the Attribute must be connected with the relation “isAttributeOf” to any other entity (typically, the subtype Mental Attribute connects to Agents). Exhibit 6 shows Mental Attribute attached to Respondent because it is the respondent who feels busy.

In Exhibit 7, we connect “feel,” which qualifies how the respondent relates to “busy,” the Attribute that is being qualified. Cognitive qualifiers always belong to a Respondent; thus, we do not code this relationship explicitly. We also coded the Spatial Qualifier “at home” as “isQualifierFor” the Activity “use.” Next, we specify that the Activity “use” involves the Information System “ICTs.”

We next connect the Cause/Enable entity by observing what entities it connects to through the “isCause” and “isEffect” relationships. Here, the Activity “use” causes the Mental Attribute “busy.” Finally, we establish the relationship between the Agreement Set and a Measurable in the indicator. This indicator has three potential target measurables: “busy” (Attribute), “use” (Activity), and “due to” (Cause/Enable). Although both Attribute and Activity have the potential to vary and different respondents may be expected to engage in different levels of “use” as well as to feel different levels of “busy,” this indicator is asking the Respondent (“I”) to state their level of agreement with the statement that “use” causes feeling “busy,” and thus Cause/Enable becomes the target measurable, as per Exhibit 8.

This coding makes it possible to consider other situations. For example, this indicator might have bisected the indicator into one measuring busyness (“I feel busy”) separately from another indicator measuring the perceived level of use (“I use the ICT at home”). In the first case, the Mental Attribute “busy” would be the target measurable, and in the second case, the Activity “use” would be the target measurable, and the relationship between the indicators would be established empirically.

## 4. Two Use Cases for the ITEM Ontology

We developed the ITEM Ontology as a highly generative new “language” that allows psychometric experts to better communicate about indicators. In this section, we present two use cases in which the ITEM Ontology is used to surface previously hard-to-address problems about indicators and scales.

![](/api/attachments/8B6RPM9S/fulltext/images/0964e571edb3cb6e2ba07894087b75a41a33a817ea062d955d6216b290619324.jpg)

## 4.1. Applying ITEM to Areas of Indicator Quality Concern

ITEM allows for operational definitions of indicator concerns and increases the ability to detect such concerns, a claim we evaluate by conducting a large literature review of indicator concerns established in prior literature and showing how this ontological operationalization surfaces a new understanding of each concern and enables semiautomatic and automatic detection. Such a shift is well-aligned with Compeau et al.’s (2022) method for construct updating, which credibly ties theory and definition with indicators but does not address underlying indicator concerns. The review surfaced 16 indicator quality concerns with multiple definitions and empirical evidence of their impact on psychometric measurement. The areas of concern were classified into six categories: (1) temporality (distant temporal context, missing time frame, temporal ambiguity); (2) vagueness (vague objects, activities, or attributes; vague values; and technical or unusual terms); (3) alternative reality (hypotheticals, presuppositions); (4) complexity (syntactical complexity, double negation, reverse indicator); (5) response set effects (restriction of range, double-barreledness, generalizations); and (6) construct grouping (grammatically redundant indicators, indicator clustering).

The results of this review are presented in Online Appendix B and represent a collection of areas of concern for indicator designers. Each of the 16 concerns is defined conceptually and operationally using ITEM, then illustrated with an example indicator published in a top IS journal coded with ITEM. The effects of the problem are specified, along with recommendations for how to improve indicators. For conciseness, we present here one such problematic indicator type—namely, double-barreled indicators. A double-barreled indicator is intrinsically ambiguous because it is unclear “whether respondents should (a) answer only one part of the question or (b) average their responses to both parts of the question” (MacKenzie and Podsakoff 2012, p. 546).

At present, scholars diverge on what constitutes double-barreledness; it has been incongruously defined as an indicator having multiple “ideas” (MacKenzie et al. 2011, p. 304), “objects” (Bradburn et al. 2004, p. 142), “questions” (Willis and Lessler 1999, p. 2), “things” (Klugman and Lamb 2019, p. 296), or “parts” (Babbie 2015, p. 250), all terms that in ITEM would be represented as entities. There are further suggestions that double-barreled indicators must be “implicit” (Willis and Lessler 1999, p. 2) or “tied together” (Bradburn et al. 2004, p. 142), terms for which no clear meaning is specified. By annotating entities and relationships using ITEM, we can operationalize doublebarreledness as a structure within an indicator. More precisely, double-barreled indicators are those where a Response Set or a target measurable (attribute, value, activity, or cause-enable entities) has two or more identical relationships. A target measurable is defined as a Measurable that is directly connected to a Response Set by means of an “isResponseSetOf” relationship. Operationalizing double-barreledness—or any other wording problem—using ITEM provides expert psychometricians with a tool to discuss more transparently whether and how wording issues affect an indicator. In fact, scholars who disagree with our operationalization of double-barreledness can use ITEM to argue for a different one.

Furthermore, we identified two types of doublebarreledness. Direct double-barreledness manifests when the indicator contains two or more target measurables; Indirect double-barreledness manifests when a target mea surable has two or more identical relationships. A direct example is, “I feel alive and vital” (Figure 2a). This indicator is double-barreled because “alive” and “vital” are two distinct Mental Attributes connected to the Response Set with two identical “isResponseSetOf” relationships. By design, a “completely true for me” response means the respondent bears high levels of both mental attributes. However, it is impossible to discern whether a respondent who answers “not true at all for me” disagrees with just one or both attributes.

Figure 2. (Color online) Detection of Indicator Problems: Double-Barreled Examples  
![](/api/attachments/8B6RPM9S/fulltext/images/295a37adfc719a7ab6ddf54ae4c14d1ebe4beebe9a484195da2beba6726743d5.jpg)  
Note. (a) Direct double-barreledness (James et al. 2019, i#19); (b) indirect double-barreledness (Pirkkalainen et al. 2019, simplified, full version in Online Appendix B).

An example of indirect double-barreledness arises from a target measurable. In Figure 2(b), the Mental Attribute “complex” is the target measurable because it is the focus of the isResponseSetOf relationship and itself has two isResponseTo relationships. Although arguments could be made for the logic of this indicator being clear (it takes only one of these to be true for the statement to be true), we include this indicator under our operational definition of double-barreled indicators because it is not clear how respondents will react to and process the logical structure. Additional details on the definition, effects, and recommendations are available in Online Appendix B.

To evaluate the quality of ITEM and the operational definitions of indicator and construct concerns, we created a new artifact called the ITEMIZER to apply those 16 operational definitions to ITEM-coded indicators. The ITEMIZER is a Python prototype that can indicate potential concerns in indicators based on indicator patterns. The inputs are the BRAT annotations of the indicators (for example, Figure 2, a and b). The ITEMIZER was designed to identify, among BRAT-annotated indicators, those that presented a pattern corresponding to any of the operational definitions.

ITEMIZER works at both the indicator and construct levels to identify potential problems in survey item wording. Six potential areas of concern are highlighted, each with further subcategories, resulting in the 16 total concerns mentioned above. The six areas of concern are temporal context, vagueness, alternative reality, complexity, response set effects, and construct grouping. Two of the areas of concern—“technical terms” and “vague objects, activities, or attributes”— are not implemented in ITEMIZER because they need manual analysis. For each area, ITEMIZER notes identified concerns. For a brief overview of the results provided by the ITEMIZER, see Figure 3 below. The generated results require a manual review to ensure overall correctness because the tool may occasionally produce false positives. Online Appendix E provides a step-bystep guide for authors and reviewers on how to assess the quality of indicators as well as recommendations for revising and improving indicators.

The ITEMIZER tool was applied to three instruments published in top journals (Venkatesh et al. 2003, Ayyagari et al. 2011, James et al. 2019). Table 1 outlines how many indicators in each instrument were found to exhibit a concern in each of the six categories.

The six types of indicator and scale concerns were found to be related to the concern types: temporal context, alternative reality, complexity, and response set effects. The system was not set up to automatically detect vagueness concerns, per the scoping, which clarifies that the ITEM Ontology cannot detect understanding that is embedded in survey designers’ or respondents minds. However, vague terms such as “productivity,” “resources,” “problems,” and “accomplishments” were found in the indicators through a manual evalua tion of attributes, activities, and values. Value ambiguity terms included “a lot” and “many more,” and technical or unusual terms included “burned out.” We also did not code construct grouping because indicator clustering could not be detected in paper indicator reporting. Although the approach can detect grammatically redundant indicators, including two indicators from Ayya gari et al. (2011) that differed in minor ways, “The [capabilities/features] provided by ICTs are [reliable/ dependable].”

The evaluation of the system surfaced different concerns for the three papers examined; only three concern types common to all three papers were detected. The most frequent concern was related to the measurement of activities without specifying a time frame.

The ITEMIZER results are based on the annotation of the indicators and therefore need a manual double-check for the semantic part of the definition. Moreover, some flagged concerns may not be relevant within the specific context of a research project. For instance, researchers often implement methodological safeguards—such as using screening or filter questions to ensure that participants meet certain presuppositions or including reverseworded items to control for response biases. Although the ITEMIZER might highlight such elements as potential issues, these concerns may already be intentionally addressed by the research design. Therefore, interpreting the ITEMIZER output always requires contextual judg ment and an understanding of the study’s specific meth odological choices.

We conclude that the ITEM Ontology was able to represent the 11 of 16 areas of concern within the scope and that doing so surfaced a much higher specificity and ability for expert psychometricians to discuss the finer points of such areas of indicator concern. Returning to the topic of double-barreled indicators, we see that every single instrument in our evaluative set displayed this issue at various levels ranging from 5% to 22% of indicators, high numbers for a supposedly wellunderstood concern.

We end by summarizing Online Appendix C, which reports a criterion evaluation of ITEMIZER against four criteria. Criterion evaluation is a central approach for assessing design science artifacts. It provides evidence for our claim that ITEMIZER surpasses alternative artifacts argued to represent a standard (Larsen et al. 2025).

Item Level  
Figure 3. Screenshot of ITEMIZER Interface Showing Possible Issues at Item and Construct Level

<table><tr><td></td><td></td><td>construct</td><td>Restriction of range</td><td>Generalizations</td><td>Temporal ambiguity</td><td>Distant temporal context</td><td>Double barreledness</td></tr><tr><td>1</td><td>to ICTs. strongly disagree (1) - strongly agree (7)</td><td>Work Overload</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>CTs. strongly disagree (1) - strongly agree (7)</td><td>Work Overload</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>uries between my job and my home life. strongly disagree (1) -</td><td>Work Home Conflict</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>ted responsibilities creates conflicts with my home responsib</td><td>Work Home Conflict</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>done at home because I find myself completingjob-related wc</td><td>Work Home Conflict</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>it my use of ICTs can be easily monitored. strongly disagree (1)</td><td>Invasion of Privacy</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>compromised because my activities using ICT scan be traced.</td><td>Invasion of Privacy</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>d violate my privacy by tracking my activities using ICTs. stron</td><td>Invasion of Privacy</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>is makes it easier to invade my privacy. strongly disagree (1) - s</td><td>Invasion of Privacy</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>ave to deal with ICT problems or with my work activities. stro</td><td>Role Ambiguity</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Construct Level

<table><tr><td>construct</td><td>Mixed-measurables</td><td>Reverse indicator</td></tr><tr><td>Anonymity</td><td></td><td></td></tr><tr><td>Complexity</td><td></td><td></td></tr><tr><td>Invasion of Privacy</td><td></td><td></td></tr><tr><td>Job Insecurity</td><td></td><td></td></tr><tr><td>Negative Affectivity</td><td></td><td></td></tr><tr><td>Negative Affectivity</td><td></td><td></td></tr><tr><td>Pace of Change</td><td></td><td></td></tr><tr><td>Presenteeism</td><td></td><td></td></tr><tr><td>Reliability</td><td></td><td></td></tr><tr><td>Role Ambiguity</td><td></td><td></td></tr></table>

This type of evaluation supports claims about what an artifact is—and is not—based on its outputs or characteristics relative to other artifacts. If successful, the evaluation provides criterion validity to the knowledge claim (Larsen et al. 2025). To do so, we examined three papers published in top IS outlets (Venkatesh et al. 2003, Ayyagari et al. 2011, James et al. 2019) using the ITEMIZER, Question Understanding Aid (QUAID;

Table 1. ITEMIZER Results

<table><tr><td>Concerns</td><td>Ayyagari et al. (2011)</td><td>James et al. (2019)</td><td>Venkatesh et al. (2003)</td></tr><tr><td colspan="4">Temporal context</td></tr><tr><td>Distant temporal context</td><td>2/48</td><td>0/20</td><td>4/31</td></tr><tr><td>Missing timeframe</td><td>0/48</td><td>9/20</td><td>1/31</td></tr><tr><td>Temporal ambiguity</td><td>6/48</td><td>12/20</td><td>4/31</td></tr><tr><td colspan="4">Alternative reality</td></tr><tr><td>Hypotheticals</td><td>7/48</td><td>2/20</td><td>11/31</td></tr><tr><td>Presuppositions</td><td>11/48</td><td>15/20</td><td>10/31</td></tr><tr><td colspan="4">Complexity</td></tr><tr><td>Syntactical complexity</td><td>12/48</td><td>15/20</td><td>10/31</td></tr><tr><td>Double negation</td><td>2/48</td><td>3/20</td><td>2/31</td></tr><tr><td>Reverse indicator</td><td>2/48</td><td>1/20</td><td>2/31</td></tr><tr><td colspan="4">Response set effects</td></tr><tr><td>Restriction of range</td><td>8/48</td><td>2/20</td><td>4/31</td></tr><tr><td>Double-barreledness</td><td>5/48</td><td>1/20</td><td>9/31</td></tr><tr><td>Generalizations</td><td>0/48</td><td>0/20</td><td>1/31</td></tr></table>

Graesser et al. 2006), Survey Quality Predictor (SQP V2.1; Felderer et al. 2024), and the Flesch-Kincaid readability test (Flesch 1948). Our premise is that existing indicator quality evaluation tools do not have the ability to detect the same kinds of concerns as ITEMIZER.

In our analysis, ITEMIZER and QUAID show the highest degree of similarity, although ITEMIZER surpasses QUAID in identifying a greater number of issues in indicators, but the tools are at different levels of aggregation, so we expect them to be complementary. ITEMIZER exhibited a substantial positive correlation of 0.297 (p < 0.05) with QUAID, indicating a consistent increase in detection of concerns as QUAID value goes up. As expected, a significant negative correlation of �0.354 (p < 0.05) was observed with SQP\_Reliability, which means that as ITEMIZER detects more concerns, SQP\_Reliability scores tend to decrease. ITEMIZER was not significantly correlated with any other criterion. Outside of SQP\_Validity’s low correlation with factor loadings, none of the detection tools were significantly correlated with the factor loadings, including ITEMIZER, suggesting that construct validity approaches are not sensitive to detecting indicator areas of concern, at least not above the level of indicator quality expected for top journal publication.

A follow-up regression analysis was conducted to further explore the relationship between ITEMIZER and the four criterion approaches. In this model, ITEMIZER is set as the predicted score, and all the criteria are predictors. Consistent with the correlation results, QUAID was found to have a positive impact on ITEMIZER (β � 0.455, p < 0.001), whereas SQP\_Reliability demonstrated a negative effect on ITEMIZER (β � �0.344, p < 0.001). Overall, 37% of the variance in indicator quality when assessed using ITEMIZER is explained by established indicator evaluation tools.

To summarize, ITEMIZER finds concerns in carefully developed studies that correlate with existing criterion indices of survey indicator quality, including QUAID and SQP\_Reliability. This indicates that ITEMIZER outputs an index for predicting survey indicator quality. Online Appendix E guides authors and editors in employing ITEM for survey indicator quality evaluation.

## 4.2. Applying ITEM to Assess Content Validity

Content validity is concerned with whether the indicators used in an instrument are relevant to and representative of the content domain implied by the definition of the targeted construct (Haynes et al. 1995, MacKenzie et al. 2011). Instruments with high content validity typically exhibit two properties: a high correspondence between indicators and their targeted construct’s definition and low correspondence between indicators and the definitions of nontargeted constructs (Colquitt et al. 2019). Unlike other forms of validity tested by examining the psychometric properties of research instruments (e.g., construct validity), content validity is not adequately addressed in IS research. Because of the lack of attention, scholars in IS have noted that the link between indicators and their targeted construct is tenuous (Schmitz and Storey 2020). This represents a significant obstacle to theory building because inadequate measures do not allow for robust inferences (Aguinis and Vandenberg 2014). The IS field is not immune to this problem, because Burton-Jones and Lee (2017) argue that a shift of emphasis toward examining the extent to which conceptualizations and operationali zations share meaning is required. The proposed ontology can help the IS scholarly community create high-quality measures because it introduces a shared language that experts can use to represent the internal structure of indicators and construct definitions. An integration of ITEM and more recent AI-powered approaches to content validity (e.g., Pillet et al. 2025) may further improve the performance of content validation.

Correspondence is measured either by whether judges can correctly associate indicators with their focal construct definitions (Anderson and Gerbing 1991) or by the extent to which they agree that an indicator is an adequate measure of its construct definition (Hinkin and Tracey 1999). Still, these approaches suffer limitations. First, judging the content of certain constructs “requires more than intellectual ability or linguistic skills” (Colquitt et al. 2019, p. 1258). To some extent, this can be addressed by preferring subject-matter experts (Lawshe 1975) to naïve judges (Anderson and Gerbing 1991, Hinkin and Tracey 1999). Even then, domain experts might lack specific training for such a task and may be biased (Schriesheim et al. 1993). Second, neither Anderson and Gerbing (1991) nor Hinkin and Tracey (1999) offer metrics to understand the extent to which indicators fail to capture parts of the conceptual domain (underrepresentation). Therefore the risk is that content validity approaches become assessments of semantic similarities without engaging with representational nuances surfaced by ITEM.

We demonstrate how to validate content using ITEM on the indicators and constructs from the technostress scale developed by Ayyagari et al. (2011). This article was selected for its careful validation procedures, rigorous construct definitions, and use of scales for established IS constructs (e.g., usefulness), non-IS constructs (e.g., work overload), and new constructs (e.g., presenteeism).

Assessing content validity entails answering two key questions. First, does at least one indicator measure more than the defined construct by containing ontological elements absent from the definition? If so, the indica tor suffers from overrepresentation because it measures more than what is implied by the construct definition, meaning it possibly measures “construct-irrelevant variance” (Messick 1995). Second, does the scale, as a whole, measure less than the defined construct? If so, that violates MacKenzie et al.’s (2011) recommendation that indicators must collectively represent the entire content domain of the construct. Thus, the measures collectively suffer from “underrepresentation” (Messick 1995). Overrepresentation and underrepresentation decrease the content validity of the measure, potentially in ways that are not evident from the scale’s psychometric properties alone, which speaks to the need for alternative methods for content validity.

Figure 4. (Color online) ITEM Annotation of the Strain Definition  
![](/api/attachments/8B6RPM9S/fulltext/images/350e0a2cb2df3899c36da6b7fe31eb66ab07cc2a36a95162119632f732ef8891.jpg)

There are subtypes of overrepresentation and underrepresentation specific to IS in that they may occur when importing constructs from reference disciplines and adjusting them to the IS context but failing to do so appropriately. We term these IS overrepresentation and IS underrepresentation because the IS entity is involved in over- or underrepresentation.

In this section, we demonstrate how to use ITEM to represent the conceptual domain of the Strain construct from Ayyagari et al. (2011), a construct imported from a reference discipline. Figure 4 shows the entities and relationships identified in the focal construct definition. This can be compared with those of its indicators, represented in Figure 5, for assessing content validity.

Figure 6 displays all entities to facilitate comparing the ontological elements represented in the construct definition (Row D) and its indicators (Rows i1�i4); in the ITEM content validity procedure, we are not mapping relationships but do use them to cluster concepts, such as the cases of different entities placed in the same column (e.g., the value “more” with the attribute ‘quickly). In the strain example, such grouping was not necessary. The process for placement in columns preserves the syntactic structure of the definition as much as possible while mapping in each column the elements of the indicators that appear to measure the same concept in the definition. Entities in the indicators not associated with an entity in the definition were assigned to extra columns (columns 1, 5, 6, and 7). Below, we proceed to assess under- and overrepresentation from left to right. To define the degree to which the indicators faithfully represent the entities of the definition, we use three levels: acceptable (green in column header), somewhat acceptable (yellow), and problematic (red).

Column 1 is somewhat acceptable, although it suggests underrepresentation. Although the definition defines Strain as a (type of) “psychological response,” all the indicators use a Frequency Set to measure how often the respondent experiences a specific psychological response, such as those listed in Column 3. A more representative formulation of the definition would be “The frequency with which an individual experiences a negative psychological response to the stressors.”

Column 2 is acceptable. The definition defines Strain as an “individual” construct, and so do the indicators by mentioning “I” or “me.”

Column 3 is somewhat acceptable and suggests underrepresentation. Admittedly, the definition defines Strain rather broadly as “psychological response” (D) to stressors, whereas indicators can reasonably measure only specific types of negative psychological responses: “drained” (i1), “tired” (i2), “strain” (i3), and “burned out” (i4). However, even assuming that the indicators represent a sufficiently broad range of types of negative “psychological responses” (D) to stressors, we note that individuals’ psychological responses to stress do not have to be negative. For example, individuals may be able to cope with moderate stressors, perhaps because “buffers” (e.g., vacations, time off, colleagues) mitigate negative psychological responses to stressors and potentially lead to “good stress” (i.e., eustress).

Column 4 is somewhat acceptable, although it suggests underrepresentation. Whereas the definition focuses on “stressors,” the indicators measure only “activities” (i1, i2, i4) and “working” (i3) as work-related “stressors.” However, there are potentially more sources of work-related stressors, such as interpersonal or work-environment factors.

Figure 5. (Color online) ITEM Annotation of the Strain Indicators  
![](/api/attachments/8B6RPM9S/fulltext/images/603aff4dba1356c56fd23d0c5ea92cc9daf1480b61a3f78d67d2ecd6bc72bfb9.jpg)

Figure 6. (Color online) Comparison of the Ontological Elements in the Strain Construct’s Definition and Its Associated Items

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">D</td><td colspan="7">An individual&#x27;s psychological response to the stressors</td></tr><tr><td colspan="2">Individual(s)individual&#x27;s</td><td>Mental Attributepsychological response</td><td>Non-Physical Objectstressors</td><td></td><td></td><td></td></tr><tr><td rowspan="2">i1</td><td colspan="7">I feel drained from activities that require me to use ICTs.</td></tr><tr><td>Frequency Setnever (1) - daily (7)</td><td>Respondent(s)i</td><td>Mental Attributedrained</td><td>Taskactivities</td><td>Cause/Enablerequire</td><td>Activityuse</td><td>ISICTs</td></tr><tr><td rowspan="2">i2</td><td colspan="7">I feel tired from my ICT activities.</td></tr><tr><td>Frequency Setnever (1) - daily (7)</td><td>Respondent(s)i</td><td>Mental Attribetired</td><td>Taskactivities</td><td>Cause/Enablefrom</td><td></td><td>ISICTs</td></tr><tr><td rowspan="2">i3</td><td colspan="7">Working all day with ICTs is a strain for me.</td></tr><tr><td>Frequency Setnever (1) - daily (7)</td><td>Respondent(s)me.</td><td>Mental Attributestrain</td><td>ActivityWorking</td><td>Cause/Enableis</td><td></td><td>ISICTs</td></tr><tr><td rowspan="2">i4</td><td colspan="7">I feel burned out from my ICT activities.</td></tr><tr><td>Frequency Setnever (1) - daily (7)</td><td>Respondent(s)i</td><td>Attributeburned out</td><td>Taskactivities</td><td>Cause/Enablefrom</td><td></td><td>ISICTs</td></tr></table>

Column 5 is problematic and contains overrepresentation because it measures the relationship between ICTrelated activities and strain, rather than strain itself. This means the responder is asked to answer to what extent they believe that strain is caused by ICT-related activities, rather than to what extent they experience strain.

Column 6 is problematic because it implies that Strain relates to “use” (i1), therefore suggesting underrepresentation.

Column 7 is problematic because it shows underrepresentation, specifically IS underrepresentation. The indicators measure Strain exclusively as an IT-driven phenomenon, originating from using “ICTs” in “activities” (i1, i2, i4) or “working” (i3). This suggests that the indicators may be capturing “techno-strain” rather than general “strain.”

Carefully addressing these aspects of a definition has major implications for the scoping and claims of a theory. If the authors dropped the agent (as was done in some of the definitions, but not for stain) because they believed that the construct covers every living human, then readers may fairly question the representativeness of their respondent sampling.

In addition to the example scale discussed in this section, Online Appendix D analyzes additional constructs, many of which have scales that we categorized as “problematic,” meaning that they are under- or overrepresenting the focal construct definition significantly enough to render the scale an invalid measure for the focal construct. Many of these scales contain examples of IS underrepresentation, which is likely due to the import of constructs from a reference discipline. Online Appendix E guides researchers and editors in the use of ITEM for content validation.

## 5. Ontology Evaluation

Our goal is to create a high-quality ontology that adheres to ontology-building and evaluation approaches targeted to an audience of expert psychometricians. We directly evaluated our claims that the ontology is reliable, representative for IS indicators, and that psychometricians interested in using the ontology find it important, accessible, and suitable (Rosemann and Vessey 2008).

## 5.1. Evaluation 1: Reliability of the ITEM Ontology

To use ITEM to define and detect problems, we first need to show that it is understandable to researchers trained to code indicators. The goal is to evaluate whether IS researchers can understand the ontology and code indicators (with the support of the ITEM Codebook in Online Appendix A) and achieve acceptable interrater agreement on a set of indicators.

We measured the interrater reliability (IRR) for entities and relationships and employed standard mea sures of interrater reliability from linguistic coding (see, e.g., Palmer et al. 2005). We conducted three separate IRR exercises: first, for all the indicators from the MIS Quarterly paper by James et al. (2019)—where the first and fifth authors used the guidelines listed in the ITEM Codebook to code the indicators; second, for the indicators from the MIS Quarterly paper by Ayyagar et al. (2011), where the first, fourth, and fifth authors followed a similar coding protocol; and third, for the indicators from the MIS Quarterly paper by Zhang et al. (2011), where the fourth and fifth authors conducted the annotation. In all exercises, the annotators independently coded the indicators following a brief meeting to discuss an initial indicator. The annotators met periodically to discuss and resolve differences. Once entity coding was complete and a final indicator code set established for all indicators, the task was repeated to code relationships.

Table 2. Interrater Reliability

<table><tr><td>Evaluation and study</td><td>Role identification (Bennett Score)</td><td>Role classification (Cohen&#x27;s Kappa)</td></tr><tr><td>Entity (James et al. 2019)</td><td>0.920</td><td>0.836</td></tr><tr><td>Relationship (James et al. 2019)</td><td>0.921</td><td>0.815</td></tr><tr><td>Entity (Ayyagari et al. 2011)</td><td>0.872</td><td>0.714</td></tr><tr><td>Relationship (Ayyagari et al. 2011)</td><td>0.805</td><td>0.703</td></tr><tr><td>Entity (Zhang et al. 2011)</td><td>0.952</td><td>0.830</td></tr><tr><td>Relationship (Zhang et al. 2011)</td><td>0.803</td><td>0.659</td></tr></table>

Table 2 shows the average performance for IRR evaluations, including the Bennett Score (Bennett et al. 1954). Role identification was high for all entity and relationship coding. Similarly, role classification agreement was high, which was likely due to clear instructions in the codebook. The role classification agreements for both entity coding and relationship coding ranged between the low end of “almost perfect” and the midrange of “substantial,” based on Landis and Koch (1977). The results show that ITEM can be used to code indicators reliably.

## 5.2. Evaluation 2: Representativeness of the ITEM Ontology for IS Indicators

The quality of an ontology is typically measured based on how faithfully it can represent a domain of interest (Recker and Green 2019). In line with ontology evaluation processes, we validate our claim that the ontology is expressive for coding IS indicators through its application to the indicators from three IS theories and 99 randomly selected IS indicators. In the evaluation, al relevant indicator parts were coded as either representing an entity or a relationship, per the example in Sections 3.2–3.6. The detailed codebook with examples and tables containing fully defined entities and relationships is available in Online Appendix A.

The ontology was also tested to examine whether it had IS specificity. That is, it was able to fully represent the richness of information systems content in the indicators despite containing only one information systems-specific entity, IS. We examined the sample of indicators coded with ITEM and found that the ontology fully represents IS concepts through its relationships. For example, the isSubtypeOf relationship showed that an IS could be instantiated through different types of technologies, such as the indicator containing both the terms “Smart Metering” and “General Technology,” which was then coded as a subtype relationship (Smart Metering isSubtypeOf General Technology). Certain types of Information were partOf of the technology, such as product information being part of a website. The partOf relationship was also used to denote functions such as an Internet tool having chat rooms. The cause relationship was used to specify the effects that the IS has on the world, for example, on tasks. Beyond this, ITEM enabled the representation of several cases where an Activity involves IS or vice versa. For example, the Activities “use” and “working” were common, but the IS also involves Activity in an agentic sense, where respondents were asked whether the IS made promises and consequently kept them. Whether a person had access to the IS was also captured through the involves relationship. Additional relationships spe cified Attributes of whether an IS was useful and easy and whether a person’s Mental Attributes, such as inter est, addiction, or knowledge, were in response to the IS. Every IS-specific indicator could be fully represented using the ITEM Ontology, suggesting expressiveness of the ontology.

Future users of the ITEM Ontology may have use cases that require a more specific set of information systems subtypes. In such cases, we recommend expanding the IS entity with the type-of subhierarchy for Information Systems Technology in the Information Systems Ontology (Mueller et al. 2022).

## 5.3. Evaluation 3: Applicability Check

To obtain insights about the potential strengths and limitations of ITEM among potential users, we performed an applicability check (Rosemann and Vessey 2008), a type of criterion model validity, with 11 IS researchers from a ranking list of top IS researchers having an average of 14 years of post-PhD, academic experience (σ � 11.2) and 4,496 Google Scholar citations (σ � 7,787). We selected the first construct provided by a participant—signal credibility from Wells et al. (2011)—for the pre- and post-tasks and provided all participants with MacKenzie et al.’s (2011) criteria for indicator quality and content validity. We then surveyed participants about the content validity and clarity of the indicators.

After the survey, the author team gave a 45-minute training session introducing the ITEM Ontology and provided a process for ontology coding and use. Following the training in the ontology, participants were again provided with the signal credibility construct definition and indicators. Each indicator had been coded with ITEM, with the ITEMIZER used to detect indicator concerns. For each indicator, concerns detected were explained in clear text along with a definition of the indicator concern.

After being presented with ITEM findings, the participants were given the same survey. For each indicator of the signal credibility construct, they were asked how clearly worded the indicator was on a five-point scale, with a 5 indicating a strong agreement that the indicator was clearly worded. The prescores $( \mu = 3 . 0 3 ; \sigma =$ 0.96) were then compared with the postscores $( \mu = 1 . 6 7 ;$ $\sigma = 0 . 6 3 )$ with a t-test finding the delta significant (p < 0.01). The participants were then asked to evaluate the content validity of the indicators relative to the definition, first using MacKenzie et al.’s (2011) guidance (µ � $2 . 9 4 ; \sigma = 0 . 8 5 )$ and after the workshop using the ITEM guidance $( \mu = 1 . 7 8 ; \sigma = 0 . 8 6 )$ , a change in perspective that was again statistically significant $( p < 0 . 0 1 )$ ) and an indication of problems with the indicators.

Participants were then given a battery of open-ended questions about the impact, advantages, and disadvantages of the ITEM Ontology, followed by a set of quantitative indicators on a five-point Likert scale from Venkatesh et al. (2003) measuring ease of use $( \mu = 3 . 2 0 ;$ $\sigma = 1 . 1 4 )$ , usefulness $( \mu = 4 . 3 0 ; \sigma = 0 . 9 2 )$ , and intention to use the ontology $( \mu = 3 . 8 0 ; \sigma = 1 . 1 0 )$ . The middling ease of use score was balanced by the high-usefulness score, where most participants strongly agreed that the ontology would be useful. However, the intention to use score supports the qualitative feedback that an evaluation tool based on ITEM would need to be automated. The importance of ITEM in improving indicator evaluation was exemplified by a comment from one of the top researchers in IS: “As someone with significant experience with psychometrics/NLP/econometrics, I see this as a very useful tool, particularly for those who have had limited training/experience in psychometrics and survey development.” Another participant suggested that “having a well-defined, systematic way of evaluating indicator quality would be exceptionally valuable in terms of developing more precise and consistent measurement instruments.”

Suitability was also reflected in an expert comment: “I like the ontology as it will sensitize the community … to the issues with the design of items.” Other comments included “a good tool,” “it helps me be more systematic,” “it sensitizes you to issues which might have been so far accepted,” and “this approach might give researchers a rule-based logic to explain an otherwise vague feeling for why certain items might be problematic.”

The participants raised two main concerns. First, although the ontology “may help screen poor questions, it does not generate better ones, and the questions produced through screening by this method may or may not ever show statistical significance or load together on a factor analysis.” Second, one participant raised a concern that the approach assumes that the indicators represent complete sentences and that for one- to two-word indicators with a common stem, the ITEM Ontology may not work.

## 5.4. Evaluation 4: External Validity Check

As a final check, we examined a claim that the ITEM Ontology would also work outside of IS and conducted a workshop at the Gallup organization, considered among the foremost survey and polling companies in the world. Five survey and polling experts participated and were asked to provide oral feedback on the ontology. We changed the applicability check workshop to show more examples of indicator problem detection and coded some of the organization’s frequently used indicators.

The responses, both qualitative and quantitative, indicated that Gallup pollsters assessed ITEM as important, relatively accessible, and suitable (Rosemann and Vessey 2008) for meeting the identified needs of the community and useful for their own research. Although accessibility was perceived as low, based on comments suggesting that the ontology was complex and should be automated, ITEM’s suitability was reflected in expert comments suggesting that “this approach might give researchers a rule-based logic to explain an otherwise vague feeling for why certain items might be problematic.”

Three other participants reinforced these views with statements such as, “I really like the ontology,” “It is super helpful for working through how different pieces of an item connect to each other,” and “I LOVE that list of qualifiers. I think I need to save that list and read through it as I write items to think through how I am qualifying items - it does make a huge difference.”

## 6. Discussion and Implications 6.1. Contributions

Our contributions lie at the intersection of research on scale development (MacKenzie et al. 2011), ontological analysis, and linguistics (Robins 2014). This research develops an ontology of indicator parts based on a widely used upper-level ontology (DOLCE), enabling systematic analysis of indicator quality. The ITEM Ontology was iteratively evaluated and refined through independent coding and discussion of the indicators in Venkatesh et al.’s (2003) review of adoption theories and through a set of randomly selected indicators published in top IS journals. We introduce 42 entities grouped into four high-level ontological types—Objects, Measurables, Qualifiers, and Response Sets—as well as 24 relationship types to capture connections between ontological entities.

ITEM establishes a shared conceptual vocabulary for psychometric researchers. Equipped with this vocabulary, researchers can consistently describe psychometric scales. An indicator coded with ITEM makes the content of a psychometric indicator more transparent, thereby increasing the trust of reviewers, editors, and readers in the findings regarding what kinds of indicators researchers should adopt.

We conducted a literature review of indicator concerns to evaluate ITEM’s ability to support operational definitions. One such concern, double-barreled indicators, is operationally defined and evaluated above to demonstrate ITEM’s capability (the other concerns are defined and evaluated in Online Appendix B). We picked this example not because it is more important than other concerns but because psychometricians are more familiar with it and, despite considerable attention, it remains poorly understood. We developed a new IT artifact, the ITEMIZER, for finding potential problems in indicators based on their operational definitions and conducted a criterion validation of ITEMI-ZER. We also developed a new approach to content validation and conducted a separate examination of content validity for a published study, which surfaced important problems. Our contributions indicate that ITEM could be integrated into current expert-based assessment methods (see, e.g., Hinkin and Tracey 1999 and MacKenzie et al. 2011) to enhance their rigor.

We evaluated the ontology according to accepted ontology evaluation and validation methods (McDaniel and Storey 2020, Larsen et al. 2025) by examining how it captures the parts of indicators in the extant IS psychometric literature, including several constructs imported from other disciplines such as behavioral medicine and psychology, which arguably increases the external validity of ITEM on top of the external validity evaluation conducted with polling experts. An applicability check with IS scholars confirmed its importance, accessibility, and suitability. The results demonstrate that ITEM can guide communication between psychometric experts, who can then use it to provide common-sense guidelines for other researchers. Our work has extensive practical implications because of its potential to explain psychometric processes.

The tools developed during the project are available at the https://www.itemontology.org/ website (Figure 7). The website contains tutorial videos introducing the ontology and the entities agent, object, activity, causeenable, attributes, qualifiers, and response set before discussing relationships.

Users of the website may then start a new project or continue an existing project by coding their indicators using the BRAT tool infused with the ITEM Ontology (Figure 8). Once they are done coding a set of indicators, they may use the ITEMIZER tool on the website to generate a report of common problems encountered in the indicators. Online Appendix E shows an example report and proceeds to discuss the use of the results for authors and editors.

## 6.2. Implications and Insights

Because ITEM provides a common language for researchers to discuss indicator content, it can help us rethink the nature and properties of indicators from a linguistic and ontological mindset, rather than from the dominant statistical standpoint. A resulting practical benefit is that researchers can develop definitions, indicators, and problem specifications in a standardized way that enables new types of evaluation. As one expert stated, “knowing that there is almost like a blueprint … I found that aspect really fascinating.” Blueprints for a definition, an indicator, and a problem statement would differ, but knowledge of how to develop each would primarily require a basic understanding of the ITEM Ontology.

Figure 7. (Color online) The ITEM Ontology Website

![](/api/attachments/8B6RPM9S/fulltext/images/e3aa7df25fb9cf977091dd012f564fa7ae5b25ae05e10270e5425fe0015b7bfc.jpg)

The ITEM Ontology Proiect provides a platform for researchers to annotate and analyze survey indicators improving the guality and validity of measurements. Through tools like BRAT and ITEMIZER, users can detect and address semantic, lexical, and structural issues in indicators, ensuring they align with theoretical constructs and support more accurate research outcomes.

Tutorial Videos

Start New Project

Continue Existing Project

Figure 8. (Color online) Example Indicator Coding  
![](/api/attachments/8B6RPM9S/fulltext/images/d1f6ed568865a9f3275b61877c765f5538d1de3f7db1ede88e5a133f46866ad7.jpg)

Through constructing ITEM, we provide several insights. First, having an ontology and coded indicators enables one to gain a deeper understanding of indicators based on the patterns of entities and relationships, as we demonstrated in the operationalization of 16 concerns never operationally defined. Our research suggests that the subindicator level has been underutilized for strengthening validation and indicator quality and that ontological relationships are crucial for understanding indicators.

Second, through coding and examining a large sample of indicators, we learned that there are two basic types of indicators used in IS research. The first and most common is represented by the direct measurement of a measurable entity such as an attribute or activity. An example of this type of indicator is the perceived ease of use of a system. In the second type, an indicator measures the relationship between two entities, asking a respondent to estimate the extent to which using a system increases their productivity (where “using” and “productivity” are measurables of interest, but the evaluation is focused on the Cause/Enable measurable “increases”). This distinction does not appear in prior work. We found several scales that contained a mix of these indicator types, and we call on the discipline to examine whether such distinctions have empirical implications.

Third, we introduce Measurables and target measurables. The idea that it would be possible to sufficiently break down an indicator so that a Response Set could be pointed directly at the entity it primarily measured was a surprise even to the researchers on the project. However, as more indicators were broken down, confidence in this finding increased. This is a potentially valuable insight because it clarifies the core of an indicator and which entities play a supporting role in further specifying the domain an indicator purports to measure.

Fourth, we found that a high proportion of indicators and construct definitions used in papers published in top IS outlets have well-known and discussed concerns, even in indicators purported to have gone through state-of-the-art validation processes and the most stringent review processes in the discipline. There may be a sense within the psychometric community that every evaluation of indicators yields many concerns; after all, if these concerns were truly an issue, why do the scales pass common validity checks? Nevertheless, in theory testing, findings suggest that results may often be linguistic mirages (see, e.g., Gefen and Larsen 2017, Maul 2017, Gefen et al. 2020, Arnulf et al. 2021), further sup porting the importance of understanding and improving our measurement instruments (Forsyth et al. 2004) and the need to refocus validity evaluations to criterion validities (Menold and Raykov 2022).

Finally, by using ITEM, researchers can assess the validity of scales by analyzing their indicators at the entity level, thereby offering a more precise level of analysis than existing standards, which treat indicators as inseparable wholes. Specifically, we have demonstrated how ITEM enables assessing aspects of indicator quality (4.2) and content validity (4.3). For content validity, ITEM can serve to assess whether the indicators are faithfully representing their construct definitions by uncovering instances of over- or underrepresentation of indicators with respect to their focal construct.

For indicator quality, ITEM can formalize recognized indicator problems as ontological patterns. Once the indicators are annotated, scholars can inspect problematic patterns. Using ITEM will make scholars more successful in identifying and resolving problems in indicators.

## 6.3. Future Research

We note several limitations of the work presented here that can generate future research opportunities.

First, although we provide simplified rules for researchers and editors for applying ITEM in indicator quality and content validity analysis, we do not develop metrics and cutoff rules, because such decisions should emerge over time. Ultimately, applying these rules might enable researchers to develop a new form of validation for psychometric research—ontological validation—in which ITEM mediates between a construct definition and measurement items to determine conceptual fit. Future research can extend our research to develop methods and standards for ontological validation.

Second, psychometrics has unique claims to providing an understanding of an individual’s thinking and motivational drivers. Future research could examine how indicator structures, such as indicators that measure an attribute versus indicators that measure a relationship, have differential predictive validity.

Third, ITEM relies on ontological entities to categorize response set types. However, we did not examine the individual entities in the Response Sets. Although Likert scales likely represent the preferred option for IS indicators, further work should establish the preferred response set types, depending on the target measurable. We found several instances of target measurables measured through suboptimal response set types, such as measuring a respondent’s past behavior occurrence and frequency with an Agreement Set rather than a Nominal Set or Frequency Set.

Fourth, ITEM does not extend to knowledge that varies among the sample of participants but is not embedded in the indicators. For example, a survey designer may have selected a sample of respondents expected to have experience with a specific technology, such as a social networking tool, and take for granted that they know the technical term “swipe right.” An ontology does not address such terms but enables the secondary development of databases of entity instances or machine-learning tools. As such, these use cases are outside the domain scope of this ontology. However, we expect the many indicators imported into IS from other disciplines, such as behavioral medicine, marketing, and psychology, to bring concerns unique to any discipline focusing on IS in development or use and scope the ontology to address several concerns endemic in such imports. With this work, we present an ontology that IS scholars can use to solve measurement issues that have been with the psychometric field since its inception.

## 7. Conclusion

Psychometric research, although more than a century in the making, still operates without a deep understanding of what drives psychometric properties. Statistical approaches for construct validity are well-prescribed but built on an unstable foundation. Poorly specified rules for definition and indicator writing and evaluation yield unworkable notions of content validity. When construct validity approaches indicate the need to remove an indicator, researchers seldom reconsider content validity, nor do they have the ontological frameworks needed to understand why the indicator did not load appropriately. ITEM addresses this issue. To support pollsters, theory-focused researchers, and psychometricians, the ITEM suite of tools is made available on an external website with the BRAT coding tool, the ITEM Ontology, the ITEMIZER, the codebook, and many training videos. For ontology designers, the ITEM Ontology is made available on the open-source Prote´ge ´ Ontology Portal.

It is not our intent that every IS psychometric scholar knows how to code with ITEM. Rather, we see ITEM as important primarily for research on improving indicator and scale development—that is, as a precise language for communication between psychometric experts in IS. For the typical user of psychometric scales, we expect that ITEM will help develop intuition around scale development and that our discussion of such concerns will help the discipline better identify and avoid such concerns in the future.

## Acknowledgments

The authors thank Joerg Evermann for assistance during the early stages of the project and dozens of research assistants at the University of Colorado.

## Endnote

<sup>1</sup> SD – SA refers to scale with endpoints “Strongly Disagree – Strongly Agree.”

## References

Anderson JC, Gerbing DW (1991) Predicting the performance of mea sures in a confirmatory factor analysis with a pretest assessment of their substantive validities. J. Appl. Psych. 76(5):732–740.

Aguinis H, Vandenberg RJ (2014) An ounce of prevention is worth a pound of cure: Improving research quality before data collection. Annual Rev. Organ. Psych. Organ. Behav. 1(1):569–595.

Arnulf JK, Larsen KR, Martinsen ØL, Nimon KF (2021) Semantic algorithms in the assessment of attitudes and personality. Fron tiers Psych. 12(1):1–3.

Arp R, Smith B, Spear AD (2015) Building Ontologies with Basic For mal Ontology (MIT Press, Cambridge, MA).

Ayyagari R, Grover V, Purvis R (2011) Technostress: Technological antecedents and implications. MIS Quart. 35(4):831–858.

Babbie ER (2015) The Practice of Social Research (Cengage Learning, South Korea).

Bennett EM, Alpert R, Goldstein A (1954) Communications through limited-response questioning. Public Opinion Quart. 18(3):303–308

Bradburn NM, Sudman S, Wansink B (2004) Asking Questions: The Definitive Guide to Questionnaire Design–For Market Research, Political Polls, and Social and Health Questionnaires (John Wiley & Sons, San Francisco).

Bunge M (1977) Treatise on Basic Philosophy: Ontology I: The Furniture of the World (Springer Science & Business Media, Dordrecht, Holland).

Burton-Jones A, Lee AS (2017) Thinking about measures and measurement in positivist research: A proposal for refocusing on fundamentals. Inform. Systems Res. 28(3):451–467.

Chin WW, Johnson N, Schwarz A (2008) A fast form approach to measuring technology acceptance and other constructs. MIS Quart. 32(4):687–703.

Chung WH, Gudal RA, Nasser JS, Chung KC (2019) Critical assessment of surveys in plastic and reconstructive surgery: A systematic review. Plastic Reconstructive Surgery 144(5):912e–922e.

Colquitt JA, Sabey TB, Rodell JB, Hill ET (2019) Content validation guidelines: Evaluation criteria for definitional correspondence and definitional distinctiveness. J. Appl. Psychol. 104(10):1243–1265.

Compeau D, Correia J, Thatcher J (2022) When constructs become obsolete: A systematic approach to evaluating and updating constructs for information systems research. MIS Quart. 46(2): 679–712.

Converse JM, Presser S (1986) Survey Questions: Handcrafting the Standardized Questionnaire (Sage Publications Ltd., Thousand Oaks, CA).

Edwards JE, Thomas MD, Rosenfeld P, Booth-Kewley S (1997) How to Conduct Organizational Surveys: A Step-by-Step Guide (SAGE Publications, Thousand Oaks, CA).

Faulkner P, Runde J (2019) Theorizing the digital object. MIS Quart. 43(4):1279–1302.

Felderer B, Repke L, Weber W, Schweisthal J, Bothmann L (2024) Predicting the validity and reliability of survey questions (No. hkngd\_v1). OSF Preprint.

Flesch R (1948) A new readability yardstick. J. Appl. Psychol. 32(3): 221–233.

Floridi L (2013) The Philosophy of Information (OUP, Oxford, UK).

Forsyth B, Rothgeb JM, Willis GB (2004) Does pretesting make a difference? An experimental test. Presser S, Rothgeb JM, Couper MP, Lessler JT, Martin E, Martin J, Singer E, eds. Methods for Testing and Evaluating Survey Questionnaires (John Wiley & Sons, Inc., Hoboken, NJ), 525–546.

Gangemi A (2002) DOLCE+DnS ultralite ontology. Ontology Design Patterns. Accessed July 17, 2025, http://www.ontologydesign patterns.org/ont/dul/DUL.owl.

Gangemi A, Guarino N, Masolo C, Oltramari A (2003) Sweetening WordNet with DOLCE. AI Magazine 24(3):13–13.

Gangemi A, Guarino N, Masolo C, Oltramari A, Schneider L (2002) Sweetening ontologies with DOLCE. Internat. Conf. Knowledge Engrg. Knowledge Management (Springer, Berlin, Heidelberg), 166–181.

Gefen D, Larsen KR (2017) Controlling for lexical closeness in survey research: A demonstration on the technology acceptance model. J. Assoc. Inform. Systems 18(10):727–757.

Gefen D, Fresneda JE, Larsen KR (2020) Trust and distrust as artifacts of language: A latent semantic approach to studying their linguistic correlates. Frontiers Psychol. 11(1):561.

Graesser AC, Cai Z, Louwerse MM, Daniel F (2006) Question under standing aid (QUAID) a web facility that tests question compre hensibility. Public Opinion Quart. 70(1):3–22.

Granic ´ A, Marangunic ´ N (2019) Technology acceptance model in educational context: A systematic literature review. Brit. J. Edu cational Tech. 50(5):2572–2593.

Guttman L (1954) A new approach to factor analysis: The radex. Lazarsfeld PF, ed. Mathematical Thinking in the Social Sciences (Free Press, New York), 258–348.

Hackett PM (2021) Facet Theory and the Mapping Sentence (Springer, Boston).

Haynes SN, Richard DCS, Kubany ES (1995) Content validity in psychological assessment: A functional approach to concepts and methods. Psych. Assessment 7(3):238–247.

Hinkin TR, Tracey JB (1999) An analysis of variance approach to content validation. Organ. Res. Methods 2(2):175–186.

James TL, Wallace L, Deane JK (2019) Using organismic integration theory to explore the associations between users’ exercise motivations and fitness technology feature set use. MIS Quart. 43(1):287–312.

Khanna K, Sood G (2018) Motivated responding in studies of factual learning. Political Behav. 40(1):79–101.

Klugman CM, Lamb EG (2019) Research Methods in Health Humanities (Oxford University Press, New York).

Krosnick JA (1991) Response strategies for coping with the cognitiv demands of attitude measures in surveys. Appl. Cognitive Psych. 5(3):213–236.

Landis JR, Koch GG (1977) The measurement of observer agreement for categorical data. Biometrics 33(1):159–174.

Larsen K, Lukyanenko R, Mueller RM, Storey V, Parsons J, Vandermeer D, Hovorka D (2025) Validity in design science. MIS Quart. 49(4):1–34.

Lawshe CH (1975) A quantitative approach to content validity. Personnel Psych. 28(4):563–575.

MacKenzie SB, Podsakoff PM (2012) Common method bias in mar keting: Causes, mechanisms, and procedural remedies. J. Retailing 88(4):542–555.

MacKenzie SB, Podsakoff PM, Podsakoff NP (2011) Construct measurement and validation procedures in MIS and behavioral research. MIS Quart. 35(2):293–334

Man D (2013) Ontologies in computer science. Didactica Mathematica 31(1):43–46.

Maul A (2017) Rethinking traditional methods of survey validation. Measurement Interdisciplinary Res. Perspect. 15(2):51–69.

McDaniel M, Storey VC (2020) Evaluating domain ontologies: Clarification, classification, and challenges. ACM Comput. Surveys 52(4):1–44.

Menold N, Raykov T (2022) On the relationship between item stem formulation and criterion validity of multiple-component measuring instruments. Ed. Psych. Measurement 82(2):356–375.

Messick S (1995) Validity of psychological assessment: Validation of inferences from persons’ responses and performances as scientific inquiry into score meaning. Amer. Psychologist 50(9):741–749.

Moore GC, Benbasat I (1991) Development of an instrument to measure the perceptions of adopting an information technology innovation. Inform. Systems Res. 2(3):192–222.

Mueller RM, Huettemann S, Larsen KR, Yan S, Handler A (2022) Toward an information systems ontology. Drechsler A, Gerber A, Hevner A, eds. The Transdisciplinary Reach of Design Science Research, Lecture Notes in Computer Science (Springer International Publishing, Cham, Switzerland), 55–67.

Noy NF, McGuinness DL (2001) Ontology Development 101: A Guide to Creating Your First Ontology (Stanford, Redwood City, CA).

Oliveira T, Thomas M, Baptista G, Campos F (2016) Mobile payment: Understanding the determinants of customer adoption and intention to recommend the technology. Comput. Human Behav. 61(1):404–414.

Osterlind SJ (1998) Constructing Test Items: Multiple-Choice, Constructed-Response, Performance, and Other Formats (Springer, New York).

Palmer M, Gildea D, Kingsbury P (2005) The proposition bank: An anno tated corpus of semantic roles. Comput. Linguist. 31(1):71–106.

Petter S, Straub D, Rai A (2007) Specifying formative constructs in information systems research. MIS Quart. 31(4):623–656.

Pillet J-C, Larsen KR, Dobolyi D, Queiroz M, Handler A, Arnulf JK, Sharma R (2025) AI-augmented content validation in behavioral research: Development and evaluation of the RATER system. MIS Quart. Forthcoming.

Pirkkalainen H, Salo M, Tarafdar M, Makkonen M (2019) Deliberate or instinctive? Proactive and reactive coping for technostress. J. Management Inform. Systems 36(4):1179–1212.

Rahimi B, Nadri H, Afshar HL, Timpka T (2018) A systematic review of the technology acceptance model in health informat ics. Appl. Clin. Inform. 9(3):604–634.

Recker J, Green P (2019) How do individuals interpret multiple conceptual models? A theory of combined ontological complete ness and overlap. J. Assoc. Inform. Systems 20(8).

Robins RH (2014) General Linguistics (Routledge, London).

Rosemann M, Vessey I (2008) Toward improving the relevance of information systems research to practice: The role of applicabil ity checks. MIS Quart. 32(1):1–22.

Rossiter JR (2002) The C-OAR-SE procedure for scale development in marketing. Internat. J. Res. Marketing 19(4):305–335.

Rossiter JR (2011) Measurement for the Social Sciences: The C-OAR-SE Method and Why It Must Replace Psychometrics (Springer Science & Business Media, New York).

Rothgeb J, Willis G, Forsyth B (2007) Questionnaire pretesting methods: Do different techniques and different organizations pro duce similar results? Bull. Sociol. Methodology 96(1):5–31.

Saris WE, Gallhofer IN (2014) Design, Evaluation, and Analysis of Questionnaires for Survey Research (John Wiley & Sons, Hoboken, NJ).

Schmitz K, Storey VC (2020) Empirical test guidelines for content validity: Wash, rinse, and repeat until clean. Comm. Assoc Inform. Systems 47(1):787–850.

Schriesheim CA, Powers KJ, Scandura TA, Gardiner CC, Lankau MJ (1993) Improving construct measurement in management research: Comments and a quantitative approach for assessing the theoretical content adequacy of paper-and-pencil survey type instruments. J. Management 19(2):385–417.

Stenetorp P, Pyysalo S, Topic ´ G, Ohta T, Ananiadou S, Ji T (2012) BRAT: A web-based tool for NLP-assisted text annotation. Proc. Demonstrations 13th Conf. Eur. Chapter Assoc. Comput. Linguistics

(Association for Computational Linguistics, Stroudsburg, PA), 102–107.

Taylor S, Todd PA (1995) Understanding information technology usage: A test of competing models. Inform. Systems Res. 6(23):144–176.

Toulmin SE (2003) The Uses of Argument (Cambridge University Press, Cambridge, UK).

Tourangeau R, Rips L, Rasinski K (2000) The Psychology of Survey Response (Cambridge University Press, Cambridge, UK).

Venkatesh V, Morris MG, Davis GB, Davis FD (2003) User acceptance of information technology: Toward a unified view. MIS Quart. 27(3):425–478.

Wand Y, Weber R (1988) An ontological analysis of some fundamental information systems concepts. Proc. 9th Internat. Conf. Inform\`. Systems (ICIS) (Minneapolis), 213–225.

Wang RY, Strong DM (1996) Beyond accuracy: What data quality means to data consumers. J. Management Inform. Systems 12(4):5–33.

Weber R (2021) Constructs and indicators: An ontological analysis. MIS Quart. 45(4):1645–1678.

Wells JD, Valacich JS, Hess TJ (2011) What signal are you sending? How website quality influences perceptions of product quality and purchase intentions. MIS Quart. 35(2):373–396.

Willis GB, Lessler JT (1999) Question Appraisal System QAS-99. (National Cancer Institute, Rockville, MD).

Xu H, Zhang N (2022) From contextualizing to context theorizing: Assessing context effects in privacy research. Management Sci 68(10):7383–7401.

Zhang T, Agarwal R, Lucas HC Jr (2011) The value of IT-enabled retailer learning: Personalized product recommendations and customer store loyalty in electronic markets. MIS Quart. 35(4):859–881.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
