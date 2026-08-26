---
otero_id: 1110
otero_key: "2Q96AQYK"
title: "Supporting factoring transactions in Brazil using reasoning maps: a language-based DSS for evaluating accounts receivable"
authors: "Gilberto Montibeller; Valerie Belton; Marcus Vinicius A. Lima"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting factoring transactions in Brazil using reasoning maps: a language-based DSS for evaluating accounts receivable

Gilberto Montibeller <sup>a,\*</sup>, Valerie Belton <sup>b</sup>, Marcus Vinicius A. Lima <sup>c</sup>

Operational Research Group, London School of Economics, Houghton Street, London WC2A 2AE, England, UK <sup>b</sup> Dept. of Management Science, University of Strathclyde, Glasgow, Scotland, UK

<sup>c</sup> Dept. of Business Administration, University of Southern Santa Catarina (UNISUL), Floriano´polis-SC, Brazil

Available online 13 January 2005

## Abstract

Factoring companies are a widespread way of providing working capital to small enterprises in Brazil. This type of financial transaction has higher risks when performed in developing countries, due to unreliable financial information on firms, an unstable environment, and particular managerial practices. This paper describes a case study in which a language-based DSS was developed for a Brazilian factoring company to evaluate the perceived risk of buying accounts receivable; and discusses the suitability of different approaches to decision support for this type of decision in Brazil—which may be relevant for similar situations in other developing countries. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Cognitive maps; Factoring; Developing countries; Qualitative decision analysis; Multi-criteria evaluation

## 1. Introduction

Factoring companies are a widespread way of providing working capital for small enterprises in Brazil. A factoring transaction is a triangular financial operation, where the factoring company buys accounts receivable from its client (the creditor firm), and takes the burden of collecting them from its client’s customers (the debtor firms). Brazilian factoring companies operate a high risk/high return business, in an environment characterised by high interest rates and spreads, an unstable macroeconomic situation, a weak legal framework which does not allow a quick recovery of collaterals, and a lack of adequate information on potential borrowers (see Ref. [9] for details on this problem). Perhaps surprisingly, given the prevalence of these operations and the general interest in credit appraisal techniques, there appears to be a lack of decision support systems developed for the tri-partite factoring transactions discussed here.

This paper is part of an ongoing action-research effort which attempts to support decision-makers dealing with this type of problem (see Ref. [4] for a discussion about the use of action-research in the DSS context). This has the dual aim of providing decision support and exploring the appropriateness of different approaches to doing so, given the distinctive characteristics of the problem context. In a previous case study, we employed a quantitative multi-criteria model, which evaluates several dimensions of perceived risk, for developing a DSS (see Ref. [5] for details). This first intervention provided several insights into particular characteristics of this problem, especially its qualitative nature and the decisionmakers’ willingness to think and talk in qualitative terms. These insights lead us to intervene again; now using a different, recently developed decision tool— called a reasoning map—which provides integrated support for both problem structuring and qualitative assessment of alternatives using a cognitive/causal map structure. Reflecting the nature of the action research, the paper is aimed at DSS practitioners and researchers with an interest in the specific application area of financial decision-making and/or the appropriateness of different approaches to decision support for this type of decision in developing countries.

The paper begins with a brief introduction to reasoning maps, which is then elaborated through its use in the development of a DSS to evaluate accounts receivable. We conclude with reflections on the process, in particular on how the specific characteristics of the problem may influence the use and development of DSSs.

## 2. Reasoning maps

A reasoning map is a tool for multi-criteria decision aid, the development of which was motivated by a desire to provide an integrated approach to problem structuring and evaluation (which, so far, have been supported by different methods [1]). It permits the evaluation of decision alternatives along a means–ends network, using qualitative assessments of performance. In this way, it extends the power of inference of causal maps, which are primarily conceived of as a tool to support problem structuring and stop short of the evaluation of alternatives.

Several ways of increasing the power of causal inference in causal maps have been proposed in the literature (e.g., Refs. [2,6,10]). However, none of these approaches were concerned with the use of a causal map to perform a multi-criteria evaluation of alternatives. On the other hand, several multicriteria methods have employed qualitative assessments but, as far as we know, none has tried to evaluate decision alternatives along chains of qualitative arguments.

The construction of a reasoning map can be divided in two main recursive phases (see Refs. [8,9] for details about the method). In the first phase, the building of a reasoning map supports problemstructuring, capturing a decision-maker’s reasoning as a network of means and ends concepts. In the second phase this map is enhanced, using a user-defined qualitative scale to define performances and strengths of influence. This latter phase supports the decisionmaker in evaluating the positive and negative impacts of an action through synthesis of the qualitative information. A set of macros in VBA Excel for Windows has been developed to perform the analysis of reasoning maps; it also allows the input of reasoning maps using standard shapes and connectors, or causal maps imported from the Decision Explorer software (www.banxia.com). In the next section we describe the intervention while, at the same time, briefly presenting the method.

## 3. Supporting factoring decisions with reasoning maps

In this section we present the intervention in which a reasoning map was developed to support the evaluation of accounts receivable by a factoring manager. We first describe the process of problem structuring, then the elicitation of preference information, and the evaluation of a small sample of accounts receivable. We conclude the section with some reflections on the modelling process.

## 3.1. The means–ends network

The first stage of the intervention aimed to encourage the decision-maker (one of the co-authors of this paper, who is an experienced factoring analyst) to reflect on the rationale for buying an account receivable and also to display how the aspects he would seek to take into account are interrelated in a means–ends network, thereby furthering understanding of the issue and providing structure to the problem.

In order to construct this means–ends network (a hierarchy of attributes–consequences–final values), the facilitator uses a semi-structured interviewing process, with question probes that produce predominantly domain-related reasoning statements. Given a set of focal anchors defined by a decision-maker (concerns, wishes, objectives, etc.), the facilitator asks for their antecedents (means) and outcomes (ends), in a process of laddering. Using this protocol, we obtained the initial elements of the map shown in Fig. 1, namely the concepts and links (note that all the links are positive in this map; the focal anchors are highlighted with a <sup>b</sup>\*<sup>Q</sup>). Formally, this model is an acyclic digraph G=(C, D), with a node set C and an edge set D. A positive value on an edge $d _ { i j } { \in } { \bf D }$ represents a positive perceived influence of a means concept $\mathrm { C } _ { i }$ on an end concept $\mathrm { C } _ { j } \mathrm { ; }$ a negative value represents a negative influence, and a zero value represents no influence.

After confirming that the map reflected his thinking, the decision-maker was asked to specify the key concepts in the map, those he felt to be of particular concern in determining the performance of the accounts receivable: $\mathrm { C } _ { 9 } , \mathrm { C } _ { 1 6 } , \mathrm { C } _ { 2 2 } ,$ , and $\mathrm { C } _ { 2 3 }$ (see Fig. 1). It was interesting to notice that all the focal anchors were related to attributes (means) rather than ends, suggesting a focus on information available rather than the purpose of seeking that information. Another significant insight for him was realising that the key concepts were towards the top of the hierarchy, and that acquiring information on the debtor firm (his initial concern, as revealed by the focal anchors) was only a means of checking these key concepts.

## 3.2. Eliciting strengths of influence

A reasoning map aims to be a method of evaluation that is cognitively valid [7]: the parameters it requires and the outputs it provides take explicit account of the cognitive limitations of human beings in providing and understanding information. For that reason all elicited information and model outputs are in qualitative terms, without any conversion to numbers. The evaluation process uses only qualitative (crisp) assessments, via an ordinal scale where each level is a linguistic term (such as <sup>d</sup>strong<sup>T</sup>, <sup>d</sup>weak<sup>T</sup>, etc.). Defining formally this scale, let $\wp$ be a partially ordered finite set with m elements $\wp = \{ p _ { 1 } , p _ { 2 } , . . . ,$ $p _ { m } \}$ , where each value p is a qualitative label.

![](/api/attachments/2Q96AQYK/fulltext/images/ea63716553d3e21dbec0b9c47af45b9350af31a7eada3ef49d9984e1ea97a05f.jpg)  
Fig. 1. The reasoning map of a Brazilian factoring analyst.

In the map, for each concept $\mathrm { C } _ { i }$ we associate a variable $\mathrm { V } _ { i } ,$ which measures the performance of alternatives on the scale $\wp$ . For each link between two concepts, the facilitator elicits, from the decision-maker, the strength of influence $e _ { i j }$ of the $\mathrm { C } _ { i }$ means concept over the $C _ { \mathrm { j } }$ end concept (again using the scale $\wp$ , in a similar way than in a fuzzy cognitive map [6]). In order to elicit each $e _ { i j }$ , we suggest anchoring the decision-maker’s judgements on the lower $\left( { { p _ { 1 } } } \right)$ and upper level $\left( { { p _ { m } } } \right)$ of $\mathrm { V } _ { i } ,$ in a way similar to that of eliciting swing weights in multi-criteria models [1].

Formally, $\forall \mathbf { C } _ { i } { \in } \mathbf { C }$ in the means–ends network G there is a variable $\mathrm { V _ { i } }$ associated $\mathrm { ( V _ { i } }$ measured on $\wp )$ Positive and negative influences are kept apart, so the means–ends network is split in two, one with positive links and one with negative links. For the positive links, each strength of perceived influence between concepts $\mathrm { C _ { i } }$ and $\mathrm { C _ { j } }$ is stored in the element $\mathrm { e _ { i j } }$ (measured on $\wp )$ of a positive edge set E. Conversely, strengths of negative links are stored in a negative edge set E.

Thus, the second phase of the intervention was to help the decision-maker in identifying variables associated with each concept in his reasoning map. For example, the concept $\mathrm { C } _ { 2 } ,$ know who are the debtor firm’s managers (Fig. 1, southwest corner) may be measured by the variable $\mathrm { V } _ { 2 }$ quality of the debtor firm’s management team. The factoring analyst defined a qualitative scale that, he felt, was appropriate to capture the strengths and performance with respect to the defined variables: $\mathrm { \Delta v w = \mathrm { ^ { * } v e r y } }$ weak<sup>T</sup>, $\mathrm { w } = ^ { \epsilon }$ weak<sup>T</sup>, m=<sup>d</sup>moderate<sup>T</sup>, $\mathbf { s } { = } ^ { \circ } \mathbf { s t r o n g } ^ { \prime }$ , and vs=<sup>d</sup>very strong<sup>T</sup>.

For every concept-attribute (i.e., having only out arrows; $\mathrm { e . g . , ~ \mathrm { C _ { 1 } ) } }$ , the decision-maker defined a description for each qualitative label of its associated variable. For example, a performance vw (<sup>b</sup>very weak<sup>Q</sup>) on variable $\mathrm { V } _ { 1 }$ (southwest corner in Fig. 1) is awarded if an account receivable has a <sup>d</sup>debtor firm without any plans of succession<sup>T</sup>. On the other hand, a performance vs (<sup>b</sup>very strong<sup>Q</sup>) would be assigned if the debtor firm has a clear plan promulgated to the market.

Using the extremes of these descriptors as anchors, we asked the decision-maker about the influence that a given means generates on a given end. For example, in terms of succession plans $\left( \mathbf { C } _ { 1 } \right)$ , a variation on $\mathrm { V } _ { 1 }$ from a <sup>d</sup>very weak<sup>T</sup> to <sup>d</sup>very strong<sup>T</sup> would influence <sup>d</sup>weakly<sup>T</sup> his appraisal of the stability and trustworthiness of the debtor $( \mathrm { V } _ { 5 } ) ;$ thus the <sup>d</sup>weak<sup>T</sup> strength of influence associated with the link $\mathrm { C } _ { 1 } { \longrightarrow } \mathrm { C } _ { 5 }$ . The same type of question was posed for every link of the map.

## 3.3. Evaluating accounts receivable

Once the information on strengths of influence was acquired and confirmed with the decision-maker, it was possible to begin evaluating accounts receivable using the model. We illustrate the approach by the evaluation of $^ 6$ accounts receivable (AR) selected by the decision-maker: $\mathrm { A R _ { 1 } }$ and $\mathrm { A R } _ { 2 }$ (<sup>d</sup>good<sup>T</sup> in his holistic assessment), $\mathrm { A R } _ { 3 }$ and $\mathrm { A R } _ { 4 }$ (<sup>d</sup>medium<sup>T</sup>), and $\mathrm { A R } _ { 5 }$ and $\mathrm { A R } _ { 6 }$ (<sup>d</sup>bad<sup>T</sup>).

Each account receivable was evaluated according to the variables of attribute-concepts in Fig 1. For example, for $\operatorname { A R } _ { 1 \cdot }$ , concerning the level of market scope $( \mathrm { V } _ { 2 1 } )$ , the debtor firm has a <sup>d</sup>strong market with a regional scope<sup>T</sup>, thus its performance in this variable is <sup>d</sup>strong<sup>T</sup> (a black dot in the strong cell near $\mathrm { C } _ { 2 1 }$ , northeast corner in Fig. 1). The same kind of evaluation was performed for each attribute, and every account receivable.

Performances along the network, in a reasoning map, are then aggregated using two operators, partial effect and total effect (see also Ref. [6]). These are calculated from bottom-up in the network, in an interactive way as explained below.

The partial effect operator controls the means–end transmission along each link. We suggest taking the Minimum of a given alternative’s performance on the means variable and the strength of influence of the link, so the latter works as a cap on the performance transmission.

For example, in the factoring problem, with $\mathrm { V } _ { 2 1 }$ $( \mathsf { A R } _ { 1 } ) { = } ^ { \circ } \mathsf { s t r o n g } ^ { \prime }$ and $e _ { 2 1 , 2 2 } { = } ^ { \circ } \mathrm { m o d e r a t e } ^ { \circ }$ (northeast corner in Fig. 1) the partial effect PE of $\mathrm { A R } _ { 1 }$ following this path $\scriptstyle \mathrm { i s } \cdot \mathrm { P E } _ { 2 1 , 2 2 } ( \mathrm { A R } _ { 1 } ) = \mathrm { M i n } \{ e _ { 2 1 , 2 2 } ; \mathrm { V } _ { 2 1 } ( \mathrm { A R } _ { 1 } ) \} =$ Min{<sup>d</sup>moderate<sup>T</sup>; <sup>d</sup>strong<sup>T</sup>}=<sup>d</sup>moderate<sup>T</sup>.

In the same way, the other partial effects of $\mathrm { A R _ { 1 } }$ impacting on concept 22 are:

$$
\begin{array}{l} \mathrm{PE} _ {1 8, 2 2} (\mathrm{AR} _ {1}) = \text {Min} \{e _ {1 8, 2 2}; \mathrm{V} _ {1 8} (\mathrm{AR} _ {1}) \} = \text {Min} \{\text {very strong}; \text {weak} \} = \text {weak}; \\ \mathrm{PE} _ {1 9, 2 2} (\mathrm{AR} _ {1}) = \text {Min} \{e _ {1 9, 2 2}; \mathrm{V} _ {1 9} (\mathrm{AR} _ {1}) \} = \text {Min} \{\text {weak}; \text {very strong} \} = \text {weak}; \\ \mathrm{PE} _ {2 0, 2 2} (\mathrm{AR} _ {1}) = \text {Min} \{e _ {2 0, 2 2}; \mathrm{V} _ {2 0} (\mathrm{AR} _ {1}) \} = \text {Min} \\ \{\text {strong}; \text {very strong} \} = \text {strong}. \end{array}
$$

At this point of the intervention, the rationale for this aggregation operator was explained to the decision-maker, describing it in terms of a <sup>b</sup>capping<sup>Q</sup> process, and the sensitivity of outcomes to different strengths of influence was demonstrated.

The total effect operator aggregates several partial effects arriving in a given node of the network. Several ordinal operators may be used for this aggregation, depending on the decision-maker’s structure of preference (e.g., Max, Min, Median; see Ref. [3] for details on these operators).

In order to aggregate the partial effects which impact on a given concept, the decision-maker decided—after testing different operators with the sample of 6 accounts receivable we were evaluating— to employ the Median operator for the total effect, taking the upper mid-point in cases of an even number of effects (the software allows the user to choose from a set of ordinal operators for calculating the total effects). The rationale for using an operator like the Median is that the performances in the partial effects are already <sup>b</sup>weighted<sup>Q</sup> by the strengths of influences, and the median produces a sense of ordinal average.

For example, the total effect $\mathrm { T E } _ { 2 2 }$ of the account receivable $\mathrm { A R _ { 1 } }$ on $\mathrm { V } _ { 2 2 }$ (with partial effects calculated above) is:

$$
\begin{array}{l} \mathrm{TE} _ {2 2} (\mathrm{AR} _ {1}) = \text {Median} \{\mathrm{PE} _ {1 8, 2 2} (\mathrm{AR} _ {1}); \mathrm{PE} _ {1 9, 2 2} (\mathrm{AR} _ {1}); \\ \mathrm{PE} _ {2 1, 2 2} (\mathrm{AR} _ {1}); \mathrm{PE} _ {2 0, 2 2} (\mathrm{AR} _ {1}) \}; \\ \mathrm{TE} _ {2 2} (\mathrm{AR} _ {1}) = \text {Median} \{\text {"weak"; weak"; moderate"; strong"} \} = \text {"moderate".} \end{array}
$$

This performance of $\mathrm { A R _ { 1 } }$ on $\mathrm { V } _ { 2 2 }$ is shown in Fig. 1 (on the left side of $\mathrm { C } _ { 2 2 }$ , with a black dot symbolising the <sup>d</sup>moderate<sup>T</sup> level). Analogous operations were employed to calculate the performance of each AR on every concept, these results are also show in the same figure.

As a decision rule, the factoring analyst stated that he would buy only accounts receivable that have at least a <sup>d</sup>moderate<sup>T</sup> performance on the variable $\mathrm { V } _ { 2 4 }$ associated with the value concept $\mathrm { C } _ { 2 4 }$ (discount rates are fixed by the market, but he can reject buying risky AR from his clients). Thus, from the sample we evaluated, he would accept (that is, buy) $\mathrm { A R } _ { 1 } { - } \mathrm { A R } _ { 4 }$ and reject $\mathrm { A R } _ { 5 }$ and $\mathrm { A R } _ { 6 }$

## 3.4. Reflections on the modelling

It is interesting to note that the model did not differentiate (with respect to $\mathrm { V } _ { 2 4 } )$ the receivables that the decision-maker considered holistically as <sup>d</sup>good<sup>T</sup> from those he considered <sup>d</sup>medium<sup>T</sup>. If we analyse their performances on the key concepts $\mathrm { C _ { 9 } } ,$ $\mathrm { C } _ { 1 6 } , \mathrm { C } _ { 2 2 }$ , and $\mathrm { C } _ { 2 3 }$ (highlighted with a border in Fig. 1), we notice that the two <sup>d</sup>good<sup>T</sup> ones have clearly outperformed the <sup>d</sup>medium<sup>T</sup> ones only on $\mathrm { V _ { 9 } }$ . Thus his holistic evaluation still reflects his very early heuristic of deciding mainly on the basis of his trust in the creditor firm (see Ref. [5]).

One conclusion from the analysis is that, indeed, the debtor firm is perceived by the credit analyst as the main source of perceived risk: the relations concerning the debtor firm $e _ { 1 6 , 2 4 }$ and $e _ { 2 3 , 2 4 }$ are <sup>d</sup>very strong (as well as $e _ { 5 , 2 3 } , \ e _ { 1 7 , 2 3 } , \ e _ { 3 } , \ e _ { 5 , 2 3 } , \ e _ { 6 , 2 3 } ,$ and $e _ { 1 8 , 2 3 } ) ;$ and $e _ { 2 2 , 2 4 }$ is <sup>d</sup>moderate<sup>T</sup>.

Another notable outcome is that, for the first time, the decision-maker started to take the time framework into consideration in his thinking when analysing the data. His first assessment of $e _ { 2 2 , 2 4 }$ was that it would be <sup>d</sup>strong<sup>T</sup>. Reflecting more carefully, however, he started to realise that, because the financial operation is set in the short-term, the economic position of the debtor firm was not so influential on the success of the operation and revised it to <sup>d</sup>moderate<sup>T</sup>.

The comparison between holistic versus decomposed judgements was important to build up the decision-maker’s confidence in the model and to better understand the problem. However, this in itself does not guarantee, in our view, the validity of a DSS based on preference modelling (even if the results are quite similar, as was the case in this intervention). The validation of models of preference is a challenging issue, in part because these are often developed, as here, within a constructivist framework [12], which seeks to encourage learning and consequentially may challenge and lead to a change in holistic judgement. Nevertheless, any evaluation of a DSS must address both theoretical and practical concerns. On the theoretical level, the underlying approach of a reasoning map was developed to be psychologically valid, as previously discussed (see also Ref. [7]). On a practical level, we aimed to build a DSS based on a requisite decision model [11], one that the decision-maker perceived as providing enough guidance and insight for supporting his decisions.

A natural progression in the use of the model would be to use the factoring manager’s reasoning map to evaluate all future accounts receivable. This could be supplemented by a database of evaluations of debtors and creditors, generated as the model is used together with the outcomes of receivable purchases, which would inform further the development of the model (confirming or disconfirming the decisionmaker’s beliefs).

## 4. Reflections on the interventions

In this section we present reflections on how DSSs may support decision-making in this context in developing countries (see Ref. [9] for details); these are derived from the experience to date in action-research interventions (described in this paper and in Ref. [5]), where we developed two different types of DSS to support the evaluation of accounts receivable.

## 4.1. The nature of the model

n Quantitative forecasts may be difficult: A lack of reliable quantitative data in developing countries may make it difficult to build a reliable quantitative model for a factoring company, and an unstable environment may create problems for extrapolating trends into the future.

n Managers may prefer a model based on beliefs: Factoring managers in developing countries cope with high degrees of uncertainty, relying on a strong network of soft information flow (<sup>d</sup>the market<sup>T</sup>) and on a set of decision heuristics (based on their beliefs). Both information and beliefs are very dynamic in nature. Thus, they tend to prefer models that try to capture those values and beliefs rather than an objective model based on hard data that they may not trust.

n Problem structuring is important: As the factoring problem lacks a clear definition, and is surrounded by uncertainty and beliefs, a phase of problem structuring is critical. Factoring managers in developing countries are generally not used to reflecting on their practice, so this phase is very likely to generate useful insights for further modelling (either quantitative or qualitative).

The use of several modelling tools in the same intervention may be challenging: Factoring managers in developing countries are not generally familiar with the use of formal models, or to thinking using this kind of artefact. Therefore, despite the potential benefits of a multi-methodological approach (see Ref. [1]), a single modelling logic may make it easier to develop DSSs that are accessible to decision-makers and also increase the likelihood of their sustained use in practice.

4.2. The nature of data and of information about preferences

n Managers may prefer qualitative thinking: Many of the factoring managers in developing countries come from a non-quantitative background, and may feel intimidated by quantitative modelling. They use language as their main reasoning tool and tend to feel more comfortable using qualitative modelling/assessment.

n Data input may be an important concern: As the number of daily transactions is high and extracting relevant data from the credit report is time consuming (and usually cannot be automated), designers of DSSs for this type of problem may need to address the ease, including time requirement, of inputting data required by the evaluation model.

## 4.3. The use of the model

n Decision support systems may need to allow some <sup>b</sup>Do-It-Yourself <sup>Q</sup> use: As the environment changes rapidly in developing countries, and the factoring managers’ beliefs have to adapt to it, the DSS may need to allow the user to easily change parameters and the structure of the model by themselves.

n DSSs need to support accountability but not necessarily <sup>b</sup>objectivity<sup>Q</sup> of decisions: As factoring companies are relatively small and privately owned, their credit analyst is usually concerned with providing justifiable solutions for the company’s owners/partners. Therefore, supporting accountability (i.e., providing logical reasons why a given action was taken) seems to be a crucial appeal of a DSS in this context. For the same reason, this type of decision may not need an <sup>b</sup>objective<sup>Q</sup> optimal solution, free of values and beliefs, which is often required to justify actions in large organisations.

These are only tentative conclusions, from two indepth case studies involving the same decision-maker (who, we should say, has a much broader market experience and much better formal qualifications than the average Brazilian factoring manager); thus we recognise that more evidence is needed to confirm or refute them. The extent to which the observations are specific to Brazil, or to developing countries in general, is a matter for further research. We believe that this is largely a matter of degree—for example, difficulties in access to reliable quantitative data may be a problem to some extent in many countries, but is particularly so in Brazil.

## 5. Conclusions and directions for further research

This paper has described the development and application of a DSS based on a recently developed and evolving approach to multicriteria decision aid, referred to as a reasoning map, which provides an integrated framework for problem structuring and evaluation. The problem considered, the evaluation of accounts receivable, is one that is faced on a regular basis by Brazilian factoring companies.

The aim of the intervention was neither to provide a normative rule of choice nor a descriptive model which reflects unaided decision-making. The objective was to enhance the decision-maker’s understanding of the issue, by taking him through a structured process which encourages hard thinking, and by providing a tool that may make him more aware of the evaluation of a given account receivable in terms of his ultimate goals, through multiple and interacting chains of influence. We also have drawn reflections from two interventions on this problem, regarding some challenges and opportunities in designing DSSs for this type of problem in developing countries.

We believe that more research involving the development of DSSs in real-world interventions in developing countries is needed. Future research may address different types of decisions in the same country using the same decision method (therefore extending in-country generalizability of outcomes), or the same type of problem in different countries using the same decision method (thus enhancing crosscountry generalizability of conclusions). Another interesting future research would be using different decision methods for this factoring problem like, for example, Expert Systems, Fuzzy Cognitive Maps or Bayesian Networks. An important aspect is, in our view, that the research design of these interventions focuses explicitly on how the developing countries specific features may influence the choice of a decision method and on the DSS design.

## Acknowledgement

We are thankful to the anonymous referees for their valuable suggestions.

## References

[1] V. Belton, F. Ackermann, I. Shepherd, Integrated support from problem structuring through to alternative evaluation using COPE and VISA, Journal of Multi-Criteria Decision Analysis 6 (1997) 115– 130.

[2] B. Chaib-draa, Causal maps: theory, implementation, and practical applications in multi-agent environments, IEEE Transactions on Knowledge and Data Engineering 14 (6) (2002) 1201– 1217.

[3] J. Domingo-Ferrer, V. Torra, Median based aggregation operators for prototype construction in ordinal scales, International Journal of Intelligent Systems 18 (6) (2003) 633 – 655.

[4] C. Eden, On evaluating the performance of <sup>d</sup>wide-band<sup>T</sup> GDSS’s, European Journal of Operational Research 81 (2) (1995) 302– 311.

[5] L. Ensslin, G. Montibeller, M.V. Lima, Constructing and implementing a DSS to help evaluate perceived risk of accounts receivable, in: Y.Y. Haimes, R.E. Steuer (Eds.), Research and Practice in Multi-Criteria Decision Making, Springer, Berlin, 2000, pp. 248– 259.

[6] B. Kosko, Fuzzy cognitive maps, International Journal of Man-Machine Studies 24 (1986) 65– 75.

[7] O.I. Larichev, Cognitive validity in design of decision-aiding techniques, Journal of Multi-Criteria Decision Analysis 1 (1992) 127–138.

[8] G. Montibeller, V. Belton, F. Ackermann, L. Ensslin, Reasoning Maps for Decision Aid, Journal of the Operational Reserach Society (forthcoming).

[9] G. Montibeller, V. Belton, M.V. Lima, Supporting factoring transactions in Brazil using Reasoning Maps, Research Paper No. 2003/8—Dept. of Management Science, Univ. of Strath clyde (2003).

[10] S. Nadkarni, P.P. Shenoy, A causal mapping approach to constructing Bayesian networks, Decision Support Systems 38 (2) (2004) 259–281.

[11] L.D. Phillips, A theory of requisite decision models, Acta Psychologica 56 (1984) 29–48.

[12] B. Roy, Decision science or decision-aid science? European Journal of Operational Research 66 (1993) 184– 203.

Gilberto Montibeller is a Lecturer (Assistant Professor) in Decision Sciences in the Operational Research Group, London School of Economics. He started his career as an executive at BAT, after receiving a BEng (Hons.) in Electrical Engineering. Returning to the academia, he was awarded an MSc and then a PhD in Production Engineering, both in the field of Operational Research. Dr. Montibeller has been researching and providing consultancy in Multi-criteria Decision Analysis for the past 10 years. His research has been published in journals such as The Journal of the Operational Research Society and OMEGA – The International Journal of Management Science. He is an Assistant Editor of the Journal of Multi-Criteria Decision Analysis.

Valerie Belton is Professor of Management Science in the Department of Management Science, University of Strathclyde in Glasgow, Scotland. After graduating with a BSc in Mathematics from Durham University and an MA in Operational Research from Lancaster University, went to work as an analyst with the Civil Aviation Authority, later returning to Cambridge University to do doctoral research into the use of methods for multicriteria analysis. Her research in this field, which emphasises the use of MCDA in practice and has involved collaborations with a wide range of UK organisations, has continued over the past 20 years. She is currently President of the International Society on Multi-Criteria Decision Making, Editor of the Journal of Multi-Criteria Decision Analysis, and the first female President of the UK Operational Research Society.

Marcus Vinicius A. Lima is Assistant Professor in the Department of Business Administration, University of Southern Santa Catarina (UNISUL), Floriano´polis, Brazil; and a private consultant for small and medium size companies. He holds a BSc in Business Administration from the ESAG Business School (Brazil), and has worked in the Brazilian financial systems during the last 20 years, as a stock market dealer in the Sa˜o Paulo stock exchange (BOVESPA), as a dealer in the currency market, and as a factoring manager. He holds an MSc in Production Engineering (UFSC) and a PhD in Production Engineering (UFSC).
