---
otero_id: 1860
otero_key: "GR2K4TE2"
title: "Using Dempster–Shafer theory and real options theory to assess competing strategies for implementing IT infrastructures: A case study"
authors: "Cokky Hilhorst; Piet Ribbers; Eric van Heck; Martin Smits"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using Dempster–Shafer theory and real options theory to assess competing strategies for implementing IT infrastructures: A case study

Cokky Hilhorst <sup>a,</sup>⁎, Piet Ribbers <sup>a</sup>, Eric van Heck <sup>b</sup>, Martin Smits <sup>a</sup>

<sup>a</sup> Tilburg University, P.O. Box 90153, 5000 LE Tilburg, The Netherlands

<sup>b</sup> RSM Erasmus University, P.O. Box 1738, 3000 DR Rotterdam, The Netherlands

## a r t i c l e i n f o

Article history: Received 23 August 2006 Received in revised form 29 June 2008 Accepted 6 July 2008 Available online 17 July 2008

Keywords: Multi-attribute decision analysis Risk Belief functions Real options theory IT infrastructure implementation strategy

## a b s t r a c t

This paper discusses the selection of a preferred strategy for implementing an IT infrastructure from a range of competing alternatives. The model presented here combines the use of an evidential reasoning approach based on the Dempster–Shafer theory of belief functions with real options analysis. We discuss the combined use of both theories and show that combining the Dempster–Shafer theory with real options analysi provides <sup>fl</sup>exible support that takes account of the multi-dimensional nature of implementation decisions. We also go into the fundamental requirements that need to be met when selecting a strategy for implementing an IT infrastructure. We conclude by outlining a number of the model's limitations.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

The consolidation of IT infrastructures in large organisations can result in development and implementation projects in which separate organisational units are required to work with the same system. This may result in complex technology development and implementation projects costing millions of euros. Since signi<sup>fi</sup>cant organisational change is required across all organisational units, and since such projects often involve the use of complex technology, they face serious risks that may result in unrealised bene<sup>fi</sup>ts, high costs or overruns. The preferred strategy for developing and implementing such projects therefore needs to reduce the degree of uncertainty and risk, and also create managerial <sup>fl</sup>exibility so as to maximise the project's bene<sup>fi</sup>ts.

Multi-attribute decision analysis is a <sup>fi</sup>eld of research in which various techniques have been developed to make ‘preference decisions (such as evaluation, prioritization, selection and so on) over the available alternatives that are characterised by multiple, usually con<sup>fl</sup>icting, criteria’ [4]. One of the more recent developments in multi-attribute decision analysis is the use of an evidential reasoning approach based on the Dempster–Shafer theory of belief functions [20,22,28]. The Dempster–Shafer theory models risk by using the notion of the plausibility of a negative outcome, and by capturing both precise data and various types of uncertainties [23].

Where the degree of uncertainty is high and the costs are irreversible, there is a consensus that real options theory can be applied to capture the <sup>fi</sup>nancial value of managerial <sup>fl</sup>exibility in IT infrastructure projects. By giving managers the ability to ‘wait and see’ in the event of uncertainty, real options analysis can help to identify the most favourable staging of investments, and can also create scope for additional learning about future payoffs before a <sup>fi</sup>nal decision is made [16].

In recent years, a growing volume of research has been performed into IT investments and real options [2,3,14,21] and IT investments and the use of multi-attribute decision analysis to account for uncertainties [9,17,18,23]. Nevertheless, to our knowledge, no attempt has been made to date, as far as we are aware, to synthesise the <sup>fi</sup>ndings of research on real options and multi-attribute decision analysis to support complex IT infrastructure investment decisions in conditions of uncertainty.

A vital issue in determining the practical value of both analytical methods is how to combine real options analysis with multi-attribute decision analysis, so as to incorporate different types of uncertainties and risks, as well as quantitative and qualitative information. Consequently, the goal of this paper is to develop formal support for de<sup>fi</sup>ning a favourable strategy for implementing an IT infrastructure that takes different types of uncertainty and risk into account. We combine real options theory and the Dempster–Shafer theory of belief functions to model risk. This allows us to analyse a fundamental problem in the implementation of IT infrastructure systems: what is the best strategy for balancing the risks and bene<sup>fi</sup>ts from both <sup>fi</sup>nancial and non-<sup>fi</sup>nancial perspectives?

We compare the combined use of real options theory and Dempster–Shafer theory with the use of:

(1) traditional Net Present Value (NPV) analysis,

(2) real options analysis,

(3) Dempster–Shafer theory and NPV analysis.

We discuss the theoretical assumptions underlying and the limitations of combining real options theory and an evidential reasoning approach based on the Dempster–Shafer theory. Using real data from a large European-based service-provider, we use this combined model to de<sup>fi</sup>ne a favourable multi-stage strategy for developing and implementing a human resource management application. We show that the combined use of these two approaches can generate important information for making a selection from competing strategies, and that this combined model takes full account of the multi-dimensional nature of IT investment decisions. We also offer a set of minimum decision-making criteria for IT infrastructure implementation projects that is consistent with prior work.

The proposed combined model covers a range of IT infrastructure projects in which a selection needs to be made from competing implementation scenarios in a setting where there is a project risk. The model provides <sup>fl</sup>exible decision support that can be adapted to the speci<sup>fi</sup>c domain in question.

The rest of the paper is organised as follows. In the next section, we take a closer look at decisions which can be modelled with the aid of an evidential reasoning approach based on the Dempster–Shafer theory of belief functions. We also introduce real options theory, present a combination of the two theories and discuss the underlying theoretical assumptions. We then describe the background to the problem and outline the decision attributes that are relevant in de<sup>fi</sup>ning an IT infrastructure implementation strategy. The application of the model in a case study is then presented, in which we use data from a large European-based service-provider to de<sup>fi</sup>ne a favourable strategy for implementing a human resource management system. Next we compare the decision-making models and discuss their limitations and we conclude with a summary of the study's main <sup>fi</sup>ndings and suggest a number of possible topics of further research.

## 2. Theoretical background

A project for developing and implementing an IT infrastructure stands more chance of being successful if it is structured to <sup>fi</sup>t the demands imposed by the risk inherent to the project [11]. Both <sup>fi</sup>nancial and non-<sup>fi</sup>nancial aspects play an important role in the investment process. In order to make a selection from competing implementation strategies in a situation where there is a project risk, both qualitative and quantitative decision attributes and different types of risk have to be taken into account.

One means of structuring decision-making is presented by an evidential reasoning approach based on the Dempster–Shafer theory of belief functions [28,29], which models both quantitative and qualitative information in a situation of risk. After discussing this approach, we then introduce the Net Present Value (NPV) method and the valuation of multi-stage options using real options theory. To calculate the option value of alternative strategies, we use the binomial options model proposed by Cox et al. [8]. This model has frequently been used in prior research to value multi-staged investment scenarios. However, researchers have not paid much attention to the way in which non-<sup>fi</sup>nancial aspects of the investment scenario affect the choice of a strategy for implementing an IT infrastructure. We show how we combined the use of real options analysis and the Dempster–Shafer theory and discuss their underlying theoretical assumptions.

2.1. The evidential reasoning approach based on the Dempster–Shafer theory of belief functions

The evidential reasoning approach based on the Dempster–Shafer theory of belief functions can be used to deal with multi-attribute decision-making problems of both a quantitative and qualitative nature, in conditions of risk. There is growing support for the use of the Dempster–Shafer theory of belief functions for analysing multiattribute decisions [23,29,30]. The approach has a number of important characteristics, which we discuss here.

In its traditional de<sup>fi</sup>nition, risk is measured as the probability of a negative outcome of an event or situation [23]. However, risk may also be conceptualised as an uncertain condition or event that has either a negative or a positive effect on the achievement of an objective [9]. The Dempster–Shafer theory of belief functions allows us to incorporate both these above notions of risk. Support for a hypothesis indicates the amount of belief that directly supports a given hypothesis, because there is no evidence that would contradict the hypothesis. Using belief functions we can withhold belief from a proposition without according that belief to the negation of the same proposition. This allows us to model the level of residual uncertainty or ambiguity that remains after the available evidence has been considered. Using belief functions allows us to model a lack of data, probabilities or vagueness in subjective judgments.

Using the Dempster–Shafer theory of belief functions, risk can be modelled by applying the notion of the plausibility (i.e. risk) of a negative outcome. To illustrate this, consider the situation where we have belief that the implementation time of a proposed IT implementation strategy (which may be subject to considerable uncertainty) could be 30% good and 20% not good, and 50% ignorance indicating we do not know whether the implementation time will be good or bad, based on what we know about the presence of threats and available countermeasures. In this case, ‘Good’ and ‘Not Good’ denote distinctive evaluation grades, and the percentage values of 30 and 20 are degrees of belief, indicating the extents to which the corresponding grades are assessed. This may be expressed as:

$$
S (\text { Implementation   time }) = \{(\text { Good }, 0. 3), (\text { Not   Good }, 0. 2) \}\tag{1}
$$

where S(Implementation time) is the implementation time of the implementation strategy and the <sup>fi</sup>gures 0.3 and 0.2 stand for the degrees of belief. In this case, the plausibility that the implementation time is not good is 70%, based on the available information. So, we have 70% risk that the implementation time is not good. As illustrated, belief in a statement represents the total belief that the statement is true. Belief of zero in a statement means lack of evidence in support of the statement, unlike representing impossibility in probability.

The evidential reasoning approach uses an extended decision matrix, in which each attribute of an alternative is described by a distributed assessment. It employs a belief function based on the Dempster–Shafer theory of belief functions to represent an assessment of an attribute as a distribution of a set of evaluation grades. Suppose there are K alternatives, $O _ { j } ( j = 1 , . . . , K ) ,$ , to choose from and M attributes, $A _ { i } ( i { = } 1 , . . . , M ) ,$ , to consider. Using a set $H { = } \{ H _ { i } \mid i { = } 1 , { \ldots } , N \}$ of evaluation grades, we can represent the assessment of an attribute $A _ { 1 }$ on an alternative $O _ { 1 } ,$ denoted by the expectation $S ( A _ { 1 } ( O _ { 1 } ) )$ , using the following belief structure:

$$
S \left(A _ {1} \left(O _ {1}\right)\right) = \left\{\left(H _ {1}, \beta_ {1, 1}\right), \left(H _ {2}, \beta_ {2, 1}\right), \dots , \left(H _ {N}, \beta_ {N, 1}\right) \right\}, \quad \text { where } 0 \leq \Sigma \beta_ {n, 1} \leq 1 \quad \text { for } \quad n = 1, \dots N\tag{2}
$$

where $\beta _ { n , 1 }$ denotes the degree of belief that attribute $A _ { 1 }$ is assessed to evaluation grade $H _ { n \cdot }$ The expectation $S ( A _ { 1 } ( O _ { 1 } ) )$ reads that attribute $A _ { 1 }$ at an alternative $O _ { 1 }$ is assessed to grade $H _ { n }$ to a degree of $\rho _ { n , 1 } ^ { \mathrm { ~ ~ } } \gamma$ ×100% $( n = 1 , . . . , N )$ . An assessment may be regarded as being complete if the sum of the degrees of belief for all n is 100%. In the evidential reasoning framework, a multi-attribute decision analysis problem with M attributes $A _ { i } \ ( i { = } 1 , . . . , M )$ , K alternatives $O _ { j } ( j = 1 , . . . , K )$ and N evaluation grades $H _ { n } \ ( n { = } 1 , . . . , \ N )$ for each attribute is represented using an extended decision matrix with $S ( A _ { i } ( O _ { j } ) )$ as its element in the ith row and jth column.

In a utility-based evidential reasoning approach to multiattribute decision analysis, an attribute can have its own set of evaluation grades that may differ from those of other attributes [28]. Rule-based or utility-based techniques can be used to devise a systematic procedure for transforming various types of information into a uni<sup>fi</sup>ed format, so that there is consistency between qualitative and quantitative information. It differs in this respect from traditional multi-attribute decision analysis approaches, most of which aggregate average scores. Instead of aggregating average scores, an evidential reasoning algorithm uses decision theory and the evidence combination rule of the Dempster–Shafer theory [20] to aggregate belief degrees. The logic behind the algorithm is that, if an object has a good (or bad) attribute, then that object must be good (or bad) to a certain extent. The extent is measured both by the relative weight, denoted by ω, that decision-makers assign to the attribute and by the degree to which the attribute belongs to the good (or bad) category. Appendix A provides details on the evidential reasoning algorithm.

The evidential reasoning approach is capable of accommodating numerical data and subjective judgments of various formats, as well as incomplete and imprecise information. In the presented analysis in Section 4, we use a window-based software tool called Intelligent Decision System (IDS) [28] to support the evidential reasoning approach based on the Dempster–Shafer theory of belief functions.

2.2. The valuation of multi-stage IT investments using the binomial options model

Researchers have used real options analysis as a capital budgeting approach that takes explicit account of the value of <sup>fl</sup>exibility in IT investment decisions [2,5,24–26]. It assumes that decision-makers can intervene if the projected level of cash <sup>fl</sup>ow is not realised due to resolved uncertainty, and that managers can actively maximise the upside potential of the investment or limit the downside loss. From an options perspective, risk is de<sup>fi</sup>ned as the upward and downward variation in expected outcomes.

Options analysis allows us to decide which implementation strategy results in the greatest managerial <sup>fl</sup>exibility, by calculating the optimum outcome for project risk and <sup>fi</sup>nancial return. The traditional NPV approach discounts the estimated cash <sup>fl</sup>ow of an investment to its present value, using a time value of money as the discount rate commensurate with the market expectations of the project risk. It assumes that initiation of a project entails a complete commitment to the cash <sup>fl</sup>ow speci<sup>fi</sup>ed. This assumption is not correct whenever the probability distribution of the returns is asymmetric, as is usually the case [16].

However, IT infrastructure development and implementation projects may involve a different range of options. This paper focuses on stage options. Stage options create value by providing an opportunity to alter or terminate a project before each new stage of funding, based on updated information about costs and bene<sup>fi</sup>ts, thus enabling project managers to learn or gather information during the investment process. As a stage is completed, the ambiguities about the net payoffs from subsequent stages may be resolved and value is created by only pursuing subsequent stages with positive payoffs.

In order to calculate the optional value of the different IT implementation alternatives, we use the binomial options model devised by Cox et al. [8]. This values the real options in discrete time using a binomial lattice and allows for the transparent and custom-tailored modelling of multi-stage investment decisions [5]. The binomial options model assumes that, starting at $t _ { 0 } = 0 ,$ the value of the risky underlying asset V may increase to uV or decrease to dV by time $t _ { 1 } = t _ { 0 } + \Delta t$ . In this case V is the value of an IT infrastructure investment. The probability that value V will rise is assumed to be q and the probability that value V will fall is $1 - q ,$ where $d < 1 , u > 1 .$ . The up and down movements in the lattice follow the equations

$$
u = \exp (\sigma \sqrt {t} / n) \quad d = \exp (- \sigma \sqrt {t} / n)\tag{3}
$$

where n is the number of steps in the binomial lattice and one time period Δt is de<sup>fi</sup>ned as the time to expiration of the option divided by the number of steps in the binomial lattice. In the option calculation, the volatility σ represents an estimate of the variance of project returns. It measures the risk associated with the project in terms of <sup>fl</sup>uctuations in the cash <sup>fl</sup>ow during the course of the project.

For an explanation of how to calculate a call option using a binomial lattice, see extensive descriptions of the model in prior literature [5,8]. We can use the binomial options model to optimise the balance between implementation risk and bene<sup>fi</sup>ts from a <sup>fi</sup>nancial perspective.

2.2.1. Real option analysis and the Dempster–Shafer theory of belief functions

In the context of the evidential reasoning approach, quantitative data can be transformed to a uni<sup>fi</sup>ed format using utilities which can be estimated explicitly using the decision-maker's preferences. In this way, a quantitative basic attribute can be transformed to an equivalent expectation so that the quantitative attribute can be aggregated in conjunction with other qualitative attributes. In order to incorporate the generated option value in the cost attribute of the evidential reasoning framework, we assume a linear marginal utility function. This assumption cannot be relaxed, as is explained below. The utility of the <sup>fi</sup>nancial attribute is normalised as follows. As the option value C is a cost and bene<sup>fi</sup>t attribute, the highest option value is preferred. Given a linear utility function, we assign $u ( C _ { \mathrm { m a x } } ) = 1$ and $u ( C _ { \mathrm { m i n } } ) { = } 0$ Then a value $C _ { j }$ on an attribute $A _ { i }$ may be represented using the following equivalent expectation:

$$
S _ {i} (C _ {j}) = \left(h _ {n, i}, \beta_ {n, j}\right), \quad \text { for } n = 1, \dots , N _ {i}\tag{4}
$$

where

$$
\beta_ {n, j} = \left(u \left(h _ {n + 1, i}\right) - u \left(h _ {j}\right)\right) / \left(u \left(h _ {n + 1, i}\right) - u \left(h _ {n, i}\right)\right) \quad \text { and } \quad \beta_ {n + 1, j} = 1 - \beta_ {n, j}\tag{5}
$$

if $u ( h _ { n , i } ) { \leq } u ( h _ { j } ) { \leq } u ( h _ { n + 1 , i } ) .$ . This transformation from a quantitative assessment to Eq. (4) is equivalent with regard to the underlying utility and rational in terms of preserving the features of the original assessment [28]. In particular, as is shown in [28] the completeness of an assessment is preserved in the transformation process. We can use this quantitative data transformation technique to incorporate the <sup>fi</sup>nancial valuation in the evidential reasoning framework.

2.3. Combining the use of real options with the Dempster–Shafer theory of belief functions

Combining real options with the Dempster–Shafer theory of belief functions appears attractive from a practical viewpoint, since it allows us to make a selection from competing implementation strategies in a situation where both qualitative and quantitative decision attributes and different types of risk have to be taken into account. However, both theories rest on certain assumptions that lead to a lack of theoretical elegance.

In the <sup>fi</sup>rst place, Goodwin and Wright [12] have already pointed out that converting NPV to utilities requires clear assumptions about the decision-maker's preferences. For example, the NPV assumes a constant rate of trade-off for sums of money between the same pair of years, irrespective of the amount of money which is transferred from next year to this [12]. From the viewpoint of the evidential reasoning approach, if this assumption is seriously violated, the NPV will not accurately represent the decision-maker's preference between sums of money arriving at different points in time.

In addition, real options analysis uses the volatility of a portfolio of securities that exactly replicates the project's payoffs as if they were traded on the market, assuming complete and perfect markets. The value of the project is indicated by the market value of this replicating portfolio. Furthermore, real options analysis assumes risk-neutral investors. Clearly, the decision-maker's probabilities and utility function for describing its preference for cash <sup>fl</sup>ow over time may well be different from this perspective. According to [22] however, the option pricing method is a simpler and more direct way of computing the project value and determining the best project management strategy than trying to de<sup>fi</sup>ne the decision-maker's probabilities and utility function for the project's NPV. Based on these theoretical assumptions of risk neutrality and perfect markets it is not meaningful from a real options perspective to use a non-linear utility function to impose the decision-maker's risk attitude into the cost-bene<sup>fi</sup>t attribute when translating the option value into an evidential reasoning framework.

Despite these objections to the combined use of theories, when estimates of future cash <sup>fl</sup>ows and volatility are carefully considered, an identi<sup>fi</sup>cation of the options and an understanding of the value of <sup>fl</sup>exibility can help managers to identify and abandon failing IT investments before they escalate out of control.

The main advantage of the combined model is that it effectively and comprehensibly combines both option analysis and the evidential reasoning approach into a practical means of accurately valuing projects. A thorough sensitivity analysis – both of the weights assigned to the criteria in the evidential reasoning approach and of the volatility in the real options analysis – generates information from a number of different perspectives. This gives us a practical advantage over the realistic alternatives of either not valuing or systematically undervaluing the different investment options associated with new products and projects [16].

## 3. Attributes for IT infrastructure strategies

In deciding on the most favourable implementation strategy, managers seek to learn about uncertainties to reduce risks and increase bene<sup>fi</sup>ts. For example, a system may need functional <sup>fl</sup>exibility to support differently organised business processes, or the organisation may need to respond to organisational changes during the course of implementation. The implementation strategy may also be a source of risk in itself; obviously, a big bang-type implementation across all organisational units is a riskier undertaking than a project staged in multiple phases. An important step in the evidential reasoning approach is de<sup>fi</sup>ning the relevant decision-making attribute hierarchy. The set of measurable attributes for modelling bene<sup>fi</sup>ts and risks is obtained from prior research on IT project risk and on the justi<sup>fi</sup>cation of IT investments.

In an attempt to deal with the continuing problem of information system failures, researchers have tried to systematically organise critical risk factors in IT projects [3,13] and have identi<sup>fi</sup>ed IT project implementation risk factors [1]. Borenstein and Betencourt [6] identify a minimum set of attributes for the justi<sup>fi</sup>cation of general IT investments with operational, tactical and strategic attributes on costs, business change and risks, based on previous research studies [7,12,19]. These attributes and risk factors lead to the formulation of three basic criteria:

(1) costs and benefits: the costs of implementation in relation to the monetary bene<sup>fi</sup>ts,

(2) project implementation risk: the reduction of exposure to organisational or system failure or to budget overshoots or time overruns,

(3) business change: the ability of the IT infrastructure to create opportunities for business transformation.

## Table 1

Attributes for de<sup>fi</sup>ning an IT infrastructure implementation strategy

<table><tr><td>Attribute label</td><td>Description</td></tr><tr><td>(e1) Costs and benefits</td><td>The costs of the implementation related to the monetary benefits</td></tr><tr><td>(e1a) Costs of the implementation</td><td>The costs of the system implementation</td></tr><tr><td>(e1b) Benefits of the implementation</td><td>The monetary benefits of the system implementation</td></tr><tr><td>(e2) Project implementation risk</td><td>Reduction of exposure to organisational or system failure, or to higher-than-expected costs or time</td></tr><tr><td>(e2a) Project size</td><td>The size of the project, measured in number of departments involved and the estimated project implementation time</td></tr><tr><td>(e2a1) Implementation time</td><td>Estimated project implementation time</td></tr><tr><td>(e2a2) Number of departments involved</td><td>Number of departments involved with implementing the system</td></tr><tr><td>(e2b) Experience with technology</td><td>The project team and organisations&#x27; familiarity with the systems technology</td></tr><tr><td>(e2b1) New hardware</td><td>The extent to which the hardware is new to the organisation</td></tr><tr><td>(e2b2) New software</td><td>The extent to which the software is new to the organisation</td></tr><tr><td>(e2b3) User IT knowledge</td><td>The extent to which the user is knowledgeable in the area of IT</td></tr><tr><td>(e2b4) Project team knowledge</td><td>The extent to which the project team is knowledgeable in the proposed application area</td></tr><tr><td>(e2c) Project structure</td><td>The nature of the task complexity the project faces, measured in changes that are needed to implement the system and the commitment to the system</td></tr><tr><td>(e2c1) Replaced functions</td><td>The percentage of existing functions that are replaced on a one-to-one basis</td></tr><tr><td>(e2c2) Procedural changes</td><td>The severity of user-department procedural changes caused by the proposed system</td></tr><tr><td>(e2c3) Structural changes</td><td>The degree of needed user-organisation structural change to meet requirements of the new system</td></tr><tr><td>(e2c4) User attitude</td><td>The general attitude of the user towards the IT solution</td></tr><tr><td>(e2c5) Management commitment</td><td>Commitment of upper-level user management to the system</td></tr><tr><td>(e3) Business change</td><td>The possibility of the IT implementation to provide opportunities for business transformation</td></tr><tr><td>(e3a) Improvement in consumer service</td><td>Changes associated with the IT which positively influence the relationship with clients</td></tr><tr><td>(e3b) IT aligned with business strategy</td><td>Level to which the IT supports the strategy of the business</td></tr><tr><td>(e3c) Improvement of organisational image</td><td>The extent to which the IT use will positively influence the image of the organisation from the clients point-of-view</td></tr><tr><td>(e3d) Improvement of strategic positioning</td><td>The impact of the IT to open up opportunities for new business changes</td></tr><tr><td>(e3e) Improved efficiency and control of internal processes</td><td>The impact of the IT to foster monitoring of internal processes</td></tr><tr><td>(e4) Learning effects</td><td>The possibility of the IT implementation strategy to support learning about the system implementation</td></tr><tr><td>(e4a) Functional flexibility</td><td>The extent to which learning is supported about the functional flexibility of the system to support differently organised business processes</td></tr><tr><td>(e4b) Technical scalability</td><td>The extent to which learning is supported about the technical scalability of the system to support different user groups</td></tr><tr><td>(e4c) Technical compatibility</td><td>The extent to which learning is supported about the technical compatibility of the system to be successfully implemented in the different departmental infrastructures</td></tr><tr><td>(e4d) Improved implementation processes</td><td>The quality of the implementation process by having less implementation problems</td></tr></table>

To these three main attributes we can add the learning effects attribute, which is the ability of the implementation strategy to support learning about the implementation of the system. With the exception of the cost and benefit attribute, all attributes address evidence for the competing implementation strategies that cannot be quanti<sup>fi</sup>ed <sup>fi</sup>nancially at the time of making a decision. In total, the attribute hierarchy consists of four <sup>fi</sup>rst-level attributes, fourteen second-level attributes and eleven third-level attributes. Table 1 summarises the attribute hierarchy, including a brief description of the attributes. The set of attributes to cover the minimum dimensions relevant to the selection of an implementation strategy may be expanded, depending on the characteristics of the speci<sup>fi</sup>c situation.

## 4. The case: implementation of a human resource management system

We used the combined model comprising the Dempster–Shafer theory and real options theory presented above to analyse a development and implementation investment decision of an IT infrastructure using data from a European-based service-provider. An organisation employing over 30,000 FTEs<sup>1</sup> developed a human resource management system (HRMS) to help the organisation match its staff complement to changing external and internal demands as effectively and ef<sup>fi</sup>ciently as possible. The organisation consisted of 18 autonomous departments, ranging in size from small to large. The HRMS needed to support strategic high-level planning to justify capital expenditure, tactical management of human resources to meet demand, and operational scheduling and individual time registration. The HRMS implementation was a large and complex project affecting all the organisation's employees to a lesser or greater degree. After the development of the HRMS, 18 separate application implementation projects were planned for the 18 different departments. The business objective was cost reduction; the bene<sup>fi</sup>ts were to consist of internal organisational bene<sup>fi</sup>ts derived from the deployment of the system.

## 4.1. The HRMS project risks

The HRMS implementation project was associated with a high degree of risk due to organisational, technological and functional uncertainties. The project was affected by several organisationspeci<sup>fi</sup>c and IT project implementation risks. These were due to endogenous factors and affect the organisation's ability to successfully implement the system. Monetary risks were caused by reasonable doubts as to whether the estimated <sup>fi</sup>nancial bene<sup>fi</sup>ts of the development and implementation of the HRMS were valid and realisable, given that the organisation had a long history of failed or delayed IT projects. There was uncertainty about the clarity of scope, since the autonomous departments differed in their organisational structures and in the way they had organised their business processes. The new IT application needed to contain the features required to support all the various departments. Risks concerning infrastructural stability and compliance, as well as adequate infrastructural support, arose from the fact that the departmental infrastructures used different technical platforms, different shared applications and different types of data. The application needed to be scalable to the larger departments and had to be compatible with departmental IT infrastructures. If the risks relating to the clarity of scope and infrastructural stability were not adequately addressed, the projected monetary bene<sup>fi</sup>ts and opportunities for business transformation might not be realised in all the departments. Project implementation risks, such as those relating to project size and project structure, arose from the absence of suf<sup>fi</sup>cient project capabilities such as supportive senior management and access to key resources to effectively deploy the system during and after implementation. Insuf<sup>fi</sup>cient project capabilities resulted from the large number of diverse departments that had to be supported during implementation. These project implementation risks could affect the success of implementation and hence the organisation's ability to achieve business change in all departments, eventually leading to a lack of monetary bene<sup>fi</sup>ts.

4.2. Application of the evidential reasoning approach based on the Dempster–Shafer theory

The case study analysis was carried out from February to October 2005. The analyses included in-depth interviews with various people working on the project, namely the IT project manager, line managers, interviews with employees from the 18 departments (both large and small) and interviews with project team members. We used open questions to roughly guide the interviews. The data provided by these interviews plus archival data based on internal documents and other written material was used to de<sup>fi</sup>ne and analyse the research problem. The data needed for the cost-bene<sup>fi</sup>t analysis was based on a system development and implementation estimation supplied by external consultants working on the project and was also obtained from internal project documents.

The process of de<sup>fi</sup>ning a preferred implementation strategy using the evidential reasoning approach based on the Dempster–Shafer theory consisted of <sup>fi</sup>ve stages:

(1) specifying the decision-making goal and the alternatives taken into consideration

(2) specifying the decision-making attributes (as presented in Section 3)

(3) assessing the attributes, including the cost-bene<sup>fi</sup>t analysis of the alternatives, and assigning weights to the attributes

(4) aggregating the individual assessments into an overall assessment (5) performing a sensitivity analysis of the weights assigned.

Having identi<sup>fi</sup>ed the speci<sup>fi</sup>c risks affecting the project, we will now present our <sup>fi</sup>ndings relating to the individual stages.

4.3. Outline of the alternative implementation strategies for the HRMS project

The <sup>fi</sup>rst stage involved specifying the decision-making goal and the alternatives. The goal of the decision is to de<sup>fi</sup>ne the best possible strategy for implementing an IT infrastructure that balances the risks and bene<sup>fi</sup>ts from both a <sup>fi</sup>nancial and a non-<sup>fi</sup>nancial viewpoint.

In order to de<sup>fi</sup>ne the alternative implementation strategies, we needed to make certain assumptions. First, the development of the HRMS would last 1 year. This assumption was based on the project planning documents for the software development phase. Second, each implementation stage would take 1 year. Moreover, due to the scarcity of resources, each implementation stage had to be completed before a new one could start. Third, the maximum duration of the entire HRMS implementation project was 3 years. If this deadline was not observed, the departments might diverge too widely in their organisational directions. We therefore decided that there should be a maximum of three one-year implementation stages. Although the costs and bene<sup>fi</sup>ts of the HRMS could vary from one department to another, we assumed that the implementation had <sup>fi</sup>xed costs and bene<sup>fi</sup>ts in all departments.

Another important assumption was that the department implementation projects did not have correlated risk pro<sup>fi</sup>les in the real options analysis. The risks associated with the development and implementation of one IT project may impact other projects as well.

This may result in a signi<sup>fi</sup>cant level of positive correlation of the organisational, technological and functional risks associated with implementation of projects with similar capabilities and dependent on similar skills. As a consequence, the valuation of a portfolio incorporating risk may be different from the sum of the valuations of individual projects if the <sup>fi</sup>rm is risk averse [2]. Although system implementation risks could change during the course of implementation as a result of learning (for example, whether the system supports different ways of working or whether it is technically scalable), we assumed that uncertainty about the organisational bene<sup>fi</sup>ts depended on departmental efforts and therefore are not correlated. Additionally, we did not have data on the correlation between risks in this case. Instead, we added the learning effects attribute, which is the ability of the implementation strategy to support learning about the implementation of the system. The assumption on the correlation of risk pro<sup>fi</sup>les in the real options analysis could be loosened if data is available. Depending on the source of the correlated risk, this may in<sup>fl</sup>uence the relevance of the added learning effects attribute, which can easily be adjusted.

In the light of these assumptions, we de<sup>fi</sup>ned four alternative development and implementation strategies. These were as follows:

(1) a one-stage implementation, where, after a development stage at t = 0, the organisation implements the HRMS in all 18 departments at once (i.e. in the form of a ‘big bang’) at t = 1;

(2) a two-stage, nine–nine implementation, where, after the development stage, the implementation is divided into two stages with nine departments in each stage;

(3) a two-stage, six–twelve implementation, where the implementation is divided into two stages at t = 1, with six departments in the <sup>fi</sup>rst stage and twelve departments in the second stage;

(4) a three-stage implementation, where implementation is divided into three stages after development, with six departments in each stage (see Fig. 1).

Thus far, we have de<sup>fi</sup>ned the decision-making goal, distinguished the alternatives and speci<sup>fi</sup>ed the decision-making attributes (see Section 3). The next section assesses and represents the evidence strength, including a cost-bene<sup>fi</sup>t analysis of the alternatives.

## 4.4. Assessment of the different implementation strategies

To assess the attributes, we started by performing a cost-bene<sup>fi</sup>t analysis of the alternatives. We evaluated the cost-bene<sup>fi</sup>t attribute for the four development and implementation strategies. First, we calculated the NPVs of the implementation scenarios without <sup>fl</sup>exibility (Section 4.4.1). We then determined the best implementation strategy using the real options theory (Section 4.4.2). The next step was to assess the non-<sup>fi</sup>nancial attributes and assign weights to the attributes (Section 4.4.3). We incorporated the results of the traditional NPV and real options theory into a multi-attribute decision analysis framework for evaluating the implementation strategies. After aggregating the individual assessments into an overall assessment for the four strategies, we performed a sensitivity analysis on the assigned weights. We then compared the combined use of Dempster– Shafer theory and real options theory with the use of:

(1) NPV analysis,

(2) real options theory,

(3) Dempster–Shafer theory and NPV analysis.

## 4.4.1. Implementation without flexibility: the NPV analysis

We conducted a standard NPV analysis, based on the cash <sup>fl</sup>ows estimation during development and implementation. We calculated the NPVs of all four strategies, i.e. one-stage, the two-stage nine–nine, two-stage six–twelve and three-stage implementation. These values were all different, since implementing the project in stages defers both costs and savings.

The project costs consist of personnel and non-personnel expenses, i.e. the costs pertaining to the project development environment (such as housing, workstations, hardware and application packages). The training costs comprise the investments made in training staff who were to work with the system. Management and maintenance costs consist of ongoing investments in IT infrastructure and maintenance. Since the organisation is a government body, we estimated a relatively low cost of capital (k=10%), involving a risk premium of 6% above the risk-free rate (r=4%).

As we have already mentioned, the project was designed to reduce costs. This means that the bene<sup>fi</sup>ts consist of internal organisational bene<sup>fi</sup>ts derived from using the system. There are two sources of <sup>fi</sup>nancial bene<sup>fi</sup>ts: lower labour costs and productivity gains. Labour costs can be lowered as the new HRMS supports the pro-active management of variable personnel expenses, leading to a reduction in overtime, picket costs, special duty costs, etc. We assumed that the reduction in labour costs consisted of an average of seven FTEs worth €40,000 a year in each department, resulting in an average reduction of approximately 0.2%/annum in the cost of labour. The total bene<sup>fi</sup>ts of the lower labour costs, once all departments are operational, would be €5 million/annum.

![](/api/attachments/GR2K4TE2/fulltext/images/697e495e528cfaab915d41c352ac5b7ebd054f495f363724ae24fa9d6173b1f9.jpg)  
Fig. 1. The different development and implementation scenarios: from ‘Big Bang’ to staged implementation.

The new HRMS would also improve staff productivity, as fewer planning mistakes would be made. The assumption here was that computerised support of capacity planning would lead to a productivity gain of one and a half percent per annum. The total bene<sup>fi</sup>ts of productivity improvement once all departments were operational would be €3.5 million/annum. In both cases, we incorporated a learning effect for the estimated project bene<sup>fi</sup>ts, assuming that 25% of the total estimated bene<sup>fi</sup>ts would be realised in each department in the <sup>fi</sup>rst deployment year, 50% in the second year, 75% in the third year and 100% as from the fourth year.

Table 2 shows the NPV analysis for the one-stage implementation project over the next 8 years (i.e. until 2013), which is the expected lifespan of the HRMS. Including the development stage and a one-step implementation in all departments, the project results in a positive NPV of €1,183,678. We then performed the same calculation for the other implementation strategies, leading to an NPV of €929,329 for the two-stage nine–nine implementation, €844,546 for the two-stage six–twelve implementation and €690,395 for the three-stage implementation. In the case of the different two-stage and three-stage implementations, whilst implementing the system in a large number of departments earlier augments the NPV because of the earlier payback of larger bene<sup>fi</sup>ts, the NPV is nonetheless not higher than in the case of a one-stage implementation strategy. Table 2a shows the NPV analysis for the two-stage nine–nine implementation as an example.

Traditional investment valuation methods would therefore suggest that the project is an attractive investment and that the system should preferably be implemented in a single stage. Of course, this analysis does not include risk and does not take accurate account of the embedded option value of a staged implementation.

4.4.2. The real options analysis: using the binomial real options model

We also performed a real options analysis using the binomial real options model including a sensitivity analysis. In order to calculate the values of the different implementation scenarios, we needed to know, for each call option in the lattice, the expected present value of the incremental cash <sup>fl</sup>ows, $V _ { t }$ and the investment $I _ { t }$ made to acquire the option, where t is the expiration time of the option. We also needed to know the volatility σ at each step.

Summary of cash-<sup>fl</sup>ows (cost and bene<sup>fi</sup>ts) for the development of the one-stage implementation of the HRMS (×1000 €)

<table><tr><td colspan="10">Development and one-step implementation</td></tr><tr><td>Year</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td></tr><tr><td>Costs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Internal staff</td><td>800</td><td>2184</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>External staff</td><td>3512</td><td>3427</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Exploitation and maintenance</td><td></td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td></tr><tr><td>Training</td><td></td><td>721</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non-personnel</td><td>100</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td></tr><tr><td>Subtotal</td><td>4412</td><td>9398</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td></tr><tr><td>Benefits</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reduction of labour costs</td><td></td><td></td><td>875</td><td>1750</td><td>2625</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td></tr><tr><td>Productivity improvement</td><td></td><td></td><td>1250</td><td>2500</td><td>3750</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td></tr><tr><td>Subtotal</td><td>0</td><td>0</td><td>2125</td><td>4250</td><td>6375</td><td>8500</td><td>8500</td><td>8500</td><td>8500</td></tr><tr><td>Net cash flow</td><td>4412</td><td>9398</td><td>940</td><td>1185</td><td>3310</td><td>5435</td><td>5435</td><td>5435</td><td>5435</td></tr></table>

Summary of cash-<sup>fl</sup>ows (cost and bene<sup>fi</sup>ts) for the development of the two-stage nine– nine implementation of the HRMS (×1000 €)

<table><tr><td colspan="11">Development and two-stage nine-nine implementation</td></tr><tr><td>Year</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td></tr><tr><td>Costs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Internal staff</td><td>800</td><td>1092</td><td>1092</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>External staff</td><td>3512</td><td>1714</td><td>1714</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Exploitationand maintenance</td><td></td><td>1510</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>3020</td><td>1510</td></tr><tr><td>Training</td><td></td><td>361</td><td>361</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non-personnel</td><td>100</td><td>23</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td><td>45</td><td>23</td></tr><tr><td>Subtotal</td><td>4412</td><td>4699</td><td>6232</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td><td>3065</td><td>1533</td></tr><tr><td>Benefits</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reduction oflabour costs</td><td></td><td></td><td>438</td><td>1313</td><td>2188</td><td>3063</td><td>3500</td><td>3500</td><td>3500</td><td>1750</td></tr><tr><td>Productivityimprovement</td><td></td><td></td><td>625</td><td>1875</td><td>3125</td><td>4375</td><td>5000</td><td>5000</td><td>5000</td><td>2500</td></tr><tr><td>Subtotal</td><td>0</td><td>0</td><td>1063</td><td>3188</td><td>5313</td><td>7438</td><td>8500</td><td>8500</td><td>8500</td><td>4250</td></tr><tr><td>Net cash flow</td><td>4412</td><td>4699</td><td>5169</td><td>122</td><td>2247</td><td>4372</td><td>5435</td><td>5435</td><td>5435</td><td>2717</td></tr></table>

In the option calculation, the volatility σ represents an estimate of the variance of project returns. A representation of the project volatility is the standard deviation of the rate of change in project returns over one time period [10,25]. It measures the risk associated with the project in terms of <sup>fl</sup>uctuations in the project's cash <sup>fl</sup>ow during the course of the project. Although a good estimate of volatility σ may be based on historical data [10], in our case the IT infrastructure was implemented in 18 autonomous, decentral departments, where no historical data were available. Instead, as in [2,25], different cash <sup>fl</sup>ow scenarios for the investment (i.e. worst-case, base-case and bestcase scenarios) were produced for the various project stages and the variance was computed using the percentile estimate for the normal distribution. As we have previously explained, the base-case scenario is based on an average labour reduction of seven FTEs per department per annum and a productivity gain of one and a half percent per annum. In the worst-case scenario, the reduction in labour costs is worth <sup>fi</sup>ve FTEs per department per annum, whereas the best-case reduction is nine FTEs per department per annum. In the worstcase scenario, the productivity gain is half that achieved in the basecase scenario, whereas the best-case gain is double that in the basecase scenario. We then calculated the standard deviation of the rate of change in project returns in the worst-case, base-case and best-case scenario over one time period, representing the volatility values for the different implementations stages. We subsequently calculated option values for each project implementation strategy as summarised in Table 3.

Volatility values for the different implementation stages (in %) and option values for the different implementation strategies (×€1000)

<table><tr><td>Implementation strategy</td><td>Volatility per stage</td><td>Option value per implementation strategy</td></tr><tr><td>One-stage implementation</td><td></td><td>4,411,823</td></tr><tr><td>Stage one (18 departments)</td><td>18.41</td><td></td></tr><tr><td>Two-stage nine-nine implementation</td><td></td><td>2,566,928</td></tr><tr><td>Stage one (nine departments)</td><td>6.66</td><td></td></tr><tr><td>Stage two (twelve departments)</td><td>6.05</td><td></td></tr><tr><td>Two-stage six-twelve implementation</td><td></td><td>2,487,099</td></tr><tr><td>Stage one (six departments)</td><td>4.44</td><td></td></tr><tr><td>Stage two (twelve departments)</td><td>8.07</td><td></td></tr><tr><td>Three-stage implementation</td><td></td><td>2,298,951</td></tr><tr><td>Stage one (six departments)</td><td>4.44</td><td></td></tr><tr><td>Stage two (six departments)</td><td>4.03</td><td></td></tr><tr><td>Stage three (six departments)</td><td>3.67</td><td></td></tr></table>

Table 4  
Table 5  
Option values at varying volatility values for the different implementation strategies of the HRMS (×1000 €)

<table><tr><td colspan="6">Option values of the different implementation strategies</td></tr><tr><td>Volatility</td><td>One-stage</td><td>Two-stage nine-nine</td><td>Two-stage six-twelve</td><td>Three-stage</td><td>Preferred strategy</td></tr><tr><td> $\sigma_0$ : 0.1</td><td>3043</td><td>2704</td><td>2591</td><td>2386</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.2</td><td>4833</td><td>4412</td><td>4272</td><td>4018</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.3</td><td>8676</td><td>8081</td><td>7882</td><td>7522</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.4</td><td>14,653</td><td>13,786</td><td>13,498</td><td>12,792</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.5</td><td>22,925</td><td>21,683</td><td>21,268</td><td>20,515</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.6</td><td>33,736</td><td>32,002</td><td>31,424</td><td>30,373</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.7</td><td>46,897</td><td>44,828</td><td>43,963</td><td>42,709</td><td>One-stage</td></tr><tr><td> $\sigma_0$ : 0.8</td><td>62,664</td><td>60,499</td><td>59,188</td><td>57,876</td><td>Two-stage nine-nine</td></tr><tr><td> $\sigma_0$ : 0.9</td><td>81,949</td><td>79,712</td><td>77,840</td><td>76,485</td><td>One-stage nine-nine</td></tr></table>

4.4.2.1. Sensitivity analysis. We conducted a sensitivity analysis for a wide range of volatility values to measure its impact on the selection of the most suitable strategy. We let σ range from σ=0.10 to σ=0.90 and used a constant volatility for each implementation stage. The option values for the different implementations at different volatility values are summarised in Table 4. The value of σ does not in<sup>fl</sup>uence the <sup>fi</sup>nal decision on the most favourable implementation strategy.

Relaxing the assumption that the volatility σ remains constant, we then lowered the volatility value at each new project implementation stage by 50%. As expected, this only strengthened the preference for a one-stage implementation. In this case, at all different volatility values (σ=0.10 to σ=0.90), a one-stage implementation is the preferred implementation strategy.

We also conducted a sensitivity analysis after augmenting the value of the organisational bene<sup>fi</sup>ts while keeping the volatility constant across all stages. Raising the organisational bene<sup>fi</sup>ts does not affect the choice of the most favourable form of project staging. Lowering the organisational bene<sup>fi</sup>ts for all departments by 25% results in a negative NPV and a positive option value for all scenarios only if σ is higher than 0.50. In these conditions, the three-stage implementation is preferable to the two-stage nine–nine, the twostage six–twelve and the one-stage implementation in this order. Thus from an options perspective, if it is likely that the organisational bene<sup>fi</sup>ts will turn out to be lower, and if there is a high degree of uncertainty as to whether these bene<sup>fi</sup>ts can be realised, a different implementation scenario then becomes more favourable.

4.4.3. Combining the use of real options analysis and Dempster–Shafer theory

We have already discussed the optimum implementation strategy from a <sup>fi</sup>nancial viewpoint using the NPV method and, when including risk and the value of embedded managerial <sup>fl</sup>exibility, using option analysis. The most favourable implementation strategy from a <sup>fi</sup>nancial viewpoint is the one-stage implementation strategy using the NPV method. The same strategy was also found to be best when we included risk and the value of embedded managerial <sup>fl</sup>exibility using option analysis

Using the framework presented above, we combine options analysis and the rule-based evidential reasoning approach. The attributes for assessing the various implementation scenarios have already been presented in Section 3. There are four thematic topics, consisting of both qualitative and quantitative attributes.

This stage involves the users assessing the strength of evidence for each attribute. This indicates the level of support for each attribute. In the evidential reasoning process, the decision-makers have to assign weights ω to the various attributes. In our case, we assessed attributes and assigned weights to the attributes using information on the project obtained both from documentation and from interviews. We veri<sup>fi</sup>ed the assessment of attributes and weights with the HRMS project manager, in terms of their plausibility with regard to the proposed implementation strategies, leading to the <sup>fi</sup>nal attribute assessment and weights set out in Table 5.

To this end, we used a window-based software tool called Intelligent Decision System (IDS) [28] to apply the evidential reasoning approach based on the Dempster–Shafer theory of belief functions.

The assessment for the different implementation strategies of the HRMS

<table><tr><td>Attribute</td><td>Weight</td><td>One-stage</td><td>Two-stage nine-nine</td><td>Two-stage six-twelve</td><td>Three-stage</td></tr><tr><td>(e1) Costs and benefits</td><td>0.15</td><td>{(E, 1.0)}</td><td>{(I, 1.0)}</td><td>{(I, 0.3), (B, 0.7)}</td><td>{(B, 1.0)}</td></tr><tr><td>(e2) Project implementation risk</td><td>0.35</td><td></td><td></td><td></td><td></td></tr><tr><td>(e2a) Project size</td><td>0.4</td><td></td><td></td><td></td><td></td></tr><tr><td>(e2a1) Implementation time</td><td>0.4</td><td>{(G, 0.5), (E, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(I, 0.7), (A, 0.3)}</td></tr><tr><td>(e2a2) Number of departments</td><td>0.6</td><td>{(B, 1.0)}</td><td>{(I, 0.4), (A, 0.6)}</td><td>{(I, 0.6), (A, 0.4)}</td><td>{(G, 0.5), (E, 0.5)}</td></tr><tr><td>(e2b) Experience with technology</td><td>0.3</td><td></td><td></td><td></td><td></td></tr><tr><td>(e2b1) New hardware</td><td>0.2</td><td>{(I, 0.5), (A, 0.5)}</td><td>{(A,1.0)}</td><td>{(A, 1.0)}</td><td>{(A, 0.5), (G, 0.5)}</td></tr><tr><td>(e2b2) New software</td><td>0.2</td><td>{(B, 1.0)}</td><td>{(A, 0.6), (G, 0.4)}</td><td>{(A, 0.4), (G, 0.6)}</td><td>{(G, 0.4), (E, 0.6)}</td></tr><tr><td>(e2b3) User IT knowledge</td><td>0.2</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td></tr><tr><td>(e2b4) Project team knowledge</td><td>0.4</td><td>{(B, 1.0)}</td><td>{(A, 0.6), (G, 0.4)}</td><td>{(A, 0.4), (G, 0.6)}</td><td>{(G, 0.4), (E, 0.6)}</td></tr><tr><td>(e2c) Project structure</td><td>0.3</td><td></td><td></td><td></td><td></td></tr><tr><td>(e2c1) Replaced functions</td><td>0.1</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td></tr><tr><td>(e2c2) Procedural changes</td><td>0.2</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td></tr><tr><td>(e2c3) Structural changes</td><td>0.2</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td><td>{(A, 0.5), (G, 0.5)}</td></tr><tr><td>(e2c4) User attitude</td><td>0.25</td><td>{(B, 0.8), (G, 0.2)}</td><td>{(B, 0.6), (G, 0.4)}</td><td>{(B, 0.4), (G, 0.6)}</td><td>{(B, 0.3), (G, 0.7)}</td></tr><tr><td>(e2c5) Management commitment</td><td>0.25</td><td>{(B, 0.8), (G, 0.2)}</td><td>{(B, 0.6), (A, 0.2), (G, 0.2)}</td><td>{(B, 0.4), (A, 0.4), (G, 0.2)}</td><td>{(B, 0.4), (A, 0.2), (G, 0.4)}</td></tr><tr><td>(e3) Business change</td><td>0.35</td><td></td><td></td><td></td><td></td></tr><tr><td>(e3a) Improvement in consumer service</td><td>0.2</td><td>{(A, 0.6), (G, 0.4)}</td><td>{(A, 0.8), (G, 0.2)}</td><td>{(A, 0.8), (G, 0.2)}</td><td>{(A, 1.0)}</td></tr><tr><td>(e3b) IT aligned with business strategy</td><td>0.1</td><td>{(G, 0.8), (E, 0.2)}</td><td>{(G, 0.6), (A, 0.4)}</td><td>{(A, 0.6), (G, 0.4)}</td><td>{(A, 1.0)}</td></tr><tr><td>(e3c) Improvement of organisational image</td><td>0.2</td><td>{(E, 1.0)}</td><td>{(G, 0.5), (E, 0.5)}</td><td>{(G, 0.4), (E, 0.6)}</td><td>{(G, 0.5), (A, 0.5)}</td></tr><tr><td>(e3d) Improvement of strategic positioning</td><td>0.2</td><td>{(E, 1.0)}</td><td>{(G, 0.6), (A, 0.4)}</td><td>{(A, 0.6), (G, 0.4)}</td><td>{(A, 1.0)}</td></tr><tr><td>(e3e) Improved efficiency and control of internal processes</td><td>0.3</td><td>{(E, 1.0)}</td><td>{(G, 0.6), (A, 0.4)}</td><td>{(A, 0.6), (G, 0.4)}</td><td>{(A, 1.0)}</td></tr><tr><td>(e4) Learning effects</td><td>0.15</td><td></td><td></td><td></td><td></td></tr><tr><td>(e4a) Functional flexibility</td><td>0.25</td><td>{(B, 1.0)}</td><td>{(B, 0.6), (A, 0.4)}</td><td>{(A, 1.0)}</td><td>{(E, 0.2), (G, 0.8)}</td></tr><tr><td>(e4b) Technical scalability</td><td>0.25</td><td>{(B, 1.0)}</td><td>{(B, 0.6), (A, 0.4)}</td><td>{(A, 1.0)}</td><td>{(E, 0.2), (G,0.8)}</td></tr><tr><td>(e4c) Technical compatibility</td><td>0.25</td><td>{(B, 1.0)}</td><td>{(B, 0.6), (A, 0.4)}</td><td>{(A, 1.0)}</td><td>{(E, 0.2), (G, 0.8)}</td></tr><tr><td>(e4d) Improved implementation processes</td><td>0.25</td><td>{(B, 1.0)}</td><td>{(B, 0.6), (A, 0.4)}</td><td>{(A, 1.0)}</td><td>{(E, 0.2), (G,0.8)}</td></tr></table>

Table 6  
Quanti<sup>fi</sup>ed assessment of implementation scenarios

<table><tr><td>Implementation strategy</td><td>Assessment</td><td>Ranking</td></tr><tr><td>One-stage implementation</td><td>0.514</td><td>2</td></tr><tr><td>Two-stage nine-nine implementation</td><td>0.491</td><td>4</td></tr><tr><td>Two-stage six-twelve implementation</td><td>0.521</td><td>1</td></tr><tr><td>Three-stage implementation</td><td>0.511</td><td>3</td></tr></table>

We de<sup>fi</sup>ned a set H of evaluation grades for assessing all the attributes of each alternative implementation strategy:

$$
H = \left\{h _ {j}, j = 1, \dots , 5 \right\} = \{\text { Excellent } (E), \text { Good } (G), \text { Average } (A), \text { Indifferent } (I), \text { Bad } (B) \}.\tag{6}
$$

All attributes, apart from quantitative ones, can be assessed using these evaluation grades. We only considered complete assessments. If certain qualitative assessment values do not refer to this set, we can use the rule-based information transformation technique to assess all attributes with reference to this set. Because of the limited amount of space available to us, we will not demonstrate this technique here and refer the reader instead to a detailed description of this technique in [28].

We then incorporated the option values into a multi-attribute decision analysis framework. To estimate the utilities of the cost attribute we assume a linear marginal utility function. For the option valuation, we normalised the option value for each alternative (see Table 3) by assigning the highest option value (one-stage implementation) u(3,411,470)=1 and the lowest option value (three-stage implementation) u(2,298,951) = 0. As we assume a linear utility function, u(3,133,340)=0.75, u(2,855,211)=0.5 and $u ( 2 , 5 7 7 , 0 8 1 ) =$ 0.25. Let

$$
h _ {1, 1} = 3, 4 1 1, 4 7 0, \quad h _ {2, 1} = 3, 1 3 3, 3 4 0, \quad h _ {3, 1} = 2, 8 5 5, 2 1 1,
$$

$$
h _ {4, 1} = 2, 5 7 7, 0 8 1, \quad h _ {5, 1} = 2, 2 9 8, 9 5 1.
$$

The option value of the two-stage six–twelve alternative can be represented using Eq. (4). The option value of the two-stage six– twelve alternative, $h _ { 1 } = 2 , 4 8 7 , 0 9 9$ . Since $h _ { 5 , 1 } < h _ { 1 } < h _ { 4 , 1 }$ , we can represent the option value as $S _ { 3 } ( 2 , 4 8 7 , 0 9 9 ) = \{ ( h _ { 4 , 1 } , \beta _ { 4 , 1 } ) , ( h _ { 5 , 1 } , \beta _ { 5 , 1 } ) \}$ where

![](/api/attachments/GR2K4TE2/fulltext/images/be8bd81102663c1d259966c1ce27dc3446d85cb5280f91476bfcb56fa722de65.jpg)  
Fig. 2. Summary of the combined approach of real options analysis and Dempster–Shafer theory.

$$
\begin{array}{l} \beta_ {4, 1} = (h _ {5, 1} - h _ {1}) / (h _ {5, 1} - h _ {4, 1}) \\ \qquad = (2, 2 9 8, 9 5 1 - 2, 4 8 7, 0 9 9) / (2, 2 9 8, 9 5 1 - 2, 5 7 7, 0 8 1) \\ \qquad = 0, 7 \quad \text { and } \\ \beta_ {5, 1} = 1 - \beta_ {4, 1} = 0. 3. \end{array}
$$

So, $S _ { 3 } ( 2 , 4 8 7 , 0 9 9 ) = \{ ( h _ { 4 , 1 } , ~ 0 . 7 ) , ~ ( h _ { 5 , 1 } , ~ 0 . 3 ) \} = \{ ( I , ~ 0 . 3 ) , ~ ( B , ~ 0 . 7 ) \}$ . In a similar way we calculate the two-stage nine–nine alternative $S _ { 2 }$ $( 2 , 5 6 6 , 9 2 8 ) = \{ ( h _ { 4 , 1 } , 1 . 0 ) \} = \{ ( I , 1 . 0 ) \}$ .

Using a similar calculation, we calculated the utilities assuming a linear utility function. We normalised the NPVs for each alternative by assigning the highest NPV (one-stage implementation) u(1,183,678)= 1 and the lowest NPV (three-stage implementation) u(690,395)=0. The NPVs may be represented as:

$$
\begin{array}{l} S _ {1} (1, 1 8 3, 6 7 8) = \{(E, 1. 0) \}, \\ S _ {2} (9 2 9, 3 2 9) = \{(E, 0. 2), (G, 0. 8) \}, \\ S _ {3} (8 4 4, 5 4 6) = \{(G, 0. 1), (A, 0. 9) \}, \quad \text { and } \\ S _ {4} (6 9 0, 3 9 5) = \{(B, 1. 0) \}. \end{array}
$$

Using the IDS software tool mentioned above, which is based on the evidential reasoning algorithm referred to in [28], we were able to calculate the overall degrees of belief. We aggregated all the attributes, leading to a <sup>fi</sup>nal assessment of the proposed implementation strategies.

Combining real options analysis with the Dempster–Shafer theory of belief functions results in a preference for the two-stage six–twelve implementation (see Table $6 ) .$ This is what one would intuitively expect, since more attributes are used that support phase-wide implementation. The one-stage implementation is ranked second, followed by the three-stage implementation and the two-stage nine–nine implementation. Fig. 2 represents a stepwise summary of our overall approach.

4.4.3.1. Sensitivity analysis. As the <sup>fi</sup>nal stage of the assessment process, we performed a sensitivity analysis to see how the preferred alternative changes if weights are assigned differently. If the weight for cost and bene<sup>fi</sup>ts changes from 0.15 to 0.24, the two-stage nine– nine implementation becomes the preferred implementation strategy. If the weight for the ‘costs and bene<sup>fi</sup>ts’ attribute is changed to 0.53, the preferred strategy changes to one-stage implementation. These outcomes support what one would intuitively expect, since the costbene<sup>fi</sup>t attribute supports earlier implementation of the system in a large number of departments because of the earlier payback of bene<sup>fi</sup>ts. If we use the NPV calculation in the multi-attribute decision analysis model, we get the same outcome, but the aggregated value for each alternative varies.

## 5. Discussion and conclusion

In this paper, we have de<sup>fi</sup>ned a theoretical model for selecting the most favourable strategy for implementing an IT infrastructure in conditions of uncertainty. The aim of this paper is to help decisionmakers to opt for the best implementation strategy by combining the Dempster–Shafer theory with real options analysis. We draw on Dempster–Shafer belief functions to evaluate decision-making attributes that cannot be easily quanti<sup>fi</sup>ed. This combined model takes full account of the multi-dimensional nature of the decision that needs to be taken. We applied the model in a case study, in which we used data from a large European-based service-provider to de<sup>fi</sup>ne a favourable strategy for implementing a human resource management system.

Decisions on IT investments are complex decisions based on multiple goals and values. It may well be because of this complexity that organisations often fail in practice to follow a well-structured, accountable and reproducible decision-making process for assessing the pro<sup>fi</sup>tability of IT investments. We have shown that our model for analysing investments in IT infrastructures, which takes account of the multi-dimensional nature of such investments, generates vital information for selecting the most appropriate strategy. Whilst previous research studies have valued multi-stage investments using real options analysis, they have ignored the multi-dimensional nature of IT infrastructure investment decisions. Although options analysis generates valuable insights into the trade-off between risk and bene<sup>fi</sup>ts from a <sup>fi</sup>nancial perspective, as we have shown in this article, adding non-<sup>fi</sup>nancial attributes that support phase-wide implementation can lead to very different outcomes in terms of the most suitable implementation strategy. Combining the Dempster– Shafer theory with real options analysis supports both qualitative and quantitative decision attributes, as well as different types of risk for both quantitative and qualitative attributes. This is shown in Table 7.

The case study shows that a combined analysis can generate valuable information that can help decision-makers to select the most suitable strategy from a range of competing strategies. This is because, as both the multi-attribute decision analysis and the real options calculation make it easy to perform a sensitivity analysis of the stated preferences, the various scenarios can be evaluated for different parameter ranges. The advantage of using the options model lies in identifying the trade-offs between risk and bene<sup>fi</sup>ts from a <sup>fi</sup>nancial viewpoint. Since the combined analysis also facilitates transparent group decision-making, it can help to overcome one of the main objections to the use of real options analysis, namely its lack of transparency for decision-makers. However, the dif<sup>fi</sup>culty of obtaining an accurate estimate of the volatility of the investment bene<sup>fi</sup>ts remains to be a source of criticism when using options valuation [28].

Our approach covers a wide range of competing strategies for IT infrastructure projects where there is a project risk. These include, for example, the implementation of group-wide computer platforms, application platforms (e.g. ERP) and data warehouses. The analysis provides <sup>fl</sup>exible decision support that can be adapted to the speci<sup>fi</sup>c domain in question.

As we have seen, a multiple attribute approach results in a different decision than when a NPV or real options analysis is used. There may be two reasons for this: <sup>fi</sup>rstly, the decision-maker's objectives may diverge from those of capital market players. Alternatively, the NPV or real options valuation may not have been correctly calculated. To elaborate on the <sup>fi</sup>rst reason, the normative decision models assume that a <sup>fi</sup>rm pursues the sole objective of stockholder wealth maximisation. However, IT infrastructure projects undertaken by large organisations are complex and involve interactions among a wide variety of stakeholders. The latter may have their own interpretations of wealth maximisation, subject to individual concerns about risk, liquidity, responsibility and so forth. For example, as is shown in the sensitivity analysis in the real options calculation, raising the degree of uncertainty leads to a higher real options value and therefore to a higher preference for the one-stage implementation strategy. However, the decision-maker in question may well have a preference for a lower project risk, resulting in a different implementation strategy. As regards the risks in relation to non-<sup>fi</sup>nancial aspects such as learning, these are dif<sup>fi</sup>cult to quantify in practice. This is easy to model by combining the Dempster–Shafer theory with real options analysis. Consequently, certain criteria that are not quanti<sup>fi</sup>ed in an NPV or real options analysis may be made explicit in a multiple attribute approach, thus resulting in a different decision.

Comparison of the different methods

<table><tr><td colspan="5">Comparison of methods</td></tr><tr><td></td><td>NPV</td><td>Real options analysis</td><td>Evidential Reasoning based on Dempster-Shafer and NPV</td><td>Evidential Reasoning based on Dempster-Shafer and real options</td></tr><tr><td colspan="5">Evaluation criteria</td></tr><tr><td>Financial</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Non-financial</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Risks</td><td>Risk-free rate of return</td><td>Variability of the projects&#x27; financial value and risk-free rate of return</td><td>Uncertainty in subjective judgments and risk-free rate of return</td><td>Uncertainty in subjective judgments and variability of the projects&#x27; financial value and risk-free rate of return</td></tr><tr><td colspan="5">Process support</td></tr><tr><td>Participatory planning</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">Impact of method</td></tr><tr><td>Learning</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Flexibility</td><td>Does not take flexibility into account</td><td>Takes managerial flexibility from a financial perspective into account</td><td>Takes multiple definitions of flexibility into account</td><td>Takes managerial flexibility from a financial perspective into account and multiple definitions of flexibility</td></tr></table>

The second possible reason for a different decision is if the NPV or real options valuation is not correct. This may be the case if cash <sup>fl</sup>ows cannot be accurately projected at the time when the decision is taken. For example, in our case, the results of the application of the improvement of strategic positioning attribute cannot be incorporated into the cash <sup>fl</sup>ow calculation for the project since it is not yet possible to place a monetary value on the attribute.

As for the limitations of our combined model, <sup>fi</sup>rstly real options and decision analysis rest on assumptions that lead to a lack of theoretical elegance when used in combination. Converting NPV to utilities requires clear assumptions about the decision-maker's preferences as described earlier. Also, the decision-maker's probabilities and utility function for describing its preference for cash <sup>fl</sup>ow over time may well be different from assumptions underlying real options theory. Violation of the theoretical assumptions underlying real options theory has been extensively discussed in literature, see for example [5], and these arguments on the validity of using real options analysis for IT infrastructure investment decisions can be extended to the combined model as presented in this paper.

Secondly, in the case we presented we assumed no project interdependencies between the 18 different HRMS implementations. Project interdependencies between two projects exist when a capability developed for one project is required by one or more other project(s) or when a capability developed for one project supports capabilities required by other projects [2]. Recently, a real options approach has been developed to prioritize a portfolio of IT projects that have interdependencies [2]. There are also examples of modelling project interdependencies using programming techniques in a multi-attribute decision analysis as in [15]. The speci<sup>fi</sup>c goal of our approach was to de<sup>fi</sup>ne an implementation strategy for an isolated application in autonomous departments which can be modelled as a stage option. Of course, also in this case project interdependencies may exist. For example, bene<sup>fi</sup>t interdependencies can occur due to a synergy effect when the HRMS is implemented in all departments.

A vital issue for further research is how to combine real options analysis with multi-attribute decision analysis to model these project interdependencies. In the presented combined model, project interdependencies from a <sup>fi</sup>nancial perspective can be made transparent by using the real options approach that deals with project interdependencies mentioned above [2]. Non-<sup>fi</sup>nancial project interdependencies can be made transparent by introducing attributes to the model that represent the interdependencies. For example, a speci<sup>fi</sup>c attribute for resource interdependencies may be added to account for the extent to which software resources can be shared among the various implementation projects.

When dealing with project interdependencies to prioritize a portfolio of IT projects, uncertainty about the bene<sup>fi</sup>ts or a lack of information on other characteristics of future projects may exist. This makes the combined use of real options and the Dempster–Shafer theory of belief functions a strong candidate for the support of these investment decisions.

The model can be further re<sup>fi</sup>ned with the aid of validation techniques such as user assessments to further extend the attribute hierarchy. It can also be extended to deal with project interdependencies as discussed above. Furthermore, for the purpose of our option analysis, we assumed that uncertainties surrounding different projects in different departments are not related. This may of course not be the case in real life. A future study should take into account the correlation of risk between projects. Also, we used the model to identify a multi-stage implementation strategy for an IT application the aim of which is to cut costs. It would also be interesting to analyse an IT infrastructure investment in which growth options form part of the investment proposal, given that there will be a greater disparity between the different implementation scenarios.

## Appendix A. The evidential reasoning algorithm

The evidential reasoning algorithm uses the concepts in set theory and probability theory for aggregating multiple attributes [28,29]. Suppose there is a simple two level evaluation hierarchy with a general attribute $A _ { i }$ at the upper level and a set of L basic attributes at the lower level. The assessments represented in Eq. (2) for an alternative $O _ { i }$ can be aggregated using the following evidential reasoning algorithm.

Suppose ω is the relative weight of the attribute A and ω and is normalised, so that $0 { \leq } \omega _ { i } { \leq } 1$ and ${ \scriptstyle \sum \omega _ { i } = 1 } { \mathrm { ~ f o r ~ } } n = 1 , . . . , L .$ . Without loss of generality, we present the evidential reasoning algorithm for combining two attribute assessments given by the assessment $S ( A _ { 1 }$ $( O _ { 1 } ) )$ as presented in $\operatorname { E q . } \left( 1 \right)$ and the assessment $S ( A _ { 2 } ( O _ { 1 } ) )$ , which is given by

$$
S (A _ {2} (O _ {1})) = \left\{\left(H _ {1}, \beta_ {1, 2}\right), \left(H _ {2},, \beta_ {2, 2}\right),..., \left(H _ {N}, \beta_ {N, 2}\right) \right\}, \quad \text { where } \quad 0 \leq \Sigma \beta_ {n, 1} \leq 1 \quad \text { for } \quad n = 1,..., N.
$$

We need to aggregate the two assessments $S ( A _ { 1 } ( O _ { 1 } ) )$ and $S ( A _ { 2 } ( O _ { 1 } ) )$ to generate a combined assessment. Suppose $S ( A _ { 1 } ( O _ { 1 } ) )$ and $S ( A _ { 2 } ( O _ { 1 } ) )$ are both complete. Let

$$
\begin{array}{l l l l l} m _ {n, 1} = \omega_ {1} \beta_ {n, 1} & \text {and} & m _ {H, 1} = 1 - \omega_ {1} \Sigma \beta_ {n, 1} = 1 - \omega_ {1} & \text {for} & n = 1, \ldots , N \\ m _ {n, 2} = \omega_ {2} \beta_ {n, 2} & \text {and} & m _ {H, 2} = 1 - \omega_ {2} \Sigma \beta_ {n, 2} = 1 - \omega_ {2} & \text {for} & n = 1, \ldots , N \end{array}
$$

where $m _ { n , 1 }$ and $m _ { n , 2 }$ are referred to as basic probability mass and each $m _ { H , i } ( \mathrm { f o r } j = 1 , 2 )$ is the remaining belief for attribute j unassigned to any of the $H _ { n }$ (where $\scriptstyle n = 1 , \ldots , N )$ . The evidential reasoning algorithm is used to aggregate the basic probability masses to generate combined probability masses, denoted by $m _ { n }$ (where $\scriptstyle n = 1 , \ldots , N )$ and $m _ { H }$ using the following equations:

$$
\begin{array}{l} \{H _ {n} \}: m _ {n}   =   k \big (m _ {n, 1} m _ {n, 2}   +   m _ {H, 1} m _ {n, 2}   +   m _ {n, 1} m _ {H, 2} \big) \quad \text { for } \quad n   =   1, \ldots , N \\ \{H \}: m _ {H}   =   k \big (m _ {H, 1} m _ {H, 2} \big) \end{array}
$$

where

$$
k = \left[ 1 - \Sigma \Sigma m _ {n, 1} m _ {p, 2} \right] ^ {- 1} \quad \text { for } \quad n = 1, \dots , N \quad \text { and } \quad p = 1, \dots , N \quad \text { and } \quad n \neq p.
$$

Now the combined probability masses can be aggregated with another assessment in the same way until all assessments are aggregated.

If there are only two assessments, the combined degrees of belief $\beta _ { n , 1 }$ for $n { = } 1 , { \ldots } , N$ are generated by:

$$
\beta_ {n} = m _ {n} / 1 - m _ {H} \quad \text { for } \quad n = 1, \dots , N.
$$

The combined assessment for the alternative $O _ { 1 }$ can then be represented as follows:

$$
S \left(O _ {1}\right) = \left\{\left(H _ {1}, \beta_ {1}\right), \left(H _ {2},, \beta_ {2}\right), \dots , \left(H _ {N}, \beta_ {N}\right) \right\} \quad \text { where } \quad 0 \leq \Sigma \beta_ {n} \leq 1 \quad \text { for } \quad n = 1, \dots , N.
$$

Since the Dempster's rule of combination proved to be commutative and associative [20], evidence can be combined in any order. In case of multiple belief structures, the combination of evidence can be carried out in a pairwise way [27].

## References

[1] L.M. Applegate, F. Warren McFarlan, J.L. McKenney, Corporate Information Systems Management, Irwin/McGraw-Hill, New York, 2005.

[2] I. Bardhan, S. Bagchi, R. Sougstad, Prioritizing a portfolio of information technology investment projects, Journal of Management Information Systems 21 (2) (2004)

[3] H. Barki, S. Rivard, J. Talbot, An integrative contingency model of software project risk management, Journal of Management Information Systems 17 (4) (2001).

[4] V. Belton, T.J. Stewart, Multiple Criteria Decision Analysis: An Integrated Approach, Kluwer Academic Publishers, 2001.

[5] M. Benaroch, R.J. Kauffman, A case for using real options pricing analysis to evaluate information technology project investments, Information Systems Research 10 (1) (1999).

[6] D. Borenstein, P.R.B. Betencourt, A multi-criteria model for the justi<sup>fi</sup>cation of IT investments INFOR, Information Systems and Operational Research 43 (1) (2005).

[7] E.K. Clemons, Strategic and competitive information systems, Journal of Management Information Systems 8 (2) (1991)

[8] J. Cox, S. Ross, M. Rubinstein, Option pricing: a simpli<sup>fi</sup>ed approach, Journal of Financial Economics 7 (3) (1991)

[9] Cutter Consortium, Exactly what is risk management? Cutter Consortium Press Release, Arlington, MA. (June 2002).

[10] B.L. Dos Santos, Justifying investments in new information technologies, Journal of Management Information Systems 7 (4) (1991).

[11] J.R. Galbraith, Organizational design: an information processing view, Interfaces 4 (3) (1974).

[12] P. Goodwin, G. Wright, Decision Analysis for Management Judgment, John Wiley and Sons, Ltd, 2005.

[13] M. Keil, P.E. Cule, K. Lyytinen, R.C. Schmidt, A framework for identifying software project risk, Communications of the ACM 41 (11) (1998).

[14] Y.J. Kim, G. Lawrence Sanders, Strategic actions in information technology investment based on real option theory, Decision Support Systems 33 (1) (2002).

[15] J.W. Lee, S.H. Kim, An integrated approach for interdependent information system project selection, International Journal of Project Management 19 (2001).

[16] J.E. Neely, R. de Neufville, Hybrid real option valuation of risky product developmen projects, International Journal of Technology, Policy and Management 1 (1) (2001).

[17] D. Petkov, O. Petkova, T. Andrew, T. Nepal, Mixing multiple criteria decision making with soft systems thinking techniques for decision support in complex situations, Decision Support Systems 43 (4) (2007).

[18] K.B. Salling, S. Leleur, A. Vestergaard Jensen, Modelling decision support and uncertainty for large transport infrastructure projects: the CLG-DSS model of the Øresund <sup>fi</sup>xed link, Decision Support Systems 43 (4) (2007).

[19] A.H. Segars, V. Grover, Strategic information systems planning success: an investigation of the construct and its measurement, Management Information Systems Quarterly 22 (2) (1998).

[20] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press, 1976.

[21] C. Singh, R. Shelor, J. Jiang, G. Klein, Rental software valuation in IT investment decisions, Decision Support Systems 38 (1) (2004).

[22] J.E. Smith, R.F. Nau, Valuing risky projects: option pricing theory and decision analysis, Management Science 41 (5) (1995).

[23] L. Sun, P.R. Srivastava, T.J., An information systems security risk assessment model under the Dempster–Shafer theory of belief functions, Journal of Management Information Systems 22 (4) (2006).

[24] A. Taudes, Software growth options, Journal of Management Information Systems 15 (1) (1998).

[25] A. Taudes, M. Feurstein, A. Mild, Options analysis of software platform decisions: a case study, MIS Ouarterly 24 (2) (2000)

[26] L. Trigeorgis, Making use of real options simple: an overview and applications in flexible-modular decision making, The Engineering Economist 50 (1) (2005).

[27] Y.M. Wang, J.B. Yang, D.L. Xu, Environmental impact assessment using the evidential reasoning approach, European Journal of Operational Research 174 (3) (2006).

[28] J.B. Yang, Rule and utility based evidential reasoning approach for multi-attribute decision analysis under uncertainties, European Journal of Operational Research 131 (1) (2001).

[29] J.B. Yang, M.G. Singh, An evidential reasoning approach for multiple attribute decision making with uncertainty, IEEE, Transactions on Systems, Man and Cybernetics 24 (1) (1994).

[30] E. Wilkins, S.H. Lavington, Belief functions and the possible words paradigm, Journal of Logic and Computation 12 (3) (2002).

## F U R T H E R R E A D I N G

[1] K. Roberts, M. Weitzman, Funding criteria for research, development and exploration projects, Econometrica 49 (5) (1981).

![](/api/attachments/GR2K4TE2/fulltext/images/c505f9be90455947cb43998b02a6b3b14591078fe120844662b7716271594c46.jpg)

Cokky Hilhorst is a doctoral student at the Department of Information Management at Tilburg University. Her research project aims to understand how managers can evaluate <sup>fl</sup>exibility in IT investment decision-making when factoring risks. She is a senior manager IT Effectiveness at PricewaterhouseCoopers Advisory N.V. in The Netherlands. She holds BSc and MSc degrees in arti<sup>fi</sup>cial intelligence from Utrecht University, was a research student at Cambridge University, England, and holds a masters degree in information management from the TIAS Business School.

![](/api/attachments/GR2K4TE2/fulltext/images/e4273313b32d1254d61951e790699c12e7c01056ed7f7336220d92826fa15c06.jpg)

Pieter Ribbers is Professor of Information Systems and Chair of the Department of Information Management at the University of Tilburg. He is the Director of the TIAS Business School's master's programme in information management. From 1991 to 1995, he was Af<sup>fi</sup>liate Professor of Information Management at Washington University in St. Louis, USA. As a researcher, teacher and consultant, his main areas of interest are the management challenges posed by IT, e-commerce and the strategic and organisational impact of IT. He has coauthored a number of books.

![](/api/attachments/GR2K4TE2/fulltext/images/e1c71a56ef3a5ba133222fe6e54a53d6a8fc41de885b924f51fafeb62b0282f6.jpg)

Eric van Heck is Professor of Information Management and Markets at RSM Erasmus University, where he combines research into and teaching on the strategic and operational uses of information technology, He is best known for his work on how companies can use on-line auctions to create value. He has co-authored a number of books and articles that have been published in journals including the California Management Review, Communications of the ACM, Decision Support Systems and Information Systems Research. He obtained both his MSc and his PhD degrees at Wageningen University.

![](/api/attachments/GR2K4TE2/fulltext/images/cf72d153c25b5e663ea2ca39be01e3e5371e98b36abe41283cdf073b64ef62af.jpg)

Martin Smits is Associate Professor of Information Systems and Management at the School of Economics and Business Administration at Tilburg University. His research focuses on strategic information systems planning, healthcare information systems, group decision support systems, inter-organisational systems, network organisations and knowledge management. He teaches at various universities on topics including information management, accounting and control, the strategic management of educational institutions, and healthcare management.
