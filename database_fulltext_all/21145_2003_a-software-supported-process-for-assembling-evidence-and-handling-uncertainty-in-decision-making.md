---
otero_id: 21145
otero_key: "94W7E29N"
title: "A software-supported process for assembling evidence and handling uncertainty in decision-making"
authors: "John P. Davis; Jim W. Hall"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00117-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A software-supported process for assembling evidence and handling uncertainty in decision-making

John P. Davis \*, Jim W. Hall

Department of Civil Engineering, University of Bristol, Queens Building, University Walk, Bristol BS8 1TR, UK

Received 1 December 1999; accepted 1 March 2002

## Abstract

Complex socio-technical decisions, such as infrastructure investment decisions, are based on large quantities of evidence assembled and manipulated by multi-disciplinary teams. Information about decision options and future states of nature will often be ambiguous, incomplete or conflicting. In this article, a software-supported approach to assembling, structuring and representing evidence in a decision, based on hierarchical modelling of the processes leading up to a decision, is presented. Uncertainty in the available evidence is represented and propagated through the evidence hierarchy using Interval Probability Theory (IPT), providing a commentary on sources and implications of uncertainty in the decision. Case studies in the oil and civil engineering industries demonstrate how the approach has helped to develop shared understanding of the implications of uncertainty. It has enabled experts to externalise their knowledge and has facilitated discussion and negotiation. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Process modelling; Uncertainty management; Evidential reasoning; Interval Probability Theory; Decision suppor

## 1. Problem domain and research objectives

Engineering and infrastructure decisions have traditionally been a primary area of attention for hard and soft decision sciences and for decision support systems. The importance of these decisions in terms of economic, social, safety and environmental impact has been a powerful motive to improve decisionmaking. That success at tackling these decision problems has been mixed comes as no surprise given the complexity of the decision processes, the knowledge that informs the decisions and the institutional environments in which they are enacted.

Descriptive investigations of organisational decision-making processes [6,11,29,35,41] demonstrate that they are only loosely structured around the conventional stages of

1. problem definition;

2. definition of decision objectives;

3. generation and analysis of options;

4. choice of the preferred option;

5. implementation;

6. monitoring and feedback;

7. problem redefinition [28,46].

In practice there are often intermediate loops, sometimes with long delays between stages in the process, with previous stages being revisited before the choice of preferred option. Under some circumstances the problem has to be reframed in entirely different terms [49].

Major infrastructure investment decisions are a multi-disciplinary endeavour involving a complex set of technical, economic and environmental issues. Individuals will be engaged in cycles of decisionmaking in their own domain, which contribute to key points of commitment in the collective process. The processes of options analysis and evaluation can involve assembling and manipulating vast quantities of evidence. The evidence will appear in a range of formats, including dense numerical model results, textual evidence in technical reports, analogous cases, expert judgements, and perceptions and value judgements from the wider stakeholder group. In other words, the evidence appears at very different levels of granularity and does not lend itself to being compressed into a single coherent format. Whilst there may be a large volume of information relating to a decision, it is on the whole only of partial relevance, incomplete and sometimes conflicting.

Where a great deal of ignorance is inherent in the situation, a variety of decision-making approaches may be used in series, beginning with the simple and highly abstract, to screen out most of the possibilities before undertaking a comprehensive investigation of the few that remain. This helps to explain why later detailed study seems often merely to confirm an apparent predisposition in favour of a particular option [32]. Ultimately, the decision will be taken by an individual or small group not expert in all of the disciplines concerned. Major infrastructure investment decisions are taken relatively few times in any individual’s professional career, so there is a difficulty in using feedback to reinforce learning. Although analogies can be helpful in this respect, decision problems are so complex that identifying appropriate analogies is by no means straightforward.

A further characteristic of the domains being addressed is the growing awareness of the impacts of uncertainty and the need for improved decisionmaking. The quest for improved decision-making is being driven by intensifying organisational and cultural change. Decision-makers in both the public and private sectors are under great pressure to use resources efficiently. There are also increasing demands to identify and mitigate adverse impacts of infrastructure decisions. At the same time, inhouse expertise has been reduced due to down-sizing and out-sourcing of technical services. As a consequence, and also due to greatly improved communication and modelling technologies, decision-makers are facing intense information processing demands [16,25].

The aim of the research described in this article has been to address the recognised need for improved decision-making by supporting the problem framing and evidence gathering stages in decision-making, supporting and not replacing human judgement [1]. To that end, the following needs for decision support were specifically identified:

 to assemble evidence from diverse sources and represent it in a common and coherent model;

 to externalise expert judgements;

 to provide a commentary on sources and implications of uncertainty in the evidence;

 to facilitate dialogue between experts and other decision stakeholders.

There are three main elements to the approach, which are described in the following sections of this article. First, the process of assembling and manipulating evidence is structured in a hierarchical process model. Second, the attributes of the process are recorded at an appropriate level of detail in order to capture the available evidence in a common structure. Third, Interval Probability Theory is used to represent the uncertainty associated with each process meeting its objectives. The measures of uncertainty are then propagated up through the process hierarchy to give an assessment of the dependability of the overall process. In practice, this approach is only feasible with software to support model construction, knowledge gathering and uncertainty handling. The software-supported process is described in Section 4 of this article. Three case studies of the practical application in the oil and civil engineering industries are described in Section 5 and evaluated in Section 6. The article closes with a set of conclusions and reflections on the benefits of the proposed approach.

## 2. Hierarchical models of the processes leading up to a decision

To achieve the objectives of decision-support outlined above requires a structure for assembling evidence that is generally applicable, is intuitive to practitioners and provides a basis for logically sound and coherent uncertainty handling. It is proposed that modelling the processes that lead up to a decision provides such a structure.

A process is a purposeful activity, in the sense that it enacts a transformation. Process is a fundamental construct in the analysis of purposeful activities like engineering decision-making. The sub-processes that contribute to the decision, for example generating options or analysing future states of nature, can be thought of as inheriting their purpose from the overall decision-making process. This leads naturally to the concept of a hierarchically structured set of subprocesses leading up to a decision, which contribute to achieving the defined objectives of that decision.

The sub-processes that are the primary focus of the decision-support described in this paper are processes of assembling and manipulating evidence about the performance of decision options against the decision objectives. The transformation that these processes enact is one of transforming very diverse evidence, be it model results, analogies or expert beliefs, into measures of the expected performance of the options against the decision objectives. They are, therefore, primarily evidence handling processes. All of the evidence that decision-makers use when they make a choice originates from some such process, be it implicit or explicit. For the decision-making process to be successful, these sub-processes must also successful. In other words, the success of a decision can be assessed by analysing the processes of assembling and manipulating evidence in the lead-up to the decision.

There are several ways of representing a process, some of which are commonplace and others less so. Examples are a simple input–output-transformation model, a flow chart, a PERT chart and a critical path network. These are essentially models describing the relationships between events, usually through time. In complex dynamic situations, process modelling becomes practically impossible without computer support, and a number of tools are now available, such as IPSE 2.5 and its successor Process-wise [47,50], IDEF-0 [12], RAD [36] and ARIS [40]. In loosely structured decision-making situations, in which there are often many iterations towards a solution goal, workflow analysis, in which the progress of tasks is prescribed and always follows a certain path, has proved to be difficult to apply. The approach adopted here endeavours to develop a richer view of the evidence that is assembled in the lead-up to a decision, by not only looking at the data content and sequencing of that information, but also capturing meta-level reflections on its dependability.

At the top of the hierarchical structure used to capture the evidence-gathering processes that lead up to a decision is the high-level process representing the decision in hand. Associated with this process is a hypothesis that the process is successful. The underlying hierarchy accumulates evidence to support or refute the hypothesis. To do so the process is progressively disaggregated into sub-processes, which capture the different facets of evidence and analysis that have contributed to the high-level process (Fig. 1). The aim is to structure the problem in a way that forms the basis for logical thinking, rational debate and new insights into the decision problem. The hierarchical structure orders the large number of processes and quantity of information that the decision-maker is expected to assimilate, providing an overview and insights into those areas of the decision complex that are most influential. Each node in the graph has key items of information associated with it (Fig. 1):

![](/api/attachments/94W7E29N/fulltext/images/384e4403f5e27e125b0a6777ef4dc0e8bcd1b89a52391078311c7bad2be99412.jpg)  
Fig. 1. Structure of the hierarchical process model.

1. a process name;

2. a measure of uncertainty;

3. a set of attributes.

The process name and attributes are input by the user at each node. Uncertainty measures are input at the lowest levels in the hierarchy and then propagated through the hierarchy using numerical connectives that the user associates with each link. The mathematics of uncertainty propagation and practicalities of eliciting uncertainty measures are addressed in subsequent sections of this paper.

The process attributes serve several important purposes.

1. The process attributes clarify the process definition, stating the transformation that the process enacts and enabling it to be placed in the process hierarchy in a logical relation with its sub- and superprocesses and its neighbours.

2. The process attributes state the objectives (success criteria) of the process, providing the standard against which the dependability of the process can be assessed.

3. The process attributes capture key items of management information, which are fundamental to the process being successful. Examples are the process owner (who is responsible for delivering the process), the client (internal or external) for whom the process is being delivered, the time-scale and the resourcing.

4. The process attributes list items of evidence that provide arguments for or against the success of the process. This summary of relevant knowledge relating to the process provides the basis for subsequent uncertainty encoding and verification, providing an auditable record of the reasoning and rationale behind uncertainty assessments. Analysis of hazards (things which may harm the success of the process) encourages reflection on areas of weakness within the process and potential impacts should those hazards materialise.

![](/api/attachments/94W7E29N/fulltext/images/ccfce16a8df47834adf269969b4cfeaab3fdf0c7973abf82496a5907ce24ec03.jpg)  
Fig. 2. An example attributes list for a geophysical interpretation process.

Blockley [9] provides a comprehensive classification of process attributes. In any particular circumstance, the list of relevant attributes will vary. For example, Fig. 2 shows an attribute list from a tightly focussed geophysical interpretation process from the oil industry.

## 3. Uncertainty handling

The approach to uncertainty handling adopted is founded in the mathematical theory of evidence [30,44]. The aim is to provide a useful support to reasoning with uncertainty in complex socio-technical situations with vague and often incomplete evidence, areas where Bayesian theories of probability have been most challenged [26,31,45]. Several versions of evidence theory have been developed, through the structures of possibility theory [51], mass assignment theory [4] and random set theory [20,38,39]. In the current research, the aim was to use a relatively straightforward approach to evidential reasoning, called Interval Probability Theory (IPT) [14,24], which retains the desirable properties that have made evidence theory more attractive than conventional Bayesian approaches:

1. IPT represents in a fairly straightforward manner aspects of ambiguity, conflict, randomness and incompleteness in evidence. Aspects of fuzziness can also be conveniently captured through the adoption of hierarchical knowledge structures.

2. The axioms of IPT provide a balance between, on the one hand, not being so weak as to provide inferences that are of limited practical use, yet on the other hand, not artificially constraining the problem and under-estimating uncertainty.

3. IPT conveniently represents dependency relationships between evidence. Dependency is an important issue in complex evidential situations, so it is important that a mathematical syntax can easily represent different levels of dependency between evidence.

4. IPT can also capture a range of inferential relationships between levels in the evidence hierarchy.

Thus, although the objective of uncertainty handling and propagation is in common with more conventional Bayesian approaches [37], the mathematization is a significant departure from these approaches, offering the theoretical advantages outlined above. In practice, IPT can be implemented in a reasonably straightforward manner that is accessible to nonspecialist practitioners. This is a function of the user-friendliness of the software implementation, but is also a consequence of the mathematization itself.

IPT is closely related to probability theory, but, in common with basic probability assignments, belief and plausibility measures and mass assignments, it is not necessary to exclusively allocate probability to a conjecture or its negation. Thus, if E is a proposition

$$
p (E) \in [ S _ {n} (E), S _ {p} (E) ]
$$

where $S _ { n } ( E )$ is the lower bound, and $S _ { p } ( E )$ is the upper bound of the probability $p ( E )$ . The negation is

$$
p (\overline {{E}}) \in [ 1 - S _ {p} (E), 1 - S _ {n} (E) ].
$$

If, as here, an interval probability is interpreted as a measure of belief, then $S _ { n } ( E )$ represents the extent to which it is certainly believed that E is true or depend-<sub>\_</sub> able, $1 - S _ { p } ( E ) = S _ { n } ( \overline { { E } } )$ represents the extent to which it is certainly believed that E is false or not dependable, and the value $S _ { p } ( E ) - S _ { n } ( E )$ represents the extent of uncertainty of belief in the truth or dependability of $E .$ Three extreme cases illustrate the meaning of this interval measure of belief:

$p ( E ) { \in } [ 0 , 0 ]$ represents a belief that $E$ is certainly false or not dependable,

$p ( E ) { \in } [ 1 , 1 ]$ represents a belief that E is certainly true or dependable, and

$p ( E ) { \in } [ 0 , 1 ]$ represents a belief that E is unknown.

## 3.1. Dependency

Interval representation is implicit in many interpretations of evidence theory, notably the Dempster –

Shafer theory of evidence [17,44]. An interval representation is also a natural consequence of dealing with families of probability distributions [3,4] and forms the basis of Support Logic Programming [7,10]. Cui and Blockley [14] developed previous work by introducing the parameter $\rho ,$ which represents the degree of dependence between propositions $E _ { 1 }$ and $E _ { 2 } \mathrm { : }$

$$
\rho = \frac {p (E _ {1} \cap E _ {2})}{\min (p (E _ {1}) , p (E _ {2}))}.
$$

Thus, $\rho = 1$ indicates that $E _ { 1 } \subset E _ { 2 }$ or $E _ { 2 } \subset E _ { 1 }$ (i.e. they are nested propositions), whilst if $E _ { 1 }$ and $E _ { 2 }$ are independent

$$
\rho = \max (p (E _ {1}), p (E _ {2}))
$$

so that

$$
p (E _ {1} \cap E _ {2}) = p (E _ {1}) p (E _ {2}).
$$

The minimum value of $\rho$ is given by

$$
\rho = \max \left[ \frac {p (E _ {1}) + p (E _ {2}) - 1}{\min (p (E _ {1}) , p (E _ {2}))}, 0 \right]
$$

where $\rho = 0$ indicates that $E _ { 1 }$ and $E _ { 2 }$ are disjoint. If $\rho$ is defined as an interval $[ \rho _ { l } , \rho _ { u } ]$ then

$$
S _ {n} (E _ {1} \cap E _ {2}) = \rho_ {l} \min (S _ {n} (E _ {1}), S _ {n} (E _ {2}))\tag{1}
$$

$$
S _ {p} (E _ {1} \cap E _ {2}) = \rho_ {u} \min (S _ {p} (E _ {1}), S _ {p} (E _ {2}))\tag{2}
$$

$$
\begin{array}{c} S _ {n} (E _ {1} \cup E _ {2}) = S _ {n} (E _ {1}) + S _ {n} (E _ {2}) \\ - \rho_ {l} \min (S _ {n} (E _ {1}), S _ {n} (E _ {2})) \end{array}\tag{3}
$$

$$
\begin{array}{c} S _ {p} (E _ {1} \cup E _ {2}) = S _ {p} (E _ {1}) + S _ {p} (E _ {2}) \\ - \rho_ {u} \min (S _ {p} (E _ {1}), S _ {p} (E _ {2})). \end{array}\tag{4}
$$

These relationships constrain the distribution of probability across the space occupied by $E _ { 1 }$ and $E _ { 2 } .$ . The probability distribution will not be uniquely defined under all circumstances, but a convex family of probability distributions can be defined and the bounds on the probability of any given sub-set can be readily extracted [24]. This approach for establishing the probability assignments to the power set of the universe of discourse can be extended to apply to three or more propositions, given the constraints of interval measures of belief in each proposition and pair-wise assignments of the dependency measure $\rho .$

The dependency parameter $\rho$ is an additional item of information, which is elicited in order to explicitly address the issue of dependency between propositions. It is a convenient means of exploring different dependence relationships when the exact nature of dependency is uncertain. The dependence parameter generalises, in a way analogous to T-norms [43], other inference rules that assume a specific dependency relationship.

## 3.2. Logical inference

The next step is to address the relationship between propositions $E _ { 1 } , E _ { 2 } , . . . , E _ { n }$ and some hypothesis, $H ,$ to which they relate. $E _ { 1 } , E _ { 2 } , . . . , E _ { n }$ partition the universe of discourse into j mutually exclusive and collectively exhaustive sub-sets, $\theta _ { 1 } , ~ \theta _ { 2 } , . . . , ~ \theta _ { j } ,$ where $j = 2 ^ { n }$ . A relatively straightforward solution to measuring the degree of support for H is based on the total probability theorem, which in this context is usually thought of as Jeffrey’s rule of conditioning [27,37,42]. The total probability theorem is axiomatic in probability theory:

$$
p (H) = \sum_ {i = 1} ^ {j} p (H \mid \theta_ {i}) p (\theta_ {i}).\tag{5}
$$

Jeffrey’s rule uses this structure as a method of estimating the degree of belief in a hypothesis, given inconclusive evidence about some propositions that influence H. Here $p ( H | \theta _ { i } )$ is the probability of $H ,$ as if $\theta _ { i }$ were true. $p ( \theta _ { i } )$ represent uncertain belief in $\theta _ { i } ,$ given available information $e .$ The situation, expressed in these terms, is represented by the Bayes conditionalization formula [37]

$$
p (H \mid e) = \sum_ {i = 1} ^ {j} p (H \mid \theta_ {i}, e) p (\theta_ {i} \mid e).
$$

Application of Jeffrey’s rule requires that the hypothetical probability $p ( H | \theta _ { i } )$ is conditionally independent of the information $e$ that which happens to be available at any given instance, i.e.

$$
p (H \mid e) = \sum_ {i = 1} ^ {j} p (H \mid \theta_ {i}) p (\theta_ {i} \mid e)
$$

The probabilities $p ( \theta _ { i } | e ) ~ ( i { = } 1 ~ \mathrm { t o } ~ j )$ are derived, as outlined above, from (equivocal) judgements of belief in $E _ { 1 } , E _ { 2 } , . . . , E _ { n }$ on the basis of available evidence $e$ and the dependencies between $E _ { 1 } , \ E _ { 2 } , . . . , \ E _ { n }$ The hypothetical probabilities $p ( H | \theta _ { i } )$ determine the relationship between the $\theta _ { i } \mathrm { ~ s ~ }$ and $H .$

Consider the case in which $n = 1$ , so the space of propositions is partitioned between two subsets E and<sub>\_ \_\_</sub> ${ \dot { \overline { { E } } } } , { \dot { 1 } } . { \mathrm { e } } . \ \theta _ { 1 } = E$ and $\theta _ { 2 } = \overline { { E } }$ and

$$
p (H) = p (H \mid E) p (E) + p (H \mid \overline {{E}}) p (\overline {{E}}).\tag{6}
$$

Dubois and Prade [19] showed that when all the terms are expressed as intervals, the bounds on $p ( H )$ are as given in Equations (7) & (8).

The conditional probability terms (corresponding to the $p ( H | \theta _ { i } )$ terms in Eq. (5)) are a feature of the structure of the inference problem. For example, $E$ may be a necessary condition for $H ,$ in which case

$$
p (H \mid E) \leq 1 \quad p (H \mid \overline {{E}}) = 0,
$$

or E may be a sufficient condition for H, in which case

$$
p (H \mid E) = 1 \qquad p (H \mid \overline {{E}}) \leq 1.
$$

In the special case when E is a necessary and sufficient condition for H

$$
p (H \mid E) = 1 \qquad p (H \mid \overline {{E}}) = 0.
$$

A weaker and more general condition is when E is relevant or partially sufficient to $H ,$ in which case

$$
0 <   p (H \mid E) \leq 1 \quad 0 \leq p (H \mid \overline {{E}}) \leq 1.
$$

Hall et al. [24] provide a worked example of the inference calculation for $n = 2$ and explain how the bounds on $p ( H )$ can be found in the general case.

To operate this inference mechanism, the user has to input

1. n interval probabilities $p ( E _ { 1 } ) . . . p ( E _ { n } )$ representing the uncertainty in each item of evidence;

2. pair-wise dependency parameters $\rho$ (also expressed as intervals), i.e. for n items of evidence $n ! / 2 ( n - 2 ) !$ interval values of $\rho ;$

3. $2 ^ { n }$ conditional probability measures $p ( H | \theta _ { 1 } ) . . .$ $p ( H | \theta _ { j } )$ (also expressed as intervals).

For higher order evidential situations, the number of judgements required from the user can become rather onerous, so some of the measures can be approximated:

1. Rather than using interval values $[ \rho _ { l } , \rho _ { u } ]$ of the dependency parameter $\rho ,$ a point value can be used.

2. Rather than using pair-wise assignments of $\rho$ in order to populate a dependency matrix, a single value can be used to approximate the level of dependency between the whole body of evidence.

3. Rather than assigning the full $2 ^ { n }$ conditional probability measures, it is possible to use only two measures for each item of evidence $p ( H | E _ { i } )$ and $p ( H | \overline { { E } } _ { i } )$ (i.e. 2n measures). The former is thought of as a measure of the sufficiency of each item of<sub>\_\_</sub> evidence. $1 - p ( H | \overline { { E } } _ { i } )$ is thought of as a measure of the necessity. The number of judgements can, if appropriate, be further reduced by using point measures rather than interval measures.

$$
\left. \begin{array}{l l} S _ {n} (H) = S _ {n} (H \mid E) S _ {n} (E) + S _ {n} (H \mid \overline {{E}}) (1 - S _ {n} (E)); & S _ {n} (H \mid E) \geq S _ {n} (H \mid \overline {{E}}) \\ S _ {n} (H) = S _ {n} (H \mid E) S _ {p} (E) + S _ {n} (H \mid \overline {{E}}) (1 - S _ {p} (E)); & \text {otherwise} \end{array} \right\}\tag{7}
$$

and

$$
\left. \begin{array}{l l} S _ {p} (H) = S _ {p} (H \mid E) S _ {p} (E) + S _ {p} (H \mid \overline {{E}}) (1 - S _ {p} (E)); & S _ {p} (H \mid E) \geq S _ {p} (H \mid \overline {{E}}) \\ S _ {p} (H) = S _ {p} (H \mid E) S _ {n} (E) + S _ {p} (H \mid \overline {{E}}) (1 - S _ {n} (E)); & \text {otherwise} \end{array} \right\}\tag{8}
$$

In the first two cases, the calculus of IPT can be used exactly as explained above. All that is being done is that some of the measures are assigned the same value. The conditional probability assignments in the third case do not uniquely specify which weights should be applied to each sub-set in the body of evidence, but it is possible to identify an approximate inference given the available information. This demonstrates the attraction of an intervalbased approach. Even if the problem is under-specified it is still possible to develop bounds that are consistent with the information that is available. The compromise here is between complexity and precision, whereas in Bayesian belief networks the compromise is between complexity and (sometimes inappropriate) assumptions of conditional independence [48]. As more information becomes available it can be used to develop tighter bounds on the inference.

## 4. A software-supported methodology for process modelling and uncertainty handling

The principles of process-based hierarchical structuring of evidence and uncertainty handling using Interval Probability Theory, described above, have been implemented in an MS Windows-based software package called JUNIPER. JUNIPER is currently being used in a number of trial applications in the oil and gas, and water sectors. The prototype software was tested for robustness, usability and for the intuitive behaviour of the uncertainty calculus at a two-day workshop involving 25 representatives from industry. The representatives were leading experts in their fields, some of whom were mathematicians with a keen interest in the rigour of the approach. The results of the workshop were very encouraging and the researchers were subsequently invited to conduct case studies in a number of the companies represented. The results of a selection of these case studies are presented later in this article.

The main steps in constructing and using a hierarchical process model to support a practical decision problem are as follows:

1. motivating and developing conceptual understanding;

2. developing the model structure;

3. entering process attributes and linking to relevant knowledge bases;

4. quantifying the structure by adding conditional probabilities and dependencies;

5. developing interval-based measures of evidence;

6. interpreting the results and engendering organisational learning.

These steps correspond closely to the procedure for quantifying judgmental uncertainty recommended by the decision analysis group at Stanford Research Institute [34]. The SRI methodology is aimed at eliciting judgements of uncertainty from individuals and groups within organisations. The correspondence between the process proposed here and the SRI methodology emphasises the importance of the psychological and organisational processes surrounding the use of the JUNIPER decision support tool.

In practice, JUNIPER has been used in a reflective learning mode [8,9,18], which is rather more complex than the six steps listed above and discussed below suggest. The process of model construction tends to inspire a range of insights and reflections, which may need to be recorded as informal memos to be revisited and incorporated in the model in a formal way at an appropriate moment. The model structure often has to be revisited once the users have reflected on the nature of the evidence gathering process and the way it contributes to the decision in hand. Some judgements of uncertainty, conditional probability or dependency may have to be revisited once the model has been completed to ensure balanced and coherent judgements across the model.

## 4.1. Step 1: motivating and developing conceptual understanding

Decision-makers in the problem domains being addressed are on the whole motivated by the need for improved decision-making. However, they need to be convinced that the expected improvements in decision-making outweigh the resource cost (which is often the opportunity cost of not using alternative methods) of any given approach. Evidence of ease of use and speed of model construction (an issue which is revisited in the discussion of the case studies) can help to overcome reservations about the resources involved.

Examples of previous effective use have been a convincing motivating mechanism, particularly when presented by colleagues rather than outsiders. The motivating effect has been particularly potent when senior managers have been shown to be convinced by the proposed approach, when other techniques have failed to communicate the issues that domain experts consider to be substantive. Meanwhile, the user’s motivational biases should be explored in order to expose issues that may influence their judgements of model structure and uncertainty [34].

Before embarking on model construction, the user should have some conceptual understanding of the reasons for a hierarchical model structure and the principles of an interval representation of uncertainty. The user should understand the importance of uncertainty and how it is accounted for in JUNIPER. These principles are communicated through a simple on-line tutorial, but as with any learning process, will be revisited and reinforced as the user becomes more proficient and insightful in the way they apply the concepts embodied in the JUNIPER tool. Contextsensitive help embedded in the tool supports this growing conceptual understanding.

## 4.2. Step 2: developing the model structure

The form of an example hierarchical model is shown in Fig. 3. The model comes from a real case study and it should be noticed that in this case only a few levels of the hierarchy were needed to describe the problem. The hierarchical structure is constructed by working downward from the top process to an appropriate level of definition, using a conventional ‘drag and drop’ interface. The user has to associate a process label with each of the processes. Use of the present participle—words ending in ‘ing’—stresses that each object in the hierarchy is a process.

![](/api/attachments/94W7E29N/fulltext/images/97b3df41a7e36fd8e20e60b0eee6b8b015069fc55ddfb4963007b52e15012dd1.jpg)  
Fig. 3. Overview of a hierarchical process model with graphical interval-based uncertainty representation.

The top-level process represents the decision process in hand, for example, ‘‘developing DNW oil field’’ or ‘‘protecting the Lincolnshire coast from flooding’’. This top-level process is then progressively disaggregated into sub-processes that contribute evidence about the success of the super-process. These sub-processes are elicited by asking the user ‘‘what sub-processes are required to ensure the success of the super-process?’’ or in other words ‘‘what do we do to make the process happen?’’ To establish a coherent structure, it is important to ensure that it is processes that are modelled rather than events, tasks or data flows.

The process model is disaggregated to a level at which the processes are sufficiently precisely defined to add numerical measures of their dependability. The motive for disaggregation is to expose the multiple facets of the decision complex, which the expert would not necessarily consider if they were making a high level judgement [21]. Disaggregation can be used to combat motivational bias by working at a level of detail that makes the expert’s judgements remote from their (high-level) personal interests [34]. Moreover, it has been suggested that the opportunity for incoherent judgements is far less when subjective probabilities are obtained in disaggregated structures [21].

## 4.3. Step 3: entering process attributes and linking to relevant knowledge bases

Each process is clarified by entering the process attributes (Fig. 4). The types of issues that can be captured in the attributes list were discussed in Section 2 and illustrated further in Fig. 2. The attributes capture the arguments for and against success of the process, which form the basis for developing numerical measures of uncertainty. They thus externalise the reasoning behind the expert’s numerical measures of uncertainty and provide a mechanism for subsequent self, peer and external scrutiny and appraisal of the judgements and of the derived uncertainty measures higher in the model.

The attributes window also contains electronic links to relevant knowledge bases and computer applications. In this way, the JUNIPER model provides a hub for evidence from a range of sources relevant to the decision in hand, structured around to the decision-making processes.

![](/api/attachments/94W7E29N/fulltext/images/c5119aa9be92b981bb7698f61b7bad16b560e49a335c508fa83537f08a5c557a.jpg)  
Fig. 4. Example attributes window.

## 4.4. Step 4: quantifying the structure by adding conditional probabilities and dependencies

The links between processes in the model structure signify a relationship of relevance. The strength of this relationship between sub-processes and the superprocess is quantified by applying conditional probabilities to the links in the network. The dependency relationship between the sub-processes linked to a given super-process is estimated using the parameter $\rho .$ This judgement of belief in the strength of the inferential relationships is done before the intervalbased belief estimates are entered in Step 5, helping to separate the expert’s judgement of relevance from their strength of belief in the available evidence.

## 4.5. Step 5: developing interval-based measures of evidence

The user inputs their interval measures of evidence for and against the success of the process at the base of the hierarchy and the calculus propagates this information up to give an expression of the depend ability of the super-processes. Disaggregation enables experts to make judgements on aspects with which they are more familiar, rather than having to judge the emergent behaviour of the whole decision complex. It should be clear from the discussion of uncertainty handling in Section 4 that IPT is used as a measure of evidence, rather than the more conventional mode of using subjective probability to estimate the probability of (often one-off) events. It is in the latter case that many of the well-known biases in subjective probability assessments appear most strongly [2]. Indeed in the context of the Dempster –Shafer theory of evidence, to which IPT is closely related, subjects once trained have been shown to cope effectively with the measurement of evidential support and make consistent assessments [15].

The interval probability expressions are input graphically. A dialogue box is used for the input of the interval measure by dragging sliding coloured bars. Fig. 5 shows the graphical mapping of $S _ { n }$ and $S _ { p }$ on the [0,1] scale with the left hand bar coloured green (evidence for the success of the process) and the right hand end coloured red (for evidence against the success of the process). The numerical values are also available in the dialogue box.

![](/api/attachments/94W7E29N/fulltext/images/f5c87248333470c0e1b3932f74e11c72da0cae6cd056ef10e8ec7d617c1dcee8.jpg)  
Fig. 5. Window for entering and editing interval probability measures.

## 4.6. Step 6: verification, interpretation and organisational learning

The calculated interval probabilities for each process are displayed in graphical form at the bottom of each of the process boxes on the process model (Fig. 3). Thus, on a single page the user can readily review the model and identify areas of vulnerability, doubt and confidence. The overview provides a quick check of the coherence of the model and provides an opportunity for users, individually and collectively, to reflect on whether it does justice to their beliefs, state of knowledge and uncertainty. If not, the user can revisit their judgements to address areas of conflict or incoherence. The consistency of the model can be checked by comparing calculated probabilities with the items of evidence listed as attributes, which are obtained at every level in the model. Errors in judgement of uncertainty and accumulating evidence become apparent when the calculated uncertainty measure is not consistent with the listed evidence for and against the success of the process. Further verification can be achieved by revisiting the model after a period of reflection or independently reconstructing it, perhaps using a different approach to knowledge elicitation, to test repeatability.

The modelling process does not provide a prescriptive answer to the decision problem. Rather it provides the experts with a model of the process through which they are moving, which enables them to develop collective understanding and to communicate that understanding, the expectation being that the decisions that subsequently follow will be based on a sounder view of the evidence available. Further insights can be gained by exploring the sensitivity of the high-level uncertainty measures to incremental changes in the uncertainty of sub-processes.

## 5. Case studies

Application of the proposed approach in practice is now illustrated through examples of case studies. Case studies were used to

 evaluate the benefits and disadvantages of the proposed approach;

 develop a set of cases that could be used to demonstrate the proposed approach and initiate future users;

 identify areas where new users are in need of help and guidance;

 identify problems to be addressed in future phases of development.

It should be clear by now that the aim of the proposed approach is not to prescribe a preferred decision option, but rather to

 externalise expert knowledge in a structured and accessible way;

 improve communication;

 encourage reflection on sources and implications of uncertainty in the available evidence;

 enable organisational learning;

and thus to improve decision-making.

Evidence regarding the extent to which these aims have been achieved originates from the individuals and organisations who participated in the studies and is captured in terms of their opinions and reflections gained from interviews, a workshop and questionnaire feedback. The decisions being addressed in the case studies were all unique, complex, major infrastructure development decisions, so quantitative studies of decision-making effectiveness over a series of decisions was not feasible, a problem that is common to evaluation of decision analysis in general [21]. However, effectiveness could be measured in terms of the perceived confidence with which the decisions were taken, and the levels of consensus reached compared with analogous situations in the past. The resource implications of the proposed approach were quantitatively assessed.

A range of strategies for participant involvement were adopted during the case studies. At one extreme, the domain experts were interviewed by a researcher using the semi-structured interview approach of Grounded Theory [23] to elicit knowledge. Documentation relating to the study was assembled by the researcher. The researcher then constructed the model using these evidence sources. The model was subsequently reviewed by the domain experts and adapted until they were happy that it was a true reflection of their perception of the decision situation. These researcher-driven studies helped to inform the research team directly about the practicability of the approach. However, they provided less insight into the level of conceptual learning required by newcomers to the approach and into the surrounding organisational issues. At the other extreme were case studies in which the domain experts were provided with the decision support tool JUNIPER to use independently, having previously been trained by the researchers. The experts were subsequently interviewed separately and then as a team to obtain feedback on the effectiveness of the approach. The intermediate study approach was for the researchers to work jointly with the domain experts in a range of decision-making situations. This enabled the researchers to become engrossed in the problem domain, yet also to query assertions and judgements made by the domain experts. As well as being the most effective way of eliciting expert knowledge whilst controlling biases in uncertainty judgements [13,34], this joint mode of working also proved to be the most effective for evaluation purposes.

Of the several case studies undertaken, three are reported here as narratives. The studies were conducted in two different sectors of industry. The first two studies were conducted in international oil companies, the third with the UK Environment Agency.

## 5.1. Study 1: a decision on whether to drill an oil well

During the development of a major oil field a decision had to be made on the potential to exploit other local sites that may or may not have borne oil. The success of the process depended on establishing that oil was present and then successfully extracting it by designing a well appropriate for the conditions (Fig. 3). Information about the site was sparse and from indirect sources.

An initial process model of the problem was constructed by the domain experts working in collaboration with the researcher. The model formed a focus around which the team pursued high quality debate about the nature and value of the scarce data upon which they had to base their decision. The lower bound of the interval number associated with the top process in the first version of the model came very close to a subjective probability assessment conducted previously within the organisation. This built confidence at an early stage in the study and provided some calibration of the disaggregation and recombination. However, the JUNIPER tool was adopted in preference to the previous approach because it was more user-friendly and could be quickly modified as new evidence appeared. The uncertainty values in the model update dynamically as the inputs are changed so that the team was able to do primitive sensitivity analysis of the sources of the most significant uncertainties.

The JUNIPER model was subsequently updated as the decision-making process proceeded. For instance, there were branches on the model indicating the relevance of the types of rock present, representing the processes of assessing the rock strata and of assessing the likelihood of a given type of rock being oil bearing. Part way through the study, significant oil was found in a rock type not previously considered important, enabling the model to be updated. At least six different iterations of the basic process model were generated as new data arrived. This formed a useful record of the evolution of the decision.

As part of the investigation, a geochemical analysis was undertaken to try to reduce the uncertainty associated with the oil migration path. The analysis revealed strong evidence that the oil in a neighbouring stratum must have passed through the area in question. The researcher therefore increased the evidence for that migration path, but this only had a minor effect on the uncertainty in the top process of the model. By this stage in the study the domain experts had decided to proceed with the exploratory well on the basis of the geochemical evidence, displaying strong recall availability bias. The well was drilled and found not to contain oil. If the team had scrutinised the updated JUNIPER model before making the decision, rather than as a shadow study, it would have encouraged rather more critical reflection on the decision. The model did provide a useful focus for analysing what went wrong in this particular decision process. Indeed the main conclusion of this study was that the approach gave the team a realistic assessment of their state of knowledge and provided a platform for externalising and debating that knowledge. It showed that subjective biases were brought to light by the structuring of the evidence in a process model.

## 5.2. Study 2: a choice of which oil field to drill

A second case study involved the comparison of two distinct oil fields. The decision related to which of the two fields should have resources expended on them for development and what form that expenditure should take. For the first field, the development process was owned by a partnership of companies. The data was complex and provided rather incomplete evidence about the prospect. One of the partners wanted to collect more seismic data, whereas the other partner wanted to either abandon the prospect or go straight to an exploratory drill.

The evidence was assembled in a process model. The top process was ‘drilling the field’. In other words, its objective was to determine if the decision to drill would lead to a successful outcome. The geologists and geophysicists found the approach using the JUNIPER software an intuitive and natural way to describe the situation. The models, together with their attribute lists, were produced in about four man-hours of expert time. The constructed models reinforced the previously held intuitive view that the available evidence was inconclusive. Interval representation of uncertainty effectively communicated the inconclusive nature of the evidence.

Next, the model was used to explore what would happen if the decision were made to obtain more seismic data. The team identified processes that would be affected by new evidence coming from new seismic data. The data could be either encouraging or discouraging in terms of the potential of the oil field. These two situations of new evidence flow were modelled by simply altering the evidence for and against in the identified processes. This demonstrated that the new evidence did not significantly affect the uncertainty in the overall process. This kind of value of information study, while not going into the financial precision of a conventional Bayesian approach, provided a clear argument at an appropriate level of detail for the decision to be taken.

The second oil field in this second case study had a licence obligation to drill. However, the team felt that the evidence, although complex, suggested that it was not worth drilling this field. The question was how to demonstrate this to managers. The overall process model produced contained 30 processes, fitting on a single sheet of paper. Graphical representation of evidence for and against the success of the processes could be seen at a glance. This enabled the team to communicate to managers quickly and concisely where the problems lay. A decision was made based on transparent reasoned arguments, when previously the teams involved had been unable to make a decision because of the complexity of the evidence. They also felt confident enough to defend the decision to their business partners.

## 5.3. Study 3: a decision to abandon a seawall

The third case study addressed public investment in an environmentally sensitive infrastructure project at an estuary site on the East Coast of the UK. The decision was how to deal with the problem of decaying coastal defences. To avoid the high cost of repair it was decided to abandon the defences and retreat the defence line inland. This had the added benefit of reinstating an area of marsh habitat. The scheme was designed based largely on the experience of the experts involved, supported with some quantitative analysis carried out by consultants. The uncertainty analysis was conducted retrospectively by the researchers, to assess the dependability of the process of choosing to implement the retreat project rather than any of the other options.

Fig. 6 shows the high level process in the process model. The model was constructed using documented evidence in the form of reports and correspondence relating to the project, together with testimony of the engineers involved. On the basis of this evidence, the support for the top process of ‘‘choosing an appropriate flood defence’’ was calculated to be [0.05, 0.75] which represents rather low dependability with low confidence in that assessment. The uncertainty model therefore demonstrated that there was substantial uncertainty in the overall process of choosing an appropriate defence option, when this was not made clear in the documentation relating to the project.

The process of choosing an appropriate flood defence was a function of four principle criteria. The chosen option had to be sound in engineering terms, economically efficient, environmentally sound and sustainable, and politically acceptable. Uncertainty in each of these processes contributed to the overall uncertainty in the decision on which scheme to implement. Exploration of the model, which contained 117 processes, demonstrated that the main reason why the dependability of the top process was calculated to be low was because of the low support for the economic appraisal process, which had a great influence on the overall dependability of the decision making process.

![](/api/attachments/94W7E29N/fulltext/images/bf889e66aaf7e16960dadbfd264631927bd1be8600a9a34e5ce4845c6099d700.jpg)  
Fig. 6. High level processes in process model of case study 3.

The economic appraisal was found to have dependability [0.03, 0.60]. The lower bound on this interval was a dominant influence on the lower bound of the top process.

Construction and use of the uncertainty model forced reflection on how the different activities and studies that had been undertaken contributed to the strategic decision to implement the project. The process model revealed considerable disequilibrium in the depth of analysis contributing to the four high-level processes. In some aspects of the project, very detailed analysis had been conducted, though this sometimes made no contribution to reducing uncertainty in the decision process. Much less effort to reduce uncertainty had been applied in other more critical areas. The final model structure was confirmed by the Environment Agency’s project manager to be a good representation of the processes leading up to the strategic decision. It proved to be of value by highlighting the levels of uncertainty in the decision, identifying the sources of uncertainty and communicating these insights across disciplines.

## 6. Evaluation of case studies

## 6.1. Conceptual learning

In the case studies where the researchers were working with the domain experts, it was possible to monitor the interpretation they were placing on the model, through analysis of their discourse and by challenging them on their behaviour during model construction and interpretation. Users rapidly developed a basic conceptual understanding of the process modelling and uncertainty handling techniques, so after support with constructing the first model, users were able to construct their own models. However, it was noted that users quickly developed their own interpretation on the model structure. On the one hand, this flexibility enabled them to use the model to articulate concepts that they considered to be of importance. On the other hand, when it led to incoherent structures, the users had to be encouraged to reflect upon the meaning they were attaching to the model structure. Similarly, quite rich interpretations were placed on the mathematization of uncertainty, which to some extent can be seen as a strength of the approach, provided that the interpretation was not inconsistent with the underlying axiomisation.

6.2. Representing uncertainty using probability intervals

The use of an interval representation has proved to be a useful way of capturing the evidence-based reasoning that characterised the decision-making processes in the case studies. The domain experts were familiar with the conventional use of subjective probability, but found interval probabilities to provide a more expressive way of representing their confidence or uncertainty in their beliefs. IPT allows the evidential support for a conjecture to be separated from the support for its negation, in particular allowing users to express high levels of uncertainty very succinctly and avoid spurious precision. This concurs with previous research, which has demonstrated that in inconclusive situations, when given the opportunity, subjects tend to withhold belief, allocating it to uncertainty [15].

Many of the experts in the case studies were familiar with statistics, so some explanation was required to emphasise that IPT was being used to support evidential reasoning rather than statistical reasoning. In the domains being addressed, statistical evidence was available only for some of the subprocesses and, because of the unique nature of each decision, was not directly applicable to the decision as a whole. An evidential mode of reasoning was therefore more applicable. An unambiguous statement that the interval measures were being used in this mode helped to remove some of the confusion between evidential and statistical reasoning, which has been identified as the source of some of the well-known biases in human probabilistic reasoning [5].

Experts readily adapted to the process of listing the evidence upon which their assessments of uncertainty were based and encoding these as uncertainty measures. The most common approach constructing probability intervals was to consider the lower bound $( S _ { n } )$ on the probability interval to represent the weight of evidence supporting the hypothesis in question, whilst they used the necessary evidence for the negation $( 1 - S _ { p } )$ to represent the weight of evidence against the hypothesis. This representation mapped conveniently onto the expert’s commonly observed mode of discourse and technical debate, which was characterised by exchange of arguments and counter-arguments, a mode of reasoning that is quite commonly observed amongst professional decision-makers [22].

## 6.3. Graphical representation of probability intervals

Graphical representation of interval probabilities using green, white and red bars was identified by many users as being one of the attractive features of the decision-support tool. Indeed the notation of the ‘Italian flag’ rapidly entered the vernacular of the participating organisations. The capacity to drag the coloured bars when constructing interval probability estimates enabled immediate feedback on the size of belief, in a much more visual way than verbal or numerical mechanisms.

Graphical representation of uncertainty in each process meant that the constructed process model provided an instant overview of the strength, weakness and uncertainty in the total body of evidence that contributed to the decision. For example, in the third case study, the overview of uncertainty measures provided an immediate demonstration to the decision-makers that the risk assessment aspect of the economic appraisal was the main source of uncertainty in the processes that had led up to the decision.

## 6.4. Demonstrating value of information issues

In all of the studies, the model was used to assess the sensitivity of the estimated uncertainty in the decision process to different types of information that were potentially available. This was supported by the software, which updates the interval measures across the model while any particular process is being changed. Although of value, these demonstrations of sensitivity and value of information only provide a means of comparing the impact of different information scenarios (including the current situation). They do not provide a direct monetary measure of the value of information, in the way that Bayesian analysis does [33]. However, in the ‘open world’ problems addressed in the case studies, it is very difficult to estimate a priori what the impact of new information may be. It can have the effect of entirely reframing the decision problem. Therefore, in these situations, a comparative estimate of the value of information may be all that is reasonably justifiable.

## 6.5. Promoting communication and organisational learning

In the first two case studies reported here and others conducted within the collaborating organisations, the process model provided a focus for high quality constructive debate and learning about the problem in hand. The model itself ‘faded into the background’. By forcing experts to externalise their judgements, it enabled an exchange of opinions and arguments, leading to a clearer understanding of the decision. The users identified this catalytic effect as being one of the main benefits of the approach. Of course, JUNIPER is by no means the only decision support tool that can have this beneficial effect of structuring a problem in a collective domain. However, the combination of interval-based graphical representation of uncertainty and rapid model construction (which is discussed below) does represent a development on existing approaches.

An aspect of communication that was noted in all of the case studies was the instant overview of the decision problem that a JUNIPER model provided. Decision-makers (usually senior managers) who had not engaged in the technical debate surrounding model construction used the model to assimilate knowledge about the problem domain and to interrogate their experts about areas of uncertainty. This communication mechanism was valued both by senior managers, who valued the speed of assimilation, and domain experts, who valued the ability to highlight the impact of substantive issues, which in the past they may have struggled to articulate in a succinct and convincing way. For the oil field studies, users commented that whereas it conventionally took a morning to make a presentation on the state of a prospect, using the output from the model an overview could be given in well under an hour.

## 6.6. Capturing qualitatively diverse and multi-attribute aspects of a decision

The case studies demonstrated how process models could be used to capture qualitatively diverse aspects of a decision. This was of particular value in the third case study reported here. Conventionally in UK flood and coastal defence, the economic, environmental and technical aspects of scheme have been pursued in parallel and then presented separately to decisionmakers and regulators. The process model provided a platform for providing a common overview of the sources of uncertainty in these qualitatively different processes. As with any multi-attribute decision-making problem, this involved developing measures of the relative contribution that different aspects of the problem made to the overall uncertainty, and these measures will always be open to challenge and debate. The high-level conditional probability measures that bring together the different aspects of the problem are much more difficult to assign than measures that connect more logically structured low-level processes. However, the approach does have the merit of being readily useable, which means that it can usefully inform the value-based debate that often surrounds multi-attribute decision-making. On the other hand, the computations are not particularly accessible to decision-makers and other stakeholders unfamiliar with probability theory, so the approach can be criticised for lack of transparency.

## 6.7. Providing a mechanism for storing, auditing and retrieving decision processes

The process models and associated electronic information that could be embedded in them, provided a convenient mechanisms for storing and retrieving knowledge and case histories. In case study 1, the various versions of the model provided a record of the dynamics of the, ultimately unsuccessful, decisionmaking process. The processes that led up to the decision, in particular the biased use of the geochemical evidence, could be traced.

## 6.8. Time and resources issues

One of the motives for developing JUNIPER and applying it to the oil industry case studies was dissatisfaction with the time and cost of more conventional decision analysis. The case studies demonstrated that experts could quickly become proficient with the tool, and then retain that proficiency even if they were using JUNIPER relatively infrequently.

The oil field studies reported here involved a team of six experts, and took approximately 24 man-hours of their time to complete. This involved initial presentations, individual interviews, team and individual sessions with a draft model and building attribute lists, with a final team session having in-depth debate about the figures being put in to the model. Further time was then spent exploring the implications. The researcher typically spent 18 man-hours reading background reports, interviewing the individuals, preparing a draft model and interacting with the experts in team sessions. The result was a process that was felt by the experts not to be intrusive, committing them only to 4 hours each on average. With smaller teams, the individual commitment did not change greatly.

## 7. Conclusions

A new approach to modelling the sources and implications of uncertainty in complex decision-making situations has been developed. The processes that contribute evidence to a decision are modelled in a hierarchical structure. The structure provides a framework for capturing diverse evidence relevant to the decision.

Uncertainty is handled in the model using Interval Probability Theory (IPT), which represents, in a fairly straightforward way, aspects of ambiguity and incompleteness in the available evidence. It can express inferential relationships between different levels in the process hierarchy and dependency relationships within each level in the hierarchy. When applied to a hierarchical process model, IPT enables the uncertainty associated with each of the sub-processes to be cascaded up the hierarchy, giving an overall assessment of the dependability of the decision-making process.

Hierarchical process modelling combined with uncertainty representation using IPT has been implemented in a software tool called JUNIPER. The tool captures in a single window view the complex processes that lead up to a decision. It provides a graphical overview of the sources of uncertainty. Attributes associated with each process in the hierarchy capture, in a collective domain, key items of evidence relating to the decision. The JUNIPER model therefore provides a hub for evidence gathering.

The approach has been tested on case studies from two industry sectors. The case studies suggest that the approach is natural and intuitive for practitioners unfamiliar with such techniques to structure their evidence. In the oil industry sector, the proposed approach helped to make sense of the complex multidisciplinary information that is used to inform major investment decisions. It fostered improved communication within asset teams and between technical experts and their managers. It was used to inform decisions about gathering further information.

In the UK Environment Agency, the sources of uncertainty in the value-laden multi-objective decision-making situations, which combined technical modelling with economic analysis and environmental assessment, were assessed. The modelling demonstrated the sources and implications of uncertainty.

The specific benefits of the proposed approach over existing methods are the ease with which it has proven to be assimilated and implemented, and the mechanism that it provides for assembling evidence, capturing expert judgements and developing shared understanding of complex decisions in multi-disciplinary teams. In situations where the available evidence is qualitatively diverse and possibly conflicting, with variable degrees of associated uncertainty, the proposed approach provides a richer overview of uncertainty than conventional decision analysis. It has formed a basis for discussion and negotiation, facilitating dialogue vertically and horizontally within organisations and with broader stakeholder groups.

## Acknowledgement

The research described in this article was initially funded by the Petroleum Science and Technology Institute. Thanks are due to those industrialists who were brave enough to allow us to try out the ideas in case studies, in particular colleagues from Shell Expro and Texaco Britain. The coastal defence studies were funded in part by the UK Environment Agency and HR Wallingford. The authors are grateful to two anonymous referees for challenging and insightful comments on draft versions of this paper.

## References

[1] A.A. Angehrn, T. Jelassi, DSS research and practice in perspective, Decision Support Systems 12 (4/5) (1994) 267–275.

[2] P. Ayton, G. Wright, Subjective probability: what should we believe? in: G. Wright, P. Ayton (Eds.), Subjective Probability, Wiley, Chichester, 1994, Chap. 8.

[3] J.F. Baldwin, Evidential support logic programming, Fuzzy Sets and Systems 24 (1987) 1– 26.

[4] J.F. Baldwin, T.P. Martin, B.W. Pilsworth, FRIL—Fuzzy and Evidential Reasoning in Artificial Intelligence, Research Studies Press, Taunton, 1995.

[5] L.R. Beach, G.P. Braun, Laboratory studies of subjective Probability, in: G. Wright, P. Ayton (Eds.), Subjective Probability, Wiley, Chichester, 1994, Chap. 6.

[6] D.E. Bell, H. Raiffa, A. Tversky (Eds.), Decision Making: Descriptive, Normative and Prescriptive Interactions, Cambridge Univ. Press, Cambridge, 1988.

[7] D.I. Blockley, Uncertainty analysis in expert systems, Civil Engineering Systems 4 (1987) 3 – 6.

[8] D.I. Blockley, Engineering from reflective practice, Research in Engineering Design 4 (1992) 13 – 22.

[9] D.I. Blockley, Process modelling from reflective practice for engineering quality, Civil and Environmental Engineering Systems 16 (1999) 287– 313.

[10] D.I. Blockley, J.F. Baldwin, Uncertain inference in knowledge-based systems, ASCE Journal of Engineering Mechanics 113 (4) (1987) 467– 481.

[11] R. Boland, R. Greenberg, S. Park, I. Han, Mapping the process of problem reformulation, implications for understanding strategic thought, in: A.S. Huff (Ed.), Mapping Strategic Thought, Wiley, Chichester, 1990, pp. 195– 226.

[12] G.J. Colquhoun, R.W. Baines, R.A. Crossley, A state of the art review of IDEF-0, International Journal of Computer Integrated Manufacturing 6 (4) (1993) 252.

[13] R.M. Cooke, Experts in Uncertainty, Oxford Univ. Press, Oxford, 1991.

[14] W.C. Cui, D.I. Blockley, Interval probability theory for evidential support, International Journal of Intelligent Systems 5 (1990) 183–192.

[15] S.P. Curley, J.I. Golden, Using belief functions to represent degrees of belief, Organisational Behaviour and Human Decision Processes 58 (1994) 271 – 303.

[16] J.P. Davis, A.J. Fletcher, Managing assets under uncertainty, SPE Asia Pacific Conference on Integrated Modelling for Asset Management, Yokohama, Japan, April 25 – 26, 2000.

[17] A.P. Dempster, Upper and lower probability inferences for families of hypotheses with monotone density ratios, Annals of Mathematical Statistics 40 (3) (1969) 953 – 969.

[18] W.P.S. Dias, D.I. Blockley, Reflective practice in engineering design, Proceedings of the Institution of Civil Engineers: Civil Engineering 108 (3) (1995) 160 – 168.

[19] D. Dubois, H. Prade, A discussion of uncertainty handling in support logic programming, International Journal of Intelligent Systems 5 (1990) 15– 42.

[20] D. Dubois, H. Prade, Random sets and fuzzy interval analysis, Fuzzy Sets and Systems 42 (1991) 87–101.

[21] W.R. Ferrell, Discrete subjective probabilities and decision analysis: elicitation, calibration and combination, in: G. Wright, P. Ayton (Eds.), Subjective Probability, Wiley, Chichester, 1994, pp. 411 –451. Chap. 17.

[22] J. Fox, On the necessity of probability: reasons to believe and grounds for doubt, in: G. Wright, P. Ayton (Eds.), Subjective Probability, Wiley, Chichester, 1994, Chap. 5.

[23] B.G. Glaser, A.L. Strauss, The Discovery of Grounded Theory: Strategies for Qualitative Research, Aldins, New York, 1967.

[24] J.W. Hall, D.I. Blockley, J.P. Davis, Uncertain inference using interval probability theory, International Journal of Approximate Reasoning 19 (3–4) (1998) 247– 264.

[25] J.W. Hall, J.P. Davis, D.I. Blockley, Uncertainty analysis of coastal projects, coastal engineering 1998, Proceedings of the 26th International Conference, Copenhagen, Denmark, June 22 – 26 (1998) 1461 – 1474.

[26] S.J. Henkind, M.C. Harrison, An analysis of four uncertainty calculi, IEEE Transactions on Systems, Man and Cybernetics 18 (5) (1988) 700– 714.

[27] R.C. Jeffrey, The Logic of Decision, University of Chicago Press, Chicago, 1983.

[28] R.L. Keeney, Decision analysis: an overview, Operations Research 30 (5) (1982) 803 – 838.

[29] P.R. Kleindorfer, H.C. Kunreuther, P.J.H. Schoemaker, Decision Sciences: An Integrative Perspective, Cambridge Univ. Press, Cambridge, 1993.

[30] G.J. Klir, T.A. Folger, Fuzzy Sets, Uncertainty and Information, Prentice-Hall, London, 1988.

[31] P.J. Krause, D.A. Clark, Representing Uncertain Knowledge: An Artificial Intelligence Approach, Intellect Books, Oxford, 1993.

[32] B.J. Loasby, Choice, Complexity and Ignorance: An Enquiry into Economic Theory and the Practice of Decision-Making, Cambridge Univ. Press, Cambridge, 1976.

[33] J.E. Matheson, Using influence diagrams to value information and control, in: R.M. Oliver, J.Q. Smith (Eds.), Influence Diagrams, Belief Nets and Decision Analysis, Wiley, Chichester, 1994, Chap. 2.

[34] M.W. Merkhoffer, Quantifying judgmental uncertainty: methodology, experiences and insights, IEEE Transactions on Systems, Man and Cybernetics 17 (1987) 741– 752.

[35] H. Mintzberg, D. Raisinghani, A. The´oreˆt, The structure of ‘‘unstructured’’ decision processes, Administrative Science Quarterly 21 (1976) 246 – 275.

[36] M.A. Ould, Business Process Modelling and Analysis for Re-Engineering and Improvement, Wiley, London, 1995.

[37] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann, San Mateo, 1988.

[38] H.E. Robbins, On the measure of random set I, Annals of Mathematical Statistics 15 (3) (1944) 70 – 74.

[39] H.E. Robbins, On the measure of random set II, Annals of Mathematical Statistics 16 (3) (1945) 342 – 347.

[40] A.W. Scheer, ARIS—Business Process Modelling, Springer Verlag, Berlin, 1998.

[41] D.A. Scho¨n, The Reflective Practitioner: How Professional Think in Action, Basic Books, New York, 1983.

[42] D.A. Schum, Evidential Foundations of Probabilistic Reasoning, Wiley, New York, 1994.

[43] B. Schweizer, A. Sklar, Probabilistic Metric Spaces, North-Holland, Amsterdam, 1983.

[44] G. Shafer, A Mathematical Theory of Evidence, Princeton Univ. Press, Princeton, 1976.

[45] G. Shafer, J. Pearl, Readings in Uncertain Reasoning, Morgan Kaufmann, San Mateo, 1990.

[46] H.A. Simon, The Shape of Automation for Men and Management, Harper and Row, New York, 1965.

[47] R.A. Snowdon, An introduction to the IPSE 2.5 project, in: F. Long (Ed.), Software Engineering Environments, Lecture Notes in Computer Science, Springer Verlag, Berlin, 1990.

[48] T. Speed, Complexity, calibration and causality in influence diagrams, in: R.M. Oliver, J.Q. Smith (Eds.), Influence Diagrams, Belief Nets and Decision Analysis, Wiley, Chichester, 1994, Chap. 3.

[49] A. Tversky, D. Kahneman, The framing of decisions and the psychology of choice, Science 211 (D) (1981) 453 – 458.

[50] B.C. Warboys, R.A. Snowdon, An introduction to processcentred environments, in: A. Finklestein, J. Kramer, B. Nuseibeh (Eds.), Software Process Modelling and Technology, Research Studies Press, Taunton, 1998.

[51] L.A. Zadeh, Fuzzy sets as a basis for a theory of possibility, Fuzzy Sets and Systems 1 (1978) 2 – 28.

![](/api/attachments/94W7E29N/fulltext/images/9b4e7bfdf2cba93040d967a6d7fcb0717a2f26ad4079f035ca788a2f8ce88e34.jpg)  
Dr. J.P. Davis is a reader in Hydroinformatics at the University of Bristol. He has a first degree in Aeronautical Engineering and a doctorate in Civil Engineering. Following his work on wave energy devices, and breakwater systems, and subsequent general studies on the intelligent monitoring of civil engineering systems, Dr. Davis spent 3 years looking at human computer interaction in computer-assisted learning. He was technical director of a European funded

programme to develop multimedia products for the European water resources sector. His current research interests are focussed on decision process support and computer-supported uncertainty handling and in several sectors of industry.

![](/api/attachments/94W7E29N/fulltext/images/8f465d300dda20d070c3b0cfa80b6f499d54d91b75a55f7337ed8d963c581c3b.jpg)

Dr. J.W. Hall has a BEng in Civil Engineering and a PhD in uncertainty management, both from the University of Bristol. He has been researching application of risk and uncertainty methods to appraisal, design and implementation of coastal defence projects. This has been extended to non-standard approaches for representing uncertainty. Dr. Hall is an advisor to the UK Department of Environment, Food and Rural Affairs and the UK Environment Agency on the

application of risk and uncertainty methods in flood and coast defence. He currently holds a Royal Academy of Engineering Research Fellowship.
