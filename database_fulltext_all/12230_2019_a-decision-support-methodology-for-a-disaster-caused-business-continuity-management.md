---
otero_id: 12230
otero_key: "MSB9RPB2"
title: "A decision support methodology for a disaster-caused business continuity management"
authors: "Frank Schätter; Ole Hansen; Marcus Wiens; Frank Schultmann"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.12.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

A decision support methodology for a disaster-caused business continuity management

Decision Support Systems

![](/api/attachments/MSB9RPB2/fulltext/images/5dabeda8c01e7836012c3ceadfd736832c66a48e0ce1d750d275fe604e4376a0.jpg)

Frank Schätter, Ole Hansen, Marcus Wiens, Frank Schultmann

PII: S0167-9236(18)30202-1

DOI: https://doi.org/10.1016/j.dss.2018.12.006

Reference: DECSUP 13019

To appear in: Decision Support Systems

Received date: 8 August 2018

Revised date: 25 November 2018

Accepted date: 19 December 2018

Please cite this article as: Frank Schätter, Ole Hansen, Marcus Wiens, Frank Schultmann , A decision support methodology for a disaster-caused business continuity management. Decsup (2018), https://doi.org/10.1016/j.dss.2018.12.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Title

A decision support methodology for a disaster-caused business continuity management

## Declarations of interest

None

## Authors

1. Frank Schätter, Karlsruhe Institute of Technology (KIT), Institute for Industrial Production (IIP), Hertzstraße 16, 76187 Karlsruhe, Germany, Tel.: +49 721 608 44551, frank.schaetter@kit.edu.

2. Ole Hansen, Kühne Logistics University (KLU), Großer Grasbrook 17, 20457 Hamburg, Germany, Tel.: +49 40 3287 07 303, ole.hansen@the-klu.org.

3. Marcus Wiens, Karlsruhe Institute of Technology (KIT), Institute for Industrial Production (IIP), Hertzstraße 16, 76187 Karlsruhe, Tel.: +49 721 608 44410, marcus.wiens@kit.edu.

4. Frank Schultmann, Karlsruhe Institute of Technology (KIT), Institute for Industrial Production (IIP), Hertzstraße 16, 76187 Karlsruhe, Tel.: +49 721 608 44469, frank.schultmann@kit.edu.

## Abstract

Supply chain risk management typically deals with the systematic identification, analysis and mitigation of risks which affect the whole supply chain network of a company. Business continuity management (BCM) forms part of supply chain risk management and is an important competitive factor for companies by ensuring the smooth functioning of critical business processes in the case of failures. If business operations are severely disrupted, the companies’ decision maker is confronted with a situation which is characterized by a high degree of uncertainty, complexity and time pressure. In such a context, decision support can be of significant value. This article presents a novel decision support methodology which leads to an improved and more robust BCM for severe disruptions caused by disasters. The methodology is part of the Reactive Disaster and supply chain Risk decision Support System (ReDRiSS) to deal with different levels of information availability and to provide decision makers with a robust decision recommendation regarding resource allocation problems. It combines scenario techniques, optimization models and approaches from decision theory to operate in an environment characterized by sparse or lacking information and dynamic changes over time. A simulation case study is presented where the methodology is applied within the BCM of a food retail company in Berlin that is affected by a pandemic disaster.

## Keywords

Business continuity management, decision support system, robust decision-making, risk management, disaster management

## 1. Introduction

The well-functioning of supply chains (SC) depends on the balance of demand and supply between its entities. A disruptive mismatch of demand and supply can trigger a persistent SC disruption which might lead to an unavailability of supplies for the affected downstream entities (Knemeyer et al. 2009). In a society, such an unavailability is in particular crucial under two conditions: firstly, when the end customers are affected and secondly when the SC is part of the critical infrastructure (CI) sectors food, water, health care or energy (Schätter et al. 2015). The past has shown that disasters in particular led to an unavailability of critical supplies in developing and industrial nations. Humanitarian aid was required to compensate for unavailable food supplies in the Maldives after a tsunami in Southeast Asia in 2004 (Samii & Van Wassenhove 2010). In 2005, Hurricane Katrina destroyed 170 drinking water facilities causing severe disturbances of water supplies in New Orleans, USA (The White House 2006). At the same time, disaster-caused CI disturbances have occurred more often in recent years (Kleindorfer & Saad 2005; Guha-Sapir et al. 2016).

The consequence of an SC disruption within an affected company is the nonfunctioning of one or more of its business processes. It is the companies’ major objective to quickly re-establish these processes or to replace them by adequate compensation measures. The scope of this article is on disastercaused disruptions triggering failures of critical supplies for end customers as the final stage of the SC.

Therefore, we focus on logistical decision problems of resource allocation with the objective of securing the critical supplies provision to people. From the companies’ perspective, such a public responsibility does not stand in contrast to their generic business objective of profit maximization: by ensuring that supplies are available, a company can maximize its revenue and profit.

Most research regarding logistical decision-making for critical supplies can be found in the field of humanitarian logistics which is predominantly dealing with the support of the affected population. Hence, the focus is on external decision makers such as representatives of governments, military, or non-governmental organizations which intervene to compensate for unavailable supplies (Van Wassenhove 2012). A large number of articles in this field underlines the momentum it has gained (Hoyos et al. 2015). Compared to the research intensity in the area of public crisis management, there is a significant lack of comparable approaches for the commercial domain which could support a disaster-affected company in dealing with logistical decision problems. This aspect is not necessarily unrelated to the effectiveness of humanitarian operations because companies can take over responsibility in an indirect way: if private SCs can provide the needed supply in a timely manner during or immediately after a crisis, humanitarian organizations can focus on the most vulnerable parts of the population in a more effective manner (Natarajarathinam et al. 2009; Galindo & Batta 2013).

However, there is a lack of research dealing with the possibility that the affected companies can handle the disaster’s consequences themselves in a context of severe uncertainty and complexity. The literature on business continuity management (BCM) is still overly restricted to IT operations and internal process management because these internal issues are easier to tackle for firms (e.g. Sahebjamnia et al. 2015). Consequently, this leaves them unprepared and exposed to the adverse consequences of large scale disasters. We address this lack by shifting the focus from humanitarian logistics to BCM of companies. When operating in a disaster-affected environment, companies face similar challenges as humanitarian aid organizations: time pressure, severe uncertainty of information and dynamic changes

# ACCEPTED MANUSCRIPT

within the environment and of incoming information over time (e.g. secondary disasters, socioeconomic dynamics). Under such conditions, it is essential that decisions are robust in terms of performing adequately under various uncertain states of the underlying environment. It follows that there is a high necessity for the BCM decision makers to learn the lessons from crisis management and to receive assistance in terms of a tailored decision support before and during a crisis.

Decision support systems (DSS) can help to structure information while reducing the uncertainty of a decision situation (Sojda 2007). Furthermore, they make the decision process more productive and agile (Holsapple 2008). To leverage these characteristics in the context of BCM for disaster management, we present a novel decision support methodology to operationalize BCM within a company. The methodology is the core part of the Reactive Disaster and supply chain Risk decision Support System (ReDRiSS). The objective of this article is to present the methodology, to discuss its foundations and to illustrate its practical application in a disaster-caused BCM decision situation. As we explicitly focus on the methodology and its application, the underlying IT environment to use ReDRiSS is just marginally addressed and an extensive presentation of its architecture is not within the scope of this article. In section 2, the foundations of our research are provided by discussing relevant literature on disaster management, DSSs, BCM and decision theory. Furthermore, the requirements decision support in disaster-caused BCM should meet are elaborated and described briefly. The generic methodology of ReDRiSS is outlined in section 3. Section 4 presents a case study where the methodology is applied to model the reactions of a food retail company in Berlin that is affected by a pandemic-caused staff absence. The findings of our research and directions for future research are discussed in section 5.

## 2. Foundations and literature

## 2.1 Disaster management

Disasters are described as large-scale hazardous events (Kovács & Tatham 2009) and the management of disasters can be split into four different phases: mitigation, preparedness, response, and recovery (Altay & Green 2006). Logistical disaster management frequently uses approaches from operations

## ACCEPTED MANUSCRIPT

research (OR) and management sciences (MS). Methods refer to analytical techniques such as mathematical programming, simulation, and statistics and to related areas like decision theory, system dynamics, multi-criteria decision-making and expert systems. The interface of OR & MS and disaster management is called disaster operations management (DOM) (Altay & Green 2006) and can be defined as the sequence of operations to prevent or to reduce negative consequences resulting from a disaster (Hoyos et al. 2015). It addresses problems in humanitarian logistics which have to be solved by external decision makers such as representatives of governments, military or non-governmental organizations (Van Wassenhove 2012), but also applies in the BCM context where internal decision makers reside within the focal company. During disaster response, the support of the affected companies’ processes is not among the first priorities of humanitarian aid organizations. Humanitarian aid is directly aimed at people and rightly so. However, significant undersupply of the population with essential resources in the wake of disasters results from collapsed business processes. Hence, it is crucial to view BCM as an additional means to mitigate the disruptive effects of disasters on SCs. This can be done by speeding up the recovery of business operations after disasters using BCM.

Although DOM can be used to address both humanitarian logistics and BCM tasks, there seems to be an imbalance in research and its literature between these two fields. In an extensive review, Altay & Green (2006) analyzed 109 peer-reviewed research articles from the domain of DOM. As a result, they hint at the increasing need for studying OR/MS issues in logistical disaster management and state that BCM in a disaster management context is neglected by academics. They report on less than a handful of articles that focus on BCM. Two technical applications of BCM in computer science (Ambs et al. 2000, Artalejo & Gomez-Corral 1999) are mentioned in addition to Bryson et al. (2002) who discuss disaster recovery alternatives of organizational crisis management in general. In their continuation of Altay & Green’s work, Galindo & Batta (2013) review 155 papers of OR/MS research in DOM and find that since 2005 “there were virtually no articles related to business continuity”. We add Sahebjamnia et al. (2015) to this exclusive list, who develop a BCM framework for disaster recovery

# ACCEPTED MANUSCRIPT

that includes all strategic, tactical, and operational decision levels with different time frames, and various elements at each level. Apart from that, literature on the topic remains scarce. Galindo & Batta (2013) furthermore state that, in regard to disruptions, researchers in BCM seem more interested in helping a general population than businesses. We aim to emphasize that these objectives are not mutually exclusive, that by helping businesses during disasters, one helps the population as well.

Both reviews found that research strongly concentrates on external decision makers. They recommend that future research should strengthen the focus on internal decision makers and BCM by considering company-level post-disaster logistical decision problems and on tools for taking theoretical and analytical research into practice. Galindo & Batta (2013) also highlight the need to support decision-making in quick and efficient ways by intensifying research on DSS, focusing on the immediate post-disaster phase. We address this need by proposing a decision support methodology that aims at the continuation of business processes and operations (BCM) right after a disaster occurrence (response phase).

## 2.2 Decision support systems

The field of DSS aims to improve and support managerial decision-making (Arnott & Pervan 2008). As disaster situations are affected by uncertainty (Day et al. 2012), they are difficult to assess for managers (Vahidov & Kersten 2004). A DSS can be defined as a computer-based system that supports decision makers in solving a decision problem (Shim et al. 2002) and allows them to make decisions more efficiently and agile (Holsapple 2008). Er (1988) states that the aim of a DSS is to support decision makers, not replace them, while Mattiussi (2012) points out that interaction of the DSS with the decision makers is an important factor for success. The usage of a DSS aims at obtaining a good solution in a reduced amount of time. There are many potential applications of DSS in disaster management as they help structure complex decision-making environments (Thompson et al. 2006) and attempt to reduce uncertainty of the decision situation (Sojda 2007). Frameworks of DSSs in disaster management have been developed early (e.g. Wallace and De Balogh 1985). An adequate DSS to aid decision makers employing BCM could speed up the recovery of business operations after disasters. However, the integration of BCM into DSS for disaster management has been lacking, both in research and practice. Our research aims at addressing this gap by focusing on BCM that becomes necessary due to a disaster.

## 2.3 Business continuity management

BCM refers to a set of principles, policies and tools to support organizations in keeping their critical business processes functioning when disruptive events occur (Peck 2006). Unlike common risk management units, the focus of BCM departments is typically on disruptive events that are characterized by high impact and low probability, leaving decision makers with a very short reaction timeframe (Zsidisin et al. 2005). When the disruption refers to a disaster, decision problems must be solved under uncertain information which might change over time in a highly dynamic environment. Regarding SCs, BCM can be understood as a cross-divisional function that bridges the gap between measures of preventive supply chain risk management (SCRM) and reactive supply chain crisis management (SCCM) (Boerse 2014), see Figure 1. This link is documented by the standard ISO 22301. BCM is described as a SCRM process that coordinates the identification and minimization of risks that might impact critical business processes. The standard defines BCM as a process that provides an action framework to withstand a disruption of the critical business processes via reactive SCCM (von Rössing 2005).

A framework to address BCM within an organization is provided through the BCM lifecycle which comprises six professional practices (PP) (BCI 2013). The first two refer to management tasks and follow the objective of disseminating BCM within the organization: the development of a policy and program management (PP 1) and its embedding into the organization’s everyday business activities and organizational culture (PP 2). The remaining practices are technical tasks which aim at developing a BCM strategy and a business continuity plan. Objectives and constraints are analyzed by business impact analyses, continuity requirements analyses and/or risk analyses (PP 3). They provide the basis to develop a BCM strategy which states how recovery from a disruption of critical business processes could be achieved (PP 4). The BCM strategy is implemented using a business continuity plan that prescribes how to manage the disruption (PP 5). To establish a permanent and effective BCM within the organization, results of the technical practices must be continuously validated (PP 6). The objective of our research is to operationalize the BCM lifecycle for disaster-caused decision-making within companies regarding logistical decision problems of resource allocation.

![](/api/attachments/MSB9RPB2/fulltext/images/15dacc15a50a704c2379d1b8b192531a3191f36b3917ea5ce077260db7369e8c.jpg)  
Figure 1: BCM and SCM (adapted from Lauwe 2007)

## 2.4 Decision situation, decision-making and requirements of the decision support methodology

The settings addressed in this article deal with an uncertain and dynamic disaster environment which in turn makes the operating environment uncertain and dynamic as well (Day et al. 2012). A disturbance of normal supply and demand behavior (van Wassenhove 2006) is, thus, to be expected. In general, the type of decision situation depends on the availability of information which might arise under certainty, risk, or ignorance (Knight 1921). Certainty assumes that all relevant aspects of the decision situation are known. Decision situations under risk is characterized by complete knowledge of the statistical distribution over the possible but uncertain outcomes of a decision alternative (Zimmermann 2000). In decision situations under ignorance, probability distributions cannot be used as just the set of possible outcomes of an alternative is known (Rommelfanger & Eickemeier 2002, Wiens 2013).

# ACCEPTED MANUSCRIPT

We follow the view widely held in literature that a disaster-affected environment corresponds to a decision situation under ignorance (e.g. de la Torre et al. 2012) and a state of ignorance is associated with lacking knowledge about the consequences of a disaster (Liberatore et al. 2013). This can refer to missing information regarding demand or supply side behavior within a critical SC. Moreover, due to the dynamic characteristic of a disaster (e.g. possible secondary disasters, impact of the disaster on the environment is hard or impossible to verify within a short time), the decision situation can in addition also exhibit elements of complexity. Complexity refers to the state of a system that is difficult to predict (Hollnagel 2012) or even unpredictable (Snowden & Boone 2007). Additionally, complex systems are characterized by irreducible uncertainty and non-linear interactions (Snowden & Boone 2007). In a complex decision situation, many alternatives may exist, predictability is limited, and it is difficult to precisely determine all outcomes of a decision recommendation (Grisogono 2006). Hence, there might not be a “global optimum” state of the system, but decision-making must rather choose between different alternatives leading to “local optima” states (Helbing & Lämmer 2008).

In an uncertain situation where optimality cannot be achieved for sure, alternative concepts that are able to evaluate a decision recommendation have to replace it. In OR literature, robustness is identified as such a concept. A robust solution of a decision problem performs well across all possible outcomes of a decision situation instead of being the best solution in just one outcome (Bertsimas & Sim 2004). While there are different specifications of robustness, it is in general considered to be a way of dealing with ignorance in a decision situation (Snyder 2006). When suggesting a recommendation for a decision, the expertise and experience as well as the preferences of the decision makers should be considered as well. In a decision situation that is subject to ignorance and complexity, methods have to be applied that can handle the related uncertainty and unpredictability. This is the first requirement a decision support methodology for a reactive disaster-caused BCM must meet. Moreover, for general applicability in BCM, the DSS should be generic, allowing for the use in various decision situations and being able to respect multiple objectives at the same time, since decision situations can have more

# ACCEPTED MANUSCRIPT

than one dimension. The re-establishment of supplies, which is a part of BCM, implies the need of solving logistical decision problems of resource allocation (e.g. facility location and transportation planning), pathing (e.g. shortest path), but also types of problems not only prevalent in logistics, like sequencing (processes). Therefore, as another requirement, OR/MS approaches should be leveraged by the DSS to ensure a high level of analytical accuracy. It should also take the risk preferences of the decision makers into account and be transparent and understandable to facilitate its application and acceptance by practitioners. Lastly, the decision support should provide recommendations according to the principle of robustness. An overview of all requirements is given in Table 1.

<table><tr><td colspan="2">Requirement of a decision support methodology for a reactive disaster-caused BCM</td></tr><tr><td>#1</td><td>Decision support under ignorance and complexity</td></tr><tr><td>#2</td><td>Generic nature</td></tr><tr><td>#3</td><td>Ability to cover multiple objectives</td></tr><tr><td>#4</td><td>High level of analytical accuracy</td></tr><tr><td>#5</td><td>Integration of risk preferences of decision makers</td></tr><tr><td>#6</td><td>Transparency and comprehensibility</td></tr><tr><td>#7</td><td>Robust decision recommendation</td></tr></table>

Table 1: Requirements

## 3. The generic methodology of the decision support system ReDRiSS

ReDRiSS is a BCM DSS that considers uncertainty and the dynamics of a disaster-affected environment. It can be integrated into the IT infrastructure of companies to facilitate near real time decision support and to prepare the company for sudden or fast onset disasters in which the impact is uncertain. In the following paragraphs, the methodology of ReDRiSS is presented.

## 3.1 Methodology

The procedural model of the ReDRiSS methodology consists of three parts: (i) implementation, (ii) two-stage scenario construction and (iii) robustness measurement which comprise seven tasks (1-7), see Figure 2. Phase (i) takes place pre-disaster as a measure of SCRM, (ii) and (iii) deal with the reactive application in the immediate aftermath as a measure of SCCM. ReDRiSS can be integrated into the BCM lifecycle of an organization. Based on an embedded BCM policy and program (PP 1 & 2), the most critical business processes and corresponding risks must be identified and analyzed (PP 3). Next, implementation is started to prepare the decision makers for a disruptive event which calls for action (PP 4). Thus, ReDRiSS is established as a system pre-disaster for decision support to develop of the tool can be continuously tested and trained (PP 6).

![](/api/attachments/MSB9RPB2/fulltext/images/21f703a7d7ea96b05776e58f06accb887d5291c744c32eab434ea1a2c5977c43.jpg)  
Figure 2: Procedural model of the ReDRiSS methodology

## 3.1.1 Implementation

Task 1 - Optimization model: The methodology is based on the rationale of scenario-based optimization which allows for analytically solving logistical decision problems by exploring the effects of different states of the environment (Comes 2011). Scenario-based approaches are considered an appropriate measure for a decision situation under ignorance (Bunn & Salo 1993, Comes 2011). The specific approach chosen in this research is described in the following paragraphs.

Suppose for example a routing problem where the decision makers have to decide about food transportation routes via trucks to various demand hubs. Let $a = \left( x _ { 1 } , \dots , x _ { J } \right) \in \Omega$ be a vector of ?? decision variables where Ω is the decision space, $f ( a ) = \{ f _ { 1 } ( a ) , \ldots , f _ { F } ( a ) \}$ a set of $F \in \mathbb { Z }$ objective functions, and $g ( a ) = \left\{ g _ { 1 } ( a ) , \ldots , g _ { G } ( a ) \right\}$ a set of $G \in \mathbb { Z }$ constraint functions. The objective is to minimize transportation costs subject to road availability conditions due to a disaster. Alternatives then refer to different transportation routes that can be selected. In general, an alternative ?? of the decision space Ω

# ACCEPTED MANUSCRIPT

refers to a decision option within the logistical decision problem; ?? is given by the discrete specifications of all decision variables $x _ { j } \in \{ x _ { 1 } , \ldots , x _ { J } \}$ . The decision problem is characterized by a set of context-specific parameters (e.g. demand, transportation times). Accordingly, the formulations of ??(??) and $g ( a )$ integrate parameters of the set $P a r = \{ p a r _ { 1 } , \ldots , p a r _ { p } , \ldots , p a r _ { P } \}$ . This set describes the decision environment as comprising all elements of the environment that must be respected when solving the logistical decision problem via the optimization model. A scenario includes exactly one specification per $p a r _ { p } \in P a r$ regarding a single scenario ?? out of the overall set of scenarios ??. The optimization model exemplarily shows the formulation of a minimization problem (maximization problems are treated analogically). Furthermore, it refers to a single objective optimization model when ?? = 1 and to a multi-objective optimization model when $F \geq 2$ (Zitzler 1999).

$$
\begin{array}{r l} & {\min _ {a} f (a, s) = \left(f _ {1} (a, s), \ldots , f _ {F} (a, s)\right)} \\ & {\mathrm{subjectto} g (a, s) = \left(g _ {1} (a, s), \ldots , g _ {G} (a, s)\right) \leq 0} \\ & {\qquad a = \left(x _ {1}, \ldots , x _ {J}\right) \in \Omega , s \in S} \end{array}\tag{1}
$$

Task 2 – Parameter classification and calibration: Scenarios aim at describing all states of the disaster-affected decision environment, ranging from probable to highly unlikely but possible states (Hites 2006). Their construction requires the development of different specifications of the parameters of ??????. We distinguish if these specifications are under the control of the decision makers (e.g. budget) or if they explicitly depend on the consequences of the disaster (e.g. failures of infrastructure). Accordingly, parameters are classified using planning variables $P V \subseteq P a r$ and environmental variables $E V \subseteq$ ??????. Specifications of each EV might be unknown in the post-disaster phase due to a lack of (environmental) information; the specification of each PV is assumed to be deterministic as (planning) information can be directly captured from the decision makers. Note that $( E V \cup P V ) = P a r$ . Constructed scenarios vary in the specifications of EV; specifications of PV are the same across all scenarios.

In preparation of the reactive scenario construction in (ii), it is important to develop a specification process per EV because information might be sparse or lacking in the immediate aftermath of a disaster. It might be impossible to specify (some) EV by deterministic values. Therefore, specification processes are needed to develop a range of possible values. Furthermore, to account for dynamic developments that are highly unlikely but possible, the decision makers should preventively foresee potential critical consequences of the disaster and re-specify the set of EV accordingly. For the sake of clarity, the rationales of the specification and re-specification processes are explained in the following section and are illustrated in the case study in section 4.

## 3.1.2 Two-stage scenario construction

Task 3 - Prognostic scenarios: The objective of prognostic scenarios is to describe probable and expected states of the decision environment. Therefore, uncertain EV, whose specifications cannot be defined deterministically due to insufficient information in the post-disaster phase, must be identified. This requires analyzing the information state of each EV. It is distinguished between the information states ‘available’ and ‘unavailable’. When its information state is ‘available’, the question arises whether this information is ‘complete’ or ‘incomplete’. ‘Complete’ indicates the EV can be specified in a deterministic manner. An ‘incomplete’ information state suggests several deterministic aspects of this specification (e.g. entries of several matrix cells of an EV). An EV is uncertain if its information state is unavailable or incomplete. For these EV, the specification processes of the implementation part (task 2) must be activated and conducted. Specification of a variable can be achieved by combining databases, statistical distributions and/or simulations (e.g. Monte Carlo).

The set of prognostic scenarios ??<sup>????????</sup> is constructed by combining each specification per uncertain EV with the constant specifications of the deterministic EV and PV. Let $P V = \{ p v _ { 1 } , \ldots , p v _ { m } , \ldots , p v _ { M } \}$ be the set of planning variables, $E V ^ { d e t } = \{ e v _ { 1 } ^ { d e t } , \dots , e v _ { d } ^ { d e t } , \dots , e v _ { D } ^ { d e t } \} \subseteq E V$ the set of deterministic environmental variables, and $E V ^ { u n c } = \{ e v _ { 1 } ^ { u n c } , \ldots , e v _ { u } ^ { u n c } , \ldots , e v _ { U } ^ { u n c } \} \subseteq E V$ the set of uncertain environmental variables. Note that $( E V ^ { d e t } \cup E V ^ { u n c } ) = E V . S ^ { p r o g }$ is defined by the Cartesian product:

$$
\begin{array}{r l} & S ^ {p r o g} = \left(V (e v _ {1} ^ {u n c}) \times \ldots \times V (e v _ {u} ^ {u n c}) \ldots \times V (e v _ {U} ^ {u n c})\right) \cup \\ & \qquad \left\{V \big (e v _ {d} ^ {d e t} \big) | d = 1, \ldots , D \right\} \cup \{V (p v _ {m}) | m = 1, \ldots , M \} \end{array}\tag{2}
$$

where $V ( e v _ { u } ^ { u n c } ) = \left\{ v _ { 1 } ( e v _ { u } ^ { u n c } ) , \ldots , v _ { n _ { u } } ( e v _ { u } ^ { u n c } ) , \ldots , v _ { N _ { u } } ( e v _ { u } ^ { u n c } ) \right\}$ is the set of $N _ { u }$ specifications of $e v _ { u } ^ { u n c } \in E V ^ { u n c }$ developed by applying specification processes, and $V \big ( e v _ { d } ^ { d e t } \big ) = \big \{ v _ { 1 } \big ( e v _ { d } ^ { d e t } \big ) \big \}$ and $V ( p v _ { m } ) = \{ v _ { 1 } ( p v _ { m } ) \}$ refer to the constant specification per $p v _ { m } \in P V$ and $e v _ { d } ^ { d e t } \in E V ^ { d e t }$ . The $l ^ { t h }$ set in $S ^ { p r o g }$ is denoted prognostic scenario $s _ { l } ^ { p r o g } \in S ^ { p r o g }$ . The number of prognostic scenarios ?? is:

$$
L = | V (e v _ {1} ^ {u n c}) | \cdot \ldots \cdot | V (e v _ {u} ^ {u n c}) | \cdot \ldots \cdot | V (e v _ {U} ^ {u n c}) | = \prod_ {u = 1} ^ {U} N _ {u}\tag{3}
$$

Task 4 - Generation of alternatives: The set $S ^ { p r o g }$ is used to formulate a number of ?? optimization sub-models (introduced in task 1) according to their ?? scenario-specific parametrizations. They are each solved deterministically to generate alternatives as solution candidates for the logistical decision problem. Either exact solvers or heuristics can be used to compute an alternative per optimization submodel. The aggregated set of alternatives ?? across $S ^ { p r o g }$ is:

$$
A = A \big (s _ {1} ^ {p r o g} \big) \cup \ldots \cup A \big (s _ {l} ^ {p r o g} \big) \cup \ldots \cup A \big (s _ {L} ^ {p r o g} \big) = \{a _ {1}, \ldots , a _ {z}, \ldots , a _ {Z} \}\tag{4}
$$

Task 5 - Hypothetical scenarios: Hypothetical scenarios represent potential dynamic developments in the environment over time and aim at covering complexity. They describe possible but highly unlikely states of the decision environment. Unlike prognostic scenarios, the construction of hypothetical scenarios is not necessarily linked to information captured from the environment. Optimization sub-models that are formulated based on the hypothetical scenarios are explicitly used to test the generated alternatives (task 4) in states that unfold toward vulnerable states or states of failure within the third part of the ReDRiSS methodology (see section 3.1.3). The construction of hypothetical scenarios is similar to stress-testing and implies the modification of the state of the decision environment assumed by a prognostic scenario. Therefore, a critical event is simulated that triggers a dynamic development within the state of the decision environment over time (e.g. shifts in population demands, secondary disasters such as earthquake aftershocks). Different environmental variables might be affected. Hence, the re-specification process per affected environmental variable and critical event (task 2) must be activated. This doesn’t necessarily impact all elements of an affected environmental variable (e.g. it might just re-specify several matrix cells of an environmental variable).

Let ?? be a critical event and $E V _ { k } ^ { c r i t } = \{ e v _ { k , 1 } ^ { c r i t } , \ldots , e v _ { k , t } ^ { c r i t } , \ldots , e v _ { k , T } ^ { c r i t } \} \subseteq E V$ the set of ?? environmental variables that must be modified due to ??. A hypothetical scenario refers to event ?? and one prognostic scenario $s _ { l } ^ { p r o g } \in S ^ { p r o g }$ . Let $V _ { l } \big ( e v _ { k , t } ^ { c r i t } \big ) = \big \{ v _ { 1 } \big ( e v _ { k , t } ^ { c r i t } \big ) \big \}$ be the re-specification of $e v _ { k , t } ^ { c r i t } \in E V _ { k } ^ { c r i t }$ in $s _ { l } ^ { p r o g }$ . Hypothetical scenario $s _ { l , k } ^ { h y p } \in S ^ { h y p }$ simulates a dynamic development within $s _ { l } ^ { p r o g }$ by integrating the re-specification $V _ { l } \big ( e v _ { k , t } \big )$ of each $e v _ { k , t } ^ { c r i t } \in E V _ { k } ^ { c r i t } ;$

$$
\begin{array}{r l} & s _ {l, k} ^ {h y p} = \Big (s _ {l} ^ {p r o g} \backslash \Big \{v _ {n _ {i}} (e v _ {i}) | \forall e v _ {i} \in E V \cap E V _ {k} ^ {c r i t}, i \in \{1, \dots , | E V | \}, n _ {i} \in \{1, \dots , N _ {i} \} \Big \} \Big) \\ & \qquad \cup \big \{V _ {l} \big (e v _ {k, t} ^ {c r i t} \big) | t = 1, \dots , T \big \} \end{array}\tag{5}
$$

## 3.1.3 Robustness measurement

Task 6 - Regret test: Robustness measurement is based on a regret test of generated alternatives across the constructed prognostic and hypothetical scenarios. The regret of an alternative in a scenario is defined as the absolute or relative deviation of an alternatives’ outcome in a scenario from the best outcome reached by any other alternative in this scenario (Scholl 2001, Gabrel & Murat 2010). To make outcomes of alternatives comparable across scenarios, the normalized regret $r _ { i } ( a , s )$ of an alternative $a \in A$ in a scenario $s \in S$ regarding objective ?? (by assuming linear normalization) is used:

$$
r _ {i} (a, s) = \frac {f _ {i} (a , s) - f _ {i} ^ {m i n} (A , s)}{f _ {i} ^ {m a x} (A , s) - f _ {i} ^ {m i n} (A , s)}\tag{6}
$$

Here $f _ { i } ( a , s )$ is the outcome of ?? when it is applied in ??, and $f _ { i } ^ { m i n } ( A , s )$ and $f _ { i } ^ { m a x } ( A , s )$ are the minimal (optimal) and maximal outcomes in ?? that are achieved by any alternative of ??. An alternative is denoted “totally robust” when it is the generic best alternative in any scenario. In fact, ?? is totally robust in ?? and regarding objective ?? if $f _ { i } ^ { m i n } ( A , s ) = f _ { i } ( a , s ) \mathrm { a s } r _ { i } ( a , s ) = 0$ . A totally robust alternative rarely exists when multiple objectives are considered, as many real-world decision problems do. Robust decision-making therefore focusses on alternatives whose regret values are acceptable across scenarios and objectives (Scholl 2001). In the case that the optimization model respects multiple objectives $( i > 1 )$ , an objective weight $w _ { i } \in [ 0 , 1 ]$ must be defined where $\begin{array} { r } { \sum _ { i } w _ { i } = 1 } \end{array}$ . The aggregated normalized regret is then:

$$
r (a, s) = \sum_ {i} w _ {i} \cdot r _ {i} (a, s)\tag{7}
$$

As a result, a set of aggregated normalized regret values is calculated per alternative and scenario category (prognostic scenarios, hypothetical scenarios). There are no occurrence probabilities of scenarios assumed following the Laplace-principle of insufficient reason. To compare the robustness implied by these values, the expected aggregated normalized regret (8) and maximal aggregated normalized regret (9) provide the basis for robustness measurement.

$$
R E (a, S) = \frac {1}{| S |} \sum_ {\forall s} r (a, s)\tag{8}
$$

$$
R M (a, S) = \max _ {\forall s} \bigl (r (a, s) \bigr)\tag{9}
$$

Task 7 - Integration of risk preferences: It is assumed that risk avoidance is the standard attitude of decision makers because critical SC disturbances can heavily affect the objectives of their organizations. Considering risk preferences in the context of ignorance and incomplete information is a tricky task because the lack of probability distributions makes it impossible to use canonical measures of risk aversion such as the Arrow-Pratt coefficients. Instead, we revert to the decision maker’s degree of pessimism, in accordance with basic decision rules under strong uncertainty, which can be interpreted as the limit of extreme ambiguity aversion (Ellsberg 1961; Gilboa & Schmeidler 1989). Two aspects must be respected: the inter- and intra-scenario degrees of pessimism which determine whether decision makers operate in a neutral or pessimistic manner. The possibility that decision makers operate in

# ACCEPTED MANUSCRIPT

an optimistic manner is excluded as it is unrealistic in BCM. Neutral decision makers would rather aim at measuring the robustness of an alternative based on the set of prognostic scenarios, regarding interscenario pessimism. In turn, pessimistic decision makers might be interested in hedging against critical and highly unlikely dynamic developments of the decision environment specified by hypothetical scenarios.

The inter-scenario degree of pessimism refers to a relative weight of each scenario category, $w e ^ { p r o g } , w e ^ { h y p } \in [ 0 , 1 ]$ , where ???? $p r o g + w e ^ { h y p } = 1$ . Regarding intra-scenario pessimism, neutral decision makers understand an alternative as robust if it achieves a small aggregated regret in any scenario of a considered scenario category. Pessimistic decision makers aim at hedging against that single scenario in which an alternative performs worst and achieves the highest aggregated regret. The intrascenario degree of pessimism is respected through a procedure that is inspired by decision theory in terms of the Hodges-Lehmann criterion. It suggests combining the $\mu$ criterion and the minimax criterion. The reliability parameter $\lambda \in [ 0 , 1 ]$ reflects the relative importance of the expected value of the considered set of outcomes $( \mu$ criterion) compared to the worst value of this set (minimax criterion) (Rommelfanger & Eickemeier 2002; Wiens 2013).

The ReDRiSS methodology adapts the rationale of the Hodges-Lehmann criterion to integrate the per scenario category, $\lambda ^ { p r o g } , \lambda ^ { h y p } \in [ 0 , 1 ]$ , is defined. Neutral decision makers totally trust in the quality of the set of aggregated regret values and follow the expected value of this set $( \lambda ^ { p r o g } , \lambda ^ { h y p }  1 )$ . Pessimistic decision makers do not trust in the quality of the set aggregated regret values and follow the maximal value of this set $( \lambda ^ { p r o g } , \lambda ^ { h y p } \to 0 )$ . Hence, the intra-scenario degree of pessimism is respected by calculating the criteria $\phi ^ { p r o g } ( \tilde { a } _ { b } ) , \phi ^ { h y p } ( a ) , \forall \tilde { a } _ { b } \in \tilde { A }$

$$
\phi^ {p r o g} (a) = \lambda^ {p r o g} \cdot R E (a, S ^ {p r o g}) + (1 - \lambda^ {p r o g}) \cdot R M (a, S ^ {p r o g})\tag{11}
$$

$$
\phi^ {h y p} (a) = \lambda^ {h y p} \cdot R E (a, S ^ {h y p}) + (1 - \lambda^ {h y p}) \cdot R M (a, S ^ {h y p})\tag{12}
$$

Subsequently, a robustness value $R V ( \widetilde { a } _ { b } )$ is calculated per $\tilde { a } _ { b } \in \tilde { A } \colon$

$$
R V (\tilde {a} _ {b}) = w e ^ {p r o g} \cdot \phi^ {p r o g} (a) + w e ^ {h y p} \cdot \phi^ {h y p} (a)\tag{13}
$$

The result is a set of robustness values $\{ R V ( a ) | \forall a \in A \}$ . Finally, a robust alternative ??̃ is provided as decision recommendation to the decision makers. This alternative represents the optimal decision option as it achieves the minimal value in the set ????:

$$
\tilde {a} = \Big (a \in A \colon R V (a) = \min _ {\forall a} (\{R V (a) \}) \Big)\tag{14}
$$

## 3.2 Addressing the requirements

The presented methodology addresses all previously derived requirements for the DSS. The generic nature and applicability in BCM are accounted for by integrating the ReDRiSS methodology into the BCM lifecycle. By setting up an optimization model during the implementation phase and by consulting the decision makers on parameter classification and calibration, a high level of analytical accuracy is ensured. The model can be set up in a way that allows for either single or multiple objective functions. In order to be able to handle the uncertainty of a disaster setting, a scenario-based approach is chosen. To address complexity, a second stage within the scenario construction process is established. It introduces hypothetical scenarios that re-evaluate decision recommendations which are made based on just prognostic scenarios. These hypothetical scenarios simulate dynamic changes in the environment that are characteristic for a complex system. During robustness measurement, the concept of regret values is introduced. Alternatives are evaluated based on their regret values in all scenarios, prognostic and hypothetical. The outcome is combined with risk preferences of decision makers to yield a robustness value for each alternative. Decision makers take on an active role during the implementation phase by helping to set up the optimization model and by classifying and calibrating model parameter values (e.g. PV). Thus, transparency and understandability are promoted, increasing the likelihood of acceptance by practitioners. Table 2 provides an overview of approaches chosen to address the requirements summarized in Table 1, section 2.4.

<table><tr><td colspan="2">Approaches to develop a decision support methodology for a reactive disaster-caused BCM</td></tr><tr><td>#1</td><td>Scenario-based approach &amp; hypothetical scenarios</td></tr><tr><td>#2</td><td>Integration into the BCM lifecycle</td></tr><tr><td>#3</td><td>Multi-objective target function in optimization model</td></tr><tr><td>#4</td><td>Optimization model using input from decision makers on parameters</td></tr><tr><td>#5</td><td>Integration of inter- and intra-scenario degree of pessimism</td></tr><tr><td>#6</td><td>Active role of decision makers during implementation and application</td></tr><tr><td>#7</td><td>Robustness measurement that combines scenario simulation results with risk preferences</td></tr></table>

Table 2: Approaches selected to address the requirements

## 4. Case study: business continuity management in the food sector

In the following, we present a case study were the methodology is applied to support a food retail company (FRC) during a pandemic disaster. The implementation of the generic functioning of Re-DRiSS was translated into Python and executed on a Lenovo ThinkPad Edge E531 Laptop with a 2.6 GHz Dual-Core Processor and 4 GB RAM using Windows 8 as OS. Both input and output files were Excel-files. Given 100 scenarios, the calculation time – comprising scenario construction and optimization, regret value calculation and robustness measurement – amounted to roughly 2 hours.

## 4.1 General description of the decision situation

An FRC owns 29 stores in the city of Berlin and is faced with a staff absence caused by a pandemic disaster. Food retail stores can be classified by the size of their sales area into consumer markets (500- 4999 m<sup>2</sup>) and self-service warehouses (5000-7000 m<sup>2</sup>) (Kotzab & Teller 2005). Activities staff members must conduct to operate a store, such as activities at the checkout area, filling up of shelves, or customer advisory services, are considered critical business processes of the FRC. By following the technical practices of the BCM lifecycle post-disaster, large-scale staff absences (e.g. pandemics) have been identified as a major risk to the critical business processes. When a disease-caused staff absence occurs, the FRC is forced to operate its stores with a reduced number of staff members which can seriously affect business operations. The situation is aggravated by an increased demand risk due to the uncertain behavior of diseased customers which is reflected by fluctuations in their food demands. Hence, the FRC develops a BCM strategy that prescribes preventively establishing ReDRiSS to receive analytical decision support in case of a disease-caused staff absence. The goal is to provide a decision recommendation for crisis operation in form of a robust allocation of the available staff members to the stores while respecting uncertain customer food demands.

## 4.2 Implementation

Task 1 - Optimization model: The major objective of the FRC is profit maximization. It is assumed that average operational costs of stores are constant under normal and crisis conditions. Accordingly, the FRC aims at maximizing throughput while taking the reduced number of staff members into account. The profit [€] that can be achieved by the FRC per day depends on the aggregated revenue [€] in all stores. This revenue depends on the throughput of the store [kg] ieved by staff members and the share of this throughput which is turned over by the cust It is assumed that the achieved throughput of a store increases linearly with the number of staff members.

Let $J = \{ 1 , 2 , \dots \}$ be the set of customers that is served by the set of stores $I = \{ 1 , 2 , \dots \}$ . The food demand of customer $j \in J$ is denoted $b _ { j \cdot } \mathbf { A }$ number of staff members ?? is available and must be allocated to the stores. The achieved throughput of a store $i \in I$ depends on its number of staff $t _ { i }$ (decision variable). The additional throughput per staff member is indicated by the constant factor ??. An opened store ?? must employ a minimum number of staff members $l _ { i } .$ . Moreover, let $u _ { i }$ be the maximum number of staff members for $i .$ The employed number of staff members $t _ { i }$ in an opened store must be between $l _ { i }$ and $u _ { i }$ . Let $d _ { i j }$ be the purchasing distance (linear distance between the customer and its next store) between ?? and ??. The binary decision variable $x _ { i }$ indicates whether store ?? is opened $( x _ { i } = 1 )$ or closed $( x _ { i } = 0 )$ which depends on the realization of $t _ { i }$ . Let $\begin{array} { r } { B _ { t o t a l } = \sum _ { j } b _ { j } } \end{array}$ be the overall customer food demand that can be satisfied by the stores during normal operation given $u _ { i }$ staff members in each store ??. The staff absence leads to the unsatisfied customer food demand $B ^ { - } = B _ { t o t a l } - \gamma \cdot m$ . Each $b _ { j } , j \in J$ can be satisfied by exactly one store. The binary decision variable $y _ { i j }$ indicates whether ?? is served by store $i ( y _ { i j } = 1 )$ ) or not $( y _ { i j } = 0 )$ . Equations (17) to (25) formulate the optimization model. A discussion of the objective function (17) and the constraint functions (18) to (25) follows.

$$
\min z = \sum_ {i} \sum_ {j} y _ {i j} \cdot d _ {i j}\tag{17}
$$

subject to

$$
\sum_ {i} t _ {i} = m
$$

$$
\forall i > 0\tag{18}
$$

$$
\sum_ {i} y _ {i j} = 1
$$

$$
\forall i, j\tag{19}
$$

$$
\sum_ {j} (y _ {i j} \cdot b _ {j}) \geq \gamma \cdot t _ {i} \cdot x _ {i}
$$

$$
\forall j, \forall i > 0\tag{20}
$$

$$
t _ {i} \geq l _ {i} \cdot x _ {i}
$$

$$
\forall i\tag{21}
$$

$$
t _ {i} \leq u _ {i} \cdot x _ {i}
$$

$$
\forall i\tag{22}
$$

$$
x _ {0} = 0\tag{23}
$$

$$
t _ {i} \in \mathbb {N} _ {0}
$$

$$
\forall i\tag{24}
$$

$$
x _ {i}, y _ {i j} \in \{0, 1 \} \quad \forall j, \forall i > 0\tag{25}
$$

When the staff members are allocated to the stores in a manner that the customers’ aggregated distance to the stores is minimized, the FRC maximizes its revenue and profit (revenue and profit maximization coincide because we abstract away from store fix cost and the m staff members are just re-allocated). Hence, the objective function (17) aims at minimizing the sum of the purchasing distances between all serving stores and served customers. For modelling reasons, the customer food demands that cannot be satisfied $( B ^ { - } )$ are served by a dummy store $( i = 0 )$ . The dummy store does not employ any staff members. The constraint function (18) ensures that a number of ?? staff members are allocated to the “real” stores $( i > 0 )$ , while (19) guarantees that a customer is assigned to exactly one store. Due to the staff absence, it might be necessary to close stores or to run stores with a lower capacity of staff members. The constraint function (20) assumes that the throughput of each store $i >$ 0 realized by customers at least matches the throughput capacity given the staff members allocated to this store. The constraint functions (21) and (22) ensure that the allocated number of staff members in

# ACCEPTED MANUSCRIPT

a store is within the allowed range, (23) ensures that the dummy store is closed and not included in result evaluation. Constraints (24) and (25) define the feasible range of values of the decision variables.

Task 2 - Parameter classification and calibration: By assumption, planning information indicates the extent of the staff availability ??, which is provided by store managers early enough to flow into the decision-making process. Further PV refer to the maximum number of staff members $u _ { i }$ that are employed in a store $i \in I$ under normal operation, minimum number of staff members $l _ { i }$ that have to be employed in a store to open it, and throughput ?? [kg] achieved in any store by a staff member per day. The optimization model comprises one EV. It refers to the customer food demand $b _ { j } , \forall j \in J$ . As customers are affected by the pandemic disaster this specification is prone to uncertainty. The pandemic may cause shifts in customer food demands that exceed everyday fluctuations. It is imaginable that the customer food demands increase as healthy people raise their food stocks for several days to be prepared for an infection or that infected customers are not able to visit stores, lowering customer food demands. Base consumption behavior is potentially altered when a great part of the diseased customers stay at home, e.g. in the more lived-in districts instead of eating out.

To be prepared for the case that information from the environment is insufficient to specify the customer food demands deterministically in the case of a pandemic, a specification process is developed that allows describing different states of the customer food demand. The specification process is steered by a gamma distribution which has been proven as an appropriate statistical distribution to estimate food consumption data (Battese et al. 1988; Vilone et al. 2014). The density function of the gamma distribution is defined as (Bol 2003):

$$
f (x) = \left\{ \begin{array}{l l} \frac {\beta^ {\alpha}}{\Gamma (\alpha)} x ^ {\alpha - 1} e ^ {- \beta x} & \text { for } x > 0 \\ 0 & \text { for } x \leq 0 \end{array} \right.\tag{26}
$$

Let $\mu _ { c u s t }$ be the average food demand of a customer per day, $\sigma _ { c u s t }$ its standard deviation. Then, $\alpha = ( \mu _ { c u s t } ) ^ { 2 } / ( \sigma _ { c u s t } ) ^ { 2 } , \beta = \mu _ { c u s t } / ( \sigma _ { c u s t } ) ^ { 2 }$ , and $\Gamma ( \alpha )$ is the function value of the gamma function.

## 4.3 Two-stage scenario construction

Per assumption, a pandemic reaches Berlin. The BCM department of the FRC activates the Re-DRiSS methodology to develop a robust allocation of the available staff members to the stores for the scope of one day. The process can be repeated with updated information, for any number of days.

Task 3 - Prognostic scenarios: Planning information indicates that the FRC deploys ?? = 42 staff members at maximum and ?? = 26 at minimum in a consumer market and $u = 9 1$ and ?? = 55 in a selfservice warehouse, respectively. Thus, the total number of staff members during normal operations equals 1757. The average throughput per additional staff member in a store is $\gamma = 2 6 6 . 1$ kg/day and assumed to be equal in both types of stores. The store manager receives the information of a staff absence of 60%; thus, $m = 7 0 2$ staff members are available. Initially, there is no information from the environment arising ad-hoc that allows a deterministic specification of the customer food demands across the districts of Berlin. Combining the market share of the FRC of 10.6% and 2.04 million households in Berlin (SBB 2012), the number of households served by the FRC is 216,300. To reduce computational effort within the case study, an aggregation factor of 10:1 is used indicating that one customer represents ten households. It is assumed that one such customer makes purchases every day to satisfy his/her food demands. According to planning information obtained by the FRC, the values $\begin{array} { r } { \mu _ { c u s t } = 2 1 . 6 2 \frac { k g } { d } } \end{array}$ and $\begin{array} { r } { \sigma _ { c u s t } = 1 . 5 6 4 ~ \frac { k g } { d } } \end{array}$ are used to parametrize the gamma distribution (26) to randomly generate the customer food demand $b _ { j }$ of each $j \in \left\{ 1 , \dots , 2 1 , 6 3 0 \right\}$ . In combination with the constant specifications of the PV, 100 prognostic scenarios $S ^ { p r o g } = \left\{ s _ { 1 } ^ { p r o g } , \dots , s _ { 1 0 0 } ^ { p r o g } \right\}$ are constructed.

Task 4 – Generation of alternatives: Per prognostic scenario of the optimization model, a best alternative is computed. It is defined by the binary values of decision variable $x _ { i } , \forall i \in I _ { \mathit { i } }$ , which indicates whether a store is opened $( x _ { i } = 1 )$ or not $( x _ { i } = 0 )$ , and $t _ { i } , \forall i \in I$ which is the number of staff members allocated to the opened stores. The binary values of decision variable $y _ { i j } , \forall i \in I , \forall j \in J$ highlight whether $b _ { j }$ is served by store ?? $( y _ { i j } = 1 )$ or not $( y _ { i j } = 0 ) ; y _ { i j } , \forall i \in I , \forall j \in J$ is adaptable to the scenario-specific characteristics when testing an alternative in a different scenario for which it has not been generated for. Hence, an alternative is defined by the binary values of $x _ { i } , \forall i \in I$ and $t _ { i } , \forall i \in I$ In total, 100 optimization sub-models are formulated and solved. The result is the set $A =$ $\{ a _ { 1 } , \dots , a _ { 4 5 } \}$ which contains 45 heterogeneous alternatives. Across ??, 19 of 29 stores are always opened while 9 of 29 stores are always closed. Seven alternatives (group 1) suggest opening an additional store (store 9, district XI). This store is closed in the remaining 38 alternatives (group 2). Alternatives within the groups differ in the allocation of staff members to the opened stores 1, 2, 5, 9, 14, 15, 17, 18, 24, and 25, store 9 being opened in group 2 and closed in group 1. Both groups allocate the minimum number of staff members to the stores 6, 11, 13, 19, 20, 22, 23 and 26 and the maximum number to stores 8 and 29. Stores 3, 4, 7, 10, 12, 16, 21, 27 and 28 are closed. Figure 4 illustrates the obtained alternatives within the geographical representation of Berlin.

![](/api/attachments/MSB9RPB2/fulltext/images/b8fab0fdedfdbe3e0d92309e440c17f15655856cd84c1dfc02736c2186b694b3.jpg)  
Figure 4: Robust and variable allocation of staff members

Task 5 – Hypothetical scenarios: The objective of hypothetical scenarios is to explore the performance of alternatives when the pandemic causes extreme but still plausible developments of customer food demands. Therefore, (i) increased fluctuations and (ii) decreased and increased levels of average customer food demand per day are simulated. The possibility of decreased fluctuations is not considered in the case study. For (i) and (ii) 100 hypothetical scenarios each are constructed. The overall set of hypothetical scenarios is denoted $S ^ { h y p } = \left\{ S _ { ( i ) } ^ { h y p } , S _ { ( i i ) } ^ { h y p } \right\} = \left\{ s _ { 1 } ^ { h y p } , \ldots , s _ { 2 0 0 } ^ { h y p } \right\}$ . The subset $S _ { ( i ) } ^ { h y p } =$ $\left\{ s _ { 1 } ^ { h y p } , \ldots , s _ { 1 0 0 } ^ { h y p } \right\}$ explores increased fluctuations of customer food demands caused by the pandemic. To translate the increased fluctuations into the specifications of $b _ { j } , \forall j \in J , \sigma _ { c u s t } = 1 . 5 6 4$ is increased by 100%, 200%, 300%, 400%, and 900%; 20 hypothetical scenarios are constructed per modification factor. The subset $S _ { ( i i ) } ^ { h y p } = \big \{ s _ { 1 0 1 } ^ { h y p } , \dots , s _ { 2 0 0 } ^ { h y p } \big \}$ explores decreased and increased average food demand of customers. The expected customer food demand $\mu _ { c u s t } = 2 1 . 6 2 \mathrm { k g / d }$ is modified by defining a decrease of 50% and an increase of 50%, 100%, 200%, and 400%, for 20 scenarios each. Note that the standard deviation $\sigma _ { c u s t }$ increases in a similar manner, so that the coefficient of variation $c _ { v } = { \frac { \sigma _ { c u s t } } { \mu _ { c u s t } } }$ of customer food demand stays stable (see Table 3).

<table><tr><td>Hypothetical scenarios</td><td> $\{s_{1-20}^{hyp}\}$ </td><td> $\{s_{21-40}^{hyp}\}$ </td><td> $\{s_{41-60}^{hyp}\}$ </td><td> $\{s_{61-80}^{hyp}\}$ </td><td> $\{s_{81-100}^{hyp}\}$ </td><td> $\{s_{101-120}^{hyp}\}$ </td><td> $\{s_{121-140}^{hyp}\}$ </td><td> $\{s_{141-160}^{hyp}\}$ </td><td> $\{s_{161-180}^{hyp}\}$ </td><td> $\{s_{181-200}^{hyp}\}$ </td></tr><tr><td> $μ_{cust}$  [kg]</td><td>21.62</td><td>21.62</td><td>21.62</td><td>21.62</td><td>21.62</td><td>10.81</td><td>32.43</td><td>43.24</td><td>64.68</td><td>108.1</td></tr><tr><td> $σ_{cust}$  [kg]</td><td>3.13</td><td>4.69</td><td>6.26</td><td>7.82</td><td>15.63</td><td>0.78</td><td>2.34</td><td>3.13</td><td>4.69</td><td>7.82</td></tr><tr><td> $c_v$ </td><td>14.47</td><td>21.7</td><td>28.93</td><td>36.17</td><td>72.34</td><td>7.23</td><td>7.23</td><td>7.23</td><td>7.23</td><td>7.23</td></tr><tr><td>Minimum Demand [kg]</td><td>8.7</td><td>6.3</td><td>4</td><td>2.1</td><td>0.1</td><td>7.5</td><td>22.1</td><td>29.9</td><td>45.7</td><td>72.6</td></tr><tr><td>Minimum Demand [kg]</td><td>39.3</td><td>49.2</td><td>61.6</td><td>81.5</td><td>170.9</td><td>14.9</td><td>43.8</td><td>60.9</td><td>92.5</td><td>147.3</td></tr></table>

Table 3: Data for the construction of hypothetical scenarios (i) and (ii)

## 4.4 Robustness measurement

Task 6 - Regret test: Robustness measurement of alternatives must respond to the following questions: (1) Should store 9 be opened (group 2) or closed (group 1)? (2) What is the most robust allocation of staff members to the stores 1, 2, 5, (9), 14, 15, 17, 18, 24, and 25? Therefore, each alternative $a _ { b } \in$ ?? is tested in each prognostic scenario $s _ { l } ^ { p r o g } \in S ^ { p r o g }$ and in each hypothetical scenario $s _ { k } ^ { h y p } \in S ^ { h y p }$ As the underlying optimization model refers to a single-objective minimization problem, the normalized regret of $a _ { b }$ in a scenario $s \in S ^ { p r o g } , S ^ { h y p }$ is calculated using a linear value function:

# ACCEPTED MANUSCRIPT

$$
r (a _ {b}, s) = \frac {z (a _ {b} , s) - z ^ {m i n} (A , s)}{z ^ {m a x} (A , s) - z ^ {m i n} (A , s)}\tag{27}
$$

where $\mathbf { \Theta } _ { Z } ( a _ { b } , s )$ is the objective function value when $a _ { b }$ is tested in the ??-specific optimization submodel, and $z ^ { m i n } ( A , s )$ and $z ^ { m a x } ( A , s )$ are the minimal (best) and maximal (worst) objective function values that can be achieved by any other alternative of ?? in this sub-model. The result is $\mathrm { ~ a ~ } 4 5 \times$ (100 + 200) matrix of normalized regret values. Based on this matrix, the expected normalized regret $R E ( a _ { b } , S ^ { p r o g } )$ and $R E ( a _ { b } , S ^ { h y p } )$ and the maximal aggregated regret $R M ( a _ { b } , S ^ { p r o g } )$ and $R M ( a _ { b } , S ^ { h y p } )$ are calculated per $a _ { b } \in A$ (see Table 4).

Task 7 - Integration of risk preferences: According to preference-related information provided by the FRC, we apply the following degrees of pessimism: $w e ^ { p r o g } = 0 . 3 , w e ^ { h y p } = 0 . 7 ; \lambda ^ { p r o g } =$ $0 . 7 , \lambda ^ { h y p } = 0 . 3 , \mathrm { s e e }$ (28). We select these values since the alternatives of set ?? are very stable. In fact, group 1 and group 2 just differ in one additionally opened st differences of the alternatives of each group are small. Thus, the FRC aims at primar g robustness based on the hypothetical scenarios to explore the effect of large-scale shifts within the customer food demand. This is reflected by the inter-scenario degree of pessimism of ?? ${ \gtrsim } ^ { p r o g } = 0 . 3$ and $w e ^ { h y p } = 0 . 7$ . The FRC prioritizes robustness of alternatives within prognostic scenarios using the expected normalized regret $( \lambda ^ { p r o g } = 0 . 7 )$ ) over hypothetical scenarios using the maximal normalized regret $( \lambda ^ { h y p } = 0 . 3 )$ .

$$
\begin{array}{c} R V (a _ {b}) = 0. 3 \cdot \left(0. 7 \cdot R E (a _ {b}, S ^ {p r o g}) + 0. 3 \cdot R M (a _ {b}, S ^ {p r o g})\right) + 0. 7 \\ \cdot \left(0. 3 \cdot R E (a _ {b}, S ^ {h y p}) + 0. 7 \cdot R M (a _ {b}, S ^ {h y p})\right) \end{array}\tag{28}
$$

The five best ranked alternatives of the obtained robustness ranking are shown in Table 4. It becomes obvious that differences in the robustness values of alternatives are small, particularly between alternatives of the same group. This is because they only differ in the allocation of few staff members. However, differences between group 1 and group 2 are significant: the three best ranked alternatives refer to group 2, suggesting opening store 9. This is confirmed by exploring the average robustness

# ACCEPTED MANUSCRIPT

value of all alternatives of group 1 (0.659) and group 2 (0.607). As alternatives of group 2 prescribe allocating the minimum number of 55 staff members to store 9, this amount must be sourced from other opened stores. This causes a decrease in the achievable throughputs of these stores. The most notable decrease of allocated staff members (compared to alternatives of group 1) refers to store 2 (- 12) and to store 24 (-14). Hence, decision support recommends implementing an alternative of group 2 (question 1) and opening store 9. Although, according to the alternatives of group 2, the exact allocation of staff members to the stores just varies slightly, a final decision must be made. Therefore, the allocation as specified by $a _ { 4 }$ is suggested as it achieves the highest robustness value (question 2).

<table><tr><td>Alternatives</td><td> $RE(a, S^{prog})$ </td><td> $RM(a, S^{prog})$ </td><td> $RE(a, S^{hyp})$ </td><td> $RM(a, S^{hyp})$ </td><td> $RV(a)$ </td></tr><tr><td> $a_4$ (group 2)</td><td>0.100</td><td>0.535</td><td>0.253</td><td>0.890</td><td>0.558</td></tr><tr><td> $a_{31}$ (group 2)</td><td>0.104</td><td>0.551</td><td>0.305</td><td>0.885</td><td>0.569</td></tr><tr><td> $a_{12}$ (group 2)</td><td>0.106</td><td>0.579</td><td>0.286</td><td>0.894</td><td>0.572</td></tr><tr><td> $a_{20}$ (group 1)</td><td>0.128</td><td>0.692</td><td>0.377</td><td>0.834</td><td>0.577</td></tr><tr><td> $a_{33}$ (group 1)</td><td>0.124</td><td>0.623</td><td>0.356</td><td>0.866</td><td>0.581</td></tr></table>

Table 4: Robustness ranking of alternatives

During our research, we interviewed managers of different FRC. They warded off the need for any continuity plans since disruptive events are highly unlikely from their point of view. Some mentioned the government’s responsibility to step in the case that the population is affected and, thus, failed to understand where BCM ends and disaster management starts. Others stated that they perceived their company’s flexibility and their own ability to spontaneously manage new situations sufficiently. It became evident that practitioners seem to be insufficiently prepared to face threats to their critical SC. As neither foresight nor planning were present regarding severe disruptive events, the presented approach can hence be considered as an improvement compared to existing solutions.

## 5. Discussion and conclusion

Organizations are increasingly affected by large-scale disasters and the need for coherent BCM measures and business continuity plans is high. To address this highly relevant issue, the focus of this

# ACCEPTED MANUSCRIPT

article is on a decision support methodology to be used within the BCM of organizations in managing disaster-caused critical SC disturbances. The ReDRiSS methodology allows for robust and flexible solutions of a wide range of logistical decision problems during the reaction phase of a disruption. It is, thus, an innovative measure of disaster risk reduction within organizations. To ensure its application in the post-disaster phase, efforts of preventive SCRM are required in the pre-disaster phase. This puts pressure on decision makers to analyze potential future scenarios, to anticipate logistical crisis strategies and to prepare for action. Anecdotic evidence abounds that in the acute phase of a disaster there is no scope for systematic crisis management. The threat of mismanaging the consequences of a disaster in its aftermath is mitigated if a tool is available to aid decision makers of SCCM analytically.

Our decision support methodology uses a two-stage scenario-based optimization approach. We guarantee that each scenario directly affects the results of the decision problem as it explicitly defines consequences in the environment rather than exploring the characteristics of the triggering event. For example, during an earthquake, the state of roads might be a crucial parameter as part of a scenario. Prognostic scenarios might focus on road disruptions close to vulnerable areas (e.g. cities). Hypothetical scenarios might consider disruptions of secondary roads (e.g. at the coast) and might exactly describe the consequences of a tsunami affecting the earthquake area in its aftermath. When a tsunami has not hit the area ever before, it could be understood as a “black swan” (Taleb 2004). Within the realm of probability theory, such events can be described by (extremely) left-skewed probability distributions and for interdependent (i.e. cascading) events of this type by the use of copula. However, our methodology is less optimistic about the availability of statistical distributions when it comes to hypothetical scenarios. In fact, the applied Hodge-Lehmann decision rule corresponds to a so-called ‘simple capacity‘. Capacities are subjective, non-additive probabilities which allow for a consideration of the decision maker’s subjective degree of confidence in the knowledge about event frequencies (Eichberger & Kelsey, 1999). This theory is part of the Fuzzy Measure Theory (Wang & Klir, 1992). An interesting alternative to this approach is the use of fuzzy numbers and to combine the fuzzy model with a real-option approach (Muzzioli & De Baets, 2017; Collan et al., 2003). Such an approach offers even more flexibility to the decision maker and could reduce the number of candidate scenarios significantly. However, this comes at the expense of an increased model complexity so that we see it as a promising model extension which goes beyond the scope of this contribution. After all, the set-up of hypothetical scenarios will always depend on some type of prior experience about very rare events,

The objective of a DSS in general is never the replacement of the decision makers who will always remain the responsible actors who deal with a decision and put it into practice. It is ensured within our analytical methodology that the decision makers are recurrently involved in the decision-making process. Their preferences are considered when developing the optimization model and solving the scenario-specific parametrizations of the optimization model. Furthermore, they participate in setting up the (re)-specification processes (scenario construction) and their degree of pessimism is integrated in robustness measurement of alternatives. This constant involvement and the resulting transparency are important prerequisites for the decision makers’ trust into the analytical methodology.

Robustness measurement explicitly reflects its ability to achieve a better outcome than the other generated alternatives. Our approach does not allow any statement concerning the achieved “absolute” robustness of an alternative, but explicitly highlights the “relative” robustness regarding the constructed sets of scenarios. It is, however, not ensured that these sets include the state of the disasteraffected decision environment that meets its real conditions. Our approach just guarantees that a sound procedure constructs scenarios to identify states that might be critical for decision-making. Hence, it cannot be excluded that the robust decision recommendation hedges against false states of the decision environment or that in retrospect further, better alternatives exist.

The quality of a decision can just be assessed in retrospect. This is especially true in the context of disaster management where the sum of all disaster-caused consequences characterizing the environment do not typically become obvious before the situation has evolved. Therefore, future research

# ACCEPTED MANUSCRIPT

should focus on further validations of the ReDRiSS methodology in terms further case studies and, in particular, practical field tests. This is important to reveal and eradicate drawbacks of the analytical methodology and to analyze the behavior of the decision makers when dealing with the system under time pressure. Case studies should re-simulate real world decision situations ex post to compare the decision made (and its consequences) and the decision that would have been recommended.

Before using the system, a preventive implementation of ReDRiSS ensures that basic components such as the optimization model, the solution algorithm and specification processes to construct scenarios are set up prior to a disaster. However, time pressure remains a crucial factor within its application. Information arising from the environment in the immediate aftermath of a disaster that provides insights about the conditions of the decision environment might be, if it is available, vague or cryptic in its format. It might be necessary to translate this information into an appropriate format and this might be time-consuming. We have assumed that the reliability of all information is guaranteed. This is a strong assumption in a real-world application and requires that upstream processes of information gathering are functional. Therefore, an essential task of future research should focus on information and communication technology (ICT) systems as well as their coupling with the methodology of ReDRiSS.

## Acknowledgements

We would like to thank the German Federal Ministry of Education and Research (BMBF) for financial support for this work within the research project SEAK.

## Literature

Altay, N. & Green, W.G., 2006. OR/MS research in disaster operations management. European Journal of Operational Research, 175(1), pp.475–493.

Ambs, K., Cwilich, S., Deng, M., Houck, D.J., Lynch, D.F., Yan, D., 2000. Optimizing Restoration Capacity in the AT&T Network. Interfaces 30 (1): pp. 26-44.

Artalejo, J. R., Gomez-Corral, A., 1999. Performance Analysis of a Single-Server Queue with Repeated Attempts. Mathematical and Computer Modelling 30: pp. 79-88.

Arnott, D., & Pervan, G. 2008. Eight key issues for the decision support systems discipline. Decision Support Systems 44, pp. 657–67.

Battese, G.E., Nusser, S.M. & Fuller, W.A., 1988. Estimation of the Distribution of Usual Intakes for Selected Dietary Components, Center for Agricultural and Rural Development, Iowa State University. BCI. 2013. A Guide to Global Good Practice in Business Continuity.

Bertsimas, D., Sim, M., 2004. The Price of Robustness. Operations Research, 52(1), pp.35–53.

Boerse, J.-H., 2014. Unternehmen durch die Krise führen. Business Continuity Management im Härtetest einer Pandemie, Hamburg: Diplomica Verlag.

Bunn, D. W., Salo, A.A., 1993. Forecasting with scenarios. European Journal of Operational Research, 68(3), pp.291–303.

Bryson, K.-M., Millar, H., Joseph, A. & Mobolurin, A., 2002. Using formal MS/OR modeling to support disaster recovery planning. European Journal of Operational Research, 141(3), pp.679–688.

Collan, M.; Carlsson, C. & Majlender, P., 2003. Fuzzy Black and Scholes Real Options Pricing, Journal of Decision Systems, 12:3-4, 391-416.

Comes, T., 2011. Decision Maps for Distributed Scenario-Based Multi-Criteria Decision Support, KIT Scientific Publishing.

Day, J., Melnyk, S., Larson, P., Whybark, D., Davis, E.W., 2012. Humanitarian and Disaster Relief Supply Chains: A Matter of Life and Death. Journal of Supply Chain Management, 48(2): pp. 21-36.

De la Torre, L.E., Dolinskaya, I.S. & Smilowitz, K.R., 2012. Disaster relief routing: Integrating research and practice. Socio-Economic Planning Sciences, 46(1), pp.88–97.

Eichberger, J. & Kelsey, D., 1999. E-Capacities and the Ellsberg Paradox, Theory and Decision, 46, 107-140.

Ellsberg, D., 1961. Risk, Ambiguity, and the Savage Axioms, Quarterly Journal of Economics, Nr. 75, pp. 643-669.

Er, M.C. 1988. Decision Support Systems: A summary, problems, and future trends. Decision Support Systems, 4(3): pp. 355–363.

Gabrel, V., Murat, C., 2010. Robustness and duality in linear programming. Journal of the Operational Research Society (61), pp. 1288 -1296.

Galindo, G. & Batta, R., 2013. Review of recent developments in OR/MS research in disaster operations management. European Journal of Operational Research, 230(2), pp.201–211.

Gilboa, I. & Schmeidler, D., 1989. Maxmin Expected Utility with a Non-Unique Prior, Journal of Mathematical Economics, No. 18, pp. 141-153.

Grisogono, A.-M., 2006. Implications of Complex Adaptive Systems Theory for C2. Command and Control Research and Technology Symposium, pp.1–19.

Guha-Sapir, D., P. Hoyois, R. Below, 2016. Annual disaster statistical review 2015: the numbers and trends, Centre for Research on the Epidemiology of Disasters (CRED).

Helbing, D. & Lämmer, S., 2008. Managing Complexity: An Introduction. In D. Helbing, ed. Managing Complexity: Insights, Concepts, Applications. Springer Berlin Heidelberg, pp. 1–16.

Hites, R., De Smet, Y., Risse, N., Salazar-Neumann, M., Vincke, P., 2006. About the applicability of MCDA to some robustness problems. European Journal of Operational Research, 174(1), pp. 322-332.

Hollnagel, E. 2012. Coping with complexity: past, present and future. Cognition, Technology and Work, 14 (3): pp.199–205.

Holsapple, C.W., 2008. Decisions and Knowledge. In F. Burstein & C. W. Holsapple, eds. Handbook on Decision Support Systems 1. Springer Berlin Heidelberg, pp. 21–53.

Hoyos, M., Morales, R., Akhavan-Tabatabaei, R., 2015. OR models with stochastic components in disaster operations management: A literature survey. Computers & Ind. Engineering, 82, pp.183-197.

Kleindorfer, P.R. & Saad, G.H., 2005. Managing Disruption Risks in Supply Chains. Production and Operations Management, 14(1), pp.53–68.

Knemeyer, A.M., Zinn, W. & Eroglu, C., 2009. Proactive planning for catastrophic events in supply chains. Journal of Operations Management, 27(2), pp. 141–153.

Knight, F.H., 1921. Risk, Uncertainty, and Profit, Boston: Houghton Mifflin Co.

Kotzab, H. & Teller, C., 2005. Development and empirical test of a grocery retail instore logistics model. British Food Journal, 107(8), pp.594–605.

Kovács, G. & Tatham, P., 2009. Responding To Disruptions in the Supply Network - From Dormant To Action. Journal of Business Logistics, 30(2), pp.215–229.

Lauwe, P., 2007. Innerbetriebliches Risiko- und Krisenmanagement. Notfallvorsorge (04), pp.14–15.

Liberatore, F., Pizarro, C., Simón de Blas, C., Ortuno, M.T. & Vitariano, B., 2013. Uncertainty in Humanitarian Logistics for Disaster Management. A Review. In B. Vitoriano, J. Montero, & D. Ruan, eds. Decision Aid Models for Disaster Management and Emergencies. Atlantis Press, pp. 45–74.

Mattiussi, A. 2012. Decision support systems for sustainable plant design. University of Udine.

Muzzioli, S. & De Baets, B. (2017): „Fuzzy Approaches to Option Price Modeling“, IEEE Transactions on Fuzzy Systems, 25:2, 392-401.

Natarajarathinam, M., Caspar, I. & Narayanan, A., 2009. Managing supply chains in times of crisis: a review of literature and insights. International Journal of Physical Distribution & Logistics Management, 39(7), pp.535–573.

Peck, H., 2006. Resilience in the food chain: a study of business continuity management in the food and drink industry.

Rommelfanger, H. & Eickemeier, S., 2002. Entscheidungstheorie, Heidelberg, Berlin: Springer.

Sahebjamnia, N., Torabi, S.A. & Mansouri, S.A., 2015. Integrated business continuity and disaster recovery planning: Towards organizational resilience. EJOR, 242(1), pp.261–273.

Samii, R. & Van Wassenhove, L., 2010. The Logistics of Emergency Response: Tsunami versus Haiti, INSEAD, Social Innovation Centre.

Schätter, F., Wiens, M. & Schultmann, F., 2015. A new focus on risk reduction: An ad-hoc decision support system for humanitarian relief logistics. Ecosystem Health and Sustainability, 1(3), pp.1–11.

SBB, 2012. Statistischer Bericht - Ergebnisse des Mikrozensus im Land Berlin 2012. Amt für Statistik Berlin-Brandenburg, p.56.

Scholl, A., 2001. Robuste Planung und Optimierung, Physica-Verlag Heidelberg.

Shim, J.P., M. Warkentin, J. F. Courtney, D. J. Power, R. Sharda, C. Carlsson. 2002. Past, present, and future of decision support technology. Decision Support Systems, 33 (2): pp.111–126.

Snowden, D., Boone, M.W., 2007. A Leader’s Framework for Decision-making. Harvard Business Review, 85: pp.67–76.

Snyder, L.V. 2006. Facility location under uncertainty: A review. IIE Transactions, 38(7), pp.537-554.

Sojda, R.S., 2007. Empirical evaluation of decision support systems: needs, definitions, potential methods, and an example pertaining to waterfowl management. Environmental Modelling & Software, 22(2): pp. 269–277.

Taleb, N.N., 2004: Bleed or Blowup? Why Do We Prefer Asymmetric Payoffs?, The Journal of Behavioral Finance, 5:1, 2-7.

Thompson, S., Altay, N., Green, III, W.G., Lapetina, J., 2006. Improving disaster response efforts with decision support systems’, International Journal of Emergency Management, 3(4): pp. 250–263.

The White House, 2006. The federal response to hurricane Katrina: lessons learned.

Vahidov, R. & Kersten, G.E., 2004. Decision station: situation decision support systems. Decision Support Systems, 38(2), pp.283–303.

Van Wassenhove, L. 2006. Humanitarian aid logistics: supply chain management in high gear. Journal of the Operational Research Society, 57(5), pp.475–489.

Van Wassenhove, L., 2012. Humanitarian Logistics and Supply Chain Management. In A. Cozzolino, ed. Humanitarian Logistics. SpringerBriefs in Business, pp. 5–16.

Vilone, G., Comiskey, D., Heraud, F. & O'Mahony, C., 2014. Statistical method to assess usual dietary intakes in the European population. Food Additives and Contaminants: Part A Chemistry, Analysis, Control, Exposure and Risk Assessment, 31(10), pp.1639–1651.

Von Rössing, R., 2005. Betriebliches Kontinuitätsmanagement, Bonn: Mitp-Verlag.

Wallace, W. A., F. De Balogh. 1985. Decision Support Systems for Disaster Management. Public Administration Review 45: pp. 134-146.

Wang, Z. & Klir, G.J., 1992. Fuzzy Measure Theory, New York: Plenum Press.

Wiens, M., 2013. Vertrauen in der ökonomischen Theorie: Eine mikrofundierte und verhaltensbezogene Analyse F. L. Sell, ed., Berlin: Lit Verlag.

Zimmermann, H.J., 2000. An application-oriented view of modeling uncertainty. European Journal of Operational Research, 122(2), pp.190–198.

Zitzler, E., 1999. Evolutionary Algorithms for Multiobjective Optimization: Methods and Applications, ETH Zürich.

Zsidisin, G.A., Melnyk, S.A. & Ragatz, G.L., 2005. An institutional theory perspective of business continuity planning for purchasing and supply management. International Journal of Production Research, 43(16), pp.3401–3420.

# ACCEPTED MANUSCRIPT

Frank Schätter holds Ph.D. in Business Engineering and is a lecturer at the Institute of Industrial Production (IIP) at the Karlsruhe Institute of Technology (KIT), Germany. He finished his Ph.D. in 2016 where he focused on decision-making in supply chain risk management. His major research interest is on model-based approaches from operations research and management sciences to solve logistical decision problems in uncertain and dynamically changing decision situations.

Ole Hansen is a PhD Candidate in the field of Logistics at Kühne Logistics University. He holds a diploma in Economics with a focus on International Economics and Supply Chain Management from the University of Kiel. Following his studies, he worked as a researcher and consultant for a logistics services company for over four years. His research interests are the engagement of companies in disaster management and inventory management of food supply chain s.

Marcus Wiens holds Ph.D. in Economics and leads the research unit in risk management at the Institute of Industrial Production at Karlsruhe Institute of Technology (KIT). His fields of research are economic systems analysis, behavioral risk management, decision theory, game theory, and experimental economics. Marcus Wiens is an adjunct professor at the International School of Management (ISM), member of the German Operation Research Society, and member of the Center for Disaster Management and Risk Reduction Technology (CEDIM), which is an interdisciplinary research center founded by the Helmholtz Association.

Frank Schultmann is Chair Professor at the Karlsruhe Institute of Technology (KIT), Germany, and the Director of the KIT’s Institute for Industrial Production (IIP) and the French-German for Environmental Research (DFIU). He is also Director of Project Management at the University of Adelaide. His research interests include sustainable production and logistics, decision support, supply chain management and optimization, systems modeling, project management, technology assessment, construction management, and information and communication technologies.

Highlights of the submission “A decision support methodology for a disaster-caused business continuity management”

\- When securing critical supplies, companies take over public responsibility

\- Decision tools for disaster-caused business continuity management are lacking

\- During disasters, companies must manage highly uncertain and complex situations

\- Logistical decision support must be analytically precise but comprehensible

\- Scenarios can help to explore critical consequences in the disaster environment

Risk preference dependent robustness measurement of decision alternatives
