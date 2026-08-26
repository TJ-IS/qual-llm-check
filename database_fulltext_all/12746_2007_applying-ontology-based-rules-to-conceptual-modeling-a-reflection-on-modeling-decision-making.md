---
otero_id: 12746
otero_key: "2SH8C4KJ"
title: "Applying ontology-based rules to conceptual modeling: a reflection on modeling decision making"
authors: "Pnina Soffer; Irit Hadar"
year: "2007"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000683"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying ontology-based rules to conceptual modeling: a reflection on modeling decision making

Pnina Soffer<sup>1</sup> and Irit Hadar<sup>1</sup>

<sup>1</sup>MIS Department, University of Haifa, Israel

Correspondence:

Pnina Soffer, MIS Department, University of Haifa, Carmel Mountain 31905, Haifa, Israel. Tel: þ 972-48288506; Fax: þ 972-48288522; E-mail: spnina@is.haifa.ac.il

## Abstract

Conceptual modeling represents a domain independently of implementation considerations for purposes of understanding the problem at hand and communicating about it. However, different people may construct different models given the same domain. Variations among correct models, while known and familiar in practice, have hardly been investigated in the literature. Their roots are in the decisions made during the modeling process, where modelers face the need to map reality into modeling constructs. This paper reports an empirical study whose aim is to explore model variations and in particular to examine possible directions for reducing them. Specifically, the study uses a multimethod research paradigm to examine the effect of applying ontology-based modeling rules on modeling decisions as reflected in resulting model variations. The findings of the study provide insights into the variations phenomenon, as well as to the application of ontology-based modeling rules. European Journal of Information Systems (2007) 16, 599–611. doi:10.1057/palgrave.ejis.3000683

Keywords: conceptual modeling; ontology; variations; empirical study

## Introduction

Conceptual modeling is aimed at reflecting the real world independently of implementation technology and constraints (Topi & Ramesh, 2002). It has an important role in defining, analyzing, and communicating about the requirements for the system to be. Nevertheless, it has been observed that different people may present different models given the same domain (Hadar & Soffer, 2006). We term the differences in constructs and relations between adequately constructed models (see Schuette & Rotthowe, 1998) model variations.

While model variations are well known to exist and are familiar to anyone who ever experienced conceptual modeling, it seems that their real essence has been overlooked so far. Model variations are the result of different decision paths taken by different modelers through the modeling process. Since conceptual models are used for understanding and communication, consistency of these models is of importance. In addition, when attempting to reuse or to match conceptual models, variations might reduce the chances of identifying adequate matches (Soffer & Hadar, 2003). Investigating model variations as a reflection of modeling decisions can lead to an understanding of the modeling process and its embedded decision making, as well as to possible directions for achieving a higher uniformity of models.

When looking at adequately constructed although different models, the variations may either reflect different perceptions of the modeled domain or inconclusiveness in the decision making during the modeling process. In particular, these decisions relate to the representation of the real world by modeling constructs. In this paper, model variations are empirically investigated for two main purposes. We wish to examine possible directions for reducing model variations, and to gain further understanding of the modeling process and its decisions. Our underlying assumption is that model variations can be reduced if better guidance is given to support transforming information about the real world into modeling constructs. Such guidance should be consistent and theoretically anchored. The remaining variations are expected to be the ones that truly reflect different perceptions of the domain. These differences should be addressed when developing an information system (IS) for that domain.

Several theoretical frameworks for conceptual modeling have been suggested in recent years. The strength of these frameworks is in their explicit guidelines, which should increase conclusiveness in the modeling decision making. Hence, applying them can be expected to reduce variations among models of different modelers. These frameworks rely on different kinds of theoretical foundations, such as ontology (e.g., Evermann & Wand (2001, 2004, 2005) and Guizzardi et al. (2002, 2004)), speech–act theory (Agerfalk & Eriksson, 2004), and classification theory (Parsons, 1996). In particular, ontology-based frameworks provide clear modeling rules to be applied when using a specific modeling grammar for conceptual modeling. Ontologies, as models of the real world, have been applied for evaluating the expressive power of modeling grammars (Wand & Weber, 1993) and as a basis for analyzing modeling constructs and their representation of real-world phenomena (Bodart et al., 2001; Opdahl et al., 2001). Evermann & Wand (2001, 2004, 2005) and Guizzardi et al. (2002, 2004), each relying on a different ontology, suggested rules for conceptual modeling using UML Class Diagram.

In this research, we empirically investigate how applying an ontology-based set of modeling rules affects model variations, and in particular, whether such rules can contribute to the reduction of model variations. The study reported here examined model variations incurred with and without applying modeling rules, while exploring the considerations and cognitive processes taking place when making modeling decisions.

The remainder of the paper is organized as follows: the next section presents theoretical background including a framework that explains model variations, a general introduction to ontology-based modeling rules, and the research questions. The following sections describe the methodology and settings of the empirical study and present its findings. We then discuss these findings and present our conclusions as well as future research directions.

## Theoretical background and research framework

## Ontology-based modeling rules

Ontology-based modeling rules rely on an ontology, which is a model of the world. The fundamental premise is that in order to fully represent the world in a conceptual model, an ontological meaning should be assigned to the modeling constructs. The use of constructs without distinct ontological meaning may lead to an ontologically meaningless or ambiguous model, or to multiple model representations of the world.

Hadar & Soffer (2006) indicate that although different ontologies yield different modeling rules (e.g., Evermann & Wand, 2001, 2004, 2005; Guizzardi et al., 2002, 2004), the availability of such rules to rely upon may assist the decision making in the modeling process. The ontological framework used in this paper is the Evermann & Wand (2001, 2004, 2005) framework. Comparing this framework with the one by Guizzardi et al. (2002, 2004), Hadar & Soffer (2006) found that it provides a broader and easier to apply set of rules for the purpose of reducing model variations. The Evermann & Wand (2001, 2004, 2005) framework is based on Bunge’s (1977, 1979) ontology as adapted for IS modeling (Wand & Weber, 1993, 2002) and follows the notion of ontological expressiveness (Wand & Weber, 1993). Their work analyzes the constructs of UML Class Diagrams, State Charts, Collaboration, and Sequence diagrams, and provides rules that are intended to assure a distinct ontological meaning of these constructs. The rules include representation rules, which define a mapping from the ontological constructs to the modeling constructs, and interpretation rules, which map in the opposite direction. In this paper, we relate to a subset of the rules addressing some of the constructs of class diagrams, as will be explained in the following section.

Note that different works have relied on Bunge’s ontology in order to provide guidance to constructing UML models (e.g., Burton-Jones & Meso, 2002; Parsons & Cole, 2004). Nevertheless, these works address specific constructs and do not provide an overall set of modeling rules. The Evermann and Wand rules were further investigated by Lu and Parsons (2005), who tried to validate them by developing a CASE tool that incorporates them. Their findings indicate the existence of some redundancies and inconsistencies with respect to the entire rule set. These findings justify our motivation to apply only a subset of the rule base in our study.

Previous empirical studies addressing ontology-based modeling guidance related to the effect of such frameworks on the understanding of models. For example, Burton-Jones & Meso (2002), Parsons & Cole (2004), and Poels et al. (2005) evaluated the understanding of models produced both in compliance and not in compliance to ontology-based modeling rules. The effect of this guidance on model construction has not, to the best of our knowledge, been empirically investigated so far.

## Research framework

Soffer & Hadar (2003) proposed a framework for understanding the sources of model variations, which was partially based on theoretical foundations by Topi & Ramesh (2002). Three classes of factors were identified as influencing the model produced by an individual for a given purpose. These include human factors, factors related to the modeling grammar, and factors related to the modeling process.

This research addresses factors related to the modeling process, and particularly the decisions of how to map real-world phenomena into modeling constructs. It is primarily aimed at exploring how modeling rules affect the conclusiveness of modeling decision making, as reflected in the resulting model variations. Hence, our main research question is: (1) what is the effect of applying modeling rules to the modeling process on model variations?

Our assumption is that model variations occur whenever a modeling decision may lead to more than one legitimate choice of a modeling construct. Considering a classification of variations to variation types, which can be related to modeling decisions from which they stem, we propose a set of modeling rules. These are specifically aimed at reducing the number of choices for each such decision type to one possible solution. In the study, we examine whether the application of the modeling rules indeed affects the modeling decisions and leads to this desired result.

In order to do so, the modeling rules should (a) be practical and simple enough to apply and (b) overcome factors that contribute to model variations (Soffer & Hadar, 2003). While testing the applicability of the modeling rules, we consider it beneficial to characterize the situations and decision types in which the rules are indeed applicable and reduce variations and the situations where they do not. To gain more understanding about decision-affecting factors and their interaction with the modeling rules, we formulate a second research question: (2) what are the factors affecting the modeling decisions as reflected in model variations, and are their effects reduced when modeling rules are used?

This question is exploratory, relating to the nature of the decisions made during the process of mapping reality into modeling constructs. In the study, we address it as a secondary research question.

## Empirical study

## Methodology

Our research questions focus on different aspects of the phenomenon we intend to study. Hence, we selected a research methodology incorporating several methods. A combination of research methods, especially from both qualitative and quantitative paradigms, was proven within the IS discipline as effective and contributing for gaining a wide and deep understanding (cf. Kaplan &

Duchon, 1988; Galliers, 1991; Lee, 1991; Landry & Banville, 1992; Mingers, 2001).

In this research, we wish to examine and draw generalizable conclusions about whether applying modeling rules reduces the extensiveness of model variations, characterize the effects of using modeling rules on the modeling process and the resulting model variations, and identify factors affecting modeling decisions made with and without applying the rules. Throughout our results presentation and analysis, the data regarding the first research question will be examined and discussed through the lens of both qualitative and quantitative methodologies. The second research question, being fully exploratory, will be discussed only from the qualitative perspective.

## Setting

In order to study the influence of modeling rules on model variations, we must first identify both dependent and independent variables, and plan their manipulation and control. Types of variables affecting model variations include human factors, the modeling grammar used, the purpose of modeling, and the modeling process. Our intention is to manipulate the modeling process via the use of modeling rules; hence, the other three categories of variables should be controlled.

The human factors include several issues such as the modelers’ experience and knowledge in systems analysis and development, their prior knowledge regarding the modeled domain, etc. In order to control these variables, we conducted our study with the participation of students, all with similar educational background, and very limited former experience in industry. As well, we designed the two tasks concerning two different domains: one was a domain very well known to all students (university) while the other referred to a domain we believed, and later verified this in class, to be quite remote to our students (physical transportation of goods).

The modeling grammar used throughout this study was UML. Therefore, no model variations whose source is the use of different modeling grammars were to be observed. The purpose of modeling, as explained to the students, was to understand the problem as a basis for IS requirements analysis.

The manipulated variable was the modeling process, influenced by the use of modeling rules. The specific rules were chosen according to the expected model variation types. In a previous exploratory study conducted in industry (Hadar & Soffer, 2006), we had identified and classified variation types in UML Class Diagram conceptual models, as summarized in Table 1.

Based on this classification, we selected a subset of modeling rules (Table 2) from the rule base suggested by Evermann & Wand (2001, 2004, 2005). Two main considerations led us in this selection. First, to include the rules relevant to the variation types previously identified (Table 1). Second, to construct a rule set minimal in size, simple, and easy to use. Our concern was to prevent creating new variations resulting from misuse of complex rules due to misunderstanding and lack of experience in applying them. Note that the phrasing of the rules is somewhat modified with respect to the original rules for the purpose of simplicity and ease of use by the students.

Table 1 Initial classification of variation types

<table><tr><td>Variation type</td><td>Description</td></tr><tr><td>Class vs association</td><td>Inconsistency in distinguishing between a regular class and an association (or association class).</td></tr><tr><td>Aggregation vs composition</td><td>Inconsistency in distinguishing aggregation from composition.</td></tr><tr><td>Abstract classes</td><td>Generalizing classes that have no instance of their own. May or may not be modeled.</td></tr><tr><td>Association vs aggregation</td><td>Inconsistency in distinguishing association from aggregation.</td></tr><tr><td>Association with classes that have part-whole relationship</td><td>Inconsistency in associating a third party class either to the whole or to the part class.</td></tr></table>

Table 2 Ontology-based modeling rules used in the study

<table><tr><td>No.</td><td>Rule</td><td>Variation types addressed</td></tr><tr><td>1</td><td>Abstract classes, which are classes that do not possess their own instances, are not to be used in conceptual modeling.</td><td>Abstract classes</td></tr><tr><td>2</td><td>Composition relations are not to be used in conceptual modeling.Part-whole relationship should always be expressed by an aggre-gation relation.</td><td>Aggregation vs composition</td></tr><tr><td>3</td><td>An aggregation relation exists when the whole possesses at least one property which is not possessed by its parts, and is a result of their aggregation.</td><td>Association vs aggregation</td></tr><tr><td>4</td><td>In aggregation relation, every property that can be associated either to the whole or to the part, shall be associated to the parts.</td><td>Association with classes that have part-whole relationship</td></tr><tr><td>5</td><td>Every association should be represented by an association class.</td><td>Class vs  $association^a$ </td></tr><tr><td>6</td><td>Association class instances cannot be substantial things.</td><td>Class vs association</td></tr><tr><td>7</td><td>If a class A is associated to a composite, whose whole is B and part is C, then if there is at least one property that is mutual to A and the whole (B), and not related to the part (C), then A is associated to B. Otherwise A is associated to C.</td><td>Association with classes that have whole-part relationship</td></tr></table>

<sup>a</sup>Rules number 5 and 6 together are aimed at guiding the modeler in representing classes and associations. First, rule number 5 determines that every association needs to be modeled as an association class, and then rule number 6 provides a clear criterion for distinguishing a ‘real’ class from an association class.

The population of the empirical study was senior undergraduate Management Information Systems (MIS) students, who took the course ‘Requirements Analysis Seminar’. The empirical study took place after the students had learnt about conceptual modeling, its essence and importance, and had experienced the construction of such models both in class and as a homework assignment. As a result, the students’ experience in conceptual modeling was sufficient so that significant learning was not expected to occur between the two modeling tasks performed in the experiment.

The participants in the experiment were first randomly divided into two groups. The experiment included three phases:

1. Each group received one of the two tasks presented below. The students created a conceptual model based on the textual description they received. Although the tasks were performed in class, no time limitation was placed.

2. The students were taught the modeling rules (Table 2). The teaching process included presentation of the rules, several examples and class discussion.

3. Each group received the task they had not handled in phase 1. The students were asked to produce a conceptual model based on the description they received while applying the modeling rules.

In addition, we had a control group, which was handled similarly, but without phase 2 of the experiment. The experiment group consisted of 37 students, randomly divided to two subgroups of 18 and 19 students. The control group consisted of 36 students, randomly divided to two subgroups of 18 students each.

The data collection included the following: (1) the conceptual models created by the participants; (2) modeling dilemma documentation – the students were asked to write down any dilemma they faced while constructing the models; (3) observations of class discussions; and (4) individual interviews with some of the participants, for an in-depth understanding of their thinking process.

The analysis of the written models was aimed at finding how using the modeling rules affected the models created, and in particular, the model variations. The quantitative analysis aimed at determining whether there was indeed such an effect and if so, how extensive this effect proved to be. It related to the following hypotheses:

H0: The difference in the choice of modeling constructs between the second and first tasks will be the same in the experiment and control groups.

H1: The difference in the choice of modeling constructs between the second and first tasks will be different in the experiment group (making choices more consistent with the modeling rules in the second task) as compared to the control group.

These hypotheses rely on the assumption that in order to reduce variations the rules are required to change the way modeling decisions are made. We tested the hypotheses separately with respect to each variation type listed in Table 1, using Mann–Whitney U-test. This test was chosen because normality assumption was not reasonable due to the relatively small number of possible modeling constructs in each model.

The qualitative content analysis of the models, documented dilemmas, class discussions, and interviews was intended to gain an in-depth understanding of how the effect of the rules was achieved. The content analysis was conducted according to the principles of Strauss & Corbin (1990). The data (i.e., models and text) were coded and classified according to variation types and emerging decision-affecting factors.

The models that were identified as clearly inadequate and could not be justified in the interview as representing a coherent line of thinking were not included in the final data analysis. The screening of inadequate models was initially conducted separately by each of the two researchers. This was followed by a discussion leading to an agreement as to the potentially inadequate constructs. A follow-up interview was conducted with each of the relevant students, to determine whether the rationalization supplied by the student was valid. The main criterion was whether consensus could be achieved (Schuette & Rotthowe, 1998) regarding the model being a representation of the domain. After eliminating the models for which no consensus was established, 68 models were included in the data obtained from the experiment group and 66 from the control group.

A summary of all data collection and analysis methods and tools, as well as the purpose and expected outcomes of each of them, is presented in Table 3.

## The tasks

Each task included a textual description of a domain. The two domains were quite different for three reasons. First, we wished to avoid a situation where in the second modeling phase the students would be biased by their previous solution rather than apply the rules as part of the modeling process. Second, we did not want our findings to reflect domain-specific phenomena. Third, we wished to control the prior domain knowledge variable, by presenting to the students two domains that differ in the prior knowledge the students possess about them. The two tasks are presented in Table 4.

## Findings

Being an exploratory study, its findings extend beyond the initially defined research questions. While the research framework was designed according to the five previously identified variation types (Table 1); in this study, two additional variation types arose from the field. In this section, we first present these two newly identified variation types. Then we present the findings related to the two predefined research questions. We describe the effect of the rules as observed in the empirical study, analyzing it for each type of variation, and present

Table 3 Data collection and analysis summary

<table><tr><td>Data</td><td>Collection tool</td><td>Analysis method</td><td>Purpose</td><td>Expected outcome</td></tr><tr><td>Models</td><td>Written models formulated by students in the class exercises.</td><td>Codification, classification, and application of Mann Whitney U-test.</td><td>Test of the effect of the rules.</td><td>To what extent and in which variations are the rules effective.</td></tr><tr><td>Class discussions</td><td>Documented observations.</td><td>Text analysis.</td><td>Identify underlying assumptions and rationale of modeling decision.</td><td>Rationale of modeling decisions.</td></tr><tr><td>Written dilemmas</td><td>Written dilemmas documented by students in the class exercises.</td><td>Text analysis.</td><td>Identify difficulties in decision making.</td><td>Factors affecting model variations.</td></tr><tr><td>Interviews</td><td>Unstructured interviews</td><td>Text analysis.</td><td>Clarify specific model constructs suggested by students</td><td>Final elimination of incorrect models from the data; rationale of modeling decisions.</td></tr></table>

## Table 4 The tasks

## Task A

A university wishes to automate its course registration procedure. The procedure is now handled as follows: for each course, several course offerings are available to the students. Each course offering entails different lecture and lab hours, and at times, different professors as lecturers. A maximum number of 40 students can be registered to each course offering. Students decide which courses and course offerings they wish to register to, fill in a registration form, and submit it to the department’s secretary, who manually adds the students to the relevant course offerings. If the course offering chosen by a student is full (40 students are already registered), the secretary adds the student to a different, available one. The planned system will enable the students to register without the secretary’s involvement.

## Task B

A transportation firm has a main warehouse and several local area centers. The firm owns a fleet of trucks, so that each local center has a specific group of trucks. At the beginning of each day, items from the main warehouse are loaded on the trucks. The loaded trucks are driven to the local centers and, after being unloaded, return empty to the main warehouse. A dispatcher allocates the requested items to the trucks according to their delivery address, considering their volume (expressed in standard volume units) and according to the capacity of the trucks, which is limited to 150 volume units each. The dispatcher assigns the drivers who work on that day to the trucks that are planned for shipment. The planned system will manage the allocation of the drivers and the items to the trucks.

findings that indicate additional factors affecting the modeling decisions.

## New variation types identified

The variation types that were observed in the study mostly overlap the initial classification we used as a basis for the rule selection. However, that initial classification was based on data collected in industry (Hadar & Soffer, 2006). In the current study, whose subjects were students, when codifying the model constructs according to the predefined scheme, we identified several constructs that did not fit this scheme. We extracted and isolated these constructs and applied content analysis, in accord with the one performed in Hadar & Soffer (2006), thus identifying two additional variation types. These relate to using the construct of an association class, and to ternary versus binary relations.

A large group of variations regarded the arity of associations. The study participants varied greatly in deciding which entities participate in each association, and in particular, whether they are binary or ternary relations, as shown in the example of Figure 1.

Another variation type found was related to whether to use association classes or simple associations in relations. Table 5 summarizes the findings regarding the use of associations and association classes in binary and ternary relations. The numbers in the table indicate the total count of each construct in the models obtained without the application of rules. We found no evidence for a structured or consistent decision-making process about whether or not to use association classes in binary associations, whereas a clear tendency to use association classes was found in ternary relations.

Although the association class variation type was not found in our previous research, the subset of the modeling rules applied in this study included a rule dealing with this issue, but no rule dealing with the arity of relations.

![](/api/attachments/2SH8C4KJ/fulltext/images/4e693a8cb5c3faae1567d597cef2fe15ef31269f78a93ad4f602814d95b74f01.jpg)  
Figure 1 Binary vs ternary relations – an example.

Table 5 Association vs association class in binary and ternary relations

<table><tr><td>Construct</td><td>Binary 1:1 relation</td><td>Binary 1:M relation</td><td>Binary M:N relation</td><td>Ternary relation</td></tr><tr><td>Association</td><td>34</td><td>90</td><td>26</td><td>4</td></tr><tr><td>Association class</td><td>7</td><td>18</td><td>7</td><td>23</td></tr></table>

## The effects of applying a set of modeling rules on model variations

Our expectation, when defining the set of rules, was that they would lead to a more consistent modeling decision process and reduce the variations. In reality, this was partially achieved. The effect was measured as follows. Consider a variation type that relates to the selection of one of two possible constructs at a certain situation (constructs A and B). For each participant in the study, we measured the ratio of selecting construct A from the total of A and B (as percentage). Assuming the rules affect the modeling decisions, this ratio should be different in the second task of the treatment group, whereas no such difference should appear in the control group. We statistically tested for significance, the difference in the ratio achieved in Task 1 and Task 2 in the treatment group as compared to the control group. The statistical test used for this purpose was Mann–Whitney U-test. Note that the expected effect in all the cases was that the ratio would increase in the treatment group when the rules are applied (Task 2), hence the mean difference should be positive.

The findings indicate that applying the modeling rules had a significant effect on the decisions made regarding two of the variation types. The types where no significant effect was made can be divided to (a) cases where only a small minority of the modelers varied in their decision from the others before the intervention, thus the sample was too small to test for significance and (b) cases where indeed no effect of the rules was observed. In what follows we discuss the findings relating to each variation type, and explain them in light of the qualitative data analysis.

## Association vs association class

As shown in Table 6, the experiment group encountered a clear effect of the rules on the decision made, as compared to the control group (P ¼ 0.0003).

Two reasons may have caused this dramatic effect. First, the relevant rule (rule no. 5, Table 2) was conclusive and easy to apply. Second, using an association class for every association does not change the semantics of the relation. It is merely conceived as a syntactical change, namely, the association class has become a part of the symbol for an association. The effect is clearly observed in the qualitatively addressed information sources. For example, one of the modeling dilemmas recorded in the first task was: ‘I don’t have any association class in the model. Is this ok?’. This issue was addressed in the experiment group in eight of the written dilemmas in the first task and in one in the second task. In the control group, this dilemma was recorded four times in the first task and five times in the second. In a class discussion about when to use association classes, some of the students argued that association classes should be used for ternary relations only, while others claimed they can be used for binary relations too, depending on the nature of the relation. However, the latter could not name any clear indication about when these should be used. When the relevant rule was introduced in class, the students were puzzled at first by the massive use of association classes; however, they expressed relief about the simplicity of the decision they are required to make.

## Association vs aggregation

The rule under consideration (rule no.3, Table 2) was expected to assist in the decision of whether a relation is an association or an aggregation. An example of this variation type is presented in Figure 2.

As shown in Table 6, the effect on decision making in the experiment group was significant as compared to the control group (P ¼ 0.0129). However, variations were not completely eliminated. The relevant rule guides the modeler to look for an emergent property, which is a property that a composite (whole) has, and is not possessed by any of its components. If such a property is identified then the relation between the entities should be aggregation (and association otherwise). The partial success in applying this rule shows that the modelers encountered difficulty in identifying an emergent property (e.g., the used capacity of a truck in the item– truck relation) and consequently, in making the decision. In an interview with one of the modelers, she described the way the rules helped her identify the relation between a course offering and a course as an aggregation. However, the same modeler explained her decision not to use an aggregation relation between a student and a course offering based on the fact that she could not identify an emergent property of a course offering as an aggregate of students. This shows that the modeler’s line of thinking was consistent with the rules, but the resulting model was not, due to her difficulty to identify an emergent property (e.g., a course offering being fully booked).

Table 6 Summary of rule application outcome

<table><tr><td rowspan="3">Variation type</td><td rowspan="3">Ratio measured</td><td rowspan="3">Comments</td><td colspan="4">Observed effect (Task 2-Task 1)</td><td rowspan="3">P-value</td></tr><tr><td colspan="2">Treatment</td><td colspan="2">Control</td></tr><tr><td>Means</td><td>SD</td><td>Means</td><td>SD</td></tr><tr><td>Association vs association class.</td><td>Association class/(association class+association).</td><td>Regarding binary relations.</td><td>56.62</td><td>47.92</td><td>-1.98</td><td>49.24</td><td>0.0003</td></tr><tr><td>Aggregation vs association.</td><td>Aggregation/(aggregation+association),</td><td>Regarding only relations that according to the rules should be aggregation.</td><td>14.95</td><td>55.45</td><td>-9.56</td><td>42.51</td><td>0.0129</td></tr><tr><td>Class vs association class.</td><td>Class/(class+association class),</td><td>Regarding only association classes confused with classes.</td><td>3.84</td><td>8.02</td><td>0.28</td><td>9.44</td><td>0.0934</td></tr><tr><td>Aggregation vs composition.</td><td>(Aggregation +association)/(aggregation+association+composition).</td><td>Regarding all relations that according to the rules should be aggregation; in some cases were modeled as association.</td><td>13.89</td><td>40.73</td><td>8.57</td><td>29.97</td><td>0.2578</td></tr><tr><td>Abstract classes.</td><td>Non-abstract class/all classes.</td><td>Not including association classes.</td><td>0.01</td><td>0.05</td><td>0.01</td><td>0.04</td><td>0.488</td></tr><tr><td>Association with part-whole.</td><td>Association with part/(association with part+association with whole).</td><td>Regarding cases where according to the rules the association should be with the part.</td><td>-9.54</td><td>45.48</td><td>-22.22</td><td>34.73</td><td>0.2207</td></tr></table>

## Class vs association class

Several entities were modeled by some students as association classes while others modeled them as regular classes, as exemplified in Figure 3.

This type of variation was not very common. The initial number of association classes used for entities that could be represented as classes was small in both groups (seven in the experiment group and five in the control group in Task 1). In the experiment group no such case was observed when the rules were applied, while the control group remained with four such cases. Due to the initial small number of instances of this phenomenon, although the number was reduced to zero in the second task, the effect of the rules was not statistically significant (P ¼ 0.0934). The evidence from the other sources suggest that the distinction between substantial and insubstantial instances (rule no. 6, Table 2) was clear and helped the modelers distinguish between ‘normal’ and association classes. For example, after presenting the modeling rules in class, an example of an employee and an organization was discussed. There was a dispute whether the employee’s salary is a class or an association class. Some of the students argued that a salary is merely a property of the association between the employee and the organization. However, relating to the rule that association classes cannot have substantial instances, all the students were convinced that a salary should be a class, since it is indeed substantial.

![](/api/attachments/2SH8C4KJ/fulltext/images/07c10bdf5fea5ed3e62357ec9ac8e2c287a5954dcd1a393b902f371be4bf8cb5.jpg)  
Figure 2 Association vs aggregation relations – an example.

## Composition vs aggregation

This inconsistency was observed in relations between a whole and a part, which some students modeled as composition while others used aggregation relation, as illustrated in Figure 4.

Even though in both groups the number of composition constructs used was small to begin with (five in the experiment group and four in the control group), it was not used at all when the rules were applied. Here too, the small number of observations did not enable identifying a statistically significant difference between the experiment and the control group. However, analyzing the effect achieved in the experiment group separately using Wilcoxon Signed Rank test for paired samples indicated a significant effect of the rules (P ¼ 0.0495), and no significant effect in the control group. The rule applied for this decision (rule no. 2, Table 2) implies a change in the semantics of the construct. However, it is conceived as a minor one. When this specific rule was introduced in class, a minority of the students claimed that structural information is lost due to this rule, while the majority of the students expressed relief that they do not have to make a decision about this issue. Many students described the distinction between composition and aggregation as being particularly difficult to make.

## Abstract classes

This variation type appeared when some students used abstract class to express the existence of common properties of two or more entities (Figure 5).

The use of abstract classes was not common in the models initially produced (it was applied by four modelers in the experiment group, and by one modeler in the control group in Task 1). Nevertheless, our expectation had been that these would not appear at all when the rules were applied, since the relevant rule (rule no. 1, Table 2) is very clear and conclusive, and does not require any decision making by the modeler. Surprisingly, no significant change was observed in the use of abstract classes in the experiment group relative to the control group (P ¼ 0.488). We relate this result to a more general phenomenon observed: the use of design considerations while dealing with conceptual modeling. When the abstract class rule was discussed in class prior to the second task (in the experiment group), several students claimed that neglecting the use of abstract classes may lead to low-quality design. Although it has been emphasized that conceptual modeling should not reflect design considerations, similar claims had already been repeatedly raised in conceptual modeling sessions. This may imply that students have difficulty in letting go of designoriented thinking. Consequently, despite the conclusiveness of the rule, students who felt the need to include abstract classes in their model (as evident in the first task) kept their view that abstract classes contribute to the quality of the model and hence used them again in the second task.

![](/api/attachments/2SH8C4KJ/fulltext/images/bee8edd3d4bba463d7d2d3109ff1be420cc67b0d11071a10b61de3c6f1594056.jpg)  
Figure 3 Class vs association Class – an example.  
Figure 4 Composition vs aggregation relations – an example.

![](/api/attachments/2SH8C4KJ/fulltext/images/c417134f44938b4442dfd9936e1e690c7c9d6ef61a56bf679255317fdbe7fb42.jpg)  
Figure 5 Using abstract class – an example.

## Associations with part–whole

This decision, illustrated in Figure 6, is whether an association is with the whole or the parts of a composite.

In order to apply the relevant rules (numbers 4 and 7, Table 2), not only did the modelers have to identify an emergent property (thus an aggregation), they also had to relate it to a mutual property arising from an association. The difficulty regarding this decision was described, for example, by a modeler in an interview: ‘I hesitated whether to relate lecturer to course or to course offering. The last rule [no. 7, Table 2] guided me to relate lecturer to course, which is the whole [whose part is course offering]’. Note that the modeler was not able to indicate a mutual property (e.g., lecture hours) related to the fact that a lecturer is assigned to a course offering rather than to a course.

## Decision-affecting factors

The results of the qualitative analysis indicate two main groups of factors that affect modeling decisions: factors inherent in the human modeler and factors embedded in the modeled domain.

The factors inherent in the human modeler mainly concern the modeler’s experience and knowledge. Prior experience may lead to conditioning and learned behavior. In particular, as elaborated in the analysis above, some of the model variations were due to implicitly applying design considerations. A clear example is the use of abstract classes, as discussed above. Another example was observed in a class discussion, where some students suggested to model a salary as a class with a method for computing itself. Such argument is clearly a design consideration, since in reality a salary cannot compute itself.

![](/api/attachments/2SH8C4KJ/fulltext/images/b00b387b1115dc0a87704a88a6ce60f79c2be5a096cf5ba3797ea360e459dd92.jpg)  
Figure 6 Association of a third party with part or with whole – an example.

The inherent knowledge that was found to influence model variations is prior domain knowledge. We found that when dealing with a familiar domain, modelers tend to rely on assumptions based on their prior knowledge in addition to the problem description. Since such assumptions are taken individually, they result in an increase of certain model variations. Our findings indicate that existing knowledge affects modeling decisions. The students dealt with two different domains, one very familiar to all of them (university), the other (transportation) was remotely known to them. While in the latter case the students leaned only on the textual description given to them, in the university task they made many additional assumptions, derived from their personal experience, which were reflected in their models. For example, in one case the course offering class was modeled as an association between a course and a lecturer. When asked, the modeler explained that each course offering was taught by a different lecturer, hence can represent this association. To the question ‘what if the same lecturer teaches two course offerings?’, he replied: ‘I never saw such a case here [at our university]’. Another example is a documented modeling dilemma: ‘I was hesitating whether to include in the university model classes such as faculty and exercise groups’. These were known to the student, although they were not mentioned in the task description.

Note that variations of this kind reflect differences in the perception and interpretation of the domain by individuals, as opposed to variations that reflect differences in mapping a uniformly perceived domain to modeling constructs. While the latter can be reduced by the application of modeling rules, the former are not affected by rules (Evermann, 2005).

The domain knowledge and perception, although related to the domain, is a property possessed by the modeler. In contrast, there are specific characteristics embedded in the domain independently of the modeler, which affect the variations observed. In particular, the specific properties of the domain discussed below seem to contribute to this effect. Note that it is very hard to isolate the effect of each such property. In our analysis we rely on qualitative evidence, which indicate the existence of such effects, without attempting to quantify them.

Tangibility: In general, the more-tangible domain (transportation) incurred fewer variations than the lesstangible one (university). Two main differences in specific variation types were observed between the two tasks. First, confusion between a class and an association occurred mainly in the university task, which is less tangible than the transportation task. From the cases where classes were modeled as association classes, 15 were in the university task and only one in the transportation task. This confusion was fully resolved by applying the rules. Second, difficulty in distinguishing between aggregation and association relations was found in both domains. However, while no quantitative evidence shows a difference between the domains in the magnitude of this confusion, the qualitative data indicates that this decision took a more complicated process and was characterized by more dilemmas in the less-tangible domain. For example, 58% of the written dilemmas in the university task related to how to associate student or lecturer to course and course offering, which are intangible things, while no similar dilemmas were reported in the transportation task. This was also supported in the interviews. One of the students, when asked to explain his considerations while deciding on the types of relations between entities explained: ‘Actually, it depends. When physical things are concerned it’s easy. I can ‘‘see’’ it. For example – a room is a part of a building. However, when abstract concepts are involved, I sometimes find it [the aggregation relations] hard to ‘‘see’’’.

Properties of part–whole relations: Our findings indicate that the identification of part–whole relations (modeled as both aggregation and composition) varied greatly with respect to different specific relations. The theoretical literature identifies a number of properties that characterize part–whole relations. In fact, according to Saksena et al. (1998) and Barbier et al. (2003), part–whole is a general name for a family of relations whose semantics is not identical, and is differentiated by the values of these properties. Examples of such properties are life-time binding between the whole and the part, shareability of parts, seperability of parts from the whole, existential dependency of the part on the whole, and behavior control of the whole over the parts.

Considering the part–whole relations in our tasks, we find linkage between the properties discussed in the theoretical literature and the identification level of the relations as part–whole. The part–whole relation that was most easily identified by the students was Course–Course Offering, while the one that was most difficult to identify was Course Offering–Student. Comparing these two examples, we find that the values of some of the abovementioned properties are opposite in these two cases. Two properties that are sometimes considered as linked (Barbier et al., 2003) are seperability of the part from the whole and existential dependency of the part on the whole. In the relation of Course–Course Offering (most identified one), there is no seperability and there is an existential dependency of the part on the whole. These values are different from the values in all the other part– whole relations in our tasks. On the other hand, the shareability property, which relates to the possibility of a part being shared by more than one whole, exists positively only in the Course Offering–Student relation (the least identified one). The life-time binding property, referring to the relationship between the lifetimes of the part and the whole, had a variety of values in the different relations of the tasks. In the case of the Course– Course Offering relation, the lifetime of the part is contained within the lifetime of the whole, whereas in the case of the Course Offering–Student relation the lifetime of the whole is contained within the lifetime of the part. In both cases, the time of the relation between the part and the whole equals to the life of the shorterlived entity. Addressing relations that had other values of the life-time binding property, easier identification of the relation was observed when the birth of the part took place after the birth of the whole. Of course, the case where the lifetime of the parts is contained in the lifetime of the whole is a special case of this and seems to be most easily identified one.

Looking at these four properties, it seems that the greater the dependency of the part on the whole, the easier it is to identify the relation. The applied rules do not address the properties discussed here. In general, as presented above, the rules significantly improved the identification of part–whole relations. This improvement was similar in all the relevant relations, regardless of the values of their properties.

Our findings regarding the decision-affecting factors and their relationship with model variations are summarized in Figure 7. We found that the identified modeler’s properties may affect variations that relate either to mapping decisions (conditioning and learned behavior) or to the perception of the domain (domain knowledge). Each of the identified domain properties, namely tangibility and part–whole properties, may affect variations of both kinds. For example, an intangible domain is more likely to be perceived differently by different modelers than a tangible one. In addition, mapping decisions might be less conclusive with respect to an intangible domain as compared to a tangible one. As mentioned above, modeling rules may reduce mapping-related variations, but not perception-related ones.

![](/api/attachments/2SH8C4KJ/fulltext/images/b2a6a9c3e8382a839a15df372cd6e25c5048eae8cb36256c92dde8b360508f7b.jpg)  
Figure 7 Decision-affecting factors.

## Discussion

The findings of the study provide insights into the nature of model variations in light of the use of ontology-based rules and beyond it. In addition to the modeling process that was manipulated in this study (via the rules), two main groups of factors that affect the modeling decision making, as reflected in the variations, were identified. Note, that these findings relate to the empirical study reported here, whose design was aimed at addressing the modeling process alone, hence other sources of variations (e.g., modeling grammar) were controlled and are not reflected here.

The overall effect of the rules was not as significant as we had expected. It seems that our intervention in the modeling process was not always sufficient for overcoming the variety of factors that lead to variations. Some of the rules, which were easier to apply, indeed had the expected effect. Others that either required a more complicated decision process (e.g., identifying emergent properties) or a certain transformation in the modeling approach (e.g., avoiding the use of abstract classes) had only a minor effect, if any. One of our conclusions from these findings is that providing the modelers with a set of technical rules is not enough for achieving the desired change in the modeling process. This requires that the modelers will adopt an ontological way of thinking, which perceives and interprets the world in ontological concepts.

The rules applied in the study form a subset of the ontology-based rules proposed by Evermann & Wand (2001, 2004). This subset was defined based on previously identified variation types, and in order to simplify the application of the rules. Nevertheless, the study results show difficulties experienced even in the application of this subset of rules. Although a larger set of rules may seem more difficult to apply, one may argue that relying on a partial set of rules essentially makes their application, a technique rather than a sound approach and renders an ontological interpretation of the world impossible. The rule base of Evermann and Wand also includes rules that relate to the combination of class diagrams and other views, such as state–machine diagram (Evermann & Wand, 2005). Here we used only rules that address class diagrams alone, and it is possible that looking at a broader context might affect the decision making.

Additional limitations of the study include the research population, which is last-year undergraduate students, whose knowledge and experience in conceptual modeling is limited. On the other hand, although limited, this knowledge and experience is relatively uniform among the subjects, which is a strength that motivated this population choice when designing the research setting.

Another limitation is the construction of models in ‘lab conditions’, based on a textual description of the domain, as opposed to real-life situations, where domain knowledge is extracted through interaction with users and domain experts. Relying on a textual description only necessarily increases the role of individual interpretation. This potential problem was taken into account when formulating the tasks and much effort was made to phrase them in a detailed and unambiguous manner.

Finally, we do not consider our findings regarding decisionaffecting factors and their effect on variations to be a complete list of such factors. Rather, the findings indicate the existence of the reported factors. Further research is needed to establish a complete model of the decisionaffecting factors that contribute to model variations.

## Conclusion

Model variations are a common and well-known phenomenon, which has not been extensively investigated so far. The importance of analyzing and understanding these variations is in the insights gained into the modeling process and the decisions involved. Different modeling decisions may result in variations; hence, these reflect vagueness in the modeling process. Many research efforts have been devoted to theoretical analysis of modeling constructs in order to obtain better-defined semantics and reduce the vagueness in their definitions. However, the success of these theories in guiding the modeling process has not been empirically tested. This paper, to the best of our knowledge, is a first attempt to rely on model variations for empirically investigating the usefulness of theory-based modeling guidance, while achieving an in-depth understanding of the decision making involved in the process and the factors that affect it. Reducing model variations is important for purposes such as communication and model matching that serves for analysis or reuse. It can only be achieved by understanding the sources of variations, such as vagueness in the modeling process.

The paper reports an empirical study, whose aim was to examine the effect of ontology-based rules on variations in UML Class Diagram conceptual models, and to explore factors that affect the relevant decision making. The findings indicate that the modeling process is complicated and includes many decisions that are affected by a variety of factors, hence should be guided both technically and conceptually. While a technical approach, such as applying structured rules, provides some assistance, we believe that further improvement may be achieved by attaching semantics to the modeling process.

The findings also provide a detailed distinction of which decisions are more difficult to make even with the guidance of the rules, and identify factors that contribute to these difficulties. As a result, it is possible to indicate where a better methodological support is required.

Future research may take several directions. One direction is toward achieving a better understanding of the model variations phenomenon, addressing specific relevant factors that were identified here, such as the tangibility of the domain. Understanding the effect of such aspects may lead to a better-targeted guidance

## About the Authors

Pnina Soffer is a lecturer in the Department of Management Information Systems in Haifa University in Israel. She has a B.Sc. and M.Sc. in Industrial Engineering and a Ph.D. in Industrial Engineering and Information Systems from the Technion, Israel Institute of Technology. She has industrial experience in analysis and design of industrial and organizational information systems and in implementation of ERP systems in organizations. Her general research interests are requirements engineering, off-theshelf information systems, and business process modeling and design. Specifically, her research deals with requirements modeling, goal analysis, requirements for process-supportive information systems, ERP systems requirements, alignment, and customization, and the

## References

throughout the modeling process. Another direction deals with the application of ontology-based rules and with how these can be conveyed to modelers. We intend to further experiment applying different sets of rules. The rules will be applied after an educational period where the modelers will be able to adopt an ontological way of thinking. This way the rules will be perceived as semantically meaningful rather than as a modeling technique. As well, empirical investigation of variations may address other theoretical frameworks besides the one investigated here. It can serve for comparison and evaluation of such frameworks in terms of their usefulness in guiding the modeling process.

AGERFALK PJ and ERIKSSON O (2004) Action-oriented conceptual modeling. European Journal of Information Systems 13(1), 80–92.

BARBIER F, HENDRESON-SELLERS B, PARC-LACAYRELLE A and BRUEL JM (2003) Formalization of the whole–part relationship in the unified modeling language. IEEE Transactions on Software Engineering 29(5), 459–470.

BODART F, PATEL A, SIM M and WEBER R (2001) Should optional properties be used in conceptual modelling? A theory and three empirical tests. Information Systems Research 12(4), 384–405.

BUNGE M (1977) Treatise on Basic Philosophy. Ontology I: The Furniture of the World. Reidel, Boston.

BUNGE M (1979) Treatise on Basic Philosophy: Vol. 4, Ontology II: A World of Systems. Reidel, Boston.

BURTON-JONES A and MESO P (2002) How good are these UML diagrams : an empirical test of the Wand and Weber good decomposition model. In Proceedings of the 23rd International Conference on Information Systems (APPLEGATE L, GALLIERS R and DEGROSS JI, Eds), pp 101–114, Barcelona, Spain.

EVERMANN J (2005) Thinking ontologically: conceptual vs. design models in UML. In Business Systems Analysis with Ontologies (GREEN P and ROSEMANN M, Eds), pp 82–104, Idea Group, Hershey.

EVERMANN J and WAND Y (2001) Towards ontologically based semantics for UML constructs. In Proceedings of ER 2001, 22nd International Conference on Conceptual Modeling (LNCS 2224). (KUNII HS, JAJODIA S and SOLVBERG A, Eds), pp 354–367, Springer-Verlag, Berlin.

development of a formal ontology-based process modeling approach.

Irit Hadar is a lecturer in the Department of Management Information Systems at the University of Haifa. Her research focuses on cognitive processes of software development, with emphasis on object technology; the role and influence of visual models in requirement engineering and software design; and human aspects – organizational, management, social, and cognitive – and their influence on software quality. She has her Ph.D. from the Department of Education in Technology and Science of the Technion – Israel Institute of Technology. Both her Master and Bachelor degrees are from the Faculty of Industrial Engineering and Management of the Technion.

EVERMANN J and WAND Y (2004) Ontology based object-oriented domain modeling: fundamental concepts. Requirements Engineering 10(2), 146–160.

EVERMANN J and WAND Y (2005) Toward formalizing domain modeling semantics in language syntax. IEEE Transactions on Software Engineering 31(1), 21–37.

GALLIERS R (1991) Choosing appropriate information systems research approaches: a revised taxonomy. In Information System Research: Issues, Methods, and Practical Guidelines (GALLIERS R, Ed), pp 144–162, Blackwell, Oxford, UK.

GUIZZARDI G, HERRE H and WAGNER G (2002) On the general ontological foundations of conceptual models. In Conceptual Modeling – ER 2002, 21st International Conference on Conceptual Modeling (LNCS 2505), (SPCCAPIETRA S, MARCH TS and KAMBYASHI Y, Eds), pp 65–78, Springer-Verlag, Berlin.

GUIZZARDI G, WAGNER G, GUARINO N and VAN SINDEREN M (2004) An ontologically well-founded profile for UML conceptual models. In Advanced Information Systems Engineering, 16th International Conference, CAiSE 2004 (LNCS 3084) pp 112–126, Springer-Verlag, Berlin.

HADAR I and SOFFER P (2006) Variations in conceptual modeling: classification and ontological analysis. Journal of the Association of Information Systems 7(8), 568–592.

KAPLAN B and DUCHON D (1988) Combining qualitative and quantitative methods in information systems research: a case study. Management Information Systems Quarterly 12(4), 571–586.

LANDRY M and BANVILLE C (1992) A disciplined methodological pluralism for MIS research. Accounting, Management and Information Technology 2(2), 77–97.

LEE A (1991) Integrating positivist and interpretivist approaches to organizational research. Organizational Science 2, 342–365.

LU S and PARSONS J (2005) Enforcing ontological rules in UML-based conceptual modeling: principles and implementation. In Proceedings of CAiSE’05 Workshops 1, pp 451–462, Porto, Portugal.

MINGERS J (2001) Combining IS research methods: towards a pluralist methodology. Information Systems Research 12(3), 240–259.

OPDAHL A, HENDERSON-SELLERS B and BARBIER F (2001) Ontological analysis of whole–part relationships in OO models. Information and Software Technology 43, 387–399.

PARSONS J (1996) An information model based on classification theory. Management Science 42(10), 1437–1453.

PARSONS J and COLE L (2004) An experimental examination of property precedence in conceptual modeling. In Proceedings of the First Asia-Pacific Conference on Conceptual Modeling, pp 101–110, Dunedine, New Zealand.

POELS G, GAILLY F, MAES A and PAEMELEIRE R (2005) Object class or association class? Testing the effect on cardinality interpretation. In Perspectives in Conceptual Modeling, ER 2005 Workshops (LNCS 3770), (AKOKA J, LIDDLE SW, SONG I-Y, BERTOLOTTO M, COMYN-WATTIAU I, CHERFI SS, VAN DEN HEUVEL WJ, THALHEIM B, KOLP M, BRECIANI P, TRUJILLO J, KOP C and MAYR HC, Eds), pp 33–42, Springer-Verlag, Berlin.

SAKSENA M, FRANCE RB and LARRONDO-PETRIE MM (1998) A characterization of aggregation. Proceedings of Fifth International Conference on Object Oriented Information Systems (OOIS’98), pp 11–19.

SCHUETTE R and ROTTHOWE T (1998) The guidelines of modeling – an approach to enhance the quality in information systems. Proceedings of ER’98 (LNCS 1507) (LING TW, RAM S and LEE ML, Eds), pp 240–254, Springer-Verlag, Berlin.

SOFFER P and HADAR I (2003) Reusability of conceptual models: The problem of model variations. EMMSAD’03, Proceedings of the Eighth CAiSE/IFIP8.1 International Workshop on Evaluation of Modeling Methods in Systems Analysis and Design (on CD).

STRAUSS A and CORBIN J (1990) Basics of Qualitative Research; Grounded Theory Procedures and Techniques. Sage, Newbury Park.

TOPI H and RAMESH V (2002) Human factors research on data modeling: a review of prior research, an extended framework and future research directions. Journal of Database Management 13(2), 3–15.

WAND Y and WEBER R (1993) On the ontological expressiveness of information systems analysis and design grammars. Journal of Information Systems 3, 217–237.

WAND Y and WEBER R (2002) Research commentary: information systems and conceptual modeling – a research agenda. Information Systems Research 13(4), 363–378.
