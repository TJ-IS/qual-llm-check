---
otero_id: 5734
otero_key: "CBHBEH6P"
title: "Comprehensive rule-based compliance checking and risk management with process mining"
authors: "Filip Caron; Jan Vanthienen; Bart Baesens"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comprehensive rule-based compliance checking and risk management with process mining

Filip Caron <sup>a,</sup>⁎, Jan Vanthienen <sup>a</sup>, Bart Baesens <sup>a,b,c</sup>

<sup>a</sup> Department of Decision Sciences and Information Management, KU Leuven, Naamsestraat 69, B-3000 Leuven, Belgium

<sup>b</sup> Vlerick Leuven Gent Management School, Vlamingenstraat 38, B-3000 Leuven, Belgium

<sup>c</sup> School of Management, University of Southampton, Highfield Southampton, SO17 1BJ, United Kingdom

## a r t i c l e i n f o

Article history: Received 11 October 2011 Received in revised form 16 August 2012 Accepted 4 December 2012 Available online 21 December 2012

Keywords: Business rules Compliance checking Risk management Process mining Process-aware information systems

## a b s t r a c t

Process mining researchers have primarily focused on developing and improving process discovery techniques, while attention for the applicability of process mining has been below par. As a result, there only exists a partial <sup>fi</sup>t with the traditional requirements for compliance checking and risk management. This paper proposes a comprehensive rule-based process mining approach for a timely investigation of a complete set of enriched process event data. Additionally, the contribution elaborates a two-dimensional business rule taxonomy that serves as a source of business rules for the comprehensive rule-based compliance checking approach. Finally, the study provides a formal grounding for and an evaluation of the comprehensive rule-based compliance checking approach.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

While the value creation abilities of an organization are increasingly determined by the <sup>fl</sup>exibility of their information systems and business processes, this <sup>fl</sup>exibility may also pose signi<sup>fi</sup>cant risks that could have an enormous negative impact on achieving the corporate objectives (such as regulatory compliance and pro<sup>fi</sup>tability) [37]. Consequently, the organization's management performs a risk assessment and implements appropriate risk responses, such as (internal) control procedures for authorization rules and approval activities. Shareholders and other stakeholders of the organizations are likely to demand an independent assessment of the effectiveness of these risk responses, which is typically performed by auditors. Both risk and control effectiveness assessments make use of (similar) compliance checking techniques.

Process mining is a promising new research area that focuses on the development of innovative techniques for analyzing event logs of process-aware information systems [43,44] that execute and manage business processes. The resulting event logs contain an untapped reservoir of detailed and structured information on the business operations, for example time indicators and originator identi<sup>fi</sup>ers for the performed activities.

While (audit) compliance checking has been suggested as a potential application for multiple process mining techniques [23,34,40], there does not exist a precise <sup>fi</sup>t with the speci<sup>fi</sup>c needs of contemporary risk and compliance activities. This paper contributes to the applied process mining research by:

• Proposing comprehensive rule-based compliance checking as a process mining technique for a timely assessment of the complete set of enriched process data.

• Introducing a two-dimensional business rule taxonomy, which serves as a source of con<sup>fi</sup>gurable rule patterns used for specifying (internal) controls and other risk management activities.

• Providing both a formal grounding for and concrete applications of the comprehensive rule-based compliance checking approach.

The outline of the paper is as follows: Section 2 provides an overview of compliance checking with process mining and describes the partial <sup>fi</sup>t. Section 3 discusses the details of the comprehensive rule-based compliance checking approach as well as its formal grounding, followed by the introduction of the running example (Section 4) and the elaboration of the business rule taxonomy (Section 5). Section 6 discusses the potential applications, opportunities, assumptions and challenges of the proposed compliance checking approach. The <sup>fi</sup>nal section concludes the paper and presents an outlook for future research in this area.

## 2. Process mining

Process mining addresses the problem that most organizations, and their stakeholders, have very limited information about what is actually happening in the business processes [17,44,52]. Insights into the real behavior are acquired through analysis of the structured information contained in information systems' event logs. Process mining has received a vast amount of research attention resulting in a plethora of techniques, including process discovery techniques [4,9,16,20,45,53], techniques for the analysis of event log data [3,41,42,46], techniques for trace classi<sup>fi</sup>cations [13,38], process metrics [11,34] and applied research [31,47]. Fig. 1 represents the process mining architecture.

## 2.1. Traditional compliance checking with process mining

Three broad sets of techniques are of main interest for compliance checking: process discovery and visualization, conformance checking and delta analysis, and logic-based property veri<sup>fi</sup>cation. Table 1 provides per technique a brief description and an overview the most in<sup>fl</sup>uential contributions for the techniques.

While the <sup>fi</sup>rst two approaches promote the analysis of the process as a whole, the last one can be used to focus on speci<sup>fi</sup>c questions.

## 2.2. Partial fit between compliance checking and existing process mining techniques

Existing process mining techniques are often not fully adapted to the contemporary compliance checking requirements. Process mining researchers have primarily focused on improving techniques for control-<sup>fl</sup>ow and to a far lesser extent for social/organizational analysis. Besides the obvious requirement to be able to analyze and perform controls on the additional data in the event logs, this research focus results in other important restrictions. Firstly, conformance metrics might provide only a <sup>fi</sup>rst impression of the overall conformance with the designed model. An in-depth evaluation of the problematic process parts, where the deviation from the designed model is signi<sup>fi</sup>cant, will be required. Additionally, we can question the correctness of the designed business processes. Procedural business process models often contain control-<sup>fl</sup>ow dependencies that are not dictated by internal or external directives, known as the overspeci<sup>fi</sup>cation of the process models [29]. Consequently, process deviations affecting the conformance measures, do not necessarily violate any internal or external directive. Moreover, de<sup>fi</sup>ning all possible execution paths to deal with natural variations in a business environment can be challenging.

Due to the assumption that an event log will not contain all possible behavior, process discovery and visualization techniques have to balance model precision and generality. However, in a risk management and compliance checking setting generality is not important.

Table 1  
Overview of traditional process mining based compliance checking techniques.

<table><tr><td>Technique type</td><td>Technique description</td><td>References</td></tr><tr><td>Process discovery and visualization</td><td>Summarize a specific aspect of the real business process dynamics in one visual. These aspects can be for example the control flow or a social network.</td><td>[9,36,45,48,49,53]</td></tr><tr><td>Conformance checking and delta analysis</td><td>Detect inconsistencies between a prescriptive model and its corresponding real-life process. Conformance checking uses the event log as a comparison base, while delta analysis uses a derived process model.</td><td>[2,5,19,34,35]</td></tr><tr><td>Logic-based property verification</td><td>Analyze specific process properties of the individual process instances. Examples of such process properties are the activity preconditions and the segregation of duties.</td><td>[8,10,26,46]</td></tr></table>

It might actually result in a cover up of (infrequent) harmful process deviations.

Similarly, the logic-based property veri<sup>fi</sup>cation research has predominantly focussed on activity ordering questions. However, business users require the ability to perform controls from a broader spectrum of common types [1].

## 3. Comprehensive rule-based compliance checking with process mining

In this section, we propose the comprehensive rule-based compliance checking approach. Subsection 3.1 presents the architecture of the pro posed approach, followed by the presentation of a business rule taxonomy in Section 3.2 and the formal speci<sup>fi</sup>cations in Section 3.3subsection 3.

## 3.1. Comprehensive rule-based compliance checking architecture

The architecture supporting the proposed comprehensive rule-based compliance checking approach consists of three main components: ‘business provenance’, ‘regulation, policies and other directives’ and ‘techniques’ (Fig. 2).

Business provenance deals with the systematic and reliant recording of business events and (evolutions of) other business artifacts. Consequently, it keeps track of both the current status and the history. As business processes are becoming heavily supported by process-aware information systems, the event logs of these information systems become a valuable source of information on the business operations. This process centric information can be further enriched with information from other data sources, such as the customer relationship management systems with the client base and the human resource data.

![](/api/attachments/CBHBEH6P/fulltext/images/c98fe72b54109f21d0a3cd89c26d9458a85dc8ab920fde2da4a374746964fe6d.jpg)  
Fig. 1. Process mining architecture with traditional compliance checking approaches.

![](/api/attachments/CBHBEH6P/fulltext/images/48e9e97dee45fc8b37f997734fea95de240147832bdf859958804b04471db40f.jpg)  
Fig. 2. Comprehensive rule-based compliance checking architecture.

Secondly, legislation, policies and other directives all impose different restrictions on the business operations of an organization. A multitude of sources exist: government, trade associations and their standards or the organization itself.

The third architectural component covers the techniques that are used in comprehensive rule-based compliance checking: con<sup>fi</sup>gurable rule patterns and the resulting rule-based controls. The directives dictate control objectives that are translated into one or more speci<sup>fi</sup>c controls. These controls often map neatly on generic rule patterns, for example segregation of duties patterns, activity existence patterns and arithmetic derivation patterns. Con<sup>fi</sup>guration to the speci<sup>fi</sup>c organizational setting is, however, required. These patterns will be discussed in Section 5. The rule-based controls are afterwards checked against the enriched process data.

## 3.2. Proposing a business rule taxonomy for process mining

A two-dimensional rule taxonomy complements the compliance checking approach by providing a clear structure for classifying the generic rule patterns. Generic rule patterns will be classi<sup>fi</sup>ed according to their process mining perspective and their rule restriction focus. Fig. 3 provides an overview of the two dimensional taxonomy and the subcategories of each dimension

## 3.2.1. Process mining perspective dimension

The <sup>fi</sup>rst dimension of the taxonomy refers to the process mining perspective (PMP) that is used in the business rule. Four different perspectives on business process modeling were introduced in [7] and can also be used to classify the business rule types in this context:

• Functional process perspective (PMP1) that deals with the process elements (such as activities, process events and originators) that are being performed/occur in a process instance, as well as the relevant process artifacts linked to these process elements. An invoice linked to a pay activity is an example of such a process artifact.

Rule Restriction Focus (RRF) Dimension

<table><tr><td colspan="2"></td><td>Cardinality-Based Rules</td><td>Coexistence Rules</td><td>Dynamic Data-Driven Rules</td><td>Relative Time Rules</td><td>Static Property Rules</td></tr><tr><td rowspan="4">Process Mining Perspectives (PMP)Dimension</td><td>Functional Process Perspective</td><td>Activity Cardinality</td><td>Activity Coexistence Event-Activity Coexistence</td><td>Data-Driven Existence</td><td>Time-Oriented Activity Existence</td><td>Event-Artifact Coexistence</td></tr><tr><td>Control-Flow Process Perspective</td><td></td><td>Non-Overlapping Activities Activity Order</td><td>Data-Driven Activity Precondition</td><td>Time-Driven Control-Flow Rules</td><td>Absolute Time</td></tr><tr><td>Organizational Process Perspective</td><td>Originator Cardinality</td><td>Segregation of Duties Binding of Duties Temporal Engagement Rules</td><td>Exogenous Authorization Originator Attribute Rules</td><td>Temporal Deontic Rules</td><td>Static Authorization Required Originator Attribute Delegation Rule</td></tr><tr><td>Data Process Perspective</td><td>Event Data Cardinality</td><td>Event Data Coexistence</td><td>Derived Event Data Rule Event Data Comparison Rule</td><td>Dynamic Integrity</td><td>Event Data Value Rule Event Data Format Rule</td></tr></table>

Fig. 3. Structure of the business rule taxonomy for process mining (section 5.x further elaborates on row x, while the individual cells are further developed in different rows of Tables 4-7)

• Control-<sup>fl</sup>ow process perspective (PMP2) that covers the process behavior in terms of when process elements can be performed/occur in a process instance, including ordering relations, complex decision conditions and entry/exit criteria.

• Organizational process perspective (PMP3) that focuses on the organization behind the business process, which agent performs the different process elements in a process instance taking into account factors such as timing and environmental conditions.

• Data process perspective (also known as informational perspective) (PMP4) that represents the informational elements that are used, produced or manipulated during the process, as well as relationships among them. These informational elements can be either event data or case data.

These process mining perspectives can be regrouped by their data requirements for event logs. For business rules from the functional and control-<sup>fl</sup>ow perspective it suf<sup>fi</sup>ces that the event log contains timestamps, event and activity identi<sup>fi</sup>ers. The organizational and data perspective based business rules require additional event data, such as an originator identi<sup>fi</sup>er or an amount.

## 3.2.2. Rule restriction focus dimension

Secondly business rules can be classi<sup>fi</sup>ed along their main rule restriction focus (RRF). Five new and distinctive business rule restriction focuses were identi<sup>fi</sup>ed:

• Cardinality-based rules (RRF1) are business rules that restrict the number of allowed instances of a speci<sup>fi</sup>c process element type in a speci<sup>fi</sup>c process instance.

• Coexistence rules (RRF2) can be de<sup>fi</sup>ned as business rules that restrict the coexistence of process elements of different types over the execution of a speci<sup>fi</sup>c process instance.

• Dynamic data-driven rules (RRF3) specify the in<sup>fl</sup>uence of speci<sup>fi</sup>c data elements and their value on the occurrence of process elements in a speci<sup>fi</sup>c process instance.

• Relative time rules (RRF4) focus on specifying a time restriction on process elements relative to certain points in a process execution, for example the start of a process or the completion of a speci<sup>fi</sup>c activity.

• Static property rules (RRF5) deal with specifying a speci<sup>fi</sup>c property for a particular type of process element at a prede<sup>fi</sup>ned process state.

While the <sup>fi</sup>rst four rule restriction focuses are history-based or future constraining and thus deal with dynamic properties, the last focus deals with static properties that belong to a speci<sup>fi</sup>c process state. Both dimensions cover the wide spectrum of controls that can be implemented and evaluated with process mining techniques.

## 3.3. Formal specification of rule patterns

An unambiguous interpretation of the business rule patterns, is crucial for compliance checking. In this subsection we indicate how the patterns can be formally speci<sup>fi</sup>ed. The use of linear temporal logic (LTL, speci<sup>fi</sup>ed in [32]) is more natural for dynamic properties, whereas <sup>fi</sup>rst order logic is more suited for static properties. An additional advantage of formal speci<sup>fi</sup>cations is the useability of existing model checking approaches for the identi<sup>fi</sup>cation of con<sup>fl</sup>icting business rules and consequently con<sup>fl</sup>icting controls.

## 3.3.1. Preliminaries: specifying business processes, business events and audit trails

This subsection provides the formal de<sup>fi</sup>nition of the concepts and their de<sup>fi</sup>ning characteristics that will be used for the speci<sup>fi</sup>cation of the rule patterns.

De<sup>fi</sup>nition 1. Business processes. A business process can be formally represented by a process schema S, which is de<sup>fi</sup>ned by the tuple ( , ℛ, , , δ, π, ℬℛ) where

• The basic constructs include: $\mathcal { A } = \{ a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . , a _ { n } \}$ that denotes the <sup>fi</sup>- nite set of all activities, $\mathcal { R } { = } \{ r _ { 1 } , r _ { 2 } , r _ { 3 } , { \ldots } , r _ { n } \}$ that is used to refer the <sup>fi</sup>- nite set of roles, $\mathcal { O } = \{ o _ { 1 } , o _ { 2 } , o _ { 3 } , . . . , o _ { n } \}$ that represents the <sup>fi</sup>nite set of originators and $\mathcal { P } { = } \{ p _ { 1 } , p _ { 2 } , p _ { 3 } , . . . , p _ { n } \}$ that stands for the <sup>fi</sup>nite set of (all other) properties.

• δ represents the property-type assignment function, $\delta : { \mathcal { P } } \longrightarrow \Delta . \ A$ possible set of generally relevant property types is de<sup>fi</sup>ned as $\Delta = \{ T i m e ,$ InstanceIdentifier, Activity, EventType, Originator, Role, String, Rational, Boolean}.

• π is the property-set function that speci<sup>fi</sup>es the set of properties that is applicable for each activity, $\pi : A  2 \mathcal { P } .$

• ℬℛ the set of business rules specifying the relevant relations and constraints for a business process, such as precedence relations and required roles). These business rules may be either implicit or explicit. A precondition in a Petri net is an example of an implicit rule, while a precondition in a declarative ConDec model would be explicit [28].

During the execution of a business process a multitude of business events can be observed.

## De<sup>fi</sup>nition 2. Business event

A business event is a relevant occurrence of something that happens at a speci<sup>fi</sup>c time and is of special interest to the business. For example, the start of a speci<sup>fi</sup>c activity is a business event. An event is speci<sup>fi</sup>ed by the values of the related relevant data properties. As such an event can be denoted as $e : { \mathcal { P } } \mathrm { - } \nu$ with $e { \in } { \mathcal { E } } { = } \{ e _ { 1 } , e _ { 2 } , e _ { 3 } , . . . , e _ { n } \}$ the set of all events and the set of all possible values for the properties. The partial function assigns a value to the properties identi<sup>fi</sup>ed by the property-set function.

Contemporary information systems store a multitude of information about these events in a structured way. Therefore, the resulting event logs (denoted by $\alpha , \beta , \mathrm { e t c . } )$ precisely describes the audit trails of all process instances, within a certain timeframe.

## De<sup>fi</sup>nition 3. Audit trail

An audit trail $\sigma { \in } { \mathcal { E } } ^ { * }$ is an event sequence, where $\mathcal { E } ^ { * }$ represents all traces composed of one or more events of ℰ. Additional properties:

$\sigma = \langle e _ { 1 } , e _ { 2 } , . . . , e _ { n } \rangle$ denotes an audit trail with |σ|=n the length of the trail and $e _ { i } { = } { \sigma } [ i ]$ (with $1 \leq i \leq n )$ the i-th event in the audit trail.

$\sigma ^ { i \cdots }$ represents the suf<sup>fi</sup>x of σ starting at σ[i], consequently $\sigma ^ { i \sim } =$ $\langle e _ { i } , e _ { i + 1 } , . . . , e _ { n } \rangle$

Each event log record contains the information of a speci<sup>fi</sup>c event, including a speci<sup>fi</sup>c event identi<sup>fi</sup>er $\mathbf { \delta } \cdot \mathbf { \delta } \iota = \{ i _ { 1 } , i _ { 2 } , i _ { 3 } , . . . , i _ { n } \}$ . The event identi-<sup>fi</sup>ers can be grouped by the case or process instance identi<sup>fi</sup>er (X) using the following subset de<sup>fi</sup>nition $\iota _ { X = y } : \{ e \in \mathcal { E } | X = y \}$

As the exact structure of a speci<sup>fi</sup>c event log is not known in advance, this contribution will use a generic and <sup>fl</sup>exible de<sup>fi</sup>nition of the function that is used to query for events. For speci<sup>fi</sup>c business rules the function notation will contain all the relevant event properties for that function. Thus for activity order rules, for example, it should suf<sup>fi</sup>ce to provide the activity (a ) and event type (t ) this results in the notation $\alpha ( a _ { i } , t _ { j } )$ . However, when a speci<sup>fi</sup>c role $\left( r _ { k } \right)$ is required the function notation will additionally include at least this role, consequently $\alpha ( a _ { i } , t _ { j } , r _ { k } )$

The elements de<sup>fi</sup>ned in these preliminaries will be used for the speci<sup>fi</sup>cation of three types of rule patterns: the dynamic, the static and the composed rule patterns. Table 2 provides a general overview.

## 3.3.2. Specifying static process aspects in first order logic

In the context of static property rules there is only a need to evaluate one speci<sup>fi</sup>c process state or event. Since the multi-state aspect is not crucial here, the semantics of the <sup>fi</sup>rst order logic expression language should suf<sup>fi</sup>ce. Examples are:

Table 2  
Overview of the rule-pattern types with preferred language and example.

<table><tr><td></td><td>Description</td><td>Language</td><td>Example</td></tr><tr><td>Static</td><td>Rule patterns for an evaluation of individual states (events)</td><td>First order logic</td><td>The value of event data type  $p_1$  is not equal to the value of event data type  $p_2$  with reference to an event of type  $e_1$  for an activity of type  $a_1$  (irreflexive event data rule) $\neg(\exists i \in \iota: (\alpha(i,a_1,t_c,p_1,p_2) \land (p_1=p_2)))$ </td></tr><tr><td>Dynamic</td><td>Rule patterns for an analysis over multiple states (events) of a single process instance</td><td>Linear temporal logic</td><td>A person P must not perform both an activity of type  $a_1$  and an activity of type  $a_2$  (dynamic segregation of duties) $\Diamond(a_1,t_c,P) \Rightarrow \neg\Diamond(a_2,t_c,P)$ </td></tr><tr><td>Composed</td><td>Rule patterns composed of multiple atomic rule patterns</td><td>Logical connectors for patterns</td><td>An activity of type  $a_1$  must be performed before an activity of type  $a_2$  can be performed AND An activity of type  $a_3$  must be performed before an activity of type  $a_2$  can be performed $(\neg(a_2,t_c)W(a_1,t_c)) \land (\neg(a_2,t_c)W(a_3,t_c))$ </td></tr></table>

• Prohibited role-based allocation rule: Activity a1 must not be performed by an originator of role $\Gamma _ { 1 }$

$$
\neg (\exists i \in \iota : \alpha (i, a _ {1}, t _ {c}, r _ {1}))
$$

• Absolute time rule: Activity $a _ { 1 }$ must be performed before $T _ { 0 }$ (with timestamp=τ)

$$
\neg (\exists i \in \iota : (\alpha (i, a _ {1}, t _ {c}, \tau) \land (\tau > T _ {0})))
$$

3.3.3. Specifying dynamic process aspects in linear temporal logic

Since business process management systems can be considered as reactive systems, patterns can be modeled using LTL. This results in formulae that can be interpreted over linear state sequences, which allows to de<sup>fi</sup>ning (internal) controls that can be interpreted over the entire set of states or events of a single process instance. However, there exists a crucial difference between a business process instance and a reactive system, which is the trace length. Regular reactive systems are considered non-terminating, which is re<sup>fl</sup>ected in the in<sup>fi</sup>nite semantics of regular LTL. Therefore a bounded version of the LTL de<sup>fi</sup>nition (in accordance with [14]) should be used. Secondly, whereas each element of a trace in regular LTL may consist of a set of properties, an audit trail contains exactly one event for each element [30].

## De<sup>fi</sup>nition 4. LTL formula

An LTL formula p over a subset of ℰ is a function p: $\mathcal { E } ^ { * }  \{ t r u e , f a l s e \}$ with σ⊨p denoting that the formula p satis<sup>fi</sup>es trace σ $( p ( \sigma ) = t r u e )$ and $\sigma \sharp p$ denoting that formula p does not satisfy trace σ $( p ( \sigma ) =$ false). For all LTL formulas p and q true, false, ¬p, $p \wedge q , p \vee q , \square p , \odot p ,$ ${ \bigcirc } p , p U q$ and p W q are LTL formulas as well. The semantics and syntax (in the Manna/Pnueli notation) of LTL can be found in Table 3.

The main advantage LTL has to offer in the context of business process compliance checking is the ability to express relative time properties between states. This becomes especially clear in controls that specify that something has to hold eventually or that something has to hold until. Examples include:

• Activity inclusion rule: Activity $a _ { 1 }$ and activity a are mutually inclusive

$\diamondsuit \alpha ( x , a _ { 1 } , t _ { c } ) \Leftrightarrow \diamondsuit ( x , a _ { 2 } , t _ { c } )$ testedforeveryinstance

• Activity start precondition: Activity $a _ { 1 }$ can only be executed in a process instance if expression μ holds

$\ ( \neg \alpha ( x , a _ { 1 } , t _ { s } ) ) W \mu$ tested for every instance

## 3.3.4. Composed business rule patterns

Most of the desired real-world controls patterns can only be obtained and implemented with a composition of multiple atomic rule patterns. These compositions can be obtained through the use of logical connectors such as $\vee , \wedge ,  , \neg .$ Two types of combination can be identi<sup>fi</sup>ed:

## • Combination of rule patterns of different types

For example a combination of a simple response and precedence rule: A register insurance policy activity $\left( a _ { 1 } \right)$ should be followed by a process premium payment activity (a ) and a process premium payment activity should be preceded by a register insurance policy (must be tested for each process instance x)

$$
\Box (\alpha (x, a _ {1}, t _ {c}) \Rightarrow \Diamond \alpha (x, a _ {2}, t _ {c})) \land (\neg (\alpha (x, a _ {2}, t _ {s}) \lor \alpha (x, a _ {2}, t _ {c}))) W \alpha (x, a _ {1}, t _ {c})
$$

• Combination of rule patterns of the same type Combination of rule patterns of the same type

For example a combination of two precedence constraints: A pay for damages activity (a ) must be preceded by an evaluate claim activity $\left( a _ { 2 } \right)$ or an provide expert review activity (a<sub>3</sub>) (must be tested for each process instance x)

$$
(\neg (\alpha (x, a _ {1}, t _ {s}) \vee \alpha (x, a _ {1}, t _ {c}))) W (\alpha (x, a _ {2}, t _ {c}) \vee \alpha (x, a _ {3}, t _ {c}))
$$

## 3.4. Determining the rule-scope for configured rule patterns

Within the context of process-oriented compliance checking three levels of rule-scope can be distinguished: global level, process level and process instance level. The global process scope requires that each process in an organization's business operations complies with that rule. For example, a ‘record <sup>fi</sup>nancial transaction activity must be performed by an agent with role accountant’. Secondly, business rules may be imposed to a speci<sup>fi</sup>c business process. This might be the case for a claim handling process where the ‘settlement proposals must be approved by a manager’. The business process scope level may cover multiple business process types, for example both the <sup>fi</sup>re and the car insurance claim handling processes of an insurance company may require an approval cycle. Thirdly, the business rule scope may be restricted to business process instances with a speci<sup>fi</sup>c characteristic. Within the context of an order-to-cash process the business rule ‘non-recurring customers must give an advance’ may be enforced.

Table 3  
Semantics and syntax of linear temporal logic (LTL).  
```txt
Atomic proposition
proposition    σ\models p if and only if p = σ[1]
Boolean connectives
not (¬)    σ\models ¬p if and only if σ ≠ p
and (∧)    σ\models p ∧ q if and only if σ\models p and σ\models q
or (∨)    σ\models p ∨ q if and only if σ\models p or σ\models q
implication (⇒)    σ\models p ⇒ q if and only if σ\models ¬p ∨ q
equivalence (⇔)    σ\models p ⇔ q if and only if σ\models (p ∧ q) ∨ (¬p ∧ ¬q)
true    σ\models true if and only if σ\models p ∨ ¬p
false    σ\models false if and only if σ ≠ true
Temporal connectives
next (○)    σ\models p if and only if σ²↔ |= p
until (U)    σ\models pU q if and only if (∃₁≤i≤n: (σⁱ↔ |= q ∧ (∀₁≤j<i: σⁱ↔ |= p))
eventually (◇)    σ\models◇ p if and only if σ\models trueU p
always (□)    σ\models □p if and only if σ\models ¬◇¬p
weak until (W)    σ\models pW q if and only if σ\models (pUq) ∨ (□p)
```

## 4. Running example: claim handling processes in the insurance industry

In this section we introduce a running example for demonstrating the use of the proposed comprehensive rule-based compliance checking approach, a claim handling process in the insurance industry. This claim handling process serves to provide speci<sup>fi</sup>c examples of business rule pattern con<sup>fi</sup>gurations in the subsequent sections.

The generic structure of an insurance claim handling process for claims that do not include bodily injuries, can be conceptualized as a three-stage process. In the <sup>fi</sup>rst stage, the claim intake stage, a frontline employee performs typical claim intake activities, such as collecting all information, claim classi<sup>fi</sup>cation and routing the claim to the preferred claim administrator. This is followed by an extensive evaluation of the claim's susceptibility (possibly including a policy review) as well as an assessment of the sustained damage (potentially including expert evaluations), resulting in the formulation of an opinion. The third stage groups all activities related to the settlement or rejection of a claim, such as proposing a settlement, approval cycles and notifying the customer of the evaluation's outcome.

Fig. 4 graphically represents a basic process model, which does not take into account any exception handling paths such as the investigation of potentially fraudulent claims. The provided model is a common representation of the functional and control-<sup>fl</sup>ow perspective. It is however not hard to see that this particular process also requires restrictions related to the organizational and data perspective, for example authorization levels or levels of sustained damage in an approval cycle.

## 5. Populating the taxonomy: identifying relevant rule patterns for compliance checking and risk management

In this section we de<sup>fi</sup>ne speci<sup>fi</sup>c business rule types for each possible combination of a process mining perspective (PMP) and a rule restriction focus (RRF). When selecting the business rule types that populate the taxonomy, we analyzed whether the rule-based controls could be tested against the typical enriched process data. Hence it appears that important (detective) controls, such as direct supervision, could not be included in the taxonomy as they are not auditable based on the enriched process data.

The discussion of the business rule types is structured around the process mining perspective dimension, which are the rows in Fig. 3. Each of the following subsections elaborates one process mining perspective. The discussion within each subsection follows the order of the rule restriction focus dimension, presented in the columns of

Fig. 3. Examples for the running insurance industry case will be provided in Tables 4–7.

## 5.1. Functional perspective

The functional perspective on business processes deals with the occurrence of process activities (and related artifacts) in a process instance. In the business rule class where the focus is put on cardinality, we typically observe activity cardinality rule subtypes. These business rule subtypes represent the rules that implement a restriction on the number of occurrences of a certain activity in a speci<sup>fi</sup>c process instance [15]. The speci<sup>fi</sup>cation of the patterns based on this and the following rule types as well as an example for each pattern can be found in Table 4 (every row corresponds to a speci<sup>fi</sup>c cell in Fig. 3).

Combining both the functional perspective and a coexistence focus, results in business rule types that describe the possibilities of coexistence between activities of different activity types and of coexistence between certain activity and event types. The subtypes range from required coexistence to a forced non-coexistence between activity types and activity-event type combinations [28]. A dynamic data-driven restriction focus results in rule types that link the existence or absence of an activity of a certain type to a data-oriented condition. This dataoriented condition can be true from the beginning if it is based on case data or can become true during the process instance execution when it is based on speci<sup>fi</sup>c event data. Relative time rules in the context of the functional process perspective can refer to the rules that link the existence or absence of a certain activity in a process instance to a relative time condition, such as before a particular amount of time units starting from the process start.

In addition to rule types that appeal to the dynamic aspect of a process, static property rule types can also be distinguished. The eventartifact coexistence rule subtypes deal with the relation between activities and certain process related artifacts in a particular process state. This rule type is related to the postcondition as speci<sup>fi</sup>ed in the Web Service Modeling Ontology (WSMO) [33].

## 5.2. Control-flow perspective

The control-<sup>fl</sup>ow perspective on business processes focuses on the ordering of the process elements in a process instance. Coexistence rules within this process perspective deal with specifying ordering rules between activities of different activity types. Whereas the non-overlapping activity rule subtype can be used for just avoiding the concurrent execution of speci<sup>fi</sup>c activities, the activity order rule subtypes de<sup>fi</sup>ne exact or dering relationships between activities of certain activity types [28].

The data-driven rule types consist of business rules that de<sup>fi</sup>ne data conditions which need to be satis<sup>fi</sup>ed prior to the start of an activity of a particular activity type, the data-driven activity preconditions. These rule subtypes can be related to the preconditions as speci<sup>fi</sup>ed in the WSMO [33].

A combination of relative time rules and the control-<sup>fl</sup>ow perspective results in two subtypes of time-driven control-<sup>fl</sup>ow rules: the activity time rule subtype and the inter-activity time rule subtype. Business rules that belong to the activity time rule subtype specify a condition on the allowable execution time of an activity of a speci<sup>fi</sup>c activity type such as a minimum or maximum duration. In contrast business rules of the inter-activity time rule subtype de<sup>fi</sup>ne comparable conditions on the allowable time interval between activities of (different) activity types. Based on the timestamp an absolute time rule type can be speci-<sup>fi</sup>ed for the static property focus.

![](/api/attachments/CBHBEH6P/fulltext/images/84261fc43db235745f78249d5dc146f5f34694a45d2ec815fa1819ea88229cce.jpg)  
Fig. 4. Basic insurance claim handling process model.

Table 4 Rule patterns for the functional process mining perspective.

<table><tr><td>Rule restriction focus</td><td>Rule type</td><td>Rule pattern</td><td>Example from the running insurance industry case</td></tr><tr><td rowspan="4">Cardinality-based rules</td><td>Activity cardinality rule</td><td></td><td></td></tr><tr><td>Activity existence rule</td><td>An activity of type  $a_1$  must be performed at least once</td><td>A review claim activity must be performed at least once</td></tr><tr><td>Activity absence rule</td><td>An activity of type  $a_1$  must not be performed</td><td>A compensation activity (e.g. deduct an invoice from an insurance payment) must not be performed</td></tr><tr><td>Activity range rule</td><td>An activity of type  $a_1$  must be executed at least i times and at most j times</td><td>A provide expert review must be executed at most 3 times (i.e. expert of the insurance company, expert of the damage sufferer and ‘second’ opinion provided by an independent expert)</td></tr><tr><td rowspan="9">Event coexistence rules</td><td>Activity coexistence rule</td><td></td><td></td></tr><tr><td>Activity inclusion rule</td><td>Activity type  $a_1$  and Activity of type  $a_2$  are mutually inclusive</td><td>The register expert invoice activity type and the pay expert activity type are mutually inclusive</td></tr><tr><td>Activity substitution rule</td><td>Activity type  $a_1$  and activity type  $a_2$  are mutually exclusive</td><td>The send claim rejection letter activity type and the pay for damages activity type are mutually exclusive</td></tr><tr><td>Responded existence rule</td><td>If an activity of type  $a_1$  is performed then an activity of type activity  $a_2$  must be performed</td><td>If a register claim activity is performed then an evaluate claim activity must be performed</td></tr><tr><td>Activity choice rule</td><td>At least n activities of activity type set  $s_A$  (with m activity types) must be performed</td><td>At least one activity of activity type set  $s_A = \{ \text{contact insurance agent}, \text{contact client} \}$  must be performed</td></tr><tr><td>Event-Activity coexistence rule</td><td></td><td></td></tr><tr><td>Event-Activity responded existence rule</td><td>An activity of type  $a_1$  must be performed if an event of type  $e_1$  occurred</td><td>A send claim receipt activity must be performed if a receive claim event occurred</td></tr><tr><td>Event-Activity responded absence rule</td><td>An activity of type  $a_1$  must not be performed if an event of type  $e_1$  occurred</td><td>A pay for damages activity must not be performed if a reject causal relationship event occurred</td></tr><tr><td>Event-Activity responded choice rule</td><td>At least n activities of activity type set  $s_A$  (with m activity types) must be performed if an event of type  $e_1$  occurred</td><td>At least 1 activity of set  $s_A = \{ \text{reject claim, accept claim} \}$  must be performed if a receive claim event occurred</td></tr><tr><td rowspan="2">Dynamic data-driven rules</td><td>Data-Driven existence rule</td><td></td><td></td></tr><tr><td>Data-driven activity inclusion rule</td><td>If expression μ becomes true before the process instance ends, then an activity of type  $a_1$  must be executed at least once</td><td>If status of claim evolves from doubt to accepted, then a create provisions activity must be executed at least once</td></tr></table>

Table 4 (continued)

<table><tr><td>Rule restriction focus</td><td>Rule type</td><td>Rule pattern</td><td>Example from the running insurance industry case</td></tr><tr><td rowspan="4">Relative time-oriented rules</td><td>Data-driven activity exclusion rule</td><td>If expression  $\mu$  becomes true before the process instance ends, then activity  $a_{1}$  must not be executed</td><td>If status of claim evolves from doubt to rejected, then a create provisions activity must not be executed</td></tr><tr><td>Time-oriented activity existence rule</td><td></td><td></td></tr><tr><td>Timed activity existence rule</td><td>An activity of type  $a_{1}$  must be started/completed before/after/on t time units (relative to  $t_{0}$ )</td><td>An evaluate claim activity must be started before date of claim receipt + t time units</td></tr><tr><td>Timed activity absence rule</td><td>An activity of type  $a_{1}$  must not be started/completed before/after/on t time units (relative to  $t_{0}$ )</td><td>A close and register claim activity should not be completed after time of claim receipt + t time units</td></tr><tr><td rowspan="3">Static property rules</td><td>Event-Artifact Coexistence Rule</td><td></td><td></td></tr><tr><td>Activity-artifact coexistence rule</td><td>If activity of type  $a_{1}$  is performed then an artifact of type  $Art_{1}$  must exist</td><td>If a send claim rejection letter is performed then a rejection letter must exist</td></tr><tr><td>Non-activity event-artifact coexistence rule</td><td>If an event of type  $e_{1}$  occurs then an artifact of type  $Art_{1}$  must exist</td><td>If a receive claim event occurs then a completed claim form should exist</td></tr></table>

There is, however, no cardinality-based rule type speci<sup>fi</sup>ed for the control-<sup>fl</sup>ow perspective. The main reason for this is the use of varying granularity: activities in coarse grained business processes may be composed of subprocesses in <sup>fi</sup>nergrained representations of the same business process. Therefore, one could also use the activity cardinality rules in this context. The combination of the business rule patterns with representative examples can be found in Table 5.

## 5.3. Organizational perspective

The organizational perspective on business processes deals with the (human) resources that perform the activities in the business processes. When focusing on cardinality, the originator cardinality rule type was identi<sup>fi</sup>ed. This rule type allows the imposition of restrictions on the allowable number of executions of activities of an activity type by a speci<sup>fi</sup>c agent within the context of a single process instance [39]. The business rule class that is de<sup>fi</sup>ned by the combination of the organizational perspective with a coexistence focus de<sup>fi</sup>nes three main business rule types: the segregation of duties rule type, the binding of duties type and the temporal engagement rule type. Whereas the segregation of duties rule subtypes focus on avoiding the risks related to letting the same agent perform all activities, the binding of duties rule type requires that a set of activities is performed by the same person. These rule subtypes have been extensively researched and presented in [12,24]. The temporal engagement rule type makes it possible to verify if a speci<sup>fi</sup>ed person had a particular role/function at a certain point in time.

Table 5  
Rule patterns for the control-<sup>fl</sup>ow process mining perspective.

<table><tr><td>Rule restriction focus</td><td>Rule type</td><td>Rule pattern</td><td>Example from the running insurance industry case</td></tr><tr><td rowspan="8">Event coexistence rules</td><td>Non-overlapping activity rule</td><td>An activity of type  $a_1$  and an activity of type  $a_2$  must not be performed in parallel</td><td>An evaluate claim activity and an appoint expert activity must not be performed in parallel</td></tr><tr><td>Activity order rule</td><td></td><td></td></tr><tr><td>Simple response rule</td><td>If activity of type  $a_1$  is performed then an activity of type  $a_2$  must be performed afterwards</td><td>If an accept claim activity is performed then a create provisions activity must be performed afterwards</td></tr><tr><td>Simple precedence rule</td><td>An activity of type  $a_1$  must be performed before an activity of type  $a_2$  can be performed</td><td>A book invoice activity must be performed before a pay for damages activity can be performed</td></tr><tr><td>Alternate response rule</td><td>If an activity of type  $a_1$  is performed then an activity of type  $a_2$  must be performed afterwards and alternation is required</td><td>If a process car insurance premium payment activity is performed then a send a proof-of-car-insurance card (i.e. valid for one year in Belgium) activity must be performed afterwards and alternation is required</td></tr><tr><td>Alternate precedence rule</td><td>An activity of type  $a_1$  must be performed before an activity type  $a_2$  can be performed and alternation is required</td><td>A register vehicle must be performed before a strike off vehicle activity can be performed and alternation is required (for insurance policy transfer when the client changes vehicle)</td></tr><tr><td>Chain response rule</td><td>An activity of type  $a_2$  must be executed immediately after each execution of an activity of type  $a_1$ </td><td>An update provisions activity must be executed immediately after each execution of a pay for damages activity</td></tr><tr><td>Chain precedence rule</td><td>Each execution of an activity of type  $a_2$  must be immediately preceded by the execution of an activity of type  $a_1$ </td><td>Each execution of a fraud investigation activity must be immediately preceded by the execution of a determine claim fraud risk</td></tr><tr><td rowspan="3">Dynamic data-driven rules</td><td>Data-driven activity precondition rule</td><td></td><td></td></tr><tr><td>Activity start precondition rule</td><td>An activity of type  $a_1$  can only be executed if expression  $\mu$  holds</td><td>An update provisions activity can only be executed if the current provisions are lower than a recent estimate of the expected costs</td></tr><tr><td>Activity end precondition rule</td><td>An activity of type  $a_1$  can only be completed if expression  $\mu$  holds</td><td>A close and classify claim activity can only be completed if there no longer exist any provisions for that claim</td></tr><tr><td rowspan="3">Relative time-oriented rules</td><td>Time-driven control-flow rule</td><td></td><td></td></tr><tr><td>Activity time rule</td><td>An activity of type  $a_1$  must be performed in at most/ exactly at most/ exactly/at least t time units</td><td>An activity evaluate claim must be completed in at most t time units</td></tr><tr><td>Inter-activity time rule</td><td>Between the execution of an activity of type  $a_1$  and of an activity of type  $a_2$  there are at most/ exactly/at least t time units</td><td>Between the execution of a register vehicle total loss activity and of a stop vehicle insurance coverage there are at most t time units</td></tr><tr><td>Static property rules</td><td>Absolute time rule</td><td>If an activity of type  $a_1$  is performed, then it must be performed before  $t_0$  (based on exact timestamp)</td><td>If a give a discount on premium activity is performed, then it must be performed before the end of the month of May</td></tr></table>

Business rule types with a dynamic data-driven focus enable the speci<sup>fi</sup>cation of organizational preconditions. Exogenous authorization rules deal with conditions and factors external to the process instance executions. Originator attribute rules de<sup>fi</sup>ne restrictions on who can perform an activity based on a combination of event/case data and originator speci<sup>fi</sup>c data. The relative time rules' main rule subtypes are linked to temporal deontic rules. These rules are based on the concept of a deontic assignment (including the obligations and permissions) while respecting a time constraint [54].

The static property rule types include the static authorization rule type, the required originator attribute rule type and the delegation rule type. The static authorization subtypes allow for the speci<sup>fi</sup>cation of non-evolving authorizations controls. Role-based authorization and prohibited allocation rules de<sup>fi</sup>ne respectively the right to perform an activity and the prohibition to perform an activity. Both are actively been researched for example in [12]. Suboptimal allocations that may affect the time/cost ef<sup>fi</sup>ciency or impede the correct execution of the business operations, can be traced down with non-optimal allocation rules. The second main type of static property rules, the required originator attribute rules, deals with verifying whether an agent possesses certain characteristics needed to perform the activity. Finally, the delegation rule subtypes cover the whole spectrum of concerns that are related to role delegation: from allowable allocations, over delegation authorizations to retract policies [51].

While the main organizational rules will focus on restricting the rights of speci<sup>fi</sup>c individuals or individuals of a certain role, several rule types could be speci<sup>fi</sup>ed for different ‘agents’ such as an organizational entity. Table 6 contains the related rule patterns with relevant examples for the insurance industry.

## 5.4. Data perspective

The data or informational perspective on business processes represents the informational elements that are used, produced or manipulated during the process, as well as the relationships among them. A distinction is made between data elements that relate to events such as an invoice amount to a pay for damages activity and data elements that are speci<sup>fi</sup>ed for a speci<sup>fi</sup>c business process instance or case like the status of the customer.

In the context of cardinality-based rules, the event data cardinality rule subtypes can be distinguished. Each of these subtypes deals with restricting the allowed number of instances of a certain data element type for a single instance of a speci<sup>fi</sup>c event type. The coexistence rules, on the other hand, specify co-occurrence restrictions for data elements of different types within the context of a single instance of a speci<sup>fi</sup>c event type.

The dynamic data driven rule types de<sup>fi</sup>ne the value of speci<sup>fi</sup>c event data elements in terms of the value of other data elements. Whereas the derived event data rule subtypes provide some sort of expression to de termine the value of a data element, the event data comparison rule subtypes de<sup>fi</sup>ne value comparison restrictions based on the value of other data elements and possibly over multiple events. These rules are related to the set comparison constraints in the Object-Role Modeling Approach [18]. Relative time rules in the data perspective mainly focus on specifying the dynamic integrity of data elements value. Admissible changes in the data elements value are speci<sup>fi</sup>ed in terms of exact time, the execution of an activity [27] or the occurrence of an event.

Table 6  
Rule patterns for the organizational process mining perspective.

<table><tr><td>Rule restriction focus</td><td>Rule type</td><td>Rule pattern</td><td>Example from the running insurance industry case</td></tr><tr><td>Cardinality-based rules</td><td>Originator cardinality rule</td><td>An activity of type  $a_1$  must not be performed more/ less then n times by the same person (in period T)</td><td>A decrease insurance premium activity must not be performed more than 3 times by the same person (in one year)</td></tr><tr><td rowspan="7">Event coexistence rules</td><td>Segregation of duties</td><td></td><td></td></tr><tr><td>Conflicting roles</td><td>A person must not be a member of both role  $r_1$  and role  $r_2$  (i.e. not perform both activities for role  $r_1$  and activities for role  $r_2$ )</td><td>A person must not be a member of both the role of intaker (i.e. first analysis and distribution of claims) and the role of controller</td></tr><tr><td>Dynamic segregation of duties</td><td>A person must not perform both an activity of type  $a_1$  and an activity of type  $a_2$ </td><td>A person must not perform both an evaluate claim activity and an approve payment activity</td></tr><tr><td>Operational segregation of duties</td><td>A person must not perform all activities of the activity type set  $s_A$  (with m activity types)</td><td>A person must not perform all activities of the activity type set  $s_A$ =claim intake, evaluate claim, determine provision increase, appoint repairer, approve payment}</td></tr><tr><td>History based segregation of duties</td><td>A person must not perform all activities in a specific process instance of process type  $s_1$ </td><td>A person must not perform all activities in a specific process instance of the new insurance policy administration process</td></tr><tr><td>Binding of duties</td><td>A person must perform all activities in activity set  $s_A$  (with m activity types)</td><td>A person must perform all activities in the contact person activity set  $s_A$ ={including answer questions, contact client,...}</td></tr><tr><td>Temporal engagement rule</td><td>Person  $o_1$  was a member of role  $r_1$  on time T (i.e. role delegation event happened before T and a role retraction event happened after T)</td><td>Person  $o_1$  was a member of role actuary on time T</td></tr><tr><td rowspan="4">Dynamic data-driven rules</td><td>Exogenous authorization rule</td><td>An activity of type  $a_1$  must be performed under μ</td><td>An evaluate claim activity must be performed at the office during regular office hours</td></tr><tr><td>Originator attribute rule</td><td></td><td></td></tr><tr><td>Static originator attribute rule</td><td>An activity of type  $a_1$  must be performed by a person who has characteristic C when μ evaluates true</td><td>A call customer activity must be performed by a person who has as mother tongue Dutch when the client is Dutch speaking</td></tr><tr><td>Dynamic originator attribute rule</td><td>An activity of type  $a_1$  must be performed by a person who has temporal characteristic C</td><td>Activity approve payment must be performed by person P who is not out of the office</td></tr><tr><td rowspan="4">Relative time-oriented rules</td><td>Temporal deontic rule</td><td></td><td></td></tr><tr><td>Temporal obligation rule (time/activity/event)</td><td>Person  $o_1$  must perform an activity of type  $a_1$  before/at/after time T (with T referring to time/activity/event)</td><td>Person  $o_1$  must perform a claim evaluation after time T = timestamp of receive claim event</td></tr><tr><td>Temporal permission rule (time/activity/event)</td><td>Person  $o_1$  can perform an activity of type  $a_1$  before/at/after time T (with T referring to time/activity/event)</td><td>Person  $o_1$  can perform an increase provision after time T = timestamp of provide expert review activity</td></tr><tr><td>Temporal prohibition rule (time/activity/event)</td><td>Person  $o_1$  must not perform an activity of type  $a_1$  before/at/after time T (with T referring to time/activity/event)</td><td>Person  $o_1$  cannot perform a reject claim after time T = timestamp of receive claim event + 20 days</td></tr><tr><td rowspan="9">Static property rules</td><td>Static authorization rule</td><td></td><td></td></tr><tr><td>Role-based activity authorization rule</td><td>An activity of type  $a_1$  must be performed by a member of role  $r_1$ </td><td>A fraud investigation activity must be performed by a member of the role forensic expert</td></tr><tr><td>Prohibited role-based allocation rule</td><td>An activity of type  $a_1$  must not be performed by a member of role  $r_1$ </td><td>An appoint repairer activity must not be performed by a member of the role claim intaker</td></tr><tr><td>Not-optimal allocation rule</td><td>It is not optimal that a member of role  $r_1$  performs an activity of type  $a_1$ </td><td>It is not optimal that a member of role management performs an evaluate claim activity</td></tr><tr><td>Required originator attribute rule</td><td>An activity of type  $a_1$  must be performed by a person who has characteristic C</td><td>A provide expert review activity must be performed by a person who has a specific certification (e.g. civil engineering, architecture or jewelry expert). depending on the case)</td></tr><tr><td>Delegation rule</td><td></td><td></td></tr><tr><td>Prohibited role acquisition rule</td><td>A person must not become a member of both role  $r_1$  and role  $r_2$ </td><td>A person must not become a member of both the insurance agent role and the claim reviewer role</td></tr><tr><td>Delegation authorization rule</td><td>A person must be a member of role  $r_1$  in order to delegate role  $r_1$ </td><td>A person must be member of the senior claim reviewer role in order to delegate the senior claim reviewer role (to a subordinate)</td></tr><tr><td>Retract restriction rule</td><td>Person  $o_1$  with role  $r_1$  cannot be retracted from role  $r_1$  when the set  $s_P$  of persons with role  $r_1$  only contains person  $o_1$ </td><td>Person  $o_1$  with the senior claim reviewer role cannot be retracted from the senior claim reviewer role when the set  $s_P$  of persons with the role senior claim reviewer only contains person  $o_1$ </td></tr></table>

Included in the static property rule types for the data perspective are both business rule types that specify acceptable event data values in terms of sets or ranges, for example, and rule types that impose a event data format, see also [18]. The corresponding business rule patterns are described in Table 6.

## 6. Discussion: applications, opportunities, assumptions and challenges of comprehensive rule-based compliance checking

The proposed comprehensive rule-based compliance checking approach has a wide variety of applications in corporate governance. Applications for the generic stakeholders with a corporate governance function are explored and described in Subsection 6.1. Afterwards the discussion section will focus on the opportunities, assumptions and challenges of comprehensive rule-based compliance checking.

Table 7  
Rule patterns for the data process mining perspective.

<table><tr><td>Rule restriction focus</td><td>Rule type</td><td>Rule pattern</td><td>Example from the running insurance industry case</td></tr><tr><td rowspan="2">Cardinality-based rules</td><td>Event data cardinality ruleMandatory event data rule</td><td>The value for event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must be specified</td><td>The value of policy number (wrt a start event for an analyze specific policy terms activity) must be specified</td></tr><tr><td>Event data multiplicity constraint</td><td>At least/ exactly/atmost n values for event data type  $p_1$  (wrt an event of event type  $e_1$  for an activity of type  $a_1$ ) must be specified</td><td>At least one value of third party identifier (wrt a complete event of a pay for damages activity) must be specified</td></tr><tr><td rowspan="2">Event coexistence rules</td><td>Event data coexistence rulesDisjunctive event data rule</td><td>The value of at least one event data element for data type set  $s_D$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must be specified</td><td>The value of at least one event data element for data type set  $s_D$  (amount paid for bodily injuries, amount paid for material damages, amount paid for financial losses) (wrt a complete event for a pay for damages activity of type  $a_1$ ) must be specified</td></tr><tr><td>Mutually exclusive event data rule</td><td>The value of exactly one event data element for data type set  $s_D$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must be specified</td><td>The value of exactly one event data type for set  $s_D = \{social\ security\ number, passport\ number\ or\ organization\ registration\ number\}$  (wrt a complete event for a register claim activity) must be specified</td></tr><tr><td rowspan="4">Dynamic data-driven rules</td><td>Derived event data ruleArithmetic derivation rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) is calculated using the mathematical expression  $\mu$ </td><td>The value of insurance surcharges (wrt a complete event for an update insurance premium activity) is calculated using the mathematical expression insurance surcharges = current premium x 0,20</td></tr><tr><td>Logical derivation rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) is determined using the expression  $\mu$ </td><td>The value of compulsory excess (wrt a complete event for a register car insurance policy activity) is determined using the expression (if age ≤ 23 then 500 else 400)</td></tr><tr><td>Event data comparison ruleEvent data equality rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) is equal to the value of event data type  $p_2$  (wrt an event of type  $e_2$  for an activity of type  $a_2$ )</td><td>The value of policy number (wrt a complete event for a register claim activity) is equal to the value of policy number (wrt a complete event for update insurance premium activity)</td></tr><tr><td>Event data exclusion rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) is not equal to the value of event data type  $p_2$  (wrt an event of type  $e_2$  for an activity of type  $a_2$ )</td><td>The value of third party identifier (wrt a complete event for a pay for damages activity) is not equal to the value of policyholder identifier (wrt a complete event for a register claim activity)</td></tr><tr><td rowspan="3">Relative time-oriented rules</td><td>Dynamic integrity ruleTime-oriented integrity rule</td><td>The value of data type  $p_1$  may not change before/at/after time  $t_0$  relative to event  $e_1$ </td><td>The value of provisions (i.e. fixed sum that is set aside at the claim receival event) may not change before the completion of a provide expert review activity</td></tr><tr><td>Activity-oriented integrity rule</td><td>The value of data type  $p_1$  may not change before/at/after a completion of activity  $a_1$ </td><td>The value of estimated damages may not change after the completion of a provide expert review activity</td></tr><tr><td>Event-oriented integrity rule</td><td>The value of data type  $p_1$  may not change before/at/after an occurrence of event  $e_1$ </td><td>The value of policy number may not change after an occurrence of a receive claim event</td></tr><tr><td rowspan="5">Static property rules</td><td>Event data value ruleEvent data value set rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must be included in set of values  $s_V$ </td><td>The value of expert identifier (wrt a complete event for a provide expert review activity) must be included in set  $s_V = \{identifier\ of\ all\ accredited\ experts\}$ </td></tr><tr><td>Event data value range rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must be included in value range  $range_V$ </td><td>The value of amount paid for bodily injuries(wrt a complete event for a pay for damages activity) must be included in value range $_V = [1,7500000]$ </td></tr><tr><td>Event data uniqueness rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must be unique</td><td>The value of policy number (wrt a complete event for a register car insurance policy activity) must be unique</td></tr><tr><td>Irreflexive event data rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) is not equal to the value of event data type  $p_2$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ )</td><td>The value of originator identifier (wrt a complete event for an evaluate claim activity) is not equal to the value of policyholder identifier (wrt a complete event for an evaluate claim activity)</td></tr><tr><td>Event data format rule</td><td>The value of event data type  $p_1$  (wrt an event of type  $e_1$  for an activity of type  $a_1$ ) must conform to data format  $f_1$ </td><td>The value of account number (wrt a complete event for a pay for damages activity) must conform to the standard account number format with check digit</td></tr></table>

## 6.1. Applications of comprehensive rule-based compliance checking

The proposed comprehensive rule-based process mining approach can provide extensive support for corporate governance activities, performed by the organization's management, its internal auditors and the external auditors.

The comprehensive rule-based compliance checking approach could complement the management's existing set of tools and techniques for risk evaluation, response and monitoring. Firstly, con<sup>fi</sup>gured rule patterns enable the identi<sup>fi</sup>cation of events that might adversely affect the achievement of the objectives and the estimation of both the risk's probability and severity, known as respectively risk identi<sup>fi</sup>cation and assessment. Moreover, the approach enables the discovery of correlations between different types of risk. Secondly, comprehensive rule-based compliance checking is well suited for the design and implementation of detective retrospective management controls, which is a risk response strategy. Thirdly, the proposed approach is suitable for monitoring the evolution of both the risk's impact and its possibility of occurrence. The identi<sup>fi</sup>ed activities are in accordance with the COSO Enterprise Risk Management Framework [6].

The main internal audit process deals with providing independent and objective opinion to the management and the audit committee on the effectiveness and the adequateness of both the risk management and control processes. Risk assessment activities and techniques, comparable to those of the management, are used by the internal audit department to delineate the scope of the audit plan and consequently to determine the work that needs to be performed in each area. During the performance of the engagement comprehensive rule-based compliance checking can be used to analyze, evaluate and collect evidence in order to achieve the internal audit objectives as described in the audit plan.

The external auditor will execute risk assessments and testing procedures comparable to those of the internal auditor. Additionally, comprehensive rule-based compliance checking could support the auditor in determining the engagement risk, affected by factors such as the domination of individuals in certain activities or the presence of a high volume of signi<sup>fi</sup>cant year-end transactions.

6.2. Opportunities, assumptions and challenges of comprehensive rule-based compliance checking

This section starts with providing and discussing the main opportunities that could result in signi<sup>fi</sup>cant progress in the research area. Afterwards a discussion of the data quality assumption and the challenges for further improving the <sup>fi</sup>t with the requirements of contemporary risk management and auditing will be presented.

6.2.1. Opportunity 1: high issue detection effectiveness — approaching absolute assurance

The comprehensive rule-based compliance checking approach enables the controller to perform (substantive) tests on large samples of enriched process event data. The higher the relative size of the sample compared to the full population the better the assurance. For full population analysis a near absolute assurance can be offered. This results in a high level of certainty about the statements on the internal control effectiveness made by the controllers.

## 6.2.2. Opportunity 2: obtaining persuasive evidence

The persuasiveness of the obtained evidence, which is strongly correlated to its competence and suf<sup>fi</sup>ciency [1], is expected to be high. Comprehensive rule-based compliance checking approaches positively effect the determinants of evidence competence, namely the provider's independence, the evaluator's direct knowledge, the degree of objectiveness and the timeliness (referring to the period covered). As the proposed rule-based technique enables the controller to timely inspect a large sample or even the whole population of events related to speci<sup>fi</sup>c transactions, there will be a rather low risk of overlooking an issue. Consequently, the evidence collected on either the effectiveness or the ineffectiveness of an internal control is expected to be suf<sup>fi</sup>cient, see Subsection 6.2.1.

## 6.2.3. Opportunity 3: realizing complete auditor independence

The higher the auditor's independence of the auditee, the more valuable the audit or evaluation [1]. Comprehensive rule-based compliance checking does not require the embedment of auditing modules in the client's systems, they only use the output of the client's systems. This type of approaches is known as external auditing modules [50]. Consequently, the functionality of the audit modules is designed and maintained by the auditor (or his/her <sup>fi</sup>rm), without any possible interference from the client or his system administrators. Secondly, architectures based on external modules can fully guarantee a non-existence of a-priori knowledge with the client about the auditing approach and procedures. In contrast, the implementation of internal modules would require cooperation of the client, which might result in a-priori knowledge.

## 6.2.4. Assumption: event log data qualit

Compliance and risk analyses require event logs that meet high quality standards in order to derive meaningful conclusions. The data in an event-log of an information system must be recorded in a trustworthy manner, making for example ID fraud or backdating impossible. Additionally, these recordings must be kept securely, which refers to the prevention of any tampering with the data after the recording. The third quality criteria, systematic recording, re<sup>fl</sup>ects the need for a timely recording of every important business event. Accuracy can be regarded as a measure that re<sup>fl</sup>ects the correctness of the representation in the event-log compared to a real-life event. This can be determined both on syntactical as well as semantical level. In [21], for example, it is argued that major ERP systems can contain missing and faulty data values. While trustworthy and securely recording looks at the possibilities for humans to in<sup>fl</sup>uence the recorded data, accuracy focuses on the ability of the provenance system to correctly record the data and on the existence of noise because of technical errors.

## 6.2.5. Challenge 1: distortions in interpretation and pattern design

The comprehensive rule-based compliance checking approach is still subject to interpretation distortions resulting from vague and ambiguous legislation, policies and directives [25]. Moreover, the compliance analyst might be confronted with expressibility limitations for a small number of extremely rare and context speci<sup>fi</sup>c internal controls. Additionally, the completeness assumption of an event log that assumes that every possible behavior is covered in the event log, can often be challenged. The results of a comprehensive rule-based compliance checking analysis should, however, not be affected by process overspeci<sup>fi</sup>cation.

6.2.6. Challenge 2: implementing comprehensive rule-based continuous auditing/monitoring

An important time-delay might be observed between the occurrence of important business events and the publishing of a monitoring or audit report, the result of the periodic nature of monitoring or auditing models. Adapting the concepts and rule types presented in this contribution to the complex event processing architecture or the monitoring control layer [50], which involves a move to event streams, will result in the development of a continuous monitoring and auditing technique. The continuous monitoring and auditing approach focuses on investigating the events simultaneously or shortly after their occurrence [22]. Consequently, the time-delay is signi<sup>fi</sup>cantly reduced and the created information becomes more valuable.

## 7. Conclusion and outlook

Process mining research has been characterized by a narrow research focus on theoretical improvements, resulting in a partial <sup>fi</sup>t between compliance checking and risk management and the existing process mining techniques. Aspects of this rather limited <sup>fi</sup>t include: the ignorance of case and event data, the reasonable doubt about the correctness of designed process models and the need for balance between precision and generality potentially whipping out suspicious behavior (for process discovery).

In this paper we proposed a comprehensive rule-based compliance checking approach as a possible solution to eliminate the limited <sup>fi</sup>t. The approach enables analysts to uncover compliance failures as well as to identify and assess potential risks. Improvements can be found in the ability to take additional data into account, the reduction of possible distortions (including over speci<sup>fi</sup>cation) and no need for generalization. Additionally, the comprehensive rulebased compliance checking approach provides information on a potential compliance risk, whereas recall/precision metrics only provide a process-wide indicator. This contribution proposed an extensive set of rule patterns that is <sup>fi</sup>t to be used in a common business setting. Whereas the comprehensibility of the rule patterns is high due to the use of native English, the formal grounding removes any ambiguity. Finally, an evaluation containing the major opportunities (effectiveness, persuasive evidence and audit independence), assumption (data quality) and challenges (distortions in interpretation and pattern design and continuous monitoring/auditing) was presented.

A logical future step in our research is to further test this approach and to tackle the identi<sup>fi</sup>ed challenges. Focus will be placed on the development of a continuous monitoring/auditing approach based on process mining techniques.

## Acknowledgments

We would like to thank the KU Leuven research council for <sup>fi</sup>nancial support under grant OT/10/010: Business Process Mining: New Techniques and Evaluation Metrics and the Flemish research council for <sup>fi</sup>nancial support under the Odysseus grant B.0915.09.

## References

[1] A.A. Arens, R.J. Elder, M.S. Beasley, Auditing and Assurance Services: An Integrated Approach, Pearson Education, 2005.

[2] J. Bang-Jensen, G.Z. Gutin, Digraphs: Theory, Algorithms and Applications, Springer Verlag, 2010.

[3] F. Chesani, P. Mello, M. Montali, F. Riguzzi, M. Sebastianis, S. Storari, Checking Compliance of Execution Traces to Business Rules, in: Business Process Management Workshops, Springer, 2009, pp. 134–145.

[4] J.E. Cook, A.L. Wolf, Discovering models of software processes from event-based data, ACM Transactions on Software Engineering and Methodology 7 (3) (1998) 215–249.

[5] J.E. Cook, A.L. Wolf, Software process validation: quantitatively measuring the correspondence of a process to a model, ACM Transactions on Software Engineering and Methodology 8 (2) (1999) 147–176.

[6] COSO, Enterprise Risk Management — Integrated Framework, Technical report, Committee of Sponsoring Organizations of the Treadway Commission, 2004.

[7] B. Curtis, M.I. Kellner, J. Over, Process Modeling, Communications of the ACM 35 (9) (1992) 75–90.

[8] H. de Beer, The LTL checker plugins: A reference manual, Technical report, Eindhoven University of Technology, 2004.

[9] A.K.A. de Medeiros, B.F. van Dongen, W.M.P. van der Aalst, A. Weijters, Process Mining: Extending the α-Algorithm to Mine Short Loops Technical report University of Technology, Eindhoven, 2004.

[10] A.K.A. de Medeiros, W.M.P. van der Aalst, C. Pedrinaci, Semantic Process Mining Tools: Core Building Blocks, in: 16th European Conference on Information Systems, Citeseer, 2008, pp. 1953–1964.

[11] R. Dijkman, M. Dumas, B. Van Dongen, R. Kaarik, J. Mendling, Similarity of business process models: metrics and evaluation, Information Systems 36 (2) (2011) 498–516.

[12] D. Ferraiolo, D.R. Kuhn, R. Chandramouli, Role-based Access Control, Artech House Publishers, 2003.

[13] D.R. Ferreira, Applied Sequence Clustering Techniques for Process Mining, Handbook of Research on Business Process Modeling, IGI Global, 2009.

[14] D. Giannakopoulou, K. Havelund, Automata-based Veri<sup>fi</sup>cation of Temporal Properties on Running Programs, in: Proceedings of the 16th Annual Conference on Automated Software Engineering, 2001, pp. 412–416, (Published by the IEEE Computer Society).

[15] S. Goedertier, R. Haesen, J. Vanthienen, Rule-based business process modelling and enactment, International Journal of Business Process Integration and Management 3 (3) (2008) 194–207.

[16] S. Goedertier, D. Martens, J. Vanthienen, B. Baesens, Robust Process Discovery with Arti<sup>fi</sup>cial Negative Events, Journal of Machine Learning Research 10 (2009) 1305–1340.

[17] R. Gopal, J.R. Marsden, J. Vanthienen, Information mining-re<sup>fl</sup>ections on recent advancements and the road ahead in data, text, and media mining, Decision Support Systems 51 (4) (2011) 727–731.

[18] T. Halpin, Object-role Modeling (ORM/NIAM), in: Handbook on Architectures of Information Systems, 2006, pp. 81–103.

[19] S.M. Huang, D.C. Yen, Y.C. Hung, Y.J. Zhou, J.S. Hua, A business process gap detecting mechanism between information system process <sup>fl</sup>ow and internal control <sup>fl</sup>ow, Decision Support Systems 47 (4) (2009) 436–454.

[20] S.Y. Hwang, W.S. Yang, On the discovery of process models from their instances\* 1, Decision Support Systems 34 (1) (2002) 41–57.

[21] J.E. Ingvaldsen, J.A. Gulla, Preprocessing Support for Large Scale Process Mining of SAP Transactions, in: Proceedings of the 2007 International Conference on Business Process Management, Springer, 2007, pp. 30–41.

[22] ISACA Standards Board, Continuous auditing: Is it fantasy or reality? Information Systems Control Journal 5 (2002).

[23] M. Jans, N. Lybaert, K. Vanhoof, J.M. van der Werf, A business process mining application for internal transaction fraud mitigation, Expert Systems with Applications 38 (10) (2011) 13351–13359.

[24] K. Knorr, H. Stormer, Modeling and analyzing separation of duties in work<sup>fl</sup>ow environments, in: Trusted Information, 2002, pp. 199–212.

[25] K.J. Lee, B. Jeon, Analysis of best practice policy and benchmarking behavior for government knowledge management, in: Knowledge Management in Electronic Government, 2004, pp. 70–79.

[26] M. Montali, Declarative process pining, Speci<sup>fi</sup>cation and Veri<sup>fi</sup>cation of Declarative Open Interaction Models (2010) 343–365.

[27] Object Management Group, Semantics of business vocabulary and rules (SBVR), Technical report, Technical Report dtc/06–03–02, 2006

[28] M. Pesic, W.M.P. van der Aalst, A declarative approach for <sup>fl</sup>exible business processes management, in: Business Process Management Workshops, Springer, 2006, pp. 169–180.

[29] M. Pesic, M.H. Schonenberg, N. Sidorova, W.M.P. Van Der Aalst, Constraint-based Work<sup>fl</sup>ow Models: Change Made Easy, in: Proceedings of the 2007 OTM Confederated international conference on the move to meaningful internet systems, Springer-Verlag, 2007, pp. 77–94.

[30] M. Pesic. Constrained-based work<sup>fl</sup>ow management systems: Shifting control to users. PhD thesis, Eindhoven University of Technology, 2008.

[31] R.S. Mans, M.H. Schonenberg, M. Song, W.M.P. Aalst, P.J.M. Bakker, Application of process mining in healthcare–a case study in a dutch hospital, Biomedical Engineering Systems and Technologies 25 (2009) 425–438.

[32] N. Rescher, A. Urquhart, Temporal Logic, Springer-Verlag, Berlin, 1971.

[33] D. Roman, U. Keller, H. Lausen, J. de Bruijn, R. Lara, M. Stollberg, A. Polleres, C. Feier, C. Bussler, D. Fensel, Web service modeling ontology, Applied Ontology 1 (1) (2005) 77–106.

[34] A. Rozinat, W.M.P. van der Aalst, Conformance checking of processes based on monitoring real behavior, Information Systems 33 (1) (2008) 64–95.

[35] A. Rozinat, W.M.P. van der Aalst, W.M.P. van der Aalst, Conformance Testing: Measuring the Fit and Appropriateness of Event Logs and Process Models, in: Business Process Management Workshops, Springer, 2006, pp. 163–176.

[36] V. Rubin, C. Gunther, W.M.P. van der Aalst, E. Kindler, B. van Dongen, W. Schafer, Process mining framework for software processes, in: Software Process Dynamics and Agility, 2007, pp. 169–181.

[37] S.W. Sadiq, M.E. Orlowska, W. Sadiq, Speci<sup>fi</sup>cation and validation of process constraints for <sup>fl</sup>exible work<sup>fl</sup>ows, Information Systems 30 (5) (2005) 349–378.

[38] M. Song, C.W. Gunther, W.M.P. Aalst, Trace Clustering in Process Mining, in: Busi ness Process Management Workshops, Springer, 2009, pp. 109–120.

[39] K. Tan, J. Crampton, C.A. Gunter, The Consistency of Task-based Authorization Constraints in Work<sup>fl</sup>ow, in: Proceedings of the 17th IEEE Computer Security Foundations Workshop, IEEE, 2004, pp. 155–169.

[40] W.M.P. van Aalst, K.M. Van Hee, J.M. van Werf, M. Verdonk, Auditing 2.0: Using Process Mining to Support Tomorrow's Auditor, Computer 43 (3) (2010) 90–93.

[41] W.M.P. van der Aalst, Business alignment: Using process mining as a tool for delta analysis and conformance testing, Requirements Engineering Journal 10 (3) (2005) 198–211.

[42] W.M.P. Van der Aalst, M. Song, Mining social networks: uncovering interaction patterns in business processes, in: Business Process Management, 2004, pp. 244–260.

[43] W.M.P. van der Aalst, B. Van Dongen, Discovering work<sup>fl</sup>ow performance models from timed logs, in: Engineering and Deployment of Cooperative Information Systems, 2480, 2002, pp. 107–110.

[44] W.M.P. van der Aalst, A. Weijters, Process mining: a research agenda, Computers in Industry 53 (3) (2004) 231–244.

[45] W. Van der Aalst, T. Weijters, L. Maruster, Work<sup>fl</sup>ow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[46] W.M.P. van der Aalst, H.T. De Beer, B.F. van Dongen, Process mining and veri<sup>fi</sup>cation of properties: an approach based on temporal logic, in: On the Move to Meaningful Internet Systems 2005: CoopIS, DOA, and ODBASE, 3760, 2005, pp. 130–147.

[47] W.M.P. van der Aalst, H.A. Reijers, A.J.M.M. Weijters, B.F. van Dongen, A.K. Alves de Medeiros, M. Song, H.M.W. Verbeek, Business process mining: an industrial application, Information Systems 32 (5) (2007) 713–732.

[48] W.M.P. van der Aalst, B. van Dongen, C. Gunther, R. Mans, A. de Medeiros, A. Rozinat, V. Rubin, M. Song, H. Verbeek, A. Weijters, ProM 4.0: Comprehensive support for real process analysis, in: Petri Nets and Other Models of Concurrency–ICATPN 2007, 2007, pp. 484–494.

[49] W.M.P. Van der Aalst, B.F. Van Dongen, C. Gunther, A. Rozinat, H.M.W. Verbeek, A. Weijters, ProM: The Process Mining Toolkit, in: Proceedings of the International Conference on Business Process Management, 2009, pp. 1–4.

[50] M.A. Vasarhelyi, M.G. Alles, A. Kogan, Principles of analytic monitoring for continuous assurance, Journal of Emerging Technologies in Accounting 1 (1) (2004) 1–21.

[51] K. Venter, M. Olivier, The Delegation Authorization Model: A Model for the Dynamic Delegation of Authorization Rights in a Secure Work<sup>fl</sup>ow Management System, in: Proceedings of Information Security South Africa (ISSA'02), 2002.

[52] A. Weijters, W.M.P. van der Aalst, Process Mining: Discovering Work<sup>fl</sup>ow Models from Event-based Data, in: Proceedings of the 13th Belgium-Netherlands Conference on Arti<sup>fi</sup>cial Intelligence (BNAIC 2001), Citeseer, 2001. pp. 283-290.

[53] A. Weijters, W.M.P. van der Aalst, A.K.A. de Medeiros, Process mining with the heuristics miner-algorithm, in: TechnischeUniversiteit Eindhoven, Tech. Rep. WP, 166, 2006

[54] P. Yolum, M.P. Singh, Reasoning about commitments in the event calculus: an approach for specifying and executing protocols, Annals of Mathematics and Arti<sup>fi</sup>- cial Intelligence 42 (1) (2004) 227–253.

![](/api/attachments/CBHBEH6P/fulltext/images/193798683de3c1a1052ef6325af8e3df32cfd6cd8ab80f13f5e4833cf8693fc5.jpg)  
Filip Caron received a Master's degree in Business Engineer ing form the KU Leuven, Belgium. He is currently a Ph.D. candi date at the Department of Decision Sciences and Information Management, Faculty of Business and Economics, KU Leuven, Belgium. His research interests include business rules, business process modeling and mining and decision support systems.

![](/api/attachments/CBHBEH6P/fulltext/images/548b578cec51567318ff9a27f773001851dca5a335a9cd938355727f491fb2ee.jpg)

Prof. dr. Bart Baesens is an associate professor at KU Leuven Belgium, and a lecturer at the University of Southampton (United Kingdom). He has done extensive research on predictive analytics, data mining, customer relationship management, fraud detection, and credit risk management. His <sup>fi</sup>ndings have been published in well-known international journals (e.g. Machine Learning, Management Science, IEEE Transactions on Neural Networks, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Evolutionary Computation and Journal of Machine Learning Research) and presented at international top conferences. He is also co-author of the book Credit Risk Management: Basic Concepts, pub lished in 2008.

![](/api/attachments/CBHBEH6P/fulltext/images/8ccafbebd1dcdd0a7abbb8f5a4c93eb337e6f518ea7b6435f2c6d06222f729ee.jpg)  
Prof. dr. Jan Vanthienen is professor of information management at KU Leuven, Department of Decision Sciences and Information Management, where he coordinates the Leuven Institute for Research in Information Systems (LIRIS). His research interests include information and knowledge management, business rules, processes & decisions, business intelligence and intelligent systems. On these topics, he has published numerous papers in reviewed international journals and conference proceedings. He received the Belgian Francqui Chair 2009 at FUNDP and an IBM Faculty Award in 2011. He is chairholder of the PricewaterhouseCoopers Chair on E-Business at KU Leuven, co-chairholder of the Microsoft Research Chair on Intelligent Environments and co-founder and president elect of the Benelux Association for Information Systems (BENAIS).
