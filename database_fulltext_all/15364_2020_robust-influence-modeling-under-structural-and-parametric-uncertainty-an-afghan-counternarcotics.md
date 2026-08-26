---
otero_id: 15364
otero_key: "JKTP33YR"
title: "Robust influence modeling under structural and parametric uncertainty: An Afghan counternarcotics use case"
authors: "William N. Caballero; Brian J. Lunday"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113161"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Robust Influence Modeling under Structural and Parametric Uncertainty: An Afghan Counternarcotics Use Case

Decision Support Systems

William N. Caballero, Brian J. Lunday

![](/api/attachments/JKTP33YR/fulltext/images/bbe4f84c37e98c9f9f0d09521a5f7be96b24f46d21345bf3c900fd09357cc71c.jpg)

PII: S0167-9236(19)30190-3

DOI: https://doi.org/10.1016/j.dss.2019.113161

Reference: DECSUP 13161

To appear in: Decision Support Systems

Received date: 19 March 2019

Revised date: 27 July 2019

Accepted date: 9 September 2019

Please cite this article as: W.N. Caballero and B.J. Lunday, Robust Influence Modeling under Structural and Parametric Uncertainty: An Afghan Counternarcotics Use Case, Decision Support Systems (2019), https://doi.org/10.1016/j.dss.2019.113161

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# Robust Influence Modeling under Structural and Parametric Uncertainty: An Afghan Counternarcotics Use Case

William N. Caballero<sup>a,∗</sup>, Brian J. Lunday<sup>a</sup>

<sup>a</sup>Department of Operational Sciences, Air Force Institute of Technology, 2950 Hobson Way, WPAFB, OH 45433, USA

## Abstract

An entity often seeks to influence the decisions of others in a system. This dynamic is apparent in a variety of settings including criminal justice, environmental regulation, and marketing applications. However, the central task of the influencing entity is confounded by uncertainty regarding their understanding of the structure and/or parameters of the decisions being made. The research herein sets forth a decision support methodology to identify robust influence strategies under such uncertain conditions. Furthermore, the utility of this framework and its proper parameterization are illustrated via an application to the contemporary, global problem of the Afghan opium trade. Utilizing open source data, we demonstrate how counternarcotic policy can be informed using a quantitative analysis that embraces both the bounded rationality of the economy’s decisionmakers and the government’s uncertainty regarding the degree of their deviation from perfect rationality. In this manner, we provide a new framework with which robust influence decisions can be identified under realistic information conditions, and we discuss how it can be used to inform real-world policy.

Keywords: Robust Decision Making, Persuasion, Behavioral OR, Prospect Theory, Behavioral Economics, Bounded Rationality

## 1. Introduction

Persuading an individual to adopt a given decision among a set of alternatives is an inherently dificult task. It requires a level of empathy to understand their full decision framework that may be dificult to achieve. In designing an influence strategy, a persuader must infer the answer to many questions: What other alternative prospects does the decisionmaker perceive? How does the decisionmaker evaluate this set of prospects? How does the decisionmaker value each respective outcome? How does the decisionmaker understand the uncertainty giving rise to these outcomes? In what way will an influence action afect the decisionmaker and their perceptions?

The answers to such questions can be inferred via human-subject testing [e.g. 1, 2]. However, the data collection requirements to do so with high confidence are substantial, and the resulting statistical insights are likely only relevant to a specific context. If automated data collection eforts are suitable or if the underlying decision setting is predictable, such dificulties are less problematic; whereas the data collection requirements do not lessen, their assembly is facilitated. As the body of knowledge for applying statistical or machine learning techniques grows to answer the aforementioned questions, existent literature [i.e., 3] describes how an optimal influence strategy can be determined.

Unfortunately, there exist many situations for which automated data collection eforts are infeasible, or wherein the underlying decisionmaking setting is less predictable. If either of these conditions hold, then direct application of the models described by Caballero and Lunday [3] is not possible; the parameter values required to formulate their persuasion programs are unknown. However, if bounded intervals for each of these unknown parameters can be identified, alternative methods can be developed to generate robust influence actions that meet some threshold of performance regardless of the parameters’ true values. This research sets forth such a methodology by leveraging the models of Caballero and

Lunday [3] within the Robust Decision Making (RDM) framework set forth by Lempert et al. [4], after which it demonstrates the methodology for a realistic use case.

The use case focuses on an application to a contemporary economic and national security problem: reducing supply for the Afghan opium trade. This objective is part of an enduring counternarcotics efort in Afghanistan. The Afghan illicit opium economy has long been suspected to be a primary revenue stream for the Taliban insurgency [5], but development of a successful strategy against it has proven elusive [6]. To aid policy development, multiple economists have quantitatively modeled the efects of counternarcotic actions [e.g., 7, 8]; however, such models generally rely on equilibrium analysis that implicitly suggests perfect rationality of all agents in the illicit economy. This research takes an alternative approach by considering the efect of counternarcotic strategies in a decision analytic instead of a game theoretic framework. By doing so, we demonstrate how a better understanding of a counternarcotic strategy’s efect can be gained by embracing the bounded rationality of the illicit economy’s decisionmakers and by acknowledging the associated uncertainty regarding their degree of departure from perfect rationality (i.e., through the usage of a descriptive theory of choice instead of the normative expected utility theory). In this manner, we illustrate how the joint treatment of behavioral economic concepts (e.g., bounded rationality) and robustness, two growing areas of study in the decision support systems community [e.g., 9, 10], can be leveraged jointly to facilitate influence policy decisions in uncertain environments.

The remainder of this manuscript is structured as follows. Section 2 reviews the influence modeling paradigm, discusses the RDM framework, and introduces how the concepts can be leveraged jointly to inform influence actions under parametric and/or structural uncertainty. Section 3 illustrates the utility of our methodology via its application to the reduction of Afghan poppy cultivation in the Badakhshan province. Finally, Section 4 provides closing comments and discusses the implications of this research.

## 2. Robust Decision Making and Influence Modeling

The persuasion programs set forth by Caballero and Lunday [3] pertain to the optimal manipulation of decision trees. In a two-stage process, a persuader starts by taking an action that influences how a decisionmaker (or set of decisionmakers) perceives the underlying risk or uncertainty, values the payof associated with each outcome, and/or evaluates the available set of prospects. After this persuader action has been taken, the decisionmaker(s) selects a preferred prospect.

Influence actions achieving such efects can take many forms. For instance, an appeal to the representativeness heuristic could alter subjective probabilities [11], alternative frames could afect payof valuations [12], or emotional appeals could afect a decisionmaker’s risk attitude [13]. Other examples, in addition to a survey on the literature supporting such efects, are discussed in greater detail by Caballero and Lunday [3].

Whereas the nature of the influence actions are assumed to be instancespecific, Caballero and Lunday [3] describe their efects within the Cumulative Prospect Theory (CPT) framework [14]. CPT is an empirically-validated, descriptive theory of choice wherein an individual’s decision is described by utility valuations from a reference point; concave and convex utility for gains and losses, respectively; loss aversion; and systematic weighting of probabilistic information. Whereas other descriptive theories of choice exist [e.g., 15], Pachur et al. [16] illustrated how many of these can be subsumed into the CPT framework. For this reason and, to maintain consistency with Caballero and Lunday [3], CPT is also utilized herein.

Consider a prospect f having n gain outcomes and m loss outcomes, respectively indexed as 1 to n and -m to −1. Each outcome value $x _ { k }$ measured from the reference point is evaluated relatively via CPT as

$$
V (f) = V ^ {+} (f) + V ^ {-} (f), \text { where }\tag{1a}
$$

$$
V ^ {+} (f) = \sum_ {k = 1} ^ {n} \pi_ {k} ^ {+} v (x _ {k}),\tag{1b}
$$

$$
V ^ {-} (f) = \sum_ {k = - m} ^ {0} \pi_ {k} ^ {-} v (x _ {k}),\tag{1c}
$$

$$
\pi_ {n} ^ {+} = W ^ {+} (A _ {n}),\tag{1d}
$$

$$
\pi_ {- m} ^ {-} = W ^ {+} (A _ {- m}),\tag{1e}
$$

$$
\pi_ {k} ^ {+} = W ^ {+} (A _ {k} \cup \dots \cup A _ {n}) - W ^ {+} (A _ {k + 1} \cup \dots \cup A _ {n}), \quad 0 \leq k \leq n - 1\tag{1f}
$$

$$
\pi_ {k} ^ {-} = W ^ {+} (A _ {- m} \cup \ldots \cup A _ {k}) - W ^ {+} (A _ {- m}, \cup \ldots \cup A _ {k - 1}), \quad 1 - m \leq k \leq 0,\tag{1g}
$$

wherein $v ( \cdot )$ is a piecewise utility function concave for gains and convex for losses; $W ^ { + }$ and $W ^ { - }$ are the event (outcome) weighting functions for gains and losses, respectively; and $\pi ^ { + }$ and $\pi$ <sup>−</sup> are the decision weights utilized to determine the respective component gains and losses, $V ^ { + } ( f )$ and ${ V } ^ { - } ( f )$

The goal of a persuasion program is to maximize the number of decisionmakers selecting some preferred course of action by altering (1) the $x _ { k } \mathrm { - v a l u e s }$ , (2) the uncertainty associated with event $A _ { k } ,$ and $/ \mathrm { o r }$ (3) the specific forms of the $W ^ { \pm } ( \cdot )$ or $v ( \cdot )$ functions. Accurately formulating a persuasion program requires a firm understanding of the structure of the decision tree, the baseline parameters, and how the persuader’s action will alter the decisionmaker and their perceptions. Human subject testing [e.g. 17] is one potential method to gain this understanding but, for a variety of reasons, it is not always practical and may not be feasible. Without these baseline parameters, a persuasion program cannot be utilized directly.

However, if uncertainty sets (or collections) can be identified for each unknown factor, a robust influence strategy can be identified. Whereas the application of robust optimization is the intuitive approach to do so, herein we illustrate how the RDM framework set forth by Lempert et al. [4] is preferable because of its

flexibility.

## 2.1. Robust Decision Making

RDM is an iterative decision analytic framework utilized in conditions of deep uncertainty. Deep uncertainty describes situations for which analysts cannot agree upon how to model the interaction of system variables, the underlying uncertainty, or the desirability of outcomes. RDM addresses these conditions by leveraging modern computer simulation, space-filling designs, and clustering algorithms.

To conduct an RDM analysis, it is necessary to identify the sets of available ${ \vec { S } } ,$ ${ \vec { F } } .$ The objective of RDM is to select some $s \in { \vec { S } }$ that performs well across any future state of the world in $\vec { F }$ . Lempert et al. [4] propose the following five step iterative process to apply RDM: identify initial candidate robust strategies, identify vulnerabilities, suggest hedges against vulnerabilities, characterize deep uncertainties and tradeofs among strategies, and consider improved hedging options and surprises.

In practice, these steps consist of building a database $\vec { E } = \vec { S } \times \vec { F }$ (i.e., the futures ensemble) with some robustness metric assigned to each strategy-future combination. A candidate strategy $s _ { c a n d }$ is then selected, and a subset of future states in $\vec { F }$ for which $s _ { c a n d }$ performs poorly is identified via clustering analysis. The next step is to determine alternative strategies less vulnerable to these future states but comparable to $s _ { c a n d }$ elsewhere, and select a new candidate strategy. This process is iteratively repeated until an acceptable course of action has been identified. After each round, there exists the potential to augment $\vec { E }$ with more strategies or future states of the world as required.

Therefore, RDM requires $\vec { F }$ to be a finite set. To account for this characteristic while accommodating situations wherein the set of plausible futures is excessively large (or infinite), a finitely-valued but adequately representative set $\vec { F }$ can be generated via a space-filling design of the region.

The conceptual steps in an RDM analysis are static. However, the spacefilling design utilized to sample the true set of futures is contingent upon the underlying uncertainties. If all uncertainty sets are connected, then standard space-filling designs (e.g., a Latin hypercube) can be utilized; otherwise, less traditional designs capable of incorporating categorical variables (e.g., fast flexible designs) may be required. In either situation, multiple design candidates exist. Analysts must be cognizant that this design selection, in addition to the particular clustering analysis utilized to identify vulnerabilities, may afect the final proposed strategy. A detailed examination of alternative designs for conducting RDM is outside the scope of this study, but we propose it to be of merit for future research.

The efect obtained by utilizing some s ∈ S<sup>\~</sup> given a potential future state is determined by a scenario generator (i.e., a computer simulation). The use of a scenario generator, in combination with the set ${ \vec { F } } _ { : }$ allows for the modeling of various system variable interactions and their efect on system performance.

The raw values provided by the scenario generator are not the object of RDM analysis. Instead comparisons are made across strategies using some measure of robustness. Many alternatives measures exist (e.g., absolute or relative regret), but the specific selection must ultimately be made in accordance with the problem setting.

## 2.2. An RDM Approach to Influence

In many influence settings, a persuader cannot be certain of many pertinent factors in the decision setting. The persuader can infer the prospects a decisionmaker(s) is considering but likely does not know these with certainty. Whereas the persuader confronts similar uncertainty with respect to a decisionmaker’s judged probabilities, outcome valuations, risk attitude, loss aversion, etc., it is likely that the persuader can bounded these factors within some range and subsequently apply the RDM framework to an influence setting.

As in Caballero and Lunday [3], herein we assume a persuader is attempting to influence a set of decisionmakers, I, to each select some prospect under conditions of risk. The set of available influence strategies<sup>1</sup>, ${ \vec { S } } ,$ is known to the persuader. Each decisionmaker i faces a finite set of prospects $J _ { i }$ such that each $j \in J _ { i }$ has a finite set of associated, uncertain outcomes, $K _ { i j }$ . That is, each decisionmaker is confronted with a decision tree. The persuader is uncertain of the specific structural form of these decision trees, but we assume a persuader is able to infer a finite collection of decision trees such that each decisionmaker’s true decision tree aligns with one of them. More formally, the persuader can identify the following uncertainty collections and uncertainty sets:

Decision Tree Uncertainty Collections

$\mathcal { I } _ { i }$ : A finite collection of prospect sets for decisionmaker i, one of which is the true $J _ { i }$

$\mathcal { K } _ { i j }$ : A finite collection of outcome sets for decisionmaker i and prospect $j ,$ one of which is the true $K _ { i j }$

Decision Tree Uncertainty Sets

$\hat { Y } _ { i j k }$ : Set of baseline raw values $\left( \hat { y } _ { i j k } \right)$ for the $k ^ { t h }$ event of prospect j for decisionmaker i

$\hat { P } _ { i j k }$ : Set of baseline probabilities $\left( \hat { p } _ { i j k } \right)$ for the $k ^ { t h }$ event of prospect $j$ for decisionmaker i

These uncertainty collections and sets describe all potential decision trees the persuader believes the decisionmakers could consider. However, the manner in which the decisionmakers evaluate the decision trees is also a source of uncertainty, as is the efect of a persuader’s influence action on both this evaluation and the decision trees themselves. Assuming the probability weighting functions and utility functions from Tversky and Kahneman [14] are utilized (i.e., equations (2a)–(2c)), these sources of uncertainty can be described via the following

uncertainty set $\mathrm { s } ^ { 2 }$ .

## Decisionmaker Uncertainty Sets

$\hat { \Gamma } _ { i }$ : Set of baseline gain probability weighting coeficients $( \hat { \gamma } _ { i } )$ for decisionmaker i

$\hat { D } _ { i }$ : Set of baseline loss probability weighting coeficients $( \hat { \delta } _ { i } )$ for decisionmaker i

${ \hat { A } } _ { i }$ : Set of baseline gain utility coeficients $\left( \hat { \alpha } _ { i } \right)$ for decisionmaker i

$\hat { B } _ { i }$ : Set of baseline loss utility coeficients $( { \hat { \beta } } _ { i } )$ for decisionmaker i

$\hat { \Lambda } _ { i }$ : Set of baseline loss aversion $( \hat { \lambda } _ { i } )$ coeficients for decisionmaker i

$\hat { R } _ { i }$ : Set of baseline reference points (ˆr ) for decisionmaker i

Influence Efect Uncertainty Sets

$F _ { i j k } ( s )$ : Set of influence efect mappings $\left( f _ { i j k } ( s ) \right)$ on the baseline raw

value for the $k ^ { t h }$ event of prospect j for decisionmaker i

$G _ { i j k } ( s )$ : Set of influence efect mappings $\left( g _ { i j k } ( s ) \right)$ ) on the baseline

probability for the $k ^ { t h }$ event of prospect j for decisionmaker i

$H _ { i } ^ { \theta }$ : Set of influence efect mappings $( h _ { i } ^ { \theta } ( s ) )$ altering decisionmaker

i’s baseline CPT-parameter $\hat { \theta }$ to $\theta , \theta \in \left\{ \gamma _ { i } , \delta _ { i } , \alpha _ { i } , \beta _ { i } , \lambda _ { i } , r _ { i } \right\}$

Moreover, this framework is also applicable to conditions of ambiguity per the results of Fox and Tversky [18]; however, select modifications are necessary to align the decision tree uncertainty sets with the tenets of Support Theory. That is, for each $K _ { i j }$ , an associated collection of sets $\mathcal { C } _ { i j }$ must be introduced, and the uncertainty set $\hat { P } _ { i j k }$ must be replaced with $\hat { P } _ { i j \Omega _ { u } }$ , respectively defined as follows:

$\mathcal { C } _ { i j }$ : Set of all non-empty subsets $\Omega _ { u } \subseteq K _ { i j }$

$\hat { P } _ { i j \Omega _ { u } }$ : Set of all baseline probabilities $\left( \hat { p } _ { i j \Omega _ { u } } \right)$ of event disjunction $\Omega _ { u }$ in prospect j by decisionmaker i.

Conceptually, the decision tree uncertainty collections $( \mathrm { i . e . , ~ } \mathcal { T } _ { i }$ and $\kappa _ { i j } )$ describe the structural uncertainty, and the remaining uncertainty sets describe the parametric uncertainty. Collectively, they also constitute all potential future states of the system. To ensure flexibility, we have left their form general; however, when discerning how to describe ${ \vec { F } } _ { : }$ , the specific properties of each uncertainty is paramount. If all of the aforementioned collections are countable, then $\vec { F }$ could potentially be taken via their enumeration. Otherwise, varying forms of space-filling designs should be considered to form ${ \vec { F } } .$ . If $\mathcal { I } _ { i }$ or $\kappa _ { i j }$ has a cardinality greater than 1, then standard space-filling designs such as the Latin hypercube are not applicable. From the perspective of experimental design, each possible $J _ { i }$ or $K _ { i j }$ is a categorical factor level. Therefore, alternative designs such as a sliced Latin hypercube [19, 20] should be considered. Other complicating factors restricting which space-filling designs can be utilized relate to the probabilistic nature of the uncertainty. When influencing a decisionmaker under risk, the axioms of probabilities must be satisfied, implying that the underlying design space is constrained. In such instances, the fast flexible design by Lekivetz and Jones [21] is an attractive alternative.

Once $\vec { F }$ has been determined, the value of each element in the futures ensemble $\vec { E }$ can be identified utilizing the scenario generator. In modeling influence, the scenario generator consists of a relatively direct application of CPT. Because each element of $\vec { E }$ considers a particular future, a specific element of each aforementioned uncertainty collections or sets is provided. In turn, each decision tree and its respective decisionmaker’s evaluation calculus is fully specified in its post influence state. As such, once the outcomes for each prospect have been sorted and partitioned into gains and losses, equations (1a)–(1g) can be applied to determine which prospect decisionmaker i prefers. More formally, for each decisionmaker i and a specified set of available prospects and associated outcomes $( \mathrm { i . e . , ~ } J _ { i } \in \mathcal { I } _ { i }$ and $K _ { i j } \in \mathcal { K } _ { i j } )$ , a set of outcome values and judged probabilities $( \mathrm { i . e . , ~ } y _ { i j k }$ and $p _ { i j k } )$ , and a tuple of CPT-parameters $( \gamma _ { i } , \delta _ { i } , \alpha _ { i } , \beta _ { i } , \lambda _ { i } , r _ { i } )$ is defined by

$$
y _ {i j k} = \hat {y} _ {i j k} + f _ {i j k} (s), \quad \forall i \in I, j \in J _ {i}, k \in K _ {i j},
$$

$$
x _ {i j k} = y _ {i j k} - r _ {i}, \quad \forall i \in I, j \in J _ {i}, k \in K _ {i j},
$$

$$
\begin{array}{r} p _ {i j k} = \hat {p} _ {i j k} + g _ {i j k} (s), \quad \forall i \in I, j \in J _ {i}, k \in K _ {i j}, \\ \theta_ {i} = \hat {\theta} _ {i} + h _ {i} ^ {\theta} (s), \quad \forall i \in I, \theta = \{\gamma_ {i}, \delta_ {i}, \alpha_ {i}, \beta_ {i}, \lambda_ {i}, r _ {i} \}, \end{array}
$$

and

$$
W ^ {+} (p _ {i j k}) = \frac {(p _ {i j k}) ^ {\gamma_ {i}}}{\left((p _ {i j k}) ^ {\gamma_ {i}} + (1 - p _ {i j k}) ^ {\gamma_ {i}}\right) ^ {\gamma_ {i} ^ {- 1}}},\tag{2a}
$$

$$
W ^ {-} (p _ {i j k}) = \frac {(p _ {i j k}) ^ {\delta_ {i}}}{\left((p _ {i j k}) ^ {\delta_ {i}} + (1 - p _ {i j k}) ^ {\delta_ {i}}\right) ^ {\delta_ {i} ^ {- 1}}},\tag{2b}
$$

$$
v (x _ {i j k}) = \left\{ \begin{array}{l} (x _ {i j k}) ^ {\alpha_ {i}}, \quad x _ {i j k} \geq 0 \\ - \lambda_ {i} (x _ {i j k}) ^ {\beta_ {i}}, \quad x _ {i j k} <   0. \end{array} \right.\tag{2c}
$$

These values are utilized in equations (1a)-(1g) to determine which prospect has the maximum value and is preferred by the decisionmaker.

The persuader’s utility is in turn afected by the collective choices of the decisionmakers. It may be the case that, for each decisionmaker and prospect set $J _ { i } ,$ the persuader prefers the decisionmaker to select some prospect $q ( J _ { i } )$ in a binary manner analogous to Caballero and Lunday [3], or the persuader may value the decisionmaker’s selection along some continuum. Therefore, the selection of this scenario generator measure is ultimately instance specific and depends upon the persuader’s goal for the system.

This selection of a scenario generator measure, in addition to the chosen robustness measure, evaluation criteria, and clustering algorithm are RDM tailorable components. As with RDM in a generic setting, each must be selected in accordance with the persuader’s objective.

## 3. Case Study: Badakhshan Landowner Crop Selection

Since the 1980s, opium cultivation has steadily increased in Afghanistan [22]. Production soared when the Taliban took control in 1996 [23], and today it has become an integral part of the rural Afghan economy [24]. In an unsecure and volatile environment, opium poppy cultivation is an appealing choice for Afghan farmers due to its high selling price, long shelf life, and profitable byproducts that can be used for, e.g., heating and livestock feed [25].

While the extent of opium cultivation is contested [26], much of the revenue associated with its trade is suspected to support the Taliban [5]. For this reason, counternarcotics and counterinsurgency have often been viewed as complementary campaigns by the United States. Unfortunately, no policy enacted over the course of the Afghan conflict has been able to meaningfully cripple the illict opium economy [6]. These failures are often attributed to a policy’s poor underpinnings to economic, social and cultural realities [25]. Whereas strategies considering such factors have long been advocated by Afghan experts [e.g., 22], the implementation of an efective counternarcotics policy has proven elusive [6].

![](/api/attachments/JKTP33YR/fulltext/images/6fd62e1e7453177fad865ab9b0754d62073e1842953516afd0a347bfaa2f8507.jpg)  
Figure 1: Badakhshan Province, Afghanistan

In this section, we illustrate how our modeling paradigm can be used to formulate policy informed by socio-economic realities and aimed at achieving a portion of the larger counternarcotics objective. Utilizing a variety of open source data, we formulate and solve a representative use case aimed at deterring the farmers in the northeastern province Badakhshan (Figure 1) from engaging in poppy cultivation. We model this province because it has witnessed high levels of poppy cultivation in areas under government control [27] and, as discussed by the Special Inspector General for Afghanistan Reconstruction (SIGAR) [6], a counternarcotic strategy requires such control to be efective.

## 3.1. Seasonal Crop Decision by Badakhshan Landowners

In this section, we illustrate how the structure of a farmer’s decision regarding what crop to plant and cultivate in a given season can be inferred. Although we utilize a variety of open source data over a variable time frame to inform this use case, an oficial policy development would be best served with recent data, tailored to the specific area of interest. As such, what follows is a representation of influence modeling under structural and parametric uncertainty. It is not meant to promote a specific policy, but instead to demonstrate the utility of the proposed methodology.

Landowners in Afghanistan generally have small holdings [28]. The same observation holds in the province of Badakhshan [29]. The Central Statistics Organization of Afghanistan [30] categorized Badakhshan farmers into three demographics: irrigated, rain-fed, and garden-plot farmers. On average, individual members of these groups own 4.2 jeribs (0.84 hectare), 6.4 jeribs (1.28 hectares), and 1.1 jeribs (0.22 hectares) of land, respectively [30]. Likewise, each demographic respectively constitutes 36%, 45%, and 19% of the 135,000 landowning households in the province [30]. The irrigated farmer demographic can be further subdivided based upon their irrigation system. A variety of irrigation systems are used in Afghanistan, including shallow wells known as arhads and man-made underground channels from aquifers known as karizs. Both of these systems are drought-resistant; however, other more vulnerable systems based on rivers, springs, and snow-melt also exist [31]. With this understanding, the irrigated farmer demographic can be subdivided into drought-resistant irrigated (DRI), and drought-vulnerable irrigated (DVI) farmers. According to the Central Statistics Organization of Afghanistan [32], between 35% and 45% of Badakhshan irrigated farmers have drought-resistant systems, compared to the Afghanistan-wide estimate of 24% [33]. Therefore, in this case study we model a “representative” decisionmaker from each of four demographics.

## I = {DRI, DVI, RF, GP}.

The relative distribution of each demographic is assumed to be 13%, 23%, 45%, and 19% of the total landowning population in Badakhshan in accordance with lower bound drought-resistant estimate provided by [32]. Likewise, we henceforth assume both rain-fed and garden-plot farmers are vulnerable to drought conditions, and that a representative farmer from each demographic owns the aforementioned average landholdings.

The crops available to Badakhshan farmers vary by district. However, there are a few staple options (e.g., potato and wheat) that are relatively ubiquitous [32]. Ideally, the influence model would consider all possible crop combinations; however, due to open source data availability and the illustrative purpose of this case study, we limit the crops available to farmers as a combination between wheat, potatoes, tomatoes, and opium poppies. To build $J _ { i } ,$ , we note that according to the Central Statistics Organization of Afghanistan [33], the majority of Afghan households cultivate one or two crops, and a minority plant up to three. We assume each farmer demographic i has the option to cultivate their land as one of the elements in the set $J _ { i }$ defined in equation (3).

$$
J _ {i} = \left[ \begin{array}{c} \text {Plant Opium Poppies (100\% of land)} \\ \text {Plant Wheat (100\% of land)} \\ \text {Plant Crop X (100\% of land)} \\ \text {Plant Opium Poppies, Wheat (50\%, 50\% of land each)} \\ \text {Plant Opium Poppies, Wheat (25\%, 75\% of land)} \\ \text {Plant Opium Poppies, Wheat (75\%, 25\% of land)} \\ \vdots \\ \text {Plant Opium, Wheat, Crop X (33\% of land each)} \\ \text {Plant Opium, Wheat, Crop X (50\%, 25\%, 25\% of land)} \\ \text {Plant Opium, Wheat, Crop X (25\%, 50\%, 25\% of land)} \\ \text {Plant Opium, Wheat, Crop X (25\%, 25\%, 50\% of land).} \end{array} \right]\tag{3}
$$

By the definition of $J _ { i } ,$ , we assume a representative basket of available options for each demographic includes three crops. Due to their widespread cultivation, we assume opium poppies and wheat are part of this basket. However, we allow for uncertainty in the third crop option (i.e., Crop X) which can be either potatoes or tomatoes. The uncertainty collection $\mathcal { I } _ { i }$ therefore has a cardinality of two for each farmer demographic i, wherein the definition in equation (3) is repeated for both possibilities of Crop X. Moreover, due to the small acreage of landholdings, we contend that the allocation strategies of 50-50 percent or 25-75 percent when planting two crops, and 33-33-33 percent or 50-25-25 percent when planting three crops are suficient to approximate actual behavior, providing 16 available prospects.

We assume a farmer considers two underlying uncertainties that afect their crop yield, and that for any decisionmaker i and prospect j, $\kappa _ { i j }$ is a singleton collection composed of the uncertainties defined in either equation (4) or (5). The amount of rainfall in a given season is a primary concern, and, if planting poppy, so is the possibility of an eradication raid by the government. Therefore, the uncertainty associated with a planting decision including poppy is

Ample Rainfall, No Raid

Drought, No Raid

Ample Rainfall, Raid

(4)

Drought, Raid

and the uncertainty associated with a planting decision excluding poppy is

$$
K _ {i j} = \left[ \begin{array}{c} \text { Ample   Rainfall } \\ \text { Drought } \end{array} \right].\tag{5}
$$

Having defined the decisionmakers and the decision tree uncertainty collections, the general form of each farmer’s crop selection decision is depicted in Figure 2.

We introduce the following alternative notation to improve readability of this use case. The payof (i.e., net income) associated with each prospect-outcome combination before influence $( \mathrm { i . e . , ~ } \hat { y } _ { i j k } )$ can also be denoted as ${ \hat { y } } _ { i } ( \%$ poppy, % wheat, % crop X, Rainfall Outcome, Raid Outcome). In the associated tuple, the first three elements describe the selected prospect j, whereas the final two elements describe the associated uncertain outcome k. A similar notational simplification is implemented for $\hat { p } _ { i j k }$

![](/api/attachments/JKTP33YR/fulltext/images/d4b661d27924db0c79191376607edf486788ad2fceda934103913126a86d301e.jpg)  
Figure 2: Generic Badakhshan Farmer Decision Tree

The uncertainty set $\hat { Y } _ { i j k }$ is compiled by combining the gross income and cost estimates by Kuhn [34] and from drought efects estimated by the UNODC [35]. Kuhn [34] provides net income projections per hectare for a variety of Afghan crops; however, these estimates were generated under the assumption of ample rainfall, judging by the coincidence of the poppy yield estimate with the actual yields observed in 2017 [35]. As such, the estimates listed by Kuhn [34] are used as a baseline for a season with ample rainfall, and they are adjusted based on observed data from the UNODC [35] to obtain net income estimates in drought seasons. That is, we utilize the UNODC [35] data to inform poppy income estimates and extrapolate the observed trends to other crops. Although this technique is not ideal for modeling accuracy, we utilize this naive approach due to a lack of data availability. The per jerib income values are listed in Table 1. Note that labor costs are assumed to be static at the rate listed by Kuhn [34], who does not itemize the price of irrigation maintenance. Likewise, the net income estimate per jerib are disparate across demographics based upon whether the household can accommodate the labor requirements internally or must hire contract labor.

For illustration purposes, we assume farmers make their decisions under conditions of risk. Likewise, since we assume independence between rainfall and poppy eradication raids, the probability associated with any outcome is simply the product of the associated rainfall and raid probabilities. A conservative approach is taken regarding the probability of drought, and it is assumed to be between [0.25, 0.75]. In accordance with the infrequent poppy eradication raids in Badakhshan in recent years [35], we assume they are viewed as improbable events with a range of [0.02, 0.05]. As such, for a prospect j with respective acreage allocations $a w$ and $a x$ for wheat and crop X without poppy cultivation,

Table 1: Estimated Per Jerib Net Income Range

<table><tr><td>Label</td><td>Farmer Demographic</td><td>Crop</td><td>Uncertain Outcome</td><td>Net Income per Jerib</td></tr><tr><td> $u_1$ </td><td>DRI</td><td>Poppy</td><td>A, NR</td><td>[$442, $1492]</td></tr><tr><td> $u_2$ </td><td>DRI</td><td>Poppy</td><td>D, NR</td><td>[$342,  $u_1$ ]</td></tr><tr><td> $u_3$ </td><td>DRI</td><td>Poppy</td><td>A/D, R</td><td>-$270</td></tr><tr><td> $u_4$ </td><td>DRI</td><td>Wheat</td><td>A, NR</td><td>[-$1, $149]</td></tr><tr><td> $u_5$ </td><td>DRI</td><td>Wheat</td><td>D, NR</td><td>[-$15,  $u_4$ ]</td></tr><tr><td> $u_6$ </td><td>DRI</td><td>Potato</td><td>A, NR</td><td>[$130, $919]</td></tr><tr><td> $u_7$ </td><td>DRI</td><td>Potato</td><td>D, NR</td><td>[$55,  $u_6$ ]</td></tr><tr><td> $u_8$ </td><td>DRI</td><td>Tomato</td><td>A, NR</td><td>[$74, $377]</td></tr><tr><td> $u_9$ </td><td>DRI</td><td>Tomato</td><td>D, NR</td><td>[$45, $u_8$ ]</td></tr><tr><td> $u_{10}$ </td><td>DVI</td><td>Poppy</td><td>A, NR</td><td>[$442, $1492]</td></tr><tr><td> $u_{11}$ </td><td>DVI</td><td>Poppy</td><td>D, NR</td><td>[$202,  $u_{10}$ ]</td></tr><tr><td> $u_{12}$ </td><td>DVI</td><td>Poppy</td><td>A/D, R</td><td>-$270</td></tr><tr><td> $u_{13}$ </td><td>DVI</td><td>Wheat</td><td>A, NR</td><td>[-$1,$149]</td></tr><tr><td> $u_{14}$ </td><td>DVI</td><td>Wheat</td><td>D, NR</td><td>[-$35,  $u_{13}$ ]</td></tr><tr><td> $u_{15}$ </td><td>DVI</td><td>Potato</td><td>A, NR</td><td>[$130, $910]</td></tr><tr><td> $u_{16}$ </td><td>DVI</td><td>Potato</td><td>D, NR</td><td>[-$50,  $u_{15}$ ]</td></tr><tr><td> $u_{17}$ </td><td>DVI</td><td>Tomato</td><td>A, NR</td><td>[$74, $377]</td></tr><tr><td> $u_{18}$ </td><td>DVI</td><td>Tomato</td><td>D, NR</td><td>[$5,  $u_{17}$ ]</td></tr><tr><td> $u_{19}$ </td><td>RF</td><td>Poppy</td><td>A, NR</td><td>[$380, $1430]</td></tr><tr><td> $u_{20}$ </td><td>RF</td><td>Poppy</td><td>D, NR</td><td>[$140,  $u_{19}$ ]</td></tr><tr><td> $u_{21}$ </td><td>RF</td><td>Poppy</td><td>A/D, R</td><td>-$333</td></tr><tr><td> $u_{22}$ </td><td>RF</td><td>Wheat</td><td>A, NR</td><td>[-$-1, 149]</td></tr><tr><td> $u_{23}$ </td><td>RF</td><td>Wheat</td><td>D, NR</td><td>[-$35,  $u_{22}$ ]</td></tr><tr><td> $u_{24}$ </td><td>RF</td><td>Potato</td><td>A, NR</td><td>[$130, $910]</td></tr><tr><td> $u_{25}$ </td><td>RF</td><td>Potato</td><td>D, NR</td><td>[-$50,  $u_{24}$ ]</td></tr><tr><td> $u_{26}$ </td><td>RF</td><td>Tomato</td><td>A, NR</td><td>[$74, $377]</td></tr><tr><td> $u_{27}$ </td><td>RF</td><td>Tomato</td><td>D, NR</td><td>[$5,  $u_{26}$ ]</td></tr><tr><td> $u_{28}$ </td><td>GP</td><td>Poppy</td><td>A, NR</td><td>[$504, $1554]</td></tr><tr><td> $u_{29}$ </td><td>GP</td><td>Poppy</td><td>D, NR</td><td>[$264,  $u_{28}$ ]</td></tr><tr><td> $u_{30}$ </td><td>GP</td><td>Poppy</td><td>A/D, R</td><td>-$208</td></tr><tr><td> $u_{31}$ </td><td>GP</td><td>Wheat</td><td>A, NR</td><td>[$26, $177]</td></tr><tr><td> $u_{32}$ </td><td>GP</td><td>Wheat</td><td>D, NR</td><td>[-$8,  $u_{31}$ ]</td></tr><tr><td> $u_{33}$ </td><td>GP</td><td>Potato</td><td>A, NR</td><td>[$174, $964]</td></tr><tr><td> $u_{34}$ </td><td>GP</td><td>Potato</td><td>D, NR</td><td>[-$6,  $u_{33}$ ]</td></tr><tr><td> $u_{35}$ </td><td>GP</td><td>Tomato</td><td>A, NR</td><td>[$117, $421]</td></tr><tr><td> $u_{36}$ </td><td>GP</td><td>Tomato</td><td>D, NR</td><td>[$48,  $u_{35}$ ]</td></tr></table>

we have

$$
\hat {P} _ {i j k} = \left\{(p _ {1}, p _ {2}) \left| \begin{array}{l} 0. 2 5 \leq p _ {1} \leq 0. 7 5, \\ 0. 2 5 \leq p _ {2} \leq 0. 7 5, \\ p _ {1} + p _ {2} = 1 \end{array} \right. \right\}
$$

where

$$
\begin{array}{l} p _ {1} = p (\text {ample rain}) = p _ {i} (0, a _ {W}, a _ {X}, \mathrm{A,NR}), \text {and} \\ p _ {2} = p (\text {drought}) = p _ {i} (0, a _ {W}, a _ {X}, \mathrm{D,NR}). \end{array}
$$

For a prospect $j$ including poppy cultivation with an acreage percentage $a _ { P } .$ , we have

$$
\hat {P} _ {i j k} = \left\{(p _ {1}, p _ {2}, p _ {3}, p _ {4}) \left| \begin{array}{l} 0. 2 5 \leq p _ {1} \leq 0. 7 5, 0. 2 5 \leq p _ {2} \leq 0. 7 5, \\ 0. 0 2 \leq p _ {3} \leq 0. 0 5, 0. 0 2 \leq p _ {4} \leq 0. 0 5 \\ p _ {1} + p _ {2} = 1, p _ {3} + p _ {4} = 1 \end{array} \right. \right\}
$$

where

$$
\begin{array}{l} p _ {1} = p (\text {ample rain}) = p _ {1}, \\ p _ {2} = p (\text {drought}) = 1 - p _ {1}, \\ p _ {3} = p (\text {raid}), \\ p _ {4} = p (\text {no raid}) = 1 - p _ {3}, \end{array}
$$

and

$$
\begin{array}{c} p _ {i} (a _ {P}, a _ {W}, a _ {X}, \mathrm{A}, \mathrm{NR}) = p _ {1} p _ {4}, \\ \vdots \\ p _ {i} (a _ {P}, a _ {W}, a _ {X}, \mathrm{D}, \mathrm{R}) = p _ {2} p _ {3}. \end{array}
$$

Finally, we turn our attention to the parameterization of the decisionmaker uncertainty sets. We leverage the works of Booij and Van de Kuilen [36], Abdellaoui [37], and Abdellaoui et al. [38] to inform the uncertainty sets associated with the probability weighting, utility curvature, and loss aversion coeficients, respectively. In the case of the utility curvature coeficients, the uncertainty sets are taken to be the range of estimates from the literature provided by Booij and Van de Kuilen [36], whereas the experimental results from [37, 38] directly inform the probability weighting and loss aversion uncertainty sets. A more simplistic approach is taken with the reference point uncertainty set, and it is derived from Table 1 by the range formed via the product of the minimum and maximin unit net income values with each demographic’s assumed landholdings. The resulting sets are quantified in Table 2 wherein $L _ { i }$ refers to the assumed size of demographic i’s landholdings. Of note, demographic decisionmaker uncertainty sets are assumed to be identical (except for the scale of ${ \hat { R } } _ { i } )$ of ambiguity relating to the manner in which Badakhshan farmers distinguish between prospects.

Table 2: Decisionmaker Uncertainty Sets

<table><tr><td> $\hat{\Gamma}_{i}$ </td><td> $\hat{D}_{i}$ </td><td> $\hat{A}_{i}$ </td><td> $\hat{B}_{i}$ </td><td> $\hat{\Lambda}_{i}$ </td><td> $\hat{R}_{I}$ </td></tr><tr><td>[0.492, 0.708]</td><td>[0.588, 0.812]</td><td>[0.22, 1.01]</td><td>[0.61, 1.06]</td><td>[0.74, 8.27]</td><td>[-333 $L_{i}$ , 1554 $L_{i}$ ]</td></tr></table>

## 3.2. Influence Actions and their Efects

In the Afghan conflict, multiple counternarcotic strategies have been attempted. The influence actions these strategies rely upon can be broadly classified into four categories [6]: eradication, interdiction, alternative development, and political support mobilization. Eradication eforts focus on the destruction of a standing poppy crop, whereas interdiction eforts, to include narcotics seizures, are applied further along the supply chain. Alternative development programs are designed to reduce poppy cultivation by increasing the attractiveness of licit livelihood opportunities. Finally, political support mobilization is a wide ranging category including public awareness campaigns and other eforts designed to strengthen Afghan institutions. Herein, we assume that the persuader’s task is to select some combination of these four actions to reduce poppy cultivation in Badakhshan.

For this case study, we adopt a strategic-level perspective and describe how each influence efort can be expected to afect the decisionmaker and the decision setting. Eradication campaigns, regardless of their form, target the farmers themselves. As such, an increase in their intensity will necessarily coincide with an increase in the probability of a poppy farming raid, and the reduced overall supply will result in increased expected income for successful harvests [39]. Conversely, interdiction eforts have an indirect efect on farmers. By targeting upstream entities, they serve to reduce the demand observed by the poppy farmers [39] and, in isolation, can be expected to decrease farm-gate values.

The efects of an alternative development program are varied. However, herein we assume that such programs targeted at potential poppy farmers are designed to increase the attractiveness of cultivating wheat, potato, or tomato via either reducing costs or increasing profits. Likewise, the efects of political support mobilization are diverse, but herein we assume such action is composed of a public awareness campaign and provincial leader engagement with the following efects. The public awareness campaign reinforces the criminality of poppy cultivation and underscores the financial risks associated with a destroyed crop, whereas the provincial leaders are encouraged to increase poppy related taxes. As such, political support mobilization can be expected to increase a farmer’s judged probability of a raid and decrease the net income associated with poppy.

Table 3: Actions Included (Y) and Excluded (N) in each Influence Strategy

<table><tr><td>Influence Strategy ( $s_{cand}$ )</td><td> $s_1$ </td><td> $s_2$ </td><td> $s_3$ </td><td> $s_4$ </td><td> $s_5$ </td><td> $s_6$ </td><td> $s_7$ </td><td> $s_8$ </td><td> $s_9$ </td><td> $s_{10}$ </td><td> $s_{11}$ </td><td> $s_{12}$ </td><td> $s_{13}$ </td><td> $s_{14}$ </td><td> $s_{15}$ </td><td> $s_{16}$ </td></tr><tr><td>Eradication</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>N</td><td>Y</td></tr><tr><td>Interdiction</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>Alternative Development</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>Pol. Sup. Mobilization</td><td>N</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr></table>

All available influence strategies $( \mathrm { i . e . , } \ \vec { S } )$ are listed in Table 3. Likewise, the uncertainty sets for influence efects that account for these dynamics are displayed in Table 4. These uncertainty sets are assumed to be static across all decisionmakers. Each strategy, if employed, is assumed to have an additive efect on the associated parameter as listed. For example, for some decisionmaker i and prospect j (including poppy) wherein outcome k represents the ample rainfall, raid outcome, we have

$$
\begin{array}{c} G _ {i j k} (s _ {2}) = [ 0, 0. 7 ], \\ p _ {i j k} = \hat {p} _ {i j k} + g _ {i j k} (s _ {2}), \quad g _ {i j k} (s _ {2}) \in G _ {i j k} (s _ {2}). \end{array}
$$

Moreover, if an influence strategy employs multiple actions simultaneously, the cumulative efect is assumed to be additive. For instance, if influence strategy $s _ { 8 }$ is utilized instead of $s _ { 2 }$ we would have

$$
\begin{array}{r l} g _ {i j k} (s _ {8}) = g _ {i j k} (s _ {2}) + g _ {i j k} (s _ {5}), & g _ {i j k} (s _ {1}) \in G _ {i j k} (s _ {2}), \\ & g _ {i j k} (s _ {5}) \in G _ {i j k} (s _ {5}), \\ p _ {i j k} = \hat {p} _ {i j k} + g _ {i j k} (s _ {8}). \end{array}
$$

Any entry not listed in Table 4 is assumed to have a null efect. Likewise,in accordance with Table 1, we assume that if a property is raided, the efect is certain (i.e., all poppy is destroyed with resulting damages).

Table 4: Influence Efects on Decision Setting

<table><tr><td>Influence</td><td>Raid Probability</td><td>Poppy Income (NR)</td><td>Wheat Income</td><td>Potato Income</td><td>Tomato Income</td></tr><tr><td> $s_{2}$ </td><td>[0.00, 0.7]</td><td>[-0.05 $\hat{y}_{ijk}$ , 0.2 $\hat{y}_{ijk}$ ]</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $s_{3}$ </td><td>-</td><td>[-0.15 $\hat{y}_{ijk}$ , 0.1 $\hat{y}_{ijk}$ ]</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $s_{4}$ </td><td>-</td><td>-</td><td>[-0.25 $\hat{y}_{ijk}$ , 5.00 $\hat{y}_{ijk}$ ]</td><td>[-0.25 $\hat{y}_{ijk}$ , 2.00 $\hat{y}_{ijk}$ ]</td><td>[-0.25 $\hat{y}_{ijk}$ , 3.00 $\hat{y}_{ijk}$ ]</td></tr><tr><td> $s_{5}$ </td><td>[-0.02, 0.05]</td><td>[-0.2 $\hat{y}_{ijk}$ , 0.1 $\hat{y}_{ijk}$ ]</td><td>-</td><td>-</td><td>-</td></tr></table>

In this case study, the numerical efects of influence are considered utilizing uncertainty sets meant to capture conflicting opinions and designed to allow for alternative efects than those anticipated (e.g., s decreasing the raid probability). Such conflict is historically characteristic of counternarcotic policy discussions in Afghanistan [40]. Therefore, the notional efects in this case study are designed to be a representation of the true policy-making environment.

## 3.3. RDM Tailorable Components

Having defined the uncertainty collections and sets, the next steps in the RDM approach consist of identifying a space filling design from which to build ${ \vec { F } } ,$ a scenario generator measure, a robustness measure, an evaluation criteria, and a clustering algorithm.

From an experimental design perspective, we are considering one categorical factor with two levels $\left( \ \mathrm { i . e . , \ } \mathcal { T } _ { i } \right)$ and 70 additional continuous factors including each decisionmaker’s CPT-parameter values, the respective influence’s efects, and each crop’s profitability. To accommodate this setting, we utilize a sliced Latin hypercube design because it allows for optimal space-filling properties to be pursued within and between the categorical factor levels [20]. The specific design used has two slices and 1000 points in each slice, yielding an $\vec { F }$ with 2000 futures.

A variety of scenario generator measures could be used depending upon the precise nature of the persuader’s priorities. For instance, the persuader may wish to reduce the total number of households cultivating poppy, or may wish to minimize the total number of jeribs utilized for poppy cultivation. Both fall within the larger counternarcotics objective, but are alternative metrics of success. Preferably, the selection of such a measure would be informed based upon the specific nature of the insurgency’s poppy-related income stream. Absent this information, we focus on the latter scenario generator measure related to minimizing the total number of poppy cultivated jeribs. In large part, this decision is made to align with the historical priorities of US and UN policymakers [6, 27].

Furthermore, absolute regret is utilized as a robustness measure to facilitate communication of results in natural units. The interpretation of this absolute regret measure is the number of additional poppy cultivated jeribs in a given scenario from the “optimal”. Moreover, the evaluation criteria selected is expected regret for similar reasons. The number of poppy cultivated jeribs in Afghanistan has a direct impact on the worldwide opium supply, and the retention of this conceptually-accessible meaning is important when communicating regret to senior policymakers.

With regard to clustering, Lempert et al. [41] advocate for the use of two hierarchical clustering algorithms (i.e., CART and PRIM). The authors argue that each of these clustering techniques have high interpretability because they segment the area of interest into hyper-rectangular regions. Empirically, both algorithms are shown to perform well; however, CART regions are guaranteed to be disjoint whereas PRIM regions may overlap. For this reason, the CART algorithm is utilized in this study.

## 3.4. Analysis and Results

The result of each influence strategy on the number of jeribs produced for each future in $\vec { F }$ is depicted in Figure 3. It can be observed that the null strategy $( \mathrm { i . e . , } s _ { 1 } )$ and most influence strategies composed of singleton actions $( \mathrm { i . e . , } \ s _ { 2 } , \ s _ { 3 } ,$ 2 $s _ { 5 } )$ result in a large number of expected poppy cultivated jeribs. Among the nonsingleton strategies, each of the strategies not including alternative development as an action $( \mathrm { e . g . } , s _ { 6 } )$ results in many poppy cultivated jeribs as well, indicating the importance of such actions in a successful influence strategy.

![](/api/attachments/JKTP33YR/fulltext/images/59a8e23992cca1a1942a7d766b5b3a6828ecfdc1e72bff04cfaf5af819c4f51c.jpg)  
Figure 3: Distribution of Poppy Cultivated Jeribs over all Futures

The amount of variability in poppy cultivated jeribs for most of the strategies depicted in Figure 3 coincides with the historical dificulties encountered by those developing counternarcotic policy. Even strategies having the greatest potential benefit may be inefectual when applied. For instance, if one were to assume all futures equally likely, $s _ { 1 6 }$ results in the lowest number of expected poppy cultivated jeribs even though instances exist having no decrease in cultivation relative to the null strategy. As such, the raw distributional data on poppy cultivated areas is not suficient to determine which of the sixteen strategies is robust, and the results of Figure 4 must be analyzed.

![](/api/attachments/JKTP33YR/fulltext/images/d3bfb96b96055210f0de7215d6622377dd127812b112dcd1b30a36b67fbf7328.jpg)  
Figure 4: Distribution of Absolute Regret over all Futures

By observing this figure, we can discriminate better between strategies. Differences between $s _ { 1 2 }$ regret ranges. A similar observation holds for $s _ { 7 }$ and $s _ { 1 6 }$ . Notably, we also see that $s _ { 7 } ,$ s<sub>12</sub>, $s _ { 1 4 } ,$ $s _ { 1 6 }$ all have an expected absolute regret of zero. However, $s _ { 1 4 }$ and $s _ { 1 6 }$ have the smallest interquartile-regret ranges and are leading contenders for the candidate strategy for policy implementation. Of the two, $s _ { 1 6 }$ has the lower 90th percentile regret and, for this reason, is chosen as $s _ { c a n d } .$

With a candidate strategy selected, the RDM methodology calls for hedging options to be explored. As in Lempert et al. [4], each future’s output is transformed into a binary response. The binary response coincides with an absolute regret threshold set forth by senior policymakers. We assume for this use case that such a limit is 2500 jeribs in regret. That is, if the poppy cultivated jeribs for $s _ { c a n d }$ exceeds 2500 jeribs of the best strategy for some future, then that future is considered a vulnerability of $s _ { c a n d }$

Utilizing this technique, the CART algorithm clusters the space into eight regions of interest. These regions are separated based on the efectiveness of select counternarcotics actions, and a subset of demographics’ perceptions on crop income. However, one cluster stands out as having a high density of vulnerabilities and high average absolute regret. It is characterized by the simultaneous efectiveness of interdiction and political support mobilization, the inefectiveness of eradication messaging, the DVI demographic believing poppy and wheat income high in ample rain conditions conditions, and the RF demographic regarding poppy income as high in ample rain conditions and tomato income as high in drought conditions. With this vulnerable narrative identified, the tradeofs between utilizing $s _ { 1 6 }$ or some other strategy in terms of expected absolute regret can be examined.

![](/api/attachments/JKTP33YR/fulltext/images/3df95cc45d8c85c0a32cda66d134066ef093631162c2b70ac4b02ae6b6c0ebd2.jpg)  
Figure 5: Cluster Tradeofs Between $s _ { 1 6 }$ and Other Strategies

Figure 5 illustrates the tradeofs between utilizing $s _ { 1 6 }$ vis-´a-vis the alternatives in terms of expected absolute regret. The coordinate location of each strategy is determined by its expected absolute regret via two narratives: the vulnerability cluster and the remaining futures. The four strategies not depicted in Figure 5 $( \mathrm { i . e . , } s _ { 1 } , s _ { 3 } , s _ { 5 } , s _ { 1 0 } )$ exceed $\mathrm { 3 \times 1 0 ^ { 5 } }$ in both narratives. A frontier of non-dominated strategy performance is formed by $s _ { 1 2 }$ and $s _ { 1 6 }$ , as depicted by the solid line. This frontier indicates that only $s _ { 1 2 }$ and $s _ { 1 6 }$ are non-dominated strategies under this narrative bifurcation. It can be observed that a persuader’s preference between the two depends upon the respective weight (perhaps in terms of probability)

At this point, the RDM process can be repeated with $s _ { 1 2 }$ as $s _ { c a n d }$ and, potentially, with the inclusion of additional information, if available. Conversely, the RDM analysis can terminate with a choice between $s _ { 1 2 }$ and $s _ { 1 6 }$ based upon the persuader’s beliefs on the vulnerable and the remaining future narratives for expected absolute regret.

Given the state of information in this case study, we cease analysis after one round of analysis. Between the two potential strategies, we contend that $s _ { 1 6 }$ is likely preferable to $s _ { 1 2 }$ due to exogenous factors. Specficially, the risk of implementing $s _ { 1 2 }$ to other objectives not quantified in Figure 5 (e.g., support from the international community) by not including host nation oficials via politica support mobilization diferentiates it from $s _ { 1 6 }$ in a negative manner. Furthermore, $s _ { 1 6 }$ has a successful precedent; its structure is akin to the policy utilized during the Helmand Food Zone (HFZ) program that successfully deterred landowners from cultivating poppy in the more opium-dependent province of Helmand [6]. Thus, the identification of $s _ { 1 6 }$ has face validity and is sensible for the provided uncertainties.

## 3.5. Discussion and Limitations

The problem formulation discussed in Sections 3.1 and 3.2 illustrates how policy-making influence problems can be parameterized and quantitatively represented. Furthermore, Sections 3.3 and 3.4 respectively demonstrate how to apply the RDM method to an influence setting, as well as the types of insights that its usage can garner from a deeply uncertain environment. The techniques described herein form a systematic and tractable decision support tool wherein fundamental behavioral assumptions are readily visible, a feature often obscured in policy-making approaches.

With regard to the analysis in Section 3.4, the selection of $s _ { 1 6 }$ as an initial candidate strategy is reinforced by counternarcotic doctrine proposed by Ward and Byrd [22] and SIGAR [6], who envision it as a multifaceted efort. The choice between $s _ { 1 2 }$ and $s _ { 1 6 }$ also coincides with core issues at the heart of the Afghan conflict: the efectiveness of interdiction and security cooperation eforts [6]. Moreover, both $s _ { 1 2 }$ and $s _ { 1 6 }$ include an eradication action, indicating that, from a myopic perspective (i.e., a single growing season), eradication may be an efective tool for deterring the cultivation of poppy by Afghan landowners. Current Afghan counternarcotic doctrine deemphasizes eradication based on its historical failure to efectively impede long term poppy cultivation trends; however, our analysis suggests that eradication may be appropriate to include in a strategy having a shorter planning horizon, which may be relevant to set the conditions for strategic actions (e.g., diplomatic negotiation).

The modeling methodology also addresses some criticisms by Mansfield and development. That is, we do not treat the Afghan farmer as a homogeneous entity maximizing gross profit, nor one who makes a binary decision between opium poppy and wheat. Instead our approach addresses the diversity of Afghanistan demographics, considers net profits, and examines a variety of crop selection profiles.

However, the modeling methodology utilized is not a perfect representation of reality. Although we addressed the diversity of Badakshan farmers, a higher fidelity characterization may be required to inform policy decisions. Badakhshan is a multiethnic region comprised of Tajiks, Uzbeks, and Pashtos, among others [42]. The efect of a farmer’s demographic on a crop decision may be non-trivial, especially when concerned with emotional stimuli. Moreover, a diverse set of crop options is available to Afghan farmers, and a richer characterization of them may be required using district rather than provincial level data. Unfortunately, the data required to inform such decisions at this granular level is not available via open source collections and would require an expansive data collection efort analogous to other United Nations Ofice on Drugs and Crime (UNODC) projects.

Our models also only consider a portion of the interconnected Afghan economy, of which farming is a critical component. It provides land-access (via sharecropping) and income (via day labor) to the rural poor. Therefore, the crop selection of Afghan landowners can have far reaching efects. Such efects were observed during the implementation of the HFZ. While the program resulted in landowners deciding to plant less poppy, their decisions resulted in less profitable sharecropping agreements and less demand for on-farm labor [43]. In turn, many landless poor migrated to former desert areas and increased poppy cultivation in these regions [6]. Just as such efects were unforeseen by the planners of the HFZ, so too would they be unforeseen in the analysis presented in this research. The decisions of the landless poor could be included and linked to the our analysis but, ultimately, the scale of the influence model must be determined based upon the persuader’s underlying objectives.

Finally, the Badakhshan landowner influence model is designed to afect change in a single growing season. Such a time frame is far too short upon which to build a comprehensive counternarcotics policy. Historically, successful policies have taken decades versus months or years [22] and, in this time frame, external market factors not incorporated in this research become increasingly relevant. Therefore, the models illustrated herein do not yield a panacea to stop poppy cultivation, but they facilitate the development of counternarcotic policy toward incremental, gradual change.

## 4. Conclusions

In this research, we presented a framework for modeling influence under parametric and structural uncertainty and illustrated how robust decisions in this setting can be identified. The utility of our methodology was demonstrated on the global, contemporary problem posed by the illicit, Afghan opium economy. Specific emphasis was applied to reducing opium poppy supply from the world’s leading poppy producing nation by targeting the Afghan province of Badakhshan.

As illustrated in the case study, our robust approach to design and assess influence strategies is capable of providing decision support and garnering insights from a deeply uncertain environment, to the extent that the underlying uncertainties have been properly identified. Such empathetic and cognizant uncertainties are an inherent feature of any influence policy decision; however, by defining these uncertainties in a manner consistent with this manuscript, others may utilize our methods to provide a systematic and tractable basis upon which robust policy decisions can be identified.

## Disclaimers

The views expressed in this paper are those of the authors and do not reflect the oficial policy or position of the United States Air Force, the Department of Defense, or the United States Government. This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## References

[1] T. Chesney, S.-H. Chuah, R. Hofmann, J. Larner, The Influence of Influence: The Efect of Task Repetition on Persuaders and Persuadees, Decision Support Systems 94 (2017) 12–18.

[2] S. J. Kim, E. Maslowska, A. Tamaddoni, The Paradox of (Dis)trust in Sponsorship Disclosure: The Characteristics and Efects of Sponsored Online Consumer Reviews, Decision Support Systems 116 (2019) 114–124.

[3] W. Caballero, B. Lunday, Influence Modeling: Mathematical Programming Representations of Persuasion under either Risk or Uncertainty, European Journal of Operational Research 278 (2019) 266–282. doi:https://doi.org/10.1016/j.ejor. 2019.04.006.

[4] R. J. Lempert, D. G. Groves, S. W. Popper, S. C. Bankes, A General, Analytic Method for Generating Robust Strategies and Narrative Scenarios, Management Science 52 (2006) 514–528.

[5] SIGAR, Quarterly Report to the United States Congress, 2018. Special Inspector General for Afghanistan Reconstruction.

[6] SIGAR, Counternarcotics: Lessons from the U.S. Experience in Afghanistan, 2018. Special Inspector General for Afghanistan Reconstruction.

[7] J. Clemens, Opium in Afghanistan: Prospects for the Success of Source Country Drug Control Policies, The Journal of Law and Economics 51 (2008) 407–432.

[8] D. Mejia, P. Restrepo, The Economics of the War on Illegal Drug Production and Traficking, Journal of Economic Behavior & Organization 126 (2016) 255–275.

[9] D. Arnott, S. Gao, Behavioral Economics for Decision Support Systems Researchers, Decision Support Systems (2019).

[10] H. Jang, A Decision Support Framework for Robust R&D Budget Allocation using Machine Learning and Optimization, Decision Support Systems 121 (2019) 1–12.

[11] D. Kahneman, A. Tversky, Subjective Probability: A Judgment of Representativeness, Cognitive Psychology 3 (1972) 430–454.

[12] A. Tversky, D. Kahneman, The Framing of Decisions and the Psychology of Choice, Science 211 (1981) 453–458.

[13] T. Kugler, T. Connolly, L. D. Ord´o˜nez, Emotion, Decision, and Risk: Betting on Gambles versus Betting on People, Journal of Behavioral Decision Making 25 (2012) 123–134.

[14] A. Tversky, D. Kahneman, Advances in Prospect Theory: Cumulative Representation of Uncertainty, Journal of Risk and Uncertainty 5 (1992) 297–323.

[15] G. Gigerenzer, R. Selten, Bounded Rationality: The Adaptive Toolbox, MIT Press, Cambridge, MA, 2002.

[16] T. Pachur, R. S. Suter, R. Hertwig, How the Twain Can Meet: Prospect Theory and Models of Heuristics in Risky Choice, Cognitive Psychology 93 (2017) 44–73.

[17] R. M. Campos-Vazquez, E. Cuilty, The Role of Emotions on Risk Aversion: A Prospect Theory Experiment, Journal of Behavioral and Experimental Economics 50 (2014) 1–9.

[18] C. R. Fox, A. Tversky, A Belief-based Account of Decision Under Uncertainty, Management Science 44 (1998) 879–895.

[19] P. Z. Qian, Sliced Latin Hypercube Designs, Journal of the American Statistical Association 107 (2012) 393–399.

[20] S. Ba, W. R. Myers, W. A. Brenneman, Optimal Sliced Latin Hypercube Designs, Technometrics 57 (2015) 479–487.

[21] R. Lekivetz, B. Jones, Fast Flexible Space-filling Designs for Nonrectangular Regions, Quality and Reliability Engineering International 31 (2015) 829–837.

[22] C. Ward, W. A. Byrd, Afghanistan’s Opium Drug Economy, World Bank Washington, DC, 2004.

[23] C. Woody, Afghanistan is Producing a Lot More Opium than Before the US In-

vasion. The US Just Can’t Stop It, https://www.businessinsider.com/the-uscant-seem-to-cut-back-afghanistans-opium-production-2018-6, 2018. Business Insider.

[24] W. A. Byrd, Disease or Symptom? Afghanistan’s Burgeoning Opium Economy in 2017, 2017. Afghanistan Research and Evaluation Unit.

[25] D. Mansfield, P. Fishstein, Time to Move on: Developing an Informed Development Response to Opium Poppy Cultivation in Afghanistan, 2016. Afghanistan Research and Evaluation Unit.

[26] D. Mansfield, Bombing Heroin Labs in Afghanistan: The Latest Act in the Theatre of Counternarcotics, 2018. LSE International Drug Policy Unit.

[27] UNODC, Afghanistan Opium Survey 2017: Challenges to Sustainable Development, Peace and Security, https://www.unodc.org/documents/cropmonitoring/Opium-survey-peace-security-web.pdf, 2018.

[28] UNODC, The Opium Economy in Afghanistan: An International Problem, 2003. United Nations Ofice on Drugs and Crime.

[29] A. Pain, Afghanistan Livelihood Trajectories: Evidence from Badakhshan, 2010. Afghanistan Research and Evaluation Unit.

[30] Central Statistics Organization of Afghanistan, Afghanistan Living Conditions Survey 2011-2012, 2013. CSO.

[31] A. S. Qureshi, Water Resources Management in Afghanistan: The Issues and Options, 2002. International Water Management Institute.

[32] Central Statistics Organization of Afghanistan, Badakhshan: A Socio-economic and Deomgraphic Profile, 2007. CSO and UNFPA.

[33] Central Statistics Organization of Afghanistan, Afghanistan Living Conditions Survey 2016-2017, 2018. CSO.

[34] G. A. Kuhn, Roots of Peace Crop Income Projection: Afghanistan 2010, 2010. Roots of Peace.

[35] UNODC, Afghanistan Opium Survey 2018: Cultivation and Production, 2018.

[36] A. S. Booij, G. Van de Kuilen, A Parameter-free Analysis of the Utility of Money for the General Population under Prospect Theory, Journal of Economic Psychology 30 (2009) 651–666.

[37] M. Abdellaoui, Parameter-Free Elicitation of Utility and Probability Weighting Functions, Management Science 46 (2000) 1497–1512.

[38] M. Abdellaoui, H. Bleichrodt, C. Paraschiv, Loss Aversion under Prospect Theory: A Parameter-free Measurement, Management Science 53 (2007) 1659–1674.

[39] E. Martin, S. Symansky, Macroeconomic Impact of the Drug Economy and Counter-Narcotics Eforts, in: Buddenberg, Doris and Byrd, William A. (Ed.), Afghanistan’s Drug Industry: Structure, Functiong Dynamics, and Implications for Counter-Narcotics Policy, The World Bank, 2006, pp. 25–51.

[40] S. Coll, Directorate S: The CIA and America’s Secret Wars in Afghanistan and Pakistan, Penguin Books, New York, NY, 2019.

[41] R. J. Lempert, B. P. Bryant, S. C. Bankes, Comparing Algorithms for Scenario Discovery, Technical Report, Santa Monica, CA: RAND Corporation, 2008.

[42] P. Fishstein, Evolving Terrain: Opium Poppy Cultivation in Balkh and Badakhshan Provinves in 2013, 2014. Afghanistan Research and Evaluation Unit.

[43] D. Mansfield, Truly Unprecedeneted: How the Helmand Food Zone Supported an

Increase in the Province’s Capacity to Produce Opium, 2017. Afghanistan Research and Evaluation Unit.

## Highlights

• A quantitative decision support framework to design influence policy is developed

• Favorable courses of action are distilled under conditions of deep uncertainty

• Uncertain agent behavior is characterized utilizing Cumulative Prospect Theory

• The method’s utility is demonstrated in an Afghan counternarcotics case study

![](/api/attachments/JKTP33YR/fulltext/images/bba5f93aad28ad07f95056fa843c5545910a5357d87e6df336449284e2d4cca2.jpg)  
Figure 1

![](/api/attachments/JKTP33YR/fulltext/images/f4f69333a7a78a57c626c7e7ce7ce097564d585e85206fe641f859285d3d4cf0.jpg)

![](/api/attachments/JKTP33YR/fulltext/images/1b01864936d58254a88340c1f7236f7aa90935a2ee6dba18bd6e48129c1bb2c1.jpg)  
Figure 3

![](/api/attachments/JKTP33YR/fulltext/images/5857e5edb443524a985c44669564332128472eaac997dcc02da09c88f84cad23.jpg)  
Figure 4

![](/api/attachments/JKTP33YR/fulltext/images/949ab5e0d262a5f0945c58ef3dede51e030b5fa35e2e05fce96963b06ee67b76.jpg)  
Figure 5
