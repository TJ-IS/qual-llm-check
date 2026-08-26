---
otero_id: 15590
otero_key: "TRRKMYEH"
title: "Evaluating a model for cost-effective data quality management in a real-world CRM setting"
authors: "Adir Even; G. Shankaranarayanan; Paul D. Berger"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.07.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluating a model for cost-effective data quality management in a real-world CRM setting

Adir Even <sup>a,</sup>⁎, G. Shankaranarayanan <sup>b</sup>, Paul D. Berger <sup>c</sup>

<sup>a</sup> Department of Industrial Engineering and Management, Ben-Gurion University of the Negev, P.O. Box 653, Beer-Sheva, 84105, Israel

<sup>b</sup> Technology, Operations, and Information Management, Babson College, Babson Park, MA 02457-0310, USA

<sup>c</sup> Marketing Department, Bentley University, Morison Hall, 175 Forest St., Waltham, MA 02452, USA

## a r t i c l e i n f o

Article history: Received 12 October 2009 Received in revised form 27 July 2010 Accepted 27 July 2010 Available online 6 August 2010

Keywords: Data quality Utility Cost–bene<sup>fi</sup>t analysis Data warehouse CRM

## a b s t r a c t

Managing data resources at high quality is usually viewed as axiomatic. However, we suggest that, since the process of improving data quality should attempt to maximize economic bene<sup>fi</sup>ts as well, high data quality is not necessarily economically-optimal. We demonstrate this argument by evaluating a microeconomic model that links the handling of data quality defects, such as outdated data and missing values, to economic outcomes: utility, cost, and net-bene<sup>fi</sup>t. The evaluation is set in the context of Customer Relationship Management (CRM) and uses large samples from a real-world data resource used for managing alumni relations. Within this context, our evaluation shows that all model parameters can be measured, and that all model-related assumptions are, largely, well supported. The evaluation con<sup>fi</sup>rms the assumption that the optimal quality level, in terms of maximizing net-bene<sup>fi</sup>ts, is not necessarily the highest possible. Further, the evaluation process contributes some important insights for revising current data acquisition and maintenance policies.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Maintaining data resources at a high quality level is a critical task in managing organizational information systems (IS). Data quality (DQ) signi<sup>fi</sup>cantly affects IS adoption and the success of data utilization [10,26]. Data quality management (DQM) has been examined from a variety of technical, functional, and organizational perspectives [22]. Achieving high quality is the primary objective of DQM efforts, and much research in DQM focuses on methodologies, tools and techniques for improving quality. Recent studies (e.g., [14,19]) have suggested that high DQ, although having clear merits, should not necessarily be the only objective to consider when assessing DQM alternatives, particularly in an IS that manages large datasets. As shown in these studies, maximizing economic bene<sup>fi</sup>ts, based on the value gained from improving quality, and the costs involved in improving quality, may con<sup>fl</sup>ict with the target of achieving a high data quality level. Such <sup>fi</sup>ndings inspire the need to link DQM decisions to economic outcomes and tradeoffs, with the goal of identifying more cost-effective DQM solutions.

The quality of organizational data is rarely perfect as data, when captured and stored, may suffer from such defects as inaccuracies and missing values [22]. Its quality may further deteriorate as the realworld items that the data describes may change over time (e.g., a customer changing address, profession, and/or marital status). A plethora of studies have underscored the negative effect of low DQ on decision performance (e.g., [7,9,16,29]) and have identi<sup>fi</sup>ed the need to develop data refreshing policies [23], to measure DQ ([13,19]), and to communicate DQ assessments to decision makers ([29,31]). However, maintaining data at a high quality level involves signi<sup>fi</sup>cant costs [12]. These costs are associated with efforts to detect and correct defects, set governance policies, redesign processes, and invest in monitoring tools. From an economic perspective, one would try to reach a certain quality level at a minimum possible cost. Targeting a higher DQ level improves utility of the data. (We use the term, “utility,” as a synonym for “value” or “bene<sup>fi</sup>t”, to be consistent with the use of this term in prominent prior literature. This has nothing to do with “utility theory”). Yet, at the same time, targeting a higher DQ level increases DQM costs [14]. However, although some DQM decisions involve signi<sup>fi</sup>cant utility/cost tradeoffs, economics-driven assessments of DQM alternatives are under-examined, barring a few exceptions. Some works (e.g., [3–5]) use utility-driven assessments to understand tradeoffs between different DQ dimensions, optimize their con<sup>fi</sup>guration accordingly, and use the results for improving data processes. An algorithm that minimizes the cost of retrieving data that meets certain quality requirements has been proposed in [2]. Policy for optimizing the cost for synchronizing the contents of a DW with the source systems from which data is retrieved has been examined in [11]. A similar issue is examined from the point of refreshing distributed data views [28] and from the point of the data retrieved by query execution in DW environments [15]. Other research has also used economic assessments for developing superior DQ measurements (e.g., [13,19]).

A framework for optimally con<sup>fi</sup>guring a tabular dataset, considering economic perspectives, has been described in [14]. In this study, we develop and evaluate that model further to examine two key questions for de<sup>fi</sup>ning optimal quality improvement policies: a) within a large data resource, what subset of records (de<sup>fi</sup>ned by the time-span coverage, as explained later) should be targeted for improvement? b) Within that chosen subset, what should be the targeted quality level? The model in [14] has been evaluated analytically, using closed-form solutions and numerical approximations to assess applicability, given certain assumptions and constraints. In this study, we describe a rigorous and comprehensive empirical evaluation, which examines the applicability and usefulness of the model in a real-world setting. We show that, within our evaluation context, all model variables can be operationalized and all parameters estimated. Further, our evaluation con<sup>fi</sup>rms our modeling assumptions about associations between decision variables (time span and quality level) and economic outcomes (utility, cost, and netbene<sup>fi</sup>t). We show that improvements to current data acquisition and maintenance policies, identi<sup>fi</sup>ed from applying the model, can signi<sup>fi</sup>cantly increase the overall bene<sup>fi</sup>t. The evaluation also highlights enhancements to the model to address similar design decisions in other data management contexts. Our evaluation illustrates the importance of quantitatively assessing and understanding the cost– bene<sup>fi</sup>t tradeoffs, particularly in large datasets where such tradeoffs can be very signi<sup>fi</sup>cant.

We evaluate the model in a CRM context. Several studies (e.g., [8,17,21,27]) have underscored the importance of managing customer data at a high quality level. DQ defects (e.g., missing, inaccurate, and/ or outdated data values) might prevent managers and analysts from having the right picture of customers and their purchase preferences and, hence, might damage marketing efforts signi<sup>fi</sup>cantly. Some studies (e.g., [19,23]) have also discussed methodologies and techniques for improving the quality of customer data. For our evaluation, we use large data samples from a real-world system that helps manage alumni relationships in a large university. This system helps segment and categorize donors, predict donor behavior, and manage solicitation campaigns, much like how a traditional CRM helps manage customers [6,23,27]. Though we focus on CRM, our model and evaluation methodology applies, in general, to data environments that manage large data resources, such as data warehouses (DW) and enterprise resource planning (ERP) systems. Such environments execute business processes, support decision making, and generate revenue through the sale of data products (e.g., [18,20,32]). We see the plethora of data usages as ways of gaining bene<sup>fi</sup>ts from the data resource. Such bene<sup>fi</sup>ts can be conceptualized as “utility” [1] — a measure for the value gained through enhancements to business performance, improvements to decision outcomes, or the data consumer's willingness to pay. We posit that assessing utility-cost tradeoffs toward the maximization of the net-bene<sup>fi</sup>t gained from using data resources must be an important goal for managing these resources.

In the remainder of this paper, we <sup>fi</sup>rst brie<sup>fl</sup>y review the dataset optimization model and state our evaluation objectives. We then describe our process for evaluating the model with the alumni data, present and analyze the results, and highlight important insights gained through such analyses. To conclude, we restate the contributions of this study, discuss implications for DQM research and practice, and suggest directions for future research.

## 2. Evaluating the dataset optimization model

Our evaluation of the dataset optimization model proposed in [14] has two important goals. First, we aim at validating and demonstrating the usability of the model within a real-world context. Second, we wish to gain important insights towards improving data quality within the speci<sup>fi</sup>c evaluation context — managing alumni data. The Total Data Quality Management (TDQM) approach [30] promotes the notion that data quality improvement is not a one-time effort, but rather an on-going cycle of incremental improvements (Fig. 1), which consists of four main stages: a) Define — identifying the evaluation objectives and scope, the set of feasible actions, and a model that describes the anticipated effect of these actions, b) Measure — assigning quantitative values to the model variables and parameters, c) Analyze — using the model for assessing the different alternatives toward identifying the optimal solution, and d) Improve — translating the analysis results to recommendation of a set of actions that should be taken toward data quality improvement.

![](/api/attachments/TRRKMYEH/fulltext/images/d7a5f71ef0a8a8429aa3f7f06ca5dce047f0750058f9f718bdfb7b12360194eb.jpg)  
Fig. 1. The data quality improvement process.

In this study, we demonstrate one full cycle of the evaluation process, along the stages of the TDQM cycle. As we discuss later, this cycle should be followed by others, which look into other possible data quality improvement and process enhancements.

## 2.1. Model overview

The design-optimization framework in [14] suggests that certain design characteristics of information systems affect utility, a measure of business bene<sup>fi</sup>ts gained from using data resources, and affect the cost of implementing and maintaining the resources. It views design characteristics as decision variables in a deterministic model that the designer con<sup>fi</sup>gures, where the goal is maximizing net-benefit — the difference between utility and cost.

The tabular dataset model, derived from that framework, addresses two key decisions that can be interpreted as being associated with managing the quality of large datasets: (a) Time Span (T) is typically de<sup>fi</sup>ned by a “cut off” record age. Data administrators may consider managing records that are older than T differently (e.g., discard or archive them). The time-span variable T ranges between 0 and $T ^ { S } ,$ , the maximum time-span coverage available. Increasing T broadens the range of data records covered by the quality improvement efforts; hence, it increases the potential for gaining utility. However, it also increases the associated costs. The preliminary model assumes that the marginal utility of data records declines exponentially with age. It can, hence, be shown that the overall utility of a dataset increases with T, but at an exponentially-decreasing rate — $\mathrm { i . e . , } U \infty ( 1 { - } e ^ { - \alpha T } )$ , where αN0. Further, the model assumes that the number of records (and cost), grows linearly with T. (b) Targeted Quality Level (Q): the presence of defects in a data resource reduces its utility, and the model uses an objective quality measurement (a [0,1] ratio) that re<sup>fl</sup>ects the presence of defects [25]. Given a certain quality level (i.e., the proportion of non-defective dataset records), one may decide to reduce the presence of defects, which improves quality and usability of the evaluated data resource; hence, the associated utility. The model assumes that dataset utility grows with quality to a certain power $( \mathrm { i } . \mathrm { e } . , U \propto Q ^ { \lambda } ,$ , where $\lambda { > } 0 )$ . However, the higher the quality level targeted, the higher are the associated improvement and maintenance costs. The model assumes that a certain quality level $( Q ^ { S } )$ is guaranteed by the data source, and that the cost increases with quality to a certain power when a higher quality is targeted $( \mathrm { i } . \mathrm { e } . , C \propto Q ^ { \delta } ,$ where δ N 0). It is likely, although not mandated, that δN1 and that the cost-mapping function is convex with Q. The model allows “quality” to be de<sup>fi</sup>ned in several different ways (e.g., re<sup>fl</sup>ecting classic DQ dimensions, such as completeness, accuracy, or validity), as long as Q is measured on a [0,1] scale and a higher value of Q indicates higher quality.

The model (Fig. 2) links the decision variables (T and Q) to economic outcomes, namely, utility (U), cost (C), and net-bene<sup>fi</sup>t (B). It suggests that the effect of the decision variables on all decision outcomes is moderated by the context of data use. The model assumes I different usages, indexed by [i], each associated with a utility cap of $u _ { i }$ (obtained, theoretically, at T→∞ (maximum time) and $Q = 1$ (perfect quality)) and individual utility-curve parameters (i.e., $U _ { i } = u _ { i } ( 1 { - } e ^ { - \alpha _ { i } T } ) Q ^ { \wedge _ { i } } )$ . The overall utility is assumed to be sumadditive (i.e., $\begin{array} { r } { U { = } \sum _ { i = 1 \dots I } U _ { i } ) } \end{array}$ . Further, it assumes that the overall cost C has a variable component which depends on the decision variables $( c ^ { V } ( Q / Q ^ { S } ) ^ { \delta } T )$ , and a <sup>fi</sup>xed component $c ^ { F } .$ The overall netbene<sup>fi</sup>t (B) is the difference between overall utility (U) and overall cost (C):

$$
\begin{array}{c} B (T, Q) = U (T, Q) - C (T, Q) = \sum_ {i = 1 \dots I} u _ {i} \Big (1 - e ^ {- \alpha_ {i} T} \Big) Q ^ {\lambda_ {i}} \\ - \Big (c ^ {F} + c ^ {V} \Big (Q / Q ^ {S} \Big) ^ {\delta} T \Big) \end{array}\tag{1}
$$

s.t., $0 \le T \le T ^ { S } , Q ^ { S } \le Q \le 1$ , where,

U, C, B — The overall utility, cost, and net-bene<sup>fi</sup>t, respectively

T, Q — The time span and the targeted DQ level, respectively (the decision variables)

I — The number of different data usages (indexed by [i])

u<sub>i</sub> — The utility cap of usage [i] at T→∞ and $Q = 1$

$\alpha _ { i } - \Lambda$ sensitivity parameter of utility [i] to the time-span coverage $( \alpha _ { i } { > } 0 )$

$\lambda _ { i } - \mathsf { A }$ sensitivity parameter of utility [i] to the targeted data quality $\left( \lambda _ { i } > 0 \right)$

$T ^ { S } -$ The maximal time-span coverage offered by the data source $Q ^ { S } -$ The minimal quality guaranteed by the data source

$c ^ { F } , c ^ { V } \cdot$ — The <sup>fi</sup>xed cost and the variable cost $( \tt a t Q { = } Q ^ { S } )$ parameters, respectively

δ — Cost sensitivity to DQ improvement, δN0.

The formulation above serves as the objective function for optimization — choose the con<sup>fi</sup>guration (i.e., targeted values) of T and Q such that the net-bene<sup>fi</sup>t is maximized. It is shown that for a single usage $( \mathrm { i } . \mathrm { e } . , I { = } 1 )$ , the optimum has a closed-form solution [14]. When optimizing T or Q alone, the optimal points $( T ^ { O P T }$ and $Q ^ { O P T } ,$ respectively) are (for ease of notation, dropping the subscript, i=1):

$$
T ^ {O P T} = - (1 / \alpha) L n \left\{\left(c ^ {V} Q ^ {\delta - \lambda}\right) / \left(\alpha u \left(Q ^ {S}\right) ^ {\delta}\right) \right\}, \text { and }
$$

$$
Q ^ {O P T} = \left(\left(\lambda u (1 - e ^ {- \alpha T}) (Q ^ {S}) ^ {\delta}\right) / (\delta c ^ {V} T)\right) ^ {1 / (\delta - \lambda)}.\tag{2}
$$

When optimizing T and Q simultaneously, the optimum $( T ^ { O P T }$ $Q ^ { o P T } )$ can be obtained from:

$$
(\lambda / \alpha) \left(e ^ {\alpha T ^ {O P T}} - 1\right) = \delta T ^ {O P T}, \text {   and   } Q ^ {O P T} = \left(\alpha u e ^ {- \alpha T ^ {O P T}} \left(Q ^ {S}\right) ^ {\delta} / c ^ {V}\right) ^ {1 / (\delta - \lambda)}.\tag{3}
$$

To summarize, we restate that the suggested formulation in Eq. (1) encapsulates a few assumptions about the link between the decision variables (T and Q) and economic outcomes (U, C, and B). These assumptions are stated below as a set of propositions that will be validated through our evaluation process:

• P1: Utility (U) and Cost (C) increase with higher Time Span (T)

• P1a: Utility (U) increases with a higher Time Span (T) at a diminishing rate

• P1b: Variable Cost (C<sup>V</sup>) increases with a higher Time Span (T) at a linear rate

• P2: Utility (U) and Cost (C) increase with higher Quality Level (Q)

• P2a: Utility (U) increases with a higher Quality Level (Q) to a certain power

• P2b: Variable Cost $( C ^ { V } )$ increases with a higher Quality Level (Q) to a certain power

• P3: The effect of Time Span (T) and Quality Level (Q) on Utility (U), Cost (C), and Net-Bene<sup>fi</sup>t (B) is moderated by the usage and implementation context.

## 2.2. Evaluation objectives

## We evaluate the model along four criteria:

Feasibility: The model represents certain (assumed) relationships between decision variables (i.e., T and Q) and outcomes (i.e., U, C, and B) in a parameterized form. Feasibility is established if the evaluation shows that these variables can be conceptualized and measured within the evaluation context, and that all parameters can be estimated. In the case of a tabular dataset, measuring both decision variables and outcomes at the record level de<sup>fi</sup>nes an association between these variables, permitting parameter estimation.

Representability: The model assumes certain relationships between decision variables and outcomes, as stated in the previous section as a set of propositions. The high-level assumptions (propositions P1, P2, and P3) are realistic and do not need explicit veri<sup>fi</sup>cation. For example, it is reasonable to assume that both utility and cost increase (or, at least, do not decrease) with larger time span and better quality. It is also reasonable to assume that the effect of the decision variables on the economic outcomes will depend on the usage and implementation context. However, the model also makes some speci<sup>fi</sup>c assumptions (propositions P1a, P1b, P2a and P2b) and our evaluation attempts to verify whether these truly represent real-world behavior and whether they are supported by empirical <sup>fi</sup>ndings.

Impact: A premise underlying the model is that optimizing utility/ cost tradeoffs in the economics-driven evaluation process may lead to a different dataset design con<sup>fi</sup>guration, compared to the one driven solely by functional and technical needs. Further, the con<sup>fi</sup>guration obtained is expected to improve economic performance. Our evaluation validates the model's impact — i.e., that the con<sup>fi</sup>guration is indeed different when the model's solution is used within the given context and that the associated net-bene<sup>fi</sup>t is higher. A con<sup>fi</sup>guration driven by functional and technical requirements would cover the maximum possible T and/or target the highest Q within given capacity constraints. An economics-driven design may limit T, or target a less-than-perfect Q. As noted, the evaluation needs to show that, in such cases, the net-bene<sup>fi</sup>t of the economics-driven con<sup>fi</sup>guration will be materially higher. The model also provides insights for better DQM, as it assesses the economic effect of the different decision variables, and estimates sensitivity to con<sup>fi</sup>guration changes. This may suggest the need to manage certain data subsets differently, closely monitor their quality, and possibly rede<sup>fi</sup>ne their content and acquisition methods. Generalizability: Can the evaluation results inform other DQ decisions within the evaluated context? Can they inform similar DQ decisions in other contexts? Generalization can help enhance analytical formulations, extend the model to address other design decisions, and/or develop methodologies for applying it in other business contexts. Generalization aspects examined here are: (a) System and process configuration: The con<sup>fi</sup>guration of speci<sup>fi</sup>c datasets (within the evaluation context) may affect other DQ decisions in the data environment in which they are managed. (b) Impact on data-resource management: The evaluation may suggest improvements to more general data maintenance and administration practices, beyond just the con<sup>fi</sup>guration of datasets and the data environment (e.g., enhancements to existing datasets and development of new quality improvement policies). Further, the evaluation may offer insights for improving business bene<sup>fi</sup>ts through better use of the data resource. (c) DQM in broader contexts: The evaluation may provide insights for better DQM in other similar data management contexts.

![](/api/attachments/TRRKMYEH/fulltext/images/1d88bd21e69048c4bd75d77736aa40e99714243a69a0bcf59ca48e47b5c24b95.jpg)  
Fig. 2. The dataset con<sup>fi</sup>guration model.

## 2.3. Evaluation context and scope

We evaluate the model using alumni data, a large data resource used by an educational institution for managing relationships with alumni, parents, friends, and other potential donors. The data supports different tasks performed by different departments such as maintaining contacts, identifying potential donors, and planning pledge campaigns. The data includes pro<sup>fi</sup>les of donors (with demographic attributes such as school of graduation, addresses, income level, and marital status), and associated gift and pledge transactions. Data acquisition and maintenance in the alumni system are associated with non-trivial variable costs. Some attribute values may be missing when a new record is added (e.g., occupation or income), and the values of others may change over time (e.g., Address/ Phone); hence, data that is not audited frequently might become un<sup>fi</sup>t for use. Correcting and enhancing data records requires contacting the right individuals, or hiring agencies specializing in list-enhancement. The data acquisition and maintenance costs grow with the number of records (hence, with time span) and with targeted quality levels, and our evaluation focuses on optimizing these factors.

The study evaluates large samples from two key datasets in the alumni system: (a) The Profiles dataset (358,372 records) captures data on potential donors. Our evaluation considers descriptive pro<sup>fi</sup>le attributes that were indicated by key users (stakeholders and decision makers) as ones most commonly used for managing alumni relations and/or for classifying donors. The values of some attributes (e.g., Graduation Year and School, Gender, Marital Status, Religion, and Ethnicity, Home Address/Phone) are included when a record is added and some of these may change over time. Values for other attributes (e.g., Income, Occupation, and Business Address/Phone) are added only later. All values were coded and for Address/Phone, we were provided only a 1/0 indicator of whether a value exists or is missing.

Two other pro<sup>fi</sup>le attributes are important in our evaluation. We use the Audit Date, the date when a pro<sup>fi</sup>le was most recently audited (i.e., has its data veri<sup>fi</sup>ed and corrected, if needed), to assess the age of data records. The other, Prospect/Non-prospect classi<sup>fi</sup>cation, re<sup>fl</sup>ects two fundamentally different usages of the data. The organization labels as “prospects” (11,445 records, \~3% of the dataset), alumni who have given large gifts, or are assessed as having a potential for a large contribution. Prospects are not approached during regular campaigns, but have dedicated staff responsible for maintaining routine contact with them. Other donors, “non-prospects”, (346,927 records, \~97% of the dataset) are typically contacted (via phone, mail, or email) during pledge campaigns targeting a large donor base. (b) The Gifts dataset (1,415,432 records) captures the history of gift transactions, including the date and the amount, each linked to a speci<sup>fi</sup>c pro<sup>fi</sup>le. Our evaluation targets acquisition and maintenance decisions with respect to the Pro<sup>fi</sup>les dataset, while the Gifts dataset is used for assessing the utility of each pro<sup>fi</sup>le. To protect privacy and con<sup>fi</sup>dentiality, all gift amounts were multiplied by a positive constant.

## 2.4. Operationalizing model variables

## 2.4.1. Utility (U)

A possible conceptualization for the utility gained from information resources is the economic bene<sup>fi</sup>ts gained by improving the performance of business processes [1]. Accordingly, we see the revenues that a <sup>fi</sup>rm gains from data usage as a form of utility. In our case of the alumni-management system, pro<sup>fi</sup>le data and the associated gift records are used to solicit alumni with donation potential toward gaining revenues. Gift transactions re<sup>fl</sup>ect the outcome of such efforts and can be associated with individual pro<sup>fi</sup>les. A common assumption in CRM is that future purchases (in our case, gifts) can be largely predicted from past activities. A high consistency in gift-giving behavior was indeed found in the evaluated dataset — positive and signi<sup>fi</sup>cant correlations between annual amounts per donor for the most recent 5 years (2002–2006). Accordingly, we used the average annual dollar gift amount between 2002 and 2006 for measuring utility — 0 if a person has not donated within this time range and positive otherwise (Fig. 3). For non-prospects, the mean utility is \$6.70, and the proportion of pro<sup>fi</sup>les with 0 utility (i.e., no gifts within 2002–2006) is relatively high (\~88%). For prospects, the mean, \$1303.50, is substantially higher and the proportion of pro<sup>fi</sup>les with 0 utility (\~54%) is much lower, but not negligible.

## 2.4.2. Time span (T)

The time-span decision re<sup>fl</sup>ects an upper bound on record age. We calculate age and time span based on the difference between the yearof-activity and 2007 (the year following the last year of activity in the dataset), so time span is expressed in years (e.g., for a record with date 3/4/2004, the age is 2007–2004=3). Initially, we considered two different operationalizations of record age: (a) Append Age, based on the year in which a pro<sup>fi</sup>le record was added to the dataset (we used the year of graduation as a proxy, as a record is typically added at graduation), and (b) Audit Age, based on the Audit Date, which re<sup>fl</sup>ects the most recent audit to a pro<sup>fi</sup>le record (following an audit, some pro<sup>fi</sup>le attributes may change if a correction is needed, or remain unchanged if the pro<sup>fi</sup>le data is up-to-date). The distribution (Fig. 4a) and the cumulative proportion (Fig. 4b) of pro<sup>fi</sup>le records plotted against the append age and the audit age are shown in Fig. 4. The record count decreases with append age, and the associated curve appears to be nearly linear with a slight negative slope. The record count also decreases with audit age, but not at a steady rate, as at certain age range (between 9 and 13 years of age), the number of records increases (administrators con<sup>fi</sup>rmed extensive data maintenance activities during this period). Correspondingly, the dataset proportion (Fig. 4b) grows close to linearly with append age (conforming to proposition P1b), but not with audit age.

![](/api/attachments/TRRKMYEH/fulltext/images/e295123ff30e34e5ea59215a995c1fc3b1e109d44075d3b7d885d392c98fc980.jpg)  
Fig. 3. Utility distribution in alumni pro<sup>fi</sup>les.

Next, we examined the association between age and utility. The optimization model assumes that the marginal added utility declines with age. The utility versus age curves (Fig. 5) show fundamentally different behavior between the two age variables. Utility consistently declines with Audit Age, both for prospects and for non-prospects. Conversely, the trends along the Append Age are inconsistent, and certainly not declining. For non-prospects, utility tends to increase for the low-end of the age range then reaches a certain plateau and later decreases. Utility for prospects increases gradually — <sup>fi</sup>rst at a lower, and then at a higher rate.

We have chosen audit age as the baseline for our modeling of time span as we believe that audit age is a more sensible age variable to use. It is reasonable to assume that when an audit takes place, the audited

(b)  
![](/api/attachments/TRRKMYEH/fulltext/images/f2113cd0d5b789e2f922a27d959f9c3191fff5ecca34b4db9bfed94a89c12edf.jpg)

![](/api/attachments/TRRKMYEH/fulltext/images/d21dba65272ce64d2465c92ca91c4549586c1814821195005235c2606093c21a.jpg)  
Fig. 4. (a) Distribution and (b) cumulative proportion of pro<sup>fi</sup>le records versus age.

![](/api/attachments/TRRKMYEH/fulltext/images/83f7f9fa12b649fc3c397100b12807edded70af60618d267247dc32337c35edd.jpg)

![](/api/attachments/TRRKMYEH/fulltext/images/59f5845098ed508a6068e7518622800075abace6d2ba6339078637ab90e8bd5d.jpg)  
Fig. 5. Distribution of utility versus (a) audit and (b) append age.

record is superior to the original one. As explained later, this choice required an adjustment to the cost model, as we determined that the number of records increases, but not linearly, with the audit age.

## 2.4.3. Quality level (Q)

To measure DQ, we chose completeness, the proportion of nonmissing values (other quality dimensions can also be accommodated by the model, as mentioned before and discussed later). The completeness measure used is the number of non-missing attributes values divided by the total number of attributes (e.g., 0 when all attributes have missing values, 0.5 when half the values are missing, and 1 when none is missing). We considered a subset of fourteen attributes (Table 1) identi<sup>fi</sup>ed by managers as the most commonly used. We observed a high variability in the rates of missing values in the different attributes. Some attributes (i.e., School, Gender, and Marital Status) have high completeness, but the completeness of several others is considerably lower.

The rates of missing values in non-prospect records is higher (dramatically, in some cases) than the rates in prospect records. Accordingly, completeness scores are signi<sup>fi</sup>cantly higher for prospects (Fig. 6). On the average, a prospect record has \~15% of the attributes missing, while a non-prospect record has \~33% of the attributes missing. Only \~15% of prospect pro<sup>fi</sup>les and \~5% of nonprospect pro<sup>fi</sup>les have no missing attributes. Fig. 7 shows the average quality level versus audit age for prospects and for non-prospects. For prospects, the audit age ranges between 0 (most recent records) and 24 (oldest records), and the data quality level is relatively steady for the entire audit-age range. For non-prospects, the audit age ranges between 0 and 20. The data quality level is relatively steady for the most recent 15 years, but noticeably declines for older records. Completeness and utility are positively and signi<sup>fi</sup>cantly correlated, as shown and quanti<sup>fi</sup>ed later.

Impartial completeness in alumni pro<sup>fi</sup>les.

<table><tr><td rowspan="2">Attributes</td><td colspan="2">Prospects (11,445)</td><td colspan="2">Non-prospects (346,927)</td><td colspan="2">Overall (358,372)</td></tr><tr><td>Non-missing</td><td>Rate</td><td>Non-missing</td><td>Rate</td><td>Non-missing</td><td>Rate</td></tr><tr><td>Grad. year</td><td>11,445</td><td>1.000</td><td>346,903</td><td>0.999</td><td>358,348</td><td>0.999</td></tr><tr><td>School</td><td>11,445</td><td>1.000</td><td>346,903</td><td>0.999</td><td>358,348</td><td>0.999</td></tr><tr><td>Gender</td><td>11,415</td><td>0.997</td><td>343,675</td><td>0.991</td><td>355,090</td><td>0.991</td></tr><tr><td>Marital</td><td>11,129</td><td>0.972</td><td>309,159</td><td>0.891</td><td>320,288</td><td>0.894</td></tr><tr><td>Income</td><td>10,194</td><td>0.891</td><td>216,240</td><td>0.623</td><td>226,434</td><td>0.632</td></tr><tr><td>Ethnicity</td><td>7608</td><td>0.665</td><td>205,888</td><td>0.594</td><td>213,496</td><td>0.596</td></tr><tr><td>Religion</td><td>8669</td><td>0.757</td><td>208,329</td><td>0.601</td><td>216,998</td><td>0.606</td></tr><tr><td>Occupation</td><td>3933</td><td>0.344</td><td>49,891</td><td>0.144</td><td>53,824</td><td>0.150</td></tr><tr><td>H. address</td><td>11,350</td><td>0.992</td><td>319,853</td><td>0.920</td><td>331,203</td><td>0.924</td></tr><tr><td>H. country/state</td><td>11,345</td><td>0.991</td><td>319,726</td><td>0.922</td><td>331,071</td><td>0.924</td></tr><tr><td>H. phone</td><td>9410</td><td>0.822</td><td>196,087</td><td>0.565</td><td>205,497</td><td>0.573</td></tr><tr><td>B. address</td><td>9976</td><td>0.872</td><td>166,586</td><td>0.480</td><td>176,562</td><td>0.493</td></tr><tr><td>B. country/state</td><td>8818</td><td>0.771</td><td>115,570</td><td>0.333</td><td>124,388</td><td>0.347</td></tr><tr><td>B. phone</td><td>9386</td><td>0.820</td><td>126,981</td><td>0.366</td><td>136,367</td><td>0.381</td></tr><tr><td>Average</td><td></td><td>0.849</td><td></td><td>0.673</td><td></td><td>0.679</td></tr></table>

DQM literature has identi<sup>fi</sup>ed a number of important quality dimensions, such as accuracy, validity, reliability, and con<sup>fi</sup>dentiality ([13,25]). The model that we evaluate address completeness and currency — both were identi<sup>fi</sup>ed as key quality dimensions in the alumni system and can be relatively easily detected and measured. To clarify the terminology that we use in this study — the variable quality level (Q) relates to the completeness dimension alone. On the other hand, the measurement of the time span along the audit age, as described earlier, assesses the currency dimension, the extent to which data is up-to-date. We intend addressing other dimensions (particularly, accuracy) in our future work, as elaborated in the concluding section.

## 2.4.4. Cost (C)

Our cost assessment is based on estimates of variable acquisition and maintenance costs that were solicited from managers that are in charge of maintaining the data and/or supervise the departments that use the data. We identi<sup>fi</sup>ed a set of possible treatments for maintaining the alumni data and improving its quality (e.g., manually updating pro<sup>fi</sup>les, automatically searching of an external database, and hiring an agency for a thorough investigation — detailed discussion of speci<sup>fi</sup>c treatments is provided later). Cost estimations for these treatments must consider: (a) Maintenance objectives: cost estimations should re<sup>fl</sup>ect maintenance efforts and/or acquisition of external data to resolve missing values. (b) Treatment impact: each treatment would address only a subset of records and/or attributes and hence, provides only a partial solution, and (c) Sources of cost: variable costs can be attributed to the time needed to gather data on a donor and audit the records, the time needed to monitor an automated process and manually resolve certain issues, and/or payments made to external agencies when acquiring data.

![](/api/attachments/TRRKMYEH/fulltext/images/8bb73832637e25949c0b176d583856aa51382c7a1fb7772c02318362ba778015.jpg)  
Fig. 7. Quality vs. audit age.

This realization that each treatment handles only a subset of attributes, has led us to propose a cost evaluation method, which takes into account the quality level of each attribute separately. Our calculation of impact assumes that once a treatment is applied to the specific relevant subset of records and attributes, it resolves all the completeness issues within this subset (i.e., raises the completeness of the targeted subset to 1). We assume J possible treatments, indexed by [j], and denote by $R _ { j }$ the proportion of records addressed by treatment [j]. We also de<sup>fi</sup>ne $W _ { m , j } \ : - \ : \mathrm { a n }$ indicator of whether attribute [m] is addressed by treatment [j] $\mid ( W _ { m , j } = 1 )$ , or not $( W _ { m , j } = 0 )$ . We denote by $q _ { m }$ the current quality level of attribute [m], and assume that missing values for each attribute are distributed evenly among dataset records. That is, prior to the treatment, the quality level of attribute [m] in the targeted subset is approximately $q _ { m } .$ After applying the treatment [j], the quality level of attribute [m] for the entire dataset (not only the subset that was treated) can be approximated by $q _ { m , j } = W _ { m , j } R _ { j } +$ $( 1 - W _ { m , j } R _ { j } ) ^ { * } q _ { m } = q _ { m } + W _ { m , j } R _ { j } ( 1 - q _ { m } ) ,$

The quality level $Q _ { j }$ of the entire dataset after applying treatment [ j] is the average of the $\{ q _ { m , j } \} \colon$

$$
Q _ {j} = (1 / M) \sum_ {m = 1 \dots M} q _ {m, j} = (1 / M) \sum_ {m = 1 \dots M} \left(q _ {m} + W _ {m, j} R _ {j} \left(1 - q _ {m}\right)\right),\tag{4}
$$

![](/api/attachments/TRRKMYEH/fulltext/images/71f588d2f1eba0c522e72181f570748469aaa4da21a5d3607e6816001ce4721d.jpg)  
Fig. 6. Completeness distribution.

where,

Q — The dataset quality level that can be obtained by treatment [ j] M — The total number of attributes (indexed by [m])

$q _ { m }$ — The current quality level (proportion of non-missing values) of attribute [m]

$q _ { m , j } -$ The quality level of attribute [m] that can be reached after applying treatment [ j]

$R _ { j } -$ The proportion of records addressed by treatment [j] $\dot { W } _ { m , j } \mathrm { ~ - ~ } \mathsf { A n }$ indicator of whether attribute [m] is addressed by treatment [ j] (=1), or not (=0).

Notably, the expression $( 1 / M ) ~ { \sum m = 1 } \dots M ~ q _ { m }$ re<sup>fl</sup>ects the current quality level $Q ^ { S }$ guaranteed by the data source (as denoted earlier in $\operatorname { E q . } \ \left( 1 \right) )$ . Eq. (4) can therefore be rewritten as: $Q _ { j } = Q ^ { S } +$ $\begin{array} { r } { \big ( R _ { j } / M \big ) \sum _ { m = 1 \dots M } W _ { m , j } ( 1 - q _ { m } ) = Q ^ { S } + \Delta _ { j } , } \end{array}$ w h e r e , $\Delta _ { j } = \left( R _ { j } / M \right)$ $\textstyle \sum _ { m = 1 \ldots M } W _ { m , j } ( 1 - q _ { m } ) ,$ <sup>ð Þ</sup>, is the quality improvement gained from treatment [ j].

Given an average variable cost per record of $\dot { \mathbf { \rho } } _ { c _ { j } }$ for treatment [ j], the overall variable cost $C _ { j } ,$ for treatment [ j] can be calculated as:

$$
C _ {j} = R _ {j} N c _ {j},\tag{5}
$$

where,

C — The overall variable cost for a treatment [ j]

N — The total number of records in the dataset

$R _ { j } -$ The proportion of records addressed by the treatment [ j]

$c _ { j } -$ Quality improvement cost per record for treatment [ j].

The treatments considered for improving quality (i.e., increasing completeness), are summarized in Table 2 (<sup>fi</sup>rst column). The second and third columns provide estimates of the dataset proportion (R ), and the attributes $\{ W _ { m , j } \}$ addressed by each treatment, respectively. Based on these, and on the estimates of current quality rates per attribute (in Table 1), we use Eq. (4) to calculate the quality improvement $( \varDelta _ { j } ) _ { \cdot }$ , and the quality improvement ratio, $Q _ { j } / Q ^ { S }$ , used later for estimating model parameters. The estimates of average cost per record (column 6, Table 2) are based on the work-time needed to treat each record (calculated as the average work minutes required to handle a single record times a certain <sup>fi</sup>xed dollar amount per minute) and/or fees paid to external agencies. Finally, we calculate the overall cost (column 7, Table 2), using Eq. (5).

The following treatments, listed in Table 2, were described by the alumni system managers and their impact and cost were estimated:

1. New profiles — At the academic year-end, pro<sup>fi</sup>les of students who just graduated are uploaded automatically from the registration system. Some manual intervention is needed to validate and correct rejections that typically occur due to missing attribute values.

2. Gift payments — Mailed payments typically include a form on which a graduate indicates current home address and phone number. Regardless of whether the forms indicate changes — the employees receiving the envelopes validate the details in the form against the alumni database.

3. Gift match — Business address and occupation can be obtained from gift match forms, but such forms are received only from a small proportion of the pro<sup>fi</sup>les.

4. Solicitation — Addresses and phone numbers (home and business) are typically veri<sup>fi</sup>ed when a person responds to a phone solicitation.

5. NCOA (New Changes of Address) — The USPS offers free access to the NCOA database, which lists the history of changes in US addresses. A process in the alumni system searches the NCOA database automatically for all US-based pro<sup>fi</sup>les (\~87% of the dataset) and typically, can successfully update \~90% of those pro<sup>fi</sup>les (overall, \~78% of the dataset). Though the process is automatic, some manual veri<sup>fi</sup>cation of rejections and failures is required.

6. Lost track — Agencies have been hired in the past for correcting pro<sup>fi</sup>les marked as “lost track” — alumni with no valid address. The system administrators would direct to this service only records that could not be corrected with the NCOA-search process.

7. Alumni survey — A recent alumni survey that reached approximately 30% of the pro<sup>fi</sup>les dataset permitted us to estimate survey cost. The surveyed person is typically approached via email <sup>fi</sup>rst, then by phone or by mail if needed. The estimated average cost per records includes both the mailing cost, and the time needed to update the database.

8. Investigation — As implied, most current methods result in relatively minor improvements to quality; hence, they do not permit precise cost estimation along the entire range $[ \bar { Q } ^ { S } , 1 ] ( \mathrm { i . e . }$ between current quality $Q = Q ^ { S }$ , and perfect quality $Q = 1 )$ Targeting high quality (e.g., beyond $Q = 0 . 9 )$ requires comprehensive investigation — searching the web, hiring external agencies, or assigning a contact person. None of these methods was used in the past and associated costs have high variability. We could not, hence, estimate these costs precisely. The estimate for alumni that reside in English-speaking countries (\~90% of the dataset) was based on the average fee charged by web-based investigation services. Data administrators indicated that investigating alumni living in other countries is impractical.

As discussed later, our estimates indicate a steep increase in costs between minor improvements to current quality, and major improvements that target a very high quality.

## 3. Results — model estimation and optimization

The decision variables in the optimization model (Eq. (1)) – time span (T) and quality level (Q) – are subject to constraints: $0 \le T \le T ^ { S }$ and $Q ^ { S } { \leq } Q { \leq } 1 , ( T ^ { S }$ and $Q ^ { S }$ being the time span and the quality level respectively, offered by the source). The optimum con<sup>fi</sup>guration point $( T ^ { o \dot { p } T } , Q ^ { o P T } )$ is not affected by the <sup>fi</sup>xed costs; hence, we initially omit the <sup>fi</sup>xed cost parameter $C ^ { F } .$ However, later in the evaluation process, we verify that the net-bene<sup>fi</sup>t gain at the optimum con<sup>fi</sup>guration point is suf<sup>fi</sup>ciently high to justify the anticipated <sup>fi</sup>xed cost. The optimal con<sup>fi</sup>guration analyzed here is based on a time horizon of 1 year, and can be re-evaluated for different horizons.

Table 2 Variable cost estimations.

<table><tr><td>Treatment</td><td>Prop. of profiles ( $R_j$ )</td><td>Attributes addressed $^a$ </td><td>Quality impr. ( $\Delta_j$ )</td><td>Impr. ratio ( $Q_j/Q^S$ )</td><td>Avg. cost per record ( $c_j$  in $)</td><td>Overall cost ( $C_j$ , in $)</td></tr><tr><td>1. New profiles</td><td>0.02</td><td>Grad. school and year, gender, marital status, religion, ethnicity, H. address and phone</td><td>0.0021</td><td>1.0031</td><td>2.25</td><td>16,127</td></tr><tr><td>2. Gift payments</td><td>0.05</td><td>H. address and phone</td><td>0.0021</td><td>1.0030</td><td>2</td><td>35,837</td></tr><tr><td>3. Gift match</td><td>0.002</td><td>B. address and occupation</td><td>0.0005</td><td>1.0007</td><td>3</td><td>2150</td></tr><tr><td>4. Solicitation</td><td>0.01</td><td>H./B. address and phone</td><td>0.0012</td><td>1.0025</td><td>5</td><td>17,919</td></tr><tr><td>5. NCOA</td><td>0.78</td><td>H. address</td><td>0.0085</td><td>1.0125</td><td>0.2</td><td>62,357</td></tr><tr><td>6. Lost track</td><td>0.10</td><td>H. address</td><td>0.0011</td><td>1.0016</td><td>2.5</td><td>89,593</td></tr><tr><td>7. Alumni survey</td><td>0.30</td><td>All</td><td>0.0962</td><td>1.1417</td><td>5</td><td>537,558</td></tr><tr><td>8. Investigation</td><td>0.90</td><td>All</td><td>0.2887</td><td>1.4250</td><td>40</td><td>12,901,392</td></tr></table>

<sup>a</sup> Address correction includes also the country and/or state.

## 3.1. Utility model estimation

Utility is modeled as a product of components: $u ( 1 - e ^ { - \alpha T } ) Q ^ { \lambda } .$ . The component, (u), is the utility at T→∞ and $Q = 1$ . The others are within [0,1], where $( 1 - e ^ { - \alpha T } )$ re<sup>fl</sup>ects utility degradation due to limiting the time span, and $Q ^ { \lambda }$ re<sup>fl</sup>ects utility degradation due to quality defects. We now estimate the associated parameters (u, α, and λ). The cumulative utility as a function of T can be written as: $U ( T ) = A ( 1 - e ^ { - \alpha T } )$ , where $A { = } u Q ^ { \lambda }$ is the utility when T approaches in<sup>fi</sup>nity (the difference in U(T) between $T = T ^ { S }$ , the upper bound, and T→∞ is negligible). When dividing both sides by A, the result is $U ( T ) / A = 1 - e ^ { - \alpha T }$ , a cumulative utility proportion curve (Fig. 8a) as a function of T (i.e., the ratio between $U ( T ) ,$ the utility as a function of T and A, the utility at T→∞ and $Q = 1 )$ This expression can be log-transformed to $L n ( 1 - U ( T ) / A ) = - \alpha T .$ Using an ordinary least-squares regression through the origin after the natural-log transformation, the estimated sensitivity parameter for prospects is $\alpha { = } 0 . 4 7$ (equivalent to an annual decline rate of \~38%), and $\alpha { = } 0 . 2 9$ for non-prospects (\~25% annual decline). Both estimates were statistically signi<sup>fi</sup>cant (P-value: \~0, adjusted R-SQR above 0.9). In essence, we have used a regression model of $\begin{array} { r } { \mathtt { Y } = \mathtt { \beta } \mathtt { X } + \mathtt { \varepsilon } , } \end{array}$ where $\mathrm { Y } { = } L n ( 1 { - } U ( T ) / A ) , \mathrm { X } { = } T ,$ and $\beta = - \alpha .$

![](/api/attachments/TRRKMYEH/fulltext/images/710679eac143f8fabff8153ad623012e58bbc395f0fc0a9baa25fdb484f5f9e4.jpg)

![](/api/attachments/TRRKMYEH/fulltext/images/4a3cde36f51e323c4eebed88afc37dd9056d28d6a09c7fca8e5f407c7fa63752.jpg)  
Fig. 8. Cumulative utility proportion versus (a) time span (T), and (b) quality level (Q).

Utility as a function of Q can be written as $U ( Q ) = A Q ^ { \lambda }$ , where $A { = } u ( 1 { - } e ^ { - \alpha T } )$ is the utility when $Q = 1$ . When dividing both sides by A, the result is $U ( Q ) / A = Q ^ { \lambda }$ , a cumulative utility proportion curve (Fig. 8b) as a function of Q (i.e., the ratio between $U ( Q )$ , the utility as a function of Q, and A, the utility at $Q = 1 )$ . This expression can be logtransformed to $L n ( U ( Q ) / A ) = \lambda L n ( Q )$ , where $U ( \mathbb { Q } ) / A$ is the proportion between the utility at a certain Q and utility at $Q = 1$ . The cumulative utility proportion curves versus Q are shown in Fig. 8b. Again, using an ordinary least-squares regression through the origin after the natural-log transformation (see the model described previously, with $\textrm { Y } \ \mathrm { n o w } = L n ( U ( Q ) / A$ , X now = Ln(Q), and β now = λ), the estimated sensitivity parameter for prospects is $\lambda { = } 0 . 8 9$ (equivalent to a utility decline of \~46% at $Q = 0 . 5 )$ . This estimate is signi<sup>fi</sup>cant (P-value of \~0.01), but with a relatively low adjusted R-SQR (\~0.44). This can be explained by the inconsistent increase in utility with quality, for prospects. For non-prospects, the sensitivity parameter is $\lambda { = } 4 . 6 1$ (utility decline of \~92% at $Q = 0 . 5 )$ This statistically signi<sup>fi</sup>cant estimate $( { \mathrm { P - V a l u e } } ; \sim 0 ,$ , adjusted R-SQR: 0.65) indicates that non-prospect records are more vulnerable to quality defects and consistently have more missing values, compared to prospects.

The parameter u is the maximum utility obtainable with the entire time span (T→∞) and perfect quality $( Q = 1 )$ . It can be calculated by transforming the utility expression to $\stackrel { \cdot } { u } = U ^ { * } [ ( 1 - e ^ { - \alpha T ^ { * } } ) Q ^ { * \lambda } ] ^ { - 1 } ,$ where $U ^ { * }$ is the utility at a known con<sup>fi</sup>guration point $[ T ^ { * } , Q ^ { * } ] .$ The total utility is estimated at \$14,918,461 for prospects and at \$2,318,667 for non-prospects. These numbers are based on the entire time span, at quality levels of 0.849 and 0.673 respectively (the weighted average of quality for the entire dataset, $Q ^ { S } = 0 . 6 7 9 )$ ). Using the transformed utility expression, the maximum utility parameter (i.e., with perfect quality, $Q = 1 )$ can be estimated a $\cdot u = \mathbb { S } 1 7 , 2 4 0 , 1 5 6$ for prospects and $\boldsymbol { u } = \$ 14,631,68 3$ for non-prospects.

## 3.2. Cost model estimation

The variable cost model $C ^ { V } { = } c ^ { V } ( Q / Q ^ { S } ) ^ { \delta } T$ assumes that the number of records N grows linearly at a <sup>fi</sup>xed rate with T. In the alumni data, the N grows at a decreasing rate with T. Hence, we consider an exponential approximation instead: $N ( T ) = N M ( 1 - e ^ { - \tau T } )$ , where NM=358,372 (the total number of records). The variable cost model is revised to $C ^ { V } { = } c ^ { V } ( Q / Q ^ { S } ) ^ { \delta } ( 1 { - } e ^ { - \tau T } )$ and, using log regression, the decline parameter is estimated at τ=0.19 (P-value: \~0, adjusted R-SQR: 0.67). The variable cost model can be rewritten as $C ^ { V } { = } A ( Q /$ $Q ^ { S } ) ^ { \delta }$ , where $A { = } N M c ^ { V } ( 1 { - } e ^ { - \tau } )$ represents the cost for the entire dataset at $Q = Q ^ { S } ,$ , and δ re<sup>fl</sup>ects the increase in cost for a higher Q. This can be log-transformed to Ln $\cdot C ^ { V } ( Q ) ) = L n ( A ) + \delta L n ( Q / Q ^ { S } )$ . Using our cost estimations (Table 2) and log–log regression, the estimated costsensitivity parameter is $\delta = 1 8 . 8$ (a sharply-convex curve), and $A = 2 2 , 2 4 5$ (P-value: 0.002, adjusted R-SQR: 0.781).

## 3.3. Optimizing net-benefit

To understand the impact of optimizing the net-bene<sup>fi</sup>t, we evaluate nine policies (Table 3) using the optimization model (Eq. (1)) with the estimated parameters.

The net-benefit curve is shown in Fig. 9a, and the relative positions of the decision policies in Table 3 are shown in Fig. 9b. The optimization results (using Excel's Solver) were validated against the closed-form solutions (Eqs. (2) and (3)).

The optimum (policy $I , ~ T = 1 5 . 6 , ~ Q = 0 . 8 7 , ~ B = 2 0 . 3 ~ \mathrm { M } )$ , is an interior point within the design space de<sup>fi</sup>ned by all possible con<sup>fi</sup>gurations. The net-bene<sup>fi</sup>t at the optimum is signi<sup>fi</sup>cantly higher than at the corner points (policies A, B, C, and D) which represent maximization and/or minimization of T or Q (notably, maximizing both T and Q will result in a net-loss). As expected, the net-bene<sup>fi</sup>t from optimizing the time span alone for minimum or maximum quality (policies G and H respectively) is lower than the net-bene<sup>fi</sup>t from jointly optimizing both. The same holds for optimizing the quality level for minimum or maximum time span (policies E and F, respectively). Compared to policy F (optimizing Q for $T = 2 4 )$ , the improvement is negligible, but all other improvements are relatively large.

Table 3  
Optimizing the time span (T) and the quality level (Q)

<table><tr><td>A. Decision policy</td><td>T</td><td>Q</td><td>Utility (U)</td><td>Cost (C)</td><td>N.B. (B)</td></tr><tr><td>B. Current - keep T at a maximum, accept current Q</td><td>24</td><td>0.68</td><td>14.7 M</td><td>~0 M</td><td>14.7 M</td></tr><tr><td>C. Minimize - accept current Q, limit T to 1 year</td><td>1</td><td>0.68</td><td>5.2 M</td><td>~0 M</td><td>5.2 M</td></tr><tr><td>D. Maximize - target the maximum possible T and Q</td><td>24</td><td>1</td><td>31.9 M</td><td>37.0 M</td><td>-5.1 M</td></tr><tr><td>E. Minimize T, but maximize Q</td><td>1</td><td>1</td><td>10.1 M</td><td>6.4 M</td><td>3.7 M</td></tr><tr><td>F. Minimize T and optimize Q</td><td>1</td><td>0.90</td><td>8.1 M</td><td>0.8 M</td><td>7.3 M</td></tr><tr><td>G. Maximize T and optimize Q</td><td>24</td><td>0.87</td><td>22.8 M</td><td>2.6 M</td><td>20.2 M</td></tr><tr><td>H. Minimize Q and optimize T</td><td>24</td><td>0.68</td><td>14.7 M</td><td>~0 M</td><td>14.7 M</td></tr><tr><td>I. Maximize Q and optimize T</td><td>2.7</td><td>1</td><td>20.5 M</td><td>14.9 M</td><td>5.6 M</td></tr><tr><td>J. Optimal - optimize T and Q, simultaneously</td><td>15.6</td><td>0.87</td><td>22.9 M</td><td>2.6 M</td><td>20.3 M</td></tr></table>

## 3.4. Sensitivity analysis

First Q is <sup>fi</sup>xed at $Q ^ { O P T } = 0 . 8 7$ and the effect of changing T is shown in Fig. 10a and summarized in Table 4. The sensitivity of net-bene<sup>fi</sup>t to changes in T around the optimum is very small — the decline in netbene<sup>fi</sup>t is negligible within 3 years from the optimal time span $T ^ { O P T } .$

Second, T is <sup>fi</sup>xed at $T ^ { O P T } = 1 5 . 6 .$ The effect of changing Q is shown in Fig. 10b and summarized in Table 5. The sensitivity to changes in Q around the optimum is more impactful compared to T. For Q within [0.85, 0.9], the net-bene<sup>fi</sup>t reduces by 3% or less. For Q between [0.8, 0.95] the decline reaches \~29% and reducing or increasing Q beyond this range results in a big decline in net-bene<sup>fi</sup>t, or even in a net-loss.

![](/api/attachments/TRRKMYEH/fulltext/images/22103d7772b2abdc7e35a82b2d3a101707d1ad1327e2c71370ed5f93c4998e43.jpg)

![](/api/attachments/TRRKMYEH/fulltext/images/d4f74dd6c2b1ce1c7cb7f788345faba6d425070214b46c550ad5835538fe9bae.jpg)  
Fig. 9. (a) The net-bene<sup>fi</sup>t curve, and (b) the position of the decision policies.

Net-bene<sup>fi</sup>t can be further improved by treating prospect and nonprospect pro<sup>fi</sup>les as two distinct datasets and optimizing each subset, separately. Optimizing prospects <sup>fi</sup>rst, the optimal con<sup>fi</sup>guration is $T = 2 0$ and Q=1 and the associated net-bene<sup>fi</sup>t is $B { = } 1 7 . 2 \mathrm { M } .$ . This implies that for prospects it would be bene<sup>fi</sup>cial to invest in bringing the entire time range of data, to the maximum possible data quality — i.e., an effort should be made to <sup>fi</sup>ll in all the missing data for prospects. For non-prospects, the optimal con<sup>fi</sup>guration is T=16.7 and $Q { = } 0 . 8 4$ with a net-bene<sup>fi</sup>t of B=5 M. The total net-bene<sup>fi</sup>t is $B { = } 2 2 . 2 \ \mathrm { M } , { \sim } 9 \%$ higher than the net-bene<sup>fi</sup>t of $B { = } 2 0 . 3 \ : \mathrm { M }$ gained by optimizing both usages and datasets combined (i.e., without segmenting).

(a)  
![](/api/attachments/TRRKMYEH/fulltext/images/d89beb8b68a39e4224214cfdbc9b3084f3aaa14d61058b502f274e7cae82687f.jpg)

(b)  
![](/api/attachments/TRRKMYEH/fulltext/images/202bf9a4d6c2270750136b21690f9ee7ada34a6aeb6b1b86740bafe81d394d07.jpg)  
Fig. 10. Sensitivity charts: (a) time span (T, at Q=0.87), and (b) quality (Q, at T=15.6).

Table 4  
Sensitivity to time-span variation (at Q=0.87).

<table><tr><td>Time span (T)</td><td>Net-benefit (B)</td><td>Difference from optimum</td><td>Decline (%)</td></tr><tr><td>13</td><td>20,250,384</td><td>-22,256</td><td>0.11</td></tr><tr><td>14</td><td>20,265,628</td><td>-7012</td><td>0.03</td></tr><tr><td>15</td><td>20,271,795</td><td>-845</td><td>0.00</td></tr><tr><td>15.6 (optimum)</td><td>20,272,640</td><td>0</td><td>0.00</td></tr><tr><td>16</td><td>20,272,362</td><td>-278</td><td>0.00</td></tr><tr><td>17</td><td>20,269,611</td><td>-3029</td><td>0.01</td></tr><tr><td>18</td><td>20,265,028</td><td>-7612</td><td>0.04</td></tr></table>

## 3.5. Summary and recommendations

Our objective was to evaluate the model for optimizing the con<sup>fi</sup>guration of tabular datasets in a real-world setting and to assess its potential contribution to better DQM of data resources. The evaluation indicates a need to improve the quality of alumni data. Many pro<sup>fi</sup>le records are not up to date (an average audit age of \~7 years), and the proportion of missing values is high (\~33% for the evaluated attributes). The evaluation shows that these DQ issues are strongly and signi<sup>fi</sup>cantly associated with lower utility. Utility declines by \~35% for prospects and \~25% for non-prospects for every year the pro<sup>fi</sup>le data is not audited, and drops signi<sup>fi</sup>cantly with missing values in key attributes. The evaluation also showed a strong and signi<sup>fi</sup>cant association between quality and cost. Marginally improving quality or maintaining the dataset as is, involves relatively low costs. However, achieving higher levels of quality requires implementing comprehensive methods at a signi<sup>fi</sup>cantly higher cost.

Net-bene<sup>fi</sup>t optimization using the tabular dataset model suggests that data improvement should focus on pro<sup>fi</sup>les that have been audited in the most recent \~15 years, and target a quality level of 0.87 (i.e., less than perfect quality, allowing an average rate of missing values to be \~13%). As indicated by our analysis of the impact and the cost of possible treatments (Table 2), such quality level (.87) can be achieved only with comprehensive investigation — e.g., internet search, specialized agency, or a contact person. Such data acquisition and maintenance efforts require large investments in time and/or monetary resources. Hence, pragmatically, they cannot be applied to all pro<sup>fi</sup>le records. Reaching alumni living abroad to collect missing data is expensive and often impossible, as indicated by the system administrators. The sensitivity to quality level was high around the optimal point. On the other hand, sensitivity to time span was minimal — increasing or decreasing the optimal point by a few years is unlikely to signi<sup>fi</sup>cantly degrade net-bene<sup>fi</sup>t. The net-bene<sup>fi</sup>t obtainable from the <sup>fi</sup>nal solution (\$20.3 M) is positive and materially higher than the net-bene<sup>fi</sup>t obtainable by keeping the current status unchanged (\$14.7 M). This difference (\$5.6 M) may more than compensate any <sup>fi</sup>xed cost associated with data acquisition and maintenance (e.g., programming efforts). Therefore the overall bene<sup>fi</sup>t is likely to stay highly positive even accounting for <sup>fi</sup>xed costs. The evaluation highlights a signi<sup>fi</sup>cant difference between the utility of pro<sup>fi</sup>les classi<sup>fi</sup>ed as prospects versus that of non-prospects. Accordingly, the optimization results indicate that the overall netbene<sup>fi</sup>t can be further improved (by \~9%) if these two subsets are managed (i.e., optimized) separately.

Table 5  
Sensitivity to quality level variation (at T=15.6).

<table><tr><td>Quality level (Q)</td><td>Net-benefit (B)</td><td>Difference from optimum</td><td>Decline (%)</td></tr><tr><td>0.75</td><td>17,032,334</td><td>-3,240,306</td><td>15.98</td></tr><tr><td>0.8</td><td>18,778,902</td><td>-1,493,739</td><td>7.37</td></tr><tr><td>0.85</td><td>20,098,903</td><td>-173,737</td><td>0.86</td></tr><tr><td>0.875 (optimum)</td><td>20,272,640</td><td>0</td><td>0.00</td></tr><tr><td>0.9</td><td>19,730,725</td><td>-541,915</td><td>2.67</td></tr><tr><td>0.95</td><td>14,433,327</td><td>-5,839,313</td><td>28.80</td></tr><tr><td>1</td><td>-3,597,603</td><td>-23,870,243</td><td>117.75</td></tr></table>

## 3.6. Assessing the optimization model

A core objective of our evaluation was to assess the extent to which the tabular dataset model can effectively assist DQM. The results indicate that the evaluation criteria were met to a great extent. We explicitly address the four criteria set forth earlier:

Feasibility: Construct operationalization was shown to be feasible, and all decision variables could be operationalized. Time span was conceptualized as setting an upper-limit on record age, and the proportion of missing values was used as an impartial quality measure. The same is true for the dependent measures — a monetary utility could be assigned to each record based on gift history, and variable data acquisition and maintenance costs could be associated with speci<sup>fi</sup>c records. All variables and measures could be operationalized at the record level and hence, all model parameters could be estimated with a relatively high reliability. Representability: The model propositions were supported to a great extent: (P1a) Utility increases with a higher time span at a diminishing rate — the exponentially-diminishing marginal utility assumption was strongly supported by the curve approximatio along audit age. (P1b) Variable cost increases with a higher time span at a linear rate — variables costs, in the original proposed model, were assumed to grow linearly with the number of records; however, the record count was found to grow non-linearly with T. This was easily resolved by adjusting the cost model, using an exponential form. (P2a) Utility increases with a higher quality level to a certain power — this was con<sup>fi</sup>rmed by the approximated curves. Interestingly, the utility-versus-quality curve for prospects was concave (0bλb1) and relatively inconsistent (relatively low adjusted R-SQR), while the curve for non-prospects was convex (λ N 1) and fairly consistent, indicating signi<sup>fi</sup>cantly different sensitivity of utility to quality degradation. A possible explanation for this <sup>fi</sup>nding, which was proposed in a discussion with th alumni-data administrators, was that the on-going contacts wit prospects rely on other complementary data sources — prospects are typically assigned with dedicated stuff members, who collect and manage detailed data on them in a separate system and, therefore, the utility for prospects is less sensitive to missing dat in the alumni data. On the other hand, for non-prospects, all solicitation efforts are based entirely on the alumni database; hence, the higher sensitivity to missing data. (P2b) Variable cost increases with a higher quality level to a certain power — this was con<sup>fi</sup>rmed by the cost estimates. The estimated sensitivit parameter δ=18.8 indicates a steep increase in variable costs when targeting very high quality levels.

Impact: The model's impact on data acquisition and maintenance decisions was shown to be high and signi<sup>fi</sup>cant. The results indicated an interior optimal point with respect to the con<sup>fi</sup>guration of T and Q, and the net-bene<sup>fi</sup>t associated with this optimum is materially higher than the net-bene<sup>fi</sup>t of each of the four cornersolutions (one of which is currently implemented in the alumni system).

Generalizability: The optimization affects policies that govern data acquisition and maintenance. Identifying and implementing these policies will require developing administrative tools for monitoring the quality of data and for improving it. However, the optimization results show no signi<sup>fi</sup>cant effect on the system design. The results do not suggest changes to the storage structure (tabular), the data model, or the data volumes to be stored. It, thus, does not affect the selection of data management technology. The results also do not change the volumes of data to be processed or data delivery requirements. It will, hence, have little effect on the selection of data processing and delivery technologies.

The results can inform the development of quality improvement policies, beyond the con<sup>fi</sup>guration of datasets. As prospect classi<sup>fi</sup>cation appears critical, data administrators should consider managing prospects in a separate dataset with a richer set of attributes. The high sensitivity of utility to DQ also demands the development of tools for communicating quality measurements to end users. It further indicates the need to systematically involve users when auditing and updating data. The numerical results in this evaluation are contextspeci<sup>fi</sup>c and cannot be generalized. However, the evaluation methodology can be generalized to other contexts, with some adjustments. A similar methodology can be reasonably applied in other CRM environments, in which customer pro<sup>fi</sup>les can be associated with purchases. In other contexts (e.g., healthcare, banking, insurance, or scienti<sup>fi</sup>c research) measuring utility and linking it to speci<sup>fi</sup>c records can be challenging and will require further investigation.

## 3.7. Limitations and future research

Our analysis is not without limitations, and some of these limitations suggest directions for extending this work in the future. First, the operationalization and the measurement of the model's outcome variables – utility and cost – can be improved. While the cost of minor quality improvements could be assessed with reasonable precision, the cost of major improvements could only be estimated. Utility, a key model construct, was aggregated along two usage categories — prospects and non-prospects. Utility analysis can be further re<sup>fi</sup>ned to consider usage by different departments or by allocating utility to speci<sup>fi</sup>c pledge campaigns. Such enhancements will require collecting additional data such as assessments of the costs associated with contacting donors and managing campaigns. Further, our dataset optimization considered existing usages only. An important resource, such as the data collected in the alumni system, introduces an opportunity to gain additional utility by re<sup>fi</sup>ning existing usages, or by developing new types of usage. These opportunities should be further explored and considered.

The evaluation described is based on a subset of alumni pro<sup>fi</sup>les (\~40%) and considered only fourteen pro<sup>fi</sup>le attributes — establishing robust DQM policies may require further evaluation of the entire set of attributes in the data resource. The actual dataset contains more attributes that may materially affect utility and cost (although using the entire set of attributes can only increase the optimal net-bene<sup>fi</sup>t — otherwise, the model will simply indicate to keep them as they are, which is the current situation when the other attributes are not used). The time span was based on the audit age of the record, which was shown to have high association with utility. The alumni system includes timestamps that can be linked to speci<sup>fi</sup>c attributes. Evaluating the audit age along speci<sup>fi</sup>c attributes instead of record level, can potentially enhance the model and the insights gained. The evaluation focused only on data acquisition and maintenance and may offer important insights to guide decisions in that area. However, it does not provide a thorough solution for managing DQ in complex data environments, which may involve many other design and con<sup>fi</sup>guration factors.

Our quality assessment focused on two commonly used quality dimensions — currency, re<sup>fl</sup>ecting the degree of data being up-to-date, and completeness, re<sup>fl</sup>ecting the existence of missing values. Obviously, developing more comprehensive and complete data maintenance policies will require modeling and measuring the impact of other quality defects (e.g., the accuracy and the validity of values). When evaluating the alumni database, we did not have explicit information on the level of accuracy in non-missing data, as there was no accurate baseline to compare to. However, it would be reasonable to assume a higher likelihood of inaccuracy defects in data that has not been audited recently (this has been con<sup>fi</sup>rmed by the managers who were involved in the evaluation process). The lack of a baseline that would permit assessing accuracy ef<sup>fi</sup>ciently is a common issue in many real-world data management environments [13]. Studies have suggested basing such assessment on statistical sampling (e.g., [22,24]). However, even a sample-based solution for assessing accuracy may turn out to be costly in a large-scale database; hence, some more research is required to address the accuracy-assessment issue methodologically. Further, with respect to data quality modeling — based on our <sup>fi</sup>ndings, we would suggest that increasing the granularity of the quality-variable (Q) de<sup>fi</sup>nition can be very useful. The current model optimizes a single variable (Q), which re<sup>fl</sup>ects the proportion of nonmissing values in the entire dataset. Our <sup>fi</sup>ndings indicate that completeness rates signi<sup>fi</sup>cantly vary among the different attributes (Table 1) and that different quality treatments target different subsets of attributes. Therefore, a useful re<sup>fi</sup>nement to our model would be to de<sup>fi</sup>ne a set of variables $\{ Q _ { m } \}$ (one per attribute) and optimize each separately.

Finally, our model does not address the issue of determining optimal marketing actions (e.g., how often to best solicit, which media to use to best solicit, etc.). We considered these issues as being outside of our study's context. A useful extension of our work may be to address these issues jointly with the evaluation of the proposed model.

## 4. Conclusions

This study is motivated by the notion that DQM can bene<sup>fi</sup>t from understanding the link between quality con<sup>fi</sup>guration decisions and economic outcomes such as utility, costs, and net-bene<sup>fi</sup>ts. In this study, we examine this notion in the context of managing alumni data, a context in which utility/cost tradeoffs are signi<sup>fi</sup>cantly affected by DQM con<sup>fi</sup>guration choices. We evaluated a model for optimizing the con<sup>fi</sup>guration of a tabular dataset within this context. Our evaluation shows that all model variables can be operationalized and that most model assumptions are supported. Our evaluation also con<sup>fi</sup>rms that the model can have a strong impact on associated economic bene<sup>fi</sup>ts.

This study offers insights into and its results have implications for, other contexts. IS environments are complex and involve many decisions that are linked to utility-cost tradeoffs. A key challenge in economics-driven evaluation is the conceptualization of economic outcomes. The monetary utility measurement used in this study is applicable to CRM. Other business domains (e.g., <sup>fi</sup>nance, healthcare, insurance, human-resources) may need different ways of conceptualizing and measuring utility. With appropriate utility measurements, the proposed model may be used for optimizing design con<sup>fi</sup>gurations in these areas. Conceptualizing and estimating costs can be challenging as well. As highlighted by our evaluation, the cost of data management activities that have not been previously implemented is dif<sup>fi</sup>cult to assess. Further, IS implementation often involves intangible costs, such as those associated with shifts in motivation, technology-adoption, and/or political struggles.

Our evaluation highlights the need for a broader perspective of DQM. So far, research in this <sup>fi</sup>eld tended to emphasize functional and technical perspectives. These are, no doubt, critical to successful DQM. However, the results of our evaluation indicate the need to methodically address the economic aspects involved in DQM con<sup>fi</sup>guration and on-going maintenance. Our study also emphasizes DQM as a continuous process and not a one-time effort. We view our study and its results as a step that justi<sup>fi</sup>es the inclusion of economic perspectives in managing the quality of data resources.

## References

[1] N. Ahituv, A systematic approach towards assessing the value of information system MIS Ouarterly 4 (4) (1980) 61–75

[2] A. Avenali, C. Batini, P. Bertolazzi, P. Missier, Brokering infrastructure for minimum cost data procurement based on quality–quantity models, Decision Support Systems 45 (1) (2008) 95–109.

[3] D.P. Ballou, H.L. Pazer, Designing information systems to optimize the accuracytimeliness tradeoff, Information Systems Research 6 (1) (1995) 51–72.

[4] D.P. Ballou, H.L. Pazer, Modeling completeness versus consistency tradeoffs in information decision contexts, IEEE Transactions on Knowledge and Data Engineering 15 (1) (2003) 240–243.

[5] D.P. Ballou, R. Wang, H. Pazer, G.K. Tayi, Modeling information manufacturing systems to determine information quality, Management Science 44 (4) (1998) 462–484.

[6] P.D. Berger, M. Eechambadi, G.D. Lehmann, R. Rizley, R. Venkatesan, From customer lifetime value to shareholder value: theory, empirical evidence, and issues for further research, Journal of Services Research 9 (2) (2006).

[7] I. Chengalur-Smith, D.P. Ballou, H.L. Pazer, The impact of data quality information on decision making: an exploratory study, IEEE Transactions on Knowledge and Data Engineering 11 (6) (1999) 853–864.

[8] R.J. Coutheoux, Marketing data analysis and data quality management, Journal of Targeting, Measurement and Analysis for Marketing 11 (4) (2003) 299–313.

[9] J. Cowie, F. Burstein, Quality of data model for supporting mobile decision making Decision Support Systems 43 (4) (2007) 1675–1683.

[10] W. DeLone, E. Mclean, Information systems success: the quest for the dependent variable, Information Systems Research 3 (1) (1992) 60–95.

[11] D. Dey, Z. Zhang, P. De, Optimal synchronization policies for data warehouses INFORMS Journal on Computing 18 (2) (2004) 229–242.

[12] M.J. Eppler, M.A. Helfert, Classi<sup>fi</sup>cation and analysis of data quality costs, Proceedings of the 9th International Conference on Information Quality (ICIQ), (2004), Cambridge, MA, USA, 2004.

[13] A. Even, G. Shankaranarayanan, Utility-driven assessment of DQ, The DATA BASE for Advances in Information Systems 38 (2) (2007) 76–93.

[14] A. Even, G. Shankaranarayanan, P.D. Berger, Economics-driven data management: an application to the design of tabular datasets, IEEE Transactions on Knowledge and Data Engineering 19 (6) (2007) 818–831.

[15] J. Fisher, D. Berndt, Creating false memories: temporal reconstruction errors in data warehouses, Proceedings of the 2001 Workshop on Technologies and Systems (WITS), (2001), New Orleans, LA, USA, 2001.

[16] C.W. Fisher, I. Chengalur-Smith, D.P. Ballou, The impact of experience and time on the use of data quality information in decision making, Information Systems Research 14 (2) (2003) 170–188.

[17] B. Foss, I. Henderson, P. Johnson, Managing the quality and completeness of data, Journal of Database Marketing 10 (2) (2002) 139–158.

[18] T.F. Gattiker, D.L. Goodhue, Understanding the local-level costs and bene<sup>fi</sup>ts of ERP through organizational information processing theory, Information and Management 41 (4) (2004) 431–443.

[19] B. Heinrich, M. Kaiser, M. Klier, A procedure to develop metrics for currency and its application in CRM, ACM Journal of Data and Information Quality 1 (1) (2009) 5.

[20] S. Jain, P.K. Kannan, Pricing of information products on online servers: issues models, and analysis, Management Science 48 (9) (2002) 1123–1142.

[21] O.E.M. Khalil, T.D. Harcar, Relationship marketing and data quality management, S.A.M. Advanced Management Journal 64 (2) (1999) 26–33

[22] S.E. Madnick, Y.R. Wang, Y.W. Lee, H. Zhu, Overview and framework for data and information quality research, ACM Journal of Data and Information Quality 1 (1) (2009) 2.

[23] M.V. Mannino, W. Zhiping, A framework for data warehouse refresh policies, Decision Support Systems 42 (1) (2006) 121–143.

[24] R.C. Morey, Estimating and improving the quality of information in the MIS, Communications of the AC 25 (5) (1982) 337–342.

[25] L.L. Pipino, W.L. Yang, R.Y. Wang, Data quality assessment, Communications of the ACM 45 (4) (2002) 211–218.

[26] T.C. Redman, Data Quality for the Information Age, Artech House, Boston, MA 1996.

[27] M.L. Roberts, P.D. Berger, Direct Marketing Management, 2nd editionPrentice-Hall, Englewood Cliffs, NJ, 1999

[28] A. Segev, F. Fang, Optimal update policies for distributed materialized views, Management Science 37 (7) (1991) 851–870.

[29] G. Shankaranarayanan, Y. Cai, Supporting data quality management in decision making, Decision Support Systems 42 (1) (2006) 302–317.

[30] R.Y. Wang, A product perspective on total data quality management, Communications of the ACM 41 (2) (1998) 58–65.

[31] S. Watts, G. Shankaranarayanan, A. Even, Data quality assessment in context: a cognitive perspective, Decision Support Systems 48 (1) (2009) 202–211.

[32] L.A. West Jr., Private markets for public goods: pricing strategies of online database vendors, Journal of Management Information Systems 17 (1) (2000) 59–84.

Adir Even, from the Information Systems group at the Department of Industrial Engineering and Management Ben-Gurion University of the Negev (Israel), explores the contribution of data and systems to value-gain and pro<sup>fi</sup>tability from both theoretical and practical perspectives, and studies implications for system design, data warehousing, business intelligence, and data quality management. His research has been published in DSS, IEEE/TDKE, CACM, CAIS, and Database. He received a DBA degree from Boston University School of Management, and has substantial software-industry experience as a senior software-development manager.

G. Shankaranarayanan received the PhD degree in management information systems from The University of Arizona Eller School of Management (1998). His research interests include data modeling and design, database schema evolution, metadata modeling and management, data quality management, and the economics of data management. His research has appeared in journals such as the Journal of Database Management, Decision Support Systems, Communications of the ACM, Database for Advances in Information Systems, and IEEE/TKDE. He serves on the editorial board of the International Journal of Information Quality. He is a member of the IEEE and a member of the ACM.

Paul D. Berger is a Visiting Scholar and Professor of Marketing at Bentley University. He is also the director of Bentley's Master of Science in Marketing Analytics (MSMA) Program. He was formerly a Professor of Marketing and Quantitative Methods at the School of Management, Boston University. He earned his S.B., S.M., and Ph.D. degrees from the Massachusetts Institute of Technology Sloan School of Management. He has co-authored several books, including Experimental Design with Applications in Management, Engineering, and The Sciences (2002), and very recently, Internet Marketing: Reaching Customers Anytime, Anyplace, Any Platform (2010). He has authored over 120 refereed-journal articles, including in such journals as Management Science, American Statistician, Technometrics, and IEEE Transactions on Knowledge and Data Engineering.
